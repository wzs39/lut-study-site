# -*- coding: utf-8 -*-
"""fix_symbols.py 的补充第二轮：只处理第一轮漏掉的 LaTeX 残留。

- `_{a}^{b}` / `^{b}` / `_{a}`：任意位置的括号上下标 → <sub>/<sup>
- `2^|S|`：竖线内容上标
- `x^π` 这类单个希腊/数学字符上标
跳过 <pre> 块与已经是代码语义的 `a ^ b`（Python 对称差）、`:^8`、报错行里的 `^`
——这些都不带 `{`、`|`、希腊字母，规则不会命中。
"""
import json, io, glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

RANGE = re.compile(r'_\{([^{}]{1,40})\}\^\{([^{}]{1,40})\}')
SUB = re.compile(r'_\{([^{}]{1,40})\}')
SUPB = re.compile(r'\^\{([^{}]{1,40})\}')
SUPPIPE = re.compile(r'\^\|([^|<>]{1,20})\|')
SUPGR = re.compile(r'(?<=[A-Za-z0-9\)\u2070-\u2089])\^([αβγδελπθστφψωℝℕℤℚ∞′″˖π])')


def fix(t):
    out = []
    i = 0
    while True:
        a = t.find('<pre', i)
        if a < 0:
            out.append(t[i:]); break
        b = t.find('</pre>', a)
        if b < 0:
            out.append(t[i:]); break
        b += len('</pre>')
        out.append(t[i:a])
        out.append(t[a:b])
        i = b
    parts = out
    res = []
    for idx, chunk in enumerate(parts):
        if idx % 2 == 1:  # pre 内容保持
            res.append(chunk)
            continue
        chunk = RANGE.sub(lambda m: '<sub>%s</sub><sup>%s</sup>' % (m.group(1), m.group(2)), chunk)
        chunk = SUPB.sub(lambda m: '<sup>%s</sup>' % m.group(1), chunk)
        chunk = SUB.sub(lambda m: '<sub>%s</sub>' % m.group(1), chunk)
        chunk = SUPPIPE.sub(lambda m: '<sup>|%s|</sup>' % m.group(1), chunk)
        chunk = SUPGR.sub(lambda m: '<sup>%s</sup>' % m.group(1), chunk)
        res.append(chunk)
    return ''.join(res)


def main():
    nfile = 0
    for f in sorted(glob.glob('content/*.json')):
        d = json.load(io.open(f, encoding='utf-8'))
        n = 0
        for l in d['lectures']:
            new = fix(l['html'])
            if new != l['html']:
                l['html'] = new
                n += 1
        if n:
            tmp = f + '.tmp'
            with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
                json.dump(d, fh, ensure_ascii=False, indent=1)
            os.replace(tmp, f)
            nfile += 1
            print('[fix2] %-8s %d lectures' % (os.path.basename(f)[:-5], n))
    print('files changed:', nfile)


if __name__ == '__main__':
    main()
