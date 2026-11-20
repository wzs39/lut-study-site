# -*- coding: utf-8 -*-
import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
    badge,
    qa,
    det,
    pre,
    code,
    chips,
)


def Q(*a):
    if len(a) == 1:
        s = a[0]
        i = s.find("<p>")
        return qa(s[:i], s[i:])
    return qa(a[0], "".join(a[1:]))


def D(*a):
    if len(a) == 1:
        s = a[0]
        i = s.find("<p>")
        return det(s[:i], s[i:])
    return det(a[0], "".join(a[1:]))


LEC = []

# ============================================================ 1
OV1 = (
    h2("本节定位")
    + p(
        "KE00BX35 English Pronunciation 是一门 1 学分、约 27 小时的自主进度课程（课程说明的算法是「每天一小时，一个月」）。它只有四个学习目标：把音素发清楚、把词与句的重音放对、用停顿与语调制造效果、听懂不同口音。第一讲先把课程的运作方式与考核规则讲清，再进入第一个目标的技术底座：<b>音素与 IPA</b>。"
    )
    + p(
        "本讲同时把课程自带的 <b>Pronunciation task</b> 词表读成一份完整的辅音清单——那张表不是让你背单词，而是让你按目标音把词归类，从而听出 /s/ 与 /z/、/ʃ/ 与 /tʃ/、/θ/ 与 /ð/、/v/ 与 /w/ 的区别。"
    )
    + p("学完本讲你应当能够：")
    + ck(
        "说清课程的通过条件、两次录音任务与两个学期的截止日期",
        "区分字母与音素，用斜杠标音位、用方括号标实际音",
        "说出辅音的三个描写维度：声带振动、发音部位、发音方式",
        "把 Pronunciation task 的词按 12 个目标音正确归类，并解释容易混的词",
        "用最小对立对（minimal pair）做听辨与产出训练",
        "解释词尾 -s 的三条读音规则并举例",
        "判断一次作业在 pass/fail 体系下是否算完成",
    )
)

DT1 = (
    h3("1.1 课程怎么运作：结构固定，进度自由")
    + p(
        "课程说明的第一段就把设计意图写明了：<i>This course is designed to be (1) structured and (2) self-paced. This means you are to (1) go through the course in the order given, but (2) you may study the material as slow or fast as you like.</i> 顺序不能乱，速度可以自己定。"
    )
    + p(
        "课程名 English Pronunciation，1 ECTS，预计工作量约 27 小时（说明里给的换算很形象：<i>a month at one hour per day</i>）。教师是 Marianna Kivistö。技术条件：内容在 Firefox 与 Google Chrome 下测试通过；录音可用任何设备与软件，不确定就用 Vocaroo，录好后上传 Moodle。"
    )
    + p(
        "还有一条容易被忽略的操作规则：<i>REMEMBER ALWAYS CLICK THE MARK AS DONE-BUTTON AFTER FINISHING A TASK, THIS IS HOW YOU CAN PROGRESS FURTHER.</i> 每个任务完成后都要点 Mark as Done，否则后续内容不会解锁。这不是形式，而是这门课唯一的「进度机制」。"
    )
    + p(
        "如果某个作业没有明确要求录音，你可以自己决定交音频还是交文字：<i>If it is not mentioned as part of an assignment that you need to record (= audio file) your answer, you can decide whether you want to send an audio or a text file.</i>"
    )
    + h3("1.2 课程的核心设计：同一段话录两次")
    + p(
        "整门课最值得理解的设计是这句：<i>The highlight of the course is recording the same speech twice: first without studying the contents of the course and then again at the very end of the course after you have studied the contents.</i>"
    )
    + p(
        "第一次录音是<b>基线</b>，第二次是<b>对照</b>。两次之间发生了三件事：你学了音素、重音、语调；你练了模仿与朗读；你听了自己的录音。第二次录音只能在完成所有其他任务之后上传（<i>You can upload the second recording only after completing all other tasks</i>），这条限制保证了对比的有效性。"
    )
    + p(
        "要让对比有意义，两次录音必须控制变量：<b>同一段文本、同样的设备、同样的环境、同样的语速意图</b>。任何一项变了，进步就无法归因于学习。建议在第一次录音时就把文件命名、设备、麦克风距离记在一张纸上，结束时照抄。"
    )
    + h3("1.3 提交、反馈与截止日期")
    + tb(
        ("事项", "规则原文要点", "对你的要求"),
        (
            "提交渠道",
            "All work completed is to be uploaded on Moodle – do not send any assignments by email.",
            "全部上传 Moodle，不发邮件",
        ),
        (
            "反馈时间",
            "This occurs weekly on Monday. Allow two weeks for assessment.",
            "按两周预期，不要催",
        ),
        (
            "反馈形式",
            "You will not get comments on each audio file but a general assessment of all your work.",
            "是整体评价，不是逐条批注",
        ),
        (
            "秋季截止",
            "the fall semester deadline is on the 13th of December",
            "12 月 13 日前完成",
        ),
        (
            "春季截止",
            "Spring semester deadline is on the 18th of May",
            "5 月 18 日前完成",
        ),
        (
            "成绩登记",
            "the teacher will check your work … and enter your completion into Sisu",
            "完成后登记到 Sisu",
        ),
    )
    + h3("1.4 考核：只有 pass 与 fail")
    + p(
        "课程的评估规则短得不能再短：<i>Pass: The student has completed all required tasks according to instructions.</i> 与 <i>Fail: The student has not completed all required tasks.</i> 没有百分比，没有等级。"
    )
    + p(
        "课程还专门给交换生一段警告，值得逐句读：<i>This course does not award a number grade. The grade you receive is either pass or fail. Should you need a numerical grade, do not take this course.</i> 原因写在后面：有些母校会把 pass 折算成最低档成绩，所以选课前要问清母校的换算规则。"
    )
    + cal(
        "exam",
        "必考",
        "pass 的唯一条件是「按说明完成全部任务」。少交一个录音、漏点一次 Mark as Done、用邮件代替 Moodle，都可能被判 fail——这门课不给部分学分。",
    )
    + h3("1.5 四个目标对应四讲")
    + tb(
        ("课程目标（原文）", "本讲义对应", "可检验的表现"),
        (
            "pronounce English phonemes more clearly and correctly",
            "第 1、2 讲",
            "最小对立对能听辨、能产出",
        ),
        (
            "stress syllables and sentences more appropriately",
            "第 3 讲",
            "词重音位置正确，句重音落在信息词上",
        ),
        (
            "use pausing and intonation for effect",
            "第 4 讲",
            "能按意义切块，能用降调/升调表达态度",
        ),
        (
            "understand various dialects and manners of speaking English",
            "第 4 讲",
            "能听懂非标准口音的关键信息",
        ),
    )
    + h3("1.6 音素与字母：26 与 44 不是一回事")
    + p(
        "英语有 26 个字母，但标准口音（RP 一类）有约 44 个音素：24 个辅音加 20 个元音（12 个单元音 + 8 个双元音）。字母与音素不是一一对应，这正是要学 IPA 的原因。"
    )
    + p(
        "写法上有两条国际惯例：<b>斜杠 / /</b> 表示音位（phoneme，语言里的区别性单位），<b>方括号 [ ]</b> 表示实际发出的音（phone，带口音与语流变化）。例如 /p/ 是音位，而 <i>pin</i> 里的 [pʰ] 是送气变体。日常学习用斜杠就够了。"
    )
    + p("拼写不可靠的例子必须背下来，它们解释了为什么不能靠字母猜音：")
    + tb(
        ("拼写", "音标", "说明"),
        ("though", "/ðəʊ/", "gh 不发音，ou 读 /əʊ/"),
        ("through", "/θruː/", "gh 不发音，ou 读 /uː/"),
        ("tough", "/tʌf/", "gh 读 /f/，ou 读 /ʌ/"),
        ("cough", "/kɒf/", "gh 读 /f/，ou 读 /ɒ/"),
        ("read（现在）", "/riːd/", "同形异音"),
        ("read（过去）", "/red/", "拼写同、读音异"),
        ("use（名词）", "/juːs/", "名词清音 /s/"),
        ("use（动词）", "/juːz/", "动词浊音 /z/"),
    )
    + p(
        "最后一组 <i>use</i> 是课程词表里直接给出的考点：<i>use (verb)</i> 归到 /z/ 一栏。名词与动词靠词尾清浊区分，这在英语里是成系统的（<i>house</i> 名词 /s/、动词 /z/；<i>excuse</i> 同理）。"
    )
    + h3("1.7 描写辅音的三把尺子")
    + p(
        "任何辅音都可以用三个问题定位：<b>声带振动吗</b>（voiced / voiceless）、<b>在哪里挡气</b>（place）、<b>怎么挡、怎么放</b>（manner）。掌握这套坐标，你就能自己描述任何一个音，而不是靠模仿。"
    )
    + tb(
        ("发音部位", "英文", "清音", "浊音"),
        ("双唇", "bilabial", "/p/", "/b/ /m/ /w/"),
        ("唇齿", "labiodental", "/f/", "/v/"),
        ("齿间", "dental", "/θ/", "/ð/"),
        ("齿龈", "alveolar", "/t/ /s/", "/d/ /z/ /n/ /l/ /r/"),
        ("齿龈后", "post-alveolar", "/ʃ/ /tʃ/", "/ʒ/ /dʒ/"),
        ("硬腭", "palatal", "—", "/j/"),
        ("软腭", "velar", "/k/", "/g/ /ŋ/"),
        ("声门", "glottal", "/h/", "—"),
    )
    + tb(
        ("发音方式", "英文", "例子"),
        ("爆破音", "plosive", "/p b t d k g/"),
        ("摩擦音", "fricative", "/f v θ ð s z ʃ ʒ h/"),
        ("塞擦音", "affricate", "/tʃ dʒ/"),
        ("鼻音", "nasal", "/m n ŋ/"),
        ("边音", "lateral", "/l/"),
        ("近音", "approximant", "/r j w/"),
    )
    + cal(
        "tip",
        "三把尺子的用法",
        "说 /z/ 时问自己：声带振动吗（是）、哪里挡气（齿龈）、怎么挡（摩擦）。三个答案齐了，音就稳了。反过来，把 /z/ 说成 /s/ 通常只是第一把尺子错了——声带没振动。",
    )
    + h3("1.8 把 Pronunciation task 读成一张辅音地图")
    + p(
        "课程给的词表按 12 个目标音分组：/s/、/z/、/ʒ/、/ʃ/、/dʒ/、/tʃ/、/t/、/k/、/p/、/ð/、/θ/、/v/，另加一组 /w/。任务不是背词，而是<b>按目标音归类并读准</b>。逐组看关键词："
    )
    + tb(
        ("目标音", "词表中的词", "要点"),
        (
            "/s/",
            "seal, ice, racer, place, price, governments, computers, success",
            "清音，声带不振动；-s 在清音后读 /s/",
        ),
        (
            "/z/",
            "zeal, eyes, razor, plays, prize, use (verb)",
            "浊音；-s 在浊音后读 /z/；eyes 与 ice 只差清浊",
        ),
        (
            "/ʒ/",
            "pleasure, usual, television, azure, equation",
            "词中 -s- 常读 /ʒ/；法语借词多",
        ),
        (
            "/ʃ/",
            "shell, sheet, brochure, schedule, efficient",
            "sh、-ti-、-ci- 都可能读 /ʃ/",
        ),
        (
            "/dʒ/",
            "gin, region, technology, juice, jeep, shortage",
            "g 在 e/i/y 前常读 /dʒ/；-ge 结尾",
        ),
        (
            "/tʃ/",
            "cheap, choose, future, commercial, lunch, teacher",
            "ch、ture、-tch 常读 /tʃ/",
        ),
        ("/t/", "tea, technical, tax, capacity", "词尾 /t/ 要清楚，不要吞掉"),
        ("/k/", "come, key, capacity", "c/k/ck 都可读 /k/"),
        ("/p/", "pig, pea, plan, place", "清音送气，纸片测试会动"),
        ("/ð/", "the, then, this, further", "浊齿间音，舌尖轻触上齿"),
        ("/θ/", "thirteen, three, health, birthday", "清齿间音，不振动"),
        ("/v/", "veal, very, envy", "唇齿浊音，上齿咬下唇"),
        ("/w/", "wheel, weekend, weevil", "双唇圆拢，无摩擦"),
    )
    + cal(
        "warn",
        "最容易混的四组",
        "① <i>seal /siːl/</i> 与 <i>zeal /ziːl/</i>；② <i>ice /aɪs/</i> 与 <i>eyes /aɪz/</i>；③ <i>sheet /ʃiːt/</i> 与 <i>cheap /tʃiːp/</i>（/ʃ/ 与 /tʃ/）；④ <i>veal /viːl/</i> 与 <i>wheel /wiːl/</i>（/v/ 与 /w/）。这四组几乎覆盖了中国与芬兰学习者的全部高频混淆。",
    )
    + p(
        "几个「一词两读」的陷阱要单独记：<i>schedule</i> 英式 /ˈʃedjuːl/、美式 /ˈskedʒuːl/（词表把它放在 /ʃ/ 一栏，说明课程取英式）；<i>technology</i> /tekˈnɒlədʒi/ 的 /dʒ/ 在第三音节；<i>equation</i> /ɪˈkweɪʒən/ 的 /ʒ/ 来自 -tion 的浊化；<i>governments</i> /ˈgʌvənmənts/ 结尾是 /ts/ 两个音，不要读成 /s/ 一个音。"
    )
    + h3("1.9 最小对立对：一个音决定一个词")
    + p(
        "最小对立对（minimal pair）指两个词只有一个音位不同：<i>seal / zeal</i>、<i>ice / eyes</i>、<i>place / plays</i>、<i>price / prize</i>。它们是听辨训练的最佳材料，因为任何混淆都会直接改变词义。"
    )
    + st(
        "听辨：让别人（或录音）随机读其中一个，你判断是哪一个，记录正确率",
        "定位：错的时候问自己错在哪个特征——清浊、部位还是方式",
        "慢速产出：对着镜子或录音，把这个特征夸张地做出来（如把手放喉结感受 /z/ 的振动）",
        "常速产出：放回短语里读，如 <i>my eyes / my ice</i>，确认在语流中仍能区分",
        "复测：一周后重做同一组，正确率应上升；不上升就换更小的单位（先单音，再词）",
    )
    + h3("1.10 词尾 -s：三条规则与一个例外")
    + p(
        "词表里 <i>governments</i>、<i>computers</i>、<i>plays</i>、<i>eyes</i> 的结尾读音不同，因为 -s 的读音由前一个音决定："
    )
    + tb(
        ("前一个音", "读音", "例"),
        (
            "清辅音（/p t k f θ/ 等）",
            "/s/",
            "governments, cats, stops, months",
        ),
        ("浊辅音与元音", "/z/", "computers /kəmˈpjuːtəz/, plays, eyes, prize"),
        ("咝音（/s z ʃ ʒ tʃ dʒ/）", "/ɪz/", "places /ˈpleɪsɪz/, watches, changes"),
    )
    + p(
        "课程词表里 <i>computers</i> 与 <i>governments</i> 并排出现，正好用来对比：前者结尾是元音 + /z/，后者结尾是 /t/ + /s/，读成 /ts/ 两个音。"
    )
    + h3("1.11 常见错误与纠正方向")
    + tb(
        ("错误", "听起来像", "纠正方向"),
        ("eyes 读成 ice", "把 /z/ 读成 /s/", "手放喉结，确认振动"),
        (
            "three 读成 tree 或 free",
            "/t/ 或 /f/ 代替 /θ/",
            "舌尖伸出轻触上齿，先慢后快",
        ),
        ("then 读成 den", "/d/ 代替 /ð/", "舌尖不要顶齿龈，要轻触上齿"),
        ("very 读成 wery", "/w/ 代替 /v/", "上齿咬下唇，不要圆唇"),
        ("pleasure 读成 pledger", "/dʒ/ 代替 /ʒ/", "/ʒ/ 是摩擦音，不爆破"),
        ("sheet 读成 cheat", "/tʃ/ 代替 /ʃ/", "先发长 /ʃ/ 再滑向 /iː/，不加爆破"),
    )
    + p(
        "这些错误都不需要「多听」来解决，需要的是<b>发音动作的诊断</b>：知道错在哪个特征，就能针对那一个动作练。下一讲会把元音与辅音的细节展开。"
    )
)

