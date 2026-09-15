"""Run directories never overwrite an earlier experiment."""
from pathlib import Path
from datetime import datetime,timezone
from importlib.metadata import version,PackageNotFoundError
import hashlib,json,platform,uuid,subprocess

def write_json(path,value):
    Path(path).write_text(json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')

def new_run(root,project,inputs=(),parameters=None):
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]
    out=Path(root)/'results/runs'/project/stamp;out.mkdir(parents=True)
    packages={}
    for name in ['bioinformatics-lab','numpy','pandas','scipy','scikit-learn','biopython','pydeseq2','matplotlib']:
        try:packages[name]=version(name)
        except PackageNotFoundError:pass
    commit=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True)
    dirty=subprocess.run(['git','status','--porcelain'],cwd=root,capture_output=True,text=True)
    write_json(out/'run.json',{'project':project,'created_utc':stamp,'python':platform.python_version(),'platform':platform.platform(),'packages':packages,'git_commit':commit.stdout.strip() if commit.returncode==0 else None,'working_tree_dirty':bool(dirty.stdout.strip()),'parameters':parameters or {},'inputs':[{'path':str(Path(p).relative_to(root)),'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'bytes':Path(p).stat().st_size} for p in inputs]})
    return out
