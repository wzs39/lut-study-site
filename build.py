#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""课程讲义站 · 静态生成器

用法:
    python build.py                     全量重建（所有课程页 + 总览页）
    python build.py --course KE00BX35   只重建某门课，并刷新总览页
    python build.py --check             检查每篇讲义的必备板块是否齐全

新增内容：在 content/ 下新建 <课程ID>.json（格式见 SPEC.md），再跑一次 build.py。
子目录：
    content/<课程ID>.json     课程内容（可手写，也可由子代理生成）
    assets/style.css          全站样式
    产出：index.html、c/<课程ID>/index.html、c/<课程ID>/<讲义>.html
"""

import datetime
import glob
import io
import html
import json
import os
import re
import sys
from site_navigation import NavItem, breadcrumbs, course_tree, page_frame, site_navigation, sequence_navigation
from learning_data import build_search_data, script_json
from learning_views import home_widgets, search_box, course_progress, lecture_controls, reading_controls
from source_info import SourceCatalogue, source_panel
from media_assets import MediaAssets

# Windows 控制台默认 GBK，讲义标题里出现 ⑪ 这类字符时 print 会抛 UnicodeEncodeError。
# 统一把标准输出改成 UTF-8，并对无法编码的字符退化为替代符，保证 --check 不因编码中断。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))
SOURCE_CATALOGUE = SourceCatalogue(ROOT)
MEDIA = MediaAssets(ROOT)
CONTENT = os.path.join(ROOT, "content")
MANIFEST = os.path.join(os.path.dirname(ROOT), "manifest2.txt")
REQUIRED = [
    "overview",
    "detail",
    "keywords",
    "examples",
    "practice",
    "exam",
    "checklist",
    "mapping",
]
DATE = datetime.date.today().isoformat()

with io.open(os.path.join(ROOT, "assets", "style.css"), encoding="utf-8") as _fh:
    CSS_TEXT = _fh.read()
with io.open(os.path.join(ROOT, "assets", "learning.css"), encoding="utf-8") as _fh:
    CSS_TEXT += "\n" + _fh.read()
with io.open(os.path.join(ROOT, "assets", "navigation.js"), encoding="utf-8") as _fh:
    NAVIGATION_JS = _fh.read()

LAYOUT = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<script>try{var s=localStorage.getItem("lut-theme");document.querySelector("meta[name=color-scheme]").content=(s==="light"||s==="dark")?s:"light dark";}catch(e){}</script>
<title>{{TITLE}}</title>
<style>{{CSSTEXT}}</style>
</head>
<body id="top" data-module="{{MODULE}}">
<a class="skip-link" href="#page-content">跳到正文</a>
<header class="topbar"><div class="topbar-in">
<a class="brand" href="{{HOME}}">课程讲义站</a>
{{NAVIGATION}}
<div class="header-actions"><a class="search-shortcut" href="{{HOME}}#site-search" aria-label="全站搜索与原版课件查询" title="全站搜索与原版课件查询 (Ctrl+K)"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></a>
<button id="thbtn" class="thbtn" title="切换配色：跟随系统 / 浅色 / 深色" type="button" aria-label="切换配色模式">
<span class="th-sys" aria-hidden="true">◐</span><span class="th-light" aria-hidden="true">☀</span><span class="th-dark" aria-hidden="true">☾</span>
</button>
</div>
</div></header>
<main id="main-content" tabindex="-1" class="wrap {{CLS}}" data-site-prefix="{{PREFIX}}">
{{CRUMB}}
{{BODY}}
</main>
<footer class="foot">内容基于原始课程文件整理 · 生成于 {{DATE}} <a href="#top" class="totop">回到顶部 ↑</a></footer>
<script>{{NAVSCRIPT}}</script>
<script src="{{PREFIX}}assets/config.js"></script><script src="{{PREFIX}}data/learning-catalog.js"></script><script src="{{PREFIX}}assets/learning.bundle.js"></script>
{{SCRIPT}}{{THEME}}
</body>
</html>
"""

LECTURE_JS = """<script>
(function(){
  var bar=document.createElement('div');bar.id='pbar';bar.setAttribute('aria-hidden','true');
  document.body.appendChild(bar);
  var btt=document.createElement('button');btt.id='btt';btt.type='button';
  btt.setAttribute('aria-label','回到顶部');btt.textContent='↑';
  btt.addEventListener('click',function(){
    window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
  });
  document.body.appendChild(btt);
  var queued=false;
  function update(){
    var h=document.documentElement,max=h.scrollHeight-h.clientHeight,y=window.scrollY||0;
    bar.style.width=(max>0?y/max*100:0)+'%';btt.classList.toggle('show',y>600);
  }
  addEventListener('scroll',function(){
    if(!queued){queued=true;requestAnimationFrame(function(){queued=false;update();});}
  },{passive:true});
  addEventListener('resize',update);update();
})();
</script>"""

THEME_JS = """<script>
(function(){
  var KEY='lut-theme', m=document.querySelector('meta[name="color-scheme"]'), b=document.getElementById('thbtn');
  function stored(){ try{ var s=localStorage.getItem(KEY); return (s==='light'||s==='dark')?s:null; }catch(e){ return null; } }
  function setMeta(v){ m.content=v||'light dark'; }
  function sysDark(){ return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches; }
  function label(){ var s=stored(); b.title='配色：'+(s==='light'?'浅色':s==='dark'?'深色':'跟随系统')+'（点击切换）'; }
  setMeta(stored()); label();
  b.addEventListener('click',function(){
    var cur=stored() || (sysDark()?'dark':'light');   /* 当前真正渲染的配色 */
    var next = cur==='dark' ? 'light' : 'dark';        /* 三态：系统 → 相反值；再次点回系统 */
    var sys = sysDark()?'dark':'light';
    var v = (next===sys) ? null : next;                /* 目标若等于系统偏好，则回到跟随系统 */
    try{ if(v) localStorage.setItem(KEY,v); else localStorage.removeItem(KEY); }catch(e){}
    setMeta(v); label();
  });
  window.addEventListener('storage',function(e){ if(e.key===KEY){ setMeta(stored()); label(); } });
})();
</script>"""



def encode_inline_controls(body):
    """Preserve literal CR/LF examples as entities without changing their DOM text."""
    return re.sub(r'<code>([\r\n]+)</code>',
                  lambda match: '<code>' + ''.join('&#%d;' % ord(char) for char in match[1]) + '</code>', body)


def page(title, body, prefix, crumb, cls="", script="", module="courses", groups=()):
    body = encode_inline_controls(MEDIA.render(scrollable_tables(body), prefix))
    return (
        LAYOUT.replace("{{TITLE}}", html.escape(title))
        .replace("{{CSSTEXT}}", CSS_TEXT)
        .replace("{{HOME}}", prefix + "index.html")
        .replace("{{PREFIX}}", prefix)
        .replace("{{CRUMB}}", breadcrumbs(crumb))
        .replace("{{MODULE}}", module)
        .replace("{{NAVIGATION}}", site_navigation(prefix, module, nested=bool(prefix)))
        .replace("{{NAVSCRIPT}}", NAVIGATION_JS)
        .replace("{{CLS}}", cls)
        .replace("{{BODY}}", page_frame(body, groups, title))
        .replace("{{SCRIPT}}", script)
        .replace("{{THEME}}", THEME_JS)
        .replace("{{DATE}}", DATE)
    )


