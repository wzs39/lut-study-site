"""Small server-rendered shells for progressive learning enhancements."""
import html
from learning_data import SECTION_NAMES


def course_options(courses):
    return '<option value="">全部课程</option>' + ''.join(
        '<option value="%s">%s</option>' % (html.escape(str(c['id']), quote=True), html.escape(c.get('name_zh', c['id'])))
        for c in courses)


def home_widgets(courses):
    return '''<section class="learning-home card" id="study-dashboard">
<h2>我的学习</h2><div id="continue-learning"><p class="sub">还没有阅读记录，从下方选择课程开始。</p></div>
<p id="study-totals" class="sub"></p>
<details id="practice-book"><summary>错题与收藏 <span id="practice-book-count">0</span></summary>
<div class="study-filters"><label>课程<select id="practice-course" name="practice-course">%s</select></label>
<label>练习状态<select id="practice-filter" name="practice-filter"><option value="all">错题与收藏</option>
<option value="wrong">做错了</option><option value="retry">需要重做</option><option value="bookmarked">已收藏</option></select></label></div>
<div id="practice-book-list"><p class="sub">做题后可在讲义中标记状态，待复习的题目会显示在这里。</p></div></details>
<details class="study-backup"><summary>学习记录备份</summary><p class="sub">记录保存在当前浏览器。导入时合并记录并保留较新的状态。</p>
<button type="button" class="study-button" id="export-study">导出学习记录</button>
<label class="study-import">导入本站备份<input type="file" id="import-study" accept="application/json,.json"></label></details>
</section>''' % course_options(courses)


def search_box(courses):
    kinds = ''.join('<option value="%s">%s</option>' % (key, label) for key, label in SECTION_NAMES.items())
    return '''<search id="site-search" class="site-search card"><form id="search-form" action="index.html" method="get" aria-label="全文搜索">
<label for="q">全文搜索</label><div class="search-query"><input id="q" name="q" type="search" class="search" maxlength="160"
 placeholder="搜索正文、英文术语、公式或例题…" autocomplete="off" autocorrect="off" autocapitalize="none" spellcheck="false" enterkeyhint="search">
<button type="submit" class="study-button primary">搜索</button><button type="button" id="search-clear" class="study-button">清除</button></div>
<div class="study-filters"><label for="search-course">课程<select id="search-course" name="course">%s</select></label>
<label for="search-kind">讲义板块<select id="search-kind" name="kind"><option value="">全部板块</option>%s</select></label></div>
<p id="search-status" role="status" class="sub">搜索覆盖正文、术语、例题与练习答案，输入关键词开始。</p></form>
<div id="search-results" hidden><ol id="search-result-list"></ol><button type="button" id="search-more" class="study-button" hidden>显示更多结果</button></div>
<noscript><p>全文搜索需要 JavaScript；下方课程与章节目录仍可直接使用。</p></noscript></search>''' % (course_options(courses), kinds)


def course_progress(course_id, total):
    return ('<div class="course-progress" data-progress-course="%s" data-progress-total="%d">'
            '<progress max="%d" value="0" aria-label="本课学习进度"></progress><span>0 / %d 讲已掌握</span></div>'
            % (html.escape(str(course_id), quote=True), total, max(1,total), total))


def lecture_controls():
    radios = ''.join('<label class="status-pill"><input type="radio" name="lecture-status" value="%s"><span>%s</span></label>' % (key,label)
                     for key,label in [('new','未开始'),('learning','学习中'),('review','待复习'),('mastered','已掌握')])
    return '''<div class="study-toolbar"><div class="study-toolbar-row"><fieldset class="study-status"><legend>学习状态</legend><div class="status-group">%s</div></fieldset>
<div class="reader-actions"><details class="reader-options"><summary>阅读设置</summary><div class="study-filters">
<label>正文字号<select id="reader-font" name="reader-font"><option value="17">标准</option><option value="19">较大</option><option value="22">大字</option></select></label>
<label>正文行距<select id="reader-line" name="reader-line"><option value="1.65">紧凑</option><option value="1.85">标准</option><option value="2.1">宽松</option></select></label></div></details>
<button type="button" class="study-button" id="focus-reading" aria-pressed="false">专注阅读</button>
<a class="study-button" id="resume-lecture" hidden>回到上次阅读位置</a></div></div>
<p class="sub study-storage-note">学习状态与复习勾选同步，记录仅保存在当前浏览器 · 快捷键：<kbd>Ctrl K</kbd> 搜索 / <kbd>[</kbd><kbd>]</kbd> 切换上下讲 / <kbd>F</kbd> 专注阅读</p></div>''' % radios


def reading_controls():
    return '''<div class="reader-toolbar reader-actions"><details class="reader-options"><summary>阅读设置</summary><div class="study-filters">
<label>正文字号<select id="reader-font" name="reader-font"><option value="17">标准</option><option value="19">较大</option><option value="22">大字</option></select></label>
<label>正文行距<select id="reader-line" name="reader-line"><option value="1.65">紧凑</option><option value="1.85">标准</option><option value="2.1">宽松</option></select></label></div></details>
<button type="button" class="study-button" id="focus-reading" aria-pressed="false">专注阅读</button></div>'''
