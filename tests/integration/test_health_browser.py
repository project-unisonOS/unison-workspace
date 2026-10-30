"""Actual browser -> renderer -> authenticated storage; synthetic, in-process upstream."""
import importlib.util
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import threading
import time

import httpx
import pytest
import uvicorn
from conftest import STORAGE

sys.path.insert(0, str(STORAGE / 'tests'))
from test_storage_authority import boundary  # noqa: E402,F401
from health_workflow import initialize_authority  # noqa: E402

RENDERER = Path(os.getenv('UNISON_TEST_RENDERER_ROOT', str(Path(__file__).resolve().parents[2]/'unison-experience-renderer'))).resolve()


def test_browser_health_workflow(boundary, monkeypatch, tmp_path):
    module, vault, headers, revoked = boundary
    if not shutil.which('node'):
        pytest.fail('Node is required for the browser acceptance journey')
    key = os.environ['STORAGE_OBJECT_ENC_KEY'].encode()
    root, ledger = tmp_path/'workflow', tmp_path/'authority'/'ledger.sqlite3'
    initialize_authority(ledger, key)
    monkeypatch.setenv('UNISON_SYNTHETIC_HEALTH_WORKFLOW','true')
    monkeypatch.setenv('UNISON_HEALTH_WORKFLOW_ROOT',str(root))
    monkeypatch.setenv('UNISON_HEALTH_AUTHORITY_PATH',str(ledger))
    monkeypatch.setenv('UNISON_HEALTH_WORKFLOW_STORAGE_URL','http://127.0.0.1:19080')
    monkeypatch.delenv('DISABLE_AUTH_FOR_TESTS',raising=False)
    sys.path.insert(0,str(RENDERER/'src'))
    spec=importlib.util.spec_from_file_location('health_experience_renderer',RENDERER/'src/main.py')
    renderer=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    calls=[]
    def transport(request):
        calls.append((request.method,request.url.path))
        response=vault.request(request.method,request.url.raw_path.decode(),headers=dict(request.headers),content=request.content)
        return httpx.Response(response.status_code,content=response.content,headers=dict(response.headers))
    renderer.app.state.health_workflow_transport=httpx.MockTransport(transport)
    sock=socket.socket(); sock.bind(('127.0.0.1',0)); port=sock.getsockname()[1]
    server=uvicorn.Server(uvicorn.Config(renderer.app,host='127.0.0.1',port=port,lifespan='off',log_level='error'))
    worker=threading.Thread(target=server.run,kwargs={'sockets':[sock]},daemon=True); worker.start()
    try:
        for _ in range(100):
            if server.started: break
            time.sleep(.05)
        assert server.started
        scopes=['storage.health.workflow.'+s for s in ('consent','import','read','delete','backup','restore')]
        token=headers(scopes=scopes,aud=['renderer','storage'])['Authorization'].split(' ',1)[1]
        env={**os.environ,'HEALTH_TEST_URL':f'http://127.0.0.1:{port}','HEALTH_TEST_TOKEN':token,
             'HEALTH_TEST_DATA_PATH':str(root/'workflow.sqlite3'),'HEALTH_TEST_SAMPLE':str(RENDERER/'src/web/health-sample.json'),
             'HEALTH_TEST_QA':str(tmp_path/'browser-evidence'),'HEALTH_RENDERER_ROOT':str(RENDERER)}
        script=Path(__file__).resolve().parents[2]/'scripts/test-health-browser.cjs'
        result=subprocess.run(['node',str(script)],env=env,text=True,capture_output=True,timeout=150)
        if os.getenv('UNISON_BROWSER_EVIDENCE'): shutil.copytree(tmp_path/'browser-evidence',os.environ['UNISON_BROWSER_EVIDENCE'],dirs_exist_ok=True)
        assert result.returncode==0, result.stdout+'\n'+result.stderr
        assert ('POST','/v1/health-workflows') in calls
        uploads=[i for i,(_,path) in enumerate(calls) if path.endswith('/upload')]
        assert all(any(p=='/v1/health-workflows' for _,p in calls[:i]) for i in uploads)
        # Keep optional evidence outside temporary state for local visual inspection.
        evidence=os.getenv('UNISON_BROWSER_EVIDENCE')
        if evidence: shutil.copytree(tmp_path/'browser-evidence',evidence,dirs_exist_ok=True)
    finally:
        server.should_exit=True; worker.join(timeout=10); sock.close()