def write(path, text):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


def fix_assets(html_text, prefix=""):
    """内容里写 assets/img|media/... 相对路径；按页面深度补前缀，使讲义页与合订本都可用。"""
    if not html_text or not prefix:
        return html_text
    return html_text.replace('src="assets/', 'src="' + prefix + 'assets/')


def decorate(body):
    toc = []
    counter = [0]

    def rep(m):
        lvl, attrs, txt = m.group(1), m.group(2) or "", m.group(3)
        plain = html.unescape(re.sub(r"<[^>]+>", "", txt)).strip()
        got = re.search(r'id="([^"]+)"', attrs)
        if got:
            sid = got.group(1)
        else:
            counter[0] += 1
            sid = "s%d" % counter[0]
            attrs += ' id="%s"' % sid
        toc.append((int(lvl), sid, plain))
        return "<h%s%s>%s</h%s>" % (lvl, attrs, txt, lvl)

    body = re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", rep, body, flags=re.S)
    nav = "".join(
        '<a class="toc-l%d" href="#%s">%s</a>' % (l, sid, html.escape(t))
        for l, sid, t in toc
    )
    return body, nav


def plain_text(s, n=180):
    t = re.sub(r"<[^>]+>", " ", s or "")
    t = html.unescape(t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:n] + ("…" if len(t) > n else "")


def section(body, kind):
    m = re.search(
        r'<section[^>]*data-type="%s"[^>]*>(.*?)</section>' % kind,
        body or "",
        flags=re.S,
    )
    return m.group(1) if m else ""


def load_courses():
    out = []
    for f in sorted(glob.glob(os.path.join(CONTENT, "*.json"))):
        try:
            with open(f, encoding="utf-8") as fh:
                c = json.load(fh)
            c.setdefault("id", os.path.splitext(os.path.basename(f))[0])
            out.append(c)
        except Exception as e:
            print("!! 读取失败 %s : %s" % (os.path.basename(f), e))
    out.sort(key=lambda c: (c.get("order", 999), c.get("id", "")))
    return out


CN2ID = {
    "BH60A7201": "29911",
    "BH60A7400": "29913",
    "BM20A9200": "30565",
    "CT10A9900": "30331",
    "CT30A1000": "30332",
    "CT60A0250": "30352",
    "CT60A4050": "30361",
    "K200DJ96": "33295",
    "K200DJ99": "34583",
    "KE00BX35": "32667",
    "KE00DA03": "32632",
    "HDD4010": "62",
    "HDD4020": "80",
    "HDD5020": "86",
    "LUT digital orientation": "29428",
}


def manifest_files():
    """源文件清单：优先用已抽取的 text/index.json（按 cid 分组），退回 manifest2.txt。"""
    g = {}
    idx = os.path.join(ROOT, "text", "index.json")
    if os.path.exists(idx):
        try:
            with io.open(idx, encoding="utf-8") as fh:
                for it in json.load(fh):
                    cid = str(it.get("cid") or "")
                    rel = it.get("rel") or ""
                    if cid and rel:
                        g.setdefault(cid, []).append(rel)
        except Exception as e:
            print("!! text/index.json 读取失败: %s" % e)
    if g:
        return g
    if os.path.exists(MANIFEST):
        with io.open(MANIFEST, encoding="utf-8") as fh:
            for line in fh:
                p = line.rstrip("\n").split("|")
                if len(p) >= 3:
                    for code, cid in CN2ID.items():
                        if code.lower() in p[0].lower():
                            g.setdefault(cid, []).append(p[1])
                            break
    return g


SECTION_LABELS = [
    ("overview", "本节定位与目标"),
    ("detail", "知识精讲"),
    ("keywords", "英文术语"),
    ("examples", "例题解析"),
    ("practice", "练习与解答"),
    ("exam", "考点与易错"),
    ("checklist", "方法清单"),
    ("mapping", "原始资料对照"),
]


def add_section_ids(html_text):
    """给每个 <section ... data-type="x"> 补 id="sec-x"，供板块快捷跳转。"""
    for kind, _ in SECTION_LABELS:
        html_text = re.sub(
            r'<section([^>]*?)data-type="%s"' % kind,
            '<section id="sec-%s"\\1data-type="%s"' % (kind, kind),
            html_text,
            count=1,
        )
    return html_text


def lecture_outline(body):
    items = []
    for kind, label in SECTION_LABELS:
        block = section(body, kind)
        if not block:
            continue
        headings, parent = [], None
        for level, anchor, text in re.findall(r'<h([23])[^>]*id="([^"]+)"[^>]*>(.*?)</h\1>', block, flags=re.S):
            node = NavItem(plain_text(text, 200), "#" + anchor)
            if level == "3" and parent:
                parent.children += (node,)
            else:
                headings.append(node)
                parent = node if level == "2" else None
        items.append(NavItem(label, "#sec-" + kind, tuple(headings)))
    return items


def scrollable_tables(body):
    # Retain native table semantics while containing wide tables on small screens.
    table_index = 0

    def scroll_table(match):
        nonlocal table_index
        table_index += 1
        return (
            '<div class="table-scroll" role="region" tabindex="0" '
            'aria-label="讲义表格 %d，可横向滚动">' % table_index
            + match.group(0) + "</div>"
        )

    return re.sub(
        r"<table\b[^>]*>.*?</table>",
        scroll_table,
        body, flags=re.S,
    )


def build_lecture(c, i):
    lecs = c["lectures"]
    lec = lecs[i]
    body, _ = decorate(add_section_ids(fix_assets(lec.get("html", ""), "../../")))
    outline = lecture_outline(body)
    src = source_panel(c, lec, SOURCE_CATALOGUE)
    head = ['<header class="lecture-head"><p class="lecture-kicker">%s · 第 %02d / %02d 讲</p>'
            % (html.escape(c.get("name_zh", c.get("id", ""))), i + 1, len(lecs))]
    head.append('<h1 id="lecture-title">%s</h1>' % html.escape(lec.get("title_zh", "")))
    if lec.get("title_en"):
        head.append('<p class="lecture-subtitle">%s</p>' % html.escape(lec["title_en"]))
    part_name = lec.get("part") or "未分章"
    part_i = next((pi for pi, (n, _) in enumerate(parts_of(c)) if n == part_name), 0)
    head.append(
        '<p class="chaptertag">所属章节：<a href="%s.html">%s</a></p>'
        % (part_slug(part_i), html.escape(part_name))
    )
    head.append(src)
    head.append(lecture_controls())
    head.append('</header>')
    nav = sequence_navigation(
        (lecs[i - 1]["slug"] + ".html", lecs[i - 1]["title_zh"]) if i else None,
        (part_slug(part_i) + ".html", part_name),
        (lecs[i + 1]["slug"] + ".html", lecs[i + 1]["title_zh"]) if i + 1 < len(lecs) else None,
        "讲",
    )
    art = '<article aria-labelledby="lecture-title" data-lecture-id="%s">' % html.escape(c["id"] + "/" + lec["slug"], quote=True) + "".join(head) + body + nav + "</article>"
    crumb = [("课程总览", "../../index.html"), (c.get("name_zh", c["id"]), "index.html"),
             (part_name, part_slug(part_i) + ".html"), (lec.get("title_zh", ""), None)]
    return page(
        "%s · %s" % (lec.get("title_zh", ""), c.get("id", "")),
        art,
        "../../",
        crumb,
        cls="lecture-page",
        script=LECTURE_JS,
        groups=[("本页内容", outline), ("课程目录", course_tree(c, lec["slug"] + ".html", parts_of(c)))],
    )


