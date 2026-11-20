# -*- coding: utf-8 -*-
"""CT60A0250 · 按 Moodle Chapter 1–13 重排；新增 Chapter 11 与两个空章说明"""

import os
import sys
import json
import io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, cal, qa, det, pre  # noqa: E402

CID = "30352"
PATH = os.path.join(SITE, "content", CID + ".json")
data = json.load(io.open(PATH, encoding="utf-8"))
by = {l["slug"]: l for l in data["lectures"]}

PARTS = {
    "ch01-env-basics": "第 1 章 入门：类型、运算与输入输出",
    "ch02-operators-io": "第 1 章 入门：类型、运算与输入输出",
    "ch03-strings-comments": "第 2 章 字符串与打印",
    "ch04-conditionals": "第 3 章 条件与布尔逻辑",
    "ch05-loops": "第 4 章 循环",
    "ch06-functions": "第 5 章 函数",
    "ch07-classes": "第 6 章 类、列表与矩阵",
    "ch08-lists-tuples": "第 6 章 类、列表与矩阵",
    "ch09-files-csv": "第 7 章 文本文件与 CSV",
    "ch10-modules": "第 8 章 Python 模块",
    "ch11-errors": "第 9 章 错误与异常",
    "ch12-dicts-sets-json": "第 10 章 数据、字典、JSON 与自有模块",
    "supp-setup-and-project": "附录 B 环境、项目与代码示例",
    "supp-code-examples": "附录 B 环境、项目与代码示例",
    "appendix-course-map": "附录 A 课程全景",
}
for s, pt in PARTS.items():
    if s in by:
        by[s]["part"] = pt

