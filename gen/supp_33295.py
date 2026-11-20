# -*- coding: utf-8 -*-
"""芬兰语 1 · 补充讲：作业与词汇表（只追加 1 讲，不改动已有讲次）"""

import os
import sys
import json
import io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, code, chips  # noqa: E402

CID = "33295"
PATH = os.path.join(SITE, "content", CID + ".json")

data = json.load(io.open(PATH, encoding="utf-8"))

overview = (
    h2("本节定位")
    + p(
        "前面 12 讲按 Tunti 顺序讲语法与课文；这一讲把散落在 Moodle 作业区的 <b>7 次 KOTITEHTÄVÄ（作业）</b>与 <b>5 份 Sanasto（词汇表）</b>收拢起来，"
        "因为它们才是考试里「填空、变格、写问句、翻译」的直接题库。"
    )
    + p("学完本节你应当能够：")
    + ck(
        "默写问候、近况、国家、家庭四组词汇，并给每个词标出词性与格",
        "判断一个词该用 a 还是 ä，并据此选 -ssa/-ssä、-lainen/-läinen",
        "用 kuka / mikä / missä / milloin / mitä / millainen 各写两个正确问句",
        "把 24 个常用动词按第一类动词变位，并说明哪些常带 partitive 宾语",
        "用 Opiskelen + partitive / translative 回答「你学什么、你做什么」",
    )
    + p(
        "与前后讲的衔接：第 1–8 讲的语法在这里被「作业化」；第 12 讲 Kertaus 的考试题型，绝大部分就来自这些作业的原题。"
    )
)

