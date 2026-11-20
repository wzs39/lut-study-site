# -*- coding: utf-8 -*-
"""CT60A0250 · 附录 A：课程全景、评分与 59 个视频索引（追加 1 讲）"""
import os
import sys
import json
import io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, cal, qa, det, pre, code  # noqa: E402

CID = '30352'
PATH = os.path.join(SITE, 'content', CID + '.json')
VID = os.path.join(SITE, 'gen', '30352_videos.json')

data = json.load(io.open(PATH, encoding='utf-8'))
vids = json.load(io.open(VID, encoding='utf-8'))

CH = {6: 'Chapter 1 · 入门', 7: 'Chapter 2 · 字符串与打印', 8: 'Chapter 3 · 条件与布尔',
      9: 'Chapter 4 · 循环', 10: 'Chapter 5 · 函数', 11: 'Chapter 6 · 类、列表与矩阵',
      12: 'Chapter 7 · 文本文件', 13: 'Chapter 8 · 模块', 14: 'Chapter 9 · 错误与异常',
      15: 'Chapter 10 · 数据、字典、CSV、JSON', 16: 'Chapter 11 · 数据结构与库'}

vt = ['<table><tr><th>章</th><th>主题</th><th>视频（Echo360）</th></tr>']
for d in vids:
    sec = d['sec']
    topics = d['topics']
    for i, u in enumerate(d['videos']):
        t = topics[i] if i < len(topics) else '（本节视频）'
        vt.append('<tr><td>%s</td><td>%s</td><td><a href="%s">video %d</a></td></tr>'
                  % (CH.get(sec, 'sec%d' % sec), t, u, i + 1))
vt.append('</table>')
VIDEO_TABLE = ''.join(vt)
SL = json.load(io.open(os.path.join(SITE, 'gen', '30352_slides.json'), encoding='utf-8'))
CHN = {6: ('Chapter 1', 'ch01-env-basics'), 7: ('Chapter 2', 'ch02-operators-io、ch03-strings-comments'),
       8: ('Chapter 3', 'ch04-conditionals'), 9: ('Chapter 4', 'ch05-loops'),
       10: ('Chapter 5', 'ch06-functions'), 11: ('Chapter 6', 'ch07-classes、ch08-lists-tuples'),
       12: ('Chapter 7', 'ch09-files-csv'), 13: ('Chapter 8', 'ch10-modules'),
       14: ('Chapter 9', 'ch11-errors'), 15: ('Chapter 10', 'ch12-dicts-sets-json'),
       16: ('Chapter 11', 'ch08-lists-tuples（元组）、ch12-dicts-sets-json（集合）、ch10-modules（包与 NumPy）')}
strows = ['<table><tr><th>Moodle 章</th><th>课件文件（本地均已收录）</th><th>本站对应讲次</th></tr>']
for k in sorted(SL, key=int):
    name, lec = CHN.get(int(k), ('sec%s' % k, ''))
    files = SL[k]
    strows.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'
              % (name, '<br>'.join(files), lec))
strows.append('</table>')
SLIDE_TABLE = ''.join(strows)


overview = (
    h2('本节定位')
    + p('前面 14 讲讲语法与代码，这一讲补的是「课程本身」：Moodle 上 39 个栏目到底有什么、分数怎么算、'
        '每章配了哪些视频、练习与考试怎么组织。它对应原始课程页而不是某个 PDF，因此单独成节。')
    + p('学完本节你应当能够：')
    + ck('说出课程总分公式与 1–5 级的分数区间',
         '算清练习、辅导课出勤、项目、考试各自的分值来源',
         '按 11 章顺序找到每章的主题视频与课件，知道哪两章是空的',
         '区分「学习材料区的 Chapter N」与「练习区的 Chapter N」',
         '明白 CodeGrade 提交次数上限与只准用课内语法的限制',
         '知道哪些内容无法离线化（视频、quiz 题目）以及为什么')
    + p('与前后讲的衔接：第 1 讲讲环境，这一讲讲清整门课的地图；复习时先看这一讲的评分公式，再决定时间分配。')
)

