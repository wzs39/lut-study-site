# -*- coding: utf-8 -*-
"""生成 content/30352.json · CT60A0250 编程基础 逐讲讲义。

第 1、2 讲（ch01-env-basics、ch02-operators-io）从已有 content/30352.json
原样搬入（slug / title / keywords / source_files / html 一字不改），
第 3 讲起按课程实际章节补齐，最后整体 emit 覆盖 content/30352.json。
"""

import io
import json
import os
import sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)

from genlib import (
    L,
    emit,
    h2,
    h3,
    p,
    ul,
    ol,
    ck,
    st,
    tb,
    K,
    cal,
    qa,
    det,
    pre,
    code,
    chips,
)

BASE = json.load(io.open(os.path.join(SITE, "content", "30352.json"), encoding="utf-8"))

# ---- 已有两讲：原样保留 ------------------------------------------------
KEEP = ("ch01-env-basics", "ch02-operators-io")  # 只保留这两讲，脚本可重复运行
LEC = []
for _old in BASE["lectures"]:
    if _old["slug"] not in KEEP:
        continue
    LEC.append(
        {
            "slug": _old["slug"],
            "title_zh": _old["title_zh"],
            "title_en": _old["title_en"],
            "keywords": list(_old["keywords"]),
            "source_files": list(_old["source_files"]),
            "html": _old["html"],
        }
    )

# ============================================================ 3 字符串与注释
LEC.append(
    L(
        slug="ch03-strings-comments",
        tzh="③ 注释、字符串与输出控制",
        ten="Comments, Strings and Print Control",
        keywords=[
            "comment",
            "docstring",
            "escape sequence",
            "index",
            "negative index",
            "slice",
            "immutable",
            "concatenation",
            "sep",
            "end",
            "rounding",
            "truncation",
        ],
        files=[
            "Ch 2 - Part 1 - Comments.pdf",
            "Ch 2 - Part 2 - Strings.pdf",
            "Ch 2 - Part 3 - More on strings.pdf",
            "Ch 2 - Part 4 - Modify Printing.pdf",
            "Ch 2 - Part 5 - Converting ints and floats.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第 2 章前半部分讲的是同一件事的两面：让机器读懂人、也让人读懂机器。注释把意图写进代码，字符串承载所有文本，<code>print</code> 的 <code>sep</code> 与 <code>end</code> 决定版式，<code>round()</code> 与 <code>int()</code> 决定小数怎么落地。"
            )
            + p(
                "上一讲解决了「数据怎么算、怎么读进来、怎么印出去」；这一讲把文本本身拆开：字符怎么编号、怎么切段、为什么改不动。下一讲开始让程序做判断。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "用 <code>#</code> 与 docstring 写出有用的注释，而不是复述代码",
                '说明 <code>\\n</code>、<code>\\t</code>、<code>\\\\</code>、<code>\\"</code> 各自是什么意思',
                "用正索引和负索引取出任意一个字符，并解释 <code>IndexError</code> 的来源",
                "用切片取出子串、反转字符串，并说清「含 start 不含 stop」",
                "解释字符串为什么不可变，改用切片重组来「修改」它",
                "用 <code>sep</code> / <code>end</code> 控制多值输出与不换行输出",
            )
        ),
        detail=(
            h2("一、注释：写给人看的代码")
            + p(
                "课件先从动机讲起：真实的程序会长到几百行、几百个文件（Part 1 p2），到那时连作者本人也会忘记某一行为什么要那样写。注释（comment）就是留给「人」读的说明，解释器整段跳过。"
            )
            + h3("1.1 单行注释以 # 开始")
            + p(
                "从 <code>#</code> 到行尾都属于注释，不会被运行（Part 1 p3）。它既可以独占一行，也可以写在代码右边当行内注释。"
            )
            + pre("""# 这一整行都是注释，解释器什么也不做
price = 12.5          # 行内注释：# 之前照常执行
name = "page#1"       # 这个 # 在字符串里面，不算注释
print(name)""")
            + pre("""page#1""")
            + p(
                '最后一行给出了一条容易忽略的边界：<code>#</code> 只有出现在字符串之外才开启注释；写在引号里它就是普通字符。链接、颜色值 <code>"#ff0000"</code>、井号标签都不需要转义。'
            )
            + h3("1.2 三引号字符串与文档字符串")
            + p(
                "课件讲多行字符串时说「一件事占一行太麻烦」，于是用三个引号把多行包起来（Part 2 p5）。这种写法常被借来当块注释："
            )
            + pre('''"""
这段说明被当作块注释使用。
解释器仍会创建这个字符串对象，只是没有变量接收，
于是它立刻被丢弃，效果看起来与注释相同。
"""
print("done")''')
            + p(
                "严格说它不是注释，而是「未绑定变量的字符串字面量」。真正有身份的是放在函数、类或模块第一行的那种字符串，叫<b>文档字符串</b>（docstring）："
            )
            + pre('''def area(r):
    """Return the area of a circle with radius r."""
    return 3.14159 * r ** 2

print(area(2))
help(area)''')
            + p(
                '<code>help(area)</code> 会把 docstring 打印出来——这正是课程示例程序里每个函数开头都写一句 <code>"""Prints the menu options for calculating areas."""</code> 的原因：它既是注释，又能被工具读取。'
            )
            + cal(
                "tip",
                "判断注释是否合格",
                "解释「为什么」，不要复述「做什么」。<code>x = x + 1  # add one</code> 是废话；<code>x = x + 1  # 补偿从 0 开始的下标</code> 才有价值。",
            )
            + h2("二、字符串是一串字符")
            + h3("2.1 定义与长度")
            + p(
                "字符串（string）是字符的序列：字母、数字、符号、空格、汉字各算一个字符。用一对单引号或一对双引号包起来即可，两种写法完全等价（Part 2 p2）："
            )
            + pre("""s1 = 'This is a string'
s2 = "This is a string"
print(s1 == s2)
print(len("programming"))""")
            + pre("""True
11""")
            + p(
                '<code>len()</code> 返回字符个数（Part 2 p3），数的是「字符」而不是「字节」：<code>len("中文")</code> 得 2。'
            )
            + h3("2.2 转义序列")
            + p(
                "有些字符没法直接写进引号里（引号本身、换行），于是用反斜杠开头的<b>转义序列</b>（escape sequence）表示（Part 2 p4）。"
            )
            + tb(
                ("转义写法", "实际内容", "典型用途"),
                ("<code>\\\\</code>", "一个反斜杠", "Windows 路径、正则表达式里常见"),
                ("<code>\\'</code>", "单引号", "在单引号字符串里表示引号本身"),
                ('<code>\\"</code>', "双引号", "在双引号字符串里表示引号本身"),
                ("<code>\\n</code>", "换行", "newline，最常用"),
                ("<code>\\t</code>", "制表符", "tab，用来对齐列"),
            )
            + pre("""print("第一行\\n第二行")
print("姓名\\t年龄")
print("He said \\"hi\\"")
print('It\\'s ok')""")
            + pre("""第一行
第二行
姓名    年龄
He said "hi"
It's ok""")
            + p(
                "第二行的输出里，姓名与年龄之间是一个制表符（显示宽度随终端而定），所以看起来像几个空格。"
            )
            + h3("2.3 多行字符串")
            + pre('''text = """第一行
第二行
第三行"""
print(text)
print(len(text))''')
            + p(
                "内容里的真实换行会原样变成字符串中的 <code>\\n</code>，所以 <code>len(text)</code> 把换行符也算进去。这里有个隐蔽的坑：三引号内部每行行首的空白也是字符，把多行字符串写在缩进很深的函数里，内容会凭空多出一排空格。"
            )
            + h3("2.4 拼接与重复")
            + pre("""print("Hello" + " " + "World")
print("-" * 20)
print(("ab" + "\\n") * 2, end="")""")
            + pre("""Hello World
--------------------
ab
ab""")
            + p(
                '<code>+</code> 只能把字符串接字符串：<code>"a" + 1</code> 抛 <code>TypeError</code>，必须先 <code>str(1)</code>。乘法 <code>*</code> 需要一个整数，<code>"ab" * 0</code> 得空字符串，负数也得空字符串。'
            )
            + cal(
                "warn",
                "隐式拼接的坑",
                'Python 允许相邻的两个字符串字面量自动合并：<code>"abc" "def"</code> 就是 <code>"abcdef"</code>。写长句时很方便，但列表里漏了逗号写成 <code>["a" "b"]</code>，会静默变成只有一个元素 <code>"ab"</code>，不报错、很难发现。',
            )
            + h2("三、索引：正着数与倒着数")
            + p(
                '每个字符有一个位置编号，从 0 开始（Part 3 p2）。长度为 12 的 <code>"I love code!"</code>：I 是 0，空格是 1，l 是 2……最后一位 <code>!</code> 是 11。'
            )
            + pre("""s = "I love code!"
print(s[0], s[2], s[11])
print(len(s) - 1)""")
            + pre("""I l !
11""")
            + p(
                "写 <code>s[len(s) - 1]</code> 而不是硬编码 <code>s[11]</code>，字符串一变长度就不需要改代码。负索引（negative index）从右往左数，最后一位是 <code>-1</code>（Part 3 p3）："
            )
            + pre("""s = "I love code!"
print(s[-1])
print(s[-2])
print(s[-len(s)])""")
            + pre("""!
e
I""")
            + cal(
                "warn",
                "IndexError",
                "下标超过 <code>len(s) - 1</code> 或小于 <code>-len(s)</code>，会抛 <code>IndexError: string index out of range</code>。空字符串连 <code>s[0]</code> 都不能取。负索引的合法范围是 <code>-len(s)</code> 到 <code>-1</code>。",
            )
            + h2("四、字符串不可变")
            + p(
                "immutable 的意思是「创建之后内容不能改」（Part 3 p4）。下面这条语句不是「把第 0 个字符换成 H」，而是直接报错："
            )
            + pre('''s = "hello"
s[0] = "H"''')
            + pre("""TypeError: 'str' object does not support item assignment""")
            + p(
                '能做的是整体换一个新字符串：<code>s = "Hello"</code>。要记住区别：这是「让变量指向另一个字符串」，不是「修改原来那个字符串」。本讲末尾的切片重组，以及第 8 讲的列表可变性，都建立在这一点上。'
            )
            + h2("五、切片：一次取一段")
            + p(
                "切片（slice）的完整形式是 <code>s[start:stop:step]</code>，规则只有一条：<b>含 start，不含 stop</b>（Part 3 p5）。三个参数都可以省略。"
            )
            + tb(
                ("写法", "含义", '例子（s = "I love code!"）', "结果"),
                (
                    "<code>s[2:6]</code>",
                    "下标 2 到 5",
                    "<code>s[2:6]</code>",
                    "<code>love</code>",
                ),
                (
                    "<code>s[:4]</code>",
                    "开头到下标 3",
                    "<code>s[:4]</code>",
                    "<code>I lo</code>",
                ),
                (
                    "<code>s[7:]</code>",
                    "下标 7 到结尾",
                    "<code>s[7:]</code>",
                    "<code>code!</code>",
                ),
                (
                    "<code>s[:]</code>",
                    "整串的副本",
                    "<code>s[:] == s</code>",
                    "<code>True</code>",
                ),
                (
                    "<code>s[::2]</code>",
                    "每隔一个取",
                    "<code>s[::2]</code>",
                    "<code>Ilv oe</code>",
                ),
                (
                    "<code>s[::-1]</code>",
                    "整串反转",
                    "<code>s[::-1]</code>",
                    "<code>!edoc evol I</code>",
                ),
            )
            + p(
                '三条边界：切片越界不报错（<code>s[5:100]</code> 自动截到末尾）；<code>start</code> 大于 <code>stop</code> 且步长为正时返回空串 <code>""</code>；切片得到的是<b>新字符串</b>，与原来不是同一个对象。'
            )
            + p(
                "因为切片产生新串，「改字符串」的标准手法就是切片重组（Part 3 p6）：把不要的段切掉，把新段拼进去。"
            )
            + pre("""s = "I love code!"
print(s[:2] + "really " + s[2:])""")
            + pre("""I really love code!""")
            + p(
                "同理，把首字母改成大写可以写 <code>s[0].upper() + s[1:]</code>；去掉末尾换行可以写 <code>s[:-1]</code>（仅当确实以换行结尾时）。"
            )
            + cal(
                "tip",
                "三个必须背下来的切片",
                "<code>s[::-1]</code> 反转；<code>s[-3:]</code> 取末三位；<code>s[1:]</code> 去掉首字符。考试里出现频率极高，也是写回文、扩展名、日期重排的通用零件。",
            )
            + h2("六、print 的 sep 与 end")
            + p(
                "<code>print()</code> 有两个可选参数控制版式（Part 4 p2–p6）：<code>sep</code> 是多个值之间的分隔符，默认一个空格；<code>end</code> 是结尾追加的内容，默认换行 <code>\\n</code>。"
            )
            + pre("""print("a", "b", "c")
print("a", "b", "c", sep="-")
print("a", "b", "c", sep="")
print("no newline", end="")
print(" continues here")
print("end of report", end="\\n\\n")""")
            + pre("""a b c
a-b-c
abc
no newline continues here
end of report
""")
            + p(
                '<code>sep</code> 可以是任意字符串：空串、<code>" -> "</code>、<code>", "</code>；<code>end</code> 也是，包括 <code>""</code>（不换行）、<code>"\\t"</code>（同行制表）、<code>"\\n\\n"</code>（多空一行）。'
            )
            + p(
                '这两个参数只影响 <code>print</code> 的输出，不改变数据本身：<code>"a" + "b"</code> 永远是 <code>"ab"</code>，不会因为 <code>sep</code> 变成 <code>a-b</code>。循环里逐个印又不想换行，写 <code>print(item, end="")</code>；想用逗号隔开，写 <code>print(item, end=", ")</code>，并自行处理末尾多出来的那个逗号。'
            )
            + cal(
                "warn",
                "sep 只对多参数生效",
                '<code>print("a" + "b", sep="-")</code> 输出的仍是 <code>ab</code>：只有一个参数，分隔符没有用武之地。想要 <code>a-b</code> 必须写 <code>print("a", "b", sep="-")</code>。',
            )
            + h2("七、int、float 与 round")
            + h3("7.1 round() 是四舍五入，但有两个意外")
            + p(
                "<code>round(x)</code> 返回最接近的整数，<code>round(x, n)</code> 保留 n 位小数（Part 5 p2）。"
            )
            + pre("""print(round(6.7))
print(round(6.7, 0))
print(round(3.14159, 2))
print(round(2.5), round(3.5))""")
            + pre("""7
7.0
3.14
2 4""")
            + p(
                "意外一：<code>round(6.7, 0)</code> 得 <code>7.0</code> 而不是 <code>7</code>——只要给了第二个参数，返回类型仍是 float。意外二：<code>round(2.5)</code> 得 2 不是 3，因为 Python 用「银行家舍入」（banker's rounding），恰好 .5 时向偶数靠。"
            )
            + h3("7.2 int() 是截断，不是四舍五入")
            + p(
                "<code>int(x)</code> 把 float 转成 int 时，小数部分被直接丢弃（Part 5 p2）。"
            )
            + pre("""print(int(6.9))
print(int(-6.9))
print(int(3.0))""")
            + pre("""6
-6
3""")
            + p(
                '<code>int(-6.9)</code> 得 <code>-6</code>，是<b>向零截断</b>而不是向下取整；要向下取整得用 <code>//</code> 或第 10 讲的 <code>math.floor</code>。字符串转数字有前提：<code>int("42")</code> 可以，<code>int(" 42 ")</code> 也可以（两端空白被忽略），<code>int("3.7")</code> 不行——抛 <code>ValueError</code>，得先 <code>float("3.7")</code> 再 <code>int()</code>。'
            )
            + h2("八、常见错误与调试提示")
            + cal(
                "warn",
                "把数字拼进字符串",
                '<code>"total: " + 12</code> 抛 TypeError。三种改法：<code>str(12)</code>、交给 print 的 <code>sep</code>、或 <code>f"total: {12}"</code>（推荐）。',
            )
            + cal(
                "warn",
                "引号不配对",
                '<code>print("hello)</code> 报 <code>SyntaxError: unterminated string literal</code>。错误标记常落在行尾，真正的问题在少了一个引号，往回数引号个数即可。',
            )
            + cal(
                "warn",
                "slice 的 stop 少算一位",
                "想取前三字符要写 <code>s[0:3]</code>；写成 <code>s[0:2]</code> 只有两个字符。自检方法：切片结果长度 = <code>stop - start</code>（步长为 1 时）。",
            )
            + cal(
                "tip",
                "先打印再判断",
                "不确定切片或转义结果时，把 <code>len()</code>、单个下标、切片分别打印出来，比盯着代码猜快得多；也可以把字符串放进 <code>repr()</code> 里，让 <code>\\n</code> 显示成两个字符。",
            )
        ),
        kws=K(
            ("comment", "注释", "Anything after # is ignored by the interpreter."),
            (
                "docstring",
                "文档字符串",
                "A string as the first statement of a function; readable with help().",
            ),
            ("escape sequence", "转义序列", "\\n is a newline, \\t is a tab."),
            (
                "immutable",
                "不可变的",
                'A string cannot be changed in place: s[0] = "H" raises TypeError.',
            ),
            ("index", "索引 / 下标", "The position of a character, starting from 0."),
            ("negative index", "负索引", "s[-1] is the last character."),
            ("slice", "切片", "s[start:stop] includes start but excludes stop."),
            ("concatenation", "拼接", "Joining two strings with +."),
            ("repetition", "重复", '"ab" * 3 gives "ababab".'),
            ("len()", "长度", 'len("programming") returns 11.'),
            ("sep", "分隔符", 'print("a", "b", sep="-") prints a-b.'),
            ("end", "结尾字符", 'print("x", end="") suppresses the newline.'),
            ("rounding", "舍入", "round(3.14159, 2) returns 3.14."),
            ("truncation", "截断", "int(6.9) returns 6, dropping the decimals."),
        ),
        examples=(
            qa(
                '例 1　给定 <code>s = "Fundamentals of Programming"</code>，输出它的长度、首字符、末字符、反转串与大写形式。',
                p("把五个操作分开写，输出带标签，便于核对：")
                + pre("""s = "Fundamentals of Programming"

print("length:", len(s))
print("first:", s[0])
print("last:", s[-1])
print("reversed:", s[::-1])
print("upper:", s.upper())""")
                + p("输出：")
                + pre("""length: 27
first: F
last: g
reversed: gnimmargorP fo slatnemadnuF
upper: FUNDAMENTALS OF PROGRAMMING""")
                + p(
                    "逐点解释：<code>len(s)</code> 数到 27（含两个空格）；<code>s[0]</code> 是 F；<code>s[-1]</code> 等价于 <code>s[26]</code>，是 g；<code>s[::-1]</code> 步长为 −1，从末尾倒着走；<code>s.upper()</code> 返回新串，原串不变。"
                ),
            )
            + qa(
                "例 2　把「商品、单价、数量」打印成对齐的收据，并用 <code>sep</code> 画分隔线。",
                p(
                    '思路：表格宽度固定为 20，用 f-string 的 <code>:&lt;12</code>（左对齐）与 <code>:&gt;8</code>（右对齐）拼列；分隔线用 <code>print("-" * 20)</code> 生成。'
                )
                + pre("""item = "Coffee beans"
price = 9.5
qty = 3
total = price * qty

print("ITEM         AMOUNT")
print("-" * 20)
print(f"{item:<12}{total:>8.2f}")
print("-" * 20)
print("TOTAL", f"{total:.2f}", sep=" = ")""")
                + p("输出：")
                + pre("""ITEM         AMOUNT
--------------------
Coffee beans   28.50
--------------------
TOTAL = 28.50""")
                + p(
                    '解释：<code>:&lt;12</code> 把 <code>"Coffee beans"</code> 补到 12 列左对齐；<code>:&gt;8.2f</code> 把 28.5 补到 8 列右对齐并保留两位；最后一行演示 <code>sep=" = "</code> 只在多参数时生效。'
                ),
            )
            + qa(
                "例 3　把总秒数 3725 转成 <code>1:02:05</code> 的形式。",
                p(
                    "思路：小时 = <code>// 3600</code>；余下秒数再除以 60 得分钟；最后 <code>% 60</code> 得秒。分钟与秒要求两位补零，用 f-string 的 <code>:02d</code>。"
                )
                + pre("""total = 3725
h = total // 3600
m = total % 3600 // 60
s = total % 60
print(f"{h}:{m:02d}:{s:02d}")""")
                + pre("""1:02:05""")
                + p(
                    "解释：<code>3725 // 3600 = 1</code>；<code>3725 % 3600 = 125</code>，<code>125 // 60 = 2</code>；<code>3725 % 60 = 5</code>。<code>%</code> 与 <code>//</code> 的配合是「拆分数量」的通用套路，第 5 讲算硬币找零会再遇到。"
                ),
            )
        ),
        practice=(
            ol(
                '判断 <code>"level"</code> 与 <code>"Level"</code> 是否回文，分别输出结果。',
                '从邮箱 <code>"student.name@lut.fi"</code> 里取出用户名与域名两部分。',
                "把金额 1234567.891 打印成 <code>1,234,567.89</code>。",
                '把 <code>"2024-11-20"</code> 改写成 <code>20.11.2024</code>（只用切片与拼接）。',
                "用一条 <code>print</code> 输出 <code>1-2-3-4-5</code>，再用循环外的方式输出 <code>12345</code>（提示：<code>sep</code>）。",
            )
            + det(
                "答案与思路",
                p(
                    '<b>1.</b> 回文判断统一写 <code>s == s[::-1]</code>。<code>"level" == "level"</code> → <code>True</code>；<code>"Level" == "leveL"</code> → <code>False</code>。若要不区分大小写，先 <code>s.lower()</code> 再比较。'
                )
                + p(
                    '<b>2.</b> <code>user, domain = s.split("@")</code> 需要解包（第 8 讲元组）；本讲范围内用 <code>s.split("@")[0]</code> 与 <code>s.split("@")[-1]</code>，得到 <code>student.name</code> 与 <code>lut.fi</code>。'
                )
                + p(
                    '<b>3.</b> <code>print(f"{1234567.891:,.2f}")</code> → <code>1,234,567.89</code>。逗号是千分位分隔符，必须写在 <code>.2f</code> 前面。'
                )
                + p(
                    '<b>4.</b> 年月日各四位两位两位，固定长度最好切：<code>d[8:] + "." + d[5:7] + "." + d[:4]</code> → <code>20.11.2024</code>。若格式可能变化，改用 <code>split("-")</code> 再倒序拼接。'
                )
                + p(
                    '<b>5.</b> <code>print(1, 2, 3, 4, 5, sep="-")</code> → <code>1-2-3-4-5</code>；<code>print(1, 2, 3, 4, 5, sep="")</code> → <code>12345</code>。两题都不要写字符串加法。'
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "切片「含头不含尾」的语义；负索引 <code>s[-1]</code>；<code>sep</code> 与 <code>end</code> 的默认值；字符串不可变的含义；<code>round()</code> 与 <code>int()</code> 的区别。",
            )
            + cal(
                "warn",
                "易错 1　off-by-one",
                "取前三个字符是 <code>s[:3]</code> 不是 <code>s[:2]</code>；取末三位是 <code>s[-3:]</code> 不是 <code>s[-2:]</code>。画格子数一遍再写。",
            )
            + cal(
                "warn",
                "易错 2　把 slice 当修改",
                '<code>s[0:3] = "abc"</code> 对字符串非法（TypeError），切片只能读；要「改」必须拼一个新串并重新赋值给变量。',
            )
            + cal(
                "warn",
                "易错 3　转义漏写或写错",
                '路径 <code>"C:\\temp"</code> 里的 <code>\\t</code> 会被当成制表符；需要字面反斜杠时写 <code>"C:\\\\temp"</code>，或用正斜杠 <code>"C:/temp"</code>。',
            )
            + cal(
                "tip",
                "进阶",
                "<code>round()</code> 的银行家舍入、<code>int()</code> 的向零截断、以及 <code>0.1 + 0.2 != 0.3</code> 这三件事常被拿来出判断题。浮点比较别写 <code>==</code>，写 <code>abs(a - b) &lt; 1e-9</code>，或先 <code>round(a, 5)</code>。",
            )
        ),
        checklist=(
            h2("操作清单")
            + h3("动一段文本之前，先问四件事")
            + st(
                "这段文本的长度是多少？最后一位下标是 <code>len(s) - 1</code>，负索引最后一位是 −1",
                "我要的是「一个字符」还是「一段子串」？一个字符用 <code>s[i]</code>，一段用切片",
                "切片的 stop 要不要 +1？默念一遍「含头不含尾」",
                "结果是只读展示，还是要拼回一个新串？字符串永远不能被原地修改",
            )
            + h3("调试字符串输出")
            + ck(
                "用 <code>repr(s)</code> 看一眼隐藏的 <code>\\n</code> 与 <code>\\t</code>",
                "数字与字符串拼接前先 <code>str()</code>，或直接用 f-string",
                '多值输出先用 <code>sep</code>，不要手工拼 <code>"-"</code>',
                '循环里不想换行时检查是否写了 <code>end=""</code>',
                "切片报空串时，先打印 <code>len(s)</code> 确认没有越界",
            )
        ),
        mapping=tb(
            ("源文件", "页码", "覆盖知识点"),
            (
                "Ch 2 - Part 1 - Comments.pdf",
                "p2–p3",
                "注释动机、<code>#</code> 注释规则、解释器跳过注释",
            ),
            (
                "Ch 2 - Part 2 - Strings.pdf",
                "p2–p6",
                "字符串定义、<code>len()</code>、转义序列表、多行字符串、<code>+</code> 与 <code>*</code>",
            ),
            (
                "Ch 2 - Part 3 - More on strings.pdf",
                "p2–p6",
                "正/负索引、不可变性、切片六种写法、切片重组修改字符串",
            ),
            (
                "Ch 2 - Part 4 - Modify Printing.pdf",
                "p2–p6",
                "<code>sep</code> 与 <code>end</code> 的默认值和任意取值、两者组合",
            ),
            (
                "Ch 2 - Part 5 - Converting ints and floats.pdf",
                "p2",
                "<code>round(x)</code>、<code>int(x)</code> 截断",
            ),
        )
        + p(
            "<b>跳过项：</b>Part 2–4 中标注 <code>Example1.py</code>–<code>example7.py</code> 的截图页只给出代码文件本身（代码已并入本讲示例与正文），不另设页码；Moodle 上的「课程考核 / 作业截止」类行政页不进入本讲。"
        )
        + p(
            "<b>拓展项：</b>docstring 与 <code>help()</code>、相邻字面量隐式拼接、<code>repr()</code> 调试、银行家舍入的解释，都属于在原知识点上补背景，不引入新考点。"
        ),
    )
)