detail = (
    h3("1. 七次作业的清单与考点")
    + p(
        "课程共布置 7 次作业，全部是「查词典 + 填表 + 造句」型任务，看起来简单，但每次都在练一个具体语法点："
    )
    + tb(
        ("作业", "主题", "练的语法点", "对应讲次"),
        (
            "KOTITEHTÄVÄ 1",
            "Tervehdykset 问候语",
            "固定表达、正式/口语双版本",
            "第 1–2 讲",
        ),
        ("KOTITEHTÄVÄ 2", "Sanasto: miten menee", "状态句、partitive 宾语", "第 3 讲"),
        ("KOTITEHTÄVÄ 3", "Vokaaliharmonia 元音和谐", "a/ä 选择、-ssa/-ssä", "第 3 讲"),
        ("KOTITEHTÄVÄ 4", "Sanasto: maat 国家", "-lainen/-läinen 派生", "第 5 讲"),
        ("KOTITEHTÄVÄ 5", "Kirjoita kysymys 写问句", "疑问词 + 语序", "第 5 讲"),
        ("KOTITEHTÄVÄ 6", "Sanasto: verbejä 动词", "第一类动词变位", "第 6 讲"),
        (
            "KOTITEHTÄVÄ 7",
            "Sanasto: Viljalan perhe 家庭",
            "属格与所有格后缀",
            "第 8 讲",
        ),
    )
    + cal(
        "tip",
        "怎么用这份清单",
        "把上表当成复习索引：考试前每一行读一遍，能在 30 秒内说出该行的规则和一个例句，就算过关。",
    )
    + h3("2. 词汇表一：问候（Tervehtiminen）")
    + p(
        "芬兰语问候有<b>正式</b>与<b>口语</b>两套，同一个意思往往两个词。正式场合用长版本，同学之间用短版本。"
    )
    + tb(
        ("Suomi", "中文", "English"),
        ("Hei! / Moi!", "嗨！/ 你好！", "Hi! / Hello!"),
        ("Hyvää huomenta! / Huomenta!", "早上好！", "Good morning!"),
        ("Hyvää päivää! / Päivää!", "你好！（白天通用，较正式）", "Good day! / Hello!"),
        ("Hyvää iltaa! / Iltaa!", "晚上好！", "Good evening!"),
        ("Hyvää yötä! / Yötä!", "晚安！（睡前）", "Good night!"),
        ("Ole hyvä!", "请 / 给你", "Here you are! / Please!"),
        ("Kiitos!", "谢谢！", "Thank you!"),
        ("Anteeksi! / Sori!", "对不起 / 打扰一下", "Excuse me! / Sorry!"),
        ("Anteeksi, että olen myöhässä.", "抱歉我迟到了", "Sorry that I am late."),
        ("Olen pahoillani!", "我很抱歉（更重）", "I am sorry."),
        ("Ei se mitään!", "没关系！", "It is all right! / Never mind!"),
        ("Onnea!", "恭喜 / 祝好运", "Congratulations!"),
        ("Onneksi olkoon!", "恭喜你（更正式）", "Congratulations to you!"),
        ("Hyvää ruokahalua!", "祝用餐愉快", "Enjoy your meal!"),
        ("Hauska tavata!", "很高兴见到你", "Nice to meet you!"),
        ("Näkemiin!", "再见（正式）", "Goodbye!"),
        ("Hei hei! / Moi moi!", "拜拜（口语）", "Bye bye!"),
    )
    + cal(
        "warn",
        "易错",
        "「Hyvää päivää」直译是「好日子」，不是「下午好」；芬兰语没有按小时切分的下午问候，白天一律 päivää。另外 <code>kiitos</code> 回答「不用谢」是 <code>ole hyvä</code> 或 <code>ei kestä</code>。",
    )
    + h3("3. 词汇表二：Miten menee?（近况问答）")
    + p(
        "<code>Miten menee?</code> 是「最近怎么样」，比 <code>Mitä kuuluu?</code> 更口语。回答常用「副词 + 形容词」的短句，"
        "而 <code>väsynyt</code>（累）这类形容词在 partitive 句里要注意宾语格。"
    )
    + tb(
        ("Suomi", "中文", "English"),
        ("Miten menee?", "你过得怎么样？", "How are you doing?"),
        ("mennä (menee)", "去、进行", "to go (goes)"),
        ("sinä (sinulla)", "你（你身上有…）", "you (at you = you have)"),
        ("ihan", "相当、完全", "quite"),
        ("vähän", "有一点", "a little"),
        ("väsynyt", "累的", "tired"),
        ("yrittää (yritä)", "尝试", "to try (try!)"),
        ("levätä", "休息", "to rest"),
        ("joo", "是啊（口语）", "yeah"),
    )
    + p(
        "典型对话：<code>— Miten menee? — Ihan hyvin, kiitos. Entä sinulle?</code>（挺好，谢谢，你呢？）"
        "注意 <code>Entä sinulle?</code> 用 allative，因为「对谁而言」是 <code>sinulle</code>。"
    )
    + h3("4. 词汇表三：国家（Maat）与国籍派生")
    + p(
        "国家名要会认，更重要的是会派生「哪国人」：词尾加 <code>-lainen</code> 或 <code>-läinen</code>，"
        "选择依据仍是元音和谐。"
    )
    + tb(
        ("Maa 国家", "中文", "国籍 -lainen/-läinen"),
        ("Suomi", "芬兰", "suomalainen"),
        ("Ruotsi", "瑞典", "ruotsalainen"),
        ("Venäjä", "俄罗斯", "venäläinen"),
        ("Viro", "爱沙尼亚", "virolainen"),
        ("Saksa", "德国", "saksalainen"),
        ("Iso-Britannia", "英国", "brittiläinen"),
        ("Irlanti", "爱尔兰", "irlantilainen"),
        ("Brasilia", "巴西", "brasilialainen"),
        ("Yhdysvallat", "美国", "yhdysvaltalainen / amerikkalainen"),
        ("Kiina", "中国", "kiinalainen"),
        ("Japani", "日本", "japanilainen"),
        ("Etelä-Korea", "韩国", "eteläkorealainen / korealainen"),
        ("Thaimaa", "泰国", "thaimaalainen"),
        ("Intia", "印度", "intialainen"),
        ("Pakistan", "巴基斯坦", "pakistanilainen"),
        ("Saudi-Arabia", "沙特阿拉伯", "saudiarabialainen"),
        ("Egypti", "埃及", "egyptiläinen"),
        ("Sudan", "苏丹", "sudanilainen"),
        ("Etelä-Afrikka", "南非", "eteläafrikkalainen"),
    )
    + cal(
        "tip",
        "记忆法",
        "先看词里有没有 ä/ö/y：<code>Venäjä → venäläinen</code>、<code>Egypti → egyptiläinen</code> 走前元音；"
        "其余走 <code>-lainen</code>。复合国名（Etelä-Korea、Etelä-Afrikka）按<b>后半部分</b>定元音和谐。",
    )
    + h3("5. 词汇表四：24 个常用动词（Verbejä）")
    + p(
        "这份表是第 6 讲「第一类动词」的题库。第一类动词以两个元音结尾（-aa/-ää、-ua/-yä、-ia/-iä 等），"
        "变位时去掉最后一个元音再加人称词尾：<code>puhua → puhun, puhut, puhuu, puhumme, puhutte, puhuvat</code>。"
    )
    + tb(
        ("Verbi", "中文", "English"),
        ("puhua", "说、讲", "to speak"),
        ("sanoa", "说（某内容）", "to say"),
        ("asua", "住", "to live (reside)"),
        ("katsoa televisiota", "看电视", "to watch TV"),
        ("kysyä", "问", "to ask"),
        ("ymmärtää", "理解", "to understand"),
        ("istua", "坐", "to sit"),
        ("seisoa", "站", "to stand"),
        ("ostaa", "买", "to buy"),
        ("maksaa", "付钱、花费", "to pay / cost"),
        ("kirjoittaa", "写", "to write"),
        ("lukea", "读", "to read"),
        ("nauraa", "笑", "to laugh"),
        ("itkeä", "哭", "to cry"),
        ("tanssia", "跳舞", "to dance"),
        ("laulaa", "唱歌", "to sing"),
        ("rakastaa", "爱", "to love"),
        ("etsiä", "寻找", "to search for"),
        ("saunoa", "蒸桑拿", "to bathe in sauna"),
        ("ajaa pyörällä", "骑自行车", "to ride a bike"),
        ("matkustaa", "旅行", "to travel"),
        ("odottaa", "等待", "to wait for"),
        ("harrastaa", "业余从事、爱好", "to do as a hobby"),
        ("kalastaa", "钓鱼", "to fish"),
    )
    + cal(
        "warn",
        "易错",
        "<code>sanoa</code> 的变位是 <code>sanon, sanot, sanoo, sanomme, sanotte, sanovat</code>（词干 sana- 加人称词尾，第一人称 -n）；"
        "<code>lukea → luet</code>（k 变弱为无）；<code>itkeä → itken</code>。这些都是 KPT 辅音交替，考试常挖空。",
    )
    + p(
        "哪些动词常带 partitive 宾语：<code>rakastaa</code>（rakastan sinua）、<code>odottaa</code>（odotan sinua）、"
        "<code>etsiä</code>（etsin avainta）、<code>katsoa</code>（katson televisiota）。原因是动作不指向「完整结果」。"
    )
    + h3("6. 词汇表五：家庭（Viljalan perhe）")
    + tb(
        ("Suomi", "中文", "English"),
        ("perhe", "家庭", "family"),
        ("naimisissa", "已婚的", "married"),
        ("vaimo", "妻子", "wife"),
        ("aviomies", "丈夫", "husband"),
        ("lapsi", "孩子", "child"),
        ("lähellä", "在附近", "near"),
        ("vanhemmat", "父母", "parents"),
        ("äiti", "母亲", "mother"),
        ("isä", "父亲", "father"),
        ("isoäiti", "祖母 / 外祖母", "grandmother"),
        ("isoisä", "祖父 / 外祖父", "grandfather"),
        ("kohta", "马上、不久", "soon"),
        ("lapsenlapsi", "孙辈", "grandchild"),
        ("sisko", "姐妹", "sister"),
    )
    + p(
        "家庭词汇的语法价值在于<b>属格</b>：<code>Viljalan perhe</code>（Viljala 家的家庭）、"
        "<code>minun äitini</code>（我的母亲）、<code>hänen isänsä</code>（他的父亲）。"
        "属格词干 + 所有格后缀是第 8 讲的重点，作业里的每个家庭词都可以拿来造句。"
    )
    + h3("7. 元音和谐作业（KOTITEHTÄVÄ 3）逐空讲解")
    + p(
        "规则：一个<b>非复合词</b>里，前元音 ä/ö/y 与后元音 a/o/u 不能混用；后缀跟着词里最后一个元音走。"
        "i、e 是中性元音，不决定方向。"
    )
    + tb(
        ("题目", "答案", "理由"),
        ("__uto", "auto（车）", "只有后元音 u、o，用 a"),
        ("__äni", "ääni（声音）", "已有 ä，用 ä"),
        ("k__iku", "kaiku（回声）", "ai + u，全是后元音，用 a"),
        ("__iti", "äiti（母亲）", "首音节是 ä"),
        ("rak__s", "rakas（亲爱的）", "a 为后元音"),
        ("vied___", "viedä / viedään", "词干含 e、ä；主动式 viedä 与被动式 viedään 都取前元音"),
    )
    + p(
        "例外与复合词：<code>olympialaiset</code>（奥运会）虽含 a/i 却仍用 a，因为它是外来词；"
        "<code>polkupyörä</code>（自行车）是 polku + pyörä 的复合词，后缀按<b>最后一个成分</b> pyörä 走，所以是 <code>polkupyörässä</code>。"
    )
    + p("配套练习 <code>-ssa / -ssä</code>（在……里）：")
    + tb(
        ("词", "入格", "说明"),
        ("metsä", "metsässä", "ä → ssä"),
        ("talo", "talossa", "a/o/u → ssa"),
        ("keittiö", "keittiössä", "ö → ssä"),
        ("kylppäri", "kylppärissä", "ä → ssä"),
        ("koulu", "koulussa", "u → ssa"),
        ("sala", "salassa", "a → ssa"),
    )
    + h3("8. 写问句作业（KOTITEHTÄVÄ 5）")
    + p(
        "六个疑问词各写两句：<code>kuka</code>（谁）、<code>mikä</code>（什么/哪个）、<code>missä</code>（哪里）、"
        "<code>milloin</code>（何时）、<code>mitä</code>（什么，partitive）、<code>millainen</code>（什么样的）。"
    )
    + p(
        "语序：疑问词 + 谓语 + 主语 + 其余。芬兰语没有 do 支持，直接把疑问词放句首即可。"
    )
    + tb(
        ("疑问词", "作业例句", "中文"),
        ("Kuka", "Kuka sinä olet?", "你是谁？"),
        ("Kuka", "Kuka on opettaja?", "谁是老师？"),
        ("Mikä", "Mikä tämä on?", "这是什么？"),
        ("Mikä", "Mikä tuo on?", "那是什么？"),
        ("Missä", "Missä koulu on?", "学校在哪里？"),
        ("Missä", "Missä sinä asut?", "你住在哪里？"),
        ("Milloin", "Milloin sinä tulet?", "你什么时候来？"),
        ("Milloin", "Milloin on ruoka-aika?", "什么时候是吃饭时间？"),
        ("Mitä", "Mitä sinä teet?", "你在做什么？"),
        ("Millainen", "Millainen päivä on tänään?", "今天是什么样的日子？"),
    )
    + cal(
        "warn",
        "易错",
        "作业提交里出现过 <code>Kuka on sinä?</code>，这是错的：<code>sinä</code> 是主语代词，应写 <code>Kuka sinä olet?</code>。"
        "只有当主语是名词短语时才说 <code>Kuka on opettaja?</code>。另外 <code>Missä koulu on?</code> 与 <code>Missä on koulu?</code> 都对，前者把已知的「学校」放焦点位置。",
    )
    + h3("9. Mitä sinä opiskelet?（你学什么）")
    + p(
        "这份课件给两组回答模板：说<b>领域</b>用 partitive，说<b>职业/学位</b>用 translative <code>-ksi</code>。"
    )
    + tb(
        ("Ala 领域", "回答", "中文"),
        ("kauppatiede", "Opiskelen kauppatiedettä.", "我学商科"),
        ("logistiikka", "Opiskelen logistiikkaa.", "我学物流"),
        ("sähkötekniikka", "Opiskelen sähkötekniikkaa.", "我学电气工程"),
        ("energiatekniikka", "Opiskelen energiatekniikkaa.", "我学能源工程"),
        ("ympäristötekniikka", "Opiskelen ympäristötekniikkaa.", "我学环境工程"),
        ("tuotantotalous", "Opiskelen tuotantotaloutta.", "我学工业管理"),
        ("yhteiskuntatieteet", "Opiskelen yhteiskuntatieteitä.", "我学社会科学"),
    )
    + tb(
        ("Ammatti / tutkinto", "回答", "中文"),
        ("fysioterapeutti", "Opiskelen fysioterapeutiksi.", "我在读物理治疗"),
        ("ensihoitaja", "Opiskelen ensihoitajaksi.", "我在读急救护理"),
        ("sairaanhoitaja", "Opiskelen sairaanhoitajaksi.", "我在读护理"),
        ("insinööri", "Opiskelen konetekniikan insinööriksi.", "我在读机械工程工程师"),
        ("rakennusmestari", "Opiskelen rakennusmestariksi.", "我在读建筑工长"),
        ("muotoilija", "Opiskelen muotoilijaksi.", "我在读设计"),
        ("tradenomi", "Opiskelen tradenomiksi.", "我在读工商管理学士"),
        ("medianomi", "Opiskelen medianomiksi.", "我在读媒体学士"),
    )
    + p(
        "地点回答：<code>Opiskelen LUT-yliopistossa eli LUTissa. Opiskelen Lappeenrannan kampuksella Skinnarilassa.</code>"
        "（我在 LUT 大学，也就是 LUT，在拉彭兰塔校区 Skinnarila。）注意 <code>eli</code> = 「也就是」，用来给缩写下定义。"
    )
    + h3("10. 作业提交与批改注意事项")
    + ul(
        "<code>Submissions</code> 目录里的 PDF 只有一页图像、没有文字层（抽取字数 5），说明是拍照/扫描提交；考试不会考提交格式，但作业分会计。",
        "同名文件常出现两个版本：<code>KOTITEHTÄVÄ, vokaaliharmonia.docx</code> 是空白题面，<code>KOTITEHTÄVÄ,_vokaaliharmonia.docx</code> 是已填写版；复习看填写版。",
        "查词典时保留原形与变位形两栏，考试写变格时直接从自己的表里取，比临场推更稳。",
    )
)

