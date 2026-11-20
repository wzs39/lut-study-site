# -*- coding: utf-8 -*-
"""CT60A0250 编程基础 · 补充讲 2：章节代码示例、项目说明与练习卷（只追加 1 讲）"""
import os
import sys
import json
import io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, cal, qa, det, pre, code, chips  # noqa: E402

CID = '30352'
PATH = os.path.join(SITE, 'content', CID + '.json')
data = json.load(io.open(PATH, encoding='utf-8'))

CODE_ESC = r"""print("Sam says, \"Hello!\"")
print('Timmy\'s balloon is red.')
print("This string\nspans multiple\nlines.")
print("Here is a backslash: \\")
print("1.\tShark\n2.\tShrimp\n10.\tSquid")"""

CODE_TRIPLE = r"""text = '''
=======================================
|                                     |
|    Introduction to Programming      |
|    for international programs       |
|                                     |
=======================================
'''
print(text)"""

CODE_CONCAT = r"""word3 = "Hello" + "World"          # HelloWorld
word3 = "Hello" + " " + "World"    # Hello World
number = 5
combination = str(number) + "Stars"  # 5Stars"""

CODE_INDENT = r"""if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")"""

CODE_SIGN = r"""num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")"""

CODE_MATH = r"""import math

radius = 5
print(2 * math.pi * radius)        # 31.4159...
print(math.floor(5.9))             # 5
print(math.ceil(5.1))              # 6
print(1000 * math.exp(0.05 * 3))   # 连续复利终值"""

CODE_RANDOM = r"""import random

random.randrange(0, 11, 2)   # 0,2,4,6,8,10
random.randint(1, 6)         # 1..6 含端点
random.choice(["apple", "banana", "cherry"])"""

CODE_DATETIME = r"""from datetime import datetime, timedelta

today = datetime.now()
print(today.replace(hour=9, minute=0))
print(today + timedelta(days=30))"""

CODE_APPEND = r"""file = open("test.txt", "a")
file.write("This is the text to append.\n")
file.close()"""

overview = (
    h2('本节定位')
    + p('第 1–12 讲按章讲语法，这一讲把 Moodle 各章「Code Examples」文件夹里散落的示例、'
        '项目说明页与练习卷集中起来：这些文件考试不直接考，但它们是作业与项目的最小可运行模板。')
    + p('学完本节你应当能够：')
    + ck('正确写出含引号、换行、制表符与反斜杠的字符串，并读懂三引号多行文本',
         '用切片完成取子串、步长、倒序与「中间改一个字符」',
         '解释缩进错误为什么是 IndentationError，并统一用 4 个空格',
         '用 math / random / datetime 三个模块解决圆周、随机与日期计算',
         '用 open(..., "a") 追加写文件，并说明与 "w" 的区别',
         '按项目说明拆出菜单循环、四个数据文件与日期解析三部分')
    + p('与前后的衔接：第 2 讲字符串、第 8 讲模块、第 9 讲文件、第 13 讲项目，在这里各取一个真实示例串起来。')
)

