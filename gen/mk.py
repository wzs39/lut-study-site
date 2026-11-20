# -*- coding: utf-8 -*-
"""讲义内容组装助手：把紧凑的块列表展开成 8 段 HTML。

块格式：
    ('h2'|'h3'|'p'|'pre'|'raw', text)
    ('ul', [item, ...])             可选第三元为 class 名
    ('ol', [item, ...])
    ('tb', [表头...], [[单元格...], ...])
    ('cal', kind, title, body)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import (L, emit, tb, cal, ul, ol, qa, det, pre, h2, h3, p, chips)  # noqa


_SIMPLE = {'h2': h2, 'h3': h3, 'p': p, 'pre': pre}


def _ul(items, cls=''):
    body = ''.join('<li>' + str(x) + '</li>' for x in items)
    if cls:
        return '<ul class="' + cls + '">' + body + '</ul>'
    return '<ul>' + body + '</ul>'


def dd(blocks):
    out = []
    for b in blocks:
        k = b[0]
        if k == 'raw':
            out.append(b[1])
        elif k in _SIMPLE:
            out.append(_SIMPLE[k](b[1]))
        elif k == 'ul':
            out.append(_ul(b[1], b[2] if len(b) > 2 else ''))
        elif k == 'ol':
            out.append(ol(*b[1]))
        elif k == 'tb':
            out.append(tb(b[1], *b[2]))
        elif k == 'cal':
            out.append(cal(b[1], b[2], b[3] if len(b) > 3 else ''))
        else:
            raise ValueError('unknown block ' + repr(k))
    return '\n'.join(out)


def ex(items):
    return '\n'.join(qa(t, b) for t, b in items)


def pr(items):
    return '\n'.join(qa(t, b) for t, b in items)


def kws(rows):
    return tb(['English', '中文', '说明 / 例句'], *rows)


def mp(rows, note=''):
    s = tb(['源文件', '覆盖内容'], *rows)
    if note:
        s += p(note)
    return s


def eg(items):
    body = []
    ans = []
    for i, (q, a) in enumerate(items, 1):
        body.append(qa('练 %d' % i, q))
        ans.append(p('<b>%d.</b> %s' % (i, a)))
    return '\n'.join(body) + det('参考答案与思路', '\n'.join(ans))