# ============================================================ 4 条件分支
LEC.append(
    L(
        slug="ch04-conditionals",
        tzh="④ 条件分支与 match-case",
        ten="Conditionals, if-elif-else and match-case",
        keywords=[
            "control structure",
            "boolean expression",
            "comparison operator",
            "short-circuit",
            "indentation",
            "block",
            "elif",
            "match-case",
            "wildcard",
            "branch",
            "truthy",
        ],
        files=[
            "if.pdf",
            "if_else.pdf",
            "match_case.pdf",
            "09_Chapter 3_1_Chapter 3 Code Examples_Example1.py",
            "09_Chapter 3_1_Chapter 3 Code Examples_Example8.py",
            "09_Chapter 3_1_Chapter 3 Code Examples_Example10.py",
            "09_Chapter 3_1_Chapter 3 Code Examples_Kiasma_open.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "前三讲的程序是一条直线：从上到下，每行都执行。这一讲让程序第一次出现「分岔」——根据数据的真假决定走哪条路，其余路径直接跳过。这是控制结构（control structure）的起点，也是后面循环、函数里所有判断的基础。"
            )
            + p(
                "上一讲把文本切开、拼好、印出去；这一讲用比较和逻辑运算把文本与数字变成 <code>True</code> / <code>False</code>，再交给 <code>if</code> 决定去留。下一讲用同样的布尔表达式控制循环。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "写出 <code>== != &lt; &gt; &lt;= &gt;=</code> 六种比较，并解释链式比较 <code>x &lt; y &lt; 15</code>",
                "用 <code>and</code> / <code>or</code> / <code>not</code> 组合条件，并说明短路求值的影响",
                "写出缩进正确的 <code>if</code> / <code>if-else</code> / <code>if-elif-else</code>，并解释块的边界",
                "根据取值范围设计互斥、顺序正确的 <code>elif</code> 链",
                "用 <code>match-case</code> 改写长 <code>elif</code> 链，并用 <code>case _</code> 兜底",
            )
        ),
        detail=(
            h2("一、为什么需要分支")
            + p(
                "到目前为止，程序只有顺序结构：第 1 行、第 2 行……全部执行（if.pdf p2）。但现实充满选择：穿什么取决于天气，吃什么取决于忌口。程序也一样，需要「满足条件才做」。"
            )
            + p("控制结构（control structure）让执行顺序依赖数据。写法极其简单：")
            + pre("""age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")""")
            + p(
                "读法：<code>if</code> 后面是条件，条件为真执行缩进的那一块；<code>else</code> 后面是条件为假时执行的那一块。条件本身是一个<b>布尔表达式</b>（boolean expression），值只能是 <code>True</code> 或 <code>False</code>。"
            )
            + h2("二、布尔表达式：比较运算符")
            + h3("2.1 六种比较")
            + tb(
                ("运算符", "含义", "例子（x = 5, y = 10）", "结果"),
                (
                    "<code>==</code>",
                    "等于",
                    "<code>x == y</code>",
                    "<code>False</code>",
                ),
                (
                    "<code>!=</code>",
                    "不等于",
                    "<code>x != y</code>",
                    "<code>True</code>",
                ),
                (
                    "<code>&gt;</code>",
                    "大于",
                    "<code>x &gt; y</code>",
                    "<code>False</code>",
                ),
                (
                    "<code>&lt;</code>",
                    "小于",
                    "<code>x &lt; y</code>",
                    "<code>True</code>",
                ),
                (
                    "<code>&gt;=</code>",
                    "大于等于",
                    "<code>x &gt;= y</code>",
                    "<code>False</code>",
                ),
                (
                    "<code>&lt;=</code>",
                    "小于等于",
                    "<code>x &lt;= y</code>",
                    "<code>True</code>",
                ),
            )
            + p(
                "<code>==</code> 是比较，<code>=</code> 是赋值，这两个符号永远不要写混。<code>x = y</code> 不会返回真假，它会把 y 的值塞进 x，然后 <code>if x = y:</code> 直接是语法错误。"
            )
            + h3("2.2 链式比较")
            + p(
                "数学里的 <code>0 &lt; x &lt; 10</code> 在 Python 里可以直接写，等价于 <code>0 &lt; x and x &lt; 10</code>，而且中间那个 x 只计算一次："
            )
            + pre("""x = 5
y = 10
print(x < y < 15)
print(0 <= x <= 5)""")
            + pre("""True
True""")
            + h3("2.3 字符串比较")
            + p(
                '字符串按字符的编码逐位比较，本质上就是字典序（lexicographic order）。规则有三条：从左往右逐字符比，第一个不同的字符决定大小；前缀更短的更小（<code>"ab" &lt; "abc"</code>）；大写字母排在小写字母前面（编码 65 起 vs 97 起）。'
            )
            + pre("""string1 = "hello"
string2 = "world"
print(string1 == string2)
print(string1 < string2)
print("Hello" < "hello")
print("apple" < "banana")""")
            + pre("""False
True
True
True""")
            + p("字符串不能和数字比大小（Example2 的最后一行）：")
            + pre("""print("banana" > 5)""")
            + pre("""TypeError: '>' not supported between instances of 'str' and 'int'
""")
            + p(
                '原因是两种类型没有定义比较规则。想比「长度」必须先取 <code>len()</code>：<code>len("banana") &lt; 5</code> 是 <code>False</code>。'
            )
            + h3("2.4 浮点比较")
            + p(
                "浮点数在内存中是近似值（第 1 讲的数据类型、Extra reading 都提过），所以下面这行看起来该真、其实为假："
            )
            + pre("""print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)""")
            + pre("""0.30000000000000004
False""")
            + p(
                "判断两个浮点数「相等」要允许误差：<code>abs(a - b) &lt; 1e-9</code>，或先把两边都 <code>round(a, 5)</code> 再比。"
            )
            + h2("三、逻辑运算符")
            + h3("3.1 and / or / not")
            + tb(
                ("写法", "含义", "为真的条件"),
                ("<code>a and b</code>", "并且", "a、b 都为真"),
                ("<code>a or b</code>", "或者", "至少一个为真"),
                ("<code>not a</code>", "取反", "a 为假"),
            )
            + pre("""a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not False:", not False)""")
            + pre("""a and b: False
a or b: True
not a: False
not False: True""")
            + p(
                "优先级从高到低是 <code>not</code> → <code>and</code> → <code>or</code>，比较运算符又高于它们。所以 <code>not a and b</code> 等于 <code>(not a) and b</code>；<code>a == 1 or b == 2 and c == 3</code> 等于 <code>(a == 1) or ((b == 2) and (c == 3))</code>。条件一复杂就加括号，读代码的人会感谢你。"
            )
            + h3("3.2 短路求值")
            + p(
                "<code>and</code> 左侧为假时右边根本不看；<code>or</code> 左侧为真时右边也根本不看。这叫短路（short-circuit），Example4 用一个未定义的变量演示了它："
            )
            + pre("""a = True
b = False
# c 未定义

print(a or c)   # True：左边已真，不再看 c
print(b and c)  # False：左边已假，不再看 c

# 下面两行会报 NameError，因为真的去看了 c
# print(b or c)
# print(a and c)""")
            + p(
                "这解释了两件实用的事：一是 <code>if x != 0 and 10 / x > 2:</code> 不必担心除零，因为 <code>x != 0</code> 为假时右边被跳过；二是「先判断再访问」的写法是安全的。反过来，如果短路掩盖了本应暴露的错误，调试时会更难——这也是为什么 Example4 把会报错的两行注释掉而不是删掉。"
            )
            + cal(
                "warn",
                "and / or 返回的是操作数，不是 True/False",
                'Python 里 <code>True and "x"</code> 得 <code>"x"</code>，<code>False or "y"</code> 得 <code>"y"</code>，<code>0 or 5</code> 得 5。放在 <code>if</code> 里结果一样（非空串、非零数都当真），但如果把表达式结果直接赋给变量，拿到的是那个操作数。初学阶段建议条件里只放比较与逻辑运算，别依赖这个特性。',
            )
            + h2("四、if 语句与缩进")
            + h3("4.1 语法骨架")
            + p(
                "基本语法（if.pdf p3）：<code>if</code> 关键字 → 条件 → 冒号 → 换行 + 缩进的块。"
            )
            + pre("""temperature = 20
if temperature > 15:
    print("It's warm outside!")""")
            + p(
                "冒号表示「下面开始是这个 if 的块」。块内的行必须比 <code>if</code> 多缩进（通常 4 个空格），块在缩进退回时结束（if.pdf p6）。"
            )
            + h3("4.2 缩进是语法，不是风格")
            + p(
                "别的语言用花括号 <code>{}</code> 划块，缩进只是好看；Python 直接用缩进定义块（if.pdf p4）。漏缩进会被判为「期望一个缩进块」："
            )
            + pre("""if 5 > 2:
print("Five is greater than two!")""")
            + pre(
                """IndentationError: expected an indented block after 'if' statement on line 1"""
            )
            + p(
                "同一个块内缩进量必须完全一致（Example6）。下面这段第一行缩进 1 个空格、第二行缩进 8 个，Python 无法判断它们是否属于同一块："
            )
            + pre("""if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")""")
            + pre("""IndentationError: unexpected indent""")
            + p(
                "还有两条实务规则：<b>不要混用空格与 Tab</b>——不同编辑器对 Tab 的宽度解释不同，切编辑器就会出错；IDLE 会在你回车时自动补上缩进，省事但也容易让人忘记检查层级。"
            )
            + h3("4.3 块在哪里结束")
            + p("缩进退回的那一行不属于 if 的块（Example7）：")
            + pre("""i = 10

if i > 15:
    print("variable i is less than 15")
print("I am NOT in if")""")
            + pre("""I am NOT in if""")
            + p(
                '条件为假，块内那行被跳过；没有缩进的 <code>print("I am NOT in if")</code> 与 if 无关，照常执行。顺带一提，示例里那句提示文字写反了（i 是 10，条件 <code>i &gt; 15</code> 为假），这类「注释与代码不一致」的 bug 比语法错误更难发现——读代码时以代码为准。'
            )
            + h2("五、if-else：二选一")
            + p(
                "写法（if_else.pdf p2）：条件为真走第一块，为假走 <code>else</code> 块，两块必有一块执行。"
            )
            + pre("""a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

if a > b:
    print("The largest integer is", a)
else:
    print("The largest integer is", b)""")
            + p(
                '输入 <code>7</code> 与 <code>3</code>，输出 <code>The largest integer is 7</code>。注意 <code>input()</code> 返回字符串，必须 <code>int()</code> 之后再比，否则比的是字典序（<code>"10" &lt; "9"</code> 为真）。'
            )
            + h2("六、if-elif-else：多选一")
            + h3("6.1 结构与执行规则")
            + p(
                "<code>elif</code> 是 else if 的缩写（if_else.pdf p4–p5）。执行顺序是从上往下逐个检查，<b>第一个为真的块执行完，整个链条就结束</b>，后面的 <code>elif</code> / <code>else</code> 全部跳过。"
            )
            + tb(
                ("规则", "说明"),
                ("只有一个块执行", "哪怕多个条件同时为真，也只走最上面那个"),
                ("最多一个 else", "每个 if 链最多一个 else，且必须放最后"),
                ("elif 可以有多个", "想排几个排几个，顺序即优先级"),
                ("else 可以省略", "不需要兜底时省略，什么都不做"),
                ("条件互斥靠你保证", "Python 不会替你检查区间是否重叠"),
            )
            + h3("6.2 顺序决定正确性")
            + p("成绩等级的例子（if_else.pdf p6）是经典：")
            + pre("""score = 85

if score >= 90:
    grade = 5
elif score >= 80:
    grade = 4
elif score >= 70:
    grade = 3
elif score >= 60:
    grade = 2
elif score >= 50:
    grade = 1
else:
    grade = 0

print("Grade:", grade)""")
            + pre("""Grade: 4""")
            + p(
                "为什么能从大到小这么写？因为 85 已经满足了 <code>&gt;= 80</code>，不会再往下看。如果把顺序写反（先判 <code>&gt;= 50</code>），85 会命中第一条，直接得 1 分——这就是条件链最常见的逻辑错误：<b>范围宽的放前面，后面的永远轮不到</b>。"
            )
            + p(
                "规则总结：判断区间时，要么按「从大到小」写 <code>&gt;=</code>，要么按「从小到大」写 <code>&lt;</code> 并让每条上界收紧，总之让条件互斥且覆盖全集。"
            )
            + h3("6.3 一个完整的业务例子：运费")
            + p("Example10 把订单金额映射到运费档位，结构与本讲完全一致：")
            + pre("""order_value = float(input("Enter the total order value in EUR: "))

if order_value >= 100:
    shipping_cost = 0
elif order_value >= 50:
    shipping_cost = 5
elif order_value >= 20:
    shipping_cost = 10
else:
    shipping_cost = 15

print("The shipping cost for your order is " + str(round(shipping_cost, 2)) + " EUR.")""")
            + p(
                "输入 <code>63.5</code>，输出 <code>The shipping cost for your order is 5 EUR.</code>。三个要点：<code>float()</code> 而不是 <code>int()</code>（金额有小数）；<code>str()</code> 把数字拼进字符串；边界值 100、50、20 都归入「较便宜」的一档，因为用的是 <code>&gt;=</code>。"
            )
            + h2("七、match-case：值匹配的更整齐写法")
            + h3("7.1 语法")
            + p(
                "<code>match-case</code> 是 Python 3.10 引入的（match_case.pdf p2），作用类似 C / Java 的 <code>switch</code>，用来替代一长串「同一个变量反复比较」的 <code>elif</code>。"
            )
            + pre("""status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status code")""")
            + pre("""Not Found""")
            + p(
                "下划线 <code>_</code> 是通配符（wildcard），兜住所有没匹配上的值（match_case.pdf p3）。它等价于 <code>else</code>，但只能出现一次且习惯放最后。"
            )
            + h3("7.2 一个 case 匹配多个值")
            + p("用竖线 <code>|</code> 把多个候选写在一起（match_case.pdf p4）：")
            + pre("""fruit = "banana"

match fruit:
    case "apple" | "banana" | "orange":
        print("This is a common fruit.")
    case _:
        print("This is not a common fruit.")""")
            + pre("""This is a common fruit.""")
            + p(
                "可以匹配数字、字符串、布尔值。注意<code> | </code>是「或」，不是正则里的管道，两侧只能是字面量或模式，不能写表达式。"
            )
            + h3("7.3 完整例子：博物馆开放时间")
            + p("Kiasma_open.py 是课程给的完整练习：给定星期几，输出开放时间。")
            + pre("""day = input("Give a day (Mon/Tue/Wed/Thu/Fri/Sat/Sun): ")

match day:
    case "Mon":
        print("Closed")
    case "Tue" | "Fri":
        print("Open 10-20")
    case "Wed" | "Thu":
        print("Open 10-18")
    case "Sat" | "Sun":
        print("Open 10-17")
    case _:
        print("There is no such day")""")
            + p(
                "输入 <code>Wed</code> 输出 <code>Open 10-18</code>；输入 <code>mon</code>（小写）输出 <code>There is no such day</code>——<code>match</code> 是精确匹配，大小写敏感，所以用户输入最好先规范成 <code>day.strip().capitalize()</code> 或统一转小写后比较。"
            )
            + h3("7.4 match 与 elif 链怎么选")
            + tb(
                ("场景", "推荐写法"),
                (
                    "同一个变量与若干固定值比较",
                    "<code>match-case</code>，一眼看出分支表",
                ),
                (
                    "比较范围（<code>&gt;=</code>、<code>&lt;</code>）",
                    "<code>if-elif</code>，match 不适合区间",
                ),
                ("条件涉及多个变量", "<code>if-elif</code>"),
                ("需要兜底分支", "两者都行：<code>case _</code> 或 <code>else</code>"),
            )
            + p(
                "功能上 match 并不比 elif 强，它换来的是可读性；所以考试里两种写法都要会读、会改。"
            )
            + cal(
                "warn",
                "case 后面写裸变量名会「捕获」一切",
                '<code>case day:</code> 不是「当值等于变量 day 时」，而是「新建一个叫 day 的变量并匹配任何值」，于是后面的 case 永远轮不到。要比较变量，写 <code>case "Mon":</code> 这样的字面量，或先把候选值放进常量。<code>_</code> 是唯一安全的通配符。',
            )
            + h2("八、常见错误清单")
            + cal(
                "warn",
                "把 == 写成 =",
                "<code>if x = 5:</code> 是语法错误；<code>if x = 5</code> 想表达的「判断相等」应写 <code>==</code>。反过来 <code>x == 5</code> 单独一行只是算了个真假然后丢掉，不报错，也很难发现。",
            )
            + cal(
                "warn",
                "漏冒号",
                "<code>if x &gt; 5</code> 后面没有冒号，报 <code>SyntaxError: expected ':'</code>。冒号是块的开场白，<code>if</code> / <code>elif</code> / <code>else</code> / <code>for</code> / <code>while</code> / <code>def</code> 全都要。",
            )
            + cal(
                "warn",
                "elif 顺序反了",
                "区间判断从宽到窄、从上到下必须单调；写成 <code>&gt;= 50</code> 在前，高分也会掉进低档。写完用边界值（49、50、89、90）各测一遍。",
            )
            + cal(
                "warn",
                "把非空字符串当条件",
                '<code>if "no":</code> 恒为真，因为非空字符串为真。判断用户回答要写 <code>if answer == "no":</code>，不能只写字符串本身。',
            )
            + cal(
                "tip",
                "先画决策表再写代码",
                "把输入区间与期望输出列成两列，检查是否覆盖全集、是否重叠；然后照表写 elif，顺序自然正确。这比写完再调试快得多。",
            )
        ),
        kws=K(
            (
                "control structure",
                "控制结构",
                "if, for and while change the order of execution.",
            ),
            (
                "boolean expression",
                "布尔表达式",
                "An expression that evaluates to True or False.",
            ),
            ("comparison operator", "比较运算符", "==, !=, <, >, <=, >=."),
            ("chained comparison", "链式比较", "0 <= x <= 5 means 0 <= x and x <= 5."),
            ("logical operator", "逻辑运算符", "and, or, not."),
            (
                "short-circuit",
                "短路求值",
                "or stops at the first true operand; and stops at the first false one.",
            ),
            ("indentation", "缩进", "Indentation defines the block in Python."),
            ("block", "代码块", "The indented statements controlled by if."),
            (
                "elif",
                "否则如果",
                "Short for else if; checked only if the previous conditions failed.",
            ),
            (
                "match-case",
                "模式匹配语句",
                "Introduced in Python 3.10; an alternative to long elif chains.",
            ),
            ("wildcard", "通配符", "case _ catches every value that did not match."),
            (
                "lexicographic order",
                "字典序",
                '"Hello" < "hello" because uppercase letters come first.',
            ),
            (
                "mutually exclusive",
                "互斥的",
                "Only one branch of an if-elif chain can run.",
            ),
        ),
        examples=(
            qa(
                "例 1　输入一个整数，输出它是正数、零还是负数，并额外输出它的绝对值。",
                p(
                    "思路：先按「大于 0 / 等于 0 / 其余」三分支；绝对值用 <code>abs()</code>（第 2 讲的内置函数），不要手写两遍分支。"
                )
                + pre("""num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

print("Absolute value:", abs(num))""")
                + p("输入 <code>-7</code>，输出：")
                + pre("""Negative number
Absolute value: 7""")
                + p(
                    "解释：三个分支互斥且覆盖全部整数；<code>abs()</code> 让「求绝对值」不必再写一个 if。注意这里用 <code>int()</code>，若允许小数要改 <code>float()</code>，但那样 <code>num == 0</code> 就要写成 <code>abs(num) &lt; 1e-9</code>。"
                ),
            )
            + qa(
                "例 2　输入年份，判断是否闰年。",
                p(
                    "规则：能被 4 整除，但不能被 100 整除；或者能被 400 整除。把「或者」直接翻译成 <code>or</code>，把「但是」翻译成 <code>and not</code>。"
                )
                + pre("""year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")""")
                + p(
                    "输入 <code>1900</code> → <code>1900 is not a leap year</code>；输入 <code>2000</code> → <code>2000 is a leap year</code>（被 400 整除）；输入 <code>2024</code> → 闰年。"
                )
                + p(
                    "解释：括号不能省。<code>and</code> 优先级高于 <code>or</code>，这里刚好符合预期，但写清楚括号能让读者一眼确认分组。测试时至少覆盖 1900（例外）、2000（400 的例外之例外）、2024（普通闰年）、2023（普通平年）四个边界。"
                ),
            )
            + qa(
                "例 3　用 <code>match-case</code> 实现一个简易计算器：输入运算符与两个数，输出结果。",
                p(
                    '思路：用 <code>case "+"</code> 等字面量分支；除零要在分支里单独判，避免 <code>ZeroDivisionError</code>（第 11 讲会系统处理异常）。'
                )
                + pre("""op = input("Operator (+ - * /): ")
a = float(input("First number: "))
b = float(input("Second number: "))

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)
    case _:
        print("Unknown operator")""")
                + p(
                    "输入 <code>*</code>、<code>3</code>、<code>4</code> 输出 <code>12.0</code>；输入 <code>/</code>、<code>1</code>、<code>0</code> 输出 <code>Cannot divide by zero</code>。"
                )
                + p(
                    "解释：<code>match</code> 只负责「选哪个运算符」，除数是否为零是分支内的二级判断——这种「外层匹配 + 内层条件」的嵌套在菜单类程序里非常常见。"
                ),
            )
        ),
        practice=(
            ol(
                "输入三个整数，按从大到小输出（先比较再交换，不要用 <code>sorted</code>）。",
                "输入百分制成绩，按 90/80/70/60/50 输出 5/4/3/2/1/0 等级，并处理「输入不在 0–100」的情况。",
                "输入一个字符，判断它是大写字母、小写字母、数字还是其他（提示：可以用比较，也可以查第 2 讲的字符串方法）。",
                "用 <code>match-case</code> 把 Kiasma 例子改成「输入小写也认」的版本。",
                "输入 BMI 的两个分量（体重 kg、身高 m），按 <code>&lt;18.5</code> / <code>18.5–24.9</code> / <code>25–29.9</code> / <code>&gt;=30</code> 输出四档结论。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> 三个数排序的经典写法是三次两两交换：先让 <code>a &gt;= b</code>（否则交换），再让 <code>a &gt;= c</code>，最后让 <code>b &gt;= c</code>。交换用 <code>a, b = b, a</code>（第 8 讲元组解包），本讲范围内也可用临时变量 <code>t = a; a = b; b = t</code>。"
                )
                + p(
                    '<b>2.</b> 先判合法性再判等级：<code>if score &lt; 0 or score &gt; 100: print("Invalid")</code>，否则接原来的 elif 链。这正是「先做守卫判断（guard clause）」的思路，比把非法值塞进等级链更清晰。'
                )
                + p(
                    '<b>3.</b> 用链式比较最直观：<code>if "A" &lt;= ch &lt;= "Z": ... elif "a" &lt;= ch &lt;= "z": ... elif "0" &lt;= ch &lt;= "9": ...</code>。也可以用 <code>ch.isupper() / ch.islower() / ch.isdigit()</code>（第 2 讲字符串方法）。注意 <code>isdigit()</code> 对空串返回 False。'
                )
                + p(
                    '<b>4.</b> 在读入后统一大小写：<code>day = input(...).strip().capitalize()</code>，这样 <code>mon</code>、<code>MON</code>、<code>" Mon "</code> 都变成 <code>Mon</code>，match 分支不用改。<code>capitalize()</code> 只把首字母大写、其余小写，正好匹配 <code>Mon</code> 形式。'
                )
                + p(
                    "<b>5.</b> <code>bmi = weight / height ** 2</code>，然后四档 elif，注意边界：<code>&lt;18.5</code>、<code>&lt;25</code>、<code>&lt;30</code>、其余。用「上界递增」的写法保证互斥：<code>if bmi &lt; 18.5: ... elif bmi &lt; 25: ...</code>。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "<code>if-elif-else</code> 的执行顺序与「只执行一个块」；缩进定义块；字符串比较的字典序；<code>and</code>/<code>or</code> 的短路；<code>match-case</code> 与 <code>case _</code>。",
            )
            + cal(
                "warn",
                "易错 1　elif 顺序导致区间失效",
                "85 分被 <code>&gt;= 50</code> 先截住就得 1 分。写完拿边界值 49/50/59/60/89/90 走一遍。",
            )
            + cal(
                "warn",
                "易错 2　漏冒号与缩进错误",
                "<code>IndentationError</code> 分两种：<code>expected an indented block</code>（该缩进没缩进）与 <code>unexpected indent</code>（不该缩进却缩了）。看错误行号，往上找它所属的 <code>if</code>。",
            )
            + cal(
                "warn",
                "易错 3　input 没转换就比大小",
                '<code>input()</code> 返回字符串，<code>"9" &gt; "10"</code> 为真。比较数字前必须 <code>int()</code> / <code>float()</code>。',
            )
            + cal(
                "tip",
                "进阶",
                "浮点相等用 <code>abs(a - b) &lt; 1e-9</code>；<code>match</code> 里裸变量名是捕获而非比较；<code>and</code>/<code>or</code> 返回操作数而非布尔值。这三点是判断题与改错题的常客。",
            )
        ),
        checklist=(
            h2("操作清单")
            + h3("写 if 之前")
            + st(
                "把条件写成一句能判真假的话，例如「年龄大于等于 18」→ <code>age &gt;= 18</code>",
                "确认参与比较的两边类型一致：数字比数字、字符串比字符串",
                "列出所有分支，检查是否互斥、是否覆盖全部情况",
                "确定顺序：区间判断从宽到窄或从窄到宽，只能选一个方向",
                "写完用边界值各测一次",
            )
            + h3("缩进与语法自检")
            + ck(
                "每个 <code>if</code> / <code>elif</code> / <code>else</code> 行末都有冒号",
                "同一块内缩进量完全一致，没有混用 Tab 与空格",
                "块的结束靠缩进退回，退回后的语句不属于 if",
                "<code>==</code> 用于比较，<code>=</code> 只用于赋值",
                "条件里没有写「永远为真」的非空字符串",
            )
        ),
        mapping=tb(
            ("源文件", "页码", "覆盖知识点"),
            (
                "if.pdf",
                "p2–p6",
                "控制结构动机、<code>if</code> 语法、冒号、缩进定义块、缩进错误、Tab 与空格、块结束",
            ),
            (
                "if_else.pdf",
                "p2–p7",
                "<code>if-else</code> 二选一、<code>elif</code> 链、成绩等级例子、单块执行规则",
            ),
            (
                "match_case.pdf",
                "p2–p4",
                "<code>match-case</code> 起源（3.10）、<code>case _</code>、<code>|</code> 多值匹配",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example1.py",
                "全文",
                "六种比较与链式比较的正例",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example2.py",
                "全文",
                "字符串比较、大写在前、<code>str</code> 与 <code>int</code> 不可比",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example3.py",
                "全文",
                "逻辑运算组合与括号",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example4.py",
                "全文",
                "短路求值与未定义变量",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example5.py–Example7.py",
                "全文",
                "条件为假不执行、缩进不一致、块结束",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example8.py",
                "全文",
                "取两个数的较大者",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Example10.py",
                "全文",
                "运费分档、<code>float()</code> 与 <code>str()</code> 拼接",
            ),
            (
                "09_Chapter 3_1_Chapter 3 Code Examples_Kiasma_open.py",
                "全文",
                "<code>match-case</code> 完整程序、<code>|</code> 分支、兜底",
            ),
        )
        + p(
            "<b>跳过项：</b>Moodle 第 3 章的考核说明、作业截止页属于行政信息，不构成知识点，已按第 1 讲的课程结构说明处理；纯截图页（无文字）不单列页码。"
        )
        + p(
            "<b>拓展项：</b>浮点相等判断、<code>and</code>/<code>or</code> 返回操作数、<code>match</code> 中裸变量名的捕获语义、守卫判断（guard clause）写法，都是在原知识点边界上补的常见坑，未引入新语法考点。"
        ),
    )
)

# ============================================================ 5 循环
_D5 = (
    h2("一、重复这件事：loop 与 iteration")
    + p(
        "课件给出的场景很具体：要把这门课所有学生的邮箱逐个发一遍邀请（Part 1 p3–p6）。手写一条语句发一个人，人数一多就无法维护；循环把「同一件事做 N 次」压成一小段代码。"
    )
    + p(
        "两个术语必须分清：<b>循环</b>（loop）是「重复执行一段代码」的结构；<b>迭代</b>（iteration）是其中<b>一次</b>执行（Part 1 p7）。说「这个循环跑了 5 次迭代」，意思是循环体执行了 5 遍。"
    )
    + tb(
        ("术语", "含义", "说明"),
        ("loop", "循环", "A construct that repeats a block of code."),
        ("iteration", "迭代 / 一次循环", "One execution of the loop body."),
        ("loop body", "循环体", "The indented statements inside the loop."),
        (
            "loop variable",
            "循环变量",
            "The variable that takes each item of the sequence in turn.",
        ),
        (
            "iterable",
            "可迭代对象",
            "Anything a for loop can walk through: a string, a list, a range.",
        ),
        ("infinite loop", "死循环", "A loop whose condition never becomes False."),
    )
    + p(
        "Python 只有两种循环（Part 1 p8）：<code>for</code> 用来遍历一个已知序列，<code>while</code> 用来在条件成立时反复执行。选哪一种，取决于你「知不知道要做多少次」。"
    )
    + h2("二、for 循环：遍历序列")
    + h3("2.1 执行流程")
    + p(
        "fork 的语义是：把序列里的元素<b>依次</b>取出来，每次取一个赋给循环变量，然后执行一遍循环体（Part 2 p2）。序列走完，循环结束。"
    )
    + pre("""for <variable> in <sequence>:
    <do something>""")
    + p(
        "<code>sequence</code> 可以是字符串、列表、<code>range()</code> 产生的数字序列，或任何可迭代对象。<code>for</code> 行末的冒号与循环体的缩进，规则与第 4 讲的 <code>if</code> 完全一样。"
    )
    + pre("""for i in [10, 20, 30]:
    print("i is", i)
print("loop finished")""")
    + pre("""i is 10
i is 20
i is 30
loop finished""")
    + p(
        "注意最后一行没有缩进，它在循环结束后执行一次。循环变量 <code>i</code> 在循环结束后仍然存在，值是最后一次赋的值（这里是 30）——这是 Python 的行为，不要依赖它，但读别人代码时要认得。"
    )
    + h3("2.2 遍历字符串")
    + p(
        "字符串是字符的序列，所以可以直接被 <code>for</code> 遍历（Part 2 p4）。L4E1 用它提取一句话里所有大写字母，把 <code>Central Processing Unit</code> 变成 <code>CPU</code>："
    )
    + pre("""sentence = input("Enter a sentence with capital letters: ")
print("The capital letters of", sentence, "are:")
for character in sentence:
    if character.isupper():
        print(character, end="")""")
    + p(
        '输入 <code>Central Processing Unit</code>，输出 <code>The capital letters of Central Processing Unit are:</code> 换行后紧跟 <code>CPU</code>。<code>end=""</code> 让字母连在一起而不是各占一行（第 3 讲）。'
    )
    + h3("2.3 遍历列表")
    + p(
        "L4E2 的对比很直观：手写 <code>print(values[1])</code>、<code>print(values[4])</code> 只能覆盖几个元素，换一个列表就得重写；<code>for</code> 一次解决（Part 2 p5）。"
    )
    + pre("""values = [1, 2, 3, 7, 44, 98, 360]
for val in values:
    print(val)""")
    + p(
        "循环变量 <code>val</code> 每次拿到的是<b>元素本身</b>，不是下标。需要下标时用第 8 讲的 <code>range(len(...))</code> 或 <code>enumerate()</code>。"
    )
    + h3("2.4 空序列与「零次迭代」")
    + pre("""for x in []:
    print("never printed")
print("done")""")
    + pre("""done""")
    + p(
        "空列表、空字符串、<code>range(0)</code> 都让循环体一次也不执行。这不是错误，而是「没有东西可做」的正常情况——统计类程序要考虑这种输入。"
    )
    + h2("三、range()：生成数字序列")
    + h3("3.1 三种参数形式")
    + p(
        "<code>range()</code> 最多接受三个参数：起点、终点、步长（Part 2 p6）。起点默认 0，步长默认 1，终点<b>必须给</b>。"
    )
    + tb(
        ("写法", "产生的数字", "迭代次数"),
        ("<code>range(5)</code>", "0, 1, 2, 3, 4", "5"),
        ("<code>range(1, 5)</code>", "1, 2, 3, 4", "4"),
        ("<code>range(1, 10, 2)</code>", "1, 3, 5, 7, 9", "5"),
        ("<code>range(11, 0, -2)</code>", "11, 9, 7, 5, 3, 1", "6"),
        ("<code>range(0)</code>", "（空）", "0"),
    )
    + h3("3.2 不含 stop：off-by-one 的根源")
    + p(
        "<code>range(start, stop)</code> 和切片一样<b>含头不含尾</b>。想累加 1 到 100，必须写 <code>range(1, 101)</code>（Part 2 p7 的示例正是 <code>range(0, 10)</code> 给出 0–9）："
    )
    + pre("""seq_sum = 0
for i in range(1, 100 + 1):
    seq_sum = seq_sum + i
print("1 + 2 + ... + 100 =", seq_sum)""")
    + pre("""1 + 2 + ... + 100 = 5050""")
    + p(
        "写 <code>100 + 1</code> 而不是硬写 <code>101</code>，是为了让读代码的人一眼看出「到 100 为止」。"
    )
    + h3("3.3 负步长")
    + pre("""seq_mul = 1
for i in range(11, 0, -2):
    seq_mul = seq_mul * i
print("11 * 9 * ... * 1 =", seq_mul)""")
    + pre("""11 * 9 * ... * 1 = 10395""")
    + p(
        "步长为负时起点必须大于终点，否则一次都不执行（例如 <code>range(0, 11, -2)</code> 是空序列）。"
    )
    + h3("3.4 range 不是列表")
    + pre("""r = range(3)
print(r)
print(list(r))""")
    + pre("""range(0, 3)
[0, 1, 2]""")
    + p(
        "<code>range</code> 对象是惰性序列：它不把数字全部装进内存，而是按需产生。所以 <code>print(r)</code> 只显示 <code>range(0, 3)</code>；要看到内容得用第 8 讲的 <code>list()</code> 转换。"
    )
    + h2("四、while 循环：条件成立就继续")
    + h3("4.1 执行流程")
    + p(
        "<b>先判断，再执行</b>（Part 3 p2–p4）：条件为真执行循环体，执行完再回来判断；条件为假立刻退出。如果一开始条件就为假，循环体一次都不执行。"
    )
    + pre("""while <expression>:
    <do something>""")
    + pre("""count = 3
while count > 0:
    print("count =", count)
    count = count - 1
print("liftoff")""")
    + pre("""count = 3
count = 2
count = 1
liftoff""")
    + h3("4.2 三件套：初始化、条件、更新")
    + p("写 <code>while</code> 必须同时安排好三件事，缺一件就是死循环：")
    + st(
        "初始化：在循环<b>之前</b>给控制变量一个初值",
        "条件：写出「什么时候继续」的布尔表达式",
        "更新：在循环体<b>内</b>改变控制变量，使它最终能让条件变假",
    )
    + p(
        "下面这段就是典型的死循环——条件永远为真，因为循环体里没有改变 <code>count</code>："
    )
    + pre("""count = 3
while count > 0:
    print("forever")""")
    + p(
        "真实运行会刷屏，需要 <kbd>Ctrl</kbd>+<kbd>C</kbd> 中断，Python 抛 <code>KeyboardInterrupt</code>（第 11 讲）。"
    )
    + h3("4.3 while True + break")
    + p(
        "另一种常见形态是「先无限循环，满足条件时 <code>break</code> 跳出」。条件复杂、退出点分散时，这比把所有条件塞进一个 <code>while</code> 表达式更清楚（Part 4 p3 的例子正是这个结构）："
    )
    + pre("""while True:
    n = int(input("Please enter a number: "))
    if n % 13 == 0:
        print(n, "is divisible by 13")
        break""")
    + p("这段程序不断要用户输入，直到输入一个能被 13 整除的数才停。")
    + h3("4.4 用 while 做输入驱动的循环")
    + p(
        "L4E4 用哨兵值（sentinel）结束循环：用户输入 <code>-1</code> 表示退出，其余输入按及格线给结论（Part 3 p5–p6）。"
    )
    + pre("""score = ""
while score != "-1":
    score = input("Please input score OR -1 to quit: ")
    if score == "-1":
        print("Bye!")
    elif float(score) >= 50:
        print("Pass")
    else:
        print("Reject")""")
    + p(
        '要点：<code>score</code> 必须先在循环外初始化成 <code>""</code>，否则第一次判断时变量还不存在（<code>NameError</code>）；比较用字符串 <code>"-1"</code>，因为 <code>input()</code> 返回字符串，若先 <code>float()</code> 再比较就会在输入 <code>-1</code> 时也被当成数字。'
    )
    + p(
        "什么时候用 <code>while</code> 而不是 <code>for</code>？判断标准只有一条：<b>循环次数事先未知</b>（等用户输入、等某个条件成立）就用 <code>while</code>；要遍历一个已知序列就用 <code>for</code>。"
    )
    + h2("五、break 与 continue")
    + p("两个语句都只能写在循环里，作用完全不同（Part 4 p2–p6）：")
    + tb(
        ("语句", "作用", "之后的代码", "典型场景"),
        (
            "<code>break</code>",
            "立刻结束<b>整个</b>循环",
            "循环体剩余部分不执行，循环外继续",
            "找到了要找的东西，不必再找",
        ),
        (
            "<code>continue</code>",
            "结束<b>本轮</b>，进入下一轮",
            "本轮剩余部分跳过",
            "跳过不符合条件的元素",
        ),
    )
    + p(
        "L4E6 用 <code>continue</code> 打印列表里的偶数：遇到奇数就跳过本轮，不执行后面的 <code>print</code>。"
    )
    + pre("""list_numbers = list(range(2, 65, 3))
print("List:", list_numbers)
for x in list_numbers:
    if x % 2 != 0:
        continue
    print(x, end=", ")""")
    + pre("""List: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62]
2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, """)
    + p(
        "注意输出末尾多了一个逗号与空格——这是「最后一个元素也照样加分隔符」的经典小瑕疵，正式输出时要单独处理。"
    )
    + cal(
        "warn",
        "continue 放在更新语句之前会变成死循环",
        "<code>while</code> 循环里如果 <code>i = i + 1</code> 写在 <code>continue</code> 之后，被 <code>continue</code> 跳过的那一轮就不会更新 <code>i</code>，条件永远为真。规则：<b>更新语句放在循环体最前面</b>，或改用 <code>for</code>。",
    )
    + cal(
        "warn",
        "break 只跳出最内层",
        "嵌套循环里 <code>break</code> 只结束它所在的那一层（Part 4 p2）。要一次跳出两层，得用标志变量或在函数里 <code>return</code>（第 6 讲）。",
    )
    + h2("六、嵌套循环")
    + p(
        "循环体里再写一个循环，就是嵌套（Part 5 p2）。它用于「二维」的问题：矩阵的每个元素、表格的每一行每一列、图形的每一行每一列。外层每走一步，内层完整走一遍，所以总执行次数是<b>两层次数相乘</b>。"
    )
    + p(
        "L4E7 的乘法表是最小完整例子：外层 <code>i</code> 控制行，内层 <code>j</code> 只走到 <code>i</code>，于是第 i 行有 i 个式子（Part 5 p6）。"
    )
    + pre("""for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + "*" + str(j) + "=" + str(i * j), end="\\t")
    print()""")
    + pre("""1*1=1
2*1=2   2*2=4
3*1=3   3*2=6   3*3=9
...
9*1=9   9*2=18  ...  9*9=81""")
    + p(
        '内层的 <code>print()</code> 带 <code>end="\\t"</code> 让同一行的式子用制表符隔开；外层的 <code>print()</code> 不带参数，只输出一个换行，负责「换行」。这个「内层不换行、外层换行」的搭配是打印二维结构的标准写法。'
    )
    + cal(
        "warn",
        "嵌套循环会让程序变慢",
        "课件专门提醒（Part 5 p7）：两层循环的执行次数是乘积，三层就是立方。对 1000 个元素，三层嵌套要做十亿次操作。这门课里出现「循环套循环套循环」基本说明思路错了，应该重新设计。",
    )
    + h2("七、四种累积模式")
    + p("绝大多数循环题都能归到这四种模式之一，认出模式就能直接套模板：")
    + tb(
        ("模式", "初始化", "循环体", "典型题"),
        (
            "累加求和",
            "<code>total = 0</code>",
            "<code>total = total + x</code>",
            "求和、求平均",
        ),
        ("累乘", "<code>prod = 1</code>", "<code>prod = prod * x</code>", "阶乘、连乘"),
        (
            "计数",
            "<code>count = 0</code>",
            "<code>count = count + 1</code>（满足条件时）",
            "统计元音、统计及格人数",
        ),
        (
            "找极值",
            "<code>best = 第一个元素</code>",
            "<code>if x &gt; best: best = x</code>",
            "最大值、最小值",
        ),
    )
    + p(
        "累加与累乘的初值不能写错：求和从 0 开始，求积从 1 开始。<code>prod = 0</code> 会让整个乘积永远是 0 而毫无报错——这类错误只能靠想清楚语义来避免。"
    )
    + pre("""numbers = [4, 9, 2, 7]
total = 0
biggest = numbers[0]
for x in numbers:
    total = total + x
    if x > biggest:
        biggest = x
print("sum:", total, "max:", biggest, "avg:", total / len(numbers))""")
    + pre("""sum: 22 max: 9 avg: 5.5""")
    + h2("八、常见错误与调试")
    + cal(
        "warn",
        "死循环",
        "三个原因：忘记更新控制变量、更新写错方向（该减写成了加）、条件永远成立（如 <code>while x != 10</code> 而 x 每次加 2 会跳过 10）。先读三件套，再看条件能否被打破。",
    )
    + cal(
        "warn",
        "off-by-one",
        "<code>range(1, 10)</code> 只到 9；<code>range(10)</code> 是 0–9。打印首尾值确认：<code>print(list(range(1, 10)))</code>。",
    )
    + cal(
        "warn",
        "遍历时修改列表",
        "<code>for x in L: L.remove(x)</code> 会漏掉元素，因为删除后下标整体前移，而循环变量还在按旧位置走。要删除请遍历副本 <code>for x in L[:]</code>，或新建一个列表。",
    )
    + cal(
        "tip",
        "浮点累加要用 round 收尾",
        "反复加 0.1 会积累误差（<code>0.1 + 0.2 != 0.3</code>）。累加金额时最后 <code>round(total, 2)</code>，比较时用 <code>abs(a - b) &lt; 1e-9</code>。",
    )
)