kws = tb(
    ("Suomi / English", "中文", "说明 / 例句"),
    ("tervehtiminen / greeting", "问候", "Hei! Hyvää päivää!"),
    ("vokaaliharmonia / vowel harmony", "元音和谐", "talossa 但 metsässä"),
    ("partitiivi / partitive", "部分格", "Opiskelen kauppatiedettä."),
    ("translatiivi / translative (-ksi)", "变成格", "Opiskelen insinööriksi."),
    ("inessiivi / inessive (-ssa/-ssä)", "在内格", "koulussa, metsässä"),
    ("allatiivi / allative (-lle)", "向格", "Entä sinulle?"),
    ("genetiivi / genitive", "属格", "Viljalan perhe, minun äitini"),
    ("kysymyssana / question word", "疑问词", "kuka, mikä, missä, milloin"),
    ("verbityyppi 1", "第一类动词", "puhua → puhun"),
    ("kotitehtävä / homework", "作业", "KOTITEHTÄVÄ 1–7"),
    ("sanasto / vocabulary", "词汇表", "Sanasto, Verbejä"),
    ("maa / country", "国家", "Suomi, Ruotsi, Kiina"),
    ("kansallisuus / nationality", "国籍", "suomalainen, kiinalainen"),
    ("ammatti / profession", "职业", "tradenomi, insinööri"),
    ("opiskella / to study", "学习", "Opiskelen LUTissa."),
    ("perhe / family", "家庭", "Viljalan perhe"),
)

