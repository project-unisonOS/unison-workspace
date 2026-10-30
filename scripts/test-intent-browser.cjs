const path=require('path'),fs=require('fs');
const modules=process.env.UNISON_BROWSER_MODULES||path.join(process.env.HEALTH_RENDERER_ROOT,'node_modules');
const {chromium}=require(path.join(modules,'playwright'));const AxeBuilder=require(path.join(modules,'@axe-core/playwright')).default;
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.UNISON_BROWSER_CHANNEL?{channel:process.env.UNISON_BROWSER_CHANNEL}:{})});
 const evidence=process.env.HEALTH_TEST_QA;fs.mkdirSync(evidence,{recursive:true});const results=[];
 try{for(const width of [320,1280])for(const mode of ['visual','screenless']){
  const context=await browser.newContext({viewport:{width,height:1000},forcedColors:width===320?'active':'none'});
  await context.addInitScript(token=>sessionStorage.setItem('unisonAccessToken',token),process.env.HEALTH_TEST_TOKEN);
  const page=await context.newPage();await page.goto(process.env.HEALTH_TEST_URL+'/static/intent-experience.html');
  await page.locator('#mode').selectOption(mode);
  async function state(value){await page.locator('#status').filter({hasText:'Current intent state: '+value}).waitFor();}
  async function choose(choice){if(mode==='visual'){await page.locator('#choices').getByRole('button',{name:choice.replaceAll('_',' '),exact:true}).click();}else{await page.locator('#command').fill(choice.replaceAll('_',' '));await page.locator('#command').press('Enter');}}
  let entered,release;const waiting=new Promise(resolve=>entered=resolve),gate=new Promise(resolve=>release=resolve);
  await page.route('**/synthetic-intent',async route=>{entered();await gate;await route.continue();},{times:1});let first=true;
  for(const mechanism of ['oauth','session','vault']){
   await page.locator('#mechanism').selectOption(mechanism);await page.locator('#start').click();
   if(first){await waiting;for(const id of ['start','send','refresh','mode','mechanism'])if(!await page.locator('#'+id).isDisabled())throw Error('pending control enabled: '+id);release();first=false;}
   await page.locator('#status').filter({hasText:/Current intent state: (proposed|waiting_repair|verified)/}).waitFor();
   if((await page.locator('#status').textContent()).endsWith('proposed')){
    if(!(await page.locator('#spoken').textContent()).includes('Delegation duration:'))throw Error('duration not presented');
    await choose('confirm');await page.locator('#status').filter({hasText:/Current intent state: (waiting_repair|verified)/}).waitFor();
   }
   if((await page.locator('#status').textContent()).endsWith('waiting_repair')){await choose('repair');await state('repair_confirmation');await choose('verify');}
   await state('verified');await page.reload();await state('verified');
   if(await page.locator('#mode').inputValue()!==mode)throw Error('mode preference lost on restart');
   await choose('delete');await state('deleted');
  }
  await page.locator('#mode').selectOption('screenless');await page.locator('#mechanism').selectOption('device-only');await page.locator('#start').click();await page.locator('#status').filter({hasText:/Current intent state: (proposed|waiting_repair)/}).waitFor();
  if((await page.locator('#status').textContent()).endsWith('proposed')){await page.locator('#command').fill('confirm');await page.locator('#send').click();}await state('waiting_repair');
  if(!(await page.locator('#spoken').textContent()).includes('no nonvisual alternative'))throw Error('unsupported challenge not disclosed');
  await page.locator('#command').fill('not now');await page.locator('#send').click();await state('paused');
  await page.locator('#mode').selectOption('visual');await state('paused');
  await page.evaluate(()=>document.documentElement.style.fontSize='200%');
  const audit=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();
  if(audit.violations.length)throw Error(JSON.stringify(audit.violations));
  if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('overflow');
  if((await page.locator('main').textContent()).toLowerCase().includes('browser'))throw Error('transport concept exposed');
  await page.screenshot({path:path.join(evidence,`intent-${width}-${mode}.png`),fullPage:true});results.push({width,mode,axeViolations:0});await context.close();
 }fs.writeFileSync(path.join(evidence,'intent-results.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results));
 }finally{await browser.close();}})().catch(error=>{console.error(error);process.exit(1);});