KW1 = K(
    ("phoneme", "音位", "A distinct sound unit: /p/ in pin."),
    (
        "IPA",
        "国际音标",
        "The International Phonetic Alphabet, written between slashes.",
    ),
    ("voiced / voiceless", "浊音／清音", "/z/ is voiced; /s/ is voiceless."),
    ("place of articulation", "发音部位", "Bilabial, dental, alveolar, velar."),
    ("manner of articulation", "发音方式", "Plosive, fricative, affricate, nasal."),
    ("minimal pair", "最小对立对", "seal and zeal differ in one sound only."),
    ("monophthong", "单元音", "A single vowel quality: /iː/, /æ/, /ʌ/."),
    ("diphthong", "双元音", "A glide from one vowel to another: /eɪ/, /aɪ/."),
    (
        "self-paced",
        "自主进度",
        "You may study the material as slow or fast as you like.",
    ),
    ("Mark as Done", "标记完成", "Click it after every task to unlock the next one."),
    ("pass / fail", "通过／不通过", "This course gives no numerical grade."),
    (
        "baseline recording",
        "基线录音",
        "The first recording, made before studying the course.",
    ),
    ("aspiration", "送气", "The puff of air in initial /p/, /t/, /k/."),
    ("sibilant", "咝音", "/s z ʃ ʒ tʃ dʒ/ take /ɪz/ in the plural."),
    ("Vocaroo", "在线录音工具", "A free tool suggested for recording speaking tasks."),
    ("allophone", "音位变体", "The aspirated [pʰ] in pin is an allophone of /p/."),
)

EX1 = (
    Q(
        "例 1　把下列词按目标音归类，并说明其中三个「看起来不像」的词为什么归到那一栏：<i>use (verb)、schedule、efficient、technology、equation、computers、governments</i>。",
        p("<b>解：</b>逐个查音标再归类。"),
        p(
            "<i>use (verb)</i> /juːz/ → /z/：名词读 /juːs/、动词读 /juːz/，词尾清浊区分词性。"
        ),
        p(
            "<i>schedule</i> /ˈʃedjuːl/ → /ʃ/：英式读法，sch 读 /ʃ/；美式 /ˈskedʒuːl/ 则归 /k/ 与 /dʒ/，课程取英式。"
        ),
        p("<i>efficient</i> /ɪˈfɪʃənt/ → /ʃ/：-ci- 在元音前读 /ʃ/，不是 /si/。"),
        p(
            "<i>technology</i> /tekˈnɒlədʒi/ → /dʒ/：-logy 的 g 在 i 前读 /dʒ/，与 <i>logic</i> /ˈlɒdʒɪk/ 同源。"
        ),
        p(
            "<i>equation</i> /ɪˈkweɪʒən/ → /ʒ/：-tion 在元音后浊化为 /ʒ/，对比 <i>nation</i> /ˈneɪʃən/。"
        ),
        p("<i>computers</i> /kəmˈpjuːtəz/ → /z/：词尾前是元音 /ə/，故 -s 读 /z/。"),
        p(
            "<i>governments</i> /ˈgʌvənmənts/ → /s/：词尾前是 /t/，-s 读 /s/，合起来是 /ts/ 两个音。"
        ),
        p(
            "<b>通用思路：</b>先写音标（不靠拼写猜）→ 找到目标音所在位置 → 检查它前面/后面的音是否触发变读（-s、-tion、-ci-）。"
        ),
    )
    + Q(
        "例 2　解释 <i>seal</i> 与 <i>zeal</i>、<i>ice</i> 与 <i>eyes</i> 的区别，并设计一套 15 分钟的练习。",
        p(
            "<b>解：</b>两组都是清浊对立。/s/ 与 /z/ 的发音部位（齿龈）与方式（摩擦）完全相同，唯一差别是声带是否振动；<i>seal</i> /siːl/ 对 <i>zeal</i> /ziːl/，<i>ice</i> /aɪs/ 对 <i>eyes</i> /aɪz/。"
        ),
        p(
            "15 分钟方案：① 3 分钟听辨，各 10 次随机播放，记录正确率；② 4 分钟单音对比，/sː/ 与 /zː/ 各持续 3 秒，手放喉结确认振动；③ 4 分钟词对朗读，慢速 10 遍、常速 10 遍；④ 4 分钟放进短语：<i>my eyes / my ice</i>、<i>a seal / a zeal</i>，最后录音回听。"
        ),
        p(
            "<b>通用思路：</b>听辨 → 单音 → 词 → 短语，四级递进；每级都要有可量化的正确率，否则无法判断是否进步。"
        ),
    )
    + Q(
        "例 3　写出 <i>though、through、tough、cough</i> 的音标，并说明这四个词对「靠拼写读英语」提出了什么警告。",
        p(
            "<b>解：</b>/ðəʊ/、/θruː/、/tʌf/、/kɒf/。四个词都含 -ough，却有四种读音：/əʊ/、/uː/、/ʌf/、/ɒf/。"
        ),
        p(
            "警告是：<b>字母组合 ough 没有固定读音</b>，必须逐词记音标。同类还有 <i>read</i> 的两种时态、<i>use</i> 的名词与动词。"
        ),
        p(
            "实用做法：遇到 -ough、-augh、-eigh 这类组合，第一件事是查词典音标，而不是套规则。"
        ),
        p(
            "<b>通用思路：</b>拼写只提供线索，音标提供事实；对不规则组合建立「逐词记」的清单，而不是寻找通则。"
        ),
    )
    + Q(
        "例 4　判断下列情形在 pass/fail 体系下的结果，并说明依据：① 完成全部任务但有一次没点 Mark as Done；② 少交第二次录音，其他全做；③ 用邮件把最后一次录音发给老师。",
        p(
            "<b>解：</b>① 结果为 fail（或至少无法登记完成）：课程明确要求每个任务后点 Mark as Done，<i>this is how you can progress further</i>，未点等于任务未完成。"
        ),
        p(
            "② fail：第二次录音是课程的核心任务（<i>the highlight of the course</i>），且只能在完成其他任务后上传，缺它就不是「完成全部任务」。"
        ),
        p(
            "③ fail：<i>All work completed is to be uploaded on Moodle – do not send any assignments by email.</i> 邮件提交不算提交。"
        ),
        p(
            "<b>通用思路：</b>判断标准只有一条——「按说明完成全部任务」；说明里的每一条操作要求（渠道、按钮、顺序）都是通过条件。"
        ),
    )
)

PR1 = ol(
    "把 <i>pleasure、usual、television、azure</i> 四个词的 /ʒ/ 位置标出来，并各造一个短句。",
    "写出 <i>places、watches、changes、governments</i> 的词尾 -s 读音，并说明规则。",
    "用 /θ/ 与 /ð/ 各写两个词，标注舌尖位置与声带状态。",
    "选三组你最容易混的最小对立对，按五步法设计一周练习表（每天 10 分钟）。",
    "列出本课程的三个通过条件（渠道、按钮、任务完整性），并说明违反任一条的后果。",
) + D(
    "答案与思路",
    p(
        "<b>1.</b> <i>pleasure</i> /ˈpleʒə/ 的 /ʒ/ 在第二音节首；<i>usual</i> /ˈjuːʒuəl/ 的 /ʒ/ 在第二音节；<i>television</i> /ˈtelɪvɪʒn/ 的 /ʒ/ 在倒数第二音节；<i>azure</i> /ˈæʒə/ 的 /ʒ/ 在第二音节。例句：<i>It was a pleasure to meet you.</i> / <i>That’s my usual route.</i> / <i>We watched it on television.</i> / <i>The sky turned azure.</i>"
    ),
    p(
        "<b>2.</b> <i>places</i> /ˈpleɪsɪz/（前为 /s/，加 /ɪz/）；<i>watches</i> /ˈwɒtʃɪz/（前为 /tʃ/，加 /ɪz/）；<i>changes</i> /ˈtʃeɪndʒɪz/（前为 /dʒ/，加 /ɪz/）；<i>governments</i> /ˈgʌvənmənts/（前为 /t/，读 /s/）。规则：咝音后 /ɪz/，清音后 /s/，浊音与元音后 /z/。"
    ),
    p(
        "<b>3.</b> /θ/：<i>think、health</i>，舌尖轻放上下齿之间，声带不振动；/ð/：<i>this、further</i>，同样位置但声带振动。检验方法：手指轻触喉结，/ð/ 有振动，/θ/ 没有。"
    ),
    p(
        "<b>4.</b> 参考表：周一听辨 20 对（记录正确率）；周二单音各 10 次×3 秒；周三词对慢速 20 遍；周四词对常速并录音；周五放进短语；周六换一组新词复测；周日回听两次录音对比。"
    ),
    p(
        "<b>5.</b> ① 全部上传 Moodle，不发邮件（邮件提交不算提交）；② 每个任务后点 Mark as Done（否则无法解锁后续、无法登记完成）；③ 完成全部任务，包括第二次录音（缺一项即 fail）。"
    ),
)