# ---------------- Chapter 11 ----------------
ch11 = L(
    slug="ch11-tuples-sets-packages-numpy",
    tzh="Chapter 11 · 元组、集合、类型转换、包与 NumPy",
    ten="Tuples, Sets, Type Conversions, Packages and NumPy",
    keywords=[
        "tuple",
        "immutable",
        "set",
        "hashable",
        "duplicate",
        "type conversion",
        "package",
        "PyPI",
        "pip",
        "NumPy",
        "array",
        "shape",
    ],
    files=[
        "tuples.pdf",
        "sets.pdf",
        "type_conversions.pdf",
        "packages.pdf",
        "installing_numpy.pdf",
        "using_numpy.pdf",
        "tuple.py",
    ],
    overview=(
        h2("本节定位")
        + p(
            "Chapter 11 是课程最后一周：把前面用过的容器补齐为「元组 / 集合 / 列表」三件套，"
            "再跨出标准库，用 pip 安装 NumPy 处理矩阵。它是期末考「容器选择 + 简单数据分析」的来源。"
        )
        + p("学完本章你应当能够：")
        + ck(
            "创建元组、索引与解包，说明为什么元组不可变",
            "用元组从函数返回多个值，并解释与返回列表的差别",
            "创建集合、去重、做交并差，说明元素为什么必须可哈希",
            "在 list / tuple / set 之间转换，并预判转换后的顺序与去重",
            "区分模块、包、PyPI 与 pip 的角色",
            "安装 NumPy 并创建一维/二维数组、读取 shape、做基本运算",
        )
        + p(
            "与前后讲的衔接：第 6 章讲过列表与矩阵，本章把「不可变版本」和「无序版本」补上；"
            "NumPy 是第 6 章矩阵的工业版实现。"
        )
    ),
    detail=(
        h3("11.1 元组：不可变的有序集合（tuples.pdf）")
        + p(
            "元组（tuple）把一组元素按固定顺序放在一起，用圆括号和逗号创建。"
            "与列表唯一的本质差别是<b>不可变</b>：创建后不能增删改元素。"
        )
        + pre(
            "point = (3, 5)\nrgb = (255, 128, 0)\nsingle = (42,)      # 一个元素也要留逗号\nempty = ()\nprint(point[0], point[-1])   # 3 5\nprint(len(rgb))              # 3"
        )
        + p(
            "正因为不可变，元组可以放进集合、可以当字典的键；列表不行。"
            "元组适合存「不该被改动」的数据：坐标、RGB 颜色、函数返回的多值。"
        )
        + tb(
            ("对比项", "tuple", "list"),
            ("可变性", "不可变", "可变（append/remove/赋值）"),
            ("括号", "()", "[]"),
            ("能否作集合元素/字典键", "可以（可哈希）", "不可以"),
            ("遍历与访问速度", "通常更快、更省内存", "因可变性略有开销"),
            ("内置方法", "只有 count()、index()", "大量方法"),
        )
        + p(
            "元组只有两个方法：<code>count(x)</code> 数出现次数，<code>index(x)</code> 返回第一次出现的下标。"
        )
        + pre("t = (1, 2, 2, 3)\nprint(t.count(2))   # 2\nprint(t.index(3))   # 3")
        + p(
            "返回多个值：Python 函数表面只能返回一个对象，用元组就能「打包」多个值，调用处再解包。"
        )
        + pre(
            "def min_max(nums):\n    return min(nums), max(nums)\n\nlow, high = min_max([3, 1, 7])\nprint(low, high)   # 1 7"
        )
        + h3("11.2 集合：无序、去重、可哈希（sets.pdf）")
        + p(
            "集合（set）对应数学集合：用花括号写元素，或用 <code>set()</code> 从列表/元组构造。"
            "三个特征：<b>元素不重复</b>、<b>没有顺序与下标</b>、<b>本身可变但元素必须不可变</b>。"
        )
        + pre(
            "a = {1, 2, 2, 3}\nprint(a)              # {1, 2, 3}\nb = set([3, 3, 4])\nprint(b)              # {3, 4}\nprint(2 in a)         # True"
        )
        + p(
            "集合用哈希表实现：加入元素时先算哈希值，因此元素必须可哈希（整数、字符串、元组可以；列表、字典不行）。"
            "这也是集合查找为 O(1) 的原因。"
        )
        + tb(
            ("运算", "写法", "结果示例"),
            ("并集", "a | b 或 a.union(b)", "{1,2,3} | {3,4} = {1,2,3,4}"),
            ("交集", "a & b 或 a.intersection(b)", "{1,2,3} & {3,4} = {3}"),
            ("差集", "a - b 或 a.difference(b)", "{1,2,3} - {3,4} = {1,2}"),
            ("对称差", "a ^ b", "{1,2,3} ^ {3,4} = {1,2,4}"),
        )
        + cal(
            "warn",
            "易错",
            "<code>{}</code> 是空字典不是空集合；空集合必须写 <code>set()</code>。"
            "另外集合没有下标，<code>s[0]</code> 会报 TypeError。",
        )
        + h3("11.3 三种容器互转（type_conversions.pdf）")
        + tb(
            ("目标", "函数", "顺序", "重复元素"),
            ("list", "list(t)", "保持原顺序（set 转 list 顺序不定）", "保留"),
            ("tuple", "tuple(l)", "保持原顺序", "保留"),
            ("set", "set(l)", "无顺序", "自动去重"),
        )
        + pre(
            "l = [3, 1, 3, 2]\nprint(list(set(l)))    # 顺序不定，长度 3\nprint(tuple(l))        # (3, 1, 3, 2)\nprint(set(tuple(l)))   # {1, 2, 3}"
        )
        + p(
            "用集合去重的经典写法是 <code>list(set(l))</code>，但要注意结果顺序不可依赖；"
            "需要「去重且保序」时，用循环 + 已见集合自己实现。"
        )
        + h3("11.4 模块、包与 PyPI（packages.pdf）")
        + tb(
            ("概念", "定义", "例子"),
            (
                "module 模块",
                "一个 .py 文件，含函数/类/变量",
                "math、random、自己写的 tools.py",
            ),
            ("package 包", "一个目录，含一个或多个模块", "numpy、pandas"),
            ("standard library 标准库", "随 Python 预装", "math、random、datetime"),
            ("PyPI", "第三方包的索引站", "pypi.org"),
            ("pip", "安装包的工具", "pip install numpy"),
        )
        + p(
            "导入方式：<code>import math</code>、<code>from math import sqrt</code>、<code>import numpy as np</code>。"
            "包要先安装才能 import，标准库不需要。"
        )
        + h3("11.5 安装 NumPy（installing_numpy.pdf）")
        + st(
            "打开终端（Terminal / PowerShell / cmd）",
            "确认 pip：<code>pip --version</code>",
            "升级 pip：<code>pip install --upgrade pip</code>",
            "安装：<code>pip install numpy</code>",
            '验证：<code>python -c "import numpy; print(numpy.__version__)"</code>',
        )
        + cal(
            "tip",
            "国内网络",
            "下载慢时可换镜像源：<code>pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple</code>；"
            "装错版本用 <code>pip install numpy==1.26.4</code> 固定版本。",
        )
        + h3("11.6 使用 NumPy（using_numpy.pdf）")
        + p(
            "NumPy 的核心是 <code>ndarray</code>：同类型元素、连续内存、固定形状。"
            "它支持逐元素运算、广播、矩阵乘法与统计函数，比嵌套列表快一个数量级。"
        )
        + pre(
            "import numpy as np\n\na = np.array([1, 2, 3, 4, 5])          # 一维\nm = np.array([[1, 2, 3], [4, 5, 6]])   # 二维\nprint(m.shape)        # (2, 3)\nprint(m[1, 2])        # 6\nprint(a * 2)          # [2 4 6 8 10]\nprint(m.sum(axis=0))  # 每列之和 [5 7 9]\nprint(np.zeros((3, 3)))\nprint(np.ones((2, 4)))"
        )
        + tb(
            ("操作", "写法", "说明"),
            ("创建", "np.array(list)", "从列表/嵌套列表构造"),
            ("全零/全一", "np.zeros(shape) / np.ones(shape)", "参数是元组"),
            ("形状", "arr.shape", "返回 (行, 列)"),
            ("变形", "arr.reshape(3, 2)", "元素总数必须一致"),
            ("矩阵乘", "a @ b 或 np.dot(a, b)", "不是逐元素乘"),
            ("统计", "arr.sum(axis=0/1)", "按列/按行求和"),
        )
        + cal(
            "warn",
            "易错",
            "<code>a * b</code> 是逐元素乘，矩阵乘要用 <code>a @ b</code>；"
            "<code>reshape</code> 不改变原数组，返回新数组。",
        )
    ),
    kws=tb(
        ("English", "中文", "说明 / 例句"),
        ("tuple", "元组", "point = (3, 5)"),
        ("immutable", "不可变", "t[0] = 1 会报错"),
        ("unpacking", "解包", "low, high = min_max(x)"),
        ("set", "集合", "a = {1, 2, 3}"),
        ("hashable", "可哈希", "元组可哈希，列表不可"),
        ("duplicate", "重复元素", "集合自动去重"),
        ("union / intersection", "并集 / 交集", "a | b, a & b"),
        ("type conversion", "类型转换", "list()、tuple()、set()"),
        ("package", "包", "numpy 是包，math 是模块"),
        ("PyPI", "Python 包索引", "pypi.org"),
        ("pip", "包安装工具", "pip install numpy"),
        ("ndarray", "NumPy 数组", "np.array([1,2,3])"),
        ("shape", "形状", "(2, 3) 表示 2 行 3 列"),
        ("broadcasting", "广播", "不同形状按规则扩展"),
    ),
    examples=(
        h2("例题 1：去重并保序")
        + qa(
            "把 <code>[3, 1, 3, 2, 1]</code> 去重且保持首次出现顺序。",
            p("直接用 <code>list(set(l))</code> 会丢顺序。正确做法是用一个已见集合：")
            + pre(
                "seen = set()\nout = []\nfor x in l:\n    if x not in seen:\n        seen.add(x)\n        out.append(x)"
            ),
        )
        + h2("例题 2：元组做字典键")
        + qa(
            "统计网格中每个坐标出现的次数，坐标用 (row, col) 表示。",
            p(
                "元组可哈希，能直接做键：<code>counts[(r, c)] = counts.get((r, c), 0) + 1</code>。"
                "若用列表 <code>[r, c]</code> 会抛 TypeError: unhashable type。"
            ),
        )
        + h2("例题 3：NumPy 求列平均")
        + qa(
            "给定 3×2 矩阵，求每列平均值。",
            p(
                "<code>m.mean(axis=0)</code> 返回长度 2 的数组；<code>axis=0</code> 表示沿行方向压缩，即按列统计。"
                "若写成 <code>axis=1</code> 得到每行平均。"
            ),
        )
    ),
    practice=(
        h2("练习")
        + p(
            "1. 写出把 <code>[1, 2, 2, 3]</code> 变成 <code>(1, 2, 2, 3)</code> 与 <code>{1, 2, 3}</code> 的代码。"
        )
        + det(
            "答案与思路",
            p("<code>tuple(l)</code> 保序保重复；<code>set(l)</code> 去重且无序。"),
        )
        + p("2. 为什么 <code>{[1,2]}</code> 会报错？怎么改？")
        + det(
            "答案与思路",
            p("列表不可哈希，不能放进集合；改成元组 <code>{(1,2)}</code>。"),
        )
        + p(
            "3. 解释 <code>pip</code>、<code>PyPI</code>、<code>package</code> 三者的关系。"
        )
        + det(
            "答案与思路",
            p(
                "PyPI 是索引站，pip 是从 PyPI 下载安装的工具，package 是被安装的包（如 numpy）。"
            ),
        )
        + p("4. 用 NumPy 创建 3×3 全零矩阵并把中心设为 1。")
        + det(
            "答案与思路",
            p("<code>m = np.zeros((3,3)); m[1,1] = 1</code>，下标从 0 开始。"),
        )
    ),
    exam=(
        h2("考点与难点")
        + cal(
            "exam",
            "必考",
            ul(
                "元组与列表的三点区别（可变性、括号、可否作键）",
                "元组解包返回多值",
                "集合去重与交并差运算",
                "三种容器互转后的顺序与去重行为",
                "模块/包/PyPI/pip 的概念区分",
                "NumPy 数组创建、shape、axis 统计",
            ),
        )
        + cal(
            "warn",
            "易错",
            ul(
                "空集合写成 {}（那是字典）",
                "用 list(set(l)) 后依赖顺序",
                "把元组当可变对象去赋值",
                "矩阵乘用 * 而不是 @",
                "reshape 以为原地修改",
            ),
        )
        + cal(
            "tip",
            "进阶",
            p(
                "能解释「集合查找为什么是 O(1)」「NumPy 为什么比嵌套列表快」，"
                "把哈希表与连续内存两件事讲清楚，是本章的加分点。"
            ),
        )
    ),
    checklist=(
        h2("方法清单")
        + st(
            "先问数据会不会变：会变用 list，不会变用 tuple",
            "需要去重或集合运算时再转 set，别过早转换",
            "要保序去重就用「已见集合 + 输出列表」",
            "用元组做复合键前确认元素都可哈希",
            "第三方包先 pip install，再 import，最后验证版本",
            "NumPy 统计先确认 axis：0 按列，1 按行",
        )
    ),
    mapping=(
        h2("源文件对应")
        + tb(
            ("源文件", "页码", "覆盖内容"),
            (
                "tuples.pdf",
                "p1–p7",
                "11.1 元组定义、不可变、创建、场景、对比、方法、返回多值",
            ),
            ("sets.pdf", "p1–p4", "11.2 集合创建、去重、无序、哈希表、交并差"),
            ("type_conversions.pdf", "p1–p4", "11.3 三种容器互转"),
            ("packages.pdf", "p1–p4", "11.4 模块、包、PyPI、pip"),
            ("installing_numpy.pdf", "p1–p4", "11.5 安装步骤与验证"),
            ("using_numpy.pdf", "p1–p6", "11.6 ndarray、创建、shape、运算与统计"),
            ("tuple.py", "代码示例", "11.1 返回多值的完整例子"),
        )
        + p(
            "<b>说明</b>：本章原属第 6、8、10 讲中的元组/集合/包内容，现按 Moodle Chapter 11 独立成章；"
            "原讲次保留作为前置复习，不重复计入本章。"
        )
    ),
)
ch11["part"] = "第 11 章 元组、集合、包与 NumPy"


