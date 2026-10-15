"""Seed convention faults in disposable B03 source copies; keep Python expectations fixed."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import tempfile
from b03_check import ROOT, expected

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    model=ROOT/'lean/B03/Model.lean'
    bridge=ROOT/'lean/bridge/B03Bridge.lean'
    hashes={p:digest(p) for p in (model,bridge)}
    source=model.read_text(encoding='utf-8-sig').split('set_option maxRecDepth',1)[0]+'\nend B03\n'
    runner=bridge.read_text(encoding='utf-8-sig').replace('import B03.Model','',1)
    want=expected()
    faults=[
      ('reverse_Y_phase','then 1 + 2 * bit','then 3 + 2 * bit'),
      ('omit_timelike_i','(euclidean m a).shift (if a < p then 0 else 1)',
       '(euclidean m a).shift (if a < p then 0 else 0)'),
      ('reverse_chirality_sign','(volume m p).shift (chiralityPhase m p)',
       '(volume m p).shift (chiralityPhase m p + 2)'),
    ]
    lake=shutil.which('lake') or str(Path.home()/'.elan/bin/lake.exe')
    with tempfile.TemporaryDirectory(prefix='b03-mutations-',dir=ROOT/'lean/.tools') as directory:
        for name,before,after in faults:
            assert source.count(before)==1,(name,'non-unique mutation')
            path=Path(directory)/f'{name}.lean'
            path.write_text(source.replace(before,after,1)+runner,encoding='utf-8')
            raw=subprocess.check_output([lake,'env','lean','--run',str(path)],cwd=ROOT/'lean',text=True)
            got={label:json.loads(payload) for label,payload in (line.rsplit('|',1) for line in raw.splitlines())}
            assert got.keys()==want.keys(),name
            failures=[label for label in want if got[label]!=want[label]]
            assert failures,f'SURVIVED: {name}'
            columns=sum(sum(a!=b for a,b in zip(got[label],want[label])) for label in failures)
            first=failures[0]
            j=next(j for j,(a,b) in enumerate(zip(got[first],want[first])) if a!=b)
            print(f'DETECTED {name}: {len(failures)} matrices, {columns} columns; '
                  f'first {first}[{j}]: Lean={got[first][j]}, Python={want[first][j]}',flush=True)
    for path,h in hashes.items():
        assert digest(path)==h,path
        print(f'UNCHANGED SHA256 {path.name}: {h}')
if __name__=='__main__': main()
