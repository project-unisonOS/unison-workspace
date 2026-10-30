"""Synthetic library integration with encrypted disk state; no live auth or speech."""
import hashlib
import json
from cryptography.fernet import Fernet
import pytest
from conftest import STORAGE, ORCHESTRATOR  # noqa: F401
from encrypted_state import EncryptedState
from source_workflow import SourceWorkflow, initialize_authority
from orchestrator.synthetic_delegation import DelegationEngine, MockCredentialAdapter, initial_state, visual_document
from unison_common.principal import PrincipalContext


def person(name='alice'):
    return PrincipalContext(principal_id=name,principal_kind='person',person_id=name,
        assistant_instance_id='synthetic-assistant',household_id='synthetic-home',membership_id='synthetic-member',
        key_handle='synthetic-key',credential_namespace=name,data_namespace=name,cache_namespace=name,index_namespace=name,
        auth_method='synthetic-fixture',assurance='high',token_id='synthetic-id',issued_at=1,expires_at=10000,
        audience=('orchestrator',),scopes=('delegation.manage','delegation.read','delegation.execute'))


def test_source_connection_multimodal_restart_and_deletion(tmp_path):
    key=Fernet.generate_key();state_path=tmp_path/'delegation.sqlite3'
    state=EncryptedState(state_path,key,initial_state());provider=MockCredentialAdapter()
    engine=DelegationEngine(state,{'mock':provider},enabled=True,clock=lambda:100)
    gid=engine.propose(person(),provider='mock',account='synthetic-account-a',purpose='source.review',
                       actions=['source.read'],recipient='self',terms='policy-v1')
    visual=engine.frame(person(),'grants',gid,audio=False)
    spoken=engine.frame(person(),'grants',gid,visual=False)
    assert visual['binding']==spoken['binding'] and visual['revision']==spoken['revision']
    assert 'Review a synthetic source' in spoken['audio_text'] and '<button' in visual_document(visual)
    engine.respond(person(),'grants',gid,spoken['revision'],'confirm',spoken['binding'])
    tasks=[engine.submit(person(),gid,'source.read','self') for _ in range(5)]
    for tid in tasks:assert engine.run(person(),tid)=='waiting_repair'
    repair=engine.repair_ticket(person(),gid)
    frame=engine.frame(person(),'tasks',tasks[0]);engine.respond(person(),'tasks',tasks[0],frame['revision'],'stop')
    frame=engine.frame(person(),'tasks',tasks[1]);engine.respond(person(),'tasks',tasks[1],frame['revision'],'revoke')
    # Reopen actual encrypted disk state, not a serialized in-memory substitute.
    engine=DelegationEngine(EncryptedState(state_path,key,{}),{'mock':provider},enabled=True,clock=lambda:100)
    assert engine.complete_repair(person(),repair,channel='screenless')=='repaired'
    assert [engine.run(person(),tid) for tid in tasks]==['paused','revoked','verified','verified','verified']
    assert provider.repairs==1 and len(provider.calls)==3
    with pytest.raises(PermissionError):engine.frame(person('bob'),'tasks',tasks[2])
    assert b'synthetic-account-a' not in state_path.read_bytes()
    assert 'opaque_' not in json.dumps(engine.frame(person(),'tasks',tasks[2]))

    ledger=tmp_path/'source-authority.sqlite3';initialize_authority(ledger,key)
    formats=[('synthetic-statement-csv.v1',b'synthetic-statement-csv.v1\nid,date,amount_minor,currency,description\n1,2026-10-20,-1200,USD,Synthetic entry\n'),
             ('synthetic-unfamiliar-document.v1',json.dumps(dict(schema_version='synthetic-unfamiliar-document.v1',synthetic=True,text='Unknown clauses; do not infer instructions.')).encode())]
    for adapter,raw in formats:
        source=SourceWorkflow(tmp_path/'sources',ledger,key,adapter)
        consent=dict(filename='synthetic',sha256=hashlib.sha256(raw).hexdigest(),size_bytes=len(raw),confirmed=True)
        sid=source.consent('alice',consent)['workflow_id'];source.upload('alice',sid,raw)
        view=source.view('alice',sid)
        assert all(r['provenance']['source_sha256']==consent['sha256'] for r in view['records'])
        assert any('unknown' in s['text'].lower() for s in view['summary'])
        bid=source.backup('alice',sid)['snapshot_id'];old=source.data.path.read_bytes()
        source.terminate('alice',sid,'deleted');source.data.path.write_bytes(old)
        source=SourceWorkflow(tmp_path/'sources',ledger,key,adapter)
        with pytest.raises(ValueError):source.view('alice',sid)
        assert source.restore('alice',sid,bid)['unavailable']
    frame=engine.frame(person(),'grants',gid);engine.respond(person(),'grants',gid,frame['revision'],'delete')
    engine=DelegationEngine(EncryptedState(state_path,key,{}),{'mock':provider},enabled=True,clock=lambda:100)
    assert engine.run(person(),tasks[2])=='deleted'