EM1 = (
    cal(
        "exam",
        "必考",
        "约 44 个音素（24 辅音 + 20 元音）；辅音的三维度描写；/s/ 与 /z/、/ʃ/ 与 /tʃ/、/θ/ 与 /ð/、/v/ 与 /w/ 的对立；词尾 -s 的三条规则；课程的 pass/fail 条件、两次录音、两个截止日期。",
    )
    + cal(
        "warn",
        "易错 1",
        "用拼写判断读音（-ough 四种读法、use 名词 /s/ 与动词 /z/、schedule 英式 /ʃ/）。",
    )
    + cal(
        "warn",
        "易错 2",
        "/θ/ 读成 /t/ 或 /s/、/ð/ 读成 /d/；/v/ 读成 /w/；/ʒ/ 读成 /dʒ/。这些都是发音动作错，不是听力问题。",
    )
    + cal(
        "warn",
        "易错 3",
        "以为课程有数字成绩而选课，或漏点 Mark as Done、用邮件提交——纯规则性失分。",
    )
    + cal(
        "tip",
        "进阶",
        "了解音位变体：<i>pin</i> 的 [pʰ] 送气、<i>spin</i> 的 [p] 不送气，二者是同一个 /p/ 的两个变体；这解释了为什么「送气太多或太少」都还能听懂，但会带口音。",
    )
)

CL1 = (
    h2("本讲方法清单")
    + h3("最小对立对五步练习法")
    + st(
        "听辨 20 对，记录正确率",
        "定位错误特征：清浊／部位／方式",
        "单音夸张练习，借助镜子与喉结触感",
        "放回短语与句子，常速朗读并录音",
        "一周后复测同一组，正确率不升就缩小单位",
    )
    + h3("第一次录音前的四项固定")
    + ck(
        "文本固定：整门课用同一段（课程提供 Text 1 一类材料）",
        "设备固定：同一台设备、同一麦克风距离",
        "环境固定：同一房间、同一时段，减少噪声差异",
        "命名固定：文件名写清 first / final 与日期，便于对比",
    )
)
MP1 = tb(
    ("源文件", "位置 / 页码", "覆盖内容"),
    (
        "2_1. Instructions and introductions/1_Course Preamble - Read and Sign/…html",
        "全篇",
        "1 ECTS 与 27 小时、结构与自主进度、两次录音设计、提交与反馈、四个目标、pass/fail、交换生警告、两个截止日期",
    ),
    (
        "2_1. Instructions and introductions/2_Technical matters.html",
        "全篇",
        "浏览器要求、录音与视频工具、Vocaroo、只交一次、未指定时可选音频或文字、技术支持",
    ),
    (
        "2_1. Instructions and introductions_3_OneDrive_for_Business_creating_a_public_link.pdf",
        "p1–p2",
        "OneDrive 公开链接六步：登录、Share、Anyone、取消编辑权限、Copy link、贴到 Moodle",
    ),
    (
        "4_3. Phonemes, stress and intonation/2_Pronunciation task.pdf",
        "p1",
        "12 组目标音的单词表（/s z ʒ ʃ dʒ tʃ t k p ð θ v/ 与 /w/）",
    ),
    ("Pronunciation task.pdf", "p1", "同上（重复副本，内容一致）"),
    (
        "（跳过）",
        "—",
        "重复副本 OneDrive pdf 与 Pronunciation task pdf 不再单独设知识点",
    ),
    (
        "（拓展）",
        "—",
        "辅音三维度表、音位与音位变体、-s 三条规则、最小对立对五步法、第一次录音的变量控制在原文中只有任务提示，展开属教学补充",
    ),
)
LEC.append(
    L(
        slug="p1-course-ipa",
        tzh="第 1 讲 · 课程规则、音素与 IPA",
        ten="Course Rules, Phonemes and the IPA",
        keywords=[
            "phoneme",
            "IPA",
            "voiced",
            "minimal pair",
            "pass / fail",
            "baseline recording",
            "articulation",
            "sibilant",
        ],
        files=[
            "2_1. Instructions and introductions_1_Course Preamble - Read and Sign_1_Course Preamble - Read and Sign.html",
            "2_1. Instructions and introductions_2_Technical matters.html",
            "4_3. Phonemes, stress and intonation_2_Pronunciation task.pdf",
        ],
        overview=OV1,
        detail=DT1,
        kws=KW1,
        examples=EX1,
        practice=PR1,
        exam=EM1,
        checklist=CL1,
        mapping=MP1,
    )
)


def cat(*xs):
    return "".join(str(x) for x in xs)


# ============================================================ 2
OV2 = cat(
    h2("本节定位"),
    p(
        "第 2 讲处理四个目标里的第一条：<b>phonemes</b>。上一讲建立了音素的概念与辅音的三维度，这一讲把 20 个元音与 24 个辅音逐个落地，重点是五组高频元音对立、词尾清浊、词尾 -s 与 -ed 的读音，以及中国与芬兰学习者最常见的负迁移。"
    ),
    p(
        "材料仍来自 Pronunciation task 的词表，以及课程目标里「把音素发得更清楚正确」这一条。学完本讲，你应该能自己查音标、自己判断一个音错在哪一维，而不是依赖「多听就会」。"
    ),
    p("学完本讲你应当能够："),
    ck(
        "列出 12 个单元音与 8 个双元音，并各举两个例词",
        "用最小对立对区分 /iː/–/ɪ/、/uː/–/ʊ/、/æ/–/e/、/ɑː/–/ʌ/、/ɜː/–/ɔː/",
        "解释 schwa 在非重读音节中的作用",
        "说出六组清浊对，并解释词尾清化为什么会让 bad 听起来像 bat",
        "按规则读出 -s 与 -ed 的三种词尾读音",
        "诊断自己的负迁移：/z/、/θ ð/、/v w/、/ʃ tʃ/、/r/、送气与辅音群",
    ),
)

DT2 = cat(
    h3("2.1 元音系统：12 个单元音与 8 个双元音"),
    p(
        "英语（RP 一类标准音）有 20 个元音：12 个单元音（monophthong，音质不变）与 8 个双元音（diphthong，从一个元音滑向另一个）。元音不靠「挡气」，而是靠舌位与唇形塑形，所以更难自查，必须借助音标与镜子。"
    ),
    tb(
        ("音标", "例词", "中文提示"),
        ("/iː/", "see, three, machine", "长、紧、嘴角向两边"),
        ("/ɪ/", "sit, ship, this", "短、松，介于 i 与 e 之间"),
        ("/e/", "bed, ten, health", "短 e，开口比 /ɪ/ 大"),
        ("/æ/", "bad, cat, plan", "开口大、舌位前低"),
        ("/ɑː/", "car, start, farther", "长、口张开、舌后低"),
        ("/ɒ/", "hot, dog, clock", "短、圆唇（英式）"),
        ("/ɔː/", "door, board, thought", "长、圆唇、舌后"),
        ("/ʊ/", "book, full, good", "短、圆唇、松"),
        ("/uː/", "food, June, school", "长、圆唇、紧"),
        ("/ʌ/", "cut, bus, country", "短、中央偏后、不圆唇"),
        ("/ɜː/", "bird, work, learn", "长、中央、英式不卷舌"),
        ("/ə/", "about, teacher, banana", "最弱、最短、永不重读"),
    ),
    tb(
        ("双元音", "例词", "滑动方向"),
        ("/eɪ/", "day, place, eight", "e → ɪ"),
        ("/aɪ/", "ice, price, eyes 的前半", "a → ɪ"),
        ("/ɔɪ/", "boy, choice", "ɔ → ɪ"),
        ("/aʊ/", "now, house", "a → ʊ"),
        ("/əʊ/", "go, though, home", "ə → ʊ"),
        ("/ɪə/", "here, near", "ɪ → ə"),
        ("/eə/", "there, care", "e → ə"),
        ("/ʊə/", "tour, pure", "ʊ → ə"),
    ),
    cal(
        "tip",
        "元音四问",
        "发任何一个元音，问四件事：舌位高还是低、舌在前还是后、唇圆不圆、长短紧松。四个答案定住，音就稳。",
    ),
    h3("2.2 五组高频对立"),
    p(
        "元音错误里八成集中在五组对立上。它们的区别不是「随便长短」，而是舌位与松紧同时变化，所以既要说对也要听对。"
    ),
    tb(
        ("对立", "例词", "区别"),
        (
            "/iː/ – /ɪ/",
            "sheep – ship, feel – fill, seat – sit",
            "长紧 vs 短松；/ɪ/ 舌位略低略后",
        ),
        ("/uː/ – /ʊ/", "fool – full, pool – pull", "长紧圆唇 vs 短松"),
        ("/æ/ – /e/", "bad – bed, man – men, sat – set", "/æ/ 开口更大、舌更低"),
        ("/ɑː/ – /ʌ/", "cart – cut, heart – hut", "长后低 vs 短中央"),
        ("/ɜː/ – /ɔː/", "bird – board, work – walk", "中央不圆唇 vs 后部圆唇"),
    ),
    p(
        "练习时不要只读长音。有效做法是「短音先定、长音再拉」：先确认 <i>ship</i> 的 /ɪ/ 是短而松的，再把 <i>sheep</i> 拉长到两倍，同时抬高舌位、拉开嘴角。这样两个音才会真正分开，而不是同一个音读两遍长短。"
    ),
    cal(
        "warn",
        "最常见的误判",
        "<i>ship</i> 与 <i>sheep</i> 的差别不只是长短。若只把 /ɪ/ 拉长，得到的是一个不存在的中间音，母语者仍然听成 ship。必须同时改舌位与松紧。",
    ),
    h3("2.3 schwa：英语里最重要的音"),
    p(
        "schwa /ə/ 是出现频率最高的元音，只出现在<b>不重读</b>的音节：<i>about</i> /əˈbaʊt/、<i>teacher</i> /ˈtiːtʃə/、<i>banana</i> /bəˈnɑːnə/（三个 a，只有第二个是 /ɑː/，另两个是 /ə/）。"
    ),
    p(
        "中国学习者常把每个音节都读成饱满元音，结果 <i>banana</i> 读成 /bæˈnænæ/，听起来生硬。修正方法是「先缩后放」：把非重读音节压到 /ə/ 或 /ɪ/，只在重读音节给足音质。这与第 3 讲的节奏是同一件事的两面。"
    ),
    h3("2.4 拼写与元音：六组陷阱"),
    tb(
        ("拼写", "读音", "例"),
        ("ea", "可读 /iː/ 或 /e/", "bead /biːd/ – bread /bred/"),
        ("oo", "可读 /uː/、/ʊ/ 或 /ʌ/", "food /fuːd/ – good /gʊd/ – blood /blʌd/"),
        (
            "ou / ough",
            "至少五种",
            "though /əʊ/ – through /uː/ – tough /ʌf/ – cough /ɒf/ – thought /ɔː/",
        ),
        ("ie", "可读 /iː/ 或 /aɪ/", "believe /ɪˈliːv/ – lie /laɪ/"),
        ("不发音字母", "gh、b、k、w、l 常不发音", "night, comb, knife, write, half"),
        ("-tion / -sion", "/ʃən/ 或 /ʒən/", "nation /ˈneɪʃən/ – equation /ɪˈkweɪʒən/"),
    ),
    p(
        "处理办法只有一个：<b>查音标，不猜拼写</b>。把 -ough、ea、oo、ie 这几组做成一张清单，遇到就记，不要试图推导通则。"
    ),
    h3("2.5 辅音清浊六对与词尾清化"),
    tb(
        ("清音", "浊音", "例词对"),
        ("/p/", "/b/", "pig – big, cap – cab"),
        ("/t/", "/d/", "ten – den, bat – bad"),
        ("/k/", "/ɡ/", "coat – goat, back – bag"),
        ("/f/", "/v/", "fan – van, leaf – leave"),
        ("/s/", "/z/", "seal – zeal, ice – eyes"),
        ("/ʃ/", "/ʒ/", "Confucian – confusion（近似对照）"),
        ("/tʃ/", "/dʒ/", "cheap – jeep, lunch – lunge"),
        ("/θ/", "/ð/", "breath – breathe, three – there 的 th"),
    ),
    p(
        "<b>词尾清化</b>是中国与芬兰学习者最隐形的错误：把词尾浊辅音读成清音，<i>bad</i> 变成 <i>bat</i>、<i>dog</i> 变成 <i>doc</i>、<i>eyes</i> 变成 <i>ice</i>。原因是母语里词尾浊音少见，声带在词尾自然放松。"
    ),
    p(
        "纠正方法：把词尾浊音「拖长半拍」并保持声带振动，例如 <i>ba-d</i>、<i>do-g</i>，手放喉结确认振动延续到最后一个音。练熟后再恢复正常时长，振动习惯会留下来。"
    ),
    h3("2.6 负迁移清单：中文与芬兰语共同的坑"),
    tb(
        ("现象", "来源", "表现", "纠正"),
        (
            "没有 /z/",
            "芬兰语与汉语拼音的 z 是 /ts/",
            "eyes → ice, plays → place",
            "手放喉结练 /z/ 的持续振动",
        ),
        (
            "没有 /θ ð/",
            "两种语言都没有齿间音",
            "three → tree 或 free, then → den",
            "舌尖伸出，轻触上齿，先慢后快",
        ),
        (
            "/v/ 与 /w/ 不分",
            "芬兰语 v 是唇齿近音但不圆唇",
            "very → wery",
            "上齿咬下唇，嘴唇不圆",
        ),
        (
            "/ʃ/ 少用",
            "汉语 sh 是卷舌音，部位更后",
            "she 读得近似 sr",
            "唇稍前突，舌叶靠近齿龈后",
        ),
        (
            "/ŋ/ 易加 /ɡ/",
            "拼写 ng 的干扰",
            "singer → singger",
            "singer 无 /ɡ/，finger 有 /ɡ/",
        ),
        (
            "/r/ 用颤音",
            "芬兰语 r 是大舌颤音",
            "very 的 r 打嘟",
            "舌尖接近齿龈但不接触、不颤",
        ),
        (
            "/p t k/ 不送气",
            "两种语言的 p t k 送气弱",
            "paper 听起来像 baby",
            "词首清音送气，纸片测试会动",
        ),
        (
            "辅音群加元音",
            "音节结构不容许三辅音",
            "street → s(i)treet, texts → tek-s(i)ts",
            "先慢速连读，再加速",
        ),
        ("词尾清化", "词尾浊音少", "bad → bat", "词尾浊音拖长半拍"),
    ),
    cal(
        "exam",
        "必考",
        "这张表的九项就是本课程朗读与听力任务的主要扣分点。每一项都对应一个可练的发音动作，不需要「天赋」。",
    ),
    h3("2.7 词尾 -ed 的三条规则"),
    tb(
        ("前一个音", "读音", "例"),
        ("清辅音（除 /t/）", "/t/", "asked, laughed, watched, helped"),
        ("浊辅音与元音（除 /d/）", "/d/", "played, arrived, opened, called"),
        ("/t/ 或 /d/", "/ɪd/", "wanted, needed, decided, started"),
    ),
    p(
        "常见错误是把 <i>asked</i> 读成 /ˈɑːskɪd/（多一个音节）或 /ˈɑːst/（吞掉 /k/）。正确是 /ɑːskt/：三个辅音相连，先慢速分开读 /k/–/s/–/t/，再连成一个音节尾。"
    ),
    h3("2.8 /l/ 与 /r/：两个细节"),
    p(
        "<b>/l/</b> 有两个变体：元音前的清晰 /l/（<i>leaf</i>、<i>light</i>，舌尖抵齿龈）与元音后的含糊 /l/（<i>feel</i>、<i>full</i>，舌后部抬起）。中国学习者常用清晰 /l/ 读词尾，听起来像多了一个元音（<i>fee-luh</i>）。"
    ),
    p(
        "<b>/r/</b> 是近音（approximant），舌尖接近齿龈但不接触、不颤。芬兰语的大舌颤音与汉语的卷舌 r 都不对。练习：先发 /ɑː/，再把舌尖轻轻抬起靠近齿龈而不碰到，气流不受阻。"
    ),
    h3("2.9 辅音群与插音"),
    p(
        "英语容许 <i>street</i> /striːt/、<i>texts</i> /teksts/、<i>asked</i> /ɑːskt/ 这样的辅音群，而汉语与芬兰语的音节结构不容许，于是学习者会插入元音：<i>sitereet</i>、<i>tek-sits</i>。"
    ),
    p(
        "纠正三步：① 先分开读每个辅音，确认都能发；② 两两合并 /st/ → /str/ → /striːt/；③ 加速到正常语速，允许极短停顿但不许加元音。"
    ),
    h3("2.10 自测表与下一讲"),
    p(
        "给自己做一张十项自测：/z/、/θ/、/ð/、/v/、/w/、/ʃ/、/tʃ/、/dʒ/、词尾浊音、辅音群。每项找两个最小对立对，录音后回听，把「听不出差别」与「说得出差别」分开记：听不出是听觉训练不足，说不出是动作不对，练法完全不同。"
    ),
    p(
        "下一讲进入重音与节奏：单词的重音位置、句子里哪些词重读、弱读式怎么压。本讲解决「单个音对不对」，下一讲解决「一串音怎么排」。"
    ),
)