def parts_of(c):
    """按 part 字段聚合同一章的讲次（允许跨位置归并），章节按首次出现排序。"""
    order = []
    bucket = {}
    for i, l in enumerate(c.get("lectures", [])):
        name = l.get("part") or "未分章"
        if name not in bucket:
            bucket[name] = []
            order.append(name)
        bucket[name].append((i, l))
    return [(n, bucket[n]) for n in order]


def part_slug(i):
    return "part-%d" % (i + 1)


def lec_card(l, course_id=""):
    kw = l.get("keywords") or []
    chips = "".join('<span class="chip">%s</span>' % html.escape(k) for k in kw[:8])
    ov = section(l.get("html", ""), "overview")
    return (
        '<div class="card" id="preview-%s"><h3><a href="%s.html">%s</a>%s</h3>'
        '<p class="lead">%s</p>%s%s</div>'
        % (
            html.escape(l.get("slug", ""), quote=True),
            l.get("slug"),
            html.escape(l.get("title_zh", "")),
            '<span class="study-state" data-study-id="%s">未开始</span>' % html.escape(course_id + "/" + l["slug"], quote=True) if course_id else "",
            html.escape(l.get("title_en", "")),
            ("<p>" + html.escape(plain_text(ov, 200)) + "</p>") if ov else "",
            ("<p>" + chips + "</p>") if chips else "",
        )
    )


def course_info(c, lecs, nparts):
    info = []
    if c.get("name_en"):
        info.append(html.escape(c["name_en"]))
    info.append('<span class="badge mute">%s</span>' % html.escape(c.get("id", "")))
    info.append('<span class="badge mute">%d 章 · %d 讲</span>' % (nparts, len(lecs)))
    if c.get("source_dir"):
        info.append('<span class="badge mute">%s</span>' % html.escape(c["source_dir"]))
    return " ".join(info)


def build_course(c):
    lecs = c.get("lectures", [])
    parts = parts_of(c)
    blocks = []
    for pi, (name, items) in enumerate(parts):
        rows = "".join(lec_card(l, c["id"]) for _, l in items)
        blocks.append(
            '<div class="chapter"><h2 id="p-%s"><a href="%s.html">%s</a> '
            '<span class="badge mute">%d 讲</span></h2>%s</div>'
            % (pi + 1, part_slug(pi), html.escape(name), len(items), rows)
        )
    parts_meta = json.dumps(
        [{"index": pi + 1, "slug": part_slug(pi), "name": name} for pi, (name, _) in enumerate(parts)],
        ensure_ascii=False,
    )
    source_panel_box = (
        '<section class="card cw-panel" id="course-source-files" data-course="%s">'
        '<details><summary>本课原始课件总表（PDF / PPTX / DOCX / 代码 / 音视频 · 按文件名或类型查询）</summary>'
        '<div class="cw-panel-body"><p class="sub">展开以加载本课原始课件列表与讲义对照。</p></div></details></section>'
        % html.escape(c.get("id", ""), quote=True)
    )
    upload_panel = (
        '<section class="card mat-panel" id="course-materials" data-course="%s" data-parts="%s">'
        '<div class="mat-empty">正在加载本课实时资料库…</div></section>'
        % (html.escape(c.get("id", ""), quote=True), html.escape(parts_meta, quote=True))
    )
    body = (
        '<h1>%s</h1><p class="lead">%s</p>%s%s'
        '<nav class="related-nav" aria-label="本课关联页面"><a href="../../review.html#r-%s">本课考点清单 →</a> '
        '<a href="../../extend.html#e-%s">本课知识拓展 →</a> '
        '<a href="reader.html#c-%s">本课合订本 →</a> '
        '<a href="#course-source-files">本课原始课件 ↓</a></nav>%s%s%s'
        % (
            html.escape(c.get("name_zh", c.get("id", ""))),
            course_info(c, lecs, len(parts)),
            ("<p>%s</p>" % html.escape(c.get("summary", "")))
            if c.get("summary")
            else "",
            course_progress(c["id"],len(lecs)),
            html.escape(c.get("id", "")),
            html.escape(c.get("id", "")),
            html.escape(c.get("id", "")),
            "".join(blocks),
            source_panel_box,
            upload_panel,
        )
    )
    crumb = [("课程总览", "../../index.html"), (c.get("name_zh", c["id"]), None)]
    outline = [NavItem(name, "#p-%d" % (pi + 1)) for pi, (name, _) in enumerate(parts)]
    outline.append(NavItem("本课原始课件", "#course-source-files"))
    outline.append(NavItem("实时资料与上传", "#course-materials"))
    mat_scripts = '<script src="../../assets/sharing-config.js"></script><script src="../../assets/materials.js"></script>'
    return page(
        "%s · 课程讲义" % c.get("name_zh", c.get("id", "")),
        body,
        "../../",
        crumb,
        script=mat_scripts,
        groups=[("本页内容", outline), ("课程目录", course_tree(c, "index.html", parts))],
    )


def build_part(c, pi):
    parts = parts_of(c)
    name, items = parts[pi]
    rows = "".join(lec_card(l, c["id"]) for _, l in items)
    nav = sequence_navigation(
        (part_slug(pi - 1) + ".html", parts[pi - 1][0]) if pi else None,
        ("index.html", c.get("name_zh", c["id"])),
        (part_slug(pi + 1) + ".html", parts[pi + 1][0]) if pi + 1 < len(parts) else None,
        "章",
    )
    upload_panel = (
        '<section class="card mat-panel" id="chapter-materials" data-course="%s" data-part="%d" data-part-name="%s">'
        '<div class="mat-empty">正在加载本章节实时资料…</div></section>'
        % (
            html.escape(c.get("id", ""), quote=True),
            pi + 1,
            html.escape(name, quote=True),
        )
    )
    body = (
        "<h1>%s</h1>"
        '<p class="lead">%s <span class="badge mute">%s</span></p>'
        '<h2 id="chapter-lectures">%s</h2>%s%s%s'
        % (
            html.escape(name),
            html.escape(c.get("name_zh", c.get("id", ""))),
            course_info(c, c.get("lectures", []), len(parts)),
            html.escape(name),
            rows,
            upload_panel,
            nav,
        )
    )
    crumb = [("课程总览", "../../index.html"), (c.get("name_zh", c["id"]), "index.html"), (name, None)]
    outline = [NavItem("本章讲义", "#chapter-lectures", tuple(
        NavItem(l.get("title_zh", ""), "#preview-" + l["slug"]) for _, l in items)),
        NavItem("补充资料与上传", "#chapter-materials")]
    mat_scripts = '<script src="../../assets/sharing-config.js"></script><script src="../../assets/materials.js"></script>'
    return page(
        "%s · %s" % (name, c.get("name_zh", "")),
        body,
        "../../",
        crumb,
        script=mat_scripts,
        groups=[("本页内容", outline), ("课程目录", course_tree(c, part_slug(pi) + ".html", parts))],
    )


