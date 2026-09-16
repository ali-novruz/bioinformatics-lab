"""Check local Markdown file links and notebooks without network access."""
from pathlib import Path
import re,sys,json
from urllib.parse import unquote
from biolab.health import check_health
ROOT=Path(__file__).resolve().parents[1]
errors=[]
try:health=check_health(ROOT)
except (ValueError,KeyError,TypeError,OSError) as exc:errors.append(str(exc))
for file in ROOT.rglob('*.md'):
    if any(x in file.parts for x in ['.git','.venv','raw','runs']):continue
    for target in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
        if '://' in target or target.startswith(('#','mailto:')):continue
        target=unquote(target.split('#')[0].split(' "')[0].strip('<>'))
        if target and not (file.parent/target).exists():errors.append(f'{file.relative_to(ROOT)} -> {target}')
for file in (ROOT/'notebooks').rglob('*.ipynb'):
    import nbformat
    try:nbformat.validate(nbformat.read(file,as_version=4))
    except Exception as exc:errors.append(f'{file.name}: {exc}')
ideas=(ROOT/'projects/IDEAS.md').read_text(encoding='utf-8')
if len(re.findall(r'^## \d+\.',ideas,re.M))<30:errors.append('Fewer than 30 project ideas')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('Local file links, notebook schemas, 30-project catalog, registry, data hashes and research graph verified:',health)