KW2 = K(
    ("monophthong", "单元音", "Twelve pure vowels, from /iː/ to /ə/."),
    ("diphthong", "双元音", "Eight gliding vowels such as /eɪ/ and /aʊ/."),
    ("vowel height", "舌位高低", "/æ/ is lower than /e/."),
    ("vowel backness", "舌位前后", "/uː/ is back, /iː/ is front."),
    ("rounded", "圆唇", "/uː/ and /ɔː/ are rounded."),
    ("schwa", "中央元音", "The weak /ə/ in about and teacher."),
    ("minimal pair", "最小对立对", "ship and sheep differ in one vowel."),
    ("final devoicing", "词尾清化", "bad may sound like bat if the /d/ is devoiced."),
    ("aspiration", "送气", "Initial /p t k/ are aspirated in English."),
    ("consonant cluster", "辅音群", "street /striːt/, texts /teksts/."),
    ("clear / dark l", "清晰／含糊 l", "leaf has clear /l/; feel has dark /l/."),
    ("approximant", "近音", "/r/ is an approximant, not a trill."),
    ("singer / finger", "无 /ɡ/ 与有 /ɡ/", "singer /ˈsɪŋə/ vs finger /ˈfɪŋɡə/."),
    ("-ed ending", "过去式词尾", "/t/, /d/ or /ɪd/ depending on the preceding sound."),
    (
        "negative transfer",
        "负迁移",
        "First-language habits that cause errors in English.",
    ),
    (
        "voicing",
        "声带振动",
        "Put your hand on your throat: /z/ vibrates, /s/ does not.",
    ),
)

EX2 = cat(
    Q(
        "例 1　纠正下列说法并给出正确音标：① <i>ship</i> 只要把 /iː/ 读短就是 /ɪ/；② <i>banana</i> 三个 a 都读 /æ/；③ <i>bad</i> 与 <i>bat</i> 的差别在元音。",
        p(
            "<b>解：</b>① 错。<i>ship</i> /ʃɪp/ 的 /ɪ/ 不仅短，而且舌位更低更后、肌肉更松；只缩短 /iː/ 得到的是中间音。"
        ),
        p("② 错。<i>banana</i> /bəˈnɑːnə/：第一与第三个 a 是 /ə/，只有第二个是 /ɑː/。"),
        p(
            "③ 错。两词元音相同，差别在词尾辅音的<b>清浊</b>：<i>bad</i> /bæd/ 与 <i>bat</i> /bæt/。"
        ),
        p(
            "<b>通用思路：</b>先查音标，再判断差异属于元音音质、词尾清浊还是重音位置；三者不能用「长短」一把尺子解释。"
        ),
    ),
    Q(
        "例 2　按 -ed 规则给下列动词归类并标音：<i>asked, played, wanted, laughed, needed, arrived, watched, opened</i>。",
        p(
            "<b>解：</b>/t/：asked /ɑːskt/、laughed /lɑːft/、watched /wɒtʃt/（前为清辅音）。"
        ),
        p(
            "/d/：played /pleɪd/、arrived /əˈraɪvd/、opened /ˈəʊpənd/（前为元音或浊辅音）。"
        ),
        p("/ɪd/：wanted /ˈwɒntɪd/、needed /ˈniːdɪd/（前为 /t/ 或 /d/）。"),
        p("注意 <i>watched</i> 结尾是 /tʃt/，塞擦与爆破相连，不要读成 /ˈwɒtʃɪd/。"),
        p(
            "<b>通用思路：</b>看 -ed 前面那个音是清、浊还是 /t d/，不看拼写字母（<i>laughed</i> 的 gh 读 /f/，是清音）。"
        ),
    ),
    Q(
        "例 3　为什么 <i>texts</i> 常被读成三个音节？给出三步纠正方案。",
        p(
            "<b>解：</b>因为汉语与芬兰语的音节结构不允许 /ksts/ 这样四个辅音收尾，学习者会插入元音，变成 /ˈtek-sɪ-ts/。"
        ),
        p(
            "三步：① 拆开读 /t/–/e/–/k/–/s/–/t/–/s/，确认每个音都能独立发出；② 两两合并 /ks/ → /ksts/，保持不插音；③ 整词慢速 <i>texts</i>，再加速，允许极短停顿但不许出现元音。"
        ),
        p(
            "同一方法适用于 <i>asked</i> /ɑːskt/、<i>sixths</i> /sɪksθs/、<i>strengths</i> /streŋθs/。"
        ),
        p(
            "<b>通用思路：</b>先保证单音，再两两合并，最后整体加速。插音是音节结构的习惯，不能靠「念快一点」解决。"
        ),
    ),
    Q(
        "例 4　同学把 <i>I have three sisters and two brothers</i> 读成 /aɪ hæv triː ˈsɪstəz æn tuː ˈbrʌdəz/。指出问题并说明纠正动作。",
        p(
            "<b>解：</b>① <i>three</i> 读成 /triː/：/θ/ 被 /t/ 替代。动作：舌尖伸出轻触上下齿之间，先发长 /θ/，感受气流从齿间通过，再滑向 /r/。"
        ),
        p(
            "② <i>brothers</i> 读成 /ˈbrʌdəz/：/ð/ 被 /d/ 替代。动作：舌尖不要顶齿龈，要放在齿间并保持声带振动。"
        ),
        p(
            "补充检查：<i>sisters</i> 的 -s 在 /t/ 后读 /s/；<i>brothers</i> 的 -s 在 /ð/ 后读 /z/。"
        ),
        p(
            "<b>通用思路：</b>先定位哪个音被替换（/θ/→/t/、/ð/→/d/），再改发音部位；词尾 -s 的清浊由前一个音决定。"
        ),
    ),
)

PR2 = cat(
    ol(
        "写出下列词中元音的音标并各组一个最小对立对：<i>ship、full、bad、cut、board</i>。",
        "给 <i>governments、computers、places、watches</i> 标出词尾 -s 读音并说明规则。",
        "按 -ed 规则读出 <i>worked、cleaned、visited、pushed、decided、travelled</i>。",
        "从负迁移清单里选三项你最严重的问题，各写一个发音动作与一条自测标准。",
        "用 /θ/ 与 /ð/ 各造一句含三个 th 词的句子，并标出舌尖位置。",
    ),
    D(
        "答案与思路",
        p(
            "<b>1.</b> <i>ship</i> /ɪ/ – <i>sheep</i> /iː/；<i>full</i> /ʊ/ – <i>fool</i> /uː/；<i>bad</i> /æ/ – <i>bed</i> /e/；<i>cut</i> /ʌ/ – <i>cart</i> /ɑː/；<i>board</i> /ɔː/ – <i>bird</i> /ɜː/。"
        ),
        p(
            "<b>2.</b> <i>governments</i> /ts/（前为 /t/，读 /s/）；<i>computers</i> /z/（前为元音）；<i>places</i> /ɪz/（前为 /s/）；<i>watches</i> /ɪz/（前为 /tʃ/）。规则：咝音加 /ɪz/，清音加 /s/，浊音与元音加 /z/。"
        ),
        p(
            "<b>3.</b> <i>worked</i> /t/；<i>cleaned</i> /d/；<i>visited</i> /ɪd/；<i>pushed</i> /t/；<i>decided</i> /ɪd/；<i>travelled</i> /d/。"
        ),
        p(
            "<b>4.</b> 参考：/z/ → 手放喉结，持续 3 秒振动，自测标准是 <i>eyes</i> 与 <i>ice</i> 能被同伴分辨；/θ/ → 舌尖伸出可见，自测标准是 <i>three</i> 不被听成 <i>tree</i>；辅音群 → 不加元音，自测标准是 <i>texts</i> 只有一个音节。"
        ),
        p(
            "<b>5.</b> 参考：<i>Three thin thieves thought a thousand thoughts.</i> 全部 /θ/ 舌尖在齿间；<i>They breathe together in this weather.</i> 全部 /ð/ 同位置但声带振动。"
        ),
    ),
)