COURSE_CATEGORIES = [
    ("cs", "编程与软件", {"30352", "30361", "30332", "86"}),
    ("math", "数学与工程", {"30565", "62", "80"}),
    ("lang", "语言课程", {"33295", "34583", "32667", "32632"}),
    ("general", "通识与导论", {"29911", "29913", "30331", "29428"}),
]


def course_category(cid):
    cid = str(cid)
    for key, label, ids in COURSE_CATEGORIES:
        if cid in ids:
            return key, label
    return "general", "通识与导论"


def build_root(courses):
    mf = manifest_files()
    total_lec = sum(len(c.get("lectures", [])) for c in courses)
    total_parts = sum(len(parts_of(c)) for c in courses)
    src_total = sum(len(v) for v in mf.values())
    cat_counts = {key: 0 for key, _, _ in COURSE_CATEGORIES}
    cards = []
    for c in courses:
        lecs = c.get("lectures", [])
        cid = c["id"]
        parts = parts_of(c)
        cat_key, cat_label = course_category(cid)
        cat_counts[cat_key] = cat_counts.get(cat_key, 0) + 1
        chapters = []
        for pi, (name, items) in enumerate(parts):
            rows = []
            for _, l in items:
                kw = " ".join((l.get("keywords") or [])[:10])
                s = (
                    c.get("id", "")
                    + " "
                    + c.get("name_zh", "")
                    + " "
                    + name
                    + " "
                    + l.get("title_zh", "")
                    + " "
                    + l.get("title_en", "")
                    + " "
                    + " ".join(l.get("source_files") or [])
                    + " "
                    + kw
                ).lower()
                rows.append(
                    '<li data-s="%s"><a class="t" href="c/%s/%s.html">%s</a><span class="study-state" data-study-id="%s">未开始</span></li>'
                    % (
                        html.escape(s, quote=True),
                        cid,
                        l.get("slug"),
                        html.escape(l.get("title_zh", "")),
                        html.escape(cid + "/" + l["slug"], quote=True),
                    )
                )
            chapters.append(
                '<li class="ch" data-s="%s"><div class="ch-head"><a class="ch-t" href="c/%s/%s.html">%s</a>'
                '<span class="n">%d 讲</span></div><ul class="lec-list">%s</ul></li>'
                % (
                    html.escape((cid + " " + name).lower(), quote=True),
                    cid,
                    part_slug(pi),
                    html.escape(name),
                    len(items),
                    "".join(rows),
                )
            )
        summary = c.get("summary") or ""
        cards.append(
            '<article class="ccard" id="c-%s" data-category="%s">'
            '<div class="ccard-top"><span class="badge mute">%s</span><span class="badge ccard-cat">%s</span></div>'
            '<h3><a href="c/%s/index.html">%s</a></h3>'
            '<div class="meta">%s%d 章 · %d 讲</div>'
            '%s%s'
            '<div class="ccard-actions"><a class="ccard-link primary" href="c/%s/index.html">进入课程 →</a>'
            '<a class="ccard-link" href="review.html#r-%s">考点清单</a>'
            '<a class="ccard-link" href="c/%s/reader.html">合订本</a></div>'
            '<details class="ccard-chapters"><summary>展开章节与讲次目录（%d 章 · %d 讲）</summary><ul class="chapters">%s</ul></details></article>'
            % (
                cid,
                cat_key,
                html.escape(cid),
                html.escape(cat_label),
                cid,
                html.escape(c.get("name_zh", cid)),
                (html.escape(c.get("name_en", "")) + " · ") if c.get("name_en") else "",
                len(parts),
                len(lecs),
                ('<p class="ccard-summary">%s</p>' % html.escape(plain_text(summary, 90))) if summary else "",
                course_progress(cid, len(lecs)),
                cid,
                cid,
                cid,
                len(parts),
                len(lecs),
                "".join(chapters),
            )
        )
    cat_buttons = ['<button type="button" class="filter-pill is-active" data-cat="all" aria-pressed="true">全部课程 <span>%d</span></button>' % len(courses)]
    for key, label, _ in COURSE_CATEGORIES:
        if cat_counts.get(key):
            cat_buttons.append(
                '<button type="button" class="filter-pill" data-cat="%s" aria-pressed="false">%s <span>%d</span></button>'
                % (key, html.escape(label), cat_counts[key])
            )
    cat_buttons.append('<button type="button" class="filter-pill" data-cat="pending" aria-pressed="false">未学完</button>')
    filter_bar = (
        '<div class="course-section-head" id="course-catalog">'
        '<h2>全部课程</h2>'
        '<div class="course-filter-bar" id="course-filter-bar" role="group" aria-label="课程分类筛选">'
        '<div class="filter-pills">%s</div>'
        '<button type="button" class="study-button compact" id="toggle-all-chapters" aria-expanded="false">展开全部章节</button>'
        '</div></div>' % "".join(cat_buttons)
    )
    courseware_box = (
        '<details class="card cw-home" id="courseware-hub">'
        '<summary>原版课件源头速查（支持按课程 / 文件名 / 扩展名检索，反查对应讲义或直开云端原件）</summary>'
        '<div class="cw-panel-body"><p class="sub">展开以按需加载全站原始课件索引（PDF / PPTX / DOCX / 音频 / 代码）。</p></div>'
        '</details>'
    )
    body = (
        '<header class="home-hero"><div class="home-hero-main">'
        "<h1>课程讲义总览</h1>"
        '<p class="lead">按「课程 → 章节 → 讲次」三级组织，支持离线全文搜索、学习进度追踪、原版课件溯源与考前分层复习。点击搜索图标或按 <kbd>Ctrl K</kbd> 可随时快捷查找。</p></div>'
        '<div class="stats"><div class="stat"><b>%d</b><span>门课程</span></div>'
        '<div class="stat"><b>%d</b><span>个章节</span></div>'
        '<div class="stat"><b>%d</b><span>讲讲义</span></div>'
        '<div class="stat"><b>%d</b><span>个原始文件</span></div></div></header>'
        '%s'
        '%s<div class="courses">%s</div>'
        '<section class="home-search-tools" aria-label="全文搜索与原版课件">%s%s</section>'
        '<details class="howto"><summary>后续如何补充新的讲义页（扩展说明）</summary>'
        '<ol class="steps">'
        "<li>已有课程加一讲：在 <code>content/&lt;课程ID&gt;.json</code> 的 <code>lectures</code> 数组末尾追加一个对象，"
        "必须含 8 个 section：<code>overview / detail / keywords / examples / practice / exam / checklist / mapping</code>，"
        "并写 <code>part</code> 指定所属章节（同名 part 会自动归入同一章）。</li>"
        "<li>新增一门课：新建 <code>content/&lt;新ID&gt;.json</code>，写 <code>id / order / name_zh / name_en / source_dir / summary / lectures</code>。</li>"
        "<li>在 <code>study-site</code> 目录运行 <code>python build.py</code>；再用 <code>python build.py --check</code> 确认 8 个板块齐全。</li>"
        "<li>新讲会自动出现在总览、课程页、章节页、期末考点清单与合订本里，不必手改任何 HTML；页面仍是单文件、可离线打开。</li>"
        "</ol></details>"
        % (
            len(courses),
            total_parts,
            total_lec,
            src_total,
            home_widgets(courses),
            filter_bar,
            "".join(cards),
            search_box(courses),
            courseware_box,
        )
    )
    return page(
        "课程讲义总览",
        body,
        "",
        [("课程总览", None)],
        script='<script src="assets/search.js"></script>',
        groups=[("本页内容", [NavItem("继续学习与错题", "#study-dashboard")]
                 + [NavItem(c.get("name_zh", c["id"]), "#c-" + c["id"]) for c in courses]
                 + [NavItem("全文搜索", "#site-search"), NavItem("原版课件速查", "#courseware-hub")])],
    )


