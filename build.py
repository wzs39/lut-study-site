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

# Windows 控制台默认 GBK，讲义标题里出现 ⑪ 这类字符时 print 会抛 UnicodeEncodeError。
# 统一把标准输出改成 UTF-8，并对无法编码的字符退化为替代符，保证 --check 不因编码中断。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))
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
<body>
<header class="topbar"><div class="topbar-in">
<a class="brand" href="{{HOME}}">课程讲义站</a>
<a class="navlink" href="{{REVIEW}}">期末考点清单</a>
<a class="navlink ext" href="{{EXT}}">知识拓展</a>
<a class="navlink alt" href="{{ALL}}">全站合订本</a>
<a class="navlink up" href="{{UPLOAD}}">上传资料</a>
<span class="crumb">{{CRUMB}}</span>
<button id="thbtn" class="thbtn" title="切换配色：跟随系统 / 浅色 / 深色" type="button" aria-label="切换配色模式">
<span class="th-sys" aria-hidden="true">◐</span><span class="th-light" aria-hidden="true">☀</span><span class="th-dark" aria-hidden="true">☾</span>
</button>
</div></header>
<main class="wrap {{CLS}}" data-site-prefix="{{PREFIX}}">
{{BODY}}
</main>
<footer class="foot">内容基于原始课程文件整理 · 生成于 {{DATE}} <a href="#top" class="totop">回到顶部 ↑</a></footer>
{{SCRIPT}}{{THEME}}
</body>
</html>
"""

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

SEARCH_JS = """<script>
(function(){
  var q=document.getElementById('q');
  if(!q) return;
  var cards=[].slice.call(document.querySelectorAll('.ccard'));
  function hit(el,k){
    return !k || (el.getAttribute('data-s')||'').toLowerCase().indexOf(k)>=0;
  }
  q.addEventListener('input',function(){
    var k=q.value.trim().toLowerCase();
    cards.forEach(function(card){
      var shown=0;
      [].slice.call(card.querySelectorAll('.chapters > li')).forEach(function(ch){
        var chHit=hit(ch,k), n=0;
        [].slice.call(ch.querySelectorAll('.lec-list li')).forEach(function(li){
          var m=chHit||hit(li,k);
          li.style.display=m?'':'none';
          if(m) n++;
        });
        ch.style.display=(!k||chHit||n>0)?'':'none';
        if(!k||chHit||n>0) shown++;
      });
      card.style.display=(!k||shown>0)?'':'none';
    });
  });
})();
</script>"""


def page(title, body, prefix, crumb, cls="", script=""):
    return (
        LAYOUT.replace("{{TITLE}}", html.escape(title))
        .replace("{{CSSTEXT}}", CSS_TEXT)
        .replace("{{REVIEW}}", prefix + "review.html")
        .replace("{{EXT}}", prefix + "extend.html")
        .replace("{{ALL}}", prefix + "all.html")
        .replace("{{UPLOAD}}", prefix + "upload.html")
        .replace("{{HOME}}", prefix + "index.html")
        .replace("{{PREFIX}}", prefix)
        .replace("{{CRUMB}}", crumb)
        .replace("{{CLS}}", cls)
        .replace("{{BODY}}", body)
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


def lecture_nav(c, cur):
    out = []
    for i, l in enumerate(c.get("lectures", [])):
        cls = ' class="toc-l3"' if i == cur else ""
        mark = "▸ " if i == cur else ""
        out.append(
            '<a%s href="%s.html">%s%s</a>'
            % (
                cls,
                l.get("slug", "lec-%d" % (i + 1)),
                mark,
                html.escape(l.get("title_zh", "")),
            )
        )
    return "".join(out)


SECTION_LABELS = [
    ("overview", "定位"),
    ("detail", "知识点"),
    ("keywords", "术语表"),
    ("examples", "例题"),
    ("practice", "练习"),
    ("exam", "考点"),
    ("checklist", "方法清单"),
    ("mapping", "溯源"),
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


def section_quicknav(html_text):
    have = set(re.findall(r'data-type="([a-z]+)"', html_text or ""))
    chips = [
        '<a class="snav" href="#sec-%s">%s</a>' % (k, lab)
        for k, lab in SECTION_LABELS
        if k in have
    ]
    if len(chips) < 2:
        return ""
    return '<nav class="snavs">' + "".join(chips) + "</nav>"


def build_lecture(c, i):
    lecs = c["lectures"]
    lec = lecs[i]
    body, toc = decorate(add_section_ids(lec.get("html", "")))
    files = lec.get("source_files") or []
    src = ""
    if files:
        src = (
            '<p class="src">原始文件：'
            + " ".join("<code>%s</code>" % html.escape(f) for f in files)
            + "</p>"
        )
    side = (
        '<aside class="side"><div class="toc"><div class="toc-t">本页目录</div>'
        + toc
        + "</div>"
        + '<div class="toc" style="margin-top:14px"><div class="toc-t">本课讲义</div>'
        + lecture_nav(c, i)
        + "</div></aside>"
    )
    head = ["<h1>%s</h1>" % html.escape(lec.get("title_zh", ""))]
    meta = []
    if lec.get("title_en"):
        meta.append(html.escape(lec["title_en"]))
    meta.append('<span class="badge mute">%s</span>' % html.escape(c.get("id", "")))
    meta.append('<span class="badge mute">第 %d / %d 讲</span>' % (i + 1, len(lecs)))
    head.append('<p class="lead">' + " ".join(meta) + "</p>")
    part_name = lec.get("part") or "未分章"
    part_i = next((pi for pi, (n, _) in enumerate(parts_of(c)) if n == part_name), 0)
    head.append(
        '<p class="chaptertag">所属章节：<a href="%s.html">%s</a></p>'
        % (part_slug(part_i), html.escape(part_name))
    )
    head.append(src)
    head.append(section_quicknav(lec.get("html", "")))
    nav = ['<div class="lnav">']
    if i > 0:
        nav.append(
            '<a class="prev" href="%s.html">← %s</a>'
            % (lecs[i - 1].get("slug"), html.escape(lecs[i - 1].get("title_zh", "")))
        )
    else:
        nav.append("<span></span>")
    if i + 1 < len(lecs):
        nav.append(
            '<a class="next" href="%s.html">%s →</a>'
            % (lecs[i + 1].get("slug"), html.escape(lecs[i + 1].get("title_zh", "")))
        )
    else:
        nav.append("<span></span>")
    nav.append("</div>")
    art = "<article>" + "".join(head) + body + "".join(nav) + "</article>"
    crumb = (
        '<a href="../../index.html">总览</a> / <a href="index.html">%s</a> / <a href="%s.html">%s</a>'
        % (
            html.escape(c.get("name_zh", c.get("id", ""))),
            part_slug(part_i),
            html.escape(part_name),
        )
    )
    return page(
        "%s · %s" % (lec.get("title_zh", ""), c.get("id", "")),
        '<div class="lec">' + side + art + "</div>",
        "../../",
        crumb,
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


def lec_card(l):
    kw = l.get("keywords") or []
    chips = "".join('<span class="chip">%s</span>' % html.escape(k) for k in kw[:8])
    ov = section(l.get("html", ""), "overview")
    return (
        '<div class="card"><h3><a href="%s.html">%s</a></h3>'
        '<p class="lead">%s</p>%s%s</div>'
        % (
            l.get("slug"),
            html.escape(l.get("title_zh", "")),
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
        rows = "".join(lec_card(l) for _, l in items)
        blocks.append(
            '<div class="chapter"><h2 id="p-%s"><a href="%s.html">%s</a> '
            '<span class="badge mute">%d 讲</span></h2>%s</div>'
            % (pi + 1, part_slug(pi), html.escape(name), len(items), rows)
        )
    parts_meta = json.dumps(
        [{"index": pi + 1, "slug": part_slug(pi), "name": name} for pi, (name, _) in enumerate(parts)],
        ensure_ascii=False,
    )
    upload_panel = (
        '<section class="card mat-panel" id="course-materials" data-course="%s" data-parts="%s">'
        '<div class="mat-empty">正在加载本课实时资料库…</div></section>'
        % (html.escape(c.get("id", ""), quote=True), html.escape(parts_meta, quote=True))
    )
    body = (
        '<h1>%s</h1><p class="lead">%s</p>%s'
        '<p><a class="chip" href="../../review.html#r-%s">本课考点速查 →</a> '
        '<a class="chip" href="../../extend.html#e-%s">本课知识拓展 →</a> '
        '<a class="chip" href="../../all.html#c-%s">本课合订本 →</a> '
        '<a class="chip" href="#course-materials">本课实时资料与上传 ↓</a></p>%s%s'
        % (
            html.escape(c.get("name_zh", c.get("id", ""))),
            course_info(c, lecs, len(parts)),
            ("<p>%s</p>" % html.escape(c.get("summary", "")))
            if c.get("summary")
            else "",
            html.escape(c.get("id", "")),
            html.escape(c.get("id", "")),
            html.escape(c.get("id", "")),
            "".join(blocks),
            upload_panel,
        )
    )
    crumb = (
        '<a href="../../index.html">总览</a> / <a href="../../index.html#c-%s">课程</a> / '
        % html.escape(c.get("id", ""))
        + html.escape(c.get("name_zh", c.get("id", "")))
    )
    mat_scripts = '<script src="../../assets/config.js"></script><script src="../../assets/materials.js"></script>'
    return page(
        "%s · 课程讲义" % c.get("name_zh", c.get("id", "")),
        body,
        "../../",
        crumb,
        script=mat_scripts,
    )


def build_part(c, pi):
    parts = parts_of(c)
    name, items = parts[pi]
    rows = "".join(lec_card(l) for _, l in items)
    nav = ['<div class="lnav">']
    if pi > 0:
        nav.append(
            '<a class="prev" href="%s.html">← %s</a>'
            % (part_slug(pi - 1), html.escape(parts[pi - 1][0]))
        )
    else:
        nav.append("<span></span>")
    if pi + 1 < len(parts):
        nav.append(
            '<a class="next" href="%s.html">%s →</a>'
            % (part_slug(pi + 1), html.escape(parts[pi + 1][0]))
        )
    else:
        nav.append("<span></span>")
    nav.append("</div>")
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
        '<p><a class="chip" href="#chapter-materials">本章补充资料 / 上传讲义 ↓</a></p>'
        "<h2>%s</h2>%s%s%s"
        % (
            html.escape(name),
            html.escape(c.get("name_zh", c.get("id", ""))),
            course_info(c, c.get("lectures", []), len(parts)),
            html.escape(name),
            rows,
            upload_panel,
            "".join(nav),
        )
    )
    crumb = '<a href="../../index.html">总览</a> / <a href="index.html">%s</a> / %s' % (
        html.escape(c.get("name_zh", c.get("id", ""))),
        html.escape(name),
    )
    mat_scripts = '<script src="../../assets/config.js"></script><script src="../../assets/materials.js"></script>'
    return page(
        "%s · %s" % (name, c.get("name_zh", "")),
        body,
        "../../",
        crumb,
        script=mat_scripts,
    )


def build_root(courses):
    mf = manifest_files()
    total_lec = sum(len(c.get("lectures", [])) for c in courses)
    total_parts = sum(len(parts_of(c)) for c in courses)
    src_total = sum(len(v) for v in mf.values())
    cards = []
    for c in courses:
        lecs = c.get("lectures", [])
        cid = c["id"]
        chapters = []
        for pi, (name, items) in enumerate(parts_of(c)):
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
                    '<li data-s="%s"><a class="t" href="c/%s/%s.html">%s</a></li>'
                    % (
                        html.escape(s, quote=True),
                        cid,
                        l.get("slug"),
                        html.escape(l.get("title_zh", "")),
                    )
                )
            chapters.append(
                '<li class="ch" data-s="%s"><a class="ch-t" href="c/%s/%s.html">%s</a>'
                '<span class="n">%d 讲</span><ul class="lec-list">%s</ul></li>'
                % (
                    html.escape((cid + " " + name).lower(), quote=True),
                    cid,
                    part_slug(pi),
                    html.escape(name),
                    len(items),
                    "".join(rows),
                )
            )
        cards.append(
            '<div class="ccard" id="c-%s"><h3><a href="c/%s/index.html">%s</a></h3>'
            '<div class="meta">%s%s · %d 章 · %d 讲</div><ul class="chapters">%s</ul></div>'
            % (
                cid,
                cid,
                html.escape(c.get("name_zh", cid)),
                html.escape(cid),
                (" · " + html.escape(c.get("name_en", ""))) if c.get("name_en") else "",
                len(parts_of(c)),
                len(lecs),
                "".join(chapters),
            )
        )
    body = (
        "<h1>课程讲义总览</h1>"
        '<p class="lead">按「课程 → 章节 → 讲次」三级组织：每门课独立成页，每章有独立章节页，每讲有独立讲义页。'
        "搜课程ID、章节名、讲义标题或关键词都能定位。</p>"
        '<div class="stats"><div class="stat"><b>%d</b><span>门课程</span></div>'
        '<div class="stat"><b>%d</b><span>个章节</span></div>'
        '<div class="stat"><b>%d</b><span>讲讲义</span></div>'
        '<div class="stat"><b>%d</b><span>个原始文件</span></div></div>'
        '<input id="q" class="search" placeholder="搜索：课程ID / 章节名 / 讲义标题 / 关键词…">'
        '<p><a class="chip" href="upload.html">📤 上传章节讲义 / 实时资料中心 →</a> '
        '<a class="chip" href="all.html">打开全站合订本（全部讲次一页读完）→</a> '
        '<a class="chip" href="review.html">期末考点提醒清单 →</a> '
        '<a class="chip" href="extend.html">知识拓展汇总页 →</a></p>'
        '<div class="courses">%s</div>'
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
            "".join(cards),
        )
    )
    return page(
        "课程讲义总览",
        body,
        "",
        "共 %d 门课 · %d 章 · %d 讲" % (len(courses), total_parts, total_lec),
        script=SEARCH_JS,
    )


def build_allinone(courses):
    total = sum(len(c.get("lectures", [])) for c in courses)
    total_parts = sum(len(parts_of(c)) for c in courses)
    toc = ['<div class="alltoc"><b>目录：课程 → 章节 → 讲次</b><ol class="steps">']
    parts = []
    for c in courses:
        cid = c.get("id", "")
        name = c.get("name_zh", cid)
        lecs = c.get("lectures", [])
        chapters = parts_of(c)
        sub = []
        for pi, (pname, items) in enumerate(chapters):
            links = "".join(
                '<li><a href="#l-%s-%s">%s</a></li>'
                % (
                    html.escape(cid),
                    html.escape(l.get("slug", "")),
                    html.escape(l.get("title_zh", "")),
                )
                for _, l in items
            )
            sub.append(
                '<li><a href="#p-%s-%d">%s</a>（%d 讲）<ol class="steps">%s</ol></li>'
                % (html.escape(cid), pi + 1, html.escape(pname), len(items), links)
            )
        toc.append(
            '<li><a href="#c-%s">%s</a>（%d 章 / %d 讲）<ol class="steps">%s</ol></li>'
            % (
                html.escape(cid),
                html.escape(name),
                len(chapters),
                len(lecs),
                "".join(sub),
            )
        )
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
                        l.get("html", ""),
                        html.escape(cid),
                        html.escape(l.get("slug", "")),
                        html.escape(cid),
                        part_slug(pi),
                        html.escape(cid),
                    )
                )
    toc.append("</ol></div>")
    body = (
        "<h1>全站合订本 · 全部课程逐讲讲义</h1>"
        '<p class="lead">%d 门课 / %d 章 / %d 讲，按「课程 → 章节」顺序连排；每章有标题，'
        "每讲之后可直接跳回独立页或章节页。适合通读、打印、离线放到手机里看。</p>%s%s"
        % (len(courses), total_parts, total, "".join(toc), "".join(parts))
    )
    return page(
        "全站合订本 · 课程讲义",
        body,
        "",
        "共 %d 门课 · %d 章 · %d 讲" % (len(courses), total_parts, total),
    )


REVIEW_JS = """<script>
(function(){
  var boxes=[].slice.call(document.querySelectorAll('input.tick'));
  var out=document.getElementById('tickprog');
  var KEY='lut-review-v1';
  var store={};
  try{ store=JSON.parse(localStorage.getItem(KEY)||'{}')||{}; }catch(e){ store={}; }
  function save(){ try{ localStorage.setItem(KEY, JSON.stringify(store)); }catch(e){} }
  function refresh(){
    var done=boxes.filter(function(b){return b.checked;}).length;
    if(out) out.textContent='已复习 '+done+' / '+boxes.length+' 讲';
  }
  boxes.forEach(function(b){
    var k=b.getAttribute('data-k');
    if(store[k]) b.checked=true;
    b.addEventListener('change',function(){ store[k]=b.checked; save(); refresh(); });
  });
  refresh();
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
    quick, sections = [], []
    for c in courses:
        cid = c.get("id", "")
        name = c.get("name_zh", cid)
        lecs = c.get("lectures", [])
        chapters = parts_of(c)
        quick.append(
            '<div class="qcourse"><div class="qhead"><a href="#r-%s">%s</a>'
            '<span class="badge mute">%d 章 / %d 讲</span></div><ul class="chapters-tick">'
            % (html.escape(cid), html.escape(name), len(chapters), len(lecs))
        )
        for pi, (pname, items) in enumerate(chapters):
            quick.append(
                '<li><a class="qp" href="c/%s/%s.html">%s</a><ul class="ticklist">'
                % (html.escape(cid), part_slug(pi), html.escape(pname))
            )
            for gi, l in items:
                key = "%s-%s" % (cid, l.get("slug", "lec-%d" % (gi + 1)))
                quick.append(
                    '<li><label><input type="checkbox" class="tick" data-k="%s"> %s</label></li>'
                    % (html.escape(key), html.escape(l.get("title_zh", "")))
                )
            quick.append("</ul></li>")
        quick.append("</ul></div>")

        blocks = []
        for pi, (pname, items) in enumerate(chapters):
            blocks.append(
                '<div class="revpart"><a href="c/%s/%s.html">%s</a>'
                '<span class="badge mute">%d 讲</span></div>'
                % (html.escape(cid), part_slug(pi), html.escape(pname), len(items))
            )
            for gi, l in items:
                slug = l.get("slug", "lec-%d" % (gi + 1))
                exam = _demote(section(l.get("html", ""), "exam"))
                chk = section(l.get("html", ""), "checklist")
                if not exam.strip():
                    continue
                body = [
                    '<div class="revlec" id="r-%s-%s">'
                    % (html.escape(cid), html.escape(slug))
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
        sections.append(
            '<section class="revcourse" id="r-%s"><h2>%s <span class="badge mute">%s</span></h2>%s</section>'
            % (html.escape(cid), html.escape(name), html.escape(cid), "".join(blocks))
        )
    body = (
        "<h1>期末总复习 · 考点提醒清单</h1>"
        '<p class="lead">把每门课每一讲的「考点与难点」「方法清单」集中到一页：先按课程勾掉已复习的讲次，'
        '再逐条过一遍必考、易错与进阶提示。适合考前 3 天扫盲、考前 1 天速查、考前 1 小时只看<span class="badge bad">必考</span>。</p>'
        '<div class="stats"><div class="stat"><b>%d</b><span>门课</span></div>'
        '<div class="stat"><b>%d</b><span>讲</span></div>'
        '<div class="stat"><b id="tickprog">已复习 0 / 0 讲</b><span>复习进度（本地保存）</span></div></div>'
        '<div class="usebar"><b>怎么用这一页：</b>'
        '<ol class="steps"><li>考前 3 天：按课程顺序过「必考」，把不会的回到原讲义补 detail。</li>'
        "<li>考前 1 天：只看「易错」，把每条错因写成一句话。</li>"
        "<li>考前 1 小时：只看 badges 为必考的公式、定义和题型名称，不做新题。</li></ol></div>"
        '<h2>复习进度总表</h2><div class="qgrid">%s</div>'
        "<h2>逐讲考点与难点</h2>%s"
        % (len(courses), total, "".join(quick), "".join(sections))
    )
    return page(
        "期末总复习 · 考点提醒清单",
        body,
        "",
        "共 %d 门课 · %d 讲" % (len(courses), total),
        script=REVIEW_JS,
    )


def build_extension(courses):
    """知识拓展专页：汇总所有讲义里的「拓展」提示框与 mapping 中标注的补充内容。"""
    anchors, blocks, total_idea, total_note = [], [], 0, 0
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
        anchors.append(
            '<li><a href="#e-%s">%s</a>（拓展框 %d · 补充条目 %d）</li>'
            % (html.escape(cid), html.escape(name), len(idea_rows), len(note_rows))
        )
        parts = [
            '<section class="revcourse" id="e-%s"><h2>%s <span class="badge mute">%s</span></h2>'
            % (html.escape(cid), html.escape(name), html.escape(cid))
        ]
        if idea_rows:
            parts.append('<div class="revpart">课内拓展提示框</div>')
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
                '<div class="revpart">mapping 中标注的补充 / 拓展内容（对照原始文件）</div>'
                '<table><tr><th>出处讲次</th><th>源文件 / 位置</th><th>补充说明</th></tr>'
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
    body = (
        "<h1>知识拓展 · 全站汇总</h1>"
        '<p class="lead">把 %d 门课讲义里所有「拓展」提示框（背景知识、推导、常见误解、前后衔接）与 '
        "mapping 板块标注的补充内容集中到一页：先看拓展框加深理解，再按 mapping 回原讲义核对边界——"
        "拓展不引入原文没有的新考点，凡是补充都会标明出处。</p>"
        '<div class="stats"><div class="stat"><b>%d</b><span>门课有拓展</span></div>'
        '<div class="stat"><b>%d</b><span>个拓展框</span></div>'
        '<div class="stat"><b>%d</b><span>条 mapping 补充</span></div></div>'
        '<div class="usebar"><b>怎么用这一页：</b>'
        '<ol class="steps"><li>按课程跳转，拓展框都带原始讲次链接，点回去能看到它在讲义里的上下文。</li>'
        "<li>mapping 补充条目按「出处讲次 / 源文件 / 补充说明」三列排列，方便区分哪些是原文、哪些是整理时加的。</li>"
        "<li>考前不需要通读本页：拓展只用来答疑与写论述题的深度，评分以原讲义 exam 板块为准。</li></ol></div>"
        '<h2>目录</h2><ol class="steps">%s</ol>%s'
        % (len(courses), total_courses, total_idea, total_note, "".join(anchors), "".join(blocks))
    )
    return page(
        "知识拓展 · 全站汇总",
        body,
        "",
        "拓展框 %d · mapping 补充 %d" % (total_idea, total_note),
    )


def build_upload(courses):
    total_parts = sum(len(parts_of(c)) for c in courses)
    body = (
        "<h1>实时资料上传中心 · Upload Center</h1>"
        '<p class="lead">支持按「课程 → 章节」上传 PDF / PPTX / DOCX / 图片 / 代码文件，或直接撰写 Markdown 补充笔记。'
        "发布后立即同步到对应章节页与全站最新动态。</p>"
        '<div id="upload-hub"><div class="mat-empty">正在加载课程与章节目录…</div></div>'
    )
    mat_scripts = '<script src="assets/config.js"></script><script src="assets/materials.js"></script>'
    return page(
        "实时资料上传中心 · 课程讲义站",
        body,
        "",
        "覆盖 %d 门课 · %d 个章节" % (len(courses), total_parts),
        script=mat_scripts,
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
    n = 0
    for c in targets:
        cid = c.get("id")
        write(os.path.join(ROOT, "c", cid, "index.html"), build_course(c))
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