EM2 = cat(
    cal(
        "exam",
        "必考",
        "12 个单元音与 8 个双元音的音标与例词；五组高频对立；schwa 只出现在非重读音节；六组清浊对与词尾清化；-s 与 -ed 的三条读音规则；辅音群不加元音。",
    ),
    cal(
        "warn",
        "易错 1",
        "把元音差异当成「长短」一种：ship/sheep、full/fool 都要同时改舌位与松紧。",
    ),
    cal(
        "warn",
        "易错 2",
        "词尾浊音清化（bad→bat、eyes→ice、dog→doc），这是最隐形的扣分点。",
    ),
    cal(
        "warn",
        "易错 3",
        "给 -ed 加多余音节（asked 读成 /ˈɑːskɪd/），或在辅音群里插元音（texts 读成三音节）。",
    ),
    cal(
        "tip",
        "进阶",
        "了解 /l/ 的清晰与含糊两个变体、/r/ 是近音而非颤音；这两项是把「外国口音」变成「轻微口音」的关键细节。",
    ),
)

CL2 = cat(
    h2("本讲方法清单"),
    h3("元音对立练习四步"),
    st(
        "查音标，确认两个音的舌位与松紧差异",
        "单音夸张：短音先定，长音再拉，同时改舌位",
        "词对朗读：慢速 10 遍、常速 10 遍，录音回听",
        "放进短语：my ship / my sheep，确认语流中仍可分",
    ),
    h3("词尾与辅音群自检"),
    ck(
        "词尾浊音能否持续振动到最后一个音（手放喉结）",
        "-s 与 -ed 是否按前一个音选择 /s z ɪz/ 与 /t d ɪd/",
        "辅音群里是否插入了元音（texts、asked、streets）",
        "/θ ð/ 是否舌尖可见（镜子测试）",
    ),
)

MP2 = tb(
    ("源文件", "位置 / 页码", "覆盖内容"),
    (
        "4_3. Phonemes, stress and intonation/2_Pronunciation task.pdf",
        "p1",
        "全部词表；本讲用于提取 -s 清浊、/θ ð/、/v w/、/ʃ tʃ dʒ/ 等对立",
    ),
    (
        "2_1. Instructions and introductions/1_Course Preamble - Read and Sign/…html",
        "Objectives 一节",
        "目标一：pronounce English phonemes more clearly and correctly",
    ),
    (
        "2_1. Instructions and introductions/2_Technical matters.html",
        "全篇",
        "录音工具与提交规则，用于本讲的录音自评",
    ),
    ("（跳过）", "—", "重复副本 Pronunciation task.pdf 不再单独设知识点"),
    (
        "（拓展）",
        "—",
        "元音四维描写、五组对立表、负迁移九项、-ed 与 -s 规则、辅音群三步纠正为教学补充，原文只给词表与目标表述",
    ),
)

LEC.append(
    L(
        slug="p2-vowels-consonants",
        tzh="第 2 讲 · 元音与辅音精讲",
        ten="Vowels and Consonants in Detail",
        keywords=[
            "monophthong",
            "diphthong",
            "schwa",
            "voicing",
            "final devoicing",
            "consonant cluster",
            "-ed ending",
            "negative transfer",
        ],
        files=[
            "4_3. Phonemes, stress and intonation_2_Pronunciation task.pdf",
            "2_1. Instructions and introductions_2_Technical matters.html",
        ],
        overview=OV2,
        detail=DT2,
        kws=KW2,
        examples=EX2,
        practice=PR2,
        exam=EM2,
        checklist=CL2,
        mapping=MP2,
    )
)
# ============================================================ 3
OV3 = cat(
    h2("本节定位"),
    p(
        "第 3 讲对应第二个目标：<b>stress syllables and sentences more appropriately</b>——把词的重音和句子的重音放对。音发对了但重音放错，母语者仍然会觉得「听不懂」或「听着累」，因为英语的节奏靠重音搭骨架。"
    ),
    p(
        "本讲从音节数起，到双音节名词与动词的重音对立、后缀的重音规则、复合名词的重音位置，再到句子层面的内容词重读与功能词弱读。它是第 2 讲（单个音）与第 4 讲（语调与停顿）之间的桥梁。"
    ),
    p("学完本讲你应当能够："),
    ck(
        "数出单词的音节数并标出主重音与次重音",
        "区分双音节名词与动词的重音位置（ˈrecord / reˈcord）",
        "按后缀规则判断 -tion、-ity、-ic、-graphy 类词的重音",
        "判断复合名词与「形容词 + 名词」短语的重音差异",
        "在句子里只重读内容词，把功能词压成弱读式",
        "用打拍子的方式练出英语的节奏感",
    ),
)

DT3 = cat(
    h3("3.1 音节与重音符号"),
    p(
        "音节（syllable）的核心是<b>一个元音</b>：有多少个元音音素（不是字母），通常就有多少个音节。<i>banana</i> /bəˈnɑːnə/ 有三个音节，<i>strengths</i> /streŋθs/ 只有一个音节——后者是很多人的盲点：辅音再多，没有元音就不成音节。"
    ),
    p(
        "音标里的重音符号有两个：<b>ˈ</b> 标主重音，放在重读音节的左上角，如 <i>teacher</i> /ˈtiːtʃə/；<b>ˌ</b> 标次重音，如 <i>ˌrepresenˈtation</i>。重读音节的三个特征是：更响、更长、音高更高。三者至少占两个，才真的重读。"
    ),
    cal(
        "tip",
        "判断重音的自测法",
        "把手掌放在嘴前 5 厘米，读一个多音节词。手掌感到气流最强的那一拍，通常就是重读音节。若每一拍气流都一样，说明你把重音读平了。",
    ),
    h3("3.2 双音节名词与动词：重音换位置"),
    p(
        "英语里有一批双音节词，名词重音在前、动词重音在后。这是最容易被听出来的口音特征，也是最容易考的规则："
    ),
    tb(
        ("名词", "动词", "说明"),
        ("ˈrecord /ˈrekɔːd/", "reˈcord /rɪˈkɔːd/", "录音（名）／记录（动）"),
        ("ˈpresent /ˈpreznt/", "preˈsent /prɪˈzent/", "礼物（名）／呈现（动）"),
        ("ˈobject /ˈɒbdʒɪkt/", "obˈject /əbˈdʒekt/", "物体（名）／反对（动）"),
        ("ˈimport /ˈɪmpɔːt/", "imˈport /ɪmˈpɔːt/", "进口（名）／进口（动）"),
        ("ˈexport /ˈekspɔːt/", "exˈport /ɪkˈspɔːt/", "出口（名）／出口（动）"),
        ("ˈcontract /ˈkɒntrækt/", "conˈtract /kənˈtrækt/", "合同（名）／收缩（动）"),
        ("ˈincrease /ˈɪnkriːs/", "inˈcrease /ɪnˈkriːs/", "增长（名）／增长（动）"),
        ("ˈpermit /ˈpɜːmɪt/", "perˈmit /pəˈmɪt/", "许可证（名）／允许（动）"),
    ),
    p(
        "这类词的重音不是「习惯」，而是有规律的：名词倾向于「重音在前」，动词倾向于「重音在后」。句子里的判断靠词性：<i>The ˈexport figures rose.</i>（名词，重音在前）／<i>We exˈport to Germany.</i>（动词，重音在后）。"
    ),
    h3("3.3 后缀决定重音位置"),
    p("多音节词的重音很大程度上由后缀决定。三条规则覆盖大多数技术词汇："),
    tb(
        ("后缀", "重音位置", "例"),
        (
            "-tion / -sion / -cian",
            "紧接后缀的前一个音节",
            "inforˈmation, deˈcision, techˈnician",
        ),
        (
            "-ic / -ical",
            "紧接后缀的前一个音节",
            "ecoˈnomic, techˈnological, geoˈgraphical",
        ),
        (
            "-ity / -ial / -ious",
            "紧接后缀的前一个音节",
            "producˈtivity, indusˈtrial, amˈbitious",
        ),
        (
            "-graphy / -logy / -metry",
            "倒数第三个音节",
            "phoˈtography, techˈnology, geˈometry",
        ),
        (
            "-ee / -eer / -ese / -ette",
            "后缀本身重读",
            "employˈee, engiˈneer, Japanˈese, kitchˈenette",
        ),
        (
            "-able / -ful / -less / -ness",
            "不改变原词重音",
            "ˈcomfortable, ˈuseful, ˈcareless, ˈkindness",
        ),
    ),
    p(
        "同族词的重音移动是最值得练的一组：<i>ˈphotograph → phoˈtography → ˌphotoˈgraphic</i>；<i>ˈeconomy → ˌecoˈnomic → ˌecoˈnomically</i>；<i>ˈnation → ˈnational → ˌnatioˈnality</i>。三个词连着读，能听出重音像波浪一样移动。"
    ),
    cal(
        "warn",
        "高频错位",
        "<i>technology</i> 的重音在第二音节 /tekˈnɒlədʒi/，不是第一音节；<i>development</i> 在第二音节 /dɪˈveləpmənt/；<i>photography</i> 在第二音节 /fəˈtɒɡrəfi/。这三词读错重音，比读错一个辅音更影响理解。",
    ),
    h3("3.4 复合名词与「形容词 + 名词」"),
    p(
        "复合名词（compound noun）的重音落在<b>第一个成分</b>：<i>ˈgreenhouse</i>（温室）、<i>ˈblackbird</i>（乌鸫）、<i>ˈdata centre</i>、<i>ˈpower station</i>、<i>ˈcross connection room</i>、<i>ˈhard drive</i>、<i>ˈmotherboard</i>。"
    ),
    p(
        "而「形容词 + 名词」的自由短语重音落在<b>名词</b>上：<i>a green ˈhouse</i>（绿色的房子）、<i>a black ˈbird</i>（一只黑色的鸟）。同一个写法，重音位置不同，意思完全不同。"
    ),
    tb(
        ("写法", "重音", "意思"),
        ("greenhouse", "ˈgreenhouse", "温室"),
        ("green house", "green ˈhouse", "绿色的房子"),
        ("blackbird", "ˈblackbird", "乌鸫（一种鸟）"),
        ("black bird", "black ˈbird", "黑色的鸟"),
        ("White House", "ˈWhite House", "白宫"),
        ("white house", "white ˈhouse", "白色的房子"),
    ),
    p(
        "这条规则在技术语境里天天用到：<i>ˈdata centre</i>、<i>ˈcooling system</i>、<i>ˈpower supply</i>、<i>ˈtest bench</i>。重音放错，听者会以为你在说两个独立的词。"
    ),
    h3("3.5 句重音：只重读内容词"),
    p(
        "句子层面的规则只有一条：<b>内容词重读，功能词弱读</b>。内容词是名词、动词、形容词、副词、数词；功能词是冠词、介词、连词、助动词、代词。"
    ),
    p(
        "例：<i>Scanfood is a ˈlarge ˈcompany by ˈFinnish ˈstandards.</i> 重读的是 large、company、Finnish、standards；is、a、by 全部弱读。若把每个词都读得一样重，句子就变成一串没有重点的音节。"
    ),
    p(
        "句重音还会因信息结构变化：回答 <i>Is Scanfood a small company?</i> 时重读 <i>ˈlarge</i>；回答 <i>Is Scanfood a Finnish company?</i> 时重读 <i>ˈFinnish</i>。同一句话，重音落在哪里，取决于对方在问什么。"
    ),
    h3("3.6 弱读式：功能词的真面目"),
    tb(
        ("词", "重读式", "弱读式", "例"),
        ("a / an", "/eɪ/ /æn/", "/ə/ /ən/", "a cup /ə ˈkʌp/"),
        ("the", "/ðiː/", "/ðə/（辅音前）", "the plug /ðə ˈplʌɡ/"),
        ("of", "/ɒv/", "/əv/", "a cup of tea /ə ˈkʌp ə ˈtiː/"),
        ("to", "/tuː/", "/tə/", "to the office /tə ði ˈɒfɪs/"),
        ("and", "/ænd/", "/ənd/ 或 /ən/", "black and white /ˈblæk ən ˈwaɪt/"),
        ("can", "/kæn/", "/kən/", "I can do it /aɪ kən ˈduː ɪt/"),
        ("was", "/wɒz/", "/wəz/", "it was late /ɪt wəz ˈleɪt/"),
        ("for", "/fɔː/", "/fə/", "for a moment /fər ə ˈməʊmənt/"),
        (
            "that（连词）",
            "/ðæt/",
            "/ðət/",
            "I think that it works /aɪ ˈθɪŋk ðət ɪt ˈwɜːks/",
        ),
    ),
    p(
        "弱读不是「偷懒」，而是英语节奏的必要条件。功能词占句子里一半以上的词，若都重读，句子就没有起伏；而母语者正是靠「重读与弱读的对比」来切分信息。"
    ),
    h3("3.7 节奏：重音计时，不是音节计时"),
    p(
        "英语是<b>重音计时</b>（stress-timed）语言：重读音节之间的时间大致相等，中间的弱读音节被压缩。汉语与芬兰语更接近<b>音节计时</b>（syllable-timed）：每个音节占时相近。这就是为什么中国与芬兰学习者说英语听起来「平」和「快」。"
    ),
    p(
        "练习方法（打拍子）：选一句 <i>ˈScanfood is a ˈlarge ˈcompany by ˈFinnish ˈstandards.</i> 用食指在桌上打出四个等间隔的重拍（Scanfood、large、company、Finnish、standards 中取四个），把中间的功能词挤进拍子之间。慢速练到能挤进去，再加速。"
    ),
    cal(
        "tip",
        "节奏的检验标准",
        "让同伴只听你的节奏（不听词），能数出重拍的数量与位置，就说明节奏对了。若对方数不出来，问题不在音，在重音分布。",
    ),
    h3("3.8 对比重音：重音改变意思"),
    p(
        "同一句话，重音落在不同词上，意思完全不同。经典例子：<i>I didn’t say he stole the money.</i>"
    ),
    tb(
        ("重读词", "含义"),
        ("I", "不是我说的（是别人说的）"),
        ("didn’t", "我确实说了（只是不是「说」这个动作，可能是暗示）"),
        ("say", "我不是「说」的（可能是写的或用别的方​式）"),
        ("he", "不是他（是别人）"),
        ("stole", "不是偷的（可能是借的）"),
        ("the money", "不是那笔钱（是别的钱）"),
    ),
    p(
        "这条规则的实用价值在会议与演讲里：想强调哪个信息，就把重音放哪个词，不要靠提高整体音量。"
    ),
    h3("3.9 常见错误与纠正"),
    tb(
        ("错误", "表现", "纠正"),
        ("每个音节都重读", "听起来像念清单", "只重读一个主重音，其余压到 /ə/ 或 /ɪ/"),
        ("重音后移", "techˈnology、deveˈlopment", "查音标，记住第二音节重读"),
        ("功能词重读", "THE plug, OF the room", "冠词、介词一律弱读"),
        ("复合名词重音错", "data ˈcentre", "复合名词重音在第一个成分"),
        ("句重音平均", "每词一样重，听不出重点", "按信息结构只重读内容词"),
    ),
    h3("3.10 与下一讲衔接"),
    p(
        "本讲解决了「哪个音节更响」。下一讲解决「声音往哪里走」：升还是降、在哪里停、停顿多长。重音与语调合起来，才是完整的「可理解的口语」。"
    ),
)