detail = (
    h3('1. 字符串里的转义：example1.py')
    + p('双引号字符串里要出现双引号，必须写成 <code>\\"</code>；单引号字符串里出现单引号写 <code>\\\'</code>。'
        '反斜杠本身要写两次 <code>\\\\</code>，换行是 <code>\\n</code>，制表符是 <code>\\t</code>。')
    + pre(CODE_ESC)
    + p('最后一行用 <code>\\t</code> 对齐、<code>\\n</code> 换行，输出就是一个两列清单。'
        '考试里常见的坑是把 <code>\\n</code> 写成 <code>/n</code>（斜杠方向错），或忘记转义导致引号提前结束字符串。')
    + cal('tip', '读法', '<code>\\t</code> = tab（制表），<code>\\n</code> = newline（换行），<code>\\\\</code> = 一个反斜杠。'
        '记忆：反斜杠是「转义开关」，要输出开关本身就得按两次。')

    + h3('2. 三引号与多行文本：example2.py')
    + p('三个引号（<code>\'\'\'</code> 或 <code>"""</code>）包住的字符串可以跨行，换行符会原样保留，'
        '常用于打印标题框、长段说明、SQL 语句。')
    + pre(CODE_TRIPLE)
    + p('要点：三引号内的缩进也会成为字符串内容；想让边框对齐，等号与竖线的数量必须逐字符数清楚。')

    + h3('3. 切片：example4.py 与 example5.py')
    + p('切片语法 <code>s[start:stop:step]</code>：含 start、不含 stop，step 为负表示倒着取。')
    + tb(('表达式', '结果', '含义'),
         ('ss[2:13]', 'ink your mil', '从下标 2 到 12'),
         ('ss[2:13:2]', 'ikyu ml', '同区间，每隔一个取'),
         ('ss[::]', 'Drink your milk!', '整串副本'),
         ('ss[::-1]', '!klim ruoy knirD', '倒序'),
         ('ss[-1:-5]', '(空串)', '默认步长为正，起点在终点右侧 → 取不到'),
         ('ss[-1:-5:-1]', '!kli', '步长为负才能从右往左取'))
    + p('example5.py 用切片修一个拼错的单词：把 <code>progsamming</code> 拆成 <code>prog</code> + <code>amming</code>，'
        '中间补 <code>r</code>，得到 <code>programming</code>。')
    + pre('word = "progsamming"\nbegin = word[:4]      # prog\nend = word[5:]        # amming\nprint(begin + "r" + end)   # programming')
    + cal('warn', '易错', '切片不会报越界：<code>s[0:100]</code> 只取到末尾。真正会报错的是用下标访问，如 <code>s[100]</code> → IndexError。')

    + h3('4. 拼接与类型：example3.py')
    + p('字符串相加是「拼接」，不会自动加空格；字符串与数字相加会抛 TypeError，必须先 <code>str()</code>。')
    + pre(CODE_CONCAT)
    + p('反过来把字符串变数字用 <code>int()</code> / <code>float()</code>，这也是 <code>input()</code> 之后必须做的转换。')

    + h3('5. 缩进与代码块：Example6.py、Example9.py')
    + p('Python 用缩进表示「哪些行属于同一个块」，同一块必须空格数一致。示例里第二行多缩进，'
        '运行会得到 <code>IndentationError: unexpected indent</code>。')
    + pre(CODE_INDENT)
    + p('Example9.py 是「正数 / 零 / 负数」三路分支的标准写法，注意 <code>elif</code> 的条件顺序与 <code>float(input(...))</code> 的转换：')
    + pre(CODE_SIGN)
    + cal('warn', '易错', '不要混用 Tab 与空格；编辑器里看起来对齐，Python 仍可能报 TabError。统一 4 个空格最稳。')

    + h3('6. math 与 random：L8E2.py–L8E4.py')
    + p('<code>math</code> 提供常量与标量函数：<code>math.pi</code>、<code>math.floor</code>、<code>math.ceil</code>、'
        '<code>math.exp</code>、<code>math.sqrt</code>。注意 <code>floor</code> 向下取整、<code>ceil</code> 向上取整，'
        '两者都不是四舍五入（四舍五入是 <code>round()</code>）。')
    + pre(CODE_MATH)
    + p('<code>random</code> 三个常用函数：<code>randrange(start, stop, step)</code> 取范围内按步长的整数，'
        '<code>randint(a, b)</code> 含两端，<code>choice(seq)</code> 从序列随机取一个。')
    + pre(CODE_RANDOM)
    + p('L8E4.py 用 <code>random.seed(42)</code> 固定随机序列，便于复现实验结果；这在不允许使用外部库的作业里很实用。')

    + h3('7. datetime 与 timedelta：L8E5.py')
    + p('<code>datetime.now()</code> 取当前时间；<code>replace(hour=9, minute=0)</code> 复制出一个改过时分的新对象（原对象不变）；'
        '<code>timedelta(days=30)</code> 表示时间间隔，可直接与 datetime 相加。')
    + pre(CODE_DATETIME)
    + p('项目里从文本读日期用 <code>datetime.strptime(s, "%d.%m.%Y")</code>，写回文本用 <code>strftime("%d.%m.%Y")</code>；'
        '这是「文本 ↔ 日期」的唯一可靠通道。')

    + h3('8. 追加写文件：append.py')
    + p('<code>open(path, "a")</code> 在文件末尾追加，不覆盖原内容；<code>"w"</code> 会清空重写。'
        '追加常用于日志，每次写一行并自己补 <code>\\n</code>。')
    + pre(CODE_APPEND)
    + p('更安全的写法是 <code>with open(...) as f:</code>，异常时也会自动关闭文件。')

    + h3('9. 项目说明与练习卷')
    + p('《2_Project instructions: Car rental management system》要求写一个菜单式租车管理系统，只用课程学过的语法：'
        '<code>print</code>、<code>input</code>、<code>def</code>、<code>while</code> 菜单、<code>for</code> 遍历列表、'
        '文件读写、<code>datetime</code>。系统依赖四个文本文件（车辆、客户、租赁记录等），每次操作后写回，直到用户选择退出。')
    + st('先跑通 project_work_concepts.py（待办清单示例），确认菜单循环与文件读写能配合',
         '确定四个文件的字段与分隔符，并写一个读入函数、一个写回函数',
         '把每个菜单项写成一个函数，主循环只负责分发',
         '金额用向上取整（math.ceil）避免少收，日期用 strptime/strftime 统一格式',
         '提交前用一组手工数据走完整流程：新增 → 修改 → 删除 → 退出后重新读入')
    + p('<code>practice_exam.png</code> 是练习卷截图（无文字层），只能作为题型参考：'
        '读代码写输出、补全函数、找错、文件读写小综合。不要把它当作正式考试范围。')
)

