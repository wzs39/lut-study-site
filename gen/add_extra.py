# -*- coding: utf-8 -*-
"""补课：32632 语法专题 + 作业听说；29428 Speaking up"""

import os
import sys
import json
import io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, cal, qa, det, pre  # noqa: E402


def load(cid):
    p = os.path.join(SITE, "content", cid + ".json")
    return p, json.load(io.open(p, encoding="utf-8"))


def save(p, d):
    with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)


def upsert(d, lec):
    d["lectures"] = [x for x in d["lectures"] if x.get("slug") != lec["slug"]]
    d["lectures"].append(lec)
    d["lectures"].sort(
        key=lambda x: 0
    )  # keep insertion order; chapter grouping uses first appearance


# ---------------- 32632 语法专题 ----------------
p32, d32 = load("32632")

g = L(
    slug="l7-word-order-questions",
    tzh="第 7 讲 · Unit 1 语法专题：语序、问句与附加疑问句",
    ten="Word Order, Questions and Question Tags",
    keywords=[
        "word order",
        "statement",
        "negative sentence",
        "Wh-question",
        "Yes/No question",
        "indirect question",
        "question tag",
        "auxiliary",
        "adverb of frequency",
    ],
    files=[
        "4_UNIT 1 Building Know-how/9_Meeting 7 homework.html",
        "5_UNIT 2 Expressing Opinions/5_GRAMMAR Online Exercises.html",
    ],
    overview=(
        h2("本节定位")
        + p(
            "Meeting 7 的作业列了一整串语法项：陈述句语序、否定句、Wh- 问句、Yes/No 问句、间接问句与附加疑问句。"
            "这些是英语写作与口语的「骨架」，也是本课唯一成体系的语法单元。"
        )
        + p("学完本节你应当能够：")
        + ck(
            "按「主语 + 谓语 + 宾语 + 方式 + 地点 + 时间」排出自然语序",
            "正确使用助动词构成否定句与疑问句",
            "区分直接问句与间接问句的语序差异",
            "写出与主句人称、时态匹配的附加疑问句",
            "在演讲与会议中避免中文式语序",
        )
        + p(
            "与前后讲的衔接：第 3 讲是词汇与语法诊所，本讲把其中的「语序」单独讲透；第 5 讲图表描述、第 6 讲会议提问都会用到。"
        )
    ),
    detail=(
        h3("7.1 陈述句的基本语序")
        + p(
            "英语陈述句的默认顺序是 <b>主语 + 谓语 + 宾语</b>，状语按「方式 → 地点 → 时间」排列（Manner–Place–Time）。"
        )
        + tb(
            ("成分", "例句", "说明"),
            ("S + V + O", "The team finished the prototype.", "最基本"),
            ("+ Manner", "The team finished the prototype quickly.", "方式副词靠动词"),
            ("+ Place", "… quickly in the lab.", "地点在方式之后"),
            ("+ Time", "… in the lab last Friday.", "时间放最后"),
        )
        + cal(
            "warn",
            "中文式语序",
            "不要写 <code>Yesterday in the lab the team quickly finished it</code>。"
            "英语习惯把时间放句末；要强调时间才前置，且用逗号隔开。",
        )
        + p(
            "频率副词（always, usually, often, sometimes, rarely, never）放在实义动词前、be 动词后："
            "<code>She usually works late.</code> / <code>She is usually late.</code>"
        )
        + h3("7.2 否定句：找助动词")
        + p(
            "否定不是简单加 not，而是「助动词 + not」。有 be/情态动词就直接加；没有就借 do/does/did，实义动词回原形。"
        )
        + tb(
            ("时态/结构", "肯定", "否定"),
            ("be 动词", "He is ready.", "He is not ready."),
            ("情态动词", "They can join.", "They cannot join."),
            ("一般现在时", "She writes reports.", "She does not write reports."),
            ("一般过去时", "We tested it.", "We did not test it."),
            ("完成时", "I have finished.", "I have not finished."),
        )
        + cal(
            "warn",
            "易错",
            "<code>She doesn't writes</code> 是错的：does 已经承担了时态，实义动词必须回原形 write。",
        )
        + h3("7.3 Wh- 问句与 Yes/No 问句")
        + p(
            "Wh- 问句 = 疑问词 + 助动词 + 主语 + 实义动词？Yes/No 问句 = 助动词 + 主语 + 实义动词？"
        )
        + tb(
            ("类型", "例句", "回答方式"),
            ("Wh-（主语提问）", "Who wrote the report?", "直接给主语，不加助动词"),
            ("Wh-（宾语提问）", "What did you test?", "给宾语"),
            ("Yes/No", "Did you test the sensor?", "Yes, I did. / No, I didn't."),
        )
        + p(
            "注意主语提问的特殊性：<code>Who wrote it?</code> 里 who 就是主语，不能再借 did。"
        )
        + h3("7.4 间接问句：问句要「降级」成陈述语序")
        + p(
            "当问句嵌在 <code>Could you tell me…</code> / <code>Do you know…</code> / <code>I wonder…</code> 之后，"
            "后面的部分要用陈述语序，不再倒装。"
        )
        + tb(
            ("直接问句", "间接问句"),
            ("Where is the station?", "Could you tell me where the station is?"),
            ("When does the meeting start?", "Do you know when the meeting starts?"),
            ("Why did they cancel it?", "I wonder why they cancelled it."),
        )
        + cal(
            "tip",
            "礼貌用法",
            "间接问句在会议、邮件里更礼貌：<code>Could you tell me when the deadline is?</code>",
        )
        + h3("7.5 附加疑问句（question tags）")
        + p("规则：前肯后否、前否后肯；助动词与时态跟主句一致；主语用代词。")
        + tb(
            ("主句", "附加部分", "理由"),
            ("It is cold,", "isn't it?", "be 动词，前肯后否"),
            ("You don't mind,", "do you?", "前否后肯"),
            ("They finished,", "didn't they?", "过去时用 did"),
            ("Let's start,", "shall we?", "Let's 固定用 shall we"),
        )
        + cal(
            "warn",
            "易错",
            "<code>I am late, am not I?</code> 不自然；标准是 <code>I am late, aren't I?</code>",
        )
        + h3("7.6 把语法用进演讲与会议")
        + ul(
            "演讲开头用间接问句拉近距离：<code>Have you ever wondered how much energy a server uses?</code>",
            "图表描述用陈述语序 + 时间状语：<code>Sales rose sharply in Q3 last year.</code>",
            "会议提问优先间接问句：<code>Could you clarify what the budget covers?</code>",
            "确认信息用附加疑问句：<code>The deadline is Friday, isn't it?</code>",
        )
    ),
    kws=tb(
        ("English", "中文", "说明 / 例句"),
        ("word order", "语序", "S + V + O + Manner + Place + Time"),
        ("statement", "陈述句", "The team finished it."),
        ("negative sentence", "否定句", "did not + 动词原形"),
        ("auxiliary verb", "助动词", "do/does/did/be/have"),
        ("Wh-question", "特殊疑问句", "What did you test?"),
        ("Yes/No question", "一般疑问句", "Did you test it?"),
        ("indirect question", "间接问句", "Could you tell me where it is?"),
        ("question tag", "附加疑问句", "isn't it?"),
        ("adverb of frequency", "频率副词", "usually, never"),
        ("statement order", "陈述语序", "间接问句用陈述语序"),
    ),
    examples=(
        h2("例题 1：改正语序")
        + qa(
            "改为自然英语：<code>Last week in the lab we carefully tested three sensors.</code>",
            p(
                "方式（carefully）→ 地点（in the lab）→ 时间（last week）："
                "<code>We carefully tested three sensors in the lab last week.</code>"
            ),
        )
        + h2("例题 2：直接问句变间接问句")
        + qa(
            "<code>Where did you buy the connector?</code> 改成 <code>Could you tell me…</code> 结构。",
            p(
                "<code>Could you tell me where you bought the connector?</code>——去掉 did，动词用过去式 bought，语序回到陈述。"
            ),
        )
        + h2("例题 3：写附加疑问句")
        + qa(
            "给 <code>The report isn't finished</code> 与 <code>They will join the call</code> 加 tag。",
            p("前否后肯：<code>is it?</code>；前肯后否：<code>won't they?</code>。"),
        )
    ),
    practice=(
        h2("练习")
        + p(
            "1. 改否定：<code>She works from home.</code> / <code>They arrived early.</code>"
        )
        + det(
            "答案与思路",
            p(
                "<code>She does not work from home.</code> / <code>They did not arrive early.</code>（助动词承担时态，动词回原形）"
            ),
        )
        + p("2. 写 Yes/No 问句：<code>you / finish / the draft</code>")
        + det("答案与思路", p("<code>Did you finish the draft?</code>"))
        + p("3. 改间接问句：<code>When does the train leave?</code>")
        + det("答案与思路", p("<code>Do you know when the train leaves?</code>"))
        + p("4. 给 <code>You sent the file</code> 加 tag。")
        + det("答案与思路", p("<code>You sent the file, didn't you?</code>"))
    ),
    exam=(
        h2("考点与难点")
        + cal(
            "exam",
            "必考",
            ul(
                "否定句与疑问句的助动词选择",
                "间接问句的陈述语序",
                "附加疑问句的前后对应",
                "方式-地点-时间顺序",
            ),
        )
        + cal(
            "warn",
            "易错",
            ul(
                "doesn't + 动词加 s",
                "间接问句仍倒装",
                "I am…, am not I?",
                "时间状语放句首不加逗号",
            ),
        )
        + cal(
            "tip",
            "进阶",
            p("能在同一段演讲里交替使用直接问句、间接问句和附加疑问句，语域切换自然。"),
        )
    ),
    checklist=h2("方法清单")
    + st(
        "写句子先定主语和谓语",
        "加状语按方式-地点-时间",
        "否定先找助动词",
        "问句先判断主语提问还是宾语提问",
        "间接问句去掉倒装",
        "tag 与主句助动词、人称一致",
    ),
    mapping=h2("源文件对应")
    + tb(
        ("源文件", "位置", "覆盖内容"),
        ("9_Meeting 7 homework.html", "UNIT 1", "7.1–7.5 全部语法项与练习清单"),
        ("5_GRAMMAR Online Exercises.html", "UNIT 2", "在线语法练习入口，对应 7.2–7.4"),
    )
    + p(
        "说明：Meeting 7 作业里还包含「中国食物 quiz」的创建任务，属于课堂活动，本讲不重复展开。"
    ),
)
g["part"] = "第 2 章 词汇语法与演讲表达"
upsert(d32, g)

