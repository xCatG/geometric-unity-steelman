"""Generate a theorem inventory and reproducible axiom audit from the Lean sources."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
(ROOT / '.tools').mkdir(exist_ok=True)
rows = []
public = {}
for path in sorted((ROOT / 'B02').glob('*.lean')):
    stack = []
    depth = 0
    for number, raw in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        # Preserve line numbers while ignoring nested Lean block comments.
        line = ''
        j = 0
        while j < len(raw):
            if raw[j:j+2] == '/-':
                depth += 1; j += 2
            elif depth and raw[j:j+2] == '-/':
                depth -= 1; j += 2
            elif depth:
                j += 1
            elif raw[j:j+2] == '--':
                break
            else:
                line += raw[j]; j += 1
        line = line.strip()
        m = re.match(r'(namespace|section)\s*(\S*)', line)
        if m:
            stack.append((m[1], m[2]))
            continue
        if re.match(r'end(?:\s|$)', line):
            if stack: stack.pop()
            continue
        m = re.search(r'\b(theorem|lemma)\s+([^\s({:]+)', line)
        if not m:
            continue
        name = '.'.join([s[1] for s in stack if s[0] == 'namespace'] + [m[2]])
        is_private = 'private' in line[:m.start()]
        row = {'name': name, 'file': path.relative_to(ROOT).as_posix(),
               'line': number, 'private': is_private}
        rows.append(row)
        if not is_private:
            if name in public:
                raise AssertionError(f'duplicate public theorem: {name}: {public[name]} and {row}')
            public[name] = row
(ROOT / '.tools/theorems.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
(ROOT / 'Audit.lean').write_text('import B02\n\n' + '\n'.join(
    '#print axioms ' + r['name'] for r in rows if not r['private']) + '\n', encoding='utf-8')
print(f'Inventory: {len(rows)} theorem declarations; {len(public)} public axiom audits; no duplicate public names')
