"""All-entry bridge for B03's real structure and chirality (no copied expectations)."""
from pathlib import Path
import json
import operator
import shutil
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from gu.clifford import Mono, chirality, gammas
from gu.rarita import SPLITS, charge_conjugation, euclid, spin_weights, even
from gu.rarita import j_square, j_preserves_chirality, j_weight_signs, chirality_vs_parity

def entries(a):
    return [[operator.index(p), operator.index(k)] for p,k in zip(a.perm,a.phase)]

def expected():
    out={}
    rows={r['split']:r for r in json.loads((ROOT/'experiments/B03/result.json').read_text())['matrix']}
    for key,(p,q,hor,nor) in SPLITS.items():
        gs,es=gammas(p,q),euclid(p,q)
        for a,g in enumerate(gs): out[f'{key}/G{a}']=entries(g)
        for a,e in enumerate(es): out[f'{key}/E{a}']=entries(e)
        out[f'{key}/B']=entries(charge_conjugation(p,q))
        out[f'{key}/C']=entries(chirality(p,q))
        out[f'{key}/Pi']=entries(Mono(range(gs[0].n),[0 if even(w) else 2 for w in spin_weights(key)]))
        for k,(a,b) in enumerate(hor+nor): out[f'{key}/h{k}']=entries((es[a]@es[b]).times_i_power(3))
        observed={'J_square':j_square(p,q),'J_preserves_chirality':j_preserves_chirality(p,q),
                  'J_weight_signs':list(j_weight_signs(key)),'chirality_vs_parity':chirality_vs_parity(key)}
        for field,value in observed.items(): assert rows[key][field]==value,(key,field,value,rows[key][field])
        print(f'RECORDED {key}: {json.dumps(observed,sort_keys=True)}')
    return out

def main():
    want=expected()
    lake=shutil.which('lake') or str(Path.home()/'.elan/bin/lake.exe')
    subprocess.run([lake,'build','B03.Model'],cwd=ROOT/'lean',check=True)
    raw=subprocess.check_output([lake,'env','lean','--run','bridge/B03Bridge.lean'],cwd=ROOT/'lean',text=True)
    got={}
    for line in raw.splitlines():
        label,payload=line.split('|',1) if line.count('|')==1 else line.rsplit('|',1)
        assert label not in got,label
        got[label]=json.loads(payload)
    assert got.keys()==want.keys(),(got.keys()-want.keys(),want.keys()-got.keys())
    for label in want:
        assert got[label]==want[label],label
    for name,data in [('python',want),('lean',got)]:
        (ROOT/f'lean/bridge/b03-{name}.actual.json').write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(f'PASS: {len(want)} monomial matrices; {sum(map(len,want.values()))} column (perm,phase) pairs; all four splits')
    print('PASS: all 16 recorded matrix-row real-structure/adapter fields match actual Python')
if __name__=='__main__': main()
