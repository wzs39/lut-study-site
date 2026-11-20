# -*- coding: utf-8 -*-
"""content/*.json 符号修复（一次性、可重复运行）。

规则（只作用于 lecture html 字段）：
1. 删除零宽/不可见字符（U+200B..U+200F, U+FEFF, U+00AD）。
2. 删除空段落 <p></p> / 空行段落。
3. 裸 `&`（不构成实体）→ `&amp;`。
4. 裸 `<`（不是合法标签开头）→ `&lt;`。
5. LaTeX 残留：`x^{AB}` → `x<sup>AB</sup>`；`a_{ij}` → `a<sub>ij</sub>`；
   `x^2`、`b^k`、`e^(rt)`、`2^m` 等短上标 → `<sup>`。只在行内文本与
   <code>/<td>/<li> 中做，跳过 <pre> 块（真代码保持原样）。
6. 修复后仍要求 <pre><code> 内的 < > 保持实体（本脚本不动 &lt; 等已有实体）。
"""
import json, io, glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

ZW = re.compile(r'[\u200b\u200c\u200d\u200e\u200f\ufeff\u00ad]')
EMPTY_P = re.compile(r'<p>\s*</p>')
BARE_AMP = re.compile(r'&(?!(?:#\d+|#[xX][0-9a-fA-F]+|[a-zA-Z]+);)')
BARE_LT = re.compile(r'<(?![a-zA-Z/!?])')

# 上标：优先 {..}，其次 (...) 或 1~2 个字符（可带前导 +/-/−）
SUP = re.compile(r'(?<=[A-Za-z0-9\)\u2070-\u2089])\^(?:\{([^{}]{1,40})\}|\(([^()]{1,20})\)|([+\-−]?[A-Za-z0-9]{1,2}))')
SUBB = re.compile(r'(?<=[A-Za-z0-9\)\]])_\{([^{}]{1,40})\}')


def fix_sup(m):
    body = m.group(1) or m.group(2) or m.group(3)
    return '<sup>%s</sup>' % body


def fix_sub(m):
    return '<sub>%s</sub>' % m.group(1)


def split_outside_pre(html):
    """把字符串按 <pre>…</pre> 切开，返回 [(is_pre, chunk)]。"""
    out = []
    i = 0
    while True:
        a = html.find('<pre', i)
        if a < 0:
            out.append((False, html[i:]))
            break
        b = html.find('</pre>', a)
        if b < 0:
            out.append((False, html[i:]))
            break
        b += len('</pre>')
        if a > i:
            out.append((False, html[i:a]))
        out.append((True, html[a:b]))
        i = b
    return out


def fix_html_text(t):
    parts = split_outside_pre(t)
    res = []
    for is_pre, chunk in parts:
        if is_pre:
            res.append(chunk)
            continue
        chunk = ZW.sub('', chunk)
        chunk = EMPTY_P.sub('', chunk)
        chunk = BARE_AMP.sub('&amp;', chunk)
        chunk = BARE_LT.sub('&lt;', chunk)
        chunk = SUBB.sub(fix_sub, chunk)
        chunk = SUP.sub(fix_sup, chunk)
        res.append(chunk)
    t = ''.join(res)
    t = ZW.sub('', t)  # <pre> 内也清一次零宽
    return t


def main():
    changed = 0
    for f in sorted(glob.glob('content/*.json')):
        d = json.load(io.open(f, encoding='utf-8'))
        n = 0
        for l in d['lectures']:
            old = l['html']
            new = fix_html_text(old)
            if new != old:
                l['html'] = new
                n += 1
        if n:
            tmp = f + '.tmp'
            with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
                json.dump(d, fh, ensure_ascii=False, indent=1)
            os.replace(tmp, f)
            changed += 1
            print('[fix] %-8s %d lectures' % (os.path.basename(f)[:-5], n))
    print('files changed:', changed)


if __name__ == '__main__':
    main()