examples = (
    h2("例题 1：元音和谐填空")
    + qa(
        "把 <code>k__iku</code>、<code>vied___</code> 补全，并说明为什么不能互换。",
        p(
            "第一步，找出词里已有的元音。<code>k?iku</code> 的元音是 i、u，其中 u 是后元音，i 中性，所以只能填 a：<code>kaiku</code>。"
        )
        + p(
            "第二步，<code>vied-</code> 的元音是 i、e、ä，ä 是前元音，所以补 ä（构成 viedä「带走」或 viedään「被带走」）。"
        )
        + p(
            "第三步，检查是不是复合词。若不是，前后元音不能混用；若是（如 polkupyörä），按最后一个成分定。"
        )
        + cal(
            "tip",
            "通用解法",
            "看词内元音 → 找最后一个 a/o/u 或 ä/ö/y → 同向填 → 排除复合词与外来词例外。",
        ),
    )
    + h2("例题 2：-ssa 还是 -ssä")
    + qa(
        "给 metsä、keittiö、koulu 加「在……里」的格尾。",
        p("<code>metsä</code>：最后一个元音 ä → <code>metsässä</code>。")
        + p("<code>keittiö</code>：ö → <code>keittiössä</code>。")
        + p("<code>koulu</code>：u → <code>koulussa</code>。")
        + p(
            "注意 <code>kylppäri</code> 虽以 i 结尾，但词里有 ä → <code>kylppärissä</code>，不要被词尾 i 骗。"
        ),
    )
    + h2("例题 3：写问句")
    + qa(
        "用 kuka 和 milloin 各写一个问句，并改正 <code>Kuka on sinä?</code>。",
        p("<code>Kuka sinä olet?</code>（你是谁？）——主语代词紧跟疑问词，动词最后。")
        + p(
            "<code>Milloin sinä tulet?</code>（你什么时候来？）——时间疑问词 + 主语 + 动词。"
        )
        + p(
            "错句 <code>Kuka on sinä?</code> 的问题是把 <code>sinä</code> 当成名词短语；代词作主语时不能这样倒装。"
        ),
    )
    + h2("例题 4：你学什么")
    + qa(
        "用 kauppatiede 和 tradenomi 各造一句「我在学……」。",
        p(
            "领域用 partitive：<code>Opiskelen kauppatiedettä.</code>（kauppatiede → kauppatiedettä，-e 变 -että）。"
        )
        + p(
            "学位/职业用 translative：<code>Opiskelen tradenomiksi.</code>（tradenomi → tradenomiksi）。"
        )
        + p(
            "判断口诀：说「学科内容」问 what → partitive；说「成为什么」问 become → -ksi。"
        ),
    )
)