KW3 = cat(
    K(
        ("syllable", "音节", "A unit with one vowel sound: ba-na-na has three."),
        ("stress", "重音", "The strongest syllable in a word: ˈteacher."),
        ("primary / secondary stress", "主重音／次重音", "ˌrepresenˈtation has both."),
        ("word stress", "词重音", "ˈrecord (noun) vs reˈcord (verb)."),
        (
            "sentence stress",
            "句重音",
            "Content words are stressed, function words are not.",
        ),
        ("weak form", "弱读式", "of is /əv/, to is /tə/ in connected speech."),
        ("schwa", "中央元音", "The vowel of almost every weak syllable."),
        (
            "stress-timed",
            "重音计时",
            "Stressed syllables come at roughly equal intervals.",
        ),
        (
            "syllable-timed",
            "音节计时",
            "Each syllable takes similar time, as in Chinese.",
        ),
        ("compound noun", "复合名词", "ˈdata centre, ˈpower supply."),
        (
            "suffix stress",
            "后缀重音",
            "-tion and -ity pull stress to the previous syllable.",
        ),
        ("contrastive stress", "对比重音", "I didn’t say HE stole it."),
        (
            "content word",
            "内容词",
            "Nouns, verbs, adjectives and adverbs are stressed.",
        ),
        ("function word", "功能词", "Articles, prepositions and auxiliaries are weak."),
        ("beat", "节拍", "Tap the beats to feel the rhythm."),
        ("stress shift", "重音移动", "ˈphotograph → phoˈtography → ˌphotoˈgraphic."),
    ),
)

EX3 = cat(
    Q(
        "例 1　标出下列词的重音并说明依据：<i>photograph、photography、photographic、economy、economic、nation、nationality</i>。",
        p(
            "<b>解：</b><i>ˈphotograph</i>（三音节，重音第一）→ <i>phoˈtography</i>（-graphy 类，重音倒数第三）→ <i>ˌphotoˈgraphic</i>（-ic 类，重音紧接后缀前）。"
        ),
        p(
            "<i>ˈeconomy</i>（重音第二，-nomy 类）→ <i>ˌecoˈnomic</i>（-ic 类，重音前移）→ <i>ˌecoˈnomically</i>（-ally 不移动重音）。"
        ),
        p(
            "<i>ˈnation</i> → <i>ˈnational</i>（-al 不移动重音）→ <i>ˌnatioˈnality</i>（-ity 类，重音前移一个音节）。"
        ),
        p(
            "<b>通用思路：</b>先数音节，再看后缀属哪一类（-ic/-ity 前移、-graphy 倒数第三、-al 不移动），最后用同族词连读检验重音是否在移动。"
        ),
    ),
    Q(
        "例 2　读下面两句，说明 record 的重音为什么不同：<i>The export record was broken last year.</i> / <i>We record every test result.</i>",
        p(
            "<b>解：</b>第一句 <i>record</i> 是名词（唱片／记录），重音在前 <i>ˈrecord</i>；第二句是动词（记录），重音在后 <i>reˈcord</i>。"
        ),
        p(
            "同句中的 <i>export</i> 在第一句作定语修饰 record，仍是名词性，读 <i>ˈexport</i>。若说 <i>We export the data</i>，则读 <i>exˈport</i>。"
        ),
        p(
            "检验方法：把词换成别的词，看句子结构。能加冠词、能作主语的是名词；能带宾语、能变时态的是动词。"
        ),
        p(
            "<b>通用思路：</b>先判词性（名词重音在前、动词重音在后），再读句子；不要凭记忆读单个词。"
        ),
    ),
    Q(
        "例 3　解释 <i>ˈgreenhouse</i> 与 <i>green ˈhouse</i>、<i>ˈblackbird</i> 与 <i>black ˈbird</i> 的差别，并各造一句。",
        p(
            "<b>解：</b>前者是复合名词，重音在第一个成分，指一个固定概念；后者是形容词 + 名词的自由短语，重音在名词，指「某种颜色的某物」。"
        ),
        p(
            "例：<i>We grow tomatoes in the ˈgreenhouse.</i>（温室）／<i>They live in a green ˈhouse near the lake.</i>（绿色的房子）。<i>A ˈblackbird landed on the fence.</i>（乌鸫）／<i>A black ˈbird flew past the window.</i>（一只黑鸟）。"
        ),
        p(
            "技术语境同构：<i>ˈpower supply</i>（电源，一个部件）／<i>a powerful supˈply</i>（供应量大）。"
        ),
        p(
            "<b>通用思路：</b>整词概念用一个重音（前），修饰关系用两个重音（后）；重音位置就是语义结构的标记。"
        ),
    ),
    Q(
        "例 4　写出 <i>a cup of tea and a piece of cake</i> 的弱读式，并说明哪些词被压缩。",
        p(
            "<b>解：</b>/ə ˈkʌp əv ˈtiː ən ə ˈpiːs əv ˈkeɪk/。重读的是 cup、tea、piece、cake；a、of、and 全部弱读。"
        ),
        p(
            "具体变化：<i>a</i> → /ə/；<i>of</i> → /əv/（元音压成 schwa，/v/ 保留）；<i>and</i> → /ən/（/d/ 脱落）；<i>of tea</i> 连读为 /əv ˈtiː/。"
        ),
        p(
            "慢速读时容易把每个词都读全，加速后才出现弱读。练习顺序应是「先慢后快」，而不是一开始就求快。"
        ),
        p(
            "<b>通用思路：</b>先标内容词（重读），其余全部压成 schwa 或 /ɪ/；连读与脱落是弱读的结果，不是额外的技巧。"
        ),
    ),
)

PR3 = cat(
    ol(
        "标出下列词的重音并注音标：<i>technology、development、photography、engineer、comfortable、productivity</i>。",
        "判断下列句子中黑体词的重音位置：<i>We need a **permit** to work here.</i> / <i>They will **permit** the change.</i>",
        "把 <i>the cross connection room</i> 与 <i>a cross connection ˈroom</i> 各读一遍，说明重音差异带来的意思差别。",
        "给 <i>Scanfood is a large company by Finnish standards.</i> 标出重读词，并把功能词写成弱读式。",
        "用打拍子的方法练 <i>We will be expanding our operations.</i>，说明重拍落在哪几个词上。",
    ),
    D(
        "答案与思路",
        p(
            "<b>1.</b> <i>technology</i> /tekˈnɒlədʒi/（第二音节）；<i>development</i> /dɪˈveləpmənt/（第二）；<i>photography</i> /fəˈtɒɡrəfi/（第二）；<i>engineer</i> /ˌendʒɪˈnɪə/（-eer 重读）；<i>comfortable</i> /ˈkʌmftəbl/（第一，且常压缩为三音节）；<i>productivity</i> /ˌprɒdʌkˈtɪvəti/（-ity 前移，主重音在 /tɪv/）。"
        ),
        p(
            "<b>2.</b> <i>ˈpermit</i>（名词，重音在前）／<i>perˈmit</i>（动词，重音在后）。"
        ),
        p(
            "<b>3.</b> <i>the ˈcross connection room</i> 是复合名词，重音在第一个成分 cross，指一个固定房间；若说 <i>a cross connection ˈroom</i>，则强调「一个用于交叉连接的房间」，重音落在 room，语义重心不同。"
        ),
        p(
            "<b>4.</b> 重读：<i>ˈScanfood … ˈlarge ˈcompany … ˈFinnish ˈstandards</i>；弱读：is /ɪz/ 或 /z/、a /ə/、by /bə/。整句 /ˈskænfuːd z ə ˈlɑːdʒ ˈkʌmpəni baɪ ˈfɪnɪʃ ˈstændədz/。"
        ),
        p(
            "<b>5.</b> 重拍落在 <i>will</i>（或 be）、<i>-PAN-</i>、<i>-RA-</i>：<i>We will be exˈpanding our opeˈrations.</i> 四个重拍大致等间隔，其余音节挤在拍间。"
        ),
    ),
)

EM3 = cat(
    cal(
        "exam",
        "必考",
        "音节数与重音符号；双音节名词／动词的重音对立；-tion/-ity/-ic/-graphy 的重音规则；复合名词重音在第一个成分；句重音只落在内容词；常见功能词的弱读式。",
    ),
    cal("warn", "易错 1", "把每个音节都读得一样重（音节计时），导致听者抓不到重点。"),
    cal(
        "warn",
        "易错 2",
        "重音位置错：techˈnology、deveˈlopment、photoˈgraphy 是最常见的三个。",
    ),
    cal(
        "warn",
        "易错 3",
        "复合名词重音放在第二个成分（data ˈcentre），与形容词短语混淆。",
    ),
    cal(
        "tip",
        "进阶",
        "用对比重音（I didn’t say HE stole it）替代提高音量来强调，是演讲与会议里最专业的做法。",
    ),
)

CL3 = cat(
    h2("本讲方法清单"),
    h3("单词重音四步判定"),
    st(
        "数音节：数元音音素，不数字母",
        "找后缀：-tion/-ity/-ic 前移一个音节，-graphy 倒数第三，-ee/-eer 后缀本身重读",
        "判词性：双音节名词重音在前，动词在后",
        "查音标核对，并把同族词连读检验重音是否移动",
    ),
    h3("句子节奏练习"),
    ck(
        "先标出内容词（名词、动词、形容词、副词、数词）",
        "把功能词写成弱读式（a /ə/、of /əv/、and /ən/）",
        "打拍子：重拍等间隔，弱读音节挤进拍间",
        "录音后只听节奏，看同伴能否数出重拍数量",
    ),
)

