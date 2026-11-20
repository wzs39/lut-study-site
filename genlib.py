# -*- coding: utf-8 -*-
"""课程讲义站 · 内容构建库（单一权威版本）

每门课一个生成脚本 gen/<cid>.py：
    from genlib import L, emit, h2, h3, p, ul, ol, tb, cal, qa, det, pre, K, chips, S
    LEC = [ L(slug=..., tzh=..., ten=..., keywords=[...], files=[...],
              overview=..., detail=..., kws=..., examples=...,
              practice=..., exam=..., checklist=..., mapping=...) ]
    emit(cid, order, name_zh, name_en, source_dir, summary, LEC)
生成 content/<cid>.json，再由 build.py 渲染成网页。
"""
import io
import json
import os

SITE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(SITE, 'content')


# ---------------- 组装 ----------------
def L(slug, tzh, ten, keywords, files, overview='', detail='', kws='',
      examples='', practice='', exam='', checklist='', mapping=''):
    def sec(kind, body):
        return '<section class="card" data-type="%s">%s</section>' % (kind, body)

    html = '\n'.join([
        sec('overview', overview),
        sec('detail', detail),
        sec('keywords', kws),
        sec('examples', examples),
        sec('practice', practice),
        sec('exam', exam),
        sec('checklist', checklist),
        sec('mapping', mapping),
    ])
    return {'slug': slug, 'title_zh': tzh, 'title_en': ten, 'keywords': list(keywords),
            'source_files': list(files), 'html': html}


def emit(cid, order, name_zh, name_en, source_dir, summary, lectures):
    os.makedirs(CONTENT, exist_ok=True)
    data = {'id': cid, 'order': order, 'name_zh': name_zh, 'name_en': name_en,
            'source_dir': source_dir, 'summary': summary, 'lectures': lectures}
    p = os.path.join(CONTENT, cid + '.json')
    tmp = p + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
    total = sum(len(x['html']) for x in lectures)
    print('[ok] %-6s %2d lec  %8d B  html %d chars' % (cid, len(lectures), os.path.getsize(p), total))
    return p


# ---------------- 片段 ----------------
def h2(t): return '<h2>' + t + '</h2>'


def h3(t): return '<h3>' + t + '</h3>'


def p(*xs): return ''.join('<p>' + str(x) + '</p>' for x in xs)


def ul(*xs): return '<ul>' + ''.join('<li>' + str(x) + '</li>' for x in xs) + '</ul>'


def ck(*xs): return '<ul class="checklist">' + ''.join('<li>' + str(x) + '</li>' for x in xs) + '</ul>'


def ol(*xs): return '<ol>' + ''.join('<li>' + str(x) + '</li>' for x in xs) + '</ol>'


def st(*xs): return '<ol class="steps">' + ''.join('<li>' + str(x) + '</li>' for x in xs) + '</ol>'


def tb(head, *rows):
    h = ''.join('<th>' + str(c) + '</th>' for c in head)
    b = ''.join('<tr>' + ''.join('<td>' + str(c) + '</td>' for c in r) + '</tr>' for r in rows)
    return '<table><tr>' + h + '</tr>' + b + '</table>'


def K(*rows):
    return tb(('English', '中文', '说明 / 例句'), *rows)


def cal(kind, title, body=''):
    k = (' ' + kind) if kind else ''
    return '<div class="callout' + k + '"><b>' + title + '</b>' + str(body) + '</div>'


def badge(kind, t):
    return '<span class="badge ' + kind + '">' + t + '</span> '


def qa(title, body):
    return '<div class="qa"><div class="q">' + title + '</div>' + str(body) + '</div>'


def det(summary, body):
    return '<details><summary>' + summary + '</summary><div class="ans">' + str(body) + '</div></details>'


def pre(code):
    t = str(code).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return '<pre><code>' + t + '</code></pre>'


def code(t): return '<code>' + str(t) + '</code>'


def kbd(t): return '<kbd>' + str(t) + '</kbd>'


def chips(items):
    return ' '.join('<span class="chip">' + str(i) + '</span>' for i in items)


def S(cid, order, zh, en, src, summary, lecs):
    return emit(cid, order, zh, en, src, summary, lecs)
