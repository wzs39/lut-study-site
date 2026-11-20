# -*- coding: utf-8 -*-
"""30352 编程基础 · 补遗一讲：macOS/Linux 环境、AI 使用准则与课程项目"""

import os, sys, json, io

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, pre, code, chips

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "30352"
PATH = os.path.join(SITE, "content", CID + ".json")
kw = K  # 术语表：10–16 条，列数与 genlib.K 一致


def qa(title, *bodies):
    """本脚本内的 qa：允许一次传多个段落，内部拼成一个 body。"""
    from genlib import qa as _qa

    return _qa(title, chr(10).join(str(b) for b in bodies))


LEC = L(
    slug="supp-setup-and-project",
    tzh="补遗 · macOS / Linux 安装、AI 使用准则与汽车租赁项目",
    ten="Installing on macOS and Linux, How to Use AI, and the Car Rental Project",
    keywords=[
        "installer",
        "universal2",
        "tkinter",
        "PATH",
        "Gatekeeper",
        "IDLE-Mod",
        "CodeGrade",
        "menu-driven",
        "main key",
        "rental duration",
        "plagiarism",
        "ASCII",
        "Unicode",
        "UTF-8",
        "two decimal places",
    ],
    files=[
        "Installing Python 3.13.7 on macOS.pdf",
        "Installing IDLE-Mod on macOS.pdf",
        "Installing IDLE-Mod on Linux.pdf",
        "HowToUseAI.pdf",
        "Extra reading.pdf",
        "Project instructions Car rental management system.html",
        "Project work concepts recap.pptx",
        "project_work_concepts.py",
        "vehicles.txt",
        "customers.txt",
        "rentedVehicles.txt",
        "transactions.txt",
        "Tutorial instructors.html",
    ],
    # ------------------------------------------------------------------ overview
    overview="\n".join(
        [
            h2("本节定位"),
            p(
                "前 12 讲按章节走完了 Python 的语言本身，但有三类材料一直没进正文："
                "一门课的开课准备（macOS 与 Linux 上怎么装 Python 与 IDLE-Mod）、"
                "一份 AI 使用准则（<code>HowToUseAI.pdf</code>）、"
                "以及占成绩很大一块的课程项目（汽车租赁管理系统，带四个数据文件与完整的提交与评分规则）。"
                "正文只讲了 Windows 安装与各章语法，这三块恰好是「动手之前」与「交作业之前」必须知道的部分。"
            ),
            p(
                "另外两份文件也要处理：<code>Extra reading.pdf</code> 讲二进制、ASCII、浮点与内存地址，"
                "原文第 2 页明确写了它<b>不考</b>（“This material is not asked in EXAM”）；<code>Tutorial instructors.html</code> 是答疑时间表，属于行政信息。"
                "两者都收进来，但标注清楚用法差别，避免复习时把力气用错地方。"
            ),
            p("学完本讲你能够："),
            ck(
                "能够在一台 Mac 或 Linux 机器上装好 Python 3.13.7（或 3.13.x）与 IDLE-Mod，并用一条命令验证 tkinter 可用；",
                "能够按报错信息定位「解释器找不到 / 版本不对 / 应用已损坏 / 子进程连不上」四类问题；",
                "能够说出课程允许与不允许的 AI 用法，并解释为什么「代写」会让你在后面的章节掉队；",
                "能够讲清 <code>vehicles.txt</code>、<code>customers.txt</code>、<code>rentedVehicles.txt</code>、"
                "<code>transactions.txt</code> 四个文件的字段含义与读写时机；",
                "能够按「每开始 24 小时算一天」算出租金，并把结果写成两位小数；",
                "能够按 CodeGrade 的要求打包提交，并说清抄袭检测为什么认得出改名的代码。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ detail
    detail="\n".join(
        [
            h2("一、三个平台的安装：macOS 与 Linux 补齐"),
            p(
                "正文第 1 讲只讲 Windows 11 的装法，这门课还有两份安装说明没被用到："
                "<code>Installing Python 3.13.7 on macOS.pdf</code> 与 <code>Installing IDLE-Mod on macOS.pdf</code>、"
                "<code>Installing IDLE-Mod on Linux.pdf</code>。三份文件加起来只讲一件事："
                "先把 Python 装成课程要求的版本，再装那个改过的 IDLE，最后用一条命令验证 tkinter 在不在。"
            ),
            h3("1.1 macOS：用官方 pkg 装 Python 3.13.7"),
            p(
                "装的是 <code>python-3.13.7-macos11.pkg</code>（67.8 MB），原文写明它能装在 Intel 与 Apple Silicon 两类 Mac 上，"
                "系统要求 macOS 10.13 或更新。文件里的插图是重绘的示意图（红框加编号标出该点哪里），不是真实截屏，"
                "所以自己的窗口长得略有差别属正常。"
            ),
            st(
                "在浏览器打开 python.org 的 3.13.7 发布页，翻到 Files 表；",
                "点「macOS 64-bit universal2 installer」，浏览器会把 pkg 存到「下载」；",
                "打开访达进「下载」，双击 pkg，出现 Install Python 窗口；",
                "Introduction 点 Continue，Read Me 再点 Continue；",
                "License 点 Continue，在滑出的框里点 Agree；",
                "若出现 Destination Select，接受默认磁盘点 Continue；",
                "Installation Type 点 Install，按提示输密码或用 Touch ID，再点 Install Software；",
                "进度条走完显示 The installation was successful，点 Close（问是否移到废纸篓就选 Move to Trash）。",
            ),
            p(
                "两个容易踩的点。第一，发布页上方那个大黄色按钮下的是 Windows 的「Python install manager」，"
                "是另一个工具，不要点；本课要的是 Files 表里的经典安装包。"
                "第二，若 macOS 拒绝打开这个文件，去「系统设置 → 隐私与安全性」，在 Security 一节点 Open Anyway；"
                "原文特意补了一句：只对从 python.org 下载的文件这么做。"
            ),
            p(
                "验证只要两条命令，都在「终端」里跑（Command + 空格，输 Terminal，回车）："
                "<code>python3 --version</code> 应回 <code>Python 3.13.7</code>；"
                "<code>pip3 --version</code> 应报告是 Python 3.13 的 pip。"
            ),
            p("出错对照（原文四条，逐条给了处理办法）："),
            tb(
                ("现象", "原因", "处理"),
                (
                    "command not found: python3",
                    "当前终端的 PATH 还没刷新",
                    "关掉终端重开一个新窗口；仍不行就双击 Python 3.13 文件夹里的 Update Shell Profile.command，再开新窗口",
                ),
                (
                    "python3 显示的是别的版本",
                    "PATH 上更前面有旧版 Python 或 Homebrew 的工具",
                    "用 which python3 看是哪一份在跑，或直接用 python3.13 调用课程这一份",
                ),
                (
                    "输 python 没反应／报错",
                    "macOS 上安装包不创建裸的 python 命令",
                    "一律用 python3 或 python3.13",
                ),
                (
                    "想卸载",
                    "pkg 没有卸载器",
                    "删「应用程序」里的 Python 3.13 文件夹、删 /Library/Frameworks/Python.framework/Versions/3.13，再清 /usr/local/bin 里的 python3.13 链接；先备份自己的项目",
                ),
            ),
            h3("1.2 IDLE-Mod：先验 tkinter，再解 Gatekeeper"),
            p(
                "IDLE-Mod 是课程改过的编辑器，本身是个独立应用，但它<b>调用你机器上已装的 Python 3.13.7</b> 跑代码；"
                "找不到这个版本就报错，不会退而求其次用别的版本。所以装之前必须先确认 tkinter 在："
            ),
            pre('python3.13 -c "import sys, tkinter; print(sys.version)"'),
            p(
                "输出必须以 3.13.7 开头。两种失败的含义不同：报 <code>No module named '_tkinter'</code> 说明这套 Python 装的时候没带 Tk，"
                "要按安装说明重装；打印出更新的 3.13.x（例如来自 Homebrew）也不行，因为那不是课程这一份，"
                "要改用 python.org 的安装包装 3.13.7。"
            ),
            st(
                "到发布页下 macOS 版，按芯片挑：Apple Silicon（M1 及以后）下 arm64，Intel 下 intel"
                "（「苹果菜单 → 关于本机」里看 Chip 或 Processor 就知道自己是哪种）；",
                "解压得到 IDLE-Mod.app；",
                "应用没有 Apple 签名，macOS 可能说它「已损坏」，在终端跑 <code>xattr -cr ~/Downloads/IDLE-Mod.app</code>（路径按实际位置改）；",
                "把 IDLE-Mod.app 拖进「应用程序」再打开；",
                "File → New File 写程序，Cmd+S 保存，F5 运行，输出与 input() 提示都出现在 Shell 里；",
                "写完后点 Generate Submission，它会在文件旁边生成一个 .zip，把这个 .zip 交到 CodeGrade。",
            ),
            p("IDLE-Mod 的报错只有四种，记住它们的因果关系就不会乱试："),
            tb(
                ("提示", "含义", "处理"),
                (
                    "Python Interpreter Not Found",
                    "找不到 3.13.7",
                    "先装 Python 3.13.7，再跑那条 tkinter 检查命令",
                ),
                (
                    "IDLE's subprocess didn't make connection",
                    "子进程起不来，多半是 tkinter 缺失",
                    "看对话框里的输出；若提到 tkinter，就用 python.org 的安装包重装",
                ),
                (
                    "IDLE-Mod is damaged",
                    "Gatekeeper 拦了未签名应用",
                    "按安装第 3 步跑 xattr -cr",
                ),
                (
                    "旧文件生成不了提交包",
                    "文件只能在保存它的那台机器上打开",
                    "换机器就重写或重新保存，不要指望跨机打开",
                ),
            ),
            h3("1.3 Linux：版本可以松一格，Tk 不能少"),
            p(
                "Linux 说明与 macOS 有两处不同。第一，Python 只要求 3.13.x——「any patch would work i.e. 3.13.x」，"
                "不强制 3.13.7。第二，Tk 通常要单独装：报 <code>No module named '_tkinter'</code> 时要「先装 Tk 包再重编」，"
                "包名是 tk-dev 或 tk-devel。若终端说 <code>python3.13: command not found</code>，那是没在 PATH 上，加进去即可。"
            ),
            st(
                '跑同一条检查命令 <code>python3.13 -c "import sys, tkinter; print(sys.version)"</code>，输出以 3.13.x 开头；',
                "下 <code>IDLE-Mod-linux.tar.gz</code>，进到下载目录解包，再运行里面的可执行文件；",
                "File → New File，Ctrl+S 保存，F5 运行；",
                "点 Generate Submission 生成 .zip，交到 CodeGrade。",
            ),
            h3("1.4 三平台对照"),
            tb(
                ("事项", "Windows（正文第 1 讲）", "macOS", "Linux"),
                ("解释器命令", "python", "python3 或 python3.13", "python3.13"),
                ("运行快捷键", "F5", "F5", "F5"),
                ("保存快捷键", "Ctrl+S", "Cmd+S", "Ctrl+S"),
                ("提交", "Generate Submission 生成 .zip", "同左", "同左"),
                (
                    "特有坑",
                    "安装时忘了勾 Add python.exe to PATH",
                    "没有裸 python；未签名应用要先 xattr -cr",
                    "要先装 tk-dev / tk-devel",
                ),
            ),
            cal(
                "warn",
                "别在 macOS 上敲 python",
                "macOS 与多数 Linux 发行版里 <code>python</code> 要么不存在、要么指向系统的旧版本。"
                "课程的所有命令都应按平台写成 <code>python</code>／<code>python3</code>／<code>python3.13</code>，"
                "报错信息里的命令名本身就是线索。",
            ),
            h2("二、HowToUseAI：五条准则与一条硬约束"),
            p(
                "<code>HowToUseAI.pdf</code> 只有一页，五条，但它决定了你整门课的学习方式。原文逐条的意思："
            ),
            ul(
                "不要直接让 AI 给你写程序——「You will learn nothing that way」；",
                "练习题假设你已经掌握前面各章；如果一味盲用 AI，很快会完全跟不上；",
                "把 AI 当老师：学新东西时可以提问；",
                "用 AI 找错：看不懂为什么跑不通时，让 AI 解释这个错误；",
                "练习题的解答<b>只能</b>用课程教过的结构，这一点由 CodeGrade 自动检查。",
            ),
            p(
                "前四条是学习建议，第五条是硬约束，性质完全不同：前四条做不到只会让你学得慢，"
                "第五条做不到会直接判「用了课外的结构」。所以即便 AI 给了你一个用 <code>try/except/finally</code> 加列表推导的漂亮答案，"
                "只要这两样还没讲到，就不能出现在提交里。"
            ),
            cal(
                "warn",
                "这条与作业规则呼应",
                "30565 的作业页也写了同一件事的另一半：不许用 AI 写最终解答，但可以用 AI 练习与加深理解。"
                "两门课的口径一致——AI 可以用来问、用来查错、用来讲解，不能用来交作业。",
            ),
            h2("三、Extra reading：数据的二进制表示（原文注明不考）"),
            cal(
                "warn",
                "先看不考声明",
                "原文第 2 页三句话：这份材料与 Python 编程关系不大；可以读一读，对「数据在内存里长什么样」有个印象；"
                "<b>This material is not asked in EXAM</b>。所以本节只作背景，考试不从这里出题。",
            ),
            h3("3.1 ASCII 与 Unicode"),
            p(
                "计算机只处理 0 和 1 的组合，所以文字、数字、图片、音乐都必须先约定编码。"
                "ASCII 是 1960 年代定下的标准（American Standard Code for Information Interchange），"
                "把每个字符表示成一串比特：小写 a 是 01100001，大写 A 是 01000001——两者只差一个比特，"
                "这也解释了为什么大小写转换在底层很便宜。"
            ),
            p(
                "最早的 ASCII 是 7 位，只有 2⁷ = 128 个字符。今天 ASCII 已被 Unicode 取代，"
                "但 UTF-8 的前 128 个字符与 ASCII 完全一致（这就是英文文本用 UTF-8 存也不变长的原因）。"
                "Unicode 标准收录 149,186 个字符，足以覆盖世界主要字母与符号。"
            ),
            p(
                'Python 里查码点用 <code>ord()</code>，它返回十进制数：<code>ord("A")</code> 得 65，'
                '<code>ord("a")</code> 得 97，<code>ord("她")</code> 得 22905。反过来用 <code>chr()</code> 把码点变回字符。'
            ),
            h3("3.2 整数：把十进制拆成 2 的幂"),
            p(
                "十进制每一位是 10 的幂，二进制每一位是 2 的幂，最右边都是「个位」。"
                "因为每个十进制数都能唯一写成 2 的幂之和，所以整数有唯一的二进制写法："
                "50 = 32 + 16 + 2 = 2⁵ + 2⁴ + 2¹，需要的幂次位写 1、其余写 0，得 110010。"
            ),
            p(
                "<code>bin(50)</code> 返回 <code>'0b110010'</code>，前缀 <code>0b</code> 只是「这是二进制」的标记，不是数值的一部分。"
                "反过来把二进制还原成十进制，就是把为 1 的那些位对应的 2 的幂加起来。"
            ),
            h3("3.3 浮点：为什么 0.1 + 0.2 不等于 0.3"),
            p(
                "小数部分同样是 2 的幂之和，但指数是负的：2⁻¹ = 0.5、2⁻² = 0.25、2⁻³ = 0.125、2⁻⁴ = 0.0625。"
                "所以 0.5625 = 0.5 + 0.0625，二进制写作 0.1001，小数点后第一位对应 2⁻¹。"
            ),
            p(
                "问题出在 0.1：它的二进制是 0.000110011001100…，从小数点后第四位起「1100」无限循环。"
                "内存有限，只能截断成近似值——原文举例说若给小数部分 23 个比特，存下来的是 "
                "2⁻⁴ + 2⁻⁵ + 2⁻⁸ + 2⁻⁹ + 2⁻¹² + 2⁻¹³ + 2⁻¹⁶ + 2⁻¹⁷ + 2⁻²⁰ + 2⁻²¹ = 0.09999990463，"
                "已经很接近 0.1，但仍不是 0.1。两个这样的近似值相加，误差就露出来了："
                "<code>0.1 + 0.2</code> 得 <code>0.30000000000000004</code>。"
            ),
            p(
                "这不是 Python 的 bug，是二进制浮点的通病。十进制里也有同样的现象：1/3 只能写成 0.333…，"
                "截到 10 位后三个相加得 0.9999999999 而不是 1。解决办法是控制显示精度："
                "<code>round(0.1 + 0.2, 5)</code> 得 0.3，第二个参数是保留几位小数。"
            ),
            h3("3.4 内存、字节与 id()"),
            p(
                "内存是一格一格的「槽」，每格一个字节（8 比特），每格有唯一地址，地址本身就是一个大整数。"
                "程序靠地址存取数据。<code>id()</code> 返回对象在内存里的地址，对象一创建就分配，"
                "同一次运行里同一对象不变，但每次运行、每台机器都可能不同。"
            ),
            p(
                "原文的例子最能说明「变量是名字不是盒子」：<code>n = 300</code> 后 <code>id(n)</code> 是一个值，"
                "<code>m = n</code> 后 <code>id(m)</code> 与它相同（两个名字指向同一个对象）；"
                "而 <code>n = 3223</code> 之后 <code>id(n)</code> 变了——不是 300 被改成了 3223，而是 n 改指向了新对象。"
                "这一点在第 8 讲讲可变与不可变时还会再遇到。"
            ),
            cal(
                "tip",
                "原文没有讲补码",
                "这份 Extra reading 只讲到 ASCII/Unicode、整数与浮点的二进制、内存地址，"
                "<b>没有</b>涉及负数在计算机里的表示（补码 / two's complement）。"
                "按原文范围复习即可，不必去找原文没有的内容；若考试出现，也只可能作为课堂口头补充。",
            ),
            h2("四、课程项目：汽车租赁管理系统"),
            p(
                "<code>Project instructions Car rental management system.html</code> 是这门课唯一一份项目说明书，"
                "信息密度很高：四个数据文件的字段、菜单的四个操作、每条校验规则、代码约束、提交时间、评分与补交、抄袭判定，全部写在这一页里。"
            ),
            h3("4.1 开工前要熟的七个概念"),
            p(
                "原文列了七条，都是课程已经讲过的：<code>print</code> 输出、<code>input</code> 读入、"
                "<code>def</code> 定义函数、<code>while</code> 显示菜单、<code>for</code> 遍历列表、"
                "文件读写、<code>datetime</code> 处理日期。配套的复习材料有三份："
                "<code>Project work concepts recap.pptx</code>（提取到三张幻灯：标题页、七条概念清单、「回去补课」的提醒）、"
                "<code>project_work_concepts.py</code>（一个待办清单管理器，把菜单循环、文件读写、文本转日期三件事串起来）、"
                "以及一段同名讲解视频。"
            ),
            p(
                "<code>project_work_concepts.py</code> 值得逐行读一遍，它用注释把每个函数对应到上面的概念编号："
                "<code>show_menu()</code> 是菜单循环（概念 1、2、4），<code>add_task()</code> 用 "
                '<code>datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()</code> 把输入串变成日期对象（概念 7），'
                "<code>view_tasks()</code> 用 <code>enumerate(tasks, start=1)</code> 编号打印（概念 5）。"
                '项目里的日期格式是 <code>DD/MM/YYYY</code>，把格式串换成 <code>"%d/%m/%Y"</code> 就是同一套写法。'
            ),
            h3("4.2 四个数据文件与字段"),
            p(
                "四个文件都是纯文本、逗号分隔、一行一条记录。原文用一张表说明了「谁只读、谁会变」："
            ),
            tb(
                ("文件", "存什么", "程序会不会改它"),
                ("vehicles.txt", "公司拥有的车", "不会，只读"),
                ("customers.txt", "所有租过车的客户", "会，新客户追加到末尾"),
                (
                    "rentedVehicles.txt",
                    "当前还没还车的租借",
                    "会，追加新行、删除已还的行",
                ),
                ("transactions.txt", "已经结束的租借", "会，追加新行"),
            ),
            p(
                "<b>vehicles.txt</b>（每行一辆车）：1 车牌号（如 FRO-377，是这辆车的标识）；2 车型（如 Toyota Yaris Cross）；"
                "3 日租金，欧元整数（如 68），用来算租金；4 起是车辆属性（如 Air Conditioning、Hybrid、Automatic Transmission）。"
                "一辆车至少有一个属性，可以有好几个，所以<b>不同行的字段数不一样</b>——程序必须能处理任意个属性，"
                "不能写死成 6 列。"
            ),
            p(
                "<b>customers.txt</b>（每行一位客户）：1 出生日期（如 14/03/1998），它同时是这位客户的<b>标识</b>；"
                "2 名；3 姓；4 邮箱。原文特别声明「No two customers have the same birthdate」——现实里当然不成立，"
                "但这个「小世界」里成立，于是可以用生日找客户。姓名必须大写字母开头且不能以数字开头，"
                "所以 janne 与 11john 都不合法，而 Xenon12 合法（首字母大写、后面可以有数字）。"
                "客户只增不删。"
            ),
            p(
                "<b>rentedVehicles.txt</b>（每行一次尚未结束的租借）：1 车牌；2 租车人的出生日期；3 起租时刻（如 14/10/2026 12:33）。"
                "租出时追加一行，归还时删掉那一行，所以文件里只有「在租」的记录，同一辆车最多出现一次。"
            ),
            p(
                "<b>transactions.txt</b>（每行一次已结束的租借）：1 车牌；2 客户生日；3 起租时刻；4 归还时刻；"
                "5 租期天数；6 租金（欧元，永远两位小数）。归还时追加一行。"
            ),
            h3("4.3 四个文件的格式纪律"),
            ul(
                "字段之间用逗号，<b>逗号两边不留空格</b>；",
                '每一行以换行符 <code>"\\n"</code> 结尾，<b>最后一行也要有</b>；',
                "日期写成 <code>DD/MM/YYYY</code>，时刻写成 <code>DD/MM/YYYY HH:MM</code>（24 小时制）；",
                "文件名区分大小写，必须一字不差地使用 <code>vehicles.txt</code> 等四个名字；",
                "嫌数据脏了不要硬修，重新下一份干净的起始文件即可。",
            ),
            h3("4.4 计费规则：向上取整到整天"),
            p(
                "这是整个项目唯一需要「想一下」的算术，原文写得很清楚："
                "<b>每一个开始的 24 小时都按一个整天收费</b>。示例：车在外面 4 天 8 小时 19 分，"
                "前 4 个整天已经计满，剩下的 8 小时 19 分也算一天，所以收 5 天。"
                "不到 24 小时的租借按 1 天算。"
            ),
            p(
                "租金 = 租期天数 × 该车的日租金。示例里 RUX-42 的日租金是 36，5 × 36 = 180.00，"
                "与 <code>transactions.txt</code> 里那一行完全对得上。"
            ),
            cal(
                "warn",
                "两个取整陷阱",
                "①「每开始 24 小时算一天」等价于<b>向上取整</b>，不是四舍五入、也不是向下取整；"
                "②恰好 24 小时整要算 1 天而不是 2 天——向上取整函数作用在「秒数 / 86400」上，"
                "整除时不能多加 1。这两种情况各写一个测试用例，比事后调 bug 便宜。",
            ),
            h3("4.5 菜单与四个操作"),
            p(
                "程序启动先显示菜单，用户选一项，做完回到菜单，直到选 0 退出。菜单原文五项："
                "1) List available cars　2) Rent a car　3) Return a car　4) Count the money　0) Exit。"
                "输入不是这五个之一时，程序要说明并重新显示菜单——原文一句硬要求："
                "<b>The program must never crash on bad input</b>。"
            ),
            st(
                "List available cars：把 <code>vehicles.txt</code> 里<b>没有</b>出现在 <code>rentedVehicles.txt</code> 的车逐辆打印，"
                "每辆给车牌、车型、日租金、属性；",
                "Rent a car：问车牌 → 不存在或已租就报错回菜单；问生日 → 格式不合法报错回菜单；"
                "年龄必须 18 到 100 岁；生日不在 customers.txt 里就是新客户，要问名、姓、邮箱并把姓名与邮箱规则验一遍后追加；"
                "老客户直接按名字打招呼、不再问资料；最后记下当前时刻追加到 rentedVehicles.txt 并确认；",
                "Return a car：问车牌 → 不在租就报错回菜单；记下当前时刻；按 4.4 算天数与租金；"
                "从 rentedVehicles.txt 删掉那一行、往 transactions.txt 追加一行；打印「租了几天、多少钱」；",
                "Count the money：把 transactions.txt 所有租金相加，按两位小数打印总额。",
            ),
            p(
                "原文给的输出样例值得照着做，因为格式本身就在传达信息："
                "「Hello Lea」＋「You rented the car FRO-377」；"
                "「The rent lasted 5 days and the cost is 180.00 euros」；"
                "「The total amount of money is 2819.00 euros」。"
                "最后这个数字就是四个起始文件算出来的总额，程序跑通后应当与它一致。"
            ),
            h3("4.6 输入校验清单"),
            tb(
                ("输入", "规则", "不合法时"),
                ("车牌", "必须存在于 vehicles.txt，且当前未租出", "告知并回菜单"),
                ("生日", "必须是 DD/MM/YYYY 的合法日期", "告知并回菜单"),
                ("年龄", "18 ≤ 年龄 ≤ 100", "告知并回菜单"),
                ("名 / 姓", "首字母大写，不能以数字开头", "告知并回菜单"),
                ("邮箱", "必须含 @，且 @ 之后至少有一个 .", "告知并回菜单"),
            ),
            h3("4.7 代码要求与提交"),
            ul(
                "整个程序写在<b>一个</b>文件 <code>project.py</code> 里，并且要用 IDLE-Mod 写；",
                "只能用课程讲过的结构与模块（见 4.1 的七条），CodeGrade 会自动检查；日期时间一律用 <code>datetime</code>；",
                "每次需要数据就<b>重新读文件</b>，每次改动<b>立刻写回</b>，保证文件始终反映当前状态；",
                "必须能处理四个文件的<b>任意合法内容</b>，不能只对样例数据正确——助教会拿自己的数据测；",
                "按功能拆成名字清楚的函数，不直观的地方写注释。",
            ),
            p(
                "提交到 CodeGrade，截止 <b>2026 年 11 月 16 日（周一）23:59</b>。没有自动打分器给你的程序打分，"
                "但 CodeGrade 会先做两项预检：文件检查（必须叫 <code>project.py</code> 且由 IDLE-Mod 产出）"
                "与代码结构检查（只用了课内结构）。"
            ),
            h3("4.8 评分与补交"),
            p(
                "助教按一张「必备功能清单」逐项核对，满分 100，等级换算如下：90 分及以上 5 级、80 及以上 4 级、"
                "70 及以上 3 级、60 及以上 2 级、50 及以上 1 级、低于 50 本轮被拒。"
                "被拒的项目要在 <b>2026 年 12 月 4 日（周五）23:59</b> 前改好重交，"
                "重交最高只能拿 3 级；第一轮拿 1 级或 2 级的项目也允许重交。"
            ),
            h3("4.9 抄袭：改名骗不过去"),
            p(
                "原文把抄袭（plagiarism）定义为「把别人的工作、想法、代码或解答当作自己的，且不给出恰当的出处」，"
                "并说明四条机制：所有项目都会用 CodeGrade 的查重工具互相比对；<b>改变量名和函数名没用</b>；"
                "每次提交都带 IDLE-Mod 加上的识别指纹，所以提交别人的代码会被认出来；"
                "系统<b>分不清谁抄谁</b>，所以查重分高的提交一律同样处理、当轮作废，并上报学校相关部门。"
                "结论很直接：不要把代码发给别人。"
            ),
            h3("4.10 起始数据的实际规模"),
            p(
                "把四个文件数一遍，可以当作自己程序的第一个回归测试基准：<code>vehicles.txt</code> 有 17 辆车、"
                "<code>customers.txt</code> 有 12 位客户、<code>rentedVehicles.txt</code> 有 6 条在租、"
                "<code>transactions.txt</code> 有 8 条成交记录。8 条租金分别是 395、102、180、592、704、576、176、94，"
                "加起来正好 2819.00，与说明书里的样例总额一致。"
                "如果你的 Count the money 打印出别的数，先查这四件事：漏读了最后一行（没有换行符的行）、"
                "把两位小数当成字符串相加、把 94.00 读成 9400、或把在租的那 6 条也算进去了。"
            ),
            h2("五、Tutorial instructors：答疑时间表"),
            p(
                "<code>Tutorial instructors.html</code> 是行政页，只列两个校区的答疑时段与当值助教，"
                "不含任何编程内容。它的用处是「卡住时找谁」："
            ),
            ul(
                "<b>Lappeenranta</b>：周一 16–18 Namondo；周二 8–10 Rose、12–14 Vladislav、14–16 Namondo；"
                "周三 8–10 Rose、12–14 Vladislav、16–18 Máté；周四 8–10 Kanishka、14–16 Nabiha、16–18 Artúr；"
                "周五 8–10 Máté、10–12 Nabiha、12–14 Artúr、14–16 Kanishka；",
                "<b>Lahti</b>：周二 12–14 Fabiha、14–16 Hamidur；周三 8–10 Rareș、14–16 Hamidur、17–19 Cristian；"
                "周四 8–10 Cristian、16–18 Fabiha；周五 8–10 Rareș、10–12 Lilla、14–16 Lilla。",
            ),
            p(
                "用法上只有一条建议：带着具体问题去，最好带上那段跑不通的代码与报错原文。"
                "「帮我看看哪里错了」和「这段 for 循环里 i 的值为什么第二次就是 3」，后者五分钟能解决。"
            ),
        ]
    ),
    # ------------------------------------------------------------------ keywords
    kws=kw(
        (
            "installer",
            "安装包",
            "python-3.13.7-macos11.pkg is the official installer for macOS.",
        ),
        (
            "universal2",
            "通用二进制",
            "One installer that runs on both Intel and Apple Silicon Macs.",
        ),
        (
            "PATH",
            "可执行文件搜索路径",
            "If python3 is not on the PATH, the shell says command not found.",
        ),
        (
            "tkinter",
            "Tk 图形库",
            'IDLE-Mod needs tkinter; check it with python3.13 -c "import tkinter".',
        ),
        (
            "Gatekeeper",
            "macOS 的签名检查",
            "An unsigned app may be reported as damaged; clear it with xattr -cr.",
        ),
        (
            "IDLE-Mod",
            "课程定制编辑器",
            "Write the file, press F5, then click Generate Submission.",
        ),
        (
            "CodeGrade",
            "提交与查重平台",
            "Submit project.py as the .zip produced by IDLE-Mod.",
        ),
        (
            "menu-driven",
            "菜单驱动",
            "The program shows a menu until the user chooses 0.",
        ),
        ("main key", "主键 / 标识", "The birthdate is the identifier of a customer."),
        ("daily rate", "日租金", "Price = rental days × daily rate."),
        (
            "rental duration",
            "租期",
            "Every started 24-hour period counts as one full day.",
        ),
        ("round up", "向上取整", "4 days 8 hours is billed as 5 days, not 4."),
        (
            "two decimal places",
            "两位小数",
            "Prices are always printed with two decimals, e.g. 180.00.",
        ),
        (
            "ASCII",
            "美国信息交换标准码",
            "Lowercase a is 01100001, uppercase A is 01000001.",
        ),
        (
            "UTF-8",
            "Unicode 的一种编码",
            "The first 128 characters of UTF-8 match ASCII.",
        ),
        ("plagiarism", "抄袭", "Renaming variables does not hide copied code."),
    ),
    # ------------------------------------------------------------------ examples
    examples="\n".join(
        [
            qa(
                "例 1 · Mac 上 python3 版本不对，怎么一步步定位",
                p(
                    "情形：装完 python-3.13.7-macos11.pkg，敲 <code>python3 --version</code> 却显示 Python 3.11.x。"
                ),
                p("<b>诊断顺序</b>（不要直接重装，重装通常解决不了 PATH 顺序问题）："),
                p(
                    "第一步，确认装上了没有：<code>python3.13 --version</code>。"
                    "如果这条给出 3.13.7，说明安装本身成功，问题只在「py3 这个名字指到了别人」。"
                ),
                p(
                    "第二步，看是谁在抢这个名字：<code>which python3</code>。"
                    "若路径落在 /opt/homebrew/bin 或 /usr/local/bin 下，那就是 Homebrew 或旧版装的副本排在前面。"
                ),
                p(
                    "第三步，按用途选择：只是自己跑程序，直接把命令写成 <code>python3.13</code>；"
                    "要让 IDLE-Mod 找到解释器，它自己会找 3.13.7，不用改 PATH。"
                ),
                p(
                    "<b>为什么不能靠重装解决</b>：安装包只会把 3.13.7 放到 /Library/Frameworks 下并建链接，"
                    "不会改动你已有的 PATH 顺序。原文给的处理也是「用 which python3 看是哪一份在跑，或直接调用 python3.13」，"
                    "并没有让你重装。"
                ),
                p(
                    "<b>若连 python3.13 都说 command not found</b>：先关掉终端重开（PATH 只在开窗口时读一次）；"
                    "仍不行就双击 Python 3.13 文件夹里的 Update Shell Profile.command，再开新窗口。"
                ),
            ),
            qa(
                "例 2 · IDLE-Mod 报「is damaged」",
                p("情形：双击 IDLE-Mod.app，macOS 弹窗说它已损坏，应该移到废纸篓。"),
                p(
                    "<b>解：</b>这不是文件真的坏了，是 Gatekeeper 对未签名应用的默认反应。"
                ),
                p(
                    "第一步，在终端跑 <code>xattr -cr ~/Downloads/IDLE-Mod.app</code>："
                    "<code>-c</code> 清除全部扩展属性、<code>-r</code> 递归处理包内所有文件，"
                    "把「来自网络」的标记与隔离属性一并去掉。路径按 app 的实际位置改；若已拖进应用程序，就写 /Applications/IDLE-Mod.app。"
                ),
                p("第二步，重新打开应用。"),
                p(
                    "<b>仍然打不开时</b>，再分两种：若是系统设置里被拦（提示「无法打开，因为无法验证开发者」），"
                    "去「隐私与安全性」点 Open Anyway；若提示是「Python Interpreter Not Found」，"
                    "那就不是签名问题而是版本问题，回到 tkinter 检查那一步。"
                ),
                p(
                    "<b>要点：</b>三种报错指向三件不同的事——damaged 指签名、Interpreter Not Found 指版本、"
                    "subprocess didn't make connection 指 tkinter。先读提示原文再动手，别一律重装。"
                ),
            ),
            qa(
                "例 3 · 算一次归还：从在租到成交",
                p(
                    "情形：<code>rentedVehicles.txt</code> 里有一行 <code>YLE-814,08/12/1965,14/10/2026 12:33</code>，"
                    "该车日租金 85。客户在 19/10/2026 22:20 还车。求租期天数与租金，并写出要追加到 transactions.txt 的那一行。"
                ),
                p(
                    "<b>解：</b>第一步，算实际时长。14/10 12:33 到 19/10 12:33 正好 5 个整天；"
                    "再走到 22:20 是 9 小时 47 分，所以总时长 5 天 9 小时 47 分。"
                ),
                p(
                    "第二步，套「每开始 24 小时算一天」：前 5 个整天计 5 天，剩下的 9 小时 47 分是「已开始但未满」的第 6 个 24 小时，"
                    "也要计 1 天，所以租期 = 6 天。"
                ),
                p("第三步，租金 = 6 × 85 = 510，写成两位小数 510.00。"),
                p(
                    "第四步，写成交行：车牌、客户生日、起租时刻、归还时刻、天数、租金，六个字段逗号分隔、不加空格："
                ),
                pre("YLE-814,08/12/1965,14/10/2026 12:33,19/10/2026 22:20,6,510.00"),
                p(
                    "<b>顺手验算总额</b>：原 transactions.txt 合计 2819.00，加这一行就是 3329.00；"
                    "Count the money 之后应当打印这个数。"
                ),
                p(
                    "<b>易错：</b>把天数算成 5（向下取整）会让租金少 85；把起租时刻抄成归还时刻会让天数为 0 却被当成 1 天。"
                    "两处都要用 datetime 相减算，不要手数日历。"
                ),
            ),
            qa(
                "例 4 · 为什么 0.1 + 0.2 不是 0.3，怎么处理",
                p(
                    "情形：<code>print(0.1 + 0.2)</code> 输出 <code>0.30000000000000004</code>。"
                ),
                p(
                    "<b>解：</b>0.1 的二进制是 0.000110011001100…，小数点后第四位起「1100」无限循环。"
                    "内存放不下无限位，只能截断成近似值（原文按 23 位小数举例，得到 0.09999990463）。"
                    "两个近似值相加，误差就显出来了，于是结果比 0.3 大一点点。"
                ),
                p(
                    "处理方式取决于用途。只是显示：<code>round(0.1 + 0.2, 5)</code> 得 0.3，第二个参数是保留几位小数。"
                    '要按货币输出：用格式串 <code>f"{value:.2f}"</code> 得到两位小数，这也是项目里租金必须两位小数的做法。'
                ),
                p(
                    "要判断相等：不要写 <code>a == b</code>，改成「差值足够小」，例如 <code>abs(a - b) &lt; 1e-9</code>。"
                ),
                p(
                    "<b>要点：</b>这不是 Python 的 bug，十进制里 1/3 截断后三个相加也不等于 1。"
                    "凡是涉及小数比较或金额显示，都要主动控制精度。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ practice
    practice="\n".join(
        [
            p(
                '<b>练习 1</b>　在 Linux 上跑 <code>python3.13 -c "import sys, tkinter; print(sys.version)"</code> 报 '
                "<code>No module named '_tkinter'</code>。按原文，下一步该做什么？为什么不是重装 IDLE-Mod？"
            ),
            det(
                "参考答案与思路",
                p(
                    "这说明这套 Python 编译时没有带 Tk。原文的处置是「rebuild it, with the Tk package installed first」，"
                    "对应的包名是 tk-dev 或 tk-devel。IDLE-Mod 只是调用你机器上的 Python，"
                    "它自己不带 Tk，所以重装 IDLE-Mod 不会让 tkinter 出现——问题在解释器，不在编辑器。"
                ),
            ),
            p(
                "<b>练习 2</b>　给项目的邮箱校验写一份判定规则，并用 4 个例子验证（至少一个通过、一个不通过）。"
            ),
            det(
                "参考答案与思路",
                p(
                    "规则两条同时成立才算合法：①含 <code>@</code>；②<code>@</code> 之后至少有一个 <code>.</code>。"
                    "例：<code>lea.moreau@gmail.com</code> 通过（有 @，@ 后有 .）；"
                    "<code>lea.moreau.gmail.com</code> 不通过（没有 @）；"
                    "<code>lea@localhost</code> 不通过（@ 后没有 .）；"
                    "<code>lea@@gmail.com</code> 依原文规则仍算通过（有 @，@ 后有 .）——"
                    "这说明原文的规则是最小校验，不是完整 RFC 校验。写代码时按原文这条最小规则即可，不要自行加严。"
                ),
            ),
            p(
                "<b>练习 3</b>　某车日租金 47，起租 08/10/2026 16:40，归还 12/10/2026 09:10。求天数、租金，并说明若误用「向下取整」会差多少。"
            ),
            det(
                "参考答案与思路",
                p(
                    "08/10 16:40 → 12/10 16:40 是 4 个整天；实际归还早于 16:40，所以总时长 3 天 16 小时 30 分。"
                    "按每开始 24 小时算一天：3 个整天 + 已开始的第 4 个 24 小时 = 4 天。"
                    "租金 4 × 47 = 188.00。若向下取整得 3 天、141.00，少收 47（正好一天）。"
                ),
            ),
            p(
                "<b>练习 4</b>　为什么「把变量名改成 a1、b2」躲不过抄袭检测？原文给了哪两条互相独立的机制？"
            ),
            det(
                "参考答案与思路",
                p(
                    "两条机制：①CodeGrade 的查重工具把所有提交互相比对，比的是结构而不是名字，改名不影响相似度；"
                    "②每次提交都带 IDLE-Mod 生成的识别指纹，所以「提交别人的文件」会被直接认出。"
                    "再加上原文那句「系统分不清谁抄谁，查重分高的一律同样处理」，所以分享代码的风险是双向的。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ exam
    exam="\n".join(
        [
            cal(
                "exam",
                "必考",
                p(
                    "① 四个数据文件的字段顺序与「谁会变、谁只读」；"
                    "② 租期按「每开始 24 小时算一天」的算法与两位小数输出；"
                    "③ 菜单循环 + 坏输入不崩（这是评分清单里最基础的一项）；"
                    "④ 只能用课内结构（CodeGrade 自动查）；"
                    "⑤ 文件读写时机：每次要数据就重读，每次改动立刻写回。"
                ),
            ),
            cal(
                "warn",
                "易错",
                p(
                    "① 把 vehicles.txt 写死成 6 列（属性个数是可变的）；"
                    '② 用 <code>"%Y-%m-%d"</code> 解析 <code>DD/MM/YYYY</code> 的日期（应 <code>"%d/%m/%Y"</code>）；'
                    "③ 天数向下取整或四舍五入；"
                    "④ 删除 rentedVehicles.txt 的行时留下空行，导致下一行读成空记录；"
                    '⑤ 用 <code>open(..., "w")</code> 追加（会清空文件，追加要用 <code>"a"</code>）；'
                    "⑥ 租金打印成 <code>180.0</code> 或 <code>180</code> 而不是 <code>180.00</code>；"
                    "⑦ 只对样例数据正确，助教换数据就崩。"
                ),
            ),
            cal(
                "tip",
                "进阶",
                p(
                    "① 把「读文件 → 列表 → 写回文件」抽成一组小函数，主流程只剩菜单与分支，这样助教一眼能看出结构；"
                    "② 写一个自测脚本：把起租时刻设成固定值、批量跑几个边界（0 分钟、23:59、整 24 小时、100 岁、18 岁），"
                    "不依赖真实时间；"
                    "③ 老客户识别只查生日一个字段即可，不要拿姓名做联合主键（原文说生日唯一）；"
                    "④ 把 <code>datetime.now()</code> 的结果格式化成 <code>DD/MM/YYYY HH:MM</code> 再写文件，"
                    "保证文件里永远是文件格式而不是对象字符串。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ checklist
    checklist="\n".join(
        [
            p("交项目之前，按顺序过一遍这十条；每一条都能在原文里找到出处："),
            st(
                '环境：<code>python3.13 -c "import sys, tkinter; print(sys.version)"</code> 输出以 3.13 开头；',
                "文件：只有一个 <code>project.py</code>，用 IDLE-Mod 写的；",
                '读取：四个文件名一字不差，读的时候按 <code>"\\n"</code> 分行并去掉每行末尾的换行；',
                '日期：用 <code>datetime.strptime(s, "%d/%m/%Y")</code> 与 <code>"%d/%m/%Y %H:%M"</code> 两种格式；',
                "天数：向上取整，且整 24 小时不多加一天；写两个用例验证；",
                '金额：<code>f"{price:.2f}"</code> 输出两位小数；',
                "校验：车牌存在且未租、生日合法且年龄 18–100、姓名首字母大写、邮箱含 @ 且 @ 后有点；",
                "写回：新增用追加模式，删除行要重写整个文件而不是留空行；",
                "健壮性：菜单里乱输、空输入、只输空格都不能崩；",
                "提交：Generate Submission 生成 .zip → CodeGrade，截止 2026-11-16 23:59；不要把代码发给同学。",
            ),
            cal(
                "tip",
                "一个自检小技巧",
                "把四个起始文件复制到另一个目录，用你的程序完整跑一遍「租一辆 → 还一辆 → 数钱」，"
                "然后比对 transactions.txt 的行数与总额是否都按预期增加了。"
                "这比只看屏幕输出可靠，因为文件才是这项作业真正的状态。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ mapping
    mapping="\n".join(
        [
            p(
                "下表把这一讲的 13 份源文件（表中 12 行，四个数据文件合并一行）逐一对到页码/章节与覆盖内容。"
                "同一份内容有两种载体的、或在不同目录重复出现的，都在备注里写明。"
            ),
            tb(
                ("文件", "页码 / 章节", "覆盖内容与备注"),
                (
                    "Installing Python 3.13.7 on macOS.pdf",
                    "p1–p4",
                    "macOS 安装：pkg 名称与大小、universal2、系统要求、8 步安装、Gatekeeper 放行、验证命令、四条报错与卸载",
                ),
                (
                    "Installing IDLE-Mod on macOS.pdf",
                    "p1–p2",
                    "tkinter 前置检查、arm64/intel 选择、xattr -cr、Cmd+S 与 F5、Generate Submission、四种报错",
                ),
                (
                    "Installing IDLE-Mod on Linux.pdf",
                    "p1–p2",
                    "与 macOS 版同一模板：3.13.x 版本放宽、tk-dev/tk-devel、tar.gz 解包、Ctrl+S、三种报错",
                ),
                (
                    "HowToUseAI.pdf",
                    "p1（单页）",
                    "五条 AI 使用准则；第五条「只能用课内结构」由 CodeGrade 检查，属硬约束",
                ),
                (
                    "Extra reading.pdf",
                    "p1–p17",
                    "ASCII 与 Unicode、ord()、整数二进制与 bin()、浮点误差与 round()、字节与 id()；<b>原文第 2 页原话：“This material is not asked in EXAM”</b>",
                ),
                (
                    "Project instructions Car rental management system.html",
                    "第 1–8 节（原文无第 7 节编号）",
                    "四个文件字段、格式纪律、计费规则、菜单与四个操作、校验规则、代码要求、提交、评分与补交、抄袭判定",
                ),
                (
                    "Project work concepts recap.pptx",
                    "slide 1–3",
                    "七条前置概念的清单与「回去补课」的提醒；重复副本：38_Project work_1_Project work concepts 目录下同名文件（仅首行 SOURCE 不同）",
                ),
                (
                    "project_work_concepts.py",
                    "全文（待办清单示例）",
                    "菜单循环 + 文件读写 + 文本转日期的可运行范例；与 pptx 是同一内容两种载体",
                ),
                (
                    "vehicles.txt / customers.txt / rentedVehicles.txt / transactions.txt",
                    "各 17 / 12 / 6 / 8 行",
                    "起始数据；transactions 的 8 条合计 2819.00，可作回归基准；四个文件在 38_Project work_3_Files for project 目录下各有一份重复副本",
                ),
                (
                    "Tutorial instructors.html",
                    "整页（行政页）",
                    "Lappeenranta 14 个时段、Lahti 10 个时段的答疑安排，无编程内容",
                ),
                (
                    "各章 Code Examples 里的 exampleN.py / L8E1–L8E5 / Example2 等",
                    "对应章节目录",
                    "章节代码示例的散件；同一份代码在「章节目录」与根目录各有一份（仅首行 SOURCE 不同），内容已由正文各讲覆盖",
                ),
                (
                    "—（本课对照）",
                    "—",
                    "本课明确「不考」的只有 Extra reading（原文原话）；安装说明与 AI 准则是操作规范，项目说明是评分依据，都不属于「不考」",
                ),
            ),
            cal(
                "tip",
                "复习顺序建议",
                "动手前看 1.1–1.4（十分钟能装完）；开项目前看第 4 节并把 4.4 的取整规则抄在纸上；"
                "考前一天只看 4.7–4.9 与第 2 节，其余都是操作细节，不在卷面上考。",
            ),
        ]
    ),
)


with io.open(PATH, encoding="utf-8") as fh:
    data = json.load(fh)

before = len(data["lectures"])
old_len = [len(x["html"]) for x in data["lectures"]]
assert not any(x["slug"] == LEC["slug"] for x in data["lectures"]), "slug 重复"
data["lectures"].append(LEC)

with io.open(PATH, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

print(
    "[ok] %s lectures %d -> %d, new html %d chars"
    % (CID, before, len(data["lectures"]), len(LEC["html"]))
)