practice = (
    h2("练习")
    + p(
        "1. 填空：<code>Minä asun ___(Suomi)</code>、<code>Minä puhun ___(suomi)</code>。"
    )
    + det(
        "答案与思路",
        p(
            "<code>Suomessa</code>（国家用 inessive）；<code>suomea</code>（语言用 partitive）。"
            "规律：住在某国用 -ssa/-ssä，说某语言用 partitive。"
        ),
    )
    + p("2. 变位：puhua、lukea、itkeä 的六个人称形式。")
    + det(
        "答案与思路",
        p(
            "<code>puhun, puhut, puhuu, puhumme, puhutte, puhuvat</code>；"
            "<code>luen, luet, lukee, luemme, luette, lukevat</code>；"
            "<code>itken, itket, itkee, itkemme, itkette, itkevät</code>。"
            "注意 KPT：lukea 的 k 在第一、二人称消失。"
        ),
    )
    + p(
        "3. 改错：<code>Kuka on sinä?</code> / <code>Missä sinä asut?</code> / <code>Minä opiskelen kauppatiede.</code>"
    )
    + det(
        "答案与思路",
        p(
            "第一句改 <code>Kuka sinä olet?</code>；第二句正确；第三句宾语要用 partitive："
            "<code>Opiskelen kauppatiedettä.</code>"
        ),
    )
    + p("4. 翻译：我的母亲住在芬兰，她的名字是 Liisa。")
    + det(
        "答案与思路",
        p(
            "<code>Minun äitini asuu Suomessa, ja hänen nimensä on Liisa.</code>"
            "所有格后缀 -ni/-nsä 加在属格词干后；<code>nimi → nimensä</code>。"
        ),
    )
    + p("5. 用五个不同疑问词各写一句关于同学的问题。")
    + det(
        "答案与思路",
        p(
            "示例：<code>Kuka hän on?</code> / <code>Mitä hän opiskelee?</code> / "
            "<code>Missä hän asuu?</code> / <code>Milloin hän tulee?</code> / <code>Millainen hän on?</code>"
        ),
    )
)