def build_allinone(courses, prefix=""):
    total = sum(len(c.get("lectures", [])) for c in courses)
    total_parts = sum(len(parts_of(c)) for c in courses)
    outline, parts = [], []
    for c in courses:
        cid = c.get("id", "")
        name = c.get("name_zh", cid)
        lecs = c.get("lectures", [])
        chapters = parts_of(c)
        sub = []
        for pi, (pname, items) in enumerate(chapters):
            sub.append(NavItem(pname, "#p-%s-%d" % (cid, pi + 1), tuple(
                NavItem(l.get("title_zh", ""), "#l-%s-%s" % (cid, l["slug"])) for _, l in items)))
        outline.append(NavItem(name, "#c-" + cid, tuple(sub)))
        parts.append(
            '<section class="allcourse" id="c-%s"><h1>%s</h1>'
            '<p class="lead">%s · %d 章 · %d 讲</p></section>'
            % (
                html.escape(cid),
                html.escape(name),
                html.escape(c.get("summary", "") or c.get("name_en", "")),
                len(chapters),
                len(lecs),
            )
        )
        for pi, (pname, items) in enumerate(chapters):
            parts.append(
                '<h2 class="allpart" id="p-%s-%d">%s <span class="badge mute">%d 讲</span> '
                '<a class="sub" href="c/%s/%s.html">章节页 →</a></h2>'
                % (
                    html.escape(cid),
                    pi + 1,
                    html.escape(pname),
                    len(items),
                    html.escape(cid),
                    part_slug(pi),
                )
            )
            for _, l in items:
                parts.append(
                    '<article class="alllec" id="l-%s-%s">'
                    '<h3>%s</h3><p class="lead">%s <span class="badge mute">%s</span></p>%s'
                    '<p class="sub">返回：<a href="c/%s/%s.html">本讲独立页</a> · '
                    '<a href="c/%s/%s.html">本章节页</a> · <a href="#c-%s">本课目录</a></p></article>'
                    % (
                        html.escape(cid),
                        html.escape(l.get("slug", "")),
                        html.escape(l.get("title_zh", "")),
                        html.escape(l.get("title_en", "") or ""),
                        html.escape(pname),
                        fix_assets(l.get("html", ""), ""),
                        html.escape(cid),
                        html.escape(l.get("slug", "")),
                        html.escape(cid),
                        part_slug(pi),
                        html.escape(cid),
                    )
                )
    body = (
        "<h1>全站合订本 · 全部课程逐讲讲义</h1>"
        '<p class="lead">%d 门课 / %d 章 / %d 讲，按「课程 → 章节」顺序连排；每章有标题，'
        "每讲之后可直接跳回独立页或章节页。适合通读、打印、离线放到手机里看。</p>%s"
        % (len(courses), total_parts, total, "".join(parts))
    )
    if prefix:
        body = body.replace('全站合订本 · 全部课程逐讲讲义', html.escape(courses[0].get('name_zh', courses[0]['id'])) + ' · 课程合订本')
        body = body.replace('href="c/', 'href="' + prefix + 'c/')
        body = fix_assets(body, prefix)
    else:
        links = ''.join('<a class="reader-pill" href="c/%s/reader.html"><span>%s</span><em>%d 讲</em></a>' % (html.escape(c['id']), html.escape(c.get('name_zh', c['id'])), len(c['lectures'])) for c in courses)
        body = ('<section class="card reader-quickbar"><h2>按单门课程阅读（页面更轻，加载更快）</h2>'
                '<p class="sub">全站合订本包含全部 15 门课（约 4 MB）；日常复习推荐直接点下方单课合订本（每课 110–590 KB）：</p>'
                '<div class="reader-pill-grid">' + links + '</div></section>') + body
    body = reading_controls() + body
    return page(
        "课程合订本" if prefix else "全站合订本 · 课程讲义",
        body,
        prefix,
        [("课程总览", prefix + "index.html"), ("课程合订本" if prefix else "全站合订本", None)],
        module="reader",
        groups=[("本页内容", outline)],
    )


REVIEW_JS = """<script>
(function(){
  var boxes=Array.from(document.querySelectorAll('input.tick')),out=document.getElementById('tickprog');
  var app=window.LUTLearning,legacy={};
  try{legacy=JSON.parse(localStorage.getItem('lut-review-v1')||'{}')||{};}catch(e){}
  function refresh(){
    boxes.forEach(function(box){box.checked=app?app.store.getLecture(box.dataset.studyId).status==='mastered':!!legacy[box.dataset.k];});
    if(out)out.textContent='已复习 '+boxes.filter(function(box){return box.checked;}).length+' / '+boxes.length+' 讲';
  }
  boxes.forEach(function(box){box.addEventListener('change',function(){
    if(app)app.commit(app.store.setLecture(box.dataset.studyId,{status:box.checked?'mastered':'review'}));
    else{legacy[box.dataset.k]=box.checked;try{localStorage.setItem('lut-review-v1',JSON.stringify(legacy));}catch(e){}}
    refresh();
  });});
  addEventListener('lut:learning-changed',refresh);refresh();
})();
</script>"""


def _demote(block):
    def up(m):
        return "<h%d%s>" % (min(int(m.group(1)) + 1, 4), m.group(2) or "")

    def down(m):
        return "</h%d>" % min(int(m.group(1)) + 1, 4)

    block = re.sub(r"<h([234])([^>]*)>", up, block or "")
    return re.sub(r"</h([234])>", down, block)


