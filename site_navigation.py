"""Shared, offline-friendly navigation markup for every generated page."""
from dataclasses import dataclass
import html


MODULES = (
    ("courses", "index.html", "课程总览"),
    ("review", "review.html", "期末考点清单"),
    ("extension", "extend.html", "知识拓展"),
    ("reader", "all.html", "全站合订本"),
    ("upload", "upload.html", "上传资料"),
)


@dataclass
class NavItem:
    label: str
    href: str
    children: tuple = ()
    current: bool = False

    @property
    def current_path(self):
        return self.current or any(child.current_path for child in self.children)


def site_navigation(prefix, module, nested=False):
    links = []
    for key, file, label in MODULES:
        state = ' aria-current="%s"' % ("true" if nested else "page") if key == module else ""
        links.append('<a class="navlink" data-module-link="%s" href="%s"%s>%s</a>'
                     % (key, html.escape(prefix + file, quote=True), state, label))
    return '<nav class="global-nav" aria-label="站点导航">' + "".join(links) + "</nav>"


def breadcrumbs(items):
    rows = []
    for index, (label, href) in enumerate(items):
        separator = '<span class="breadcrumb-separator" aria-hidden="true">›</span>' if index else ""
        text = html.escape(label)
        link = ('<a href="%s">%s</a>' % (html.escape(href, quote=True), text)) if href else (
            '<span aria-current="page">%s</span>' % text)
        rows.append("<li>%s%s</li>" % (separator, link))
    return '<nav class="breadcrumbs" aria-label="当前位置"><ol>' + "".join(rows) + "</ol></nav>"


def course_tree(course, current_href, parts):
    # Keep chapter/lecture order identical on course, chapter and lecture pages.
    chapters = []
    for index, (name, lectures) in enumerate(parts, 1):
        href = "part-%d.html" % index
        children = tuple(NavItem(lecture.get("title_zh", ""), lecture["slug"] + ".html",
                                 current=lecture["slug"] + ".html" == current_href)
                         for _, lecture in lectures)
        chapters.append(NavItem(name, href, children, href == current_href))
    return [NavItem(course.get("name_zh", course["id"]), "index.html", tuple(chapters),
                    current_href == "index.html")]


def page_directory(groups, context):
    counter = 0

    def tree(items, depth=0):
        nonlocal counter
        out = ['<ol class="directory-list">']
        for index, item in enumerate(items, 1):
            counter += 1
            child_id = "directory-branch-%d" % counter
            state = ' aria-current="page"' if item.current else ""
            ancestor = ' class="directory-link ancestor"' if item.current_path else ' class="directory-link"'
            number = '<span class="directory-index" aria-hidden="true">%02d</span>' % index if depth == 0 else ""
            suffix = '<span class="directory-current">当前页</span>' if item.current else ""
            out.append('<li><div class="directory-row"><a%s href="%s"%s>%s<span class="directory-label">%s</span>%s</a>'
                       % (ancestor, html.escape(item.href, quote=True), state, number,
                          html.escape(item.label), suffix))
            if item.children:
                out.append('<button class="directory-expand" type="button" hidden '
                           'aria-controls="%s" aria-expanded="true" data-start-open="%s" '
                           'aria-label="展开或收起：%s"><span aria-hidden="true">›</span></button>'
                           % (child_id, "true" if item.current_path else "false", html.escape(item.label, quote=True)))
            out.append("</div>")
            if item.children:
                out.append('<div id="%s">%s</div>' % (child_id, tree(item.children, depth + 1)))
            out.append("</li>")
        return "".join(out) + "</ol>"

    out = ['<aside class="page-side" aria-label="页面导航"><section class="page-directory">'
           '<p class="directory-heading">页面目录</p>'
           '<button class="directory-toggle" id="directory-toggle" type="button" hidden '
           'aria-expanded="true" aria-controls="directory-content">'
           '<strong>页面目录</strong><span class="directory-toggle-state">收起</span>'
           '<span class="directory-chevron" aria-hidden="true">⌄</span></button>'
           '<div id="directory-content"><p class="directory-context">%s</p>' % html.escape(context)]
    for index, (label, items) in enumerate(groups):
        spy = ' data-scrollspy="true"' if index == 0 else ""
        nav_label = "本页目录" if index == 0 else label
        out.append('<p class="directory-group-title">%s</p><nav class="directory-tree" aria-label="%s"%s>%s</nav>'
                   % (html.escape(label), html.escape(nav_label, quote=True), spy, tree(items)))
    out.append("</div></section></aside>")
    return "".join(out)


def page_frame(body, groups, context):
    return ('<div class="page-layout">%s<div class="page-content" id="page-content" tabindex="-1">%s</div></div>'
            % (page_directory(groups, context), body))


def sequence_navigation(previous, parent, following, unit):
    out = ['<nav class="sequence-nav" aria-label="顺序导航">']
    for key, target, label in [("previous", previous, "上一" + unit),
                                ("parent", parent, "返回目录"),
                                ("next", following, "下一" + unit)]:
        if target:
            href, title = target
            out.append('<a data-sequence="%s" href="%s"><span>%s</span><strong>%s</strong></a>'
                       % (key, html.escape(href, quote=True), label, html.escape(title)))
        else:
            out.append('<span class="sequence-disabled" data-sequence="%s" aria-disabled="true">'
                       '<span>%s</span><strong>已到%s</strong></span>'
                       % (key, label, "开头" if key == "previous" else "末尾"))
    return "".join(out) + "</nav>"