def empty_chapter(num, exist_note):
    slug = "ch%d-not-open" % num
    tzh = "Chapter %d · 未开放（源课程为空）" % num
    ov = (
        h2("本节定位")
        + p(
            "Moodle 上 Chapter %d 这一栏在 2026 学年是空的：既没有 slides/video，也没有代码示例或练习。"
            "本页说明它的状态，避免你在总览里误以为「漏抓」。" % num
        )
        + ck(
            "确认该章在源课程中确实为空",
            "知道替代的复习材料在哪里",
            "遇到后续开放时如何补进来",
        )
    )
    de = (
        h3("%d.1 抓取证据" % num)
        + p(
            "登录后打开 <code>course/view.php?id=30352&section=%s</code>：section 里只有标题，"
            "没有 <code>mod_label</code>、<code>mod_folder</code>、<code>mod_resource</code> 或 video 链接。"
            % (17 if num == 12 else 18)
        )
        + p("%s" % exist_note)
        + h3("%d.2 为什么可能出现空章" % num)
        + ul(
            "课程进度未到：材料按周发布，后两章可能排在期末之后；",
            "内容合并：部分年份把最后两章并入 Chapter 10/11 或项目工作；",
            "权限/隐藏：section 被设置为对 students 隐藏。",
        )
        + h3("%d.3 现在该复习什么" % num)
        + p(
            "用已发布的 Chapter 10（数据、字典、CSV、JSON、自有模块）与 Chapter 11（元组、集合、包、NumPy）"
            "覆盖容器与库的全部考点；再用附录 A 的视频索引补看项目与考试说明。"
        )
    )
    return L(
        slug=slug,
        tzh=tzh,
        ten="Chapter %d (not published)" % num,
        keywords=["not published", "empty section", "Chapter %d" % num, "Moodle"],
        files=["Moodle course page section %s" % (17 if num == 12 else 18)],
        overview=ov,
        detail=de,
        kws=tb(
            ("English", "中文", "说明"),
            ("section", "栏目", "Moodle 课程分区"),
            ("not published", "未发布", "无材料"),
        ),
        examples=h2("说明")
        + qa(
            "这一章有考试内容吗？",
            p("源课程未发布材料，无法据此判断考点；以老师公告为准，不要自行推测。"),
        ),
        practice=h2("练习")
        + p("1. 打开课程页确认该 section 是否仍为空。")
        + det("提示", p("登录 Moodle，展开对应 section，看是否有新增资源。")),
        exam=h2("考点与难点")
        + cal("warn", "提示", p("空章不代表不考；若老师后续补发材料，以新材料为准。")),
        checklist=h2("方法清单")
        + st(
            "每月回看一次该 section 是否有更新",
            "关注公告论坛",
            "用相邻章节材料覆盖同类考点",
        ),
        mapping=h2("源文件对应")
        + tb(
            ("来源", "位置", "状态"),
            (
                "Moodle course page",
                "section %s" % (17 if num == 12 else 18),
                "空（无资源）",
            ),
        ),
    )


