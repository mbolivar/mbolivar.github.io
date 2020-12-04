import os
from pathlib import Path
import shlex
from subprocess import run, CalledProcessError
import shutil
import sys

def runs(string, *args, **kwargs):  # 'run string'
    kwargs['check'] = True
    print(f'>>> {string}')
    sys.stdout.flush()
    return run(shlex.split(string), *args, **kwargs)

here = Path(__file__).parent.resolve()
docs = here / 'docs'
html = here / 'build' / 'html'
ref = runs('git rev-parse refs/heads/master',
           capture_output=True).stdout.decode().strip()

os.chdir(here)

runs('git checkout -q gh-pages')

try:
    print(f'>>> removing {docs}')
    if docs.is_dir():
        shutil.rmtree(docs)
    print(f'>>> copying {html} to {docs}')
    shutil.copytree(html, docs)
    print(f'>>> touching {docs / ".nojekyll"}')
    (docs / '.nojekyll').touch()
    runs('git add docs')
    try:
        runs(f'git commit -m "deploying {ref}"')
    except CalledProcessError:
        pass
    runs('git push --force-with-lease origin gh-pages')
finally:
    runs('git checkout master')