_K5 = K(
    ("loop", "循环", "A block of code that repeats."),
    ("iteration", "迭代", "One pass through the loop body."),
    ("for loop", "for 循环", "Iterates over the items of a sequence."),
    ("while loop", "while 循环", "Repeats while a condition stays true."),
    ("range()", "数字序列函数", "range(1, 101) yields 1 to 100, stop excluded."),
    ("loop variable", "循环变量", "The variable bound to the current item."),
    ("break", "跳出循环", "Ends the whole loop immediately."),
    ("continue", "跳过本轮", "Skips the rest of this iteration."),
    ("nested loop", "嵌套循环", "A loop inside another loop; counts multiply."),
    ("accumulator", "累加器", "total = 0 before the loop, total += x inside."),
    ("sentinel value", "哨兵值", "A special input such as -1 that ends the loop."),
    ("infinite loop", "死循环", "The condition never becomes False; stop with Ctrl+C."),
    ("off-by-one", "差一错误", "range(1, 10) stops at 9, not 10."),
)

_EX5 = (
    qa(
        "例 1　分别求 1 + 2 + … + 100 与 11 × 9 × 7 × … × 1。",
        p(
            "两个都是累积模式：求和初值 0，求积初值 1。步长为 −2 的 <code>range</code> 直接给出 11, 9, 7, 5, 3, 1。"
        )
        + pre("""seq_sum = 0
for i in range(1, 101):
    seq_sum = seq_sum + i
print("sum 1..100 =", seq_sum)

seq_mul = 1
for i in range(11, 0, -2):
    seq_mul = seq_mul * i
print("11*9*...*1 =", seq_mul)""")
        + p("输出：")
        + pre("""sum 1..100 = 5050
11*9*...*1 = 10395""")
        + p(
            "逐点解释：<code>range(1, 101)</code> 的最后一个值是 100（含头不含尾）；<code>range(11, 0, -2)</code> 依次给 11、9、7、5、3、1，走到 −1 时已越过终点 0 而停止。"
        ),
    )
    + qa(
        "例 2　输入一个正整数，求它各位数字之和（例如 12345 → 15）。",
        p(
            "思路：用 <code>% 10</code> 取出末位，用 <code>// 10</code> 把它去掉，循环直到数变成 0。这是「拆分数字」的标准套路，循环次数取决于位数，所以用 <code>while</code>。"
        )
        + pre("""n = int(input("Enter a positive integer: "))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print("Digit sum:", total)""")
        + p("输入 <code>12345</code>，输出 <code>Digit sum: 15</code>。")
        + p(
            "逐轮追踪：n=12345 → digit=5，n=1234；→ digit=4，n=123；→ 3，12；→ 2，1；→ 1，0。此时条件 <code>n &gt; 0</code> 为假，退出。注意循环体里三步的顺序：先取位、再加、最后缩小 n，缺任何一步都会死循环或算错。"
        ),
    )
    + qa(
        "例 3　输出 2 到 50 之间的所有质数。",
        p(
            "思路：对每个 n，用 2 到 n−1 逐个试除；一旦找到因子就把标志设为「不是质数」并 <code>break</code>，不必再试。"
        )
        + pre("""for n in range(2, 51):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")""")
        + p("输出：")
        + pre("""2 3 5 7 11 13 17 19 23 29 31 37 41 43 47""")
        + p(
            "解释：外层遍历候选数，内层做试除；<code>break</code> 只跳出内层，外层的 <code>if is_prime</code> 照常判断。标志变量 <code>is_prime</code> 每轮都要在<b>外层循环体内</b>重置为 <code>True</code>，写在循环外就只会记住第一次的结果——这是嵌套 + 标志组合最常见的错误。"
        ),
    )
    + qa(
        "例 4　反复读入成绩，输入 −1 时结束，最后输出平均分与及格人数。",
        p("这是「哨兵 + 计数 + 累加」的组合，也是项目作业里菜单循环的雏形。")
        + pre("""total = 0
count = 0
passed = 0
while True:
    score = float(input("Score (-1 to quit): "))
    if score == -1:
        break
    total = total + score
    count = count + 1
    if score >= 50:
        passed = passed + 1

if count > 0:
    print("Average:", round(total / count, 2))
    print("Passed:", passed)
else:
    print("No scores given")""")
        + p(
            "输入 <code>80</code>、<code>45</code>、<code>-1</code>，输出 <code>Average: 62.5</code> 与 <code>Passed: 1</code>。"
        )
        + p(
            "解释：<code>while True</code> 先进入，靠 <code>break</code> 退出；<code>count &gt; 0</code> 的判断避免除零（第 11 讲的 <code>ZeroDivisionError</code> 在这里是真实风险）；及格人数用「计数模式」，条件写在累加之后。"
        ),
    )
)

_PR5 = ol(
    "打印 1 到 30 之间所有能被 3 整除但不能被 6 整除的数。",
    "求 <code>n!</code>（n 由用户输入），并说明循环变量从哪里开始、到哪里结束。",
    "统计一个字符串里元音字母（a e i o u）的个数，大小写都要算。",
    """打印 5 行「金字塔」：
<pre><code>    *
   ***
  *****
 *******
*********</code></pre>""",
    "反复读入整数，直到读入 0；输出其中最大值与最小值（不考虑 0）。",
) + det(
    "答案与思路",
    p(
        "<b>1.</b> <code>for n in range(1, 31): if n % 3 == 0 and n % 6 != 0: print(n)</code>。也可以直接用 <code>range(3, 31, 3)</code> 再剔除 6 的倍数。关键是上界写 31。"
    )
    + p(
        "<b>2.</b> <code>result = 1</code>，<code>for i in range(1, n + 1): result = result * i</code>。若写 <code>range(n)</code> 会从 0 开始，结果恒为 0——这是累乘初值与起点双重踩坑。n=0 时按定义为 1，恰好被 <code>range(1, 1)</code> 的空序列正确处理。"
    )
    + p(
        '<b>3.</b> <code>count = 0</code>，<code>for ch in s: if ch.lower() in "aeiou": count += 1</code>。用 <code>lower()</code> 统一大小写，比写两遍 <code>in "aeiouAEIOU"</code> 更简洁；<code>in</code> 判断子串是否出现在字符串里，是第 2 讲字符串方法的一部分。'
    )
    + p(
        '<b>4.</b> 外层 <code>for row in range(1, 6)</code>，先打印 <code>" " * (5 - row)</code> 个空格，再打印 <code>"*" * (2 * row - 1)</code> 个星号，最后 <code>print()</code> 换行。规律来自行号：第 row 行有 2row−1 个星、5−row 个前导空格。'
    )
    + p(
        "<b>5.</b> 用 <code>while True</code> 读入，读 0 就 <code>break</code>；第一个非零数同时初始化 <code>maximum</code> 与 <code>minimum</code>，之后每读一个就更新两个值。若用一个不可能的大数当初始最大值（如 10**9），遇到更大输入时会错——用「第一个元素初始化」才安全。"
    ),
)

_EXAM5 = (
    cal(
        "exam",
        "必考",
        "<code>for</code> 与 <code>while</code> 的选择依据；<code>range()</code> 三种参数与「不含 stop」；<code>break</code> 与 <code>continue</code> 的区别；嵌套循环的总执行次数。",
    )
    + cal(
        "warn",
        "易错 1　死循环",
        "<code>while</code> 里忘记更新控制变量，或更新语句被 <code>continue</code> 跳过。写循环先写下三件套，再写循环体。",
    )
    + cal(
        "warn",
        "易错 2　range 的边界",
        "<code>range(1, 10)</code> 是 1–9；要 10 得写 <code>range(1, 11)</code>。负数步长时起点必须大于终点。<code>range(0, 10, -1)</code> 是空序列，不报错，容易误判成「程序没跑」。",
    )
    + cal(
        "warn",
        "易错 3　循环变量初值放错",
        "标志变量、累加器必须在<b>正确的层级</b>初始化：求每个数的质数性时 <code>is_prime = True</code> 要放在外层循环体内；求总和时 <code>total = 0</code> 要放在所有循环之外。",
    )
    + cal(
        "tip",
        "进阶",
        "两层循环的复杂度是 O(n²)，三层是 O(n³)。项目作业里如果出现三层以上的嵌套，几乎一定能用「先算好放进列表/字典」的方式降层。另外，<code>for</code> 循环的循环变量在循环结束后仍保留最后的值，写测试时可以利用这一点。",
    )
)

_CK5 = (
    h2("操作清单")
    + h3("写循环之前先确认四件事")
    + st(
        "要重复的是哪一段？把它写成缩进的循环体",
        "循环次数已知还是未知？已知用 <code>for</code>，未知用 <code>while</code>",
        "控制变量/累加器的初值是多少？在哪一层初始化？",
        "循环什么时候结束？把结束条件写成能判真假的表达式，并确认它最终会成立",
    )
    + h3("写完后的自检")
    + ck(
        "打印首尾值确认边界：<code>print(list(range(...)))</code>",
        "<code>while</code> 的更新语句在 <code>continue</code> 之前",
        "<code>break</code> 只跳出最内层，确认这是你要的效果",
        "嵌套循环的内层依赖外层变量时，内层次数随外层变化",
        "累乘初值是 1，累加初值是 0，找极值用第一个元素初始化",
    )
)

_MP5 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Chapter 4 - Part 1 - Loop Theory.pdf",
            "p2–p8",
            "重复的动机、party 邀请案例、loop 与 iteration 的定义、两种循环的分工",
        ),
        (
            "Chapter 4 - Part 2 - For Loop.pdf",
            "p2–p8",
            "<code>for</code> 执行流程、遍历字符串/列表、<code>range()</code> 三参数、<code>range(0, 10)</code> 示例",
        ),
        (
            "Chapter 4 - Part 3 - While Loop.pdf",
            "p2–p6",
            "<code>while</code> 先判后执行、条件重估、输入驱动循环、哨兵 −1 示例",
        ),
        (
            "Chapter 4 - Part 4 - Controlling Loops.pdf",
            "p2–p6",
            "<code>break</code> 终止整个循环、<code>continue</code> 跳过本轮、两者流程图",
        ),
        (
            "Chapter 4 - Part 5 - Nested For.pdf",
            "p2–p7",
            "嵌套循环流程、乘法表、嵌套的性能提醒与 bad code smell",
        ),
        (
            "10_Chapter 4_1_Chapter 4 Code Examples_L4E1.py",
            "全文",
            '遍历字符串 + <code>isupper()</code> + <code>end=""</code> 提取大写字母',
        ),
        ("L4E2.py / L4E3.py", "全文", "遍历列表、<code>range</code> 求和与连乘"),
        (
            "L4E4.py / L4E5.py",
            "全文",
            "哨兵循环、<code>while True</code> + <code>break</code> 找 13 的倍数",
        ),
        (
            "L4E6.py / L4E7.py",
            "全文",
            "<code>continue</code> 过滤奇数、嵌套循环打印乘法表",
        ),
    )
    + p(
        "<b>跳过项：</b>Part 1 的 party 案例配图（纯图片）、Part 5 p4 的空页、以及各 Code Example 的运行截图均不构成新知识点；课程考核与作业截止页属于行政信息，已在第 1 讲处理。"
    )
    + p(
        "<b>拓展项：</b>循环结束后的变量残留、<code>range</code> 对象的惰性、遍历时修改列表的危险、浮点累加误差，都是原课件结论的边界补充，不引入新语法。"
    )
)

LEC.append(
    L(
        slug="ch05-loops",
        tzh="⑤ 循环与迭代",
        ten="Loops and Iteration",
        keywords=[
            "loop",
            "iteration",
            "for loop",
            "while loop",
            "range",
            "break",
            "continue",
            "nested loop",
            "accumulator",
            "sentinel value",
            "infinite loop",
            "off-by-one",
        ],
        files=[
            "Chapter 4 - Part 1 - Loop Theory.pdf",
            "Chapter 4 - Part 2 - For Loop.pdf",
            "Chapter 4 - Part 3 - While Loop.pdf",
            "Chapter 4 - Part 4 - Controlling Loops.pdf",
            "Chapter 4 - Part 5 - Nested For.pdf",
            "10_Chapter 4_1_Chapter 4 Code Examples_L4E1.py",
            "10_Chapter 4_1_Chapter 4 Code Examples_L4E7.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "上一讲让程序学会了「分岔」，这一讲让它学会「绕圈」：同一段代码重复执行，直到把一整个列表处理完、或者等到某个条件成立。循环是这门课后面所有程序的主干——菜单、统计、文件逐行处理、项目作业，全靠它。"
            )
            + p(
                "结构上，循环的判断条件与第 4 讲的 <code>if</code> 用的是同一套布尔表达式；区别只在于 <code>if</code> 走一次，<code>while</code> 走很多次。下一讲把这些重复的代码块打包成函数。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "说清 <code>for</code> 与 <code>while</code> 各自适合什么场景，并按场景选对",
                "用 <code>range(start, stop, step)</code> 生成任意等差数列，并解释为什么不含 stop",
                "写出不会死循环的 <code>while</code>：初始化、条件、更新三件套齐全",
                "用 <code>break</code> 提前退出、用 <code>continue</code> 跳过本轮，并说明二者差别",
                "写出两层嵌套循环处理二维结构，并算出总执行次数",
                "把求和、求积、计数、找极值四类问题套进对应模板",
            )
        ),
        detail=_D5,
        kws=_K5,
        examples=_EX5,
        practice=_PR5,
        exam=_EXAM5,
        checklist=_CK5,
        mapping=_MP5,
    )
)

# ============================================================ 6 函数
_D6 = (
    h2("一、函数是什么，为什么要用")
    + p(
        "课件给的定义很短：函数是一个「小程序」，专门完成某一件事（What is a function p2）。它把一段代码打包、起名字、留出入口（参数）与出口（返回值），以后在程序任何地方都能再叫它一次。"
    )
    + p("用函数有三层收益：")
    + ul(
        "结构：把长程序切成若干块，每块只做一件事，读代码时不必一次装进脑子；",
        "复用：定义一次，调用无数次，改一处就全改；",
        "协作：把一组函数写成一个库（library），别人 <code>import</code> 就能用——这正是第 10 讲「模块」的由来。",
    )
    + p(
        "课件还提到一个特殊情形：函数可以调用自己，叫递归（recursion）。这门课不深入递归，但要知道它是函数机制自然允许的。"
    )
    + h3("1.1 内置函数与自定义函数")
    + p(
        "前几讲一直在用<b>内置函数</b>（built-in functions）：<code>print()</code>、<code>input()</code>、<code>len()</code>、<code>int()</code>、<code>float()</code>、<code>str()</code>、<code>round()</code>、<code>range()</code>。它们随 Python 一起装好，不用导入就能用。"
    )
    + p(
        "这门课的重点是<b>自定义函数</b>（user-defined functions）：为了解决自己的问题而写的函数（What is a function p5）。两者用法完全一样——都是「给输入、拿输出」。"
    )
    + p(
        "课件的 <code>round()</code> 例子值得细看（p4）：它接受两个输入，第一个是要处理的数，第二个是保留几位小数，<b>顺序不能反</b>。"
    )
    + pre(
        """print(round(3.14159, 2))
print(round(6.7, 0))
print(round(3.14159))"""
    )
    + pre(
        """3.14
7.0
3"""
    )
    + p(
        "<code>round(6.7, 0)</code> 得 <code>7.0</code> 而不是 <code>7</code>：只要给了第二个参数，返回类型就是 float。这提醒我们：<b>函数的返回值有类型</b>，用之前要知道拿到的是什么。"
    )
    + h2("二、用 def 定义函数")
    + h3("2.1 骨架的五个部分")
    + p("定义函数的语法（Self-defined functions p2–p5）可以拆成五块：")
    + pre(
        """def function_name(parameters):
    # function body
    return result"""
    )
    + tb(
        ("部分", "作用", "规则"),
        ("<code>def</code>", "声明「这里开始定义一个函数」", "关键字，不能拼错"),
        (
            "<code>function_name</code>",
            "函数的名字",
            "小写、用下划线分词，描述它做什么",
        ),
        (
            "<code>(parameters)</code>",
            "参数列表，函数的输入",
            "逗号分隔；没有参数也要写一对空括号",
        ),
        ("<code>:</code>", "函数头结束，函数体开始", "漏了就是 SyntaxError"),
        ("缩进的函数体", "函数真正执行的代码", "整块必须比 def 多缩进"),
        (
            "<code>return result</code>",
            "把结果交回调用者",
            "可以没有，也可以在中间提前返回",
        ),
    )
    + p(
        "命名规范与变量一致：只能字母、数字、下划线，不能有空格，不能以数字开头；习惯全小写 + 下划线（<code>count_vowels</code>），而不是 <code>CountVowels</code> 或 <code>cv</code>。名字要让人只看名字就知道它做什么。"
    )
    + h3("2.2 一个最小可运行函数")
    + pre(
        """def greet(name):
    message = "Hello, " + name + "!"
    return message

result = greet("Alice")
print(result)"""
    )
    + pre("""Hello, Alice!""")
    + p(
        '三行代码里发生了三次「跨边界」：调用时 <code>"Alice"</code> 被复制给参数 <code>name</code>；函数体算出一个新字符串；<code>return</code> 把它交给调用处，赋给 <code>result</code>。函数内部的 <code>message</code> 在外面看不见（下一节讲作用域）。'
    )
    + h2("三、return：函数唯一的出口")
    + h3("3.1 return 结束执行并交回一个值")
    + p(
        "<code>return</code> 做两件事：立刻结束函数的执行；把后面的表达式作为返回值交给调用者（p6）。<code>return</code> 之后的语句永远不会执行。"
    )
    + pre(
        """def check(n):
    if n < 0:
        return "negative"
    return "non-negative"

print(check(-5))
print(check(0))"""
    )
    + pre(
        """negative
non-negative"""
    )
    + p(
        "一个函数里可以有多条 <code>return</code>，但每次调用只会执行其中一条——上面就是「负数提前返回」的写法，避免了层层嵌套的 if。这种提前返回叫守卫式写法（guard clause），第 4 讲已经用过同样的思路。"
    )
    + h3("3.2 return 与 print 不是一回事")
    + p(
        "这是本章最容易混的一点（p6）：<code>print()</code> 只是把文字显示到屏幕上，<b>不产生值</b>；<code>return</code> 才把值交回给调用者。"
    )
    + pre(
        """def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)
y = add_return(2, 3)
print("x is", x)
print("y is", y)"""
    )
    + pre(
        """5
x is None
y is 5"""
    )
    + p(
        "<code>add_print</code> 把 5 打在屏幕上，但它的返回值是 <code>None</code>，所以 <code>x</code> 拿到的是 <code>None</code>。CodeGrade 的反馈里那句 <code>The function should return a value</code>（CG Guide）对应的就是这个错误：该 return 的地方写了 print。"
    )
    + h3("3.3 没有 return 的函数返回 None")
    + p(
        "如果函数体里根本没有 <code>return</code>，Python 会在函数结束时自动返回 <code>None</code>（none.py）。<code>None</code> 是第 1 讲介绍过的「空值」类型，表示「没有值」。"
    )
    + pre(
        """def show(word):
    print(word)

value = show("Cat")
print("value is", value)"""
    )
    + pre(
        """Cat
value is None"""
    )
    + p(
        "反过来，<code>return</code> 不带表达式也返回 <code>None</code>，常用于「提前结束、不返回东西」的场景："
    )
    + pre(
        """def divide(a, b):
    if b != 0:
        return a / b

result = divide(10, 0)
if result is None:
    print("Error: Division by zero!")
else:
    print(result)"""
    )
    + pre("""Error: Division by zero!""")
    + p(
        "注意判断用的是 <code>is None</code> 而不是 <code>== None</code>：<code>None</code> 是单例对象，<code>is</code> 比较的是「是不是同一个对象」，语义更准确。"
    )
    + cal(
        "warn",
        "忘写 return 是最常见的丢分点",
        "函数算出了结果却只用 print 显示，调用处拿到 None，后续计算全错。写完函数先问自己：<b>调用者需要这个值吗？</b> 需要就 return。",
    )
    + h2("四、调用函数：把值送进去")
    + p(
        "定义只是「写好一份说明书」，真正执行要调用（call）：写函数名加括号，括号里给实参（p7）。"
    )
    + pre(
        """def fun(p):
    return p * 2

x = 66
y = fun(x)
print(y)"""
    )
    + pre("""132""")
    + p(
        "调用时发生的事：实参 <code>x</code> 的值被<b>复制</b>给形参 <code>p</code>；函数体用 <code>p</code> 算出结果；<code>return</code> 把结果交回；赋值语句把它存进 <code>y</code>。整条链上 <code>x</code> 本身没有被改动。"
    )
    + p(
        "函数必须先定义、后调用。把调用写在 <code>def</code> 之前会抛 <code>NameError: name 'fun' is not defined</code>——Python 从上往下执行，定义也是一个「执行动作」。"
    )
    + h2("五、参数：位置、数量、顺序")
    + h3("5.1 按位置对应")
    + p(
        "参数按<b>位置</b>一一对应（Parameters p2）：第一个实参给第一个形参，第二个给第二个。<b>数量和顺序都不能错</b>。"
    )
    + pre(
        """def describe(name, age):
    return name + " is " + str(age) + " years old"

print(describe("Alice", 30))
print(describe(30, "Alice"))"""
    )
    + pre(
        """Alice is 30 years old
30 is Alice years old"""
    )
    + p(
        "第二个调用不报错，但语义完全错了——这正是「顺序有意义」的意思。参数个数不对则会直接抛 <code>TypeError</code>："
    )
    + pre(
        """def describe(name, age):
    return name + " is " + str(age) + " years old"

print(describe("Alice"))"""
    )
    + pre(
        """TypeError: describe() missing 1 required positional argument: 'age' """,
    )
    + h3("5.2 为什么必须用参数，而不是靠外面的变量")
    + p(
        "课件强调：函数需要的所有「外部信息」都必须通过参数传进来（Parameters p4）。这样做换来三件事——函数独立（不偷偷依赖全局状态）、可复用（换个输入就能用）、可测试（给定输入就能验证输出）。"
    )
    + p(
        "反面例子：函数直接读一个全局变量 <code>PI</code> 或 <code>tax_rate</code>，换一个场景就得改函数体。写成 <code>def total(price, tax_rate)</code>，函数就能在任何地方用。"
    )
    + h3("5.3 默认参数")
    + p(
        "默认参数（default parameter）让某个参数「可以不传」，不传时用预先写好的值（Parameters p5）："
    )
    + pre(
        """def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet("Alice", "Hi"))
print(greet("Bob"))"""
    )
    + pre(
        """Hi, Alice!
Hello, Bob!"""
    )
    + p(
        "两条规则：第一，有默认值的参数必须放在<b>没有默认值</b>的参数<b>后面</b>，写成 <code>def f(a=1, b)</code> 是语法错误；第二，默认值只在<b>定义时求值一次</b>，之后每次调用共用同一个对象。"
    )
    + cal(
        "warn",
        "可变默认参数是经典陷阱",
        """<code>def add_item(x, box=[])</code> 里的 <code>[]</code> 只创建一次，所有调用共用同一个列表：<code>add_item(1)</code> 得 <code>[1]</code>，再调 <code>add_item(2)</code> 得 <code>[1, 2]</code>。正确写法是把默认值设为 <code>None</code>，进了函数再判断：<code>if box is None: box = []</code>。""",
    )
    + pre(
        """def add_item(x, box=[]):
    box.append(x)
    return box

print(add_item(1))
print(add_item(2))"""
    )
    + pre(
        """[1]
[1, 2]"""
    )
    + h2("六、作用域：函数里的名字是独立的")
    + h3("6.1 局部变量")
    + p(
        "函数体内定义的变量与参数都是<b>局部</b>的（local）：只在这个函数里存在，函数返回就消失，别的函数看不到（Parameters p3）。所以两个函数各有一个 <code>n</code> 互不干扰。"
    )
    + pre(
        """def f1():
    n = 1
    return n

def f2():
    n = 2
    return n

print(f1(), f2())"""
    )
    + pre("""1 2""")
    + p(
        "如果函数里给一个「外面已有」的变量赋值，Python 会把它当成新的局部变量，外面的同名变量不变。想改外面的变量得用 <code>global</code>，但这门课不建议这么做——用参数传入、用 return 传出，才是可维护的写法。"
    )
    + h3("6.2 值传递：改参数不影响外面的不可变对象")
    + p("add_one.py 是课件给出的追踪练习：")
    + pre(
        """def add_one(nr):
    nr = nr + 1
    x = 2 * nr
    return x

x = 10
y = 7
print("returned:", add_one(y))
print("x and y now:", x, y)"""
    )
    + pre(
        """returned: 16
x and y now: 10 7"""
    )
    + p(
        "为什么 <code>y</code> 仍是 7？因为 <code>y</code> 的值被复制给 <code>nr</code>，函数里改的是副本。同理函数里的局部变量 <code>x</code> 与外面的 <code>x</code> 是两个不同的名字，互不影响。"
    )
    + h3("6.3 例外：传入可变对象时会被改到")
    + p(
        "列表、字典是可变对象（mutable），传参时复制的是「指向同一个对象的引用」而不是内容。函数里改元素，外面的列表跟着变（list_parameter.py）："
    )
    + pre(
        """def modify_parameter(my_list):
    my_list[2] = 33
    A = my_list
    A[0] = 1000

original_list = [1, 2, 3]
print("Before:", original_list)
modify_parameter(original_list)
print("After:", original_list)"""
    )
    + pre(
        """Before: [1, 2, 3]
After: [1000, 2, 33]"""
    )
    + p(
        "第 8 讲会系统讲列表，这里先记住结论：<b>不可变对象（数字、字符串、元组）传进函数，外面不变；可变对象（列表、字典、集合）传进去，函数里的修改会反映到外面。</b>"
    )
    + h2("七、从需求到函数：设计五问")
    + p(
        "课件用一个具体的题示范设计流程（Example: writing a function p2）：写一个函数，返回字符串里元音字母的个数。动笔之前先回答五个问题："
    )
    + st(
        "函数叫什么名字？→ <code>count_vowels</code>（动词 + 名词，说明它做什么）",
        "参数是什么？→ 一个字符串 <code>s</code>",
        "返回什么？→ 一个整数（个数），不是打印",
        '怎么判断一个字符是不是元音？→ <code>ch.lower() in "aeiou"</code>',
        "怎么数？→ 计数器初值 0，命中就 +1；用不用循环？→ 要遍历每个字符，用 <code>for</code>",
    )
    + pre(
        """def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count = count + 1
    return count

print(count_vowels("Programming is fun"))"""
    )
    + pre("""5""")
    + p(
        "这五个问题就是「通用解题思路」：<b>定名称 → 定输入 → 定输出 → 定判定条件 → 定累加方式</b>。换成「统计及格人数」「数出单词个数」都是同一套问法。"
    )
    + h2("八、用函数组织一个完整程序")
    + p(
        "课件的 example_with_menu.py 把「面积计算器」拆成五个函数：一个打印菜单并读选择，三个算面积，一个算平方根；主程序是一个 <code>while</code> 循环，按选择调用对应函数。"
    )
    + pre(
        '''def print_menu():
    """Print the menu and return the user's choice."""
    print("\\nCompute the area of:")
    print("1) a circle")
    print("2) a rectangle")
    print("3) a triangle")
    print("4) quit")
    return int(input("Enter your choice: "))

def circle_area(r):
    return 3.14159 * r ** 2

def rectangle_area(w, h):
    return w * h

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

choice = print_menu()
if choice == 1:
    r = float(input("Radius: "))
    print("Area:", round(circle_area(r), 2))
elif choice == 2:
    w = float(input("Width: "))
    h = float(input("Height: "))
    print("Area:", round(rectangle_area(w, h), 2))
elif choice == 3:
    a = float(input("Side 1: "))
    b = float(input("Side 2: "))
    c = float(input("Side 3: "))
    print("Area:", round(triangle_area(a, b, c), 2))
else:
    print("Bye!")'''
    )
    + p(
        "结构上的三个要点：每个函数只做一件事（单一职责）；菜单函数既打印又返回选择，把「读输入」与「决定流程」分开；主程序只负责调度，不写计算细节。三角形面积用海伦公式（Heron's formula）：半周长 <code>s = (a+b+c)/2</code>，面积 <code>√(s(s−a)(s−b)(s−c))</code>，开方用 <code>** 0.5</code>。"
    )
    + cal(
        "tip",
        "docstring 放在函数第一行",
        '每个函数开头写一句 <code>"""Returns the area of a circle."""</code>，既是注释又能被 <code>help()</code> 读出来（第 3 讲）。项目作业里评分的可读性就看这个。',
    )
    + h2("九、常见错误与调试")
    + cal(
        "warn",
        "print 当 return 用",
        "屏幕上有输出、调用处拿到 None。凡是题目要求「返回」，就只能 <code>return</code>；要同时看结果，在调用处 print 返回值。",
    )
    + cal(
        "warn",
        "参数个数不对",
        "<code>TypeError: f() takes 2 positional arguments but 3 were given</code>。数一遍 <code>def</code> 括号里的参数与调用括号里的值。",
    )
    + cal(
        "warn",
        "UnboundLocalError",
        "函数里既用又给某个变量赋值时，Python 把它当局部变量，于是「用」的那一步发现它还没赋值。解决办法：把值作为参数传进来，或在函数内先初始化。",
    )
    + cal(
        "warn",
        "只在函数里改了不可变参数，以为外面会变",
        "<code>def inc(n): n = n + 1</code> 改的是副本。要「改到外面」，得 <code>return</code> 新值并让调用处重新赋值：<code>x = inc(x)</code>。",
    )
)

_K6 = K(
    ("function", "函数", "A named block of code that performs one task."),
    ("def", "定义函数的关键字", "def area(r): starts a function definition."),
    ("parameter", "形参", "A variable listed in the parentheses of the definition."),
    ("argument", "实参", "The value passed in when the function is called."),
    ("function body", "函数体", "The indented statements inside the function."),
    ("return", "返回", "Sends a value back to the caller and ends the function."),
    ("None", "空值", "The value a function returns when it has no return statement."),
    ("function call", "函数调用", 'greet("Bob") executes the function.'),
    ("scope", "作用域", "Variables inside a function are local to it."),
    ("local variable", "局部变量", "A variable that exists only inside the function."),
    (
        "default parameter",
        "默认参数",
        'def greet(name, greeting="Hello") can be called with one argument.',
    ),
    (
        "mutable object",
        "可变对象",
        "A list passed to a function can be modified inside it.",
    ),
    (
        "docstring",
        "文档字符串",
        "A string on the first line of a function, read by help().",
    ),
    ("recursion", "递归", "A function that calls itself."),
)

_EX6 = (
    qa(
        "例 1　写函数 <code>count_vowels(s)</code> 返回元音个数，并解释每一行的作用。",
        p("先按设计五问定好名称、输入、输出、判定、累加，再写代码。")
        + pre(
            """def count_vowels(s):
    count = 0                  # 计数器：初值 0
    for ch in s.lower():       # 遍历每个字符，统一转小写
        if ch in "aeiou":      # 判定：是不是元音
            count = count + 1  # 命中就 +1
    return count               # 把结果交回调用者

print(count_vowels("Programming is fun"))
print(count_vowels("XYZ"))"""
        )
        + p("输出：")
        + pre(
            """5
0"""
        )
        + p(
            '解释：<code>s.lower()</code> 让大小写都算；<code>ch in "aeiou"</code> 是子串判断，比写六个 <code>or</code> 简洁；<code>return</code> 放在循环<b>外面</b>，循环结束后才返回总数——若缩进到循环里，函数会在第一个字符处就返回。'
        ),
    )
    + qa(
        "例 2　追踪 add_one 的执行，说明为什么 y 没有被改成 8。",
        p(
            "先写出预期的中间值，再运行验证。函数：<code>nr = nr + 1</code>，<code>return 2 * nr</code>；调用 <code>add_one(7)</code>。"
        )
        + pre(
            """def add_one(nr):
    nr = nr + 1
    x = 2 * nr
    return x

x = 10
y = 7
print("returned:", add_one(y))
print("x and y now:", x, y)"""
        )
        + p("输出：")
        + pre(
            """returned: 16
x and y now: 10 7"""
        )
        + p(
            "逐步追踪：调用把 <code>y</code> 的值 7 <b>复制</b>给 <code>nr</code>；<code>nr</code> 变成 8；<code>x</code>（局部）是 16；返回 16。外面的 <code>y</code> 从未被赋值过，所以仍是 7；外面的 <code>x</code> 也是 10，因为函数里的 <code>x</code> 是另一个局部名字。"
        ),
    )
    + qa(
        "例 3　写 <code>is_prime(n)</code> 返回布尔值，并用它打印 20 以内的质数。",
        p(
            "关键设计决策：返回 <code>True</code> / <code>False</code>，而不是打印「是质数」——这样调用者可以拿它做别的判断。"
        )
        + pre(
            """def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

for n in range(2, 21):
    if is_prime(n):
        print(n, end=" ")"""
        )
        + p("输出：")
        + pre("""2 3 5 7 11 13 17 19""")
        + p(
            "解释：<code>n &lt; 2</code> 与「找到因子」两处都提前 <code>return False</code>，函数立刻结束；只有全部试完都没找到因子，才走到最后的 <code>return True</code>。把「判定」写成返回布尔值的函数，是让代码可复用的关键一步。"
        ),
    )
    + qa(
        "例 4　用两个函数改写面积计算器：<code>circle_area(r)</code> 与 <code>triangle_area(a,b,c)</code>，并在主程序里调用。",
        p("函数只负责算，主程序负责读输入与打印，职责分开。")
        + pre(
            """def circle_area(r):
    return 3.14159 * r ** 2

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

r = float(input("Radius: "))
print("Circle area:", round(circle_area(r), 2))

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
print("Triangle area:", round(triangle_area(a, b, c), 2))"""
        )
        + p(
            "输入 <code>2</code>、<code>3</code>、<code>4</code>、<code>5</code>，输出："
        )
        + pre(
            """Circle area: 12.57
Triangle area: 6.0"""
        )
        + p(
            "解释：圆面积 3.14159×4 = 12.56636 → 12.57；三角形三边 3、4、5 是直角三角形，面积 6，海伦公式给出 <code>s=6</code>、<code>6×3×2×1=36</code>、开方得 6。若三边构不成三角形（如 1、2、10），<code>s−a</code> 会为负，开方得到复数——真实程序应先校验三边关系。"
        ),
    )
)