def build_review(courses):
    total = sum(len(c.get("lectures", [])) for c in courses)
    quick, sections, outline = [], [], [NavItem("复习进度总表", "#review-progress")]
    for c in courses:
        cid = c.get("id", "")
        name = c.get("name_zh", cid)
        lecs = c.get("lectures", [])
        chapters = parts_of(c)
        quick.append(
            '<div class="qcourse" data-course="%s"><div class="qhead"><a class="qhead-title" href="#r-%s">%s</a>'
            '<span class="qhead-badges"><span class="badge ok qcourse-done">0 / %d 已复习</span><span class="badge mute">%d 章</span></span></div><ul class="chapters-tick">'
            % (html.escape(cid, quote=True), html.escape(cid, quote=True), html.escape(name), len(lecs), len(chapters))
        )
        for pi, (pname, items) in enumerate(chapters):
            quick.append(
                '<li><span class="qp">%s</span><ul class="ticklist">' % html.escape(pname)
            )
            for gi, l in items:
                key = "%s-%s" % (cid, l.get("slug", "lec-%d" % (gi + 1)))
                quick.append(
                    '<li><label><input type="checkbox" class="tick" data-k="%s" data-study-id="%s"> %s</label></li>'
                    % (html.escape(key), html.escape(cid + "/" + l["slug"],quote=True), html.escape(l.get("title_zh", "")))
                )
            quick.append("</ul></li>")
        quick.append("</ul></div>")

        blocks, chapter_links = [], []
        for pi, (pname, items) in enumerate(chapters):
            chapter_links.append(NavItem(pname, "#rp-%s-%d" % (cid, pi + 1), tuple(
                NavItem(l.get("title_zh", ""), "#r-%s-%s" % (cid, l["slug"]))
                for _, l in items if section(l.get("html", ""), "exam").strip())))
            blocks.append(
                '<div class="revpart" id="rp-%s-%d"><a href="c/%s/%s.html">%s</a>'
                '<span class="badge mute">%d 讲</span></div>'
                % (html.escape(cid), pi + 1, html.escape(cid), part_slug(pi), html.escape(pname), len(items))
            )
            for gi, l in items:
                slug = l.get("slug", "lec-%d" % (gi + 1))
                exam = _demote(section(l.get("html", ""), "exam"))
                chk = section(l.get("html", ""), "checklist")
                if not exam.strip():
                    continue
                body = [
                    '<div class="revlec" id="r-%s-%s" data-study-id="%s">'
                    % (html.escape(cid), html.escape(slug), html.escape(cid + "/" + slug, quote=True))
                ]
                body.append(
                    '<h4><a href="c/%s/%s.html">%s</a> <span class="badge mute">第 %d 讲</span>'
                    ' <span class="badge mute">%s</span></h4>'
                    % (
                        html.escape(cid),
                        html.escape(slug),
                        html.escape(l.get("title_zh", "")),
                        gi + 1,
                        html.escape(l.get("title_en", "") or ""),
                    )
                )
                body.append('<div class="revbody">' + exam + "</div>")
                if chk.strip():
                    body.append(
                        '<details><summary>方法清单 / Method checklist</summary><div class="ans">%s</div></details>'
                        % chk
                    )
                body.append(
                    '<p class="src"><a href="c/%s/%s.html">回本讲完整讲义 →</a></p>'
                    % (html.escape(cid), html.escape(slug))
                )
                body.append("</div>")
                blocks.append("".join(body))
        outline.append(NavItem(name, "#r-" + cid, tuple(chapter_links)))
        sections.append(
            '<section class="revcourse" id="r-%s"><h2>%s <span class="badge mute">%s</span></h2>%s</section>'
            % (html.escape(cid), html.escape(name), html.escape(cid), "".join(blocks))
        )
    course_opts = '<option value="">全部课程</option>' + ''.join(
        '<option value="%s">%s</option>' % (html.escape(str(c['id']), quote=True), html.escape(c.get('name_zh', c['id'])))
        for c in courses
    )
    rev_filter = (
        '<section class="card filter-toolbar" id="review-filter-bar" aria-label="考点筛选工具">'
        '<div class="filter-toolbar-row">'
        '<div class="filter-pills" role="group" aria-label="按重要程度筛选">'
        '<button type="button" class="filter-pill is-active" data-rev-mode="all" aria-pressed="true">全部考点</button>'
        '<button type="button" class="filter-pill pill-bad" data-rev-mode="must" aria-pressed="false">仅看必考</button>'
        '<button type="button" class="filter-pill pill-warn" data-rev-mode="warn" aria-pressed="false">仅看易错</button>'
        '<button type="button" class="filter-pill" data-rev-mode="adv" aria-pressed="false">仅看进阶</button>'
        '</div>'
        '<div class="filter-controls">'
        '<label class="filter-select-label"><span>课程</span><select id="review-course-filter">%s</select></label>'
        '<label class="filter-check"><input type="checkbox" id="review-only-unreviewed"><span>仅看未复习</span></label>'
        '</div></div>'
        '<p class="sub filter-status" id="review-filter-status" role="status"></p></section>' % course_opts
    )
    body = (
        "<h1>期末总复习 · 考点提醒清单</h1>"
        '<p class="lead">把每门课每一讲的「考点与难点」「方法清单」集中到一页：支持按必考、易错、进阶、课程与未复习状态一键过滤，'
        '适配考前 3 天扫盲、考前 1 天只看<span class="badge warn">易错</span>、考前 1 小时只看<span class="badge bad">必考</span>。</p>'
        '<div class="stats"><div class="stat"><b>%d</b><span>门课</span></div>'
        '<div class="stat"><b>%d</b><span>讲</span></div>'
        '<div class="stat"><b id="tickprog">已复习 0 / 0 讲</b><span>复习进度（本地保存）</span></div></div>'
        '%s'
        '<details class="review-matrix" open><summary><span id="review-progress">复习进度总表（点击可收起）</span></summary>'
        '<div class="qgrid">%s</div></details>'
        "<h2>逐讲考点与难点</h2>%s"
        % (len(courses), total, rev_filter, "".join(quick), "".join(sections))
    )
    return page(
        "期末总复习 · 考点提醒清单",
        body,
        "",
        [("课程总览", "index.html"), ("期末考点清单", None)],
        script=REVIEW_JS,
        module="review",
        groups=[("本页内容", outline)],
    )