MP3 = tb(
    ("源文件", "位置 / 页码", "覆盖内容"),
    (
        "4_3. Phonemes, stress and intonation/2_Pronunciation task.pdf",
        "p1",
        "词表本身即重音练习材料；本讲取多音节词作重音示范",
    ),
    (
        "4_3. Phonemes, stress and intonation/7_19. Read and record the story…/Text 1 Scanfood new.pdf",
        "p1",
        "句重音与节奏的整段语料（Scanfood 介绍）",
    ),
    (
        "2_1. Instructions and introductions/1_Course Preamble - Read and Sign/…html",
        "Objectives 一节",
        "目标二：stress syllables and sentences more appropriately",
    ),
    ("（跳过）", "—", "重复副本 Text 1 与 Pronunciation task 不再单独设知识点"),
    (
        "（拓展）",
        "—",
        "后缀重音规则表、复合名词与形容词短语的对比、弱读式清单、对比重音六读法为教学补充，原文只给目标与语料",
    ),
)

LEC.append(
    L(
        slug="p3-stress-rhythm",
        tzh="第 3 讲 · 词重音与句子节奏",
        ten="Word Stress and Sentence Rhythm",
        keywords=[
            "syllable",
            "word stress",
            "suffix stress",
            "compound noun",
            "sentence stress",
            "weak form",
            "stress-timed",
            "contrastive stress",
        ],
        files=[
            "4_3. Phonemes, stress and intonation_7_19. Read and record the story___pausing, pitch and intonation_intro_Text 1 Scanfood new.pdf",
            "4_3. Phonemes, stress and intonation_2_Pronunciation task.pdf",
        ],
        overview=OV3,
        detail=DT3,
        kws=KW3,
        examples=EX3,
        practice=PR3,
        exam=EM3,
        checklist=CL3,
        mapping=MP3,
    )
)
# ============================================================ 4
OV4 = cat(
    h2("本节定位"),
    p(
        "第 4 讲对应第三、第四个目标：<b>use pausing and intonation for effect</b> 与 <b>understand various dialects</b>。到这里，音素（第 2 讲）与重音（第 3 讲）已经就位，剩下的是把它们串成语流：在哪里停、停多久、声音往上还是往下、相邻的音如何连起来。"
    ),
    p(
        "本讲的落地材料是课程提供的朗读任务：<i>Read and record the story — pausing, pitch and intonation</i>，文本是 Text 1 Scanfood。它既是朗读练习，也是整门课「同一段话录两次」的对照材料。"
    ),
    p("学完本讲你应当能够："),
    ck(
        "把一段话切成语调单位，标出三档停顿",
        "用降调、升调、降升调分别表达陈述、疑问与保留",
        "正确读出列举、选择疑问句与反意疑问句的语调",
        "识别并读出连读、省音、同化与缩略四类语流音变",
        "按标注朗读 Text 1 Scanfood，并录下可与首次录音对比的版本",
        "听懂非标准口音的关键信息，不被个别音素卡住",
    ),
)

DT4 = cat(
    h3("4.1 语调单位：一口气说一个意思"),
    p(
        "语调单位（tone unit / intonation unit）是语流的基本单位，通常对应一个意义块，含一个<b>核心重音</b>（nucleus，最后一个重读词）。一个语调单位内音高走一条曲线，单位之间停顿。"
    ),
    p(
        "例：<i>Scanfood is a ˈlarge ˈcompany | by ˈFinnish ˈstandards.</i> 两个语调单位：前者给出身份，后者给出判断标准。核心重音分别是 company 与 standards。"
    ),
    p(
        "划分语调单位与第 2 讲的分块是同一件事：<b>一个块 = 一个语调单位 = 一条音高曲线</b>。块切错，语调必然错。"
    ),
    h3("4.2 停顿：三个作用、三档长度"),
    p(
        "停顿（pausing）在口语里有三个作用：<b>换气</b>（生理需要）、<b>分句</b>（告诉听者一个意思结束）、<b>强调</b>（在关键词前留白）。课程朗读任务明确要求「pausing, pitch and intonation」，说明停顿是被评分的项目，而不是自然产物。"
    ),
    tb(
        ("长度", "记号", "时机", "例"),
        (
            "短停 0.3–0.5 秒",
            "|",
            "语调单位之间",
            "The head office is located | outside Lappeenranta.",
        ),
        (
            "中停 0.8–1 秒",
            "||",
            "句子之间、段落转折",
            "It has over 4 000 employees. || It is one of the leading manufacturers …",
        ),
        ("长停 1.5 秒以上", "|||", "段落之间、演讲换页", "（朗读长文时在段末留白）"),
    ),
    p(
        "停顿位置错，意义就变。经典例：<i>I didn’t say | he stole the money.</i>（我没说｜他偷了钱）与 <i>I didn’t say he stole | the money.</i>（我没说他偷了｜那笔钱）。同一个句子，两种停顿，两种含义。"
    ),
    cal(
        "warn",
        "最常见的破句",
        "在介词与宾语之间停：<i>located outside | Lappeenranta</i>。听者会以为句子结束。正确是 <i>located | outside Lappeenranta</i>，把介词短语整块读出。",
    ),
    h3("4.3 四种调型与它们的功能"),
    tb(
        ("调型", "符号", "典型功能", "例"),
        (
            "降调 falling",
            "↘",
            "陈述、Wh- 问句、命令、确定",
            "It has over 4 000 employees. ↘",
        ),
        (
            "升调 rising",
            "↗",
            "Yes/No 问句、列举中的非末项、不确定",
            "Is it a large company? ↗",
        ),
        (
            "降升调 fall-rise",
            "↘↗",
            "保留、对比、委婉否定",
            "It’s ˈgood … ↘↗ but not perfect.",
        ),
        ("升降调 rise-fall", "↗↘", "惊讶、强烈赞同或讽刺", "ˈReally? ↗↘"),
    ),
    p(
        "降调是最「安全」的调型：陈述句、Wh- 问句、命令都用它。中国学习者常把陈述句句末上扬，听起来像在征询同意，这在专业场合会削弱确定感。"
    ),
    p(
        "升调用在 Yes/No 问句上是语法要求，不是态度问题：<i>Does the plug comply with the standard? ↗</i> 若用降调，听起来像在陈述而不是提问。"
    ),
    h3("4.4 列举与选择疑问句"),
    p(
        "列举的语调是「前面的项升、最后一项降」：<i>We have subsidiaries in the ˈUSA ↗, ˈCanada ↗, and ˈScandinavia ↘.</i> 这条规则让听者知道「还没说完」。若每项都降，听者会以为列举结束。"
    ),
    p(
        "选择疑问句是「前项升、后项降」：<i>Would you like ˈtea ↗ or ˈcoffee ↘?</i> 这与中国学习者常把整句读成升调的习惯不同。"
    ),
    h3("4.5 反意疑问句的两种语调"),
    p("反意疑问句的语调决定它是「求确认」还是「真提问」："),
    tb(
        ("语调", "含义", "例"),
        ("降调", "我确信，你同意吧", "It’s a large company, ˈisn’t it? ↘"),
        ("升调", "我真的不确定，想问你", "It’s a large company, ˈisn’t it? ↗"),
    ),
    p(
        "同理，回答 <i>It’s quite expensive, isn’t it?</i> 时，若对方用降调，你只需附和；用升调，则需要给出真实判断。"
    ),
    h3("4.6 语调与态度：礼貌、保留、讽刺"),
    ul(
        "<b>礼貌请求</b>用升调或降升调：<i>Could you check the wiring? ↗</i> 比降调柔和。",
        "<b>委婉否定</b>用降升调：<i>It’s … ˈpossible ↘↗.</i> 表示「有可能，但有保留」。",
        "<b>安慰与确认</b>用降调：<i>I’m afraid not. ↘</i> 明确、不拖泥带水。",
        "<b>讽刺</b>常用升降调：<i>ˈLovely weather. ↗↘</i> 字面与实际相反。",
    ),
    p(
        "这解释了为什么同一句 <i>I’m afraid not</i> 在不同语调下感觉完全不同：降调是专业的拒绝，降升调则像还有余地，容易被误解为「再问问也许行」。"
    ),
    h3("4.7 语流音变：连读、省音、同化、缩略"),
    tb(
        ("类型", "机制", "例"),
        (
            "连读 linking",
            "辅音接元音，音节重新划分",
            "an apple → /əˈnæpl/；one of → /ˈwʌnəv/",
        ),
        (
            "省音 elision",
            "某些音在语流中脱落",
            "next day → /neks deɪ/；asked → /ɑːst/（口语）",
        ),
        (
            "同化 assimilation",
            "相邻音互相影响",
            "ten bikes → /tem baɪks/；good boy → /gʊb bɔɪ/",
        ),
        (
            "缩略 contraction",
            "助动词压缩",
            "it is → it’s；they will → they’ll；I would → I’d",
        ),
        (
            "滑音 glides",
            "元音间插入 /j/ 或 /w/",
            "I agree → /aɪ j əˈɡriː/；two apples → /tuː w ˈæplz/",
        ),
    ),
    p(
        "这些现象不是「说快了才出现」，而是英语语流的常态。听的时候若逐词找音，就会「每个词都认识，整句听不懂」；正确策略是按语调单位整体识别。"
    ),
    h3("4.8 Text 1 Scanfood：带标注的朗读示范"),
    p(
        "下面按「停顿 + 调型 + 重读」标注课程朗读文本的前半段（| 短停，|| 中停，↘ 降调，↗ 升调，粗体为句中重读词）："
    ),
    p(
        "<i>ˈScanfood is a <b>ˈlarge</b> <b>ˈcompany</b> | by <b>ˈFinnish</b> <b>ˈstandards</b>. ↘ || It has <b>ˈover</b> <b>ˈ4 000</b> emˈployees. ↘ || It is <b>ˈone</b> of the <b>ˈleading</b> manuˈfacturers | of <b>ˈfoodstuffs</b> | in <b>ˈScandinavia</b> ↗, | and it has proˈduction plants | in <b>ˈseveral</b> <b>ˈplaces</b> in <b>ˈFinland</b>. ↘ || The <b>ˈhead</b> <b>ˈoffice</b> is loˈcated | <b>ˈoutside</b> <b>ˈLappeenranta</b>. ↘</i>"
    ),
    p(
        "标注背后的四个决定：① 每个语调单位一个核心重音，落在信息量最大的词上（company、standards、employees、Lappeenranta）；② 介词短语整块读，不在介词后停；③ 第二句末尾的 <i>Scandinavia</i> 用升调，因为后面还有 and 引导的并列内容；④ 每个句子结束用降调，给听者明确的收束信号。"
    ),
    p(
        "朗读时还要注意三处连读：<i>one of</i> → /ˈwʌnəv/、<i>is a</i> → /ɪzə/、<i>located outside</i> → /ləʊˈkeɪtɪd aʊtˈsaɪd/（/d/ 与 /aʊ/ 连读）。"
    ),
    h3("4.9 两次录音：怎么让对比有意义"),
    p(
        "课程的核心任务是同一段话录两次：第一次在学习之前，第二次在完成所有任务之后。第二次只能在其他任务全部完成后上传。要让对比可解释，需要固定四件事：文本、设备、环境、时长意图。"
    ),
    st(
        "第一次：不预读、不查词，按自己习惯读，保留原始状态",
        "学习中：按本讲标注重读一次，逐句改停顿与调型",
        "第二次：用同一设备、同一房间，按标注朗读，不复述第一次的错误",
        "对比：把两次录音并排听，只比较三项——停顿位置、句末调型、重读音节",
    ),
    p(
        "对比时不要听「像不像母语者」，只听三件事是否改善：该停的地方停了没有、陈述句句末降了没有、重读音节对不对。这三项改善，整段的可懂度就会明显提高。"
    ),
    h3("4.10 听懂不同口音"),
    p(
        "课程第四个目标是 <i>understand various dialects and manners of speaking English</i>。要听懂，先要知道差异在哪里："
    ),
    tb(
        ("差异", "例子", "听的时候怎么处理"),
        ("r 音发不发", "car 英 /kɑː/、美 /kɑːr/", "不要等 /r/，抓元音与重音"),
        ("元音前后", "bath 英 /bɑːθ/、美 /bæθ/", "按语境判断词，不按音判断"),
        ("t 的弱化", "water 美 /ˈwɔːdər/", "/t/ 变浊不影响识别"),
        ("语速与弱读程度", "印度英语、芬兰英语弱读较少", "抓内容词，忽略功能词"),
        ("重音位置差异", "ˈaddress / adˈdress", "以内容词与句法补足"),
    ),
    p(
        "策略是「容忍模糊」：不必每个音都听清，只要抓住语调单位里的核心重音与关键词，就能重建意思。反过来，逐词抠音会让你在第一个陌生的音上卡住，后面全丢。"
    ),
    h3("4.11 常见错误与收束"),
    tb(
        ("错误", "后果", "纠正"),
        ("每句句末都上扬", "听起来不确定、像在求同意", "陈述句与 Wh- 问句一律降调"),
        ("列举每项都降", "听者以为列举结束", "非末项升、末项降"),
        ("停顿在介词后", "句意断裂", "介词短语整块读"),
        ("逐词读、无弱读", "没有节奏，听起来像念稿", "功能词压成弱读式"),
        ("忽视连读", "语流生硬、语速上不去", "按语调单位整体练，先慢后快"),
    ),
    p(
        "四讲到这里闭环：音素决定「对不对」，重音决定「清不清楚」，语调与停顿决定「像不像话」，口音适应决定「听不听得懂」。这四项合起来，就是这门 1 学分课程想给你的全部能力。"
    ),
)