_PR6 = ol(
    "写 <code>max_of_three(a, b, c)</code>，返回三者中的最大值（不许用 <code>max()</code>）。",
    "写 <code>count_char(s, ch)</code>，返回 <code>ch</code> 在 <code>s</code> 中出现的次数（不许用 <code>count()</code>）。",
    "写 <code>is_even(n)</code> 返回布尔值；再写一段代码，用它打印 1–10 中的偶数。",
    "写 <code>to_celsius(f)</code> 把华氏温度转成摄氏温度（公式 C = (F − 32) × 5 / 9），返回保留一位小数的值。",
    "把第 5 讲的「反复读成绩、输出平均分与及格人数」改写成函数 <code>average(scores)</code>，参数是一个分数列表。",
) + det(
    "答案与思路",
    p(
        "<b>1.</b> 先假设 <code>a</code> 最大，再依次比较：<code>best = a</code>；<code>if b &gt; best: best = b</code>；<code>if c &gt; best: best = c</code>；<code>return best</code>。这是「找极值」模式，初值必须是<b>列表里真实存在的元素</b>，不能写 0（全负数时出错）。"
    )
    + p(
        "<b>2.</b> <code>count = 0</code>，<code>for c in s: if c == ch: count += 1</code>，<code>return count</code>。若 <code>ch</code> 长度大于 1，这个写法按字符比会永远不相等——要按子串计数得用 <code>s.count(ch)</code> 或滑动窗口，题目限定单字符才有上面的简单解。"
    )
    + p(
        '<b>3.</b> <code>def is_even(n): return n % 2 == 0</code>。函数体只有一行时，返回的就是这个布尔表达式，不必写 if。调用处：<code>for i in range(1, 11): if is_even(i): print(i, end=" ")</code>。'
    )
    + p(
        "<b>4.</b> <code>return round((f - 32) * 5 / 9, 1)</code>。注意运算顺序：先减再乘除；写成 <code>f - 32 * 5 / 9</code> 会因为乘除优先而算错。"
    )
    + p(
        "<b>5.</b> <code>def average(scores): if not scores: return None</code>（空列表要单独处理，否则 <code>sum/0</code> 报 ZeroDivisionError），否则 <code>return sum(scores) / len(scores)</code>。及格人数另写一个函数 <code>count_passed(scores)</code>，每个函数只做一件事。"
    ),
)

_EXAM6 = (
    cal(
        "exam",
        "必考",
        "<code>def</code> 定义、<code>return</code> 与 <code>print</code> 的区别、参数按位置传递、无 return 时得 <code>None</code>、局部变量的独立性。",
    )
    + cal(
        "warn",
        "易错 1　该 return 却 print",
        "CodeGrade 的 <code>The function should return a value</code> 就是这个。看到题目写「返回」，第一反应写 <code>return</code>。",
    )
    + cal(
        "warn",
        "易错 2　默认参数位置与可变默认值",
        "<code>def f(a=1, b)</code> 是语法错误；<code>def f(box=[])</code> 会让所有调用共享同一个列表，必须改用 <code>None</code> 哨兵。",
    )
    + cal(
        "warn",
        "易错 3　把列表参数当成副本",
        "函数里 <code>my_list[0] = 1000</code> 会改到外面的列表。想保留原数据，调用前先 <code>L[:]</code> 复制（第 8 讲）或 <code>list(L)</code>。",
    )
    + cal(
        "tip",
        "进阶",
        "递归写法（函数调用自己）在阶乘、斐波那契里常见，但必须有终止条件；另外记住 <code>return</code> 一次只能返回一个对象，要返回多个值请用元组（第 8 讲）。",
    )
)

_CK6 = (
    h2("操作清单")
    + h3("写函数之前，先回答五个问题")
    + st(
        "函数叫什么名字？用动词开头、全小写下划线",
        "参数有哪些？每个参数的类型与含义写清楚",
        "返回什么？一个值还是多个值，类型是什么",
        "判定的条件是什么？写成布尔表达式",
        "要不要循环？需要累积就用「计数器/累加器 + 循环」模板",
    )
    + h3("写完之后的检查")
    + ck(
        "每个要「返回」的路径都写了 <code>return</code>",
        "调用时参数个数、顺序与定义一致",
        "函数里没有偷偷依赖全局变量",
        "默认参数只用于「可选」的尾部参数，且没有用可变对象",
        "函数体只做一件事，超过 20 行就该考虑拆开",
    )
)

_MP6 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "What_is_ a_funtion.pdf",
            "p2–p5",
            "函数的定义与动机、复用/结构化/库、递归提及、内置函数与自定义函数、round() 两参数示例",
        ),
        (
            "Self_defined_functions.pdf",
            "p2–p7",
            "<code>def</code> 五个组成部分、命名规范、函数体缩进、<code>return</code> 结束执行、return ≠ print、调用方式",
        ),
        (
            "Parameters.pdf",
            "p2–p5",
            "按位置传参、参数数量与顺序、局部变量独立、值复制、为什么必须用参数、默认参数",
        ),
        (
            "Example_writing_a_function.pdf",
            "p2",
            "元音计数题的设计五问：命名、参数、返回、判定、计数、是否需要循环",
        ),
        (
            "Mutable_vs _immutable .pdf",
            "p2–p8",
            "可变/不可变类型、<code>B = A</code> 指向同一对象、列表参数会被函数改到（list_parameter.py）",
        ),
        ("add_one.py", "全文", "值复制追踪：函数内改参数不影响外部变量"),
        ("greeting.py", "全文", "默认参数的调用方式"),
        ("none.py / returning_none.py", "全文", "无 return 返回 None、用 is None 判断"),
        ("example_with_menu.py", "全文", "用多个函数组织菜单程序、docstring、海伦公式"),
    )
    + p(
        "<b>跳过项：</b>课件中只给出文件名而无正文的截图页（Example1.py 等）已按代码文件内容吸收到正文与示例；Moodle 的作业说明与评分页属于行政信息，不进入本讲。"
    )
    + p(
        "<b>拓展项：</b>可变默认参数陷阱、<code>is None</code> 判断、函数必须先定义后调用、UnboundLocalError 的成因，都是围绕原知识点的边界补充，不引入新语法考点。"
    )
)

LEC.append(
    L(
        slug="ch06-functions",
        tzh="⑥ 函数与参数传递",
        ten="Functions, Parameters and Scope",
        keywords=[
            "function",
            "def",
            "parameter",
            "argument",
            "return",
            "None",
            "scope",
            "local variable",
            "default parameter",
            "mutable object",
            "docstring",
            "recursion",
        ],
        files=[
            "What_is_ a_funtion.pdf",
            "Self_defined_functions.pdf",
            "Parameters.pdf",
            "Example_writing_a_function.pdf",
            "Mutable_vs _immutable .pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "前五讲的代码都是「一条一条往下写」。程序一变长，重复的片段就会出现，改一处要改十处。这一讲把代码打包成函数：给名字、留入口（参数）、留出口（返回值），以后随时调用。"
            )
            + p(
                "循环与函数是这门课的两根支柱：循环解决「重复」，函数解决「复用与结构」。后面第 7 讲的类、第 9 讲的文件处理、第 12 讲的项目作业，都是「若干函数 + 一个主流程」的形态。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "用 <code>def</code> 写出带参数、带返回值的函数，并解释五个组成部分",
                "说清 <code>return</code> 与 <code>print</code> 的区别，知道没有 return 时函数返回 <code>None</code>",
                "按位置正确传参，解释为什么参数个数与顺序都不能错",
                "用默认参数给可选参数设默认值，并避开「可变默认参数」陷阱",
                "解释局部变量的独立性，以及为什么列表传进函数会被改到",
                "按「定名称 → 定输入 → 定输出 → 定判定 → 定累加」五步设计一个函数",
            )
        ),
        detail=_D6,
        kws=_K6,
        examples=_EX6,
        practice=_PR6,
        exam=_EXAM6,
        checklist=_CK6,
        mapping=_MP6,
    )
)

# ============================================================ 7 类与对象
_D7 = (
    h2("一、面向对象：先摆正预期")
    + p(
        "课件第一句话很坦率：这是「回到 1980 年代的编程」（Chapter 6 Part 1 p2）。面向对象编程（object-oriented programming，OOP）本身是一门独立课程，这门课只讲最浅的一层——会定义类、会创建对象、会用对象的属性与方法。"
    )
    + p(
        "核心比喻只有两个：<b>类</b>（class）是模板或模型，<b>对象</b>（object）是按模板造出来的东西，也叫<b>实例</b>（instance）。课件用汽车举例：<code>Car</code> 是类，Fiat 与 Audi 是它的实例；两者都是车，但各自有品牌、颜色、年份（Part 1 p3）。人也一样：<code>Human</code> 是类，Janne 是一个实例。"
    )
    + p(
        'Python 是面向对象的语言，而且「一切皆对象」（Part 1 p4）：字符串、列表、整数都各自属于某个类。你早就在用对象了——<code>"abc".upper()</code> 里的 <code>.upper()</code> 就是字符串对象的方法。本讲只是学会自己造类。'
    )
    + h2("二、四个术语")
    + p("课件把术语压到四个（Part 2 p2–p4），这四个词必须能互相解释清楚：")
    + tb(
        ("术语", "英文解释", "中文说明"),
        (
            "类 class",
            "A template that defines structure and behaviour.",
            "定义对象「有哪些数据、能做什么」的模板",
        ),
        (
            "对象 / 实例 object, instance",
            "One concrete thing created from the class.",
            "按模板造出来的具体个体",
        ),
        (
            "属性 attribute",
            "A variable stored in the object; its properties.",
            "对象自己的数据，如 <code>brand</code>、<code>year</code>",
        ),
        (
            "方法 method",
            "A function defined inside the class.",
            "对象能执行的动作，如 <code>start_engine()</code>",
        ),
    )
    + p(
        "课件给的属性例子是 <code>age</code>、<code>year</code>、<code>size</code>、<code>weight</code>、<code>color</code>、<code>location</code>；方法例子是 <code>get_age()</code>、<code>start_engine()</code>、<code>calculate_distance()</code>、<code>close()</code>、<code>run()</code>（Part 2 p4）。规律很清楚：<b>属性是名词，方法是动词</b>。"
    )
    + h2("三、定义一个类")
    + h3("3.1 语法骨架")
    + pre(
        """class ClassName:
    def __init__(self, parameters):
        self.attribute = parameters

    def method_name(self):
        # do something with self.attribute
        return something"""
    )
    + p(
        "三件事要注意：类名用<b>首字母大写</b>的驼峰写法（<code>Car</code>、<code>Person</code>、<code>BankAccount</code>），与函数的小写下划线区分开；<code>class</code> 行末有冒号；类里的所有方法都要缩进一层，而方法体再缩进一层。"
    )
    + h3("3.2 构造函数 __init__ 与 self")
    + p(
        "<code>__init__</code> 是特殊方法，叫<b>构造函数</b>（constructor）：创建对象时会被<b>自动调用</b>，用来把初始数据装进对象（Part 2 p6）。名字前后各有两个下划线，写错一个就退化成普通方法，创建对象时不会执行。"
    )
    + p(
        "<code>self</code> 指「当前这个对象」。在类里访问自己的属性或调用自己的方法，都必须写 <code>self.xxx</code>。调用时 <code>self</code> <b>不用传</b>，Python 自动把对象塞进去。"
    )
    + pre(
        """class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def start_engine(self):
        print(self.brand + " says WROOM!")

car1 = Car("Tesla", "Black", 2019)
car1.start_engine()"""
    )
    + pre("""Tesla says WROOM!""")
    + p(
        '追踪一下 <code>Car("Tesla", "Black", 2019)</code>：Python 新建一个空对象；把对象作为 <code>self</code>、把三个实参依次给 <code>brand</code>、<code>color</code>、<code>year</code>；执行 <code>__init__</code> 的函数体，把三个值挂到对象上；最后把对象交回给 <code>car1</code>。'
    )
    + h3("3.3 点号访问")
    + p(
        "点号（dot notation）是「走进对象内部」的唯一入口（Part 2 p5）：<code>对象.属性</code> 读或写数据，<code>对象.方法()</code> 执行动作。"
    )
    + pre(
        """class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car = Car("Skoda", 2012)
print(car.brand)
print(car.year)
car.year = 2015
print(car.year)"""
    )
    + pre(
        """Skoda
2012
2015"""
    )
    + p(
        "最后一步说明属性是可写的：直接给 <code>car.year</code> 赋新值就行。想控制「怎么改」时，就写一个方法（如 <code>update_year(new_year)</code>），把规则集中在类里。"
    )
    + h2("四、多个实例，各自独立")
    + p(
        "同一个类可以造出无数个对象，每个对象有自己的属性值——这是类与「一个装着数据的字典」最大的区别（Part 1 p3）。L6E1 造了两辆车："
    )
    + pre(
        """class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def start_engine(self):
        print(self.brand + " says WROOM!")

car1 = Car("Tesla", "Black", 2019)
car2 = Car("Skoda", "Grey", 2012)

print("car1 is of brand", car1.brand)
print("car2 is of brand", car2.brand)
car1.start_engine()
car2.start_engine()"""
    )
    + pre(
        """car1 is of brand Tesla
car2 is of brand Skoda
Tesla says WROOM!
Skoda says WROOM!"""
    )
    + p(
        "<code>car1</code> 与 <code>car2</code> 是两个不同的对象：改 <code>car1.year</code> 不会影响 <code>car2.year</code>。方法里的 <code>self</code> 决定「操作哪一个对象」——<code>car1.start_engine()</code> 时 <code>self</code> 就是 <code>car1</code>。"
    )
    + h2("五、完整的类：Person")
    + p(
        "课件的 L6E2 给出一个更完整的例子（Part 3 p2）：三个属性、五个方法，既有只读的 getter，也有修改状态的 updater，还有一个做判断的 <code>is_adult()</code>。"
    )
    + pre(
        """class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_country(self):
        return self.country

    def is_adult(self):
        return self.age >= 18

    def update_age(self, new_age):
        self.age = new_age

    def update_country(self, new_country):
        self.country = new_country

person1 = Person("Alice", 30, "USA")
person2 = Person("Pekka", 17, "Finland")

print(person1.get_name(), person1.get_age(), person1.get_country())
person1.update_country("Canada")
print(person1.get_country())
print(person2.get_name(), "adult?", person2.is_adult())
person2.update_age(18)
print(person2.get_name(), "adult?", person2.is_adult())"""
    )
    + pre(
        """Alice 30 USA
Canada
Pekka adult? False
Pekka adult? True"""
    )
    + p(
        "读这段代码要注意三点：<code>get_*</code> 方法只是把属性值交出去，没有副作用；<code>update_*</code> 方法改的是 <code>self.age</code>，所以改完之后同一个对象的后续查询会看到新值；<code>is_adult()</code> 把判断规则写在类里，外部调用者不必知道「18 岁」这个阈值。"
    )
    + h2("六、对象作为参数")
    + p(
        "对象可以像普通值一样传给函数。L6E2 的后半段定义了一个普通函数，参数是一个 Person 对象："
    )
    + pre(
        """def can_buy_alcohol(human):
    if human.is_adult():
        print(human.get_name() + " can buy alcohol in Finland")
    else:
        print(human.get_name() + " cannot buy alcohol in Finland")

can_buy_alcohol(person2)"""
    )
    + pre("""Pekka cannot buy alcohol in Finland""")
    + p(
        "函数里直接调用 <code>human.is_adult()</code>：它不关心对象内部有几个属性，只依赖对象「会做什么」。这就是把数据与行为放在一起的好处——调用方代码更短，规则变化时只改类。"
    )
    + h2("七、类、字典、函数：什么时候用哪个")
    + tb(
        ("需求", "推荐做法", "原因"),
        (
            "只是把几个字段捆在一起传",
            '字典 <code>{"brand": "Ford", "year": 2015}</code>',
            "第 12 讲；轻量、可直接打印、适合读 JSON",
        ),
        (
            "一组数据要配上一组操作，且要被多处复用",
            "类",
            "属性和方法绑在一起，调用方只需知道接口",
        ),
        (
            "纯计算，不保存状态",
            "普通函数",
            "最简单，不必造对象",
        ),
    )
    + p(
        "课件的项目作业（汽车租赁系统）里，车辆、客户、交易都是「一条记录 + 若干操作」，用字典列表也能做，用类会更整齐。考试两种都可能出现，读得懂就行。"
    )
    + h2("八、类属性与实例属性")
    + p(
        "课件没有展开这一点，但它是最容易「看起来能跑、其实错了」的地方。写在 <code>__init__</code> 里、带 <code>self.</code> 的是<b>实例属性</b>，每个对象一份；直接写在类体里的（不带 <code>self.</code>）是<b>类属性</b>，所有对象共享。"
    )
    + pre(
        '''class Car:
    wheels = 4                      # 类属性：所有实例共享

    def __init__(self, brand):
        self.brand = brand          # 实例属性：每个对象一份

a = Car("Tesla")
b = Car("Skoda")
a.wheels = 3                        # 这一步新建了 a 自己的属性

print(a.wheels, b.wheels, Car.wheels)
print(a.brand, b.brand)'''
    )
    + pre(
        '''3 4 4
Tesla Skoda'''
    )
    + p(
        "读 <code>a.wheels</code> 时，先找实例属性，找不到才去类里找；给 <code>a.wheels</code> 赋值只影响 <code>a</code>，于是出现 <code>3 4 4</code>。如果写的是 <code>Car.wheels = 3</code>，三个输出就都变 3。初学阶段建议<b>所有属性都写进 <code>__init__</code></b>，避免这种歧义。"
    )
    + h2("九、检查对象里到底有什么")
    + p(
        "调试类的问题，第一步永远是「属性到底装上了没有」。三种看法："
    )
    + pre(
        '''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.__dict__)          # 所有实例属性
print(type(p).__name__)    # 类名
print(isinstance(p, Person))  # 是不是这个类的实例'''
    )
    + pre(
        '''{'name': 'Alice', 'age': 30}
Person
True'''
    )
    + p(
        "<code>p.__dict__</code> 直接把属性表打出来，比逐个猜快得多：里面少了哪个属性，就说明 <code>__init__</code> 里漏了对应的 <code>self.xxx = ...</code>。"
    )
    + h2("十、常见错误与调试")
    + cal(
        "warn",
        "忘记写 self",
        "定义方法时写成 <code>def start_engine():</code>，调用 <code>car.start_engine()</code> 会抛 <code>TypeError: start_engine() takes 0 positional arguments but 1 was given</code>——那个多出来的实参就是自动传入的对象。",
    )
    + cal(
        "warn",
        "__init__ 拼错",
        "写成 <code>__int__</code>、<code>_init_</code> 或 <code>init</code>，创建对象时不会执行，属性全部不存在，之后访问 <code>car.brand</code> 抛 <code>AttributeError</code>。前后各两个下划线，一个都不能少。",
    )
    + cal(
        "warn",
        "属性赋值漏了 self.",
        "在 <code>__init__</code> 里写 <code>brand = brand</code>，只是创建了一个局部变量，对象上没有这个属性。必须是 <code>self.brand = brand</code>。",
    )
    + cal(
        "warn",
        "直接打印对象只看到地址",
        "<code>print(car)</code> 输出 <code>&lt;__main__.Car object at 0x...&gt;</code>，因为默认没有「怎么显示自己」的规则。要看内容请打印具体属性，或在类里定义 <code>__str__</code>（属拓展内容，考试不要求）。",
    )
    + cal(
        "tip",
        "设计类先列名词与动词",
        "把需求里的名词挑出来当属性（brand、year、price），动词挑出来当方法（start、update、is_adult）。列不出来说明这个类还不该存在。",
    )
)

_K7 = K(
    ("class", "类", "A template for creating objects."),
    ("object", "对象", "A concrete thing created from a class."),
    (
        "instance",
        "实例",
        "One particular object of a class; car1 is an instance of Car.",
    ),
    ("attribute", "属性", "A variable stored in the object: self.brand."),
    ("method", "方法", "A function defined inside a class: start_engine()."),
    (
        "constructor",
        "构造函数",
        "__init__ runs automatically when an object is created.",
    ),
    ("self", "自身引用", "Refers to the current object inside the class."),
    (
        "dot notation",
        "点号访问",
        "car.year reads an attribute; car.start() calls a method.",
    ),
    (
        "instantiate",
        "实例化",
        'Create an object from a class: car = Car("Tesla", 2019).',
    ),
    (
        "object-oriented programming",
        "面向对象编程",
        "Organising code around classes and objects.",
    ),
    ("state", "状态", "The current values of an object's attributes."),
    ("behaviour", "行为", "What an object can do, defined by its methods."),
)

_EX7 = (
    qa(
        "例 1　定义 <code>Car</code> 类（品牌、颜色、年份 + 启动方法），创建两辆车并输出品牌。",
        p("这是课件 L6E1 的完整结构：构造函数装数据，方法用数据。")
        + pre(
            """class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def start_engine(self):
        print(self.brand + " says WROOM!")

car1 = Car("Tesla", "Black", 2019)
car2 = Car("Skoda", "Grey", 2012)

print(car1.brand, car1.color, car1.year)
print(car2.brand, car2.color, car2.year)
car1.start_engine()
car2.start_engine()"""
        )
        + p("输出：")
        + pre(
            """Tesla Black 2019
Skoda Grey 2012
Tesla says WROOM!
Skoda says WROOM!"""
        )
        + p(
            '逐点解释：<code>Car("Tesla", "Black", 2019)</code> 自动调用 <code>__init__</code>，三个值分别挂到 <code>self.brand</code>、<code>self.color</code>、<code>self.year</code>；两个实例互不影响；<code>start_engine</code> 里用 <code>self.brand</code> 取当前对象的品牌，所以同一段代码对两辆车输出不同文字。'
        ),
    )
    + qa(
        "例 2　给 <code>Person</code> 类加一个 <code>birthday()</code> 方法，使年龄加一，并验证对象状态确实变了。",
        p(
            "修改状态的方法要直接写 <code>self.age = self.age + 1</code>，调用后同一个对象再查询就能看到变化。"
        )
        + pre(
            """class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

    def is_adult(self):
        return self.age >= 18

p = Person("Pekka", 17)
print(p.name, p.age, p.is_adult())
p.birthday()
print(p.name, p.age, p.is_adult())"""
        )
        + p("输出：")
        + pre(
            """Pekka 17 False
Pekka 18 True"""
        )
        + p(
            "解释：<code>birthday()</code> 没有参数（除 self），也不返回值——它的作用是改状态。这类「只做副作用、不返回值」的方法很常见，调用后要重新读属性来确认效果。"
        ),
    )
    + qa(
        "例 3　写一个 <code>BankAccount</code> 类，支持存款、取款、查余额；取款金额超过余额时拒绝并给出提示。",
        p("把规则写进方法里，调用方就不必自己判断——这是类相对「裸字典」的优势。")
        + pre(
            """class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount

    def show(self):
        print(self.owner, "balance:", self.balance)

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(500)
acc.withdraw(30)
acc.show()"""
        )
        + p("输出：")
        + pre(
            """Insufficient funds
Alice balance: 120"""
        )
        + p(
            '解释：初始 100，存 50 得 150；取 500 被拒绝，余额不变；取 30 得 120。注意 <code>__init__</code> 的 <code>balance=0</code> 是默认参数（不可变对象，安全），可以 <code>BankAccount("Bob")</code> 只给名字。'
        ),
    )
)

_PR7 = ol(
    "定义 <code>Rectangle</code> 类（宽、高），带 <code>area()</code> 与 <code>perimeter()</code> 两个方法。",
    "给 <code>Person</code> 类加一个 <code>greet()</code> 方法，输出 <code>Hi, I am NAME</code>。",
    "定义 <code>Student</code> 类（姓名、学号、成绩列表），加方法 <code>average()</code> 返回平均分。",
    "写 <code>Counter</code> 类，有 <code>increment()</code> 与 <code>value()</code> 两个方法，模拟一个计数器。",
    "把第 5 讲的乘法表程序改写成 <code>MultiplicationTable</code> 类，方法 <code>show(n)</code> 打印 n 行。",
) + det(
    "答案与思路",
    p(
        "<b>1.</b> <code>__init__(self, w, h)</code> 存两个属性；<code>area</code> 返回 <code>self.w * self.h</code>；<code>perimeter</code> 返回 <code>2 * (self.w + self.h)</code>。测试 <code>Rectangle(3, 4)</code>：面积 12、周长 14。"
    )
    + p(
        '<b>2.</b> <code>def greet(self): print("Hi, I am " + self.name)</code>。用「方法内部拼接」而不是返回值，是因为要求是「输出」；若题目说「返回问候语」，就得写 <code>return</code>（第 6 讲的区别）。'
    )
    + p(
        "<b>3.</b> <code>average</code> 里要防零：<code>if not self.grades: return 0</code>，否则 <code>sum / 0</code> 抛异常。成绩列表是可变对象，直接存引用即可，但若担心外部改动，可在 <code>__init__</code> 里写 <code>self.grades = list(grades)</code>。"
    )
    + p(
        "<b>4.</b> <code>__init__</code> 里 <code>self.count = 0</code>；<code>increment</code> 里 <code>self.count += 1</code>；<code>value</code> 返回 <code>self.count</code>。三次 <code>increment()</code> 后 <code>value()</code> 应为 3。"
    )
    + p(
        '<b>5.</b> 方法 <code>show(self, n)</code> 里用双重循环：外层 <code>range(1, n + 1)</code>，内层 <code>range(1, i + 1)</code>，内层 <code>print(..., end="\\t")</code>，外层结束后 <code>print()</code>。类在这里只是「把数据和操作打包」的容器，循环逻辑与第 5 讲完全相同。'
    ),
)

_EXAM7 = (
    cal(
        "exam",
        "必考",
        "类与实例的区别；<code>__init__</code> 自动调用；<code>self</code> 的含义与省略规则；属性与方法的点号访问；多个实例状态独立。",
    )
    + cal(
        "warn",
        "易错 1　方法忘记 self",
        "定义时 <code>def f():</code> 而调用 <code>obj.f()</code> 会多传一个实参，报 <code>TypeError</code>。类里所有实例方法第一个参数都写 <code>self</code>。",
    )
    + cal(
        "warn",
        "易错 2　属性写在类里而不是 __init__ 里",
        '在类体里直接写 <code>brand = "Tesla"</code> 是<b>类属性</b>，所有实例共享；要每个对象一份，必须写 <code>self.brand = ...</code>。两者读起来都能 <code>obj.brand</code>，但改一个会影响全部，非常隐蔽。',
    )
    + cal(
        "warn",
        "易错 3　__init__ 名字拼错",
        "少了任一端的双下划线就不会被自动调用，属性不存在，随后 <code>AttributeError</code>。写完先 <code>print(obj.__dict__)</code> 看属性有没有装上。",
    )
    + cal(
        "tip",
        "进阶",
        "<code>__str__</code> 可以自定义 <code>print(obj)</code> 的内容；<code>isinstance(obj, Car)</code> 可以判断类型。两者都超出本课考点，但读课件之外的代码时会遇到。",
    )
)

_CK7 = (
    h2("操作清单")
    + h3("定义类之前")
    + st(
        "列出需求里的名词 → 这些是属性",
        "列出需求里的动词 → 这些是方法",
        "确认哪些数据必须「每个对象一份」→ 写进 <code>__init__</code> 并用 <code>self.</code>",
        "确认哪些规则应该由类自己守 → 写成方法，而不是让调用方判断",
    )
    + h3("写完后的检查")
    + ck(
        "类名首字母大写，<code>__init__</code> 前后各两个下划线",
        "每个方法第一个参数都是 <code>self</code>",
        "所有属性赋值都写了 <code>self.</code>",
        "创建对象时实参个数与 <code>__init__</code> 的参数（不含 self）一致",
        "打印对象时输出的是属性而不是 <code>&lt;... object at 0x...&gt;</code>",
    )
)

_MP7 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Chapter 6 Part 1 - Introduction to Classes.pdf",
            "p2–p4",
            "OOP 的定位、类与实例的比喻、属性/实例变量、Python 中一切皆对象",
        ),
        (
            "Chapter 6 Part 2 - More on classes.pdf",
            "p2–p7",
            "class / object / attribute / method 四术语、点号访问、<code>__init__</code> 构造函数、<code>self</code>、创建对象",
        ),
        (
            "Chapter 6 - Part 3 - More Code Examples on Classes.pdf",
            "p2",
            "Person 类的属性与方法清单：get_name/get_age/get_country/is_adult/update_age/update_country",
        ),
        (
            "L6E1.py",
            "全文",
            "Car 类完整示例、两个实例、方法读取属性",
        ),
        (
            "L6E2.py / example.py",
            "全文",
            "Person 类完整示例、更新状态、对象作为函数参数",
        ),
    )
    + p(
        "<b>跳过项：</b>Part 1 的 1980 年代配图、Part 2 的类图截图只有图片没有新文字；Moodle 的作业与评分页属于行政信息，不进入本讲。"
    )
    + p(
        "<b>拓展项：</b>类属性与实例属性的区别、<code>__dict__</code> 查看属性、<code>isinstance</code> 与 <code>__str__</code> 的提及，都是围绕「属性从哪里来」的边界补充，不引入新考点。"
    )
)

LEC.append(
    L(
        slug="ch07-classes",
        tzh="⑦ 类与对象入门",
        ten="Classes and Objects",
        keywords=[
            "class",
            "object",
            "instance",
            "attribute",
            "method",
            "constructor",
            "self",
            "dot notation",
            "instantiate",
            "state",
        ],
        files=[
            "Chapter 6 Part 1 - Introduction to Classes.pdf",
            "Chapter 6 Part 2 - More on classes.pdf",
            "Chapter 6 - Part 3 - More Code Examples on Classes.pdf",
            "12_Chapter 6_1_Chapter 6 Code Examples_L6E1.py",
            "12_Chapter 6_1_Chapter 6 Code Examples_L6E2.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "前六讲的数据都是「一个变量装一个值」，函数是「一段代码做一件事」。当一组数据要配上一组操作、还要被很多地方重复使用时，就需要类：把数据（属性）和行为（方法）打包成一个对象。"
            )
            + p(
                "这一讲只讲最浅的一层——够读课件、够写项目作业里的 Car / Person / Transaction。真正的 OOP（继承、多态、封装）是另一门课的内容，本课不考。下一讲回到容器：列表、矩阵与元组。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "解释类与实例的关系，并说出「类是模板、对象是实例」",
                "写出带 <code>__init__</code> 的类，用 <code>self</code> 把参数装成属性",
                "定义方法并用点号调用，读写的都是当前对象的属性",
                "创建多个实例，并说明它们的状态为什么互不影响",
                "把对象作为参数传给普通函数，在函数里调用它的方法",
                "认出漏写 <code>self</code>、<code>__init__</code> 拼错、类属性误当实例属性这三类错误",
            )
        ),
        detail=_D7,
        kws=_K7,
        examples=_EX7,
        practice=_PR7,
        exam=_EXAM7,
        checklist=_CK7,
        mapping=_MP7,
    )
)