def build_extension(courses):
    """知识拓展专页：汇总所有讲义里的「拓展」提示框与 mapping 中标注的补充内容。"""
    outline, blocks, total_idea, total_note = [], [], 0, 0
    for c in courses:
        cid = c.get("id", "")
        name = c.get("name_zh", cid)
        idea_rows, note_rows = [], []
        for l in c.get("lectures", []):
            slug = l.get("slug", "")
            tzh = l.get("title_zh", "")
            seen_boxes = set()
            for m in re.finditer(
                r'<div class="callout[^">]*"(?:\s[^>]*)?>.*?</div>',
                l.get("html", ""), flags=re.S
            ):
                box = m.group(0)
                if '<b>' not in box:
                    continue
                if 'data-ext=' not in box and 'class="callout idea"' not in box:
                    continue
                if box in seen_boxes:
                    continue
                seen_boxes.add(box)
                idea_rows.append((tzh, slug, box))
            mp = section(l.get("html", ""), "mapping")
            for m in re.finditer(r"<tr>.*?</tr>", mp, flags=re.S):
                row = m.group(0)
                if re.search(r"补充|拓展", re.sub(r"<[^>]+>", "", row)):
                    note_rows.append((tzh, slug, row))
        if not idea_rows and not note_rows:
            continue
        total_idea += len(idea_rows)
        total_note += len(note_rows)
        children = []
        if idea_rows:
            children.append(NavItem("课内拓展提示框", "#e-%s-ideas" % cid))
        if note_rows:
            children.append(NavItem("补充内容与原始文件对照", "#e-%s-notes" % cid))
        outline.append(NavItem(name, "#e-" + cid, tuple(children)))
        parts = [
            '<section class="revcourse" id="e-%s"><h2>%s <span class="badge mute">%s</span></h2>'
            % (html.escape(cid), html.escape(name), html.escape(cid))
        ]
        if idea_rows:
            parts.append('<div class="revpart" id="e-%s-ideas">课内拓展提示框</div>' % html.escape(cid))
            for tzh, slug, box in idea_rows:
                parts.append(
                    '<div class="extidea"><div class="extsrc"><a href="c/%s/%s.html">%s</a></div>%s</div>'
                    % (
                        html.escape(cid),
                        html.escape(slug),
                        html.escape(tzh),
                        box,
                    )
                )
        if note_rows:
            parts.append(
                '<div class="revpart" id="e-%s-notes">mapping 中标注的补充 / 拓展内容（对照原始文件）</div>'
                '<table><tr><th>出处讲次</th><th>源文件 / 位置</th><th>补充说明</th></tr>'
                % html.escape(cid)
            )
            for tzh, slug, row in note_rows:
                cells = re.findall(r"<td.*?</td>", row, flags=re.S)
                lead = (
                    '<td><a href="c/%s/%s.html">%s</a></td>'
                    % (html.escape(cid), html.escape(slug), html.escape(tzh))
                )
                parts.append("<tr>" + lead + "".join(cells[1:]) + "</tr>")
            parts.append("</table>")
        parts.append(
            '<p class="src"><a href="c/%s/index.html">回到 %s 课程页 →</a></p>'
            % (html.escape(cid), html.escape(name))
        )
        parts.append("</section>")
        blocks.append("".join(parts))
    total_courses = len(blocks)
    ext_opts = '<option value="">全部课程</option>' + ''.join(
        '<option value="%s">%s</option>' % (html.escape(str(c['id']), quote=True), html.escape(c.get('name_zh', c['id'])))
        for c in courses if any(nav.href == "#e-" + str(c['id']) for nav in outline)
    )
    ext_filter = (
        '<section class="card filter-toolbar" id="extend-filter-bar" aria-label="拓展筛选工具">'
        '<div class="filter-toolbar-row">'
        '<div class="filter-pills" role="group" aria-label="按内容类型筛选">'
        '<button type="button" class="filter-pill is-active" data-ext-kind="all" aria-pressed="true">全部拓展</button>'
        '<button type="button" class="filter-pill" data-ext-kind="ideas" aria-pressed="false">仅看课内拓展框</button>'
        '<button type="button" class="filter-pill" data-ext-kind="notes" aria-pressed="false">仅看 mapping 补充</button>'
        '</div>'
        '<div class="filter-controls">'
        '<label class="filter-select-label"><span>课程</span><select id="extend-course-filter">%s</select></label>'
        '</div></div>'
        '<p class="sub filter-status" id="extend-filter-status" role="status"></p></section>' % ext_opts
    )
    body = (
        "<h1>知识拓展 · 全站汇总</h1>"
        '<p class="lead">把 %d 门课讲义里所有「拓展」提示框（背景知识、推导、常见误解、前后衔接）与 '
        "mapping 板块标注的补充内容集中到一页：先看拓展框加深理解，再按 mapping 回原讲义核对边界——"
        "拓展不引入原文没有的新考点，凡是补充都会标明出处。</p>"
        '<div class="stats"><div class="stat"><b>%d</b><span>门课有拓展</span></div>'
        '<div class="stat"><b>%d</b><span>个拓展框</span></div>'
        '<div class="stat"><b>%d</b><span>条 mapping 补充</span></div></div>'
        '%s%s'
        % (len(courses), total_courses, total_idea, total_note, ext_filter, "".join(blocks))
    )
    return page(
        "知识拓展 · 全站汇总",
        body,
        "",
        [("课程总览", "index.html"), ("知识拓展", None)],
        module="extension",
        groups=[("本页内容", outline)],
    )


def build_upload(courses):
    total_parts = sum(len(parts_of(c)) for c in courses)
    body = (
        '<h1 id="upload-intro">实时资料上传中心 · Upload Center</h1>'
        '<p class="lead">支持按「课程 → 章节」上传 PDF / PPTX / DOCX / 图片 / 代码文件，或直接撰写 Markdown 补充笔记。'
        "连接云端后可共享到对应章节；本机预览模式仅自己可见。</p>"
        '<details class="card" id="courseware-cloud"><summary>云端原始课件库配置（推荐 Cloudflare R2 · 兼容 GCS / S3）</summary>'
        '<p class="sub">原始课件（820 份去隐私后的公开课件，约 656 MB）推荐托管在 <strong>Cloudflare R2</strong>（每月 10 GB 免费 + 永久 0 流量费），网页继续托管在 GitHub Pages。按 <code>SETUP_R2.md</code> 同步后填入公开前缀地址即可全站直开原件。</p>'
        '<div class="study-filters"><label>云端课件公开前缀地址（HTTPS）<input id="gcs-base-url" type="url" placeholder="https://pub-xxxxxxxxxxxxxxxx.r2.dev/courseware" autocomplete="off" spellcheck="false"></label></div>'
        '<div class="reader-actions"><button class="study-button" type="button" id="gcs-test">抽检云端课件连接</button>'
        '<button class="study-button primary" type="button" id="gcs-save">保存本机生效并刷新</button>'
        '<button class="study-button" type="button" id="gcs-reset">清除本机覆盖</button></div>'
        '<p id="gcs-status" role="status" class="sub"></p>'
        '<p class="sub">全站生效请写入 <code>assets/config.js</code>：<code id="gcs-config-snippet"></code></p></details>'
        '<details class="card" id="sharing-setup"><summary>共享连接设置与检查</summary>'
        '<p>维护者先运行 supabase/schema.sql。这里只填写项目地址和公开客户端密钥，设置仅作用于当前浏览器；全站启用请填写 assets/config.js 后部署。</p>'
        '<div class="study-filters"><label>Supabase 项目地址<input id="sharing-url" type="url" placeholder="https://project.supabase.co" autocomplete="off" spellcheck="false"></label>'
        '<label>公开 publishable / anon 密钥<input id="sharing-key" type="password" autocomplete="off" spellcheck="false"></label></div>'
        '<div class="reader-actions"><button class="study-button" type="button" id="sharing-test">只读检查连接</button>'
        '<button class="study-button primary" type="button" id="sharing-save" disabled>保存本机连接并刷新</button>'
        '<button class="study-button" type="button" id="sharing-reset">清除本机覆盖设置</button></div>'
        '<p id="sharing-status" role="status" class="sub"></p></details>'
        '<div id="upload-hub"><div class="mat-empty">正在加载课程与章节目录…</div></div>'
    )
    mat_scripts = '<script src="assets/sharing-config.js"></script><script src="assets/materials.js"></script>'
    return page(
        "实时资料上传中心 · 课程讲义站",
        body,
        "",
        [("课程总览", "index.html"), ("上传资料", None)],
        script=mat_scripts,
        module="upload",
        groups=[("本页内容", [NavItem("上传说明", "#upload-intro"), NavItem("云端课件库配置", "#courseware-cloud"), NavItem("课程与章节资料", "#upload-hub")])],
    )


