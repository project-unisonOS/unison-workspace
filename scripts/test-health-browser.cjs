const path=require('path'), fs=require('fs');
const modules=process.env.UNISON_BROWSER_MODULES || path.join(process.env.HEALTH_RENDERER_ROOT,'node_modules');
const {chromium}=require(path.join(modules,'playwright'));
const AxeBuilder=require(path.join(modules,'@axe-core/playwright')).default;
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.UNISON_BROWSER_CHANNEL?{channel:process.env.UNISON_BROWSER_CHANNEL}:{})});
 const qa=process.env.HEALTH_TEST_QA;fs.mkdirSync(qa,{recursive:true}); const results=[];
 try {
  for(const width of [320,1280]) for(const forcedColors of ["none","active"]) {
   const context=await browser.newContext({viewport:{width,height:1000},forcedColors});
   await context.addInitScript(token=>sessionStorage.setItem('unisonAccessToken',token),process.env.HEALTH_TEST_TOKEN);
   const page=await context.newPage();
   await page.goto(process.env.HEALTH_TEST_URL+'/static/health-export.html');
   async function audit(state){ await page.screenshot({path:path.join(qa,`audit-${width}-${forcedColors}-${state}.png`),fullPage:true});
    const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();
    if(result.violations.length)throw Error(JSON.stringify(result.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))}))));
    if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('horizontal overflow');
    results.push({width,forcedColors,state,axeViolations:0});
   }
   await audit('initial');
   for(const mode of ['revoke','delete']) {
    await page.locator('#export-file').setInputFiles(process.env.HEALTH_TEST_SAMPLE);
    // Selecting a file alone is not consent and does not upload.
    await page.locator('#import').click();
    await page.getByRole('status').filter({hasText:'permit its use'}).waitFor();
    await page.locator('#consent').focus();await page.keyboard.press('Space');
    await page.locator('#import').focus();await page.keyboard.press('Enter');
    await page.locator('#review').waitFor({state:'visible'});
    if(await page.locator('#facts article').count()!==2)throw Error('expected two source facts');
    await page.locator('#facts details summary').first().click();
    if(!(await page.locator('#facts').textContent()).includes('/observations/0'))throw Error('missing provenance');
    await page.locator('#summarize').focus();await page.keyboard.press('Enter');
    await page.locator('#summary').waitFor({state:'visible'});
    const summary=await page.locator('#summary-text').textContent();
    if(!summary.includes('420 minutes')||!summary.includes('unknown; Device not worn'))throw Error('incorrect deterministic summary');
    const link=page.locator('#summary-text a').first();await link.click();
    if(!page.url().includes('#fact-'))throw Error('source link failed');
    await audit('summary-'+mode);
    await page.screenshot({path:path.join(qa,`summary-${width}-${forcedColors}-${mode}.png`),fullPage:true});
    await page.locator('#backup').click();await page.getByRole('status').filter({hasText:'backup saved'}).waitFor();
    const old=fs.readFileSync(process.env.HEALTH_TEST_DATA_PATH);
    await page.locator('#'+mode).click();await page.getByRole('status').filter({hasText:'Current facts and saved snapshots removed'}).waitFor();
    // Restore actual old encrypted data, retaining separate current authority.
    fs.writeFileSync(process.env.HEALTH_TEST_DATA_PATH,old);
    await page.locator('#restore').click();await page.getByRole('status').filter({hasText:'remains unavailable'}).waitFor();
    if(await page.locator('#facts article').count()!==0||await page.locator('#summary').isVisible())throw Error('revoked facts resurfaced');
    await audit('restored-'+mode);
   }
   await page.evaluate(()=>document.documentElement.style.fontSize='200%'); await audit('text-200');
   await context.close();
  }
  fs.writeFileSync(path.join(qa,'results.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results));
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exit(1);});