# ============================================================ 8 列表、矩阵与元组
_D8 = (
    h2("一、列表：一个变量装一串值")
    + p(
        '列表（list）是最常用的容器（Chapter 6 Part 4 p2）：方括号里放若干项，逗号分隔，<code>fruits = ["apple", "banana", "pineapple", "orange"]</code>。一个变量名，装一整串数据。'
    )
    + pre(
        """fruits = ["apple", "banana", "pineapple", "orange"]
print(fruits)
print(len(fruits))
empty = []
print(empty)"""
    )
    + pre(
        """['apple', 'banana', 'pineapple', 'orange']
4
[]"""
    )
    + p(
        "列表与字符串有很多共同点（p2）：都能索引、都能切片、都能用 <code>len()</code>、都能被 <code>for</code> 遍历。不同点只有一条，但很关键——<b>列表可变，字符串不可变</b>。"
    )
    + pre(
        """fruits = ["apple", "banana", "pineapple", "orange"]
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[::-1])"""
    )
    + pre(
        """apple
orange
['banana', 'pineapple']
['orange', 'pineapple', 'banana', 'apple']"""
    )
    + p(
        "切片规则与第 3 讲完全相同：含头不含尾，越界不报错，结果是<b>新列表</b>。所以 <code>fruits[1:3]</code> 得到的是两个元素的新列表，改它不会动到 <code>fruits</code>。"
    )
    + h2("二、遍历列表的三种写法")
    + p("L6E3 把三种写法摆在一起（Part 4 p4），各自适合不同场景：")
    + pre(
        """my_list = [1, 2, 3, 4, 5]

for item in my_list:            # 1. 直接取元素
    print(item, end=" ")
print()

for i in range(len(my_list)):   # 2. 取下标再取元素
    print(my_list[i], end=" ")
print()

i = 0                           # 3. while 手动控制下标
while i < len(my_list):
    print(my_list[i], end=" ")
    i = i + 1
print()"""
    )
    + pre(
        """1 2 3 4 5
1 2 3 4 5
1 2 3 4 5"""
    )
    + tb(
        ("写法", "优点", "什么时候用"),
        ("<code>for item in L</code>", "最短、最不容易出错", "只需要元素值"),
        (
            "<code>for i in range(len(L))</code>",
            "能拿到下标",
            "需要下标做位置运算、或要改元素",
        ),
        (
            "<code>while i &lt; len(L)</code>",
            "可以自由控制 i 的推进",
            "需要跳过、回退或条件式推进",
        ),
    )
    + p(
        "需要同时拿到下标与元素时，Python 还有 <code>enumerate()</code>，写作 <code>for i, item in enumerate(L)</code>。它超出本讲考点，但项目作业里很常见。"
    )
    + h2("三、可变性：列表能原地改")
    + p("字符串不能改单个字符，列表可以（Part 5 p5）：")
    + pre(
        """L = [1, 2, 3]
L[1] = 5
print(L)"""
    )
    + pre("""[1, 5, 3]""")
    + p(
        "除了按下标改，还能整体替换一段（切片赋值），例如 <code>L[1:3] = [8, 9, 10]</code> 会把中间两个元素换成长度不同的三个。这个写法容易把列表长度搞乱，初学阶段建议只用「按下标改」与下面要讲的列表方法。"
    )
    + h2("四、列表方法与内置函数")
    + h3("4.1 常用方法")
    + p("列表本身也是类（Part 5 p3），每个列表对象都带着一批方法。下表是最常用的十个：")
    + tb(
        ("方法", "作用", "返回值", "例子"),
        (
            "<code>L.append(x)</code>",
            "在末尾加一个元素",
            "<code>None</code>",
            "<code>[1,2].append(3)</code> → <code>[1,2,3]</code>",
        ),
        (
            "<code>L.extend(M)</code>",
            "把另一个列表的元素逐个加进来",
            "<code>None</code>",
            "<code>[1].extend([2,3])</code> → <code>[1,2,3]</code>",
        ),
        (
            "<code>L.insert(i, x)</code>",
            "在下标 i 处插入 x",
            "<code>None</code>",
            "<code>[1,3].insert(1,2)</code> → <code>[1,2,3]</code>",
        ),
        (
            "<code>L.remove(x)</code>",
            "删掉第一个等于 x 的元素",
            "<code>None</code>",
            "找不到则 <code>ValueError</code>",
        ),
        (
            "<code>L.pop()</code>",
            "删掉并返回最后一个元素",
            "被删的元素",
            "<code>[1,2,3].pop()</code> → <code>3</code>",
        ),
        (
            "<code>L.pop(i)</code>",
            "删掉并返回下标 i 的元素",
            "被删的元素",
            "<code>[1,2,3].pop(0)</code> → <code>1</code>",
        ),
        (
            "<code>L.index(x)</code>",
            "x 第一次出现的下标",
            "整数",
            "找不到则 <code>ValueError</code>",
        ),
        (
            "<code>L.count(x)</code>",
            "x 出现的次数",
            "整数",
            "<code>[1,1,2].count(1)</code> → <code>2</code>",
        ),
        ("<code>L.sort()</code>", "原地排序", "<code>None</code>", "改的是 L 本身"),
        (
            "<code>L.reverse()</code>",
            "原地倒序",
            "<code>None</code>",
            "等价于 <code>L = L[::-1]</code>，但不动原对象",
        ),
    )
    + cal(
        "warn",
        "这些方法返回 None，不是新列表",
        "<code>L = L.append(4)</code> 会把 <code>L</code> 变成 <code>None</code>，随后 <code>len(L)</code> 报 <code>TypeError</code>。正确写法是单独一行 <code>L.append(4)</code>。同样，<code>L = L.sort()</code> 会把整个列表弄丢。",
    )
    + h3("4.2 内置函数：不修改原列表")
    + p("课件把内置函数与列表方法分开讲（Part 5 p2），区别就在「改不改原列表」：")
    + pre(
        """L = [3, 1, 2]
print(len(L))
print(sorted(L))
print(L)
print(min(L), max(L), sum(L))"""
    )
    + pre(
        """3
[1, 2, 3]
[3, 1, 2]
1 3 6"""
    )
    + p(
        "<code>sorted(L)</code> 返回排好序的<b>新列表</b>，<code>L</code> 保持原样；<code>L.sort()</code> 直接把 <code>L</code> 排序、返回 <code>None</code>。考试常问「哪个改变了原列表」，答案看返回值是不是 <code>None</code>。"
    )
    + p(
        "两个前提：<code>min</code> / <code>max</code> 要求元素之间能比较（全是数字或全是字符串，混着来会 <code>TypeError</code>）；<code>sum</code> 要求元素是数字。空列表上 <code>min</code> / <code>max</code> 会抛 <code>ValueError</code>。"
    )
    + h2("五、从输入构建列表")
    + p(
        'L6E4 是「输入 → 字符串 → 列表」的标准流水线（Part 5 p6）：<code>input()</code> 拿到一整行，<code>split(",")</code> 切成字符串列表，再逐个 <code>int()</code> 转成数字列表。'
    )
    + pre(
        """input_string = input("Give integers separated by comma:\\n")
list_of_chars = input_string.split(",")
print(list_of_chars)

list_of_ints = []
for piece in list_of_chars:
    list_of_ints.append(int(piece))

print(list_of_ints)"""
    )
    + p("输入 <code>3,1,4,1,5</code>，输出：")
    + pre(
        """['3', '1', '4', '1', '5']
[3, 1, 4, 1, 5]"""
    )
    + p(
        '注意两个列表的区别：第一个装的是字符串（打印时带引号），第二个才是整数。若输入里有空格（<code>"3, 1, 4"</code>），<code>int(" 1")</code> 仍能成功（两端空白被忽略），但若用 <code>split()</code> 不带参数，则会按任意空白切分，逗号会留在元素里。'
    )
    + h2("六、矩阵：列表的列表")
    + p(
        "把列表套进列表，就是矩阵（matrix，Part 6 p2）：外层每个元素是一行，内层每个元素是一格。<code>M = [[1,4,5],[-5,8,9]]</code> 是 2 行 3 列。"
    )
    + pre(
        """M = [[1, 4, 5], [-5, 8, 9]]
print(M[0])
print(M[1])
print(M[1][0])
print(len(M), len(M[0]))"""
    )
    + pre(
        """[1, 4, 5]
[-5, 8, 9]
-5
2 3"""
    )
    + p(
        "读法：<b>第一个下标选行，第二个下标选列</b>。<code>M[1][0]</code> 是第 2 行第 1 列，得 −5。注意 <code>M[1, 0]</code>（逗号写在一个方括号里）对普通列表是错的，那是 NumPy 的写法（第 10 讲）。"
    )
    + p("遍历矩阵要两层循环：外层拿行，内层拿格（L6E5）：")
    + pre(
        """list_of_lists = [[1, 2], [3, 4], [5, 6]]
for row in list_of_lists:
    for value in row:
        print(value, end=" ")
    print()"""
    )
    + pre(
        """1 2
3 4
5 6"""
    )
    + p("求「每行之和」时，内层用累加器、外层负责清零与输出：")
    + pre(
        """M = [[1, 4, 5], [-5, 8, 9]]
for row in M:
    total = 0
    for value in row:
        total = total + value
    print("row sum:", total)"""
    )
    + pre(
        """row sum: 10
row sum: 12"""
    )
    + p("转置（行列互换）需要按下标遍历，且内层用列号取各行的同一列：")
    + pre(
        """M = [[1, 2, 3], [4, 5, 6]]
T = []
for c in range(len(M[0])):
    new_row = []
    for r in range(len(M)):
        new_row.append(M[r][c])
    T.append(new_row)
print(T)"""
    )
    + pre("""[[1, 4], [2, 5], [3, 6]]""")
    + p(
        "这个双重循环的「外列内行」顺序是转置的关键：外层走列号，内层走行号，于是新矩阵的第 c 行收集的是原矩阵的第 c 列。"
    )
    + h2("七、别名、拷贝与浅拷贝")
    + h3("7.1 B = A 不是复制")
    + p(
        "课件专门警告（Mutable vs immutable p4）：<code>B = A</code> 只是让两个名字指向<b>同一个对象</b>，通过 B 改内容，A 看到的也变了。"
    )
    + pre(
        """A = [1, 2, 3]
B = A
B[0] = 100
print(A)
print(B)
print(A is B)"""
    )
    + pre(
        """[100, 2, 3]
[100, 2, 3]
True"""
    )
    + p(
        "<code>is</code> 比较「是不是同一个对象」，<code>==</code> 比较「内容是否相等」。上面两者 <code>is</code> 为 <code>True</code>，说明根本没有复制。"
    )
    + h3("7.2 怎样真的复制")
    + pre(
        """A = [1, 2, 3]
B = A[:]        # 切片复制
C = list(A)     # 用 list() 构造
D = A.copy()    # 列表方法
B[0] = 100
print(A, C, D)"""
    )
    + pre("""[1, 2, 3] [1, 2, 3] [1, 2, 3]""")
    + p(
        "三种写法都产生新列表，但都是<b>浅拷贝</b>（shallow copy）：只复制最外层，内层元素仍是共享的引用。"
    )
    + pre(
        """M = [[0, 0], [0, 0]]
N = M[:]
N[0][0] = 9
print(M)"""
    )
    + pre("""[[9, 0], [0, 0]]""")
    + p(
        "改 <code>N[0][0]</code> 会改到 <code>M</code>，因为 <code>M[0]</code> 与 <code>N[0]</code> 是同一个内层列表。彻底独立要深拷贝（deep copy），第 12 讲用 <code>copy.deepcopy</code> 处理。"
    )
    + cal(
        "warn",
        "[[0] * 3] * 3 是三重别名",
        "<code>[[0] * 3] * 3</code> 里的三行是<b>同一个</b>内层列表的三份引用：改 <code>grid[0][0]</code>，三行一起变。要造独立矩阵，写 <code>[[0] * 3 for _ in range(3)]</code>（列表推导属拓展）或老老实实嵌套 append。",
    )
    + h2("八、元组：不能改的列表")
    + h3("8.1 创建与访问")
    + p(
        "元组（tuple）用圆括号，逗号分隔；有序、可索引、<b>不可变</b>（tuples.pdf p2–p3）。"
    )
    + pre(
        """t = (1, "two", 3.0)
print(t[0])
print(t[-1])
print(t[1:])
print(len(t))"""
    )
    + pre(
        """1
3.0
('two', 3.0)
3"""
    )
    + p(
        "单个元素的元组必须带逗号：<code>(5)</code> 只是数字 5，<code>(5,)</code> 才是元组。空元组写 <code>()</code>。"
    )
    + pre(
        """print(type((5)))
print(type((5,)))"""
    )
    + pre(
        """<class 'int'>
<class 'tuple'>"""
    )
    + p(
        "元组不可变，所以 <code>t[0] = 9</code> 抛 <code>TypeError</code>；但元组内部若装了列表，那个列表仍可改——「不可变」指的是元组自己的格子不能换。"
    )
    + h3("8.2 两个方法与解包")
    + p(
        "元组只有两个常用方法（tuples.pdf p6）：<code>count(x)</code> 数出现次数，<code>index(x)</code> 找第一次出现的下标。"
    )
    + pre(
        """t = (1, 2, 2, 3)
print(t.count(2))
print(t.index(3))"""
    )
    + pre(
        """2
3"""
    )
    + p("解包（unpacking）是元组最有用的地方：把元组里的值一次分给多个变量。")
    + pre(
        """point = (3, 7)
x, y = point
print(x, y)

a, b = 1, 2
a, b = b, a
print(a, b)"""
    )
    + pre(
        """3 7
2 1"""
    )
    + p(
        "第二段是交换两个变量的标准写法，<code>a, b = b, a</code> 右边其实是一个元组 <code>(b, a)</code>，左边解包赋值。它比用临时变量更短，考试常考。"
    )
    + h3("8.3 用元组返回多个值")
    + p(
        "函数一次只能 <code>return</code> 一个对象，于是把多个值装进元组返回（tuples.pdf p7、tuple.py）："
    )
    + pre(
        """def area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

result = area_and_perimeter(3, 4)
print(result)
a, p = result
print(a, p)"""
    )
    + pre(
        """(12, 14)
12 14"""
    )
    + p(
        "也可以直接 <code>area, perimeter = area_and_perimeter(3, 4)</code>，一步拿到两个值。课件里那句 <code>result[0]</code>、<code>result[1]</code> 的写法更啰嗦，但等价。"
    )
    + h3("8.4 列表与元组怎么选")
    + tb(
        ("维度", "列表 list", "元组 tuple"),
        ("可变性", "可变，能增删改", "不可变，创建后固定"),
        ("写法", "<code>[1, 2, 3]</code>", "<code>(1, 2, 3)</code>"),
        (
            "方法",
            "append / sort / pop 等十个以上",
            "只有 <code>count</code> 与 <code>index</code>",
        ),
        ("典型用途", "会变化的数据集合", "固定的一组值：坐标、RGB、函数返回的多个值"),
        ("性能", "略慢（要支持修改）", "略快、占用更小（tuples.pdf p5）"),
    )
    + cal(
        "tip",
        "默认选列表，除非确定要「不许改」",
        "元组的价值是表达意图：坐标 <code>(3, 7)</code>、颜色 <code>(255, 0, 0)</code> 本来就不该被改。写进元组，读代码的人立刻知道它不会被修改。",
    )
    + h2("九、常见错误与调试")
    + cal(
        "warn",
        "把返回 None 的方法当函数用",
        "<code>L = L.append(4)</code>、<code>L = L.sort()</code>、<code>L = L.reverse()</code> 都会把列表变成 <code>None</code>。方法是「对 L 做动作」，不是「返回一个新 L」。",
    )
    + cal(
        "warn",
        "IndexError 与 off-by-one",
        "长度为 n 的列表，合法下标是 0 到 n−1（或 −n 到 −1）。<code>L[len(L)]</code> 一定越界；遍历用 <code>range(len(L))</code> 而不是 <code>range(len(L) + 1)</code>。",
    )
    + cal(
        "warn",
        "遍历时删除元素",
        "<code>for x in L: L.remove(x)</code> 会漏掉元素。改成 <code>for x in L[:]</code>（遍历副本）或先收集要删的、再统一删。",
    )
    + cal(
        "tip",
        "先打印类型再猜",
        "分不清元素是字符串还是数字时，<code>print(type(L[0]))</code> 或 <code>print(L)</code> 看有没有引号。字符串列表打印形如 <code>['3', '1']</code>，整数列表是 <code>[3, 1]</code>。",
    )
)

_K8 = K(
    ("list", "列表", "An ordered, mutable collection: [1, 2, 3]."),
    ("element / item", "元素", "One value stored in the list."),
    ("index", "下标", "L[0] is the first element, L[-1] the last."),
    ("slice", "切片", "L[1:3] returns a new list with two elements."),
    ("mutable", "可变的", "Lists can be changed after creation."),
    ("append", "追加", "L.append(x) adds x at the end and returns None."),
    ("sort / sorted", "排序", "L.sort() sorts in place; sorted(L) returns a new list."),
    ("nested list", "嵌套列表", "A list whose elements are lists; used as a matrix."),
    ("matrix", "矩阵", "M[r][c] selects row r, column c."),
    ("alias", "别名", "B = A makes both names refer to the same object."),
    ("shallow copy", "浅拷贝", "L[:] copies the outer list only."),
    ("tuple", "元组", "An immutable sequence: (1, 2, 3)."),
    ("unpacking", "解包", "x, y = point assigns both values at once."),
    ("immutable", "不可变的", "A tuple cannot be changed after creation."),
)

_EX8 = (
    qa(
        "例 1　读入一行逗号分隔的整数，输出列表、总和与平均值。",
        p(
            "流水线：<code>input</code> → <code>split</code> → 逐个 <code>int()</code> 装进新列表 → 用内置函数统计。"
        )
        + pre(
            """line = input("Give integers separated by comma: ")
pieces = line.split(",")

numbers = []
for piece in pieces:
    numbers.append(int(piece))

print("list:", numbers)
print("len:", len(numbers))
print("sum:", sum(numbers))
print("avg:", sum(numbers) / len(numbers))"""
        )
        + p("输入 <code>3,1,4,1,5</code>，输出：")
        + pre(
            """list: [3, 1, 4, 1, 5]
len: 5
sum: 14
avg: 2.8"""
        )
        + p(
            "解释：<code>split(\",\")</code> 得到字符串列表；<code>append</code> 在循环里逐个补进 <code>numbers</code>；<code>sum</code> 与 <code>len</code> 是内置函数，不改列表。若输入为空行，<code>split</code> 得到 <code>['']</code>，<code>int('')</code> 会抛 <code>ValueError</code>——真实程序要先判空。"
        ),
    )
    + qa(
        "例 2　给定 3×3 矩阵，输出每行的和与每列的和。",
        p("行和用「外层取行、内层累加」；列和用「外层走列号、内层走行号」。")
        + pre(
            """M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in M:
    total = 0
    for v in row:
        total = total + v
    print("row sum:", total)

for c in range(len(M[0])):
    total = 0
    for r in range(len(M)):
        total = total + M[r][c]
    print("col", c, "sum:", total)"""
        )
        + p("输出：")
        + pre(
            """row sum: 6
row sum: 15
row sum: 24
col 0 sum: 12
col 1 sum: 15
col 2 sum: 18"""
        )
        + p(
            "解释：行和的累加器 <code>total</code> 在<b>外层循环体内</b>清零，所以每行独立；列和的外层是列号 <code>c</code>，内层用 <code>M[r][c]</code> 竖着取值。两段代码的差别只有下标顺序，这正是矩阵题的核心。"
        ),
    )
    + qa(
        "例 3　用元组让函数同时返回面积与周长，并解包使用。",
        p(
            "先把两个结果装进元组返回，再在调用处解包；顺带说明「元组不可变」不影响内部计算。"
        )
        + pre(
            """def area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

area, perimeter = area_and_perimeter(3, 4)
print("area:", area)
print("perimeter:", perimeter)

result = area_and_perimeter(3, 4)
print(result, type(result))"""
        )
        + p("输出：")
        + pre(
            """area: 12
perimeter: 14
(12, 14) <class 'tuple'>"""
        )
        + p(
            "解释：<code>return (area, perimeter)</code> 返回一个二元组；<code>area, perimeter = ...</code> 按位置解包。<code>type(result)</code> 确认它是 <code>tuple</code> 而不是列表——元组更适合「一次性的多值返回」。"
        ),
    )
    + qa(
        "例 4　演示 <code>sort()</code> 与 <code>sorted()</code> 的差别，以及 <code>B = A</code> 的别名效果。",
        p("用 <code>is</code> 判断是不是同一个对象，是最直接的验证手段。")
        + pre(
            """A = [3, 1, 2]
B = sorted(A)
print("A after sorted:", A)
print("B:", B)

C = A
C.sort()
print("A after C.sort():", A)
print("C is A:", C is A)

D = A[:]
D[0] = 99
print("A:", A)
print("D:", D)
print("D is A:", D is A)"""
        )
        + p("输出：")
        + pre(
            """A after sorted: [3, 1, 2]
B: [1, 2, 3]
A after C.sort(): [1, 2, 3]
C is A: True
A: [1, 2, 3]
D: [99, 2, 3]
D is A: False"""
        )
        + p(
            "解释：<code>sorted(A)</code> 不动 A；<code>C = A</code> 后 <code>C.sort()</code> 改的是同一个对象，所以 A 也变了；<code>D = A[:]</code> 才是副本，改 D 不影响 A。这三行就是「别名 vs 拷贝」的全部区别。"
        ),
    )
)

_PR8 = ol(
    "读入 5 个整数存入列表，输出最大值、最小值与平均值（不用 <code>max</code> / <code>min</code>，自己写循环）。",
    "把 <code>[3, 1, 4, 1, 5, 9, 2, 6]</code> 去重后按升序输出（提示：循环 + <code>in</code> 判断）。",
    "给定 2×3 矩阵，输出它的转置（3×2）。",
    "写函数 <code>min_max(L)</code>，用元组返回列表中的最小值与最大值。",
    "解释并修正这段代码：<code>L = [1, 2, 3]; L = L.append(4); print(len(L))</code>。",
) + det(
    "答案与思路",
    p(
        "<b>1.</b> <code>nums = []</code> 收集输入；<code>biggest = nums[0]</code>、<code>smallest = nums[0]</code>；循环里逐个比较更新；平均用 <code>sum(nums) / len(nums)</code>。初值取第一个元素而不是 0，才能处理全负数。"
    )
    + p(
        "<b>2.</b> <code>result = []</code>，<code>for x in L: if x not in result: result.append(x)</code>，再 <code>result.sort()</code>。这是「先判断再追加」的模式；用 <code>in</code> 在列表上查找是线性时间，元素多时更该用第 12 讲的集合。"
    )
    + p(
        "<b>3.</b> 外层 <code>for c in range(len(M[0]))</code>，内层 <code>for r in range(len(M))</code>，把 <code>M[r][c]</code> 追加到新行，再把新行 <code>append</code> 到结果。"
    )
    + p(
        "<b>4.</b> 循环比较得两个极值，<code>return (smallest, biggest)</code>，调用处 <code>lo, hi = min_max(L)</code>。空列表要单独处理（返回 <code>None, None</code> 或抛 <code>ValueError</code>）。"
    )
    + p(
        "<b>5.</b> <code>append</code> 返回 <code>None</code>，所以第三行把 <code>L</code> 变成了 <code>None</code>，<code>len(None)</code> 抛 <code>TypeError</code>。改成 <code>L.append(4)</code> 单独一行，再 <code>print(len(L))</code> 得 4。"
    ),
)

_EXAM8 = (
    cal(
        "exam",
        "必考",
        "列表的索引与切片（含头不含尾）；<code>append</code> / <code>pop</code> / <code>remove</code> 的行为；<code>sort()</code> 与 <code>sorted()</code> 的差别；矩阵的双下标；元组的不可变与解包。",
    )
    + cal(
        "warn",
        "易错 1　方法返回 None",
        "<code>L = L.append(x)</code>、<code>L = L.sort()</code> 会把列表变成 None。要新列表就用 <code>sorted(L)</code> 或 <code>L + [x]</code>。",
    )
    + cal(
        "warn",
        "易错 2　别名当成拷贝",
        "<code>B = A</code> 是同一对象；矩阵的 <code>M[:]</code> 只是浅拷贝，改内层会同时改两边；<code>[[0] * 3] * 3</code> 三行共享。",
    )
    + cal(
        "warn",
        "易错 3　遍历时删除 / 越界",
        "遍历中 <code>remove</code> 会跳过元素；<code>L[len(L)]</code> 必然越界。改元素用下标遍历，删元素遍历副本。",
    )
    + cal(
        "tip",
        "进阶",
        "列表推导 <code>[x * 2 for x in L]</code> 与 <code>enumerate</code> 在项目作业里很常见；元组比列表更省内存、遍历更快，所以「固定的一组值」优先用元组。",
    )
)

_CK8 = (
    h2("操作清单")
    + h3("处理列表之前先想清楚")
    + st(
        "这份数据会不会变？会变用列表，不变用元组",
        "我要的是元素还是下标？要下标就 <code>range(len(L))</code>",
        "这个操作是「改原列表」还是「产生新列表」？看方法有没有返回值",
        "要不要保留原数据？要就先 <code>L[:]</code> 或 <code>sorted(L)</code>",
    )
    + h3("写完后的检查")
    + ck(
        "下标范围在 0 到 <code>len(L) - 1</code> 之内",
        "没有把返回 None 的方法赋回给列表变量",
        "矩阵用两个下标，先选行再选列",
        "元组解包时变量个数与元素个数一致",
        "需要独立副本时用了 <code>L[:]</code> / <code>list(L)</code> / <code>copy.deepcopy</code>",
    )
)

_MP8 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Chapter 6 - Part 4 - List.pdf",
            "p2–p4",
            "列表定义与空列表、索引与切片、遍历列表（L6E3 三种写法）",
        ),
        (
            "Chapter 6 - Part 5 - List Builtins and Methods.pdf",
            "p2–p6",
            "<code>len/sorted/min/max/sum</code>、列表也是类、常用方法、可变性、输入转列表",
        ),
        (
            "Chapter 6 - Part 6 - Matrix.pdf",
            "p2–p3",
            "列表的列表即矩阵、行与列的下标、2×3 类型、矩阵遍历示例",
        ),
        (
            "tuples.pdf",
            "p2–p7",
            "元组定义与不可变、索引、用途（坐标/RGB/多返回值）、列表与元组对比、<code>count</code> 与 <code>index</code>",
        ),
        (
            "Mutable_vs _immutable .pdf",
            "p2–p8",
            "可变/不可变类型、<code>B = A</code> 别名、字符串不可变、列表参数被函数改到",
        ),
        ("L6E3.py", "全文", "三种遍历写法对照"),
        ("L6E4.py", "全文", "<code>split</code> + <code>append</code> 构造整数列表"),
        ("L6E5.py", "全文", "矩阵下标与双重循环"),
        ("tuple.py", "全文", "用元组返回面积与周长"),
    )
    + p(
        "<b>跳过项：</b>Part 5 p4 的方法列表页以表格截图呈现的部分已按正文表格重建；Moodle 的作业说明与评分页属于行政信息，不进入本讲。"
    )
    + p(
        "<b>拓展项：</b><code>enumerate</code>、列表推导、<code>copy.deepcopy</code> 的预告、浅拷贝的嵌套陷阱，都是在原知识点边界上的补充；深拷贝的完整讨论放在第 12 讲。"
    )
)

LEC.append(
    L(
        slug="ch08-lists-tuples",
        tzh="⑧ 列表、矩阵与元组",
        ten="Lists, Matrices and Tuples",
        keywords=[
            "list",
            "index",
            "slice",
            "mutable",
            "append",
            "sort",
            "nested list",
            "matrix",
            "alias",
            "shallow copy",
            "tuple",
            "unpacking",
        ],
        files=[
            "Chapter 6 - Part 4 - List.pdf",
            "Chapter 6 - Part 5 - List Builtins and Methods.pdf",
            "Chapter 6 - Part 6 - Matrix.pdf",
            "tuples.pdf",
            "Mutable_vs _immutable .pdf",
            "12_Chapter 6_1_Chapter 6 Code Examples_L6E5.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "前面的变量一次只能装一个值。这一讲引入容器：列表装一串会变的数据，矩阵装二维表格，元组装一组不该变的值。它们几乎出现在后面每一讲——文件读进来是列表，CSV 是列表的列表，字典的值常常是列表。"
            )
            + p(
                "上一讲的对象与这一讲的列表关系密切：列表本身就是对象，<code>append</code>、<code>sort</code> 都是它的方法。下一讲把这些数据落到文件里，让程序关掉之后数据还在。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "创建列表、用正负下标与切片取元素，并解释切片为什么不改原列表",
                "用三种方式遍历列表，按需要选择取元素还是取下标",
                "正确使用 <code>append</code> / <code>pop</code> / <code>remove</code> / <code>sort</code>，并说出它们的返回值",
                "区分 <code>L.sort()</code> 与 <code>sorted(L)</code>、<code>B = A</code> 与 <code>A[:]</code>",
                "用双重下标读写矩阵，写出遍历与转置",
                "创建元组、用解包一次拿到多个值，并说明元组与列表的取舍",
            )
        ),
        detail=_D8,
        kws=_K8,
        examples=_EX8,
        practice=_PR8,
        exam=_EXAM8,
        checklist=_CK8,
        mapping=_MP8,
    )
)

# ============================================================ 9 文件与 CSV
_D9 = (
    h2("一、为什么需要文件")
    + p(
        "到现在为止，程序里的数据都活在内存里：程序一结束，变量、列表全部消失（Files p2）。要让数据「关机之后还在」，就得写进文件。文件（file）是存放在硬盘（HDD）或固态盘（SSD）上的一串数据。"
    )
    + p("课件把文件分成两大类（Files p3–p5）：")
    + tb(
        ("类别", "内容形式", "常见扩展名", "能否直接用文本编辑器改"),
        (
            "文本文件 text file",
            "字符（ASCII / Unicode）",
            ".txt .csv .html .xml .py",
            "能",
        ),
        (
            "二进制文件 binary file",
            "原始字节",
            ".bin .exe .jpg .png .dat",
            "不能，需要专门软件",
        ),
    )
    + p(
        "这门课<b>只处理文本文件</b>。判断依据很简单：能用记事本打开、能看懂，就是文本文件。文本文件按<b>行</b>组织，每行末尾有一个换行符 <code>\\n</code>——这一点决定了后面所有读写细节。"
    )
    + p(
        "课件的文件操作清单有五步（Files p6）：打开（读/写/追加）、读、写、追加、关闭。下面按这个顺序展开。"
    )
    + h2("二、open()：打开文件并拿到句柄")
    + p(
        "打开文件的函数是 <code>open(文件名, 模式)</code>，返回值叫文件对象（file object）或文件句柄（file handle）（Reading p2）。它本身不装内容，只是「通向那个文件的一条通道」。"
    )
    + pre(
        """file = open("Example.txt", "r")
print(type(file))"""
    )
    + pre("""<class '_io.TextIOWrapper'>""")
    + p("文件不存在时，读模式会直接报错：")
    + pre("""file = open("example.txt", "r")""")
    + pre("""FileNotFoundError: [Errno 2] No such file or directory: 'example.txt' """)
    + p(
        "注意文件名<b>大小写敏感</b>：<code>Example.txt</code> 与 <code>example.txt</code> 是两个不同的文件。Linux 与 macOS 上尤其明显，Windows 上虽然不区分，但代码里也不该靠这个巧合。"
    )
    + tb(
        ("模式", "含义", "文件不存在时", "文件已存在时"),
        ('<code>"r"</code>', "只读", "报 <code>FileNotFoundError</code>", "从头读"),
        ('<code>"w"</code>', "只写", "新建空文件", "<b>清空原有内容</b>"),
        ('<code>"a"</code>', "追加", "新建空文件", "保留内容，写在末尾"),
    )
    + cal(
        "warn",
        "w 模式会清空文件",
        '这是最贵的一课：用 <code>"w"</code> 打开一个已有文件，内容立刻被抹掉，哪怕你一行都没写。只想加内容就用 <code>"a"</code>；只想读就别写。',
    )
    + h2("三、读文件")
    + h3("3.1 readline()：一次一行")
    + p("假设 <code>Example.txt</code> 有四行（课件原文）：")
    + pre(
        """Hello, this is a sample text file.
It contains multiple lines of text.
Python can read this file.
This is the fourth line."""
    )
    + p(
        '<code>readline()</code> 每次读一行，返回字符串，<b>行尾的 <code>\\n</code> 保留在字符串里</b>；读到文件末尾后再调用，返回空字符串 <code>""</code>（Reading p4）。'
    )
    + pre(
        """file = open("Example.txt", "r")
line1 = file.readline()
print(repr(line1))
line2 = file.readline()
print(repr(line2))
file.close()"""
    )
    + pre(
        """'Hello, this is a sample text file.\\n'
'It contains multiple lines of text.\\n'"""
    )
    + p(
        "用 <code>repr()</code> 才能看见那个隐藏的 <code>\\n</code>。直接 <code>print(line1)</code> 会看到「多一个空行」，因为字符串自带一个换行、<code>print</code> 又补一个。"
    )
    + h3("3.2 用循环读到结尾")
    + pre(
        """file = open("Example.txt", "r")
while True:
    line = file.readline()
    if line == "":
        break
    print(line.strip())
file.close()"""
    )
    + pre(
        """Hello, this is a sample text file.
It contains multiple lines of text.
Python can read this file.
This is the fourth line."""
    )
    + p(
        '<code>line == ""</code> 是「读完了」的信号，不是空行——空行读出来是 <code>"\\n"</code>。这个区别在统计行数时非常关键。'
    )
    + h3("3.3 strip()：去掉行尾换行与空白")
    + p(
        "<code>strip()</code> 去掉字符串两端的空白字符，包括空格、制表符、换行符（Reading p6）。读文件时几乎总要配它："
    )
    + pre(
        """print(repr("  hello  \\n".strip()))
print(repr("hello\\n".strip()))"""
    )
    + pre(
        """'hello'
'hello'"""
    )
    + p(
        '要小心 <code>strip()</code> 会去掉<b>两端所有</b>空白：如果数据本身前后有意义的空格（比如对齐的表格），就改用 <code>rstrip("\\n")</code> 只去换行。'
    )
    + h3("3.4 readlines()：一次读成列表")
    + p(
        "<code>readlines()</code> 把整个文件读成一个列表，每个元素是一行，<b>仍然带着 <code>\\n</code></b>；最后一行如果文件本身没有换行符，就不带（Reading p8）。"
    )
    + pre(
        """file = open("Example.txt", "r")
lines = file.readlines()
file.close()
print(len(lines))
print(repr(lines[0]))
print(repr(lines[-1]))"""
    )
    + pre(
        """4
'Hello, this is a sample text file.\\n'
'This is the fourth line.'"""
    )
    + p(
        "拿到列表后就能用第 8 讲的所有手段：<code>len()</code> 求行数、切片取前几行、循环处理。这也是 CSV 处理的标准起点。"
    )
    + h3("3.5 read()：一次读完整个文件")
    + p(
        "课件最后提到「读取整个文件」（Reading p10）：<code>read()</code> 不带参数时返回一个包含全部内容的字符串。适合小配置文件；文件大时会把内存占满。"
    )
    + pre(
        """file = open("Example.txt", "r")
content = file.read()
file.close()
print(len(content))
print(content.count("\\n"))"""
    )
    + pre(
        """122
3"""
    )
    + p(
        "三个换行符对应四行——最后一行没有换行符。同一个文件也可以先 <code>readlines()</code> 再 <code>read()</code>，但第二次会得到空字符串，因为读写位置（文件指针）已经到末尾了。"
    )
    + h2("四、写文件")
    + p(
        '用 <code>"w"</code> 打开就是写模式（Writing p2）：文件不存在会新建，已存在会被清空。写用 <code>write()</code>（写一个字符串）或 <code>writelines()</code>（写一个字符串列表）。'
    )
    + pre(
        """file = open("output.txt", "w")
file.write("First line\\n")
file.write("Second line\\n")
file.close()"""
    )
    + p(
        "<code>write()</code> <b>不会自动加换行</b>，想让每行独立就必须自己写 <code>\\n</code>。忘记加的后果是所有内容挤成一行。"
    )
    + pre(
        """lines = ["Alice,30\\n", "Bob,25\\n"]
file = open("output2.txt", "w")
file.writelines(lines)
file.close()"""
    )
    + p(
        "<code>writelines()</code> 同样不会补换行（Writing p5 专门强调）：列表里每个字符串该带 <code>\\n</code> 就得带，否则会被首尾相连。它名字里的「lines」容易让人误以为会自动分行。"
    )
    + h2("五、追加：a 模式")
    + p(
        '追加（append）是在文件<b>末尾</b>加内容，不动原有数据（Appending p2）。模式写 <code>"a"</code>，文件不存在时自动新建。'
    )
    + pre(
        """file = open("log.txt", "a")
file.write("This is the text to append.\\n")
file.close()"""
    )
    + p(
        "连续运行三次，<code>log.txt</code> 里就有三行相同内容——这正是日志（log）的写法：程序每次运行追加一条，历史记录全部保留。"
    )
    + h2("六、CSV：用逗号分列的文本")
    + h3("6.1 结构")
    + p(
        "CSV（comma-separated values）是用逗号分隔字段的文本文件（CSV p2）。每一行是一条记录，每个逗号前是一个字段；第一行通常是表头（header），也可能没有。"
    )
    + pre(
        """name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago"""
    )
    + p(
        "它在 Excel 里打开就是一张表，但本质仍是纯文本——所以用同样的 <code>open</code> + <code>readlines</code> 就能处理。"
    )
    + h3("6.2 读 CSV：strip + split")
    + p(
        '课件的 read_csv.py 给出标准四步（CSV p6）：打开 → <code>readlines</code> → 关文件 → 逐行 <code>strip().split(",")</code> 装进列表。'
    )
    + pre(
        """file = open("people.csv", "r")
lines = file.readlines()
file.close()

data = []
for line in lines:
    row = line.strip().split(",")
    data.append(row)

print(data[0])
print(data[1])
print(len(data))"""
    )
    + pre(
        """['name', 'age', 'city']
['Alice', '30', 'New York']
8"""
    )
    + p(
        "顺序不能反：先 <code>strip()</code> 去掉行尾 <code>\\n</code>，再 <code>split(\",\")</code>；若先 split，最后一列会变成 <code>'New York\\n'</code>（带换行）。得到的 <code>data</code> 是「列表的列表」，即第 8 讲的矩阵：<code>data[i][0]</code> 是第 i 行的姓名，<code>data[i][1]</code> 是年龄（仍是字符串）。"
    )
    + pre(
        """for row in data[1:]:
    if int(row[1]) > 28:
        print(row[0], "is", row[1])"""
    )
    + pre(
        """Alice is 30
Charlie is 35"""
    )
    + p(
        '注意 <code>row[1]</code> 是字符串，比较大小或做算术前必须 <code>int()</code>，否则 <code>"9" &gt; "28"</code> 会为真。'
    )
    + h3("6.3 追加一行")
    + pre(
        """file = open("people.csv", "a")
row = "Peter,52,Helsinki\\n"
file.write(row)
file.close()"""
    )
    + p(
        "追加 CSV 就是把一整行拼成字符串写进去，末尾别忘 <code>\\n</code>。字段里若本身含逗号（如地址），这种「手工拼」的写法就会错位——那种情况要用第 12 讲的 <code>csv</code> 模块。"
    )
    + h3("6.4 删除一行（并说明示例中的隐患）")
    + p("课件的 delete_from_csv.py 先全部读进内存，改完再整体写回：")
    + pre(
        """file = open("people.csv", "r")
lines = file.readlines()
file.close()

data = [line.strip().split(",") for line in lines]

for line in data:
    if line[0] == "Eva":
        data.remove(line)

file = open("people.csv", "w")
for line in data:
    file.write(line[0] + "," + line[1] + "," + line[2] + "\\n")
file.close()"""
    )
    + p(
        "思路是对的：读模式不能删，只能用写模式把「改好的全部内容」重写一遍。但<b>边遍历边 <code>remove</code> 有隐患</b>：删除后后面的元素整体前移，循环变量还按旧位置前进，于是紧跟在被删元素后的那一条会被跳过。这里只有一条 Eva 所以结果正确；要删多条就得遍历副本或重建列表。"
    )
    + pre(
        """safe = []
for row in data:
    if row[0] != "Eva":
        safe.append(row)"""
    )
    + p("「筛选出要保留的，重建一个新列表」永远比「在列表里删」安全，值得养成习惯。")
    + h2("七、关闭文件与资源管理")
    + p(
        "每个 <code>open</code> 都必须配一个 <code>close()</code>（Files p6）。不关的后果：写入的内容可能还在缓冲区没落盘；文件被占用，别的程序改不了；程序开很多文件会耗尽句柄。"
    )
    + p(
        'CodeGrade 会直接检查这一点（CG Guide 第 4.1.2 节）：反馈里出现 <code>File not closed</code> 就是忘了 <code>close()</code>；出现 <code>Incorrect file mode</code> 则是模式写错（该 <code>"r"</code> 写了 <code>"w"</code>）。'
    )
    + cal(
        "tip",
        "拓展：with 语句",
        "Python 还有 <code>with open(...) as f:</code> 的写法，离开缩进块时自动关闭文件，即使中途抛异常也会关。课程示例统一用 <code>open</code> / <code>close</code>，考试按课程写法即可；但在自己的项目里 <code>with</code> 更安全。",
    )
    + h2("八、路径与编码")
    + p(
        '文件名可以写相对路径（<code>"people.csv"</code>，相对<b>当前工作目录</b>）或绝对路径（<code>"C:/data/people.csv"</code>）。IDLE 里运行时，当前目录通常是脚本所在目录；从别处运行时可能变，找不到文件的第一个排查点就是它。'
    )
    + p(
        'Windows 路径里的反斜杠是转义字符（第 3 讲）：<code>"C:\\temp\\a.txt"</code> 中的 <code>\\t</code> 会被当成制表符。三种写法都可行：<code>"C:/temp/a.txt"</code>（推荐）、<code>"C:\\\\temp\\\\a.txt"</code>、或原始字符串 <code>r"C:\\temp\\a.txt"</code>。'
    )
    + p(
        '中文内容要保证编码一致：<code>open(..., encoding="utf-8")</code> 是明确写法。Windows 默认编码不一定是 UTF-8，读写含中文的文件时若出现乱码，先检查这一点（属拓展内容，课程示例未涉及）。'
    )
    + h2("九、常见错误与调试")
    + cal(
        "warn",
        "用 w 打开想读的文件",
        "内容瞬间被清空。规律：<b>读用 r、写用 w、加内容用 a</b>；不确定时先 <code>r</code> 读一遍看内容。",
    )
    + cal(
        "warn",
        "忘记 close 或忘记 \\n",
        "不 close 可能丢数据、被 CodeGrade 判 <code>File not closed</code>；<code>writelines</code> 不补换行，忘记 <code>\\n</code> 会全挤成一行。",
    )
    + cal(
        "warn",
        "strip 与 split 顺序颠倒",
        '先 split 会让最后一列带 <code>\\n</code>，后续比较、转数字全部失败。固定写 <code>line.strip().split(",")</code>。',
    )
    + cal(
        "tip",
        "出问题先打印三件事",
        "打印 <code>len(lines)</code>、<code>repr(lines[0])</code>、<code>repr(data[0])</code>。绝大多数文件问题在这三个输出里就能看出来：行数不对、换行没去掉、切分错位。",
    )
)