def build_catalog_json(courses):
    catalog = []
    for c in courses:
        catalog.append(
            {
                "id": c.get("id", ""),
                "name_zh": c.get("name_zh", c.get("id", "")),
                "name_en": c.get("name_en", ""),
                "parts": [
                    {
                        "index": pi + 1,
                        "slug": part_slug(pi),
                        "name": name,
                        "lecture_count": len(items),
                    }
                    for pi, (name, items) in enumerate(parts_of(c))
                ],
            }
        )
    write(
        os.path.join(ROOT, "data", "catalog.json"),
        json.dumps(catalog, ensure_ascii=False, indent=2),
    )


def build_uploads_json(courses):
    """Scan static uploads/<course_id>/part-<N>/* in repo and write data/uploads.json."""
    part_names = {}
    for c in courses:
        cid = str(c.get("id", ""))
        for pi, (name, _) in enumerate(parts_of(c)):
            part_names[(cid, pi + 1)] = name

    uploads_root = os.path.join(ROOT, "uploads")
    items = []
    if os.path.isdir(uploads_root):
        for root_dir, _, files in os.walk(uploads_root):
            for fn in sorted(files):
                if fn.startswith(".") or fn.lower() == "readme.md":
                    continue
                full = os.path.join(root_dir, fn)
                rel = os.path.relpath(full, ROOT).replace("\\", "/")
                segs = rel.split("/")
                if len(segs) < 4:
                    continue
                cid = segs[1]
                m = re.match(r"part-(\d+)$", segs[2])
                if not m:
                    continue
                pi = int(m.group(1))
                st = os.stat(full)
                items.append(
                    {
                        "id": "repo-" + rel,
                        "course_id": cid,
                        "part_index": pi,
                        "part_name": part_names.get((cid, pi), "Part %d" % pi),
                        "title": os.path.splitext(fn)[0],
                        "description": "仓库静态同步资料",
                        "kind": "file",
                        "file_name": fn,
                        "file_path": rel,
                        "file_size": st.st_size,
                        "uploader": "GitHub Repo",
                        "created_at": datetime.datetime.fromtimestamp(
                            st.st_mtime, datetime.timezone.utc
                        ).isoformat(),
                    }
                )
    write(
        os.path.join(ROOT, "data", "uploads.json"),
        json.dumps(items, ensure_ascii=False, indent=2),
    )


def check(courses):
    bad = 0
    for c in courses:
        for l in c.get("lectures", []):
            have = re.findall(r'data-type="([a-z]+)"', l.get("html", ""))
            miss = [k for k in REQUIRED if k not in have]
            flag = "OK  " if not miss else "缺失"
            if miss:
                bad += 1
            print(
                "[%s] %s / %s  缺少: %s"
                % (
                    flag,
                    c.get("id"),
                    l.get("title_zh"),
                    ",".join(miss) if miss else "-",
                )
            )
    print(
        "\n共 %d 篇讲义，%d 篇不完整"
        % (sum(len(c.get("lectures", [])) for c in courses), bad)
    )
    return bad


def build_learning_assets(courses):
    data = build_search_data(courses, lambda body: decorate(add_section_ids(body))[0])
    catalogue = {key:data[key] for key in ("version", "courses", "lectures")}
    write(os.path.join(ROOT,"data","learning-catalog.js"), "window.LUT_LEARNING_CATALOG=" + script_json(catalogue) + ";\n")
    write(os.path.join(ROOT,"data","search-index.js"), "window.LUT_SEARCH_DATA=" + script_json({"version":1,"documents":data["documents"]}) + ";\n")
    scripts = ["search-core.js","study-store.js","study.js","reader-tools.js","practice.js","courseware.js","quick-nav.js"]
    bundle = []
    for name in scripts:
        with io.open(os.path.join(ROOT,"assets",name),encoding="utf-8") as source:
            bundle.append("/* " + name + " */\n" + source.read())
    write(os.path.join(ROOT,"assets","learning.bundle.js"), "\n;\n".join(bundle))


def main():
    args = sys.argv[1:]
    only = None
    if "--course" in args:
        only = args[args.index("--course") + 1]
    courses = load_courses()
    if "--check" in args:
        sys.exit(1 if check(courses) else 0)
    targets = [c for c in courses if only is None or c.get("id") == only]
    if only and not targets:
        print("!! content/%s.json 不存在" % only)
        sys.exit(1)
    build_learning_assets(courses)
    n = 0
    for c in targets:
        cid = c.get("id")
        write(os.path.join(ROOT, "c", cid, "index.html"), build_course(c))
        write(os.path.join(ROOT, "c", cid, "reader.html"), build_allinone([c], "../../"))
        for i in range(len(c.get("lectures", []))):
            slug = c["lectures"][i].get("slug", "lec-%d" % (i + 1))
            write(os.path.join(ROOT, "c", cid, slug + ".html"), build_lecture(c, i))
            n += 1
        for pi in range(len(parts_of(c))):
            write(
                os.path.join(ROOT, "c", cid, part_slug(pi) + ".html"), build_part(c, pi)
            )
        print("  好 %s : %d 篇" % (cid, len(c.get("lectures", []))))
    write(os.path.join(ROOT, "index.html"), build_root(courses))
    write(os.path.join(ROOT, "review.html"), build_review(courses))
    write(os.path.join(ROOT, "extend.html"), build_extension(courses))
    write(os.path.join(ROOT, "all.html"), build_allinone(courses))
    write(os.path.join(ROOT, "upload.html"), build_upload(courses))
    build_catalog_json(courses)
    build_uploads_json(courses)
    print(
        "完成：%d 门课 / %d 篇讲义 -> index.html + review.html + upload.html + data/*.json"
        % (len(courses), sum(len(c.get("lectures", [])) for c in courses))
    )
    if only:
        print("提示：本次只重建了 %s，总览页已刷新。" % only)


if __name__ == "__main__":
    main()