detail = (
    h3('1. 课程组织')
    + p('课程同时在 Lahti 与 Lappeenranta 两个校区开设，教学由课堂讲座、学习视频、课件、每周练习与项目工作组成，'
        '结束时必须通过期末考试。官方语言是英语。每周练习、项目与考试都必须在本年度内完成。')
    + tb(('角色', 'Lahti', 'Lappeenranta'),
         ('负责教师', 'Jouni Järvinen', 'Janne Parkkila（10 月前由 Eero Suomalainen 代课）'),
         ('CodeGrade 管理', 'Lilla Bagossi', '—'),
         ('助教', 'Lilla Bagossi、Fabiha Bushra、Hamidur Khan、Cristian Taietu、Rareș-Cristian Radu',
          'Rose Brennan、Artúr Kiss、Kanishka Ashok Kumar、Vladislav Levinschi、Máté Molnár'))
    + p('通知渠道：公告论坛（Announcements）的帖子会同步发到邮箱，必须自行关注；技术问题先查 Discord，不要在 Moodle 里发联系人请求。')

    + h3('2. 分数怎么算')
    + tb(('组成', '权重', '说明'),
         ('ExerciseGrade', '25%', '每周 CodeGrade 练习，每周 20 分'),
         ('ProjectGrade', '25%', '汽车租赁项目，CodeGrade 自动检查语法范围'),
         ('ExamGrade', '50%', '期末考试（三次考试机会）'),
         ('CourseGrade', '—', '0.25×练习 + 0.25×项目 + 0.5×考试，四舍五入，.5 一律进位'))
    + p('三个部分各自按 0（不合格）、1–5（通过）评定；只有三部分都通过才得到课程等级。最终等级按总分区间：')
    + tb(('等级', '分数区间'),
         ('1', '140–184'), ('2', '185–229'), ('3', '230–274'), ('4', '275–319'), ('5', '320 及以上'))
    + cal('tip', '策略含义', '考试占一半：练习拿满 25 分也只抵得上考试 2.5 个等级点。'
        '先把练习与项目做到稳定通过，再把时间压到考试题型上。')
    + p('练习规则：提交到 CodeGrade，只能使用课程教过的语法与结构；每道题最多提交 17 次；'
        '每周练习共 20 分；正确答案在每周辅导课（Tutorials）上讲评；自愿上台讲题可加 2 分。')
    + p('辅导课出勤：参加一次辅导课得 5 分（第一周 20 分），每周只能参加一次；'
        '为尚未抵达芬兰的学生安排线上场次，9 月后合并。')

    + h3('3. 39 个栏目全景')
    + p('Moodle 课程页按 section 编号 0–38，前 19 个是「学习材料区」，后 19 个是「练习区」。'
        '同名的 Chapter 12/13 在前区是空的，后区也没有内容，说明这两章本年度未开放。')
    + tb(('section', '栏目', '内容'),
         ('0', 'General', '课程说明、时间表、两校区信息'),
         ('1', 'Personnel', '负责教师与助教名单'),
         ('2', 'Communication', '公告论坛与 Discord'),
         ('3', 'Grading', '总分公式与等级说明'),
         ('4', 'Tutorials', '辅导课选时段（Lahti / Lappeenranta）与教师页'),
         ('5', 'Learning materials', '说明：材料 = 视频 + 课件，按概念成对'),
         ('6–16', 'Chapter 1–11', '每章一个主题标签（slides + video）+ 代码示例文件夹'),
         ('17–18', 'Chapter 12–13', '空（未开放）'),
         ('19', 'Exercises', '练习提交规则（CodeGrade、17 次上限、每周 20 分）'),
         ('20', 'Exercise grade', '等级 1–5 的分数区间'),
         ('21', 'CodeGrade', '平台入口、第一周出勤分、Tutorial 1 的 4 个任务'),
         ('22–32', 'Chapter 1–11（练习区）', '每章 C-Q 小测 + C-T 编程任务'),
         ('33–34', 'Chapter 12–13（练习区）', '空'),
         ('35', 'IDLE-Mod', '定制 IDE 安装与 Generate Submission'),
         ('36', 'AI tutor', 'AI 助教说明（仅 Chrome）'),
         ('37', 'Project work', '项目说明、时间表、概念回顾、文件与提交'),
         ('38', 'Exam', '三次考试、练习考试预约'))
    + cal('warn', '别混淆', '学习材料区的 Chapter N 里有 slides 和 video；练习区的 Chapter N 里是 C-Q 小测与 C-T 任务。'
        '两者同名但内容完全不同。')

    + h3('4. 每章主题与视频索引（59 个）')
    + p('每个主题都配一个 Echo360 视频；下面按章列出。视频是流媒体，不在离线包里，点链接会打开浏览器。')
    + VIDEO_TABLE
    + cal('tip', '怎么用视频', '先读对应 PDF 课件，再用视频补「老师怎么讲这一步」；1.5 倍速看，遇到代码演示暂停跟敲。'
        '同一主题的 slides 与 video 是配套的，不要只看视频不读课件。')

    + h3('5. 练习与测验的结构')
    + p('每章练习区固定两类：C-Q 小测（Moodle quiz）与 C-T 编程任务（CodeGrade LTI）。以第 1 章为例：')
    + tb(('名称', '类型', '作用'),
         ('C1-Q1 … C1-Q5', 'Quiz', '概念小测，题量小，用于自检'),
         ('C1-T1 … C1-T3', 'CodeGrade LTI', '编程任务，自动判分'),
         ('Chapter N tutorials participation points', 'Assignment', '辅导课出勤与讲题加分'),
         ('First week tutorial participation points', 'Assignment', '第一周出勤 20 分'))
    + p('各章题目数量不同：第 1 章 5 个 quiz + 3 个任务；第 2–5 章 4 个 quiz + 4–5 个任务；'
        '第 6–8 章 3 个 quiz + 5 个任务；第 9–11 章 2 个 quiz + 4–5 个任务。'
        'quiz 题目需要开始作答才可见，且作答会留下记录，所以本页只登记题目位置，不代替你点开。')
    + cal('warn', '不要代做', '自动打开 quiz 会消耗一次作答机会，可能影响成绩。复习时请用本页归纳的语法点，'
        '再去 quiz 做自测。')

    + h3('6. 项目与考试')
    + p('项目工作在第二学段开始，持续约三周。代码由 CodeGrade 自动检查，确保只使用课程教过的语法与概念；'
        '项目本身不自动评分。项目页包含：About project work（要求与时间表）、概念回顾视频与代码、'
        'Car rental management system 说明、四个数据文件、提交与重交入口。')
    + p('考试共三次，均为电子考试（EXAM 环境）：没有 CodeGrade，也不能访问外网。'
        '可在 EXAM 预约练习考试熟悉环境。考试信息 10 月后公布。')
    + p('IDLE-Mod 是定制版 IDLE，课程后半段使用；提交前要点「Generate Submission」打包，'
        '它会强制技术限制（例如禁止某些语法），所以平时就用它写作业，避免最后改代码。')

    + h3('7. 哪些内容无法放进离线包')
    + ul('59 个 Echo360 视频是流媒体，离线包里只保留链接，不下载视频文件；',
         'quiz 题目需登录并开始作答才显示，本页只列题号，不复制题目；',
         'CodeGrade 任务在 LTI 平台内，题目与判分都在线；',
         'Chapter 12/13 在源课程里本来就是空的，没有可抓内容；',
         '公告、Discord、AI tutor 属于动态内容，只保留入口说明。')
    + h3('8. Moodle Chapter ↔ 课件 ↔ 本站讲次')
    + p('下表把每个 Chapter 的全部课件文件与本站讲次对上，可以直接核对「某个 PDF 收在哪里」。'
        '例如 Chapter 11 的 tuples.pdf 收在第 8 讲的 8.1–8.4 节。')
    + SLIDE_TABLE
    + p('说明：Chapter 11 同时包含 tuples / sets / packages / NumPy，因此分散在第 8、10、12 讲；'
        'Chapter 6 同时包含类与列表，分散在第 7、8 讲。这是按主题合并的结果，不是漏抓。')
)