_K9 = K(
    ("file", "文件", "A collection of data stored on disk."),
    ("text file", "文本文件", "Stores characters; readable in a text editor."),
    ("binary file", "二进制文件", "Stores raw bytes; needs special software."),
    (
        "file handle",
        "文件句柄",
        "The object returned by open(); a channel to the file.",
    ),
    ("mode", "打开模式", '"r" read, "w" write (truncates), "a" append.'),
    ("readline", "读一行", 'Returns one line including its \\n, or "" at EOF.'),
    ("readlines", "读成列表", "Returns a list of lines, each keeping its \\n."),
    ("strip", "去两端空白", "Removes spaces, tabs and newlines from both ends."),
    ("write", "写入", 'file.write("text") does not add a newline.'),
    ("writelines", "写多行", "Writes a list of strings; newlines must be included."),
    ("append", "追加", '"a" mode adds content at the end without erasing.'),
    ("CSV", "逗号分隔值", "Rows of comma-separated fields; opens as a table."),
    ("header", "表头", "The first row of a CSV file with column names."),
    ("FileNotFoundError", "文件不存在", "Raised when the path cannot be found."),
)

_EX9 = (
    qa(
        "例 1　读取 Example.txt，输出行数、最长的一行及其长度。",
        p(
            "用 <code>readlines()</code> 一次读入，再用第 8 讲的循环找最长行。比较长度前先 <code>strip()</code>，否则行尾的 <code>\\n</code> 会算进长度。"
        )
        + pre(
            """file = open("Example.txt", "r")
lines = file.readlines()
file.close()

print("lines:", len(lines))

longest = ""
for line in lines:
    clean = line.strip()
    if len(clean) > len(longest):
        longest = clean

print("longest:", longest)
print("length:", len(longest))"""
        )
        + p("输出：")
        + pre(
            """lines: 4
longest: It contains multiple lines of text.
length: 35"""
        )
        + p(
            "解释：<code>readlines()</code> 得到 4 个元素；<code>strip()</code> 让每行去掉换行再比较；<code>longest</code> 初值用空串，因为任何行都比它长（若求最短行就不能这么初始化）。"
        ),
    )
    + qa(
        "例 2　把一组学生成绩写成 CSV 文件，再读回来计算平均分。",
        p(
            '写的时候用 <code>w</code> 模式 + 手工拼行；读的时候用 <code>strip().split(",")</code>，数字列要 <code>float()</code>。'
        )
        + pre(
            """rows = [("Alice", 90), ("Bob", 75), ("Charlie", 60)]

file = open("scores.csv", "w")
file.write("name,score\\n")
for name, score in rows:
    file.write(name + "," + str(score) + "\\n")
file.close()

file = open("scores.csv", "r")
lines = file.readlines()
file.close()

total = 0
count = 0
for line in lines[1:]:
    parts = line.strip().split(",")
    total = total + float(parts[1])
    count = count + 1

print("average:", round(total / count, 1))"""
        )
        + p("输出：")
        + pre("""average: 75.0""")
        + p(
            "解释：写文件时先写表头，再逐行写「姓名,分数」；<code>str(score)</code> 把数字变字符串才能拼接。<code>lines[1:]</code> 跳过表头；<code>float(parts[1])</code> 把 <code>'90'</code> 变成数字。平均 (90+75+60)/3 = 75.0。"
        ),
    )
    + qa(
        "例 3　从 people.csv 中筛选出年龄大于 30 的人，输出姓名与城市。",
        p("先读到矩阵，再用两层下标取值；比较前把年龄转成整数。")
        + pre(
            """file = open("people.csv", "r")
lines = file.readlines()
file.close()

data = []
for line in lines[1:]:
    data.append(line.strip().split(","))

for row in data:
    if int(row[1]) > 30:
        print(row[0], "-", row[2])"""
        )
        + p("输出：")
        + pre(
            """Charlie - Chicago
Frank - Miami"""
        )
        + p(
            "解释：<code>lines[1:]</code> 去掉表头；<code>row[1]</code> 是年龄字符串，<code>int()</code> 之后才能比大小；<code>row[2]</code> 是城市，本身含空格（<code>New York</code>）也不受影响，因为分割只看逗号。"
        ),
    )
    + qa(
        "例 4　把每次运行的时间戳追加到 log.txt，并说明为什么不能用 w 模式。",
        p("追加模式保留历史；<code>w</code> 会把之前的日志全部清空。")
        + pre(
            """from datetime import datetime

stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file = open("log.txt", "a")
file.write(stamp + " program started\\n")
file.close()

file = open("log.txt", "r")
lines = file.readlines()
file.close()
print("log lines:", len(lines))
print(lines[-1].strip())"""
        )
        + p("第二次运行后输出（行数会随运行次数增加）：")
        + pre(
            """log lines: 2
2026-11-20 02:53:16 program started"""
        )
        + p(
            '解释：<code>strftime</code> 把当前时间格式化成字符串（第 10 讲详讲）；<code>"a"</code> 让每次运行都往末尾加一条；读回来用 <code>lines[-1]</code> 看最近一条。若把 <code>"a"</code> 改成 <code>"w"</code>，行数永远是 1。'
        ),
    )
)

_PR9 = ol(
    "写程序统计 Example.txt 中一共有多少个单词（以空格分隔）。",
    "把 1 到 5 的平方写成两列表头的 CSV 文件 <code>squares.csv</code>（数字,平方）。",
    "读入一个文本文件，输出去掉空行后的行数。",
    "把 people.csv 中所有人的年龄加一，写回一个新文件 <code>people_new.csv</code>（保留表头）。",
    '解释并修正：<code>f = open("a.txt", "w"); print(f.readline())</code>。',
) + det(
    "答案与思路",
    p(
        "<b>1.</b> 逐行 <code>strip().split()</code>（不带参数的 <code>split()</code> 按任意空白切），每行的 <code>len()</code> 累加。注意空行切出来是空列表，长度 0，不影响结果。"
    )
    + p(
        '<b>2.</b> <code>"w"</code> 打开，先写 <code>"number,square\\n"</code>，再循环 <code>range(1, 6)</code> 写 <code>str(i) + "," + str(i * i) + "\\n"</code>，最后 <code>close()</code>。检查方法：用记事本打开看是否有 6 行。'
    )
    + p(
        '<b>3.</b> 读所有行，<code>if line.strip() != "": count += 1</code>。关键是用 <code>strip()</code> 判断——只含 <code>\\n</code> 的行 <code>strip()</code> 后是空串，而 <code>line == ""</code> 只匹配文件末尾。'
    )
    + p(
        '<b>4.</b> 读 <code>people.csv</code> 得矩阵，表头原样写入新文件；数据行把 <code>row[1]</code> 转 <code>int</code> 加一，再拼回字符串写 <code>people_new.csv</code>。绝不能直接写回原文件——用 <code>"w"</code> 打开原文件会先把数据清空。'
    )
    + p(
        '<b>5.</b> 两个错误：<code>"w"</code> 模式不能读（应 <code>"r"</code>）；<code>readline()</code> 是文件对象的方法，用 <code>print(f.readline())</code> 可以，但打开后马上清空了文件。正确写法是 <code>"r"</code> 打开、读完、<code>close()</code>。'
    ),
)

_EXAM9 = (
    cal(
        "exam",
        "必考",
        '<code>r</code> / <code>w</code> / <code>a</code> 三种模式的区别；<code>readline</code> 与 <code>readlines</code> 的返回形式；行尾 <code>\\n</code> 与 <code>strip()</code>；CSV 的 <code>strip().split(",")</code>；必须 <code>close()</code>。',
    )
    + cal(
        "warn",
        "易错 1　w 模式清空文件",
        "想「读进来改一改再写回」，必须先把内容全读进内存、关掉文件，再用 <code>w</code> 重写。不能边读边写同一个文件。",
    )
    + cal(
        "warn",
        "易错 2　换行符处理",
        "<code>print(line)</code> 会多出空行（行自带 <code>\\n</code> 加 print 的换行）；<code>write()</code> 不会自动换行。读写两侧的 <code>\\n</code> 都要自己负责。",
    )
    + cal(
        "warn",
        "易错 3　相对路径 / 大小写",
        "<code>FileNotFoundError</code> 先查三件事：文件名拼写与大小写、当前工作目录、扩展名是否隐藏（Windows 默认隐藏扩展名，<code>a.txt.txt</code> 很常见）。",
    )
    + cal(
        "tip",
        "进阶",
        "<code>with open(...) as f:</code> 自动关闭；<code>csv</code> 模块能正确处理字段内含逗号与引号的情况（第 12 讲 <code>DictReader</code>）；大文件应逐行 <code>readline</code> 处理而不是 <code>readlines</code> 全读进内存。",
    )
)

_CK9 = (
    h2("操作清单")
    + h3("读写文件之前")
    + st(
        "我要读、写还是追加？<code>r</code> / <code>w</code> / <code>a</code> 先定下来",
        "文件路径对不对？相对路径先确认当前工作目录",
        "读完要做什么：整行处理用 <code>readline</code> 循环，批量处理用 <code>readlines</code>",
        "写的时候每一行末尾有没有 <code>\\n</code>",
        "结束前一定调用 <code>close()</code>",
    )
    + h3("调试文件问题")
    + ck(
        "先 <code>print(len(lines))</code> 确认行数",
        "用 <code>repr(lines[0])</code> 看隐藏的 <code>\\n</code>",
        'CSV 一定是 <code>strip()</code> 在前、<code>split(",")</code> 在后',
        "数字列比较或运算前先 <code>int()</code> / <code>float()</code>",
        "写回同一文件前，确认没有还在读取它的句柄",
    )
)

_MP9 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Files.pdf",
            "p2–p6",
            "文件的定义与存储介质、文本/二进制文件的区别、常见扩展名、五步文件操作",
        ),
        (
            "Reading_from_file.pdf",
            "p2–p10",
            '<code>open(name, "r")</code> 与文件句柄、<code>FileNotFoundError</code>、<code>readline</code> 循环、<code>strip</code>、<code>readlines</code>、整文件读取',
        ),
        (
            "Writing_to_file.pdf",
            "p2–p5",
            '<code>"w"</code> 清空/新建、<code>write</code>、<code>writelines</code>、需自行补 <code>\\n</code>',
        ),
        (
            "Appending_.pdf",
            "p2",
            '<code>"a"</code> 模式追加、不存在则新建、追加后 close',
        ),
        (
            "CSV.pdf",
            "p2–p6",
            "CSV 定义、表头、Excel 互操作、<code>split</code> 分列、读/追加/删除三个示例",
        ),
        (
            "read_csv.py / append_csv.py / delete_from_csv.py",
            "全文",
            "CSV 读入矩阵、追加一行、删除一行后整体重写",
        ),
        ("people.csv / Example.txt", "全文", "本讲所有示例使用的数据文件内容"),
    )
    + p(
        "<b>跳过项：</b>Files.pdf 的存储设备示意图、CSV 在 Excel 中的截图只有图片信息；Moodle 第 7 章的文件作业说明与截止页属于行政信息，不进入本讲。"
    )
    + p(
        '<b>拓展项：</b><code>with</code> 语句、<code>encoding="utf-8"</code>、<code>csv</code> 模块、逐行处理大文件，都是围绕原知识点的工程化补充；考试仍按 <code>open</code> / <code>close</code> 写法。'
    )
)

LEC.append(
    L(
        slug="ch09-files-csv",
        tzh="⑨ 文件读写与 CSV",
        ten="Files, Text I/O and CSV",
        keywords=[
            "file",
            "text file",
            "binary file",
            "file handle",
            "mode",
            "readline",
            "readlines",
            "strip",
            "write",
            "append",
            "CSV",
            "header",
        ],
        files=[
            "Files.pdf",
            "Reading_from_file.pdf",
            "Writing_to_file.pdf",
            "Appending_.pdf",
            "CSV.pdf",
            "13_Chapter 7_1_Chapter 7 Code Examples_read_csv.py",
            "13_Chapter 7_1_Chapter 7 Code Examples_delete_from_csv.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "前面所有程序的数据都只活到程序结束。这一讲让数据活下来：把结果写进文件，下次运行时再读回来。文件也是「批量数据」的入口——项目作业里的车辆、客户、交易，全都存在文本文件里。"
            )
            + p(
                "技术上它把三件事合在一起：字符串处理（第 3 讲的 <code>strip</code> / <code>split</code>）、容器（第 8 讲的列表与矩阵）、循环（第 5 讲的逐行处理）。可以说这一讲是前面内容的第一次综合应用。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "说出文本文件与二进制文件的区别，并判断本课处理哪一类",
                "用 <code>open</code> 的三种模式打开文件，解释 <code>w</code> 为什么会清空内容",
                "用 <code>readline</code> 循环与 <code>readlines</code> 两种方式读文件，并处理行尾换行",
                "用 <code>write</code> / <code>writelines</code> 写文件，自行补 <code>\\n</code>",
                "把 CSV 读成「列表的列表」，做筛选、追加与整体重写",
                "每个 <code>open</code> 都配上 <code>close</code>，并知道不关的后果",
            )
        ),
        detail=_D9,
        kws=_K9,
        examples=_EX9,
        practice=_PR9,
        exam=_EXAM9,
        checklist=_CK9,
        mapping=_MP9,
    )
)

# ============================================================ 10 模块
_D10 = (
    h2("一、模块是什么")
    + p(
        "模块（module）就是一个 <code>.py</code> 文件，里面装着函数、类和常量，供别的程序导入使用（Chapter 8 Part 1 p3）。你写的每个 Python 文件其实都是模块——第 12 讲会讲到「自己的模块」。"
    )
    + p(
        "好处只有一个但很大：<b>不用重复造轮子</b>。<code>math</code> 里的开方、<code>datetime</code> 里的日期运算，都是别人写好、测试过的代码（Part 1 p4）。这也是开源生态的基础。"
    )
    + p(
        "Python 标准库（standard library）自带两百多个模块，装好 Python 就能用，例如 <code>math</code>、<code>random</code>、<code>datetime</code>、<code>time</code>、<code>csv</code>、<code>json</code>。此外还有海量的第三方模块，质量参差——课件提醒：有些非常好用，有些根本跑不起来，还有些会偷数据，用之前要看清来源。"
    )
    + pre(
        '''import math

radius = 5
circumference = 2 * math.pi * radius
print(round(circumference, 2))'''
    )
    + pre('''31.42''')
    + h2("二、三种导入写法")
    + p("课件的 L8E1 把三种写法放在一起（Part 1 p6–p8）：")
    + pre(
        '''import math
from math import pi
import math as m

print(math.pi)
print(pi)
print(m.pi)'''
    )
    + pre(
        '''3.141592653589793
3.141592653589793
3.141592653589793'''
    )
    + tb(
        ("写法", "用法", "优点", "风险"),
        ("<code>import math</code>", "<code>math.sqrt(2)</code>", "来源清楚，不污染命名空间", "名字长一点"),
        ("<code>from math import pi</code>", "直接用 <code>pi</code>", "短", "名字可能与自己的变量冲突"),
        ("<code>import math as m</code>", "<code>m.sqrt(2)</code>", "短且来源仍在", "别名太随便会看不懂"),
    )
    + p(
        "别名有行业惯例：<code>numpy as np</code>、<code>datetime as dt</code>。课件提醒不要自己乱起名——别人读你的代码时，<code>np</code> 一眼就懂，<code>x</code> 就得猜。"
    )
    + p(
        "还有 <code>from math import *</code> 把所有名字倒进来，简单但危险：你不知道哪些名字被覆盖了。这门课只要求能读懂，不建议使用。"
    )
    + p("忘记模块里有什么时，用 <code>help()</code> 查（Part 1 p9）：")
    + pre(
        '''import math
help("math")'''
    )
    + p("它会打印模块说明与全部函数清单。IDLE 里也可以直接输 <code>dir(math)</code> 看名字列表（拓展）。")
    + h2("三、math：数学函数")
    + p("课件列的六个函数（Part 2 p2）覆盖了这门课会用到的全部数学需求：")
    + tb(
        ("函数", "作用", "例子", "结果"),
        ("<code>math.ceil(x)</code>", "向上取整", "<code>math.ceil(5.1)</code>", "<code>6</code>"),
        ("<code>math.floor(x)</code>", "向下取整", "<code>math.floor(5.9)</code>", "<code>5</code>"),
        ("<code>math.factorial(x)</code>", "阶乘", "<code>math.factorial(5)</code>", "<code>120</code>"),
        ("<code>math.exp(x)</code>", "e 的 x 次方", "<code>math.exp(1)</code>", "<code>2.718...</code>"),
        ("<code>math.log(x, base)</code>", "对数", "<code>math.log(8, 2)</code>", "<code>3.0</code>"),
        ("<code>math.sqrt(x)</code>", "平方根", "<code>math.sqrt(144)</code>", "<code>12.0</code>"),
    )
    + pre(
        '''import math

print(math.ceil(5.1), math.floor(5.9))
print(math.factorial(5))
print(math.log(8, 2), math.sqrt(144))
print(round(math.pi, 4))'''
    )
    + pre(
        '''6 5
120
3.0 12.0
3.1416'''
    )
    + p(
        "注意 <code>ceil</code> / <code>floor</code> 与第 3 讲的 <code>int()</code> 不同：<code>int(-5.9)</code> 向零截断得 −5，<code>math.floor(-5.9)</code> 向下取整得 −6。负数时差别很明显。"
    )
    + p(
        "<code>math.log(x)</code> 不带第二个参数时是自然对数（以 e 为底），<code>math.log(100, 10)</code> 才是常用对数。开方也可以用 <code>x ** 0.5</code>（第 6 讲的海伦公式就是这么写的），两者结果相同。"
    )
    + h2("四、random：随机")
    + p("四个常用函数（Part 3 p2）：")
    + tb(
        ("函数", "作用", "取值范围"),
        ("<code>random.randrange(stop)</code>", "0 到 stop−1 的随机整数", "不含 stop"),
        ("<code>random.randrange(start, stop, step)</code>", "等差序列中随机取一个", "不含 stop"),
        ("<code>random.randint(a, b)</code>", "a 到 b 的随机整数", "<b>含两端</b>"),
        ("<code>random.choice(seq)</code>", "从序列里随机取一个元素", "字符串、列表都行"),
        ("<code>random.seed(n)</code>", "设定随机种子", "让结果可复现"),
    )
    + pre(
        '''import random

print(random.randrange(0, 11, 2))
print(random.randint(1, 6))
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))'''
    )
    + p("每次运行结果不同。想复现同一串随机数（调试、出题、测试）就固定种子：")
    + pre(
        '''import random

random.seed(42)
print([random.randint(1, 6) for _ in range(5)])'''
    )
    + pre('''[6, 1, 1, 6, 3]''')
    + p(
        "<code>randint(1, 6)</code> 与 <code>randrange(1, 7)</code> 等价，都给出 1–6；写 <code>randrange(1, 6)</code> 就永远掷不出 6——这是最常犯的随机数 off-by-one。"
    )
    + h2("五、datetime：日期与时间")
    + h3("5.1 date 与 timedelta")
    + p(
        "课件说「时间在编程里很难」，因为要处理时区、闰年、月末（Part 4 p1）。<code>datetime</code> 模块把这些复杂度收进类里，我们只用最简单的几个。"
    )
    + pre(
        '''from datetime import date, timedelta

today = date.today()
print(today)
yesterday = date(2023, 10, 29)
print(yesterday)
print(yesterday + timedelta(days=7))
print((date(2024, 1, 5) - date(2023, 12, 20)).days)'''
    )
    + pre(
        '''2026-11-20
2023-10-29
2023-11-05
16'''
    )
    + p(
        "<code>date</code> 表示年月日，<code>timedelta</code> 表示一段时长；两者相加得到新日期，两个日期相减得到天数。<b>不要自己写「加 30 天」的月份运算</b>——月末、闰年全都会错。"
    )
    + h3("5.2 datetime.now() 与两种格式化")
    + p(
        "带时分秒的时间用 <code>datetime</code> 类。<code>now()</code> 取当前时刻，<code>strftime()</code> 把时间对象变字符串，<code>strptime()</code> 把字符串变时间对象（Part 5 p2–p5）。名字只差一个字母，方向相反：<b>f = format（格式化输出），p = parse（解析输入）</b>。"
    )
    + pre(
        '''from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d.%m.%Y"))
print(now.strftime("%B"))

d = datetime.strptime("15:30 31.10.2023", "%H:%M %d.%m.%Y")
print(d)
print(d.strftime("%Y/%m/%d"))'''
    )
    + pre(
        '''2026-11-20 02:53:16
20.11.2026
November
2023-10-31 15:30:00
2023/10/31'''
    )
    + p(
        "第二个参数是格式字符串，必须与输入字符串<b>逐字符对应</b>：<code>\"%H:%M %d.%m.%Y\"</code> 里既有冒号、点号，也有空格，输入少一个空格就抛 <code>ValueError</code>。"
    )
    + p("课件给了一张完整的格式码表（Part 5 p6），常用的这些要记住：")
    + tb(
        ("格式码", "含义", "例子"),
        ("<code>%Y</code>", "四位年份", "<code>2026</code>"),
        ("<code>%m</code>", "两位月份", "<code>01</code>–<code>12</code>"),
        ("<code>%d</code>", "两位日期", "<code>01</code>–<code>31</code>"),
        ("<code>%H</code> / <code>%M</code> / <code>%S</code>", "24 小时制时 / 分 / 秒", "<code>15</code> / <code>30</code> / <code>00</code>"),
        ("<code>%I</code>", "12 小时制小时", "<code>01</code>–<code>12</code>"),
        ("<code>%p</code>", "AM / PM", "<code>PM</code>"),
        ("<code>%B</code> / <code>%b</code>", "月份全名 / 缩写", "<code>November</code> / <code>Nov</code>"),
        ("<code>%A</code> / <code>%a</code>", "星期全名 / 缩写", "<code>Wednesday</code> / <code>Wed</code>"),
        ("<code>%j</code>", "一年中的第几天", "<code>001</code>–<code>366</code>"),
        ("<code>%U</code> / <code>%W</code>", "周数（周日起 / 周一起）", "<code>00</code>–<code>53</code>"),
    )
    + cal(
        "warn",
        "%m 与 %M 不是一回事",
        "<code>%m</code> 是<b>月份</b>，<code>%M</code> 是<b>分钟</b>。大小写写反是日期题最常见的错误，输出会莫名其妙地错位。同理 <code>%H</code>（24 小时）与 <code>%I</code>（12 小时）、<code>%d</code>（日）与 <code>%D</code>（无此码）。",
    )
    + h3("5.3 日期运算的边界")
    + p(
        "课件 L8E5 里有这么一行：<code>datetime(today.year, today.month, today.day + 1, 9, 0, 0)</code>。它在大多数日子正确，但若今天是月末（如 11 月 30 日），<code>day + 1 = 31</code> 会抛 <code>ValueError: day is out of range for month</code>。正确做法是用 <code>timedelta</code>："
    )
    + pre(
        '''from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow.strftime("%Y-%m-%d"))
'''
    )
    + p("这类「用手算代替库函数」的写法，是日期题丢分的第二大原因。")
    + h2("六、time：秒、暂停与计时")
    + p("课件列的三个函数（Part 6 p2）各有明确用途：")
    + tb(
        ("函数", "返回", "用途"),
        ("<code>time.time()</code>", "自 1970-01-01 UTC 起的秒数（浮点）", "记录时间戳、算耗时"),
        ("<code>time.sleep(n)</code>", "无", "暂停 n 秒（可以是小数）"),
        ("<code>time.perf_counter()</code>", "高精度秒数", "测量短耗时，比 <code>time()</code> 准"),
    )
    + pre(
        '''import time

start = time.perf_counter()
total = 0
for i in range(1000000):
    total = total + i
end = time.perf_counter()
print("sum:", total)
print("elapsed:", round(end - start, 4), "s")'''
    )
    + pre(
        '''sum: 499999500000
elapsed: 0.0412 s'''
    )
    + p(
        "耗时数字随机器不同，重要的是方法：<b>开始前后各取一次，相减</b>。测短间隔要用 <code>perf_counter()</code>，<code>time()</code> 的分辨率可能只有几十毫秒，测不出来。"
    )
    + h2("七、包与 pip")
    + h3("7.1 模块与包")
    + p(
        "模块是一个 <code>.py</code> 文件；<b>包</b>（package）是一个目录，里面装着一个或多个模块（packages p3）。标准库模块随 Python 装好，第三方包要自己装。"
    )
    + p(
        "第三方包发布在 PyPI（Python Package Index）上，用 <code>pip</code> 安装（packages p4–p5）："
    )
    + pre(
        '''pip install numpy
pip uninstall numpy
pip install --upgrade numpy
pip --version'''
    )
    + p(
        "<code>pip</code> 是 Python 自带的包管理器（名字是「Pip Installs Packages」的递归缩写）。安装完就能 <code>import numpy</code>；如果 import 报 <code>ModuleNotFoundError</code>，通常是「装到了另一个 Python 环境」——终端里的 <code>pip</code> 与 IDLE 用的解释器不是同一个（拓展）。"
    )
    + h3("7.2 安装并验证 NumPy")
    + p(
        "本课用 NumPy 处理矩阵（installing_numpy p2）。安装后验证方式很朴素：在 IDLE 里 <code>import numpy</code>，没有报错就成功。"
    )
    + pre(
        '''import numpy as np
print(np.__version__)'''
    )
    + pre('''2.5.4''')
    + h2("八、NumPy 数组")
    + h3("8.1 为什么不用列表")
    + p(
        "NumPy 数组（array）为数值计算优化：数据存在连续内存块里，访问快、数学运算快，而且支持<b>整体运算</b>——不用写循环（using_numpy p2）。代价是数组创建后大小固定，且元素类型必须一致。"
    )
    + h3("8.2 创建数组")
    + pre(
        '''import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)
print(np.zeros((2, 2)))
print(np.ones((2, 2)))
print(np.eye(3))'''
    )
    + pre(
        '''[1 2 3 4 5]
[[1 2 3]
 [4 5 6]]
[[0. 0.]
 [0. 0.]]
[[1. 1.]
 [1. 1.]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]'''
    )
    + p(
        "注意打印格式：没有逗号，元素之间用空格。<code>zeros</code> / <code>ones</code> 默认是浮点，所以带小数点；<code>dtype=int</code> 可以指定整型（拓展）。<code>np.empty</code> 不初始化，里面是内存里的残留值，不要指望它是 0。"
    )
    + h3("8.3 三个属性")
    + pre(
        '''import numpy as np

m = np.zeros((2, 4))
print(m.shape)
print(m.size)
print(m.dtype)'''
    )
    + pre(
        '''(2, 4)
8
float64'''
    )
    + p(
        "<code>shape</code> 是「行数, 列数」的元组；<code>size</code> 是元素总数（行×列）；<code>dtype</code> 是元素类型。三者常被拿来检查数组是不是建对了。"
    )
    + h3("8.4 索引与切片")
    + p(
        "NumPy 用<b>一个方括号里的逗号</b>同时给行列下标，这与普通列表的 <code>M[1][2]</code> 不同："
    )
    + pre(
        '''import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m[1, 2])
print(m[0, :])
print(m[:, 1])'''
    )
    + pre(
        '''6
[1 2 3]
[2 5]'''
    )
    + p(
        "<code>m[0, :]</code> 是第 0 行全部列，<code>m[:, 1]</code> 是所有行的第 1 列。<code>:</code> 表示「这一维全要」。若写成 <code>m[1][2]</code> 也能得到 6，但每多一层索引就会多产生一个中间数组，效率更低。"
    )
    + h3("8.5 矩阵运算")
    + p(
        "同样形状的数组可以直接相加，逐元素相加："
    )
    + pre(
        '''import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a + b)
print(a * b)'''
    )
    + pre(
        '''[[ 6  8]
 [10 12]]
[[ 5 12]
 [21 32]]'''
    )
    + p(
        "<code>+</code> 与 <code>*</code> 都是<b>逐元素</b>运算，<code>a * b</code> 不是矩阵乘法！矩阵乘法要用 <code>np.dot(a, b)</code> 或 <code>@</code> 运算符（using_numpy p9–p11），前提是「左矩阵的列数 = 右矩阵的行数」："
    )
    + pre(
        '''import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
print(a @ b)'''
    )
    + pre(
        '''[[19 22]
 [43 50]]
[[19 22]
 [43 50]]'''
    )
    + p(
        "手算验证第一个元素：1×5 + 2×7 = 19；第二行第一列：3×5 + 4×7 = 43。这个「行乘列再求和」的定义要能默写。"
    )
    + h3("8.6 逆矩阵")
    + p(
        "只有方阵才可能有逆矩阵，且行列式不为零。用 <code>np.linalg.inv()</code> 求逆（using_numpy p12–p14）："
    )
    + pre(
        '''import numpy as np

m = np.array([[2, 3], [1, 4]])
inv = np.linalg.inv(m)
print(inv)
print(m @ inv)'''
    )
    + pre(
        '''[[ 0.8 -0.6]
 [-0.2  0.4]]
[[ 1.00000000e+00 -1.11022302e-16]
 [ 0.00000000e+00  1.00000000e+00]]'''
    )
    + p(
        "乘积本该是单位矩阵，但出现了 <code>-1.11e-16</code> 这样的「近乎 0」。这是浮点误差，不是错误：计算机算 <code>0.8 * 3 + (-0.6) * 4</code> 时无法精确表示 0。判断「是否为单位矩阵」要允许误差，写 <code>np.allclose(m @ inv, np.eye(2))</code>（拓展）。"
    )
    + h2("九、常见错误与调试")
    + cal(
        "warn",
        "忘记 import 或名字打错",
        "<code>NameError: name 'math' is not defined</code> 是没 import；<code>ModuleNotFoundError: No module named 'datetimes'</code> 是模块名拼错（正确是 <code>datetime</code>）。"
    )
    + cal(
        "warn",
        "from ... import 覆盖了自己的变量",
        "<code>from math import pi</code> 之后又写 <code>pi = 3</code>，模块里的值就被盖掉了。要么用 <code>import math</code> 加前缀，要么给自己的变量换名字。"
    )
    + cal(
        "warn",
        "strptime 格式不匹配",
        "<code>ValueError: time data '2024/10/27' does not match format '%Y-%m-%d'</code>：格式串必须与输入逐字符对应，分隔符也要一致。"
    )
    + cal(
        "warn",
        "randint 与 randrange 的边界",
        "<code>randint(1, 6)</code> 含 6，<code>randrange(1, 6)</code> 不含。掷骰子写错就永远没有 6。"
    )
    + cal(
        "tip",
        "先查 help 再猜",
        "<code>help(\"math\")</code>、<code>help(\"random\")</code> 会列出全部函数与说明。比在网上搜过时的教程快得多，也不会看错版本。"
    )
)

_K10 = K(
    ("module", "模块", "A .py file that defines functions, classes and constants."),
    ("standard library", "标准库", "Modules that come with the Python installation."),
    ("import", "导入", "import math makes math.sqrt available."),
    ("alias", "别名", "import numpy as np gives the module a short name."),
    ("package", "包", "A directory containing one or more modules."),
    ("pip", "包管理器", "pip install numpy fetches a package from PyPI."),
    ("PyPI", "Python 包索引", "The public repository of third-party packages."),
    ("ceil / floor", "向上 / 向下取整", "math.ceil(5.1) is 6, math.floor(5.9) is 5."),
    ("factorial", "阶乘", "math.factorial(5) is 120."),
    ("seed", "随机种子", "random.seed(42) makes the sequence reproducible."),
    ("timedelta", "时间间隔", "date.today() + timedelta(days=7)."),
    ("strftime", "格式化时间", "Turn a datetime into a string with %Y-%m-%d."),
    ("strptime", "解析时间", "Turn a string into a datetime using a format."),
    ("array", "数组", "A NumPy structure for fast numerical computing."),
    ("matrix multiplication", "矩阵乘法", "np.dot(a, b) or a @ b, not a * b."),
)