KW4 = cat(
    K(
        ("tone unit", "语调单位", "One meaning block with one pitch curve."),
        ("nucleus", "核心重音", "The last stressed word in a tone unit."),
        (
            "pausing",
            "停顿",
            "Short pauses separate tone units; long pauses separate sentences.",
        ),
        (
            "falling tone",
            "降调",
            "Statements and wh-questions end with a falling tone.",
        ),
        ("rising tone", "升调", "Yes/No questions and non-final list items rise."),
        ("fall-rise", "降升调", "Signals reservation or polite disagreement."),
        ("rise-fall", "升降调", "Signals surprise or sarcasm."),
        (
            "listing intonation",
            "列举语调",
            "Rise on each item except the last, which falls.",
        ),
        (
            "question tag",
            "反意疑问句",
            "Falling tag asks for agreement; rising tag asks a real question.",
        ),
        ("linking", "连读", "an apple → /əˈnæpl/."),
        ("elision", "省音", "next day → /neks deɪ/."),
        ("assimilation", "同化", "ten bikes → /tem baɪks/."),
        ("contraction", "缩略", "it is → it’s."),
        ("glide", "滑音", "I agree → /aɪ j əˈɡriː/."),
        ("dialect", "口音／方言", "Rhotic and non-rhotic accents differ in final /r/."),
        (
            "intelligibility",
            "可懂度",
            "The real goal: listeners understand you without effort.",
        ),
    ),
)

EX4 = cat(
    Q(
        "例 1　给下面两句标注语调单位、停顿与调型：<i>It has over 4 000 employees. It is one of the leading manufacturers of foodstuffs in Scandinavia.</i>",
        p(
            "<b>解：</b>第一句一个单位，句末降调：<i>It has ˈover ˈ4 000 emˈployees. ↘</i>"
        ),
        p(
            "第二句切三个单位：<i>It is ˈone of the ˈleading manuˈfacturers | of ˈfoodstuffs | in ˈScandinavia. ↘</i> 因为主语较长、介词短语两层，必须分块，否则一口气读完会丢重音。"
        ),
        p(
            "若这句后面还有 and 引导的并列内容，则 Scandinavia 改用升调 ↗，表示「还没完」。"
        ),
        p(
            "<b>通用思路：</b>先按意义切块（主语／谓语＋宾语／介词短语）→ 每块一个核心重音 → 句末按信息是否结束选降或升。"
        ),
    ),
    Q(
        "例 2　说明停顿如何改变 <i>I didn’t say he stole the money</i> 的意思，并各写一句语境。",
        p(
            "<b>解：</b>停顿一：<i>I didn’t say | he stole the money.</i> 意思是「我没有说（这件事）：他偷了钱」——否认自己说过这句话。语境：同事说「你昨天说他偷钱」，你否认。"
        ),
        p(
            "停顿二：<i>I didn’t say he stole | the money.</i> 意思是「我没说他偷了那笔钱」（可能偷了别的东西）——否认的是宾语。语境：调查时澄清具体对象。"
        ),
        p(
            "若把重音也移动（<i>I didn’t say HE stole the money</i>），否认的对象又变成「他」。停顿与重音是两个独立的手段，可以叠加。"
        ),
        p(
            "<b>通用思路：</b>先确定要否认的是哪个成分（整句／动作／宾语／主语），再决定停在哪里、重读哪个词。"
        ),
    ),
    Q(
        "例 3　判断下列句子的调型并说明理由：① <i>Where is the head office?</i>　② <i>Is the plug the wrong type?</i>　③ <i>We have plants in Finland, Sweden, and Norway.</i>　④ <i>It’s a large company, isn’t it?</i>（你已亲眼看到四千名员工）",
        p("<b>解：</b>① 降调 ↘：Wh- 问句问的是信息，不是 yes/no，句末下沉。"),
        p("② 升调 ↗：Yes/No 问句必须升，否则听起来像陈述。"),
        p(
            "③ 前两项升、末项降：<i>ˈFinland ↗, ˈSweden ↗, and ˈNorway ↘</i>，让听者知道列举结束。"
        ),
        p(
            "④ 降调 ↘：你已经确定，只是在寻求附和；若用升调，则表示你真的不确定，想询问对方。"
        ),
        p(
            "<b>通用思路：</b>先判句型（陈述／Wh-／Yes-No／列举／反问），再判信息状态（确定／不确定／未结束），两者共同决定调型。"
        ),
    ),
    Q(
        "例 4　找出 <i>It is one of the leading manufacturers of foodstuffs</i> 中的连读与弱读，并写出近似音标。",
        p(
            "<b>解：</b><i>It is</i> → /ɪt ɪz/，/t/ 与 /ɪ/ 连读，实际近似 /ɪtɪz/；<i>one of</i> → /ˈwʌnəv/（of 弱读为 /əv/，与 one 连读）；<i>of the</i> → /əv ðə/（the 在辅音前读 /ðə/）；<i>manufacturers of</i> → /ˌmænjuˈfæktʃərəz əv/（of 几乎完全弱化）。"
        ),
        p("整句近似：/ɪt ɪz ˈwʌn əv ðə ˈliːdɪŋ ˌmænjuˈfæktʃərəz əv ˈfuːdstʌfs/。"),
        p(
            "注意 <i>manufacturers</i> 的重音在第三音节 /ˈfæk/，不是第一音节；这也是常见的重音错位。"
        ),
        p(
            "<b>通用思路：</b>先标功能词并弱化，再看辅音＋元音的交界处连读，最后核对多音节词的重音。"
        ),
    ),
)

PR4 = cat(
    ol(
        "给 <i>The head office is located outside Lappeenranta.</i> 标停顿与调型，并说明为什么不能在 outside 后停。",
        "写出下列句子的调型：<i>Could you check the wiring?</i> / <i>When is a standstill possible?</i> / <i>Would you like tea or coffee?</i>",
        "把 <i>We have six subsidiaries: one in the USA, one in Canada and the others in Scandinavia.</i> 按列举语调标注。",
        "找出 <i>Our future looks good and we will be expanding our operations.</i> 中的缩略与弱读，并写出近似音标。",
        "用 100 字说明你会怎样安排两次录音，使对比能够说明进步。",
    ),
    D(
        "答案与思路",
        p(
            "<b>1.</b> <i>The ˈhead ˈoffice is loˈcated | ˈoutside ˈLappeenranta. ↘</i> 不能在 outside 后停，因为 outside Lappeenranta 是一个完整的介词短语，拆开会让听者以为句子在 outside 处结束。"
        ),
        p(
            "<b>2.</b> <i>Could you check the wiring? ↗</i>（请求，升调）；<i>When is a standstill possible? ↘</i>（Wh- 问句，降调）；<i>Would you like ˈtea ↗ or ˈcoffee ↘?</i>（选择疑问句，前升后降）。"
        ),
        p(
            "<b>3.</b> <i>one in the ˈUSA ↗, | one in ˈCanada ↗, | and the ˈothers in Scanˈdinavia ↘.</i> 前三项升，末项降；每个列举项可作为一个语调单位。"
        ),
        p(
            "<b>4.</b> <i>we will</i> → <i>we’ll</i> /wɪl/ 或 /wl/；<i>and</i> → /ən/；<i>our</i> → /ɑː/ 或 /ə/；<i>operations</i> 重音在第三音节 /ˌɒpəˈreɪʃnz/。整句近似 /ɑː ˈfjuːtʃə lʊks ˈɡʊd ən wɪl bi ɪkˈspændɪŋ ɑːr ˌɒpəˈreɪʃnz/。"
        ),
        p(
            "<b>5.</b> 参考：同一段文本、同一设备与房间；第一次不预读，第二次按标注朗读；只比较停顿位置、句末调型、重读音节三项；中间隔至少两周，避免短期记忆影响；文件按 first／final 命名，便于并排回听。"
        ),
    ),
)

EM4 = cat(
    cal(
        "exam",
        "必考",
        "语调单位的划分与核心重音；三档停顿与记号；降调／升调／降升调的功能；列举与选择疑问句的语调；反意疑问句的两种语调；连读、省音、同化、缩略四类音变；Text 1 的朗读任务。",
    ),
    cal(
        "warn",
        "易错 1",
        "陈述句句末上扬（听起来不确定），Yes/No 问句句末下降（听起来像陈述）。",
    ),
    cal("warn", "易错 2", "列举每项都降，或在介词与宾语之间停顿，导致意义断裂。"),
    cal("warn", "易错 3", "逐词朗读、不做弱读与连读，语流生硬，语速上不去。"),
    cal(
        "tip",
        "进阶",
        "用降升调表达保留（It’s possible ↘↗），在会议与答辩里比直接否定更专业，也更难被追问。",
    ),
)

CL4 = cat(
    h2("本讲方法清单"),
    h3("朗读四步标注法"),
    st(
        "按意义切块，用 | 与 || 标出短停与中停",
        "每块圈一个核心重音（信息量最大的词）",
        "句末标 ↘ 或 ↗，列举的非末项标 ↗",
        "标出连读与弱读处，录音后按「停顿／调型／重音」三项自评",
    ),
    h3("语调选择三问"),
    ck(
        "这是陈述还是提问（Yes/No 问句必须升）",
        "信息结束了没有（未结束用升，结束用降）",
        "我确定还是在留余地（确定用降，保留用降升）",
    ),
)

MP4 = tb(
    ("源文件", "位置 / 页码", "覆盖内容"),
    (
        "4_3. Phonemes, stress and intonation/7_19. Read and record the story…/Text 1 Scanfood new.pdf",
        "p1",
        "朗读全文：公司规模、员工数、行业地位、总部位置、历史、产品、出口与子公司",
    ),
    (
        "2_1. Instructions and introductions/1_Course Preamble - Read and Sign/…html",
        "Objectives 与 How it works 两节",
        "目标三（pausing and intonation for effect）、目标四（understand various dialects）、两次录音设计",
    ),
    (
        "2_1. Instructions and introductions/2_Technical matters.html",
        "全篇",
        "录音与提交的技术要求，用于本讲的录音任务",
    ),
    ("（跳过）", "—", "重复副本 Text 1 Scanfood new.pdf 不再单独设知识点"),
    (
        "（拓展）",
        "—",
        "调型功能表、列举与选择题语调、反意疑问句两种语调、四类语流音变、口音差异表为教学补充，原文只给朗读任务与目标",
    ),
)

LEC.append(
    L(
        slug="p4-intonation-pausing",
        tzh="第 4 讲 · 语调、停顿与语流",
        ten="Intonation, Pausing and Connected Speech",
        keywords=[
            "tone unit",
            "pausing",
            "falling tone",
            "rising tone",
            "fall-rise",
            "linking",
            "elision",
            "dialect",
        ],
        files=[
            "4_3. Phonemes, stress and intonation_7_19. Read and record the story___pausing, pitch and intonation_intro_Text 1 Scanfood new.pdf",
            "2_1. Instructions and introductions_1_Course Preamble - Read and Sign_1_Course Preamble - Read and Sign.html",
        ],
        overview=OV4,
        detail=DT4,
        kws=KW4,
        examples=EX4,
        practice=PR4,
        exam=EM4,
        checklist=CL4,
        mapping=MP4,
    )
)

emit(
    "32667",
    10,
    "KE00BX35 英语语音",
    "English Pronunciation",
    "KE00BX35 英语语音",
    "1 学分、约 27 小时的自主进度发音课，按「音素—重音—语调—口音」四步推进：先用 IPA 与最小对立对纠正辅音元音，再练词重音与句子节奏，最后用停顿、调型与语流音变完成整段朗读。考核为 pass/fail，核心任务是同一段话在学期初与学期末各录一次。",
    LEC,
)