kws = tb(('English', '中文', '说明 / 例句'),
         ('escape sequence', '转义序列', '\\n, \\t, \\\\, \\"'),
         ('triple-quoted string', '三引号字符串', "'''...''' 可跨行"),
         ('slicing', '切片', 's[start:stop:step]'),
         ('negative step', '负步长', 's[::-1] 倒序'),
         ('concatenation', '拼接', '"a" + "b"'),
         ('type conversion', '类型转换', 'str(5), int("5")'),
         ('indentation', '缩进', '同一代码块空格数一致'),
         ('IndentationError', '缩进错误', '多缩进导致 unexpected indent'),
         ('module', '模块', 'import math'),
         ('floor / ceil', '向下/向上取整', 'floor(5.9)=5, ceil(5.1)=6'),
         ('seed', '随机种子', 'random.seed(42)'),
         ('timedelta', '时间间隔', 'today + timedelta(days=30)'),
         ('append mode', '追加模式', 'open(path, "a")'))

examples = (
    h2('例题 1：读代码写输出')
    + qa('<code>ss = "Drink your milk!"</code>，写出 <code>print(ss[2:13:2])</code> 与 <code>print(ss[::-1])</code> 的结果。',
         p('先标下标：s[0]=D, 1=r, 2=i … 12=空格? 逐字符写出来再切片，别心算。')
    + p('<code>ss[2:13]</code> = <code>ink your mil</code>（含 2 不含 13）；再每隔一个取 → <code>ikyu ml</code>。')
    + p('<code>ss[::-1]</code> 从末尾倒着取全部 → <code>!klim ruoy knirD</code>。')
    + h2('例题 2：修 bug')
    + qa('下面代码为什么报错？<code>print("Total: " + 5)</code>', p('字符串只能与字符串相加，5 是 int，Python 不做隐式转换，抛 TypeError。'))
    + p('改法一：<code>print("Total: " + str(5))</code>；改法二：<code>print("Total:", 5)</code>（print 的逗号会自动加空格）；'
        '改法三：f-string <code>print(f"Total: {5}")</code>。')
    + h2('例题 3：缩进错误')
    + qa('<code>if x &gt; 0:</code> 下一行缩进 4 空格，再下一行缩进 8 空格，会发生什么？',
         p('第二行属于 if 块，第三行缩进更多却没有新的块语句（如 if/for/def），Python 报 <code>IndentationError: unexpected indent</code>。'))
    + p('修法：同一块统一 4 空格；需要嵌套就明确写出内层语句。'))
)

practice = (
    h2('练习')
    + p('1. 用一行代码把 <code>"2026-11-20"</code> 变成 <code>"20.11.2026"</code>（提示：切片 + 拼接）。')
    + det('答案与思路', p('<code>s = "2026-11-20"; print(s[8:] + "." + s[5:7] + "." + s[:4])</code>'))
    + p('2. 用 random 生成 10 个 1–100 的整数并求平均值（不允许用 statistics 模块）。')
    + det('答案与思路', p('循环 10 次 <code>random.randint(1,100)</code> 累加，再除以 10；注意不要用 randrange(1,100) 因为不含 100。'))
    + p('3. 读文件 <code>vehicles.txt</code>，把每行按 <code>;</code> 分割后打印第二个字段。')
    + det('答案与思路', p('<code>with open("vehicles.txt") as f: for line in f: print(line.strip().split(";")[1])</code>；'
                        'strip() 去掉行尾换行，否则最后一段会带 \\n。'))
    + p('4. 解释 <code>open("log.txt","a")</code> 与 <code>open("log.txt","w")</code> 的区别，并说明为什么日志要用前者。')
    + det('答案与思路', p('"w" 打开即清空，之前内容全丢；"a" 指针在末尾，保留历史。日志需要累积，所以用 "a"。'))
)

