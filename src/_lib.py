# -*- coding: utf-8 -*-
"""讲义内容公共库：把结构化片段拼成站点要求的 8 段 HTML。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
CONTENT = os.path.join(SITE, 'content')


def h2(t):
    return '<h2>%s</h2>' % t


def h3(t):
    return '<h3>%s</h3>' % t


def p(*a):
    return ''.join('<p>%s</p>' % x for x in a)


def ul(*a):
    return '<ul>' + ''.join('<li>%s</li>' % x for x in a) + '</ul>'


def ol(*a):
    return '<ol>' + ''.join('<li>%s</li>' % x for x in a) + '</ol>'


def ck(*a):
    return '<ul class="checklist">' + ''.join('<li>%s</li>' % x for x in a) + '</ul>'


def st(*a):
    return '<ol class="steps">' + ''.join('<li>%s</li>' % x for x in a) + '</ol>'


def tb(head, rows):
    hs = ''.join('<th>%s</th>' % c for c in head)
    rs = ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in rows)
    return '<table><tr>%s</tr>%s</table>' % (hs, rs)


def kw(rows):
    return tb(['English', '中文', '说明 / 例句'], rows)


def note(kind, title, body):
    k = (' ' + kind) if kind else ''
    return '<div class="callout%s"><b>%s</b>%s</div>' % (k, title, body)


def qa(q, a):
    return '<div class="qa"><div class="q">%s</div>%s</div>' % (q, a)


def det(summary, body):
    return '<details><summary>%s</summary><div class="ans">%s</div></details>' % (summary, body)


def code(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return '<pre><code>%s</code></pre>' % t


def badge(kind, t):
    return '<span class="badge %s">%s</span>' % (kind, t)


def lec(slug, zh, en, kws, files, ov, dt, kws_html, ex, pr, em, ck_html, mp):
    html = ''.join([
        '<section class="card" data-type="overview">' + ov + '</section>',
        '<section class="card" data-type="detail">' + dt + '</section>',
        '<section class="card" data-type="keywords">' + kws_html + '</section>',
        '<section class="card" data-type="examples">' + ex + '</section>',
        '<section class="card" data-type="practice">' + pr + '</section>',
        '<section class="card" data-type="exam">' + em + '</section>',
        '<section class="card" data-type="checklist">' + ck_html + '</section>',
        '<section class="card" data-type="mapping">' + mp + '</section>',
    ])
    return {'slug': slug, 'title_zh': zh, 'title_en': en, 'keywords': list(kws),
            'source_files': list(files), 'html': html}


def emit(cid, order, name_zh, name_en, source_dir, summary, lectures):
    data = {'id': cid, 'order': order, 'name_zh': name_zh, 'name_en': name_en,
            'source_dir': source_dir, 'summary': summary, 'lectures': lectures}
    os.makedirs(CONTENT, exist_ok=True)
    fp = os.path.join(CONTENT, cid + '.json')
    with open(fp, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    n = len(lectures)
    tot = sum(len(x['html']) for x in lectures)
    print('[ok] %-6s %2d 讲  %7d B  %7d 字符' % (cid, n, os.path.getsize(fp), tot))
    return fp