exam = (
    h2("考点与难点")
    + cal(
        "exam",
        "必考（几乎每年都出）",
        ul(
            "四组词汇的拼写与意思：问候、近况、国家、家庭",
            "元音和谐：a/ä 填空、-ssa/-ssä、-lainen/-läinen",
            "六个疑问词造句与语序",
            "第一类动词六人称变位（含 KPT 交替）",
            "Opiskelen + partitive / translative 的区分",
        ),
    )
    + cal(
        "warn",
        "易错（改错题高发）",
        ul(
            "<code>Kuka on sinä?</code> 语序错误",
            "国家名用 -ssa，语言用 partitive（Suomessa / suomea）",
            "复合词元音和谐按最后成分（polkupyörässä）",
            "外来词例外（olympialaiset）",
            "<code>lukea</code> 的 k 在第一、二人称脱落",
        ),
    )
    + cal(
        "tip",
        "进阶（拉开分差）",
        p(
            "能把 <code>-ksi</code>、<code>-lle</code>、属格后缀放进同一个句子里，例如："
            "<code>Minä opiskelen insinööriksi, ja minun siskoni opiskelee lääkäriksi.</code>"
            "说明你已理解「变成」与「所属」两套格。"
        ),
    )
)

checklist = h2("方法清单") + st(
    "读题先圈出词性：名词？动词？形容词？",
    "名词先定数（单/复）再定格（-ssa / -ssä / -lle / -ksi / 属格）",
    "看到 a/ä 犹豫时，回看词内最后一个元音，而不是词尾",
    "动词先判断类型，再去掉词尾元音加人称",
    "写问句用「疑问词 + 主语 + 动词 + 其余」模板",
    "交作业前对照本讲词汇表逐条自查拼写（尤其 ä/ö）",
)