kws = tb(('English', '中文', '说明 / 例句'),
         ('CourseGrade', '课程总分', '0.25·Exercise + 0.25·Project + 0.5·Exam'),
         ('ExerciseGrade', '练习等级', '每周 20 分'),
         ('ProjectGrade', '项目等级', '三周项目'),
         ('ExamGrade', '考试等级', '电子考试，无外网'),
         ('CodeGrade', '自动判分平台', '每题最多提交 17 次'),
         ('tutorial', '辅导课', '出勤 5 分，第一周 20 分'),
         ('participation points', '出勤分', 'Assignment 形式登记'),
         ('quiz', '小测', 'C1-Q1 形式'),
         ('LTI', '外部工具集成', 'CodeGrade 任务以 LTI 嵌入'),
         ('Echo360', '视频平台', '每主题一个视频'),
         ('section', '课程栏目', '0–38 共 39 个'),
         ('Generate Submission', '生成提交包', 'IDLE-Mod 的打包按钮'),
         ('AI tutor', 'AI 助教', '仅 Chrome 可用，不能代做题'),
         ('electronic exam', '电子考试', 'EXAM 环境'))

examples = (
    h2('例题 1：算一次总分')
    + qa('练习 4 级、项目 3 级、考试 5 级，课程等级是多少？',
         p('按公式：0.25×4 + 0.25×3 + 0.5×5 = 1 + 0.75 + 2.5 = 4.25，四舍五入为 4 级。')
    + p('若考试掉到 3 级：0.25×4 + 0.25×3 + 0.5×3 = 3.25 → 3 级。考试权重决定了它是最敏感的一项。'))
    + h2('例题 2：练习分怎么变成等级')
    + qa('某学生每周拿满 20 分，共 11 周，总 220 分；等级区间是 230–274 为 3 级、185–229 为 2 级，他几级？',
         p('220 落在 185–229 → 2 级。差 10 分到 3 级，相当于多做对半周练习或上台讲 5 次题（每次 2 分）。'))
    + h2('例题 3：该先复习哪一块')
    + qa('只剩两周，练习已 3 级、项目未开始、考试未准备，时间怎么分？',
         p('先把项目做到能通过（占 25%，且三周任务可压缩为最小可用版本），再用剩余时间刷考试题型（占 50%）。'
           '练习边际收益最低，维持即可。'))
)