exam = (
    h2('考点与难点')
    + cal('exam', '必考',
          ul('转义字符与三引号字符串的输出结果',
             '切片三要素（含/不含端点、负步长）',
             '字符串与数字相加的类型错误及三种改法',
             '缩进规则与 IndentationError 的成因',
             'math / random / datetime 的基本调用'))
    + cal('warn', '易错',
          ul('把 \\n 写成 /n',
             'ss[-1:-5] 以为能倒取（默认步长为正，结果空串）',
             'floor/ceil 与 round 混用',
             'randint 与 randrange 端点差异',
             '"w" 当追加用，把数据清空'))
    + cal('tip', '进阶',
          p('能说清 <code>datetime.replace()</code> 返回新对象而不是修改原对象，以及 <code>timedelta</code> 可跨月/跨年正确进位，'
            '说明你理解了「不可变对象 + 运算返回新值」这一 Python 设计。'))
)

checklist = (
    h2('方法清单')
    + st('写字符串前先决定用单引号还是双引号，再决定哪些字符要转义',
         '切片前把下标逐字符标出来，负步长单独验证一次',
         '遇到 TypeError 先看两边类型，不要先怀疑语法',
         '缩进统一 4 空格，粘贴代码后检查是否混入 Tab',
         '用模块前先 import，函数名前带模块名（math.floor）',
         '文件操作优先 with open，追加用 "a"，重写才用 "w"')
)

mapping = (
    h2('源文件对应')
    + tb(('源文件', '位置', '覆盖内容'),
         ('example1.py', '08_Chapter 2/1_Chapter 2 Code Examples', '第 1 节 转义、换行、制表符'),
         ('example2.py', '同上', '第 2 节 三引号多行文本'),
         ('example3.py', '同上', '第 4 节 拼接与 str() 转换'),
         ('example4.py / example5.py', '同上', '第 3 节 切片、步长、倒序与改字'),
         ('example6.py', '同上', '第 4 节 print 的 sep 参数'),
         ('Example6.py', '09_Chapter 3/1_Chapter 3 Code Examples', '第 5 节 缩进错误'),
         ('Example9.py', '同上', '第 5 节 三路分支'),
         ('L8E2.py', '14_Chapter 8/1_Chapter 8 Code Examples', '第 6 节 math 常量与取整'),
         ('L8E3.py / L8E4.py', '同上', '第 6 节 random 三函数与 seed'),
         ('L8E5.py', '同上', '第 7 节 datetime 与 timedelta'),
         ('append.py', '13_Chapter 7/1_Chapter 7 Code Examples', '第 8 节 追加写文件'),
         ('2_Project instructions Car rental management system.html', '38_Project work', '第 9 节 项目要求与实现步骤'),
         ('practice_exam.png', '根目录', '第 9 节 练习卷题型（图片无文字层）'))
    + p('<b>重复副本</b>：根目录的 example1–6.py、L8E2–L8E5.py、append.py、Example9.py 与章节目录同名文件内容一致，按 md5 去重。'
        '<b>拓展</b>：第 7 节的 strptime/strftime 与第 8 节的 with open 为补充写法，不改变课程原有考点。')
)

lec = L(
    slug='supp-code-examples',
    tzh='补充 · 章节代码示例、项目说明与练习卷',
    ten='Chapter Code Examples, Project Brief and Practice Exam',
    keywords=['escape sequence', 'slicing', 'triple-quoted string', 'indentation',
              'math', 'random', 'datetime', 'timedelta', 'append mode', 'type conversion'],
    files=['example1.py', 'example2.py', 'example3.py', 'example4.py', 'example5.py', 'example6.py',
           'Example6.py', 'Example9.py', 'L8E2.py', 'L8E3.py', 'L8E4.py', 'L8E5.py', 'append.py',
           '2_Project instructions Car rental management system.html', 'practice_exam.png'],
    overview=overview, detail=detail, kws=kws, examples=examples,
    practice=practice, exam=exam, checklist=checklist, mapping=mapping,
)
lec['part'] = '第 7 章 代码示例与练习卷'

data['lectures'] = [x for x in data['lectures'] if x.get('slug') != lec['slug']]
data['lectures'].append(lec)

with io.open(PATH, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
print('ok', len(data['lectures']), len(lec['html']))