"""One entry point for listing, fetching and running the implemented projects."""
from pathlib import Path
import argparse
import importlib.util
import json
import subprocess
import sys
import os
import time
from biolab.registry import load_registry
from biolab.reporting import new_run,write_json,finish_run

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description='Bioinformatics Lab project launcher')
    sub=parser.add_subparsers(dest='action',required=True)
    sub.add_parser('list')
    run=sub.add_parser('run');run.add_argument('project');run.add_argument('--offline',action='store_true')
    args=parser.parse_args()
    registry=ROOT/'projects/registry.json'
    projects=load_registry(ROOT)
    if args.action=='list':
        for p in projects:print(f'{p["id"]:15} {"offline" if p["offline"] else "download":8} {p["title"]}')
        return
    selected=projects if args.project=='all' else [p for p in projects if p['id']==args.project]
    if not selected:parser.error('Unknown project; run python scripts/lab.py list')
    skipped=[p['id'] for p in selected if args.offline and not p['offline']]
    if skipped and args.project!='all':parser.error('This project requires downloadable inputs; omit --offline')
    selected=[p for p in selected if p['id'] not in skipped]
    if any(p.get('research') for p in selected) and importlib.util.find_spec('pydeseq2') is None:
        parser.error('RNA-seq requires research dependencies: python -m pip install -e ".[dev,research]"')
    out=new_run(ROOT,'project-suite',[registry],{'project':args.project,'offline':args.offline})
    report={'status':'running','selected':[p['id'] for p in selected],'skipped_requires_download':skipped,'projects':[]}
    write_json(out/'suite.json',report)
    suite_start=time.perf_counter()
    failures=0
    for p in selected:
        print(f'Running {p["id"]}...',flush=True)
        log=out/(p['id']+'.log')
        commands=[[sys.executable,str(ROOT/'scripts/fetch_data.py'),'--dataset',dataset] for dataset in ([] if args.offline else p['fetch'])]
        commands.append([sys.executable,str(ROOT/'scripts'/p['script']),*p['args']])
        status=0
        start=time.perf_counter()
        receipt=out/(p['id']+'.receipts.jsonl')
        environment={**os.environ,'BIOLAB_RUN_RECEIPT':str(receipt)}
        executed=[]
        error=None
        with log.open('w',encoding='utf-8',newline='\n') as handle:
            for command in commands:
                executed.append(command)
                try:
                    completed=subprocess.run(command,cwd=ROOT,stdout=handle,stderr=subprocess.STDOUT,env=environment)
                    status=completed.returncode
                except OSError as exc:
                    status=127;error=str(exc);handle.write(error+'\n')
                if status:break
        elapsed=time.perf_counter()-start
        run_paths=[json.loads(line)['run_path'] for line in receipt.read_text(encoding='utf-8').splitlines()] if receipt.exists() else []
        if status==0 and not run_paths:
            status=1;error='Project exited without recording a run'
        for run_path in run_paths:
            finish_run(ROOT/run_path,status='complete' if status==0 else 'failed',elapsed_seconds=elapsed,error=error)
        report['projects'].append({'id':p['id'],'exit_code':status,'log':log.name,
                                   'commands':executed,'elapsed_seconds':elapsed,'run_paths':run_paths,'error':error})
        if status:failures+=1
        print(f'{p["id"]}: {"FAILED" if status else "passed"}',flush=True)
        write_json(out/'suite.json',report)
    report['status']='failed' if failures else 'complete'
    report['elapsed_seconds']=time.perf_counter()-suite_start
    write_json(out/'suite.json',report)
    finish_run(out,status=report['status'],elapsed_seconds=report['elapsed_seconds'])
    print(out,flush=True)
    if skipped:print('Skipped downloadable projects: '+', '.join(skipped))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