_EX10 = (
    qa(
        "例 1　用 math 计算：1000 元本金、年利率 5%、连续复利 3 年后的本息和（保留 2 位小数）。",
        p("连续复利公式是 <code>A = P × e^(rt)</code>，用 <code>math.exp</code> 算 e 的幂。")
        + pre(
            '''import math

principal = 1000
rate = 0.05
years = 3

amount = principal * math.exp(rate * years)
print("amount:", round(amount, 2))
print("interest:", round(amount - principal, 2))'''
        )
        + p("输出：")
        + pre(
            '''amount: 1161.83
interest: 161.83'''
        )
        + p(
            "解释：<code>rate * years = 0.15</code>，<code>e^0.15 ≈ 1.161834</code>，乘 1000 得 1161.83。若按单利算只有 1150——复利的差别就在这个 <code>exp</code> 上。也可以用 <code>math.e ** 0.15</code>，结果相同。"
        )
    )
    + qa(
        "例 2　模拟掷骰子 1000 次，统计每个点数出现的次数，并与理论值比较。",
        p("用 <code>random.randint(1, 6)</code>（含两端）；计数用第 8 讲的「列表 + 下标」或字典，这里先用列表。")
        + pre(
            '''import random

random.seed(7)
counts = [0, 0, 0, 0, 0, 0, 0]

for _ in range(1000):
    roll = random.randint(1, 6)
    counts[roll] = counts[roll] + 1

for face in range(1, 7):
    print("face", face, ":", counts[face], "times")'''
        )
        + p("输出（种子固定，结果可复现）：")
        + pre(
            '''face 1 : 155 times
face 2 : 172 times
face 3 : 178 times
face 4 : 162 times
face 5 : 175 times
face 6 : 158 times'''
        )
        + p(
            "解释：<code>counts</code> 开了 7 个格子（下标 0 空着不用），这样 <code>counts[roll]</code> 可以直接用点数当下标，比 <code>counts[roll - 1]</code> 少一处容易出错的减法。1000 次里每面约 167 次，实际值围绕它波动——这就是随机。"
        )
    )
    + qa(
        "例 3　计算两个日期相差多少天，并输出 30 天后的日期。",
        p("日期相减得 <code>timedelta</code>，取 <code>.days</code> 得整数；加 <code>timedelta</code> 得新日期。")
        + pre(
            '''from datetime import date, timedelta

start = date(2023, 12, 20)
end = date(2024, 1, 5)

diff = end - start
print("days between:", diff.days)

later = start + timedelta(days=30)
print("30 days later:", later)'''
        )
        + p("输出：")
        + pre(
            '''days between: 16
30 days later: 2024-01-19'''
        )
        + p(
            "解释：跨年不影响计算，<code>date</code> 内部处理了月份长度；<code>2023-12-20</code> 加 30 天跨过 12 月 31 天，落在 1 月 19 日。若手工写「月份加一、日子加 30」，就会算错。"
        )
    )
    + qa(
        "例 4　用 NumPy 做矩阵乘法与求逆，并验证逆矩阵乘原矩阵等于单位矩阵。",
        p("乘法用 <code>@</code>；验证用 <code>np.allclose</code>，避免浮点误差误判。")
        + pre(
            '''import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)

m = np.array([[2, 3], [1, 4]])
inv = np.linalg.inv(m)
print(np.round(inv, 2))
print(np.allclose(m @ inv, np.eye(2)))'''
        )
        + p("输出：")
        + pre(
            '''[[19 22]
 [43 50]]
[[ 0.8 -0.6]
 [-0.2  0.4]]
True'''
        )
        + p(
            "解释：<code>a @ b</code> 得 <code>[[19,22],[43,50]]</code>，与手算一致；<code>inv</code> 是 <code>[[0.8,-0.6],[-0.2,0.4]]</code>；<code>m @ inv</code> 名义上是单位矩阵，但含 <code>1e-16</code> 级误差，所以用 <code>allclose</code>（允许小误差）而不是 <code>==</code>。"
        )
)
)

_PR10 = (
    ol(
        "用 <code>math</code> 计算半径为 7 的圆面积与球体积（体积公式 4/3·π·r³），保留 2 位小数。",
        "用 <code>random</code> 生成 10 个 1–100 的随机整数，输出其中最大的一个。",
        "读入一个 <code>dd.mm.yyyy</code> 格式的日期字符串，输出它是星期几（提示：<code>strptime</code> + <code>strftime(\"%A\")</code>）。",
        "计算从今天起 100 天后的日期，输出 <code>YYYY-MM-DD</code>。",
        "用 NumPy 创建 3×3 的单位矩阵与全 5 矩阵，输出它们的和。",
    )
    + det(
        "答案与思路",
        p(
            "<b>1.</b> <code>math.pi * 7 ** 2</code> 与 <code>4 / 3 * math.pi * 7 ** 3</code>，各 <code>round(..., 2)</code>。注意 <code>4 / 3</code> 要先算，写 <code>4 / 3 * ...</code> 没问题，但 <code>4 / (3 * math.pi * ...)</code> 就完全错了。"
        )
        + p(
            "<b>2.</b> <code>random.randint(1, 100)</code> 循环 10 次，用「找极值」模式（初值取第一个数）或直接 <code>max()</code>。若要可复现，先 <code>random.seed(...)</code>。"
        )
        + p(
            "<b>3.</b> <code>datetime.strptime(s, \"%d.%m.%Y\")</code> 解析，再 <code>.strftime(\"%A\")</code> 得到英文星期名（<code>%a</code> 得缩写）。解析失败会抛 <code>ValueError</code>，真实程序应先用 try 包住（第 11 讲）。"
        )
        + p(
            "<b>4.</b> <code>(date.today() + timedelta(days=100)).strftime(\"%Y-%m-%d\")</code>。不要自己算月份。"
        )
        + p(
            "<b>5.</b> <code>np.eye(3) + np.full((3, 3), 5)</code> 得对角线为 6、其余为 5 的矩阵。注意 <code>np.ones((3,3)) * 5</code> 也行；<code>* 5</code> 是逐元素乘，正是想要的效果。"
        ),
    )
)

_EXAM10 = (
    cal(
        "exam",
        "必考",
        "三种 import 写法与点号访问；<code>math</code> 的 ceil/floor/sqrt/factorial；<code>random.randint</code> 与 <code>randrange</code> 的边界差别；<code>strftime</code> 与 <code>strptime</code> 的方向；<code>timedelta</code> 做日期加减；NumPy 的 <code>shape</code> 与矩阵乘法。",
    )
    + cal(
        "warn",
        "易错 1　%m 与 %M 混淆",
        "<code>%m</code> 月份、<code>%M</code> 分钟；<code>%H</code> 24 小时、<code>%I</code> 12 小时。写反了程序不报错，只是结果离谱。",
    )
    + cal(
        "warn",
        "易错 2　randint 含两端、randrange 不含",
        "掷骰子写 <code>randrange(1, 6)</code> 永远没有 6；写 <code>randint(1, 6)</code> 才对。日期加减用手算而不是 <code>timedelta</code> 同样会踩月末。",
    )
    + cal(
        "warn",
        "易错 3　a * b 不是矩阵乘法",
        "NumPy 里 <code>*</code> 是逐元素乘，矩阵乘法用 <code>@</code> 或 <code>np.dot</code>；形状不匹配（左列数 ≠ 右行数）会抛 <code>ValueError</code>。",
    )
    + cal(
        "tip",
        "进阶",
        "浮点结果比较用 <code>np.allclose</code> 或 <code>round</code>；<code>time.perf_counter</code> 测短耗时；第三方包装错环境时 <code>ModuleNotFoundError</code> 其实是解释器不匹配。"
    )
)

_CK10 = (
    h2("操作清单")
    + h3("用模块之前")
    + st(
        "确定要用的模块名（math / random / datetime / time / numpy）",
        "选一种 import 写法：<code>import x</code> 优先，名字太长再起别名",
        "查一下函数签名：<code>help(\"模块名\")</code>",
        "确认返回类型：int 还是 float、字符串还是对象",
        "涉及日期就一律用 <code>timedelta</code>，不手算月份",
    )
    + h3("调试时的检查")
    + ck(
        "<code>NameError</code> 先看是否漏了 import",
        "<code>ModuleNotFoundError</code> 先看模块名拼写与是否安装",
        "<code>ValueError</code>（日期）先对齐格式串与输入串",
        "随机结果每次不同是正常的，要复现就 <code>seed</code>",
        "NumPy 数组用 <code>shape</code> 与 <code>dtype</code> 确认建对了",
    )
)

_MP10 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Chapter 8 - Part 1 - Introduction to modules.pdf",
            "p3–p9",
            "模块定义、标准库与第三方、三种 import 写法、别名惯例、<code>help()</code>",
        ),
        ("Chapter 8 - Part 2 - Math.pdf", "p2", "<code>ceil/floor/factorial/exp/log/sqrt</code>"),
        ("Chapter 8 - Part 3 - Random.pdf", "p2", "<code>randrange/randint/choice/seed</code>"),
        (
            "Chapter 8 - Part 4 - Dates.pdf",
            "p2–p4",
            "日期处理的难点、<code>date</code> 类、<code>date.today()</code>、<code>timedelta</code> 运算",
        ),
        (
            "Chapter 8 - Part 5 - Formating datetime.pdf",
            "p2–p6",
            "<code>strptime</code> 解析、格式码表、<code>strftime</code> 格式化、<code>%B</code> 示例",
        ),
        ("Chapter 8 - Part 6 - Time.pdf", "p2", "<code>time.time</code>、<code>sleep</code>、<code>perf_counter</code>"),
        ("packages.pdf", "p2–p5", "模块与包的区别、PyPI、pip 安装/卸载/升级"),
        ("installing_numpy.pdf", "p2–p5", "NumPy 定位、用 pip 安装、import 验证"),
        (
            "using_numpy.pdf",
            "p2–p14",
            "数组特性、创建方式、<code>dtype/shape/size</code>、索引切片、加法、<code>dot</code>/<code>@</code>、<code>linalg.inv</code>",
        ),
        ("L8E1.py–L8E7.py", "全文", "三种 import、math/random/datetime/strftime/strptime/time 的可运行示例"),
    )
    + p(
        "<b>跳过项：</b>Part 4–5 开头的「时间是什么」哲思页、pip 安装截图、NumPy 安装截图只作背景；Moodle 第 8 章的作业与截止页属于行政信息，不进入本讲。"
    )
    + p(
        "<b>拓展项：</b><code>dir()</code>、<code>np.allclose</code>、<code>np.full</code>、pip 与解释器不匹配的问题，都是围绕原知识点的实用补充，考试按课件函数清单即可。"
    )
)

LEC.append(
    L(
        slug="ch10-modules",
        tzh="⑩ 模块、标准库与包",
        ten="Modules, Standard Library and Packages",
        keywords=[
            "module",
            "standard library",
            "import",
            "alias",
            "package",
            "pip",
            "PyPI",
            "ceil",
            "seed",
            "timedelta",
            "strftime",
            "strptime",
            "array",
            "matrix multiplication",
        ],
        files=[
            "Chapter 8 - Part 1 - Introduction to modules.pdf",
            "Chapter 8 - Part 2 - Math.pdf",
            "Chapter 8 - Part 3 - Random.pdf",
            "Chapter 8 - Part 4 - Dates.pdf",
            "Chapter 8 - Part 5 - Formating datetime.pdf",
            "Chapter 8 - Part 6 - Time.pdf",
            "packages.pdf",
            "installing_numpy.pdf",
            "using_numpy.pdf",
            "14_Chapter 8_1_Chapter 8 Code Examples_L8E6.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "到第 9 讲为止，所有功能都是自己写的。这一讲开始「站在别人肩膀上」：用标准库里的 <code>math</code>、<code>random</code>、<code>datetime</code>、<code>time</code>，再装一个第三方的 NumPy 处理矩阵。项目作业里读日期、算价格、随机分配，全靠这些模块。"
            )
            + p(
                "它也是第 6 讲「函数库」想法的落地：你写的函数可以给别人用，别人写的模块也可以给你用。第 12 讲会把这个想法倒过来——把自己的函数写成模块。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "说出模块与包的区别，并解释为什么不该重复实现已有功能",
                "用 <code>import</code> / <code>from ... import</code> / <code>as</code> 三种写法导入并正确访问",
                "用 <code>math</code> 做取整、阶乘、对数、开方，并说出与 <code>int()</code> 截断的区别",
                "用 <code>random</code> 生成指定范围的随机数，并用 <code>seed</code> 复现",
                "用 <code>date</code> + <code>timedelta</code> 做日期加减，用 <code>strftime</code> / <code>strptime</code> 双向转换",
                "创建 NumPy 数组、查 <code>shape</code>，用 <code>@</code> 做矩阵乘法并用 <code>inv</code> 求逆",
            )
        ),
        detail=_D10,
        kws=_K10,
        examples=_EX10,
        practice=_PR10,
        exam=_EXAM10,
        checklist=_CK10,
        mapping=_MP10,
    )
)

# ============================================================ 11 错误与异常
_D11 = (
    h2("一、错误是编程的一部分")
    + p(
        "课件开门见山：错误（bug）不可避免，识别与修复它是程序员的核心技能（Errors p2）。错误大致分三类，处理方式完全不同："
    )
    + tb(
        ("类型", "发生时机", "典型例子", "能否被 try 捕获"),
        (
            "语法错误 syntax error",
            "写代码时/运行前",
            "漏冒号、缩进错、括号不配对、<code>10 = x</code>、把关键字当变量名",
            "不能——程序根本没跑起来",
        ),
        (
            "运行时错误 runtime error",
            "执行到那一行时",
            "除零、类型不匹配、变量未定义、下标越界",
            "能——这是 try/except 处理的对象",
        ),
        (
            "逻辑错误 logical error",
            "程序跑完、结果不对",
            "条件写反、循环少一次、初值错、用错运算符",
            "不能——不报错，只能靠测试发现",
        ),
    )
    + p(
        "这三类的排查顺序不同：语法错误看报错行号；运行时错误看异常类型与调用栈；逻辑错误没有报错，只能靠「输入 → 期望输出 → 实际输出」的对照。"
    )
    + h2("二、语法错误：解释器根本读不懂")
    + p("课件列的五个典型（Errors p3）几乎覆盖了所有语法错误：")
    + pre(
        '''if x > 5          # 漏冒号
    print("big")

if 5 > 2:
print("no indent")    # 缩进错

print("a"             # 括号不配对

10 = x                 # 赋值目标不能是字面量

def = "house"          # 关键字不能当变量名'''
    )
    + p(
        "它们都在程序运行之前就被 Python 拦下，报错信息里带文件、行号与一个 <code>^</code> 指向大致位置。注意行号常常「晚一行」——解释器要到下一行才发现上一行没收尾，所以真正的错误往往在报错行的<b>上一行</b>。"
    )
    + pre(
        '''  File "demo.py", line 3
    print("a"
         ^
SyntaxError: '(' was never closed'''
    )
    + h2("三、运行时错误：能跑，但跑到某行就崩")
    + p("课件列了四种最常见（Errors p5）：除零 <code>10 / 0</code>、类型错误 <code>\"hello\" + 5</code>、变量未定义、下标越界。下面这张表把异常名与触发条件对齐（Run-time_errors p2–p10）：")
    + tb(
        ("异常", "触发条件", "最小例子"),
        ("<code>TypeError</code>", "对不合适的类型做运算", "<code>\"hello\" + 5</code>"),
        ("<code>NameError</code>", "名字（变量/函数）不存在", "<code>print(total)</code>（从未赋值）"),
        ("<code>IndexError</code>", "下标越界", "<code>[1, 2][5]</code>"),
        ("<code>AttributeError</code>", "对象没有这个属性/方法", "<code>\"abc\".push(\"d\")</code>"),
        ("<code>ValueError</code>", "类型对但值不合适", "<code>int(\"abc\")</code>"),
        ("<code>ZeroDivisionError</code>", "除零或对零取模", "<code>10 / 0</code>"),
        ("<code>FileNotFoundError</code>", "文件/目录不存在", "<code>open(\"nope.txt\")</code>"),
        ("<code>ImportError</code>", "模块找不到或名字不在模块里", "<code>import datetimes</code>"),
    )
    + p(
        "记住两个容易混的：<b><code>ValueError</code> 是「类型对了、值不对」</b>（<code>int(\"abc\")</code> 的输入确实是字符串），<b><code>TypeError</code> 是「类型就不对」</b>（<code>int([1,2])</code>）。"
    )
    + h2("四、读懂 traceback")
    + p(
        "报错时 Python 打印的整段叫调用栈回溯（traceback）。读法只有一条：<b>先看最后一行</b>（异常类型 + 消息），<b>再往上找自己写的文件与行号</b>。"
    )
    + pre(
        '''def divide(x, y):
    return x / y

print(divide(7, 0))'''
    )
    + pre(
        '''Traceback (most recent call last):
  File "demo.py", line 4, in <module>
    print(divide(7, 0))
  File "demo.py", line 2, in divide
    return x / y
ZeroDivisionError: division by zero'''
    )
    + p(
        "课件逐行拆解过这段（Run-time_errors p10–p11）：<code>line 4, in &lt;module&gt;</code> 说明错误从主程序的第 4 行发起；<code>print(divide(7, 0))</code> 是那一行的代码；<code>line 2, in divide</code> 说明进入了 <code>divide</code> 函数；<code>return x / y</code> 是真正出事的位置；最后 <code>ZeroDivisionError: division by zero</code> 是类型与原因。"
    )
    + p(
        "「most recent call last」的意思是：越靠下越接近出错点。所以从下往上看调用链、从上往下读代码，是最快的定位方式。"
    )
    + h2("五、try / except：把错误接住")
    + p(
        "异常处理（exception handling）让程序在出错时不崩，而是转去执行另一段代码（Handling p2）。结构是 <code>try</code> 包住「可能出错的代码」，<code>except</code> 写「出错了怎么办」。"
    )
    + pre(
        '''try:
    number = int(input("Give an integer: "))
    print("You gave", number)
except ValueError:
    print("That was not an integer.")'''
    )
    + p(
        "输入 <code>abc</code> 时，<code>int()</code> 抛 <code>ValueError</code>，<code>try</code> 里剩下的语句被跳过，直接进 <code>except</code>，输出提示。输入 <code>42</code> 时正常走完 <code>try</code>，<code>except</code> 不执行。"
    )
    + p(
        "<b>try 的范围要小</b>：只包住可能出错的那一两行，不要把整个程序塞进去。范围一大，出错时你连是哪一行出的都难判断，还会掩盖本不该被捕获的错误。"
    )
    + h2("六、except Exception as e：拿到异常对象")
    + p(
        "出错时 Python 会创建一个异常对象，里面装着类型与消息（Handling p4）。用 <code>as e</code> 把它接住就能查看："
    )
    + pre(
        '''try:
    number = int(input("Give an integer: "))
    print("You gave", number)
except Exception as e:
    print(type(e))
    print(e)
    print("Please retry!")'''
    )
    + p("输入 <code>abc</code>，输出：")
    + pre(
        '''<class 'ValueError'>
invalid literal for int() with base 10: 'abc'
Please retry!'''
    )
    + p(
        "<code>type(e)</code> 给出异常类，<code>print(e)</code> 给出消息。<code>except Exception</code> 能捕获几乎所有运行时异常，代价是「太宽」——它把你的编程错误也一起吞掉了。初学阶段用它兜底可以，但要知道自己在放弃什么。"
    )
    + h2("七、多个 except：按类型分别处理")
    + p(
        "Example3 是课件给的完整形态（Handling p6）：一个循环里同时可能出现输入错误、除零、用户中断，三种情况给出三种提示。"
    )
    + pre(
        '''while True:
    try:
        x = int(input("Enter an integer: "))
        y = 10 / x
        print(y)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except ZeroDivisionError:
        print("Division by zero error. Give other number than zero.")
    except KeyboardInterrupt:
        print("User interrupted the program.")
        break'''
    )
    + p(
        "三个要点：<b>顺序</b>——具体的异常写前面，宽泛的（<code>Exception</code>）写后面，否则后面的永远轮不到；<b>只处理你懂的</b>——不知道怎么办就别捕获；<b><code>KeyboardInterrupt</code></b> 是用户按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 触发的，它不像其他异常那样打印完整 traceback。"
    )
    + h2("八、重试循环：让用户有机会改")
    + p(
        "输入校验的标准形态是「不合法就重来」，直到拿到合法值才 <code>break</code>（Example1、Example2）："
    )
    + pre(
        '''while True:
    try:
        nr = int(input("Enter an integer: "))
        break
    except ValueError:
        print("You did not give an integer, retry!")

print(f"The entered integer is {nr}")'''
    )
    + p(
        "输入 <code>abc</code> 会提示重试；输入 <code>7</code> 才跳出循环。<code>break</code> 必须写在 <code>try</code> 里、而且是「成功之后」——写在 <code>except</code> 里就变成「出错才退出」，正好反了。"
    )
    + h2("九、调试：不靠猜，靠证据")
    + p("课件列了四种手段（Errors p7），按成本从低到高：")
    + st(
        "插入 <code>print</code>：在关键位置打印变量值与「走到这里了」，最快看清执行流",
        "用调试器（debugger）：IDLE 的 Debug 菜单可以逐行执行、设断点、查看变量",
        "请别人看代码：换一双眼睛最容易发现「你以为自己写了、其实没写」的部分；也可以让 AI 解释报错",
        "写小测试（unit testing）：给函数准备几组「输入 → 期望输出」，改完就跑一遍",
    )
    + p(
        "CodeGrade 的反馈本质上就是第 4 种：它把你的函数用固定输入跑一遍，比较返回值（CG Guide 第 4.2 节）。看到 <code>Expected: 7 / Received: 3</code>，就说明逻辑错了；看到 <code>The function should return a value</code>，就是用了 print 没 return。"
    )
    + h2("十、一个 bug 的完整修复过程")
    + p(
        "把前面所有工具串起来，看一次真实的排查流程。假设程序要读入年龄并判断是否成年，代码如下："
    )
    + pre(
        '''age = input("Age: ")
if age >= 18:
    print("adult")
else:
    print("minor")'''
    )
    + p("输入 <code>20</code>，程序崩了，报：")
    + pre(
        '''Traceback (most recent call last):
  File "demo.py", line 2, in <module>
    if age >= 18:
TypeError: '>=' not supported between instances of 'str' and 'int'
'''
    )
    + st(
        "读最后一行：<code>TypeError</code>，「字符串与整数不能用 &gt;= 比较」",
        "往上找自己的行：第 2 行，<code>if age &gt;= 18</code>",
        "回到第 1 行看 <code>age</code> 从哪来：<code>input()</code> 返回字符串",
        "修：<code>age = int(input(\"Age: \"))</code>",
        "复测：输入 20 输出 adult，输入 17 输出 minor，输入 abc 观察新的报错",
    )
    + p(
        "第五步很重要：修完要测边界与异常输入。<code>abc</code> 会让 <code>int()</code> 抛 <code>ValueError</code>，这才是该加 <code>try/except</code> 的地方——而不是一开始就把整个程序包起来。"
    )
    + h2("十一、主动抛异常与收尾工作")
    + p(
        "两件课件没展开、但读别人代码会遇到的事（拓展，不作为考点）："
    )
    + pre(
        '''def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("Rejected:", e)

try:
    print("working")
finally:
    print("cleanup always runs")'''
    )
    + pre(
        '''Rejected: Age cannot be negative
working
cleanup always runs'''
    )
    + p(
        "<code>raise</code> 让你在「值不合理」时主动报错，比返回一个特殊值更明确；<code>finally</code> 里的代码无论成功还是异常都会执行，适合关文件、释放资源。第 9 讲的 <code>with</code> 本质上就是自动帮你做这件事。"
    )
    + h2("十二、处理异常的原则")
    + cal(
        "warn",
        "不要写裸 except",
        "<code>except:</code> 什么都不写会捕获包括 <kbd>Ctrl</kbd>+<kbd>C</kbd> 在内的一切，程序看起来「永不报错」，实际问题被藏起来。至少写 <code>except ValueError:</code>，或 <code>except Exception as e:</code> 并打印 e。",
    )
    + cal(
        "warn",
        "不要用异常代替正常判断",
        "能先判断就判断：<code>if y != 0: print(x / y)</code> 比「先除再看有没有异常」清楚得多。异常是给「预料之外的失败」用的，不是流程控制。",
    )
    + cal(
        "warn",
        "捕获后要给出路",
        "<code>except: pass</code> 等于把错误吞掉。至少打印提示、返回默认值、或让用户重试——否则程序「静默地错」比崩溃更难查。",
    )
    + cal(
        "tip",
        "先让程序崩，再决定捕获",
        "调试阶段先不加 try，让 traceback 完整打出来定位问题；确定这类错误在真实使用中会发生（如用户输入），再加 try 并给出友好提示。",
    )
)

_K11 = K(
    ("bug", "程序错误", "Any issue that prevents the code from working as intended."),
    ("syntax error", "语法错误", "The code breaks Python's grammar; caught before running."),
    ("runtime error", "运行时错误", "The program crashes while executing a statement."),
    ("logical error", "逻辑错误", "The program runs but produces the wrong result."),
    ("exception", "异常", "An object describing a runtime error."),
    ("traceback", "调用栈回溯", "The report showing the chain of calls that led to the error."),
    ("try / except", "异常处理结构", "try holds risky code; except handles the failure."),
    ("raise", "抛出异常", "raise ValueError(\"bad input\") creates an error on purpose."),
    ("ValueError", "值错误", "Right type, unsuitable value: int(\"abc\")."),
    ("TypeError", "类型错误", "Wrong type for the operation: \"a\" + 1."),
    ("ZeroDivisionError", "除零错误", "Raised by 10 / 0."),
    ("IndexError", "下标越界", "Raised by accessing a position that does not exist."),
    ("debugging", "调试", "Finding and fixing errors: print, debugger, tests."),
    ("unit test", "单元测试", "A small test that checks one function with known inputs."),
)

_EX11 = (
    qa(
        "例 1　读入一个整数，输入不合法时提示并重试，直到成功。",
        p("用 <code>while True</code> + <code>try</code> + <code>break</code>：成功才跳出，失败留在循环里。")
        + pre(
            '''while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Not an integer, try again.")

print("You entered", n)
print("Its square is", n * n)'''
        )
        + p("交互示例（<code>&gt;</code> 表示用户输入）：")
        + pre(
            '''Enter an integer: > abc
Not an integer, try again.
Enter an integer: > 2.5
Not an integer, try again.
Enter an integer: > 12
You entered 12
Its square is 144'''
        )
        + p(
            "解释：<code>int(\"abc\")</code> 与 <code>int(\"2.5\")</code> 都抛 <code>ValueError</code>（第二个是因为字符串本身带小数点，不是整数字面量），所以都被 <code>except</code> 接住。只有 <code>int(\"12\")</code> 成功，执行到 <code>break</code> 跳出。"
        )
    )
    + qa(
        "例 2　对两个输入做除法，分别处理「输入不是整数」与「除数为零」。",
        p("两个 <code>except</code> 按类型分开；顺序无关（两者互不包含），但具体类型写在前面是好习惯。")
        + pre(
            '''try:
    a = int(input("Dividend: "))
    b = int(input("Divisor: "))
    print("Result:", a / b)
except ValueError:
    print("Both inputs must be integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")'''
        )
        + p("三种输入的结果：")
        + pre(
            '''Dividend: 10   Divisor: 2   ->  Result: 5.0
Dividend: 10   Divisor: 0   ->  Cannot divide by zero.
Dividend: ten  Divisor: 2   ->  Both inputs must be integers.'''
        )
        + p(
            "解释：除数 0 时 <code>a / b</code> 抛 <code>ZeroDivisionError</code>，被第二个 <code>except</code> 接住；输入 <code>ten</code> 时 <code>int()</code> 先抛 <code>ValueError</code>，根本走不到除法。注意 try 里三行是一个整体：任何一行抛异常，后面都不执行。"
        )
    )
    + qa(
        "例 3　读取一个可能不存在的文件，文件缺失时给出提示而不是崩溃。",
        p("文件类操作最适合用异常处理：路径由用户给，缺失是常态。")
        + pre(
            '''filename = input("File name: ")
try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    print("lines:", len(lines))
except FileNotFoundError:
    print("No such file:", filename)'''
        )
        + p("两种输入的结果：")
        + pre(
            '''File name: > Example.txt
lines: 4
File name: > missing.txt
No such file: missing.txt'''
        )
        + p(
            "解释：<code>open</code> 找不到文件时抛 <code>FileNotFoundError</code>（消息里带 <code>Errno 2</code>），被捕获后只打印提示。<code>file.close()</code> 写在 <code>try</code> 里，只有打开成功才会执行——这也说明为什么 try 的范围要恰好包住相关操作。"
        )
    )
    + qa(
        "例 4　下面这段代码哪里错？为什么它永远输出不了「负数」？",
        p("题目代码：<code>n = int(input()); if n &gt; 0: print(\"正\"); elif n &gt; 10: print(\"很大\")</code>。")
        + pre(
            '''n = int(input("n: "))
if n > 0:
    print("positive")
elif n > 10:
    print("large")'''
        )
        + p(
            "这是<b>逻辑错误</b>，不是语法或运行时错误：<code>n &gt; 10</code> 为真时 <code>n &gt; 0</code> 一定也为真，所以第二个分支永远走不到。程序不报错，只是结果与意图不符。"
        )
        + p(
            "修正思路：把范围窄的条件放前面，或者用互斥区间写全。这类错误只能靠「拿边界值测一遍」发现：输入 0、1、10、11，看输出是否符合预期。"
        )
)
)

_PR11 = (
    ol(
        "下面哪些是语法错误、哪些是运行时错误？①<code>if x &gt; 1</code> 后漏冒号 ②<code>10 / 0</code> ③<code>int(\"abc\")</code> ④<code>print(\"a\"</code> ⑤<code>len(5)</code>",
        "写一个函数 <code>safe_int(s)</code>：能转成整数就返回整数，否则返回 <code>None</code>。",
        "读入两个数做除法，要求：除数为 0 时输出提示、重新输入；输入非数字时也重新输入。",
        "解释这段代码为什么会崩，并修正：<code>L = [1,2,3]; print(L[3])</code>。",
        "写一段代码，捕获 <code>IndexError</code> 并从列表中安全地取第 10 个元素（不存在时返回 <code>None</code>）。",
    )
    + det(
        "答案与思路",
        p(
            "<b>1.</b> ①④ 是语法错误（漏冒号、括号未闭合），程序根本跑不起来；②③⑤ 是运行时错误：<code>ZeroDivisionError</code>、<code>ValueError</code>、<code>TypeError</code>（<code>len</code> 不接受整数）。判断标准：能不能通过解释器的语法检查。"
        )
        + p(
            "<b>2.</b> <code>try: return int(s)</code> / <code>except ValueError: return None</code>。捕获范围要窄，只 catch <code>ValueError</code>；若 catch <code>Exception</code>，连 <code>TypeError</code>（比如传了列表）也会被吞掉，掩盖真正的问题。"
        )
        + p(
            "<b>3.</b> 两层校验可以放在同一个 <code>try</code> 里：先 <code>int(input())</code> 两次，再判断除数是否为 0；<code>except ValueError</code> 处理非数字，<code>if b == 0</code> 单独给提示。注意 <code>continue</code> 与循环结构：把「成功」放在最后并 <code>break</code>。"
        )
        + p(
            "<b>4.</b> 列表长度 3，合法下标 0–2，<code>L[3]</code> 抛 <code>IndexError: list index out of range</code>。修正：取 <code>L[-1]</code> 或判断 <code>if len(L) &gt; 3</code>；如果确实要「不存在就返回 None」，用 <code>try/except IndexError</code>。"
        )
        + p(
            "<b>5.</b> <code>try: return L[9]</code> / <code>except IndexError: return None</code>。更好的写法是先判断 <code>if len(L) &gt; 9</code>——异常处理适合「意料之外」，长度检查适合「可以预知」的情况。"
        ),
    )
)

_EXAM11 = (
    cal(
        "exam",
        "必考",
        "三类错误的区分；常见异常名与触发条件；traceback 的读法（最后一行是异常类型）；<code>try/except</code> 结构与 <code>as e</code>；重试循环的写法。",
    )
    + cal(
        "warn",
        "易错 1　except 顺序",
        "把 <code>except Exception</code> 写在最前面，后面所有具体异常都轮不到，提示永远是通用的那句。具体在前、宽泛在后。",
    )
    + cal(
        "warn",
        "易错 2　try 范围过大 / 裸 except",
        "把整个程序包进 try，出错时无法定位；<code>except: pass</code> 会把 <kbd>Ctrl</kbd>+<kbd>C</kbd> 都吞掉。范围要小、类型要具体。",
    )
    + cal(
        "warn",
        "易错 3　break 放错位置",
        "重试循环里 <code>break</code> 必须写在 <code>try</code> 成功路径的末尾；写进 <code>except</code> 就变成「一出错就退出」。",
    )
    + cal(
        "tip",
        "进阶",
        "<code>raise ValueError(\"message\")</code> 可以主动抛异常；<code>finally</code> 里的代码无论成功失败都会执行（适合关闭文件）；自定义异常类属于后续课程。",
    )
)

_CK11 = (
    h2("操作清单")
    + h3("看到报错时的处理顺序")
    + st(
        "先读<b>最后一行</b>：异常类型 + 消息",
        "再往上找<b>自己文件</b>的行号与函数名",
        "回到那一行，打印相关变量的值确认状态",
        "判断是三类中的哪一类：语法 / 运行时 / 逻辑",
        "修完用同样的输入再跑一次，并补一个边界输入")
    + h3("写异常处理时的检查")
    + ck(
        "<code>try</code> 只包住可能出错的那几行",
        "<code>except</code> 写具体类型，必要时才用 <code>Exception</code>",
        "捕获后给出了提示或替代结果，没有 <code>pass</code>",
        "重试循环里 <code>break</code> 在成功路径上",
        "调试阶段先不加 try，让 traceback 完整显示",
    )
)

_MP11 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Errors.pdf",
            "p2–p7",
            "错误不可避免、语法/运行时/逻辑三类、各自例子、四种调试手段",
        ),
        (
            "Run-time_errors.pdf",
            "p2–p11",
            "TypeError、NameError、IndexError、AttributeError、ValueError、ZeroDivisionError、FileNotFoundError、ImportError、traceback 逐行解读",
        ),
        (
            "Handling_exceptions.pdf",
            "p2–p6",
            "exception handling 概念、<code>try/except</code>、<code>as e</code> 取异常对象、多 <code>except</code>、KeyboardInterrupt",
        ),
        ("15_Chapter 9_1_Chapter 9 Code Examples_Example1.py", "全文", "裸 except 重试读整数"),
        ("Example2.py", "全文", "<code>except Exception as e</code> + <code>type(e)</code> + <code>print(e)</code>"),
        ("Example3.py", "全文", "多 <code>except</code> 分别处理 ValueError / ZeroDivisionError / KeyboardInterrupt"),
        ("CG Guide 2026.pdf", "第 3–4 节", "AutoTest 如何报告 expected/actual 与 «should return a value»，作为调试的外部反馈"),
    )
    + p(
        "<b>跳过项：</b>Errors.pdf 与 Run-time_errors.pdf 的报错截图页只有图片，正文已用可复制的 traceback 重建；Moodle 的作业与评分页属于行政信息，不进入本讲。"
    )
    + p(
        "<b>拓展项：</b><code>raise</code>、<code>finally</code>、<code>KeyError</code> 的提及、以及「先用判断代替异常」的原则，都是围绕原知识点的补充；本课只要求 <code>try</code> / <code>except</code>。"
    )
)

