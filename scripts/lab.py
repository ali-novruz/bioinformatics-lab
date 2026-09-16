"""One entry point for listing, fetching and running the implemented projects."""
from pathlib import Path
import argparse
import importlib.util
import json
import subprocess
import sys
from biolab.reporting import new_run,write_json

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description='Bioinformatics Lab project launcher')
    sub=parser.add_subparsers(dest='action',required=True)
    sub.add_parser('list')
    run=sub.add_parser('run');run.add_argument('project');run.add_argument('--offline',action='store_true')
    args=parser.parse_args()
    registry=ROOT/'projects/registry.json'
    projects=json.loads(registry.read_text(encoding='utf-8'))['projects']
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
    report={'selected':[p['id'] for p in selected],'skipped_requires_download':skipped,'projects':[]}
    failures=0
    for p in selected:
        print(f'Running {p["id"]}...',flush=True)
        log=out/(p['id']+'.log')
        commands=[[sys.executable,str(ROOT/'scripts/fetch_data.py'),'--dataset',dataset] for dataset in ([] if args.offline else p['fetch'])]
        commands.append([sys.executable,str(ROOT/'scripts'/p['script']),*p['args']])
        status=0
        with log.open('w',encoding='utf-8',newline='\n') as handle:
            for command in commands:
                completed=subprocess.run(command,cwd=ROOT,stdout=handle,stderr=subprocess.STDOUT)
                if completed.returncode:
                    status=completed.returncode;break
        report['projects'].append({'id':p['id'],'exit_code':status,'log':log.name})
        if status:failures+=1
        print(f'{p["id"]}: {"FAILED" if status else "passed"}',flush=True)
        write_json(out/'suite.json',report)
    print(out,flush=True)
    if skipped:print('Skipped downloadable projects: '+', '.join(skipped))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