mapping = (
    h2("源文件对应")
    + tb(
        ("补充文件", "位置", "覆盖内容"),
        (
            "KOTITEHTÄVÄ 1 + Sanasto, Tervehdykset",
            "Tunti 1 / 根目录",
            "第 2 节问候词汇表（17 条，含提交版中英对照）",
        ),
        ("KOTITEHTÄVÄ 2 + Sanasto, miten menee", "Tunti 3", "第 3 节近况词汇与对话"),
        (
            "KOTITEHTÄVÄ 3 Vokaaliharmonia",
            "Tunti 3",
            "第 7 节元音和谐逐空讲解、-ssa/-ssä",
        ),
        ("KOTITEHTÄVÄ 4 + Sanasto, maat", "Tunti 5", "第 4 节国家与国籍派生"),
        ("KOTITEHTÄVÄ 5 Kirjoita kysymys", "Tunti 5", "第 8 节疑问词与语序"),
        (
            "KOTITEHTÄVÄ 6 + Sanasto, Verbejä",
            "Tunti 6",
            "第 5 节 24 个动词与第一类变位",
        ),
        ("KOTITEHTÄVÄ 7 + Sanasto, Viljalan perhe", "Tunti 8", "第 6 节家庭词汇与属格"),
        (
            "Mitä sinä opiskeletS2022.pptx",
            "Tunti 6",
            "第 9 节领域 partitive 与职业 -ksi",
        ),
        (
            "202609231415.pdf / 202609301402.pdf",
            "Tunti 5、6 提交",
            "无文字层（扫描件），仅确认提交存在，不据此推断内容",
        ),
    )
    + p(
        "<b>重复副本</b>：带下划线前缀的 docx 与根目录同名文件内容一致，按内容 md5 去重，只算一份。"
        "<b>拓展</b>：国籍派生表、动词宾格说明为本讲补充的背景知识，不改变课程原有考点。"
    )
)

lec = L(
    slug="supp-homework-vocab",
    tzh="补充 · 七次作业与五份词汇表",
    ten="Homework Sets and Vocabulary Lists",
    keywords=[
        "kotitehtävä",
        "sanasto",
        "vokaaliharmonia",
        "partitiivi",
        "translatiivi",
        "inessiivi",
        "kysymyssana",
        "verbityyppi 1",
        "kansallisuus",
        "perhe",
    ],
    files=[
        "KOTITEHTÄVÄ, kysymykset.docx",
        "KOTITEHTÄVÄ, vokaaliharmonia.docx",
        "Sanasto, Tervehdykset-korjattu.docx",
        "Sanasto, miten menee.docx",
        "Sanasto, maat.docx",
        "Sanasto, Verbejä.docx",
        "Sanasto,  Viljalan perhe.docx",
        "Mitä sinä opiskeletS2022.pptx",
    ],
    overview=overview,
    detail=detail,
    kws=kws,
    examples=examples,
    practice=practice,
    exam=exam,
    checklist=checklist,
    mapping=mapping,
)

if not any(x.get("slug") == lec["slug"] for x in data["lectures"]):
    data["lectures"].append(lec)

with io.open(PATH, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

print("ok", len(data["lectures"]), len(lec["html"]))
