# -*- coding: utf-8 -*-
"""把 extensions/<cid>.json 里的知识拓展注入 content/<cid>.json。

数据契约（extensions/<cid>.json）：
{
  "<slug>": [
     {"kind": "idea", "title": "拓展", "html": "<p>…</p>"},
     {"kind": "idea", "title": "背景", "html": "…"}
  ],
  "_note": "可选，说明来源"
}
- key 是讲次 slug；value 是拓展块列表（1–3 个）。
- kind 目前支持 "idea"（紫色拓展框）与 "tip"（绿色技巧框）。
- html 里只写 <p>/<ul>/<ol>/<table>/<code>/<strong>，不要写 <section>/<h2>/<h3>。

注入位置：detail 板块的 </section> 之前，即知识点主体最后。
幂等：已注入过的讲次（含 data-ext="<slug>-<i>" 标记）不会重复注入。
"""
import json, io, os, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SITE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(SITE, 'content')
EXT = os.path.join(SITE, 'extensions')


def build_blocks(cid, slug, items):
    out = []
    for i, it in enumerate(items):
        kind = it.get('kind', 'idea')
        title = it.get('title', '拓展')
        body = it.get('html', '').strip()
        if not body:
            continue
        mark = 'data-ext="%s-%d"' % (slug, i)
        out.append('<div class="callout %s" %s><b>%s</b>%s</div>' % (kind, mark, title, body))
    return ''.join(out)


def inject_one(lec_html, cid, slug, items):
    marker = 'data-ext="%s-0"' % slug
    if marker in lec_html:
        return lec_html, 0
    blocks = build_blocks(cid, slug, items)
    if not blocks:
        return lec_html, 0
    m = re.search(r'(<section[^>]*data-type="detail"[^>]*>)(.*?)(</section>)',
                  lec_html, flags=re.S)
    if not m:
        return lec_html, 0
    new_detail = m.group(1) + m.group(2) + blocks + m.group(3)
    out = lec_html[:m.start()] + new_detail + lec_html[m.end():]
    return out, len(items)


def main():
    if not os.path.isdir(EXT):
        print('!! extensions/ 不存在')
        return 1
    total_files = total_lectures = 0
    missing = []
    for ef in sorted(glob.glob(os.path.join(EXT, '*.json'))):
        cid = os.path.splitext(os.path.basename(ef))[0]
        cf = os.path.join(CONTENT, cid + '.json')
        if not os.path.exists(cf):
            print('!! 没有对应课程内容: %s' % cid)
            continue
        ext = json.load(io.open(ef, encoding='utf-8'))
        d = json.load(io.open(cf, encoding='utf-8'))
        n = 0
        have_slugs = set()
        for l in d['lectures']:
            items = ext.get(l['slug'])
            if not items:
                missing.append('%s/%s' % (cid, l['slug']))
                continue
            have_slugs.add(l['slug'])
            new, k = inject_one(l['html'], cid, l['slug'], items)
            if k:
                l['html'] = new
                n += 1
        unknown = [k for k in ext if k not in ('_note',) and k not in have_slugs]
        if unknown:
            print('!! %s: extensions 里的 slug 在 content 中不存在: %s' % (cid, ','.join(unknown)))
        if n:
            tmp = cf + '.tmp'
            with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
                json.dump(d, fh, ensure_ascii=False, indent=1)
            os.replace(tmp, cf)
            total_files += 1
            total_lectures += n
            print('[ext] %-8s 注入 %d 讲' % (cid, n))
    print('合计：%d 门课 / %d 讲注入拓展' % (total_files, total_lectures))
    if missing:
        print('未提供拓展的讲次 (%d)：' % len(missing))
        for m in missing[:40]:
            print('   ', m)
    return 0


if __name__ == '__main__':
    sys.exit(main())