# ---------------- 32632 作业与听说 ----------------
a = L(
    slug="l8-assignments-listening",
    tzh="第 8 讲 · 四项作业、口语测试与课堂听说材料",
    ten="Assignments, Oral Test and Classroom Listening",
    keywords=[
        "baseline assignment",
        "elevator pitch",
        "pronunciation test",
        "presentation",
        "rubric",
        "video submission",
        "class recording",
        "vocabulary",
    ],
    files=[
        "3_Assignments/1_BASELINE ASSIGNMENT Introduction Video [DL Sep 10]/intro/intro.html",
        "3_Assignments/2_ASSIGNMENT 1 Elevator Pitch [DL Nov 5]/intro/intro.html",
        "3_Assignments/3_ASSIGNMENT 2 Pronunciation Test [DL Nov 18]/Submissions/Zishuo Wang/Online text.html",
        "3_Assignments/4_ASSIGNMENT 3 Presentation [DL Nov 27]/intro/intro.html",
        "课堂录音 2026-10-29.mp3",
        "课堂录像 2026-09-04.mp4",
    ],
    overview=(
        h2("本节定位")
        + p(
            "大学英语的成绩几乎全由四次作业构成：Baseline 自我介绍视频、Elevator Pitch、Pronunciation Test、"
            "Presentation。这一讲把四项要求、交付方式与评分关注点一次讲清，并补上课堂录音里的词汇听写。"
        )
        + p("学完本节你应当能够：")
        + ck(
            "按 Baseline 要求录一段 1–2 分钟自我介绍",
            "写出 60 秒电梯演讲的五段结构",
            "知道发音测试考什么、怎么录、交到哪里",
            "按评分表准备一次 5–8 分钟工程演讲",
            "听懂并拼写课堂听写的 10 个工程高频词",
        )
    ),
    detail=(
        h3("8.1 Baseline：自我介绍视频（DL Sep 10）")
        + p(
            "任务：录一段 1–2 分钟英文自我介绍，说明姓名、背景、专业、为什么选 LUT、这门课想获得什么。"
            "重点是「可听懂、结构清楚」，不是口音完美。"
        )
        + tb(
            ("段落", "内容", "时长"),
            ("Opening", "Hello, I'm … I'm from …", "10 秒"),
            ("Background", "本科专业、做过什么项目", "30 秒"),
            ("Motivation", "为什么来芬兰 / LUT", "20 秒"),
            ("Goal", "这门课想练什么", "15 秒"),
            ("Closing", "Thank you.", "5 秒"),
        )
        + cal(
            "warn",
            "常见失分",
            "照稿念、镜头只拍头顶、背景噪音大、超时。手机横屏、光线在正面、先录一遍听回放。",
        )
        + h3("8.2 Assignment 1：60 秒电梯演讲（DL Nov 5，Meeting 11 现场）")
        + p(
            "电梯演讲是「我是谁 + 我能带来什么价值」的 60 秒版本，芬兰面试常以 Tell us about yourself 开头。"
        )
        + st(
            "Hook：一句让人想听下去的话（项目/问题）",
            "Who：你的专业与身份",
            "Value：你能解决什么问题（用动词与数字）",
            "Proof：一个具体项目或成果",
            "Ask：你希望对方做什么（实习/合作/提问）",
        )
        + p(
            "结构示例：<code>I build embedded systems that cut energy use. In my last project I reduced idle power by 18%. I'm looking for a summer trainee role in automation.</code>"
        )
        + cal(
            "tip",
            "训练法",
            "写好 120 词稿 → 计时朗读 → 删到 90 词 → 只留关键词卡片 → 每天对镜练 3 遍。不要背到像念稿。",
        )
        + h3("8.3 Assignment 2：发音测试（DL Nov 18）")
        + p(
            "作业页只给了提交入口：录制视频并提交链接（示例提交为 YouTube 链接）。"
            "评分关注：元音长短、辅音（th / v / w）、单词重音、句子节奏与可理解度。"
        )
        + tb(
            ("考点", "练习方法"),
            ("元音长短", "ship /ʃɪp/ vs sheep /ʃiːp/ 最小对立对"),
            ("th", "think /θ/ vs this /ð/，咬舌不咬唇"),
            ("v / w", "very vs wary，上齿轻触下唇"),
            ("单词重音", "PHOtograph vs phoTOgraphy"),
            ("句子节奏", "重读实词、弱读冠词与介词"),
        )
        + cal(
            "warn",
            "提交前",
            "确认视频能公开访问（unlisted 即可），链接粘在 Online text 里；不要上传超大附件。",
        )
        + h3("8.4 Assignment 3：工程演讲（DL Nov 27）")
        + p(
            "5–8 分钟，讲一个工程主题，必须有幻灯片与至少一张图表。评分通常看：结构、图表解读、语言准确度、"
            "互动与问答。"
        )
        + tb(
            ("部分", "要求"),
            ("Opening", "问题或数据开场，给出路线图"),
            ("Body", "3 个要点，每点一个证据/图表"),
            ("Chart", "读趋势 → 给原因 → 给结论"),
            ("Closing", "总结 + 一个行动建议"),
            ("Q&A", "用间接问句确认问题，再回答"),
        )
        + p(
            "图表句型：<code>As you can see, X rose by 20% between 2024 and 2025.</code> / "
            "<code>There was a sharp drop in Q2, mainly because…</code>"
        )
        + h3("8.5 课堂录音与录像：词汇听写")
        + p(
            "课堂录音（2026-10-29，39 秒）是一段工程词汇听写，10 个词都配有例句。原音频里 technician 被读成 "
            "<code>technican</code>，正确拼写是 technician，注意 -ician 结尾。"
        )
        + tb(
            ("单词", "中文", "例句"),
            ("visual", "视觉的", "I need a visual plan to understand."),
            ("feasible", "可行的", "The plan is not feasible."),
            ("inconsistent", "不一致的", "The test results are inconsistent."),
            ("function", "功能；函数", "We added a poor function."),
            ("verification", "验证", "Management verification is required."),
            ("materials", "材料", "We only use renewable materials."),
            ("technician", "技术员", "Two technicians practised in the training."),
            ("manufacturer", "制造商", "The components are manufactured in Finland."),
            ("sketch", "草图", "The initial sketch was very unclear."),
            ("design tool", "设计工具", "SolidWorks is my preferred design tool."),
        )
        + p(
            "课堂录像（2026-09-04，46 MB）是第一次课的完整录屏，可用于回看自我介绍与发音示范；"
            "文件较大，不建议放进离线包，按需在本地播放。"
        )
    ),
    kws=tb(
        ("English", "中文", "说明"),
        ("baseline assignment", "基线作业", "自我介绍视频"),
        ("elevator pitch", "电梯演讲", "60 秒自我推介"),
        ("pronunciation test", "发音测试", "录视频提交链接"),
        ("presentation", "演讲", "5–8 分钟 + 幻灯片"),
        ("rubric", "评分表", "结构/语言/图表/互动"),
        ("minimal pair", "最小对立对", "ship vs sheep"),
        ("word stress", "词重音", "PHOtograph"),
        ("verification", "验证", "management verification"),
        ("manufacturer", "制造商", "components are manufactured"),
        ("technician", "技术员", "注意 -ician 拼写"),
    ),
    examples=(
        h2("例题 1：60 秒稿压缩")
        + qa(
            "把 150 词的自我介绍压到 90 词，保留哪三样？",
            p(
                "保留：身份 + 一个可量化成果 + 一个明确请求（ask）。删掉形容词、家乡细节、课程列表。"
            ),
        )
        + h2("例题 2：图表句改写")
        + qa(
            "把 <code>The number went up.</code> 改成有数据、有时间的演讲句。",
            p(
                "<code>Energy consumption rose by 12% in 2025 compared with the previous year.</code>"
            ),
        )
        + h2("例题 3：发音自测")
        + qa(
            "录 ship / sheep、think / sink，回放判断是否区分长短音与齿间音。",
            p(
                "若 ship/sheep 听起来一样，先练 /ɪ/ 短促与 /iː/ 拉长；think 的 /θ/ 必须舌尖轻触上齿。"
            ),
        )
    ),
    practice=(
        h2("练习")
        + p("1. 写一段 80–100 词的电梯演讲稿，标出五段结构。")
        + det(
            "答案与思路",
            p("按 Hook-Who-Value-Proof-Ask 各一句；数字至少一个；结尾给明确请求。"),
        )
        + p("2. 列出你最容易混的三个最小对立对，并各写一个句子。")
        + det(
            "答案与思路", p("如 ship/sheep、think/sink、very/wary；句子要能读出对比。")
        )
        + p("3. 为你的演讲选一张图表，写三句：趋势、原因、结论。")
        + det(
            "答案与思路",
            p("趋势用 rose/fell by；原因用 because/due to；结论用 This suggests…"),
        )
    ),
    exam=(
        h2("考点与难点")
        + cal(
            "exam",
            "必考",
            ul(
                "四次作业的截止与交付方式",
                "电梯演讲五段结构",
                "图表描述三句法",
                "发音测试提交要求",
            ),
        )
        + cal(
            "warn",
            "易错",
            ul(
                "视频链接不可访问",
                "演讲超时",
                "图表只读数字不给结论",
                "technician 拼写",
            ),
        )
        + cal(
            "tip",
            "进阶",
            p("把作业 1 的稿子改写成作业 3 的开场，形成一条可复用的个人叙事线。"),
        )
    ),
    checklist=h2("方法清单")
    + st(
        "先看作业页的 DL 与提交方式",
        "写稿 → 计时 → 删词 → 卡片",
        "录音回放自评发音",
        "图表三句法：趋势-原因-结论",
        "提交后自己点开链接验证",
    ),
    mapping=h2("源文件对应")
    + tb(
        ("源文件", "位置", "覆盖内容"),
        ("Baseline intro.html", "Assignments 1", "8.1 自我介绍结构与时长"),
        ("Elevator Pitch intro.html", "Assignments 2", "8.2 五段结构与现场要求"),
        ("Pronunciation Test 提交页", "Assignments 3", "8.3 发音考点与提交方式"),
        ("Presentation intro.html", "Assignments 4", "8.4 演讲结构与图表句"),
        ("课堂录音 2026-10-29.mp3", "根目录", "8.5 十个工程词汇与例句"),
        ("课堂录像 2026-09-04.mp4", "根目录", "8.5 第一次课回看说明"),
    )
    + p(
        "说明：Pronunciation Test 没有独立的 intro 文件，只有提交记录，因此 8.3 的考点按课程发音模块与常见评分项归纳。"
    ),
)
a["part"] = "第 4 章 作业、交付与考核"
upsert(d32, a)
save(p32, d32)

# ---------------- 29428 Speaking up ----------------
p29, d29 = load("29428")
s = L(
    slug="speaking-up",
    tzh="第 2 讲 · Speaking up：遇到不当行为怎么开口",
    ten="Speaking Up: Addressing Unacceptable Behaviour",
    keywords=[
        "speaking up",
        "harassment",
        "discrimination",
        "respectful confrontation",
        "non-verbal cues",
        "bystander",
        "reporting channel",
    ],
    files=["13_Equality and Ethical guidelines/1_Speaking up_instructions_LTKY.pdf"],
    overview=(
        h2("本节定位")
        + p(
            "LUT 的平等与伦理指南里有一页 Speaking up：当你遇到歧视、骚扰或不当言论时，如何当场、私下或事后处理。"
            "这是新生数字导览里唯一的「人际安全」内容。"
        )
        + ck(
            "判断哪些行为属于不当行为",
            "用三句话开场进行私下沟通",
            "知道什么时候停止对话并走正式渠道",
            "作为旁观者能做什么",
        )
    ),
    detail=(
        h3("2.1 先稳住自己")
        + p(
            "指南第一条是 <b>Try to stay calm</b>：深呼吸、整理思路。感到 upset 是正常的，但保持 composure 才能把话说清楚。"
        )
        + p(
            "第二条是心态：指出问题<b>不是 judgement or criticism</b>，而是中性、尊重地一起找解决方案；"
            "有时只是双方对同一情境理解不同。"
        )
        + h3("2.2 开口的三句模板")
        + tb(
            ("目的", "英文原句", "中文"),
            (
                "争取私下时间",
                "Can I talk to you in private for a minute?",
                "能私下聊一分钟吗？",
            ),
            (
                "指出当下行为",
                "How do you think you're behaving right now?",
                "你觉得你现在的行为合适吗？",
            ),
            ("直接点明", "That comment was not actually nice.", "那句话其实并不友善。"),
        )
        + p(
            "三句的强度递增：先给对话空间，再让对方自省，最后直接陈述感受。按情境选择，不必三句都用。"
        )
        + h3("2.3 非语言信号")
        + ul(
            "保持平静的语调与稳定的目光接触；",
            "不要笑着说出严肃的话，避免对方误解为玩笑；",
            "选择相对私密、双方都能离开的场合；",
            "如果对方情绪升级，先结束对话，改走正式渠道。",
        )
        + h3("2.4 什么时候停止对话、走正式渠道")
        + p(
            "出现以下情况不要再自行处理：对方否认并继续、涉及肢体接触或威胁、反复发生、你是旁观者而非当事人。"
            "此时记录时间、地点、原话、在场人，向课程的 responsible teacher、学校 equality 联系人或不当时刻的 reporting channel 报告。"
        )
        + h3("2.5 作为旁观者")
        + p(
            "旁观者最有效的动作往往不是正面冲突，而是：转移话题、把当事人带离现场、事后私下支持并陪同报告。"
        )
        + cal(
            "tip",
            "边界",
            "本讲只讲沟通方法与报告路径，不评判具体个案；遇到紧急或安全风险，直接联系校园安全与应急渠道。",
        )
    ),
    kws=tb(
        ("English", "中文", "说明"),
        ("speaking up", "开口指出问题", "中性、尊重"),
        ("harassment", "骚扰", "不受欢迎的行为"),
        ("discrimination", "歧视", "基于身份的差别对待"),
        ("composure", "镇定", "stay calm"),
        ("non-verbal cue", "非语言信号", "语调、目光、距离"),
        ("bystander", "旁观者", "转移话题、陪同报告"),
        ("reporting channel", "报告渠道", "教师/平等联系人"),
    ),
    examples=(
        h2("例题 1：私下开场")
        + qa(
            "同学在小组讨论里反复打断你，怎么开口？",
            p(
                "<code>Can I talk to you in private for a minute? I noticed I couldn't finish my point twice. Could we agree on a turn-taking signal?</code>"
            )
            + p(
                "要点：描述可观察行为（打断两次），不贴标签（你没礼貌），给具体方案（轮流发言信号）。"
            ),
        )
        + h2("例题 2：直接点明")
        + qa(
            "同事开了带有地域刻板印象的玩笑，你怎么回应？",
            p(
                "<code>That comment was not actually nice. I'd prefer we keep jokes out of work topics.</code>"
            )
            + p("直接、短、不解释太多；把边界说清楚即可。"),
        )
    ),
    practice=(
        h2("练习")
        + p("1. 写出你所在文化里「沉默」通常表示什么，以及在芬兰语境可能被如何理解。")
        + det(
            "提示",
            p(
                "很多人用沉默表示保留；芬兰语境常把沉默读作「同意/可以继续」，需要主动说明。"
            ),
        )
        + p("2. 设计一句既不指责又能制止的话。")
        + det("提示", p("句式：I noticed + 具体行为 + I'd prefer + 具体请求。"))
    ),
    exam=h2("考点与难点")
    + cal(
        "exam",
        "常考",
        ul("三句开场模板", "不当行为的判断", "何时转正式渠道", "旁观者策略"),
    )
    + cal(
        "warn",
        "易错",
        ul("用玩笑语气说严肃内容", "在公开场合让对方下不来台", "只描述感受不描述行为"),
    )
    + cal("tip", "进阶", p("把「行为-影响-请求」三步说清，比争论动机更有效。")),
    checklist=h2("方法清单")
    + st(
        "先稳住情绪",
        "选私下场合",
        "描述具体行为与影响",
        "提出可执行请求",
        "无效则记录并报告",
        " bystander 先转移再陪同",
    ),
    mapping=h2("源文件对应")
    + tb(
        ("源文件", "页码", "覆盖内容"),
        ("1_Speaking up_instructions_LTKY.pdf", "p1", "2.1–2.5 全部要点与三句模板"),
    )
    + p(
        "说明：原文为单页英文信息图，本讲按原句重组并补充了报告渠道与旁观者策略的说明。"
    ),
)
s["part"] = "第 2 章 平等与伦理"
upsert(d29, s)
save(p29, d29)
print("ok", len(d32["lectures"]), len(d29["lectures"]))