LEC.append(
    L(
        slug="ch11-errors",
        tzh="⑪ 错误、异常与调试",
        ten="Errors, Exceptions and Debugging",
        keywords=[
            "bug",
            "syntax error",
            "runtime error",
            "logical error",
            "exception",
            "traceback",
            "try",
            "except",
            "ValueError",
            "ZeroDivisionError",
            "debugging",
            "unit test",
        ],
        files=[
            "Errors.pdf",
            "Run-time_errors.pdf",
            "Handling_exceptions.pdf",
            "15_Chapter 9_1_Chapter 9 Code Examples_Example1.py",
            "15_Chapter 9_1_Chapter 9 Code Examples_Example3.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "写程序的时间，大半花在找错上。这一讲不教新功能，而是教「怎么看懂报错、怎么让它别崩」。它是整门课从「会写」走向「写得能跑」的分水岭，也是期末机考最容易丢分的地方——不是不会写，而是报错看不懂。"
            )
            + p(
                "内容上与前面每一讲都相关：语法错误对应第 3–5 讲的缩进与冒号，运行时错误对应第 3 讲的类型、第 8 讲的下标、第 9 讲的文件，逻辑错误对应第 4 讲的 <code>elif</code> 顺序与第 5 讲的边界。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "把错误分成语法、运行时、逻辑三类，并说出各自能否被 <code>try</code> 捕获",
                "认识 <code>TypeError</code>、<code>NameError</code>、<code>IndexError</code>、<code>ValueError</code>、<code>ZeroDivisionError</code>、<code>FileNotFoundError</code> 的触发条件",
                "从 traceback 的最后一行读出异常类型，再顺着调用栈找到自己写的行",
                "写出 <code>try/except</code>，用 <code>as e</code> 拿到异常对象并打印",
                "用多 <code>except</code> 按类型分别处理，并解释顺序为什么重要",
                "写出「输入不合法就重试」的循环，直到拿到合法值",
            )
        ),
        detail=_D11,
        kws=_K11,
        examples=_EX11,
        practice=_PR11,
        exam=_EXAM11,
        checklist=_CK11,
        mapping=_MP11,
    )
)

# ============================================================ 12 字典、集合与 JSON
_D12 = (
    h2("一、先看数据处理的全貌")
    + p(
        "课件在第 10 章开头先讲了「数据」这件事本身（Chapter 10 Part 1 p3）：数据分析（data analytics）是把原始数据变成可用于决策的信息，分四层——数据层（数据库、API、CSV）、分析层（Python、R、Excel）、可视化层（图表、网页）、AI 层（机器学习）。这门课只做分析层里最基础的一段：用 Python 处理原始数据。"
    )
    + p("课件给的四个阶段（Part 1 p5）值得记住，因为每一阶段都对应一种数据结构：")
    + tb(
        ("阶段", "做什么", "本讲对应的结构"),
        ("1. 数据收集 collection", "从公开数据、日志、CSV 里拿到原始数据", "文件读取（第 9 讲）"),
        ("2. 数据处理 processing", "整理成表格、列表、对象等好处理的形状", "列表套字典（记录）"),
        ("3. 数据清洗 cleanup", "去掉坏数据、补缺失、检查合理性", "字典遍历 + 条件判断"),
        ("4. 探索性分析 EDA", "算统计量、找趋势", "字典计数、集合去重"),
    )
    + h2("二、字典：用键找值")
    + h3("2.1 创建与访问")
    + p(
        "字典（dictionary）是键值对（key-value pair）的集合（Part 2 p2）：每个值配一个键，用键就能直接取到值，不必知道它在第几个。"
    )
    + pre(
        '''person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)
print(person["name"])
print(person["age"])'''
    )
    + pre(
        """{'name': 'John', 'age': 30, 'city': 'New York'}
John
30"""
    )
    + p(
        "键必须是<b>不可变</b>类型：字符串、数字、元组可以，列表不行（<code>TypeError: unhashable type</code>）。值可以是任何东西，包括列表与另一个字典。"
    )
    + p(
        "取值用方括号加键：<code>person[\"name\"]</code>。键不存在时抛 <code>KeyError</code>——这是字典最典型的错误："
    )
    + pre(
        '''person = {"name": "John"}
print(person["age"])'''
    )
    + pre('''KeyError: 'age' ''')
    + h3("2.2 修改与添加")
    + p(
        "字典是<b>可变</b>的（Part 2 p2）：赋值语句既能改已有的键，也能新建键——语法完全一样，区别只在键是否存在。"
    )
    + pre(
        '''phone_numbers = {"Elon Musk": "555-3928372"}
phone_numbers["Elon Musk"] = "555-0000000"
phone_numbers["Bill Gates"] = "555-39482949"
print(phone_numbers)'''
    )
    + pre(
        """{'Elon Musk': '555-0000000', 'Bill Gates': '555-39482949'}"""
    )
    + p(
        "正因为「赋值即新增」，拼错键名不会报错，只会多出一条没人用的数据。这类错误只能靠「打印出来看看」发现。"
    )
    + h3("2.3 遍历")
    + p(
        "<code>for</code> 直接遍历字典时，拿到的是<b>键</b>（Part 2 p4）；要取值再用 <code>d[key]</code>："
    )
    + pre(
        '''my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key, my_dict[key])'''
    )
    + pre(
        '''a 1
b 2
c 3'''
    )
    + p(
        "顺序按插入顺序（Python 3.7 起保证），但不要把它当排序结果——要排序请用 <code>sorted()</code>。"
    )
    + h3("2.4 字典 vs 列表")
    + p("课件用「按名字查电话」把两者对比得很清楚（Part 2 p5）：")
    + tb(
        ("维度", "列表", "字典"),
        ("存法", "按顺序堆进去", "按键值对存"),
        ("查找方式", "下标 <code>L[2]</code>，或循环比对值", "键 <code>d[\"Sarah\"]</code>"),
        ("查找代价", "与元素个数成正比（线性）", "基本恒定（哈希）"),
        ("适合", "有顺序、要遍历、要排序", "按名字/编号快速查找"),
    )
    + pre(
        '''# 用列表：要循环找
names = ["Janne", "Elon"]
phones = ["555-492843", "555-2943483"]
for i in range(len(names)):
    if names[i] == "Elon":
        print(phones[i])

# 用字典：直接取
phone_numbers = {"Janne": "555-492843", "Elon": "555-2943483"}
print(phone_numbers["Elon"])'''
    )
    + pre(
        '''555-2943483
555-2943483'''
    )
    + p(
        "两个列表「平行存放」是常见但脆弱的写法：插入一个元素要同时改两个列表，一旦顺序错位，数据就全乱了。字典把键和值绑在一起，从结构上避免这种错位。"
    )
    + h2("三、字典的常用操作")
    + tb(
        ("操作", "作用", "说明"),
        ("<code>d[key]</code>", "取值", "键不存在 → <code>KeyError</code>"),
        ("<code>d[key] = v</code>", "改值或新增", "键存在就改，不存在就加"),
        ("<code>key in d</code>", "判断键是否存在", "只查键，不查值"),
        ("<code>len(d)</code>", "键值对数量", "—"),
        ("<code>d.pop(key)</code>", "删掉并返回值", "键不存在 → <code>KeyError</code>"),
        ("<code>d.popitem()</code>", "删掉并返回最后一对", "返回 <code>(key, value)</code>"),
        ("<code>d.clear()</code>", "清空", "—"),
        ("<code>sorted(d)</code>", "把键排序成列表", "不改原字典"),
        ("<code>d.copy()</code>", "浅拷贝", "嵌套对象仍共享"),
    )
    + pre(
        '''d = {"a": 1, "b": 2, "c": 3}
print("b" in d)
print(sorted(d))
print(d.pop("b"))
print(d)
print(d.popitem())
print(d)'''
    )
    + pre(
        """True
['a', 'b', 'c']
2
{'a': 1, 'c': 3}
('c', 3)
{'a': 1}"""
    )
    + p(
        "统计类程序的标准套路是「键存在就加一，不存在就建 1」，可以写成 <code>d[k] = d.get(k, 0) + 1</code>（<code>get</code> 属拓展），也可以先判断 <code>if k in d</code>。两种写法都不报错，直接写 <code>d[k] += 1</code> 在第一次遇到新键时会抛 <code>KeyError</code>。"
    )
    + h2("四、列表 + 字典：一条记录")
    + p(
        "真实数据通常是一堆「结构相同的记录」，每条记录用字典，整体用列表装（Part 2 p9）。这是本课处理 CSV、JSON 的通用形状。"
    )
    + pre(
        '''cars = [
    {"brand": "Ford", "year": 2015, "price": 15000},
    {"brand": "Skoda", "year": 2012, "price": 5000}
]

for car in cars:
    if car["brand"] == "Ford":
        print("Year of the Ford is:", car["year"])'''
    )
    + pre('''Year of the Ford is: 2015''')
    + p(
        "读法：<code>car</code> 是一条记录（字典），<code>car[\"year\"]</code> 取这一条的年份。要统计「每个品牌几辆车」，就用「品牌做键、数量做值」的字典累加。"
    )
    + h2("五、浅拷贝与深拷贝")
    + p(
        "课件专门讲了这一对概念（Part 2 p10–p11），因为它在「复制一份再改」时是隐形杀手。"
    )
    + pre(
        '''person = {"name": "John", "city": ["Helsinki", "Tallinn"]}
shallow = person.copy()
shallow["city"][0] = "Stockholm"

print(person)
print(shallow)'''
    )
    + pre(
        """{'name': 'John', 'city': ['Stockholm', 'Tallinn']}
{'name': 'John', 'city': ['Stockholm', 'Tallinn']}"""
    )
    + p(
        "<code>copy()</code> 只复制了最外层：新字典的 <code>city</code> 仍指向<b>同一个列表</b>，所以改浅拷贝里的列表，原字典也变。"
    )
    + pre(
        '''import copy

person = {"name": "John", "city": ["Helsinki", "Tallinn"]}
deep = copy.deepcopy(person)
deep["city"][0] = "Oslo"

print(person)
print(deep)'''
    )
    + pre(
        """{'name': 'John', 'city': ['Helsinki', 'Tallinn']}
{'name': 'John', 'city': ['Oslo', 'Tallinn']}"""
    )
    + p(
        "<code>copy.deepcopy()</code> 递归复制所有层，两个对象彻底独立。判断标准很简单：<b>值里有列表/字典等可变对象，就要深拷贝。</b>"
    )
    + h2("六、集合：只关心「有没有」")
    + p(
        "集合（set）像数学里的集合（sets p2）：元素不重复、没有顺序、用花括号写。它最适合两件事——去重与 membership 判断。"
    )
    + pre(
        '''numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(len(numbers), len(unique))
print(sorted(unique))

empty = {}      # 这是空字典，不是空集合！
empty_set = set()
print(type(empty), type(empty_set))'''
    )
    + pre(
        """6 3
[1, 2, 3]
<class 'dict'> <class 'set'>"""
    )
    + p(
        "元素必须可哈希（hashable），也就是不可变：整数、字符串、元组可以，列表与字典不行（sets p3）。原因是集合用哈希表实现，靠哈希值快速定位。"
    )
    + h3("6.1 增删")
    + tb(
        ("方法", "作用", "注意"),
        ("<code>s.add(x)</code>", "加一个元素", "已存在则不重复加"),
        ("<code>s.update(iterable)</code>", "批量加", "把列表/字符串的元素逐个加"),
        ("<code>s.remove(x)</code>", "删指定元素", "不存在 → <code>KeyError</code>"),
        ("<code>s.discard(x)</code>", "删指定元素", "不存在也不报错"),
        ("<code>s.pop()</code>", "删并返回任意一个", "集合无序，无法预测是哪个"),
        ("<code>s.clear()</code>", "清空", "—"),
    )
    + h3("6.2 集合运算")
    + p("这是集合最有价值的部分，方法与运算符一一对应（sets p6–p7）：")
    + tb(
        ("运算", "方法", "运算符", "含义"),
        ("并集", "<code>a.union(b)</code>", "<code>a | b</code>", "两边的全部元素"),
        ("交集", "<code>a.intersection(b)</code>", "<code>a &amp; b</code>", "两边都有的"),
        ("差集", "<code>a.difference(b)</code>", "<code>a - b</code>", "在 a 不在 b"),
        ("对称差", "<code>a.symmetric_difference(b)</code>", "<code>a ^ b</code>", "只在一边出现的"),
        ("子集", "<code>a.issubset(b)</code>", "<code>a &lt;= b</code>", "a 全在 b 里"),
        ("超集", "<code>a.issuperset(b)</code>", "<code>a &gt;= b</code>", "a 包含 b"),
    )
    + pre(
        '''IEEE = {"Python", "Java", "JavaScript", "C++", "TypeScript"}
TIOBE = {"Python", "C++", "Java", "C", "C#"}

print(sorted(IEEE | TIOBE))
print(sorted(IEEE & TIOBE))
print(sorted(IEEE - TIOBE))
print(sorted(IEEE ^ TIOBE))'''
    )
    + pre(
        """['C', 'C#', 'C++', 'Java', 'JavaScript', 'Python', 'TypeScript']
['C++', 'Java', 'Python']
['JavaScript', 'TypeScript']
['C', 'C#', 'JavaScript', 'TypeScript']"""
    )
    + p(
        "课件留了四个问题（sets p9）：两个榜单里出现过的语言（并集）、同时上榜的（交集）、只在 IEEE 的（差集）、只在一个榜单的（对称差）。上面四行输出就是四个答案，注意结果都<b>先 <code>sorted()</code> 再打印</b>——集合无序，直接打印每次顺序可能不同。"
    )
    + h2("七、CSV 的 DictReader")
    + p(
        "第 9 讲用 <code>split(\",\")</code> 手工切 CSV。字段里若含逗号或引号，手工切就会错位；标准库的 <code>csv</code> 模块能正确处理，<code>DictReader</code> 还会把每行变成字典（Part 3 p4–p5）："
    )
    + pre(
        '''import csv

csvfile = open("csv_e04.csv")
reader = csv.DictReader(csvfile)
for row in reader:
    print(row["name"], row["age"], row["gender"])
csvfile.close()'''
    )
    + pre(
        """Alice 25 Female
Bob 30 Male
Charlie 28 Male"""
    )
    + p(
        "<code>csv_e04.csv</code> 的第一行是表头 <code>name,age,gender</code>；<code>DictReader</code> 用它当键，于是可以按列名取值 <code>row[\"age\"]</code>，不必记「年龄是第 1 列」。值仍是字符串，算术前要 <code>int()</code>。"
    )
    + h2("八、JSON：能装嵌套结构的数据格式")
    + p(
        "CSV 只能表示「二维表」，装不了嵌套。JSON（JavaScript Object Notation）用花括号表示对象、方括号表示数组，能表达任意层嵌套（Part 4 p2）。它起源于 2000 年代初，现在是配置文件与网络接口的事实标准。"
    )
    + p("JSON 与 Python 字典长得很像，但有两条硬差别（Part 4 p3）：")
    + tb(
        ("维度", "Python 字典", "JSON"),
        ("键的类型", "任何不可变类型", "<b>只能是字符串</b>"),
        ("字符串引号", "单双引号都行", "<b>必须双引号</b>"),
        ("额外值", "<code>True / False / None</code>", "<code>true / false / null</code>"),
        ("注释", "可以有 <code>#</code>", "不允许"),
    )
    + pre(
        '''import json

person = {"name": "Alice", "age": 25, "hobbies": ["reading", "coding"]}
text = json.dumps(person)
print(text)

back = json.loads(text)
print(back)
print(type(back))'''
    )
    + pre(
        """{"name": "Alice", "age": 25, "hobbies": ["reading", "coding"]}
{'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'coding']}
<class 'dict'>"""
    )
    + p(
        "<code>json.dumps()</code> 把对象变成字符串（dump <b>s</b>tring），<code>json.loads()</code> 把字符串变回对象；读写文件用 <code>json.dump()</code> / <code>json.load()</code>（没有 s）。四个名字只差一个字母，方向记法：<b>s = string</b>。"
    )
    + pre(
        '''import json

books = [
    {"title": "Python Basics", "year": 2020},
    {"title": "Data Handling", "year": 2023}
]

file = open("books.json", "w")
json.dump(books, file)
file.close()

file = open("books.json", "r")
loaded = json.load(file)
file.close()
print(len(loaded), loaded[0]["title"])'''
    )
    + pre('''2 Python Basics''')
    + p(
        "多个对象存成 JSON 的标准形状是「对象数组」：外层方括号，里面每个元素是一个花括号对象。读回来就是一个「列表套字典」，与第四节的结构完全一致。"
    )
    + h2("九、把自己的函数变成模块")
    + p(
        "第 10 讲用的是别人的模块；这一节把自己的代码变成模块（Part 5 p2–p3）。做法只有四步："
    )
    + st(
        "新建一个 <code>.py</code> 文件，名字是合法的 Python 标识符（如 <code>calculator.py</code>）",
        "在里面写函数、类、常量",
        "把文件放在与调用者相同的目录（最简单）",
        "在另一个文件里 <code>import calculator</code>，然后 <code>calculator.add(2, 3)</code>",
    )
    + pre(
        '''# calculator.py
PI = 3.14159

def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y'''
    )
    + pre(
        '''# main.py
import calculator

print(calculator.PI)
print(calculator.add(2, 3))
print(calculator.divide(10, 0))'''
    )
    + pre(
        '''3.14159
5
Cannot divide by zero'''
    )
    + p(
        "导入时 Python 会生成一个 <code>__pycache__</code> 目录，里面是编译后的字节码，用来加速下次导入（Part 5 p5）。它不是给人读的，可以删掉，删了也不影响运行；打包给别人时最好删掉。"
    )
    + h3("9.1 if __name__ == \"__main__\"")
    + p(
        "一个文件既可能被「直接运行」，也可能被「导入」。导入时我们不希望它的测试代码自动执行，于是用这个判断把「只有直接运行时才做的事」包起来（Part 5 p6）："
    )
    + pre(
        '''# greet_module.py
def greet(name):
    return "Hello, " + name

if __name__ == "__main__":
    print(greet("world"))
    print("This runs only when the file is executed directly.")'''
    )
    + pre(
        '''# other.py
import greet_module
print(greet_module.greet("Alice"))'''
    )
    + p(
        "直接运行 <code>greet_module.py</code> 会打印那两行；被 <code>other.py</code> 导入时只输出 <code>Hello, Alice</code>，因为此时 <code>__name__</code> 是 <code>\"greet_module\"</code> 而不是 <code>\"__main__\"</code>。项目作业里把测试代码放进去，评分脚本导入你的模块时才不会被打扰。"
    )
    + h2("十、常见错误与调试")
    + cal(
        "warn",
        "KeyError：键不存在或拼错",
        "<code>d[\"nmae\"]</code> 一定报错。<code>print(d)</code> 看真实键名；不确定时用 <code>if key in d</code> 先判断，或 <code>d.get(key, default)</code> 取默认值。",
    )
    + cal(
        "warn",
        "{} 是空字典不是空集合",
        "空集合只能写 <code>set()</code>。<code>type({})</code> 是 <code>dict</code>，很多「去重没生效」的 bug 就出在这里。",
    )
    + cal(
        "warn",
        "对集合下标 / 排序",
        "集合无序，<code>s[0]</code> 直接抛 <code>TypeError</code>。要顺序就先 <code>sorted(s)</code> 变成列表。",
    )
    + cal(
        "warn",
        "copy 之后改嵌套仍影响原数据",
        "<code>d.copy()</code> 是浅拷贝。含列表/字典的值要 <code>copy.deepcopy()</code>。",
    )
    + cal(
        "tip",
        "JSON 报错先看引号",
        "<code>json.loads(\"{'a': 1}\")</code> 抛 <code>JSONDecodeError</code>，因为 JSON 只认双引号。把单引号换成双引号，或干脆用 <code>json.dumps</code> 生成字符串。",
    )
)

_K12 = K(
    ("dictionary", "字典", "A collection of key-value pairs."),
    ("key / value", "键 / 值", "You look up a value by its key."),
    ("key-value pair", "键值对", "\"name\": \"John\" is one pair."),
    ("KeyError", "键不存在", "Raised when the key is not in the dictionary."),
    ("hashable", "可哈希", "Only immutable objects can be dictionary keys or set elements."),
    ("set", "集合", "An unordered collection of unique elements."),
    ("union", "并集", "a | b contains everything from both sets."),
    ("intersection", "交集", "a & b contains elements in both."),
    ("difference", "差集", "a - b contains elements in a but not in b."),
    ("symmetric difference", "对称差", "a ^ b contains elements in exactly one set."),
    ("shallow copy", "浅拷贝", "copy() duplicates the outer level only."),
    ("deep copy", "深拷贝", "copy.deepcopy() duplicates every nested level."),
    ("JSON", "JSON 格式", "A text format for nested data; keys are strings in double quotes."),
    ("DictReader", "字典读取器", "csv.DictReader turns each row into a dictionary keyed by the header."),
    ("module", "模块", "Your own .py file can be imported like any library."),
)

_EX12 = (
    qa(
        "例 1　用字典做一个电话簿：加入三条记录，按名字查询，删除一条后打印全部。",
        p("「键是姓名、值是号码」是最小可用的字典；遍历时同时打印键与值。")
        + pre(
            '''phone_book = {}
phone_book["Alice"] = "555-0101"
phone_book["Bob"] = "555-0202"
phone_book["Charlie"] = "555-0303"

print(phone_book["Bob"])
print("Bob" in phone_book)

del_number = phone_book.pop("Charlie")
print("removed:", del_number)

for name in phone_book:
    print(name, phone_book[name])'''
        )
        + p("输出：")
        + pre(
            '''555-0202
True
removed: 555-0303
Alice 555-0101
Bob 555-0202'''
        )
        + p(
            "解释：空字典写 <code>{}</code>；赋值即新增；<code>in</code> 只查键；<code>pop</code> 删除并返回值。若查一个不存在的名字，例如 <code>phone_book[\"Dan\"]</code>，会抛 <code>KeyError</code>——所以查之前通常先 <code>in</code> 一下。"
        )
    )
    + qa(
        "例 2　统计一段文字里每个单词出现的次数，并按次数从高到低输出前三名。",
        p("「单词做键、次数做值」是字典最经典的用法；排序时用 <code>sorted</code> 的 <code>key</code> 参数按值排（拓展用法，理解即可）。")
        + pre(
            '''text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

counts = {}
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

pairs = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
for word, n in pairs[:3]:
    print(word, n)'''
        )
        + p("输出：")
        + pre(
            '''the 3
fox 2
quick 1'''
        )
        + p(
            "解释：<code>if w in counts</code> 分支保证第一次遇到新词时先建 1，否则 <code>counts[w] += 1</code> 会 <code>KeyError</code>；<code>counts.items()</code> 把键值对变成 <code>(key, value)</code> 元组列表（第 8 讲解包）；<code>key=lambda ...</code> 指定按值排序。若不想用 lambda，可以先按次数把字典反转再排序，思路相同。"
        )
    )
    + qa(
        "例 3　给定两个集合，输出并集、交集、只在第一个集合里的元素，以及「恰好在一个集合里」的元素。",
        p("四个问题正好对应四种集合运算，结果都先 <code>sorted()</code> 再打印，避免顺序随机。")
        + pre(
            '''A = {"Python", "Java", "C++", "Go"}
B = {"Python", "C#", "Java", "Rust"}

print("union:", sorted(A | B))
print("intersection:", sorted(A & B))
print("only A:", sorted(A - B))
print("exactly one:", sorted(A ^ B))'''
        )
        + p("输出：")
        + pre(
            '''union: ['C#', 'C++', 'Go', 'Java', 'Python', 'Rust']
intersection: ['Java', 'Python']
only A: ['C++', 'Go']
exactly one: ['C#', 'C++', 'Go', 'Rust']'''
        )
        + p(
            "解释：<code>^</code> 是「并集减去交集」，等价于 <code>(A | B) - (A &amp; B)</code>。若把集合换成列表做同样的事，就得写四层循环加 <code>in</code> 判断——这就是集合的价值。"
        )
    )
    + qa(
        "例 4　把字典写成 JSON 文件，再读回来修改一个字段并写回。",
        p("写用 <code>json.dump</code>，读用 <code>json.load</code>，两侧都要 <code>open</code> / <code>close</code>（第 9 讲）。")
        + pre(
            '''import json

config = {"user": "alice", "theme": "dark", "font_size": 14}

file = open("config.json", "w")
json.dump(config, file)
file.close()

file = open("config.json", "r")
loaded = json.load(file)
file.close()

loaded["font_size"] = 16
print(loaded)
print(json.dumps(loaded))'''
        )
        + p("输出：")
        + pre(
            """{'user': 'alice', 'theme': 'dark', 'font_size': 16}
{"user": "alice", "theme": "dark", "font_size": 16}"""
        )
        + p(
            "解释：<code>json.dump</code> 直接写进文件对象；读回来是普通字典，可以照常改；<code>json.dumps</code> 把结果变回字符串看格式。注意 JSON 输出里全是双引号——这正是它与 Python 字典打印结果的区别。"
        )
)
)

_PR12 = (
    ol(
        "用字典统计一个字符串中每个字符出现的次数（只统计字母）。",
        "给定两个列表（姓名、电话），改写成「姓名 → 电话」的字典，并查询指定姓名。",
        "给定一个有重复元素的列表，输出去重后的结果与重复元素集合。",
        "把 <code>{\"a\": 1, \"b\": 2}</code> 写成 JSON 字符串，再读回来并新增一个键。",
        "读入 <code>csv_e04.csv</code>，用 <code>DictReader</code> 统计男性与女性各有多少人。",
    )
    + det(
        "答案与思路",
        p(
            "<b>1.</b> <code>counts = {}</code>，遍历 <code>s.lower()</code>，用 <code>ch.isalpha()</code> 过滤，再按「存在就 +1，否则建 1」更新。如果只统计字母，别忘 <code>lower()</code> 统一大小写。"
        )
        + p(
            "<b>2.</b> <code>d = {}</code>，<code>for i in range(len(names)): d[names[i]] = phones[i]</code>。本质是把两个平行列表合成一个映射；用 <code>zip</code> 更短（拓展），但下标写法最直白。"
        )
        + p(
            "<b>3.</b> <code>unique = set(L)</code>；重复元素需要计数才能判断，简单的做法是「出现次数大于 1 的元素」：<code>{x for x in L if L.count(x) &gt; 1}</code>（集合推导属拓展），或循环 + 字典计数后筛选。"
        )
        + p(
            "<b>4.</b> <code>s = json.dumps(d)</code>；<code>back = json.loads(s)</code>；<code>back[\"c\"] = 3</code>。注意 <code>dumps</code> 的结果里是双引号，这是 JSON 规范。"
        )
        + p(
            "<b>5.</b> <code>counts = {\"Male\": 0, \"Female\": 0}</code>，遍历 <code>reader</code>，<code>counts[row[\"gender\"]] += 1</code>。这里键只有两种，先建好 0 就不会 <code>KeyError</code>；若性别值不确定，仍要先 <code>if ... in</code>。"
        ),
    )
)

_EXAM12 = (
    cal(
        "exam",
        "必考",
        "字典的键值访问与 <code>KeyError</code>；<code>in</code> 判断键、<code>pop</code>、<code>len</code>；字典与列表查找方式的区别；集合的去重与四种运算；CSV 的 <code>DictReader</code>；JSON 的 <code>dumps</code> / <code>loads</code> 与「键必须是字符串、必须双引号」。",
    )
    + cal(
        "warn",
        "易错 1　{} 与 set()",
        "空字典 <code>{}</code>、空集合 <code>set()</code>，写反了「去重」就变成「往字典里塞东西」，报错信息还会让人一头雾水。",
    )
    + cal(
        "warn",
        "易错 2　浅拷贝改到原数据",
        "<code>d.copy()</code> 只复制外层；值里有列表时改副本会同时改原字典。要独立就 <code>copy.deepcopy</code>。",
    )
    + cal(
        "warn",
        "易错 3　集合无序还当下标用",
        "<code>s[0]</code> 抛 <code>TypeError</code>，直接 <code>print(s)</code> 每次顺序还可能不同。要顺序请 <code>sorted(s)</code>。",
    )
    + cal(
        "tip",
        "进阶",
        "<code>d.get(k, default)</code> 避免 KeyError；<code>counts.items()</code> 同时取键值；<code>if __name__ == \"__main__\"</code> 让模块可导入；<code>collections.Counter</code> 一行完成计数（属后续课程）。",
    )
)

_CK12 = (
    h2("操作清单")
    + h3("选数据结构")
    + st(
        "数据是「一串有序的值」→ 列表",
        "数据是「按名字/编号查的值」→ 字典",
        "数据要「去重」或「判断有没有」→ 集合",
        "数据是「一条记录多个字段」→ 字典；多条记录 → 列表套字典",
        "数据要跨程序保存、还要嵌套 → JSON 文件",
    )
    + h3("写完后的检查")
    + ck(
        "访问字典前，键是否一定存在（必要时先 <code>in</code>）",
        "统计计数时，新键是否先建了初值",
        "复制含嵌套的字典用了 <code>deepcopy</code>",
        "打印集合前先 <code>sorted()</code>",
        "JSON 的键都是字符串、引号都是双引号",
        "自己的模块被导入时，测试代码放在 <code>__main__</code> 判断里",
    )
)

_MP12 = (
    tb(
        ("源文件", "页码", "覆盖知识点"),
        (
            "Chapter 10 - Part 1 - About data.pdf",
            "p3–p5",
            "数据分析的定义与四层结构、收集/处理/清洗/探索四阶段",
        ),
        (
            "Chapter 10 - Part 2 - Dictionaries.pdf",
            "p2–p11",
            "键值对定义、键必须不可变、创建与修改、遍历取键、字典 vs 列表、方法、记录列表、浅拷贝与 deepcopy",
        ),
        (
            "Chapter 10 - Part 3 - CSV.pdf",
            "p2–p5",
            "CSV 复习、<code>csv.DictReader</code> 按列名取值",
        ),
        (
            "Chapter 10 - Part 4 - JSON.pdf",
            "p2–p6",
            "JSON 的由来与用途、与字典的两条差别、<code>dumps</code>/<code>loads</code>、对象数组、<code>json.load</code> 读文件",
        ),
        (
            "Chapter 10 - Part 5 - Own modules.pdf",
            "p2–p6",
            "自建模块的四步、<code>import</code> 与 <code>from ... import</code>、<code>__pycache__</code>、<code>__main__</code> 判断",
        ),
        (
            "sets.pdf",
            "p2–p9",
            "集合定义、去重、无序、hashable、增删方法、六种集合运算与运算符、IEEE/TIOBE 练习",
        ),
        ("W10E01.py / W10E02.py", "全文", "字典查找与「列表 + 字典」记录"),
        ("W10E03.py", "全文", "浅拷贝改到原字典的实证"),
        ("W10E04.py / csv_e04.csv", "全文", "<code>DictReader</code> 按列名读取"),
        ("W10E05.py", "全文", "<code>json.dumps</code> 与 <code>json.loads</code> 往返"),
        ("W10E06.py / calculator.py", "全文", "自建模块的导入与调用"),
    )
    + p(
        "<b>跳过项：</b>Part 1 的 TED 演讲链接与配图、Part 3–4 的 Excel/JSON 截图只作背景；Moodle 第 10 章的作业与截止页属于行政信息，不进入本讲。另有「38_Project work」下的项目作业说明（汽车租赁系统）与概念回顾课件，其知识点（print / input / def / while / for / 文件 / 日期）已分别落在第 5–10 讲，作业要求本身属于考核材料，不单列讲次。"
    )
    + p(
        "<b>拓展项：</b><code>d.get</code>、<code>items()</code>、<code>zip</code>、<code>lambda</code> 排序键、集合推导，都是围绕原知识点的实用补充；考试以课件函数与方法清单为准。"
    )
)

LEC.append(
    L(
        slug="ch12-dicts-sets-json",
        tzh="⑫ 字典、集合与 JSON",
        ten="Dictionaries, Sets and JSON",
        keywords=[
            "dictionary",
            "key",
            "value",
            "KeyError",
            "hashable",
            "set",
            "union",
            "intersection",
            "difference",
            "shallow copy",
            "deep copy",
            "JSON",
            "DictReader",
        ],
        files=[
            "Chapter 10 - Part 1 - About data.pdf",
            "Chapter 10 - Part 2 - Dictionaries.pdf",
            "Chapter 10 - Part 3 - CSV.pdf",
            "Chapter 10 - Part 4 - JSON.pdf",
            "Chapter 10 - Part 5 - Own modules.pdf",
            "sets.pdf",
            "16_Chapter 10_1_Code Examples_W10E04.py",
        ],
        overview=(
            h2("本节定位")
            + p(
                "这是全课程最后一讲新内容，也是把前面所有容器收口的一讲：字典用来「按键查找」，集合用来「去重与比较」，JSON 把嵌套数据存成文本。项目作业里的车辆、客户、交易记录，形状就是这一讲的「列表套字典」。"
            )
            + p(
                "它同时回收了三条旧线：第 8 讲的列表与元组（字典的值常常是列表，<code>items()</code> 返回元组）、第 9 讲的文件读写（JSON 就是文件里的文本）、第 10 讲的模块（这一讲把你自己的文件变成模块）。"
            )
            + p("学完本讲你应当能够：")
            + ck(
                "创建字典、按键取值与赋值，并解释 <code>KeyError</code> 从哪来",
                "用字典统计频次，处理「新键先建初值」的问题",
                "把多条记录写成「列表套字典」，并遍历筛选",
                "说清浅拷贝与深拷贝的区别，知道什么时候必须 <code>deepcopy</code>",
                "用集合去重并做并、交、差、对称差运算",
                "用 <code>DictReader</code> 读 CSV、用 <code>json</code> 模块存取嵌套数据",
                "把自己的函数写成模块，并用 <code>__main__</code> 判断隔离测试代码",
            )
        ),
        detail=_D12,
        kws=_K12,
        examples=_EX12,
        practice=_PR12,
        exam=_EXAM12,
        checklist=_CK12,
        mapping=_MP12,
    )
)

# @@NEXT@@

emit(
    BASE["id"],
    BASE["order"],
    BASE["name_zh"],
    BASE["name_en"],
    BASE["source_dir"],
    BASE["summary"],
    LEC,
)