ph12 = empty_chapter(
    12,
    "Chapter 12 section 的 <code>courseindex-sectioncontent</code> 列表为空，且 section 带锁图标。",
)
ph13 = empty_chapter(
    13, "Chapter 13 section 同样为空，且位于课程末尾、紧接 Exercises 之前。"
)
ph12["part"] = "第 12 章 未开放"
ph13["part"] = "第 13 章 未开放"

# ---------------- 重新排序 ----------------
order = [
    "ch01-env-basics",
    "ch02-operators-io",
    "ch03-strings-comments",
    "ch04-conditionals",
    "ch05-loops",
    "ch06-functions",
    "ch07-classes",
    "ch08-lists-tuples",
    "ch09-files-csv",
    "ch10-modules",
    "ch11-errors",
    "ch12-dicts-sets-json",
]
lecs = [by[s] for s in order if s in by]
lecs.append(ch11)
lecs.append(ph12)
lecs.append(ph13)
for s in ["appendix-course-map", "supp-setup-and-project", "supp-code-examples"]:
    if s in by:
        lecs.append(by[s])
data["lectures"] = lecs
data["lectures"] = (
    [
        x
        for x in data["lectures"]
        if x["slug"]
        not in ("ch11-tuples-sets-packages-numpy", "ch12-not-open", "ch13-not-open")
    ]
    + [ch11, ph12, ph13]
    if False
    else lecs
)

with io.open(PATH, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
print("ok", len(lecs), [x["slug"] for x in lecs])