practice = (
    h2('练习')
    + p('1. 写出课程总分公式，并说明为什么 0.5 的考试权重意味着「练习满分也救不了考试崩」。')
    + det('答案与思路', p('CourseGrade = 0.25E + 0.25P + 0.5X；考试每降 1 级直接损失 0.5，而练习从 5 降到 1 只损失 1.0。'))
    + p('2. 学习材料区第 3 章与练习区第 3 章分别有什么？')
    + det('答案与思路', p('材料区：Chapter 3 主题标签（bool、条件、match-case 的 slides+video）与 Code Examples 文件夹；'
                        '练习区：C3-Q1–Q4 小测与 C3-T1–T4 编程任务。'))
    + p('3. 为什么 Chapter 12/13 没有讲义？')
    + det('答案与思路', p('源课程的两个 Chapter 12/13 section 为空（未开放/未发布材料），不是抓取遗漏。'))
    + p('4. CodeGrade 的 17 次上限对复习策略有什么影响？')
    + det('答案与思路', p('不能靠反复提交试错；先在本地用 IDLE-Mod 跑通样例，再提交，把次数留给边界情况。'))
)

exam = (
    h2('考点与难点')
    + cal('exam', '必考（课程规则类）',
          ul('总分公式与三个组成部分的权重',
             '等级 1–5 的分数区间',
             '每周练习 20 分、每题 17 次提交上限',
             '考试为电子考试、无外网与 CodeGrade'))
    + cal('warn', '易错',
          ul('把学习材料区的 Chapter N 与练习区同名栏目混淆',
             '以为 quiz 可以随便点开看题（会消耗作答）',
             '以为视频会打包进离线包（实为流媒体链接）'))
    + cal('tip', '进阶',
          p('能用分数公式反推「每多对一个 C-T 任务值多少最终等级」，据此安排每周投入，而不是平均用力。'))
)

checklist = (
    h2('方法清单')
    + st('先确认本周 section 属于材料区还是练习区',
         '读 slides → 看 video → 在 IDLE-Mod 跟敲示例',
         '练习先在本地跑通样例，再进 CodeGrade 提交',
         '每周记录练习得分，对照 140/185/230/275/320 的等级线',
         '项目与考试优先于刷练习（权重 25% + 50%）',
         '复习时用本页视频索引定位薄弱主题，而不是从头看所有视频')
)

mapping = (
    h2('源文件对应')
    + tb(('Moodle 栏目', 'section', '覆盖内容'),
         ('General / Personnel / Communication / Grading', '0–3', '第 1–2 节：组织、名单、通知、评分'),
         ('Tutorials', '4', '第 2 节：辅导课出勤分值'),
         ('Learning materials', '5', '第 3 节：材料构成说明'),
         ('Chapter 1–11', '6–16', '第 4 节：59 个主题视频索引与课件清单'),
         ('Chapter 12–13', '17–18, 33–34', '第 3、7 节：空栏目说明'),
         ('Exercises / Exercise grade / CodeGrade', '19–21', '第 5 节：练习规则与平台'),
         ('Chapter 1–11 练习区', '22–32', '第 5 节：C-Q 小测与 C-T 任务矩阵'),
         ('IDLE-Mod / AI tutor', '35–36', '第 6–7 节：定制 IDE 与 AI 助教'),
         ('Project work', '37', '第 6 节：项目要求、文件、提交'),
         ('Exam', '38', '第 6 节：三次电子考试与练习考试'))
    + p('<b>说明</b>：本节内容来自登录后的 Moodle 课程页（2026-11-20 抓取），不包含 quiz 题目与视频文件本身；'
        '课件 PDF 与代码示例已在第 1–13 讲逐份对应。')
)

lec = L(
    slug='appendix-course-map',
    tzh='附录 A · 课程全景、评分与视频索引',
    ten='Course Map, Grading and Video Index',
    keywords=['CourseGrade', 'ExerciseGrade', 'ProjectGrade', 'ExamGrade', 'CodeGrade',
              'tutorial', 'quiz', 'LTI', 'Echo360', 'electronic exam'],
    files=['Moodle course page (sections 0–38)'],
    overview=overview, detail=detail, kws=kws, examples=examples,
    practice=practice, exam=exam, checklist=checklist, mapping=mapping,
)
lec['part'] = '附录 A 课程全景'

data['lectures'] = [x for x in data['lectures'] if x.get('slug') != lec['slug']]
data['lectures'].append(lec)

with io.open(PATH, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
print('ok', len(data['lectures']), len(lec['html']))