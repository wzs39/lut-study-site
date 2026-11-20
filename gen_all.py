# -*- coding: utf-8 -*-
import importlib.util, os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from genlib import emit
PARTS = os.path.join(HERE, 'parts')

groups, metas = {}, {}
for fn in sorted(os.listdir(PARTS)) if os.path.isdir(PARTS) else []:
    if not fn.endswith('.py') or fn.startswith('_'):
        continue
    spec = importlib.util.spec_from_file_location('part_' + fn[:-3], os.path.join(PARTS, fn))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print('!! %-16s fail: %s' % (fn, e)); continue
    meta, lec = getattr(mod, 'META', None), getattr(mod, 'LEC', None)
    if not isinstance(meta, dict) or not isinstance(lec, list):
        print('!! %-16s no META/LEC' % fn); continue
    cid = str(meta.get('cid') or '')
    metas[cid] = meta
    groups.setdefault(cid, []).extend(lec)
    print('   %-16s -> %-6s %2d lec' % (fn, cid, len(lec)))

only = sys.argv[1] if len(sys.argv) > 1 else None
print('')
for cid in sorted(groups, key=lambda c: metas[c].get('order', 999)):
    if only and cid != only:
        continue
    m = metas[cid]
    emit(cid, m.get('order', 999), m.get('name_zh', cid), m.get('name_en', ''),
         m.get('source_dir', ''), m.get('summary', ''), groups[cid])
