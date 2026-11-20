# -*- coding: utf-8 -*-
"""K200DJ99 芬兰语2（Finnish 2）逐讲讲义生成脚本。

源文本：text/34583/*.txt（由 学习资料/K200DJ99 芬兰语2/ 下的 pdf、docx、pptx、html 抽取）
产出：content/34583.json
"""

import os
import sys

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

LEC = []

# ============================================================ 第 1 讲
LEC.append(
    L(
        slug="t1-intro-numbers",
        tzh="第 1 讲 · 自我介绍、数字与存在句",
        ten="Introducing Yourself, Numbers and the Existential Sentence",
        keywords=[
            "personal pronouns",
            "question word",
            "cardinal number",
            "existential sentence",
            "partitive",
            "essive ending",
            "language name",
        ],
        files=[
            "02_Tunti 1/1_PUHU UUDELLE PARILLE.html",
            "02_Tunti 1/2_Numerot, bingo.docx",
            "02_Tunti 1/3_PUHU PARILLE Kuinka monta_.html",
            "02_Tunti 1/4_PUHU PARILLE Onko sinulla_.html",
        ],
        overview=(
            h2("本节定位")
            + p(
                "这是 K200DJ99 的第一讲。课程从「把自己说清楚」开始：姓名怎么写、从哪来、住在哪、学什么、家里有什么人。这些看似简单的问答，其实一次性把三个最核心的格（-sta/-stä、-ssa/-ssä、部分格 -a/-ä）和数字系统都带了出来，后面十讲都在反复使用它们。"
            )
            + p(
                "本讲对应 Tunti 1 的四份口语卡与数字练习。它不涉及动词变位体系（那是第 5、7 讲的内容），只要求把 <code>olen</code>、<code>asun</code>、<code>puhun</code>、<code>opiskelen</code>、<code>minulla on</code> 这几组高频形式当成整块记住。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "用十二个标准问句完成一段 1 分钟的芬兰语自我介绍，并听懂对方的同类提问",
                "读出 0–1000 之间的任意整数，说出电话号码与门牌号的读法习惯",
                "用 <code>Minulla on …</code> / <code>Minulla ei ole …</code> 说明拥有与不拥有，并知道否定句里名词要变部分格",
                "回答 <code>Kuinka monta … on?</code> 这类「有多少」的问题，把被数名词放进部分格单数",
                "区分「来自某国」（-sta/-stä）、「住在某地」（-ssa/-ssä）、「说某语言」（-a/-ä）三种不同后缀",
            )
        ),
        detail=(
            h3("1.1 这一讲在整门课里的位置")
            + p(
                "芬兰语入门课的第一次课通常不做语法体系，而是先给一批「能立刻用」的句子。Tunti 1 的四份材料正好构成一个闭环：先问个人信息（PUHU UUDELLE PARILLE），再补数字（Numerot, bingo），然后用数字去数教室里的东西（Kuinka monta），最后落到「你有没有……」这种拥有句（Onko sinulla）。"
            )
            + p(
                "从语法角度看，这四份材料合起来已经暴露了本课程最重要的一个事实：<b>芬兰语的名词在句子里几乎不会以词典形式出现</b>。同一个「书」在「这是一本书」里是 <code>kirja</code>，在「我来自……」里可能带 -sta，在「我没有书」里变成 <code>kirjaa</code>。第一讲的任务不是背下所有变化，而是先建立这个警觉。"
            )
            + h3("1.2 十二个自我介绍问句与答句模板")
            + p(
                "下面这张表是 Tunti 1 口语卡的全部内容。左边是问句，中间是可以直接套用的答句模板，右边标出这一问涉及的语法点。模板里的下划线表示要替换成自己的信息。"
            )
            + tb(
                ("问句", "答句模板", "语法点"),
                (
                    "Mikä sinun nimi on?",
                    "Minun nimi on ______ .",
                    "属格 <code>sinun</code>、<code>minun</code> 作定语",
                ),
                (
                    "Miten se tavataan/kirjoitetaan?",
                    "Minun nimi tavataan/kirjoitetaan (A-N-N-A).",
                    "被动式 <code>tavataan</code>、<code>kirjoitetaan</code> 作固定说法",
                ),
                (
                    "Kuinka vanha sinä olet?",
                    "Minä olen ______ vuotta.",
                    "年龄用部分格 <code>vuotta</code>，不用 <code>vuosi</code>",
                ),
                (
                    "Mistä maasta sinä olet kotoisin?",
                    "Minä olen kotoisin ______ -sta/-stä.",
                    "出处格 -sta/-stä",
                ),
                (
                    "Mitä kieliä sinä puhut?",
                    "Minä puhun ______ -a/-ä ja ______ -a/-ä.",
                    "语言名用部分格 -a/-ä",
                ),
                (
                    "Missä sinä asut?",
                    "Minä asun ______ -ssa/-ssä (Lahdessa).",
                    "内格 -ssa/-ssä",
                ),
                (
                    "Mitä sinä opiskelet?",
                    "Minä opiskelen ______ .",
                    "学科名用部分格或原形，视动词而定",
                ),
                (
                    "Oletko naimisissa?",
                    "Kyllä, olen naimisissa. / Ei, en ole naimisissa.",
                    "状态用 -ssa/-ssä；否定 <code>en ole</code>",
                ),
                (
                    "Seurusteletko?",
                    "Kyllä, seurustelen. / Ei, en seurustele.",
                    "一般疑问句在动词后加 -ko/-kö",
                ),
                (
                    "Mikä sinun sähköpostiosoite on?",
                    "Minun sähköpostiosoite on ______ .",
                    "主语是 <code>osoite</code>，谓语用 <code>on</code>",
                ),
                (
                    "Mikä sinun puhelinnumero on?",
                    "Minun puhelinnumero on ______ .",
                    "同上，注意复合词整体不变格",
                ),
                (
                    "Millainen perhe sinulla on?",
                    "Minulla on ______ . / Minun perheessä on ______ .",
                    "拥有句 <code>minulla on</code>（-lla 加「有」）",
                ),
            )
            + cal(
                "tip",
                "答题顺序",
                "自我介绍按「名字 → 拼写 → 年龄 → 来自哪 → 语言 → 住哪 → 学什么 → 家庭」的顺序说，对方最容易跟上。芬兰人习惯先报名字再补充，不要一上来就说专业。",
            )
            + h3("1.3 三个后缀：-sta/-stä、-ssa/-ssä、-a/-ä")
            + p(
                "<b>出处格 -sta/-stä</b> 表示「从……里面出来 / 来自」。问句 <code>Mistä maasta sinä olet kotoisin?</code> 里的 <code>mistä</code> 本身就是 <code>mikä</code> 的出处格。答句 <code>Minä olen kotoisin Suomesta</code>（我来自芬兰）、<code>Minä olen kotoisin Kiinasta</code>（我来自中国）、<code>Minä olen kotoisin Saksasta</code>（我来自德国）。多数国名直接加 -sta/-stä，但有一类例外：<code>Venäjä</code>（俄罗斯）的来源形式是 <code>Venäjältä</code>，用的是 -lta/-ltä。原因是这类词被视为「表面上的地点」而不是「有内部的容器」，详见 1.8 的说明。"
            )
            + p(
                "<b>内格 -ssa/-ssä</b> 表示「在……里面」。<code>Missä sinä asut?</code> → <code>Minä asun Lahdessa</code>（我住在拉赫蒂）、<code>Minä asun Helsingissä</code>（我住在赫尔辛基）、<code>Minä asun Suomessa</code>。地名加 -ssa/-ssä 时会发生辅音交替：<code>Lahti</code> → <code>Lahdessa</code>（t→d），<code>Turku</code> → <code>Turussa</code>（k→∅），<code>Oulu</code> → <code>Oulussa</code>（不变）。"
            )
            + p(
                "<b>部分格 -a/-ä</b> 在这一讲只以两种面貌出现：语言名（<code>Minä puhun suomea, englantia ja vähän ruotsia</code>）和年龄（<code>Olen 22 vuotta</code>）。语言名用部分格，是因为「说某种语言」被视为一种持续的、非整体的动作；年龄用部分格，是因为 <code>vuotta</code> 后面省略了「岁」这个量词概念，芬兰语固定说 <code>kaksikymmentä vuotta</code>。"
            )
            + tb(
                ("问句", "答句", "为什么用这个格"),
                (
                    "Mistä sinä olet kotoisin?",
                    "Minä olen kotoisin Suomesta.",
                    "-sta 表示来源",
                ),
                ("Missä sinä asut?", "Minä asun Lahdessa.", "-ssa 表示所在"),
                (
                    "Mitä kieliä sinä puhut?",
                    "Minä puhun suomea ja englantia.",
                    "语言作部分格宾语",
                ),
                ("Kuinka vanha sinä olet?", "Minä olen 25 vuotta.", "年龄固定用部分格"),
                (
                    "Mihin sinä menet?",
                    "Minä menen kauppaan.",
                    "-hVn 表示去往（第 4 讲展开）",
                ),
            )
            + h3("1.4 数字 0–1000 的构成规则")
            + p(
                "芬兰语数字是<b>规则拼装</b>的，掌握四个零件就能读出 0–999 的任何数：个位词 0–9、<code>kymmenen</code>（10）、<code>sata</code>（100）、<code>tuhat</code>（1000）。"
            )
            + p(
                "规则一：0–10 必须逐个背。<code>nolla, yksi, kaksi, kolme, neljä, viisi, kuusi, seitsemän, kahdeksan, yhdeksän, kymmenen</code>。"
            )
            + p(
                "规则二：11–19 = 个位词 + <code>toista</code>。<code>yksitoista</code>(11)、<code>kaksitoista</code>(12)、<code>kolmetoista</code>(13)、<code>neljätoista</code>(14)、<code>viisitoista</code>(15)、<code>kuusitoista</code>(16)、<code>seitsemäntoista</code>(17)、<code>kahdeksantoista</code>(18)、<code>yhdeksäntoista</code>(19)。<code>toista</code> 本义是「第二个十位」，所以 15 的逻辑是「五在第二个十位里」。"
            )
            + p(
                "规则三：整十 = 个位词 + <code>kymmentä</code>。<code>kaksikymmentä</code>(20)、<code>kolmekymmentä</code>(30)、<code>neljäkymmentä</code>(40)、<code>viisikymmentä</code>(50)、<code>kuusikymmentä</code>(60)、<code>seitsemänkymmentä</code>(70)、<code>kahdeksankymmentä</code>(80)、<code>yhdeksänkymmentä</code>(90)。例外：10 是 <code>kymmenen</code> 而不是 <code>yksikymmentä</code>。"
            )
            + p(
                "规则四：几十几 = 整十 + 个位，<b>连写成一个词</b>。<code>kaksikymmentäkolme</code>(23)、<code>kolmekymmentäkaksi</code>(32)、<code>neljäkymmentäkolme</code>(43)、<code>viisikymmentäviisi</code>(55)、<code>kuusikymmentäkahdeksan</code>(68)、<code>seitsemänkymmentäviisi</code>(75)。"
            )
            + p(
                "百位同理：<code>sata</code>(100)、<code>kaksisataa</code>(200)、<code>kolmesataa</code>(300)、<code>viisisataa</code>(500)。百位与后面的十位、个位也连写：<code>satakaksikymmentä</code>(120)、<code>satakaksikymmentäkaksi</code>(122)、<code>satakolmekymmentäkaksi</code>(132)、<code>sataseitsemänkymmentäviisi</code>(175)、<code>kolmesataakaksitoista</code>(312)、<code>viisisataaseitsemäntoista</code>(517)、<code>tuhat</code>(1000)。"
            )
            + tb(
                ("数字", "芬兰语写法", "组装说明"),
                ("7", "seitsemän", "个位词，需背"),
                ("15", "viisitoista", "5 + toista"),
                ("23", "kaksikymmentäkolme", "20 + 3，连写"),
                ("32", "kolmekymmentäkaksi", "30 + 2，连写"),
                ("100", "sata", "百位词"),
                ("120", "satakaksikymmentä", "100 + 20，连写"),
                ("175", "sataseitsemänkymmentäviisi", "100 + 70 + 5"),
                ("312", "kolmesataakaksitoista", "300 + 12"),
                ("517", "viisisataaseitsemäntoista", "500 + 17"),
                ("1000", "tuhat", "千位词"),
            )
            + cal(
                "warn",
                "数字的两个坑",
                "第一，<b>不要加空格</b>：写成 <code>kaksikymmentä kolme</code> 是把一个数拆成两个数，书面语里是错的。第二，<b>11–19 里的 <code>toista</code> 不是「二十」</b>，<code>kaksitoista</code> 是 12，不是 22；22 是 <code>kaksikymmentäkaksi</code>。",
            )
            + h3("1.5 Onko sinulla：存在句与部分格初现")
            + p(
                "「我有」在芬兰语里不说「我 + 有」，而说「我这儿 + 是」：<b><code>Minulla on …</code></b>。其中 <code>minulla</code> 是 <code>minä</code> 的 -lla 形式（adessiivi，表示「在……身上 / 在……这儿」）。这一点决定了否定句的形态："
            )
            + p(
                "肯定：<code>Minulla on kissa.</code>（我有一只猫）／否定：<code>Minulla ei ole kissaa.</code>（我没有猫）。否定句里 <code>on</code> 变成 <code>ei ole</code>，而且<b>宾语必须变部分格</b>。这是芬兰语否定句的普遍规则，后面第 10 讲会系统展开。"
            )
            + tb(
                ("问句", "肯定答句", "否定答句"),
                (
                    "Onko sinulla äiti?",
                    "Kyllä, minulla on äiti.",
                    "Ei, minulla ei ole äitiä.",
                ),
                (
                    "Onko sinulla sisko?",
                    "Kyllä, minulla on sisko.",
                    "Ei, minulla ei ole siskoa.",
                ),
                (
                    "Onko sinulla veli?",
                    "Kyllä, minulla on veli.",
                    "Ei, minulla ei ole veljeä.",
                ),
                (
                    "Onko sinulla lapsia?",
                    "Kyllä, minulla on 1 lapsi. / 2 lasta.",
                    "Ei, minulla ei ole lapsia.",
                ),
                (
                    "Onko sinulla serkku?",
                    "Kyllä, minulla on serkku. / 3 serkkua.",
                    "Ei, minulla ei ole serkkua.",
                ),
                (
                    "Onko sinulla lemmikki?",
                    "Kyllä, minulla on lemmikki.",
                    "Ei, minulla ei ole lemmikkiä.",
                ),
                (
                    "Onko sinulla auto?",
                    "Kyllä, minulla on auto.",
                    "Ei, minulla ei ole autoa.",
                ),
                (
                    "Onko sinulla pyörä?",
                    "Kyllä, minulla on pyörä.",
                    "Ei, minulla ei ole pyörää.",
                ),
            )
            + p(
                "注意第三行 <code>veli</code> 的部分格是 <code>veljeä</code>（i→e 的变形），第六行 <code>lemmikki</code> 变成 <code>lemmikkiä</code>（k 不变），这些细节在第 10 讲有完整规则表，此处先当成词块记住。"
            )
            + p(
                "单数与复数的答法也值得注意：<code>Onko sinulla lapsia?</code> 问的是「有没有孩子」（可能多个），所以用部分格复数 <code>lapsia</code>；答「一个」时用单数 <code>lapsi</code>，答「两三个」时用部分格单数 <code>lasta</code> —— <b>芬兰语数词 2 以上后面接部分格单数</b>，这是本课最容易被忽略的一条。"
            )
            + h3("1.6 Kuinka monta：数数句型")
            + p(
                "问数量用 <code>Kuinka monta … on?</code>，被数的名词同样落在<b>部分格单数</b>："
            )
            + ul(
                "<code>Kuinka monta tuolia on?</code> —— 有几把椅子？（tuoli → tuolia）",
                "<code>Kuinka monta opiskelijaa on?</code> —— 有几个学生？（opiskelija → opiskelijaa）",
                "<code>Kuinka monta opettajaa on?</code> —— 有几个老师？（opettaja → opettajaa）",
                "<code>Kuinka monta pöytää on?</code> —— 有几张桌子？（pöytä → pöytää）",
                "<code>Kuinka monta läppäriä on?</code> —— 有几台笔记本？（läppäri → läppäriä）",
                "<code>Kuinka monta ikkunaa on?</code> —— 有几扇窗？（ikkuna → ikkunaa）",
                "<code>Kuinka monta ovea on?</code> —— 有几扇门？（ovi → ovea，i→e）",
                "<code>Kuinka monta kuukautta on?</code> —— 有几个月？（kuukausi → kuukautta）",
                "<code>Kuinka monta päivää on tässä kuussa?</code> —— 这个月有几天？（päivä → päivää）",
            )
            + p(
                "答句直接把数字放在前面：<code>Tässä luokassa on kaksikymmentä tuolia.</code>（这间教室有二十把椅子）。<code>Kuinka monta</code> 与 <code>monta</code> 的区别在于：前者是疑问，后者用于陈述「许多」，如 <code>Minulla on monta ystävää</code>（我有很多朋友），后面同样接部分格单数。"
            )
            + h3("1.7 疑问词与语序")
            + p(
                "芬兰语的疑问词放在句首，之后是「主语 + 谓语」的正常语序，不倒装：<code>Missä sinä asut?</code> 而不是 <code>Asut sinä missä?</code>。一般疑问句（是非问）则在<b>动词</b>后加 -ko/-kö，并把动词提到句首：<code>Oletko naimisissa?</code>、<code>Seurusteletko?</code>、<code>Onko sinulla koiraa?</code>。"
            )
            + tb(
                ("疑问词", "含义", "例句"),
                ("mikä", "什么（问事物、名字）", "Mikä sinun nimi on?"),
                ("kuka", "谁（问人）", "Kuka sinä olet?"),
                ("mistä", "从哪里", "Mistä sinä olet kotoisin?"),
                ("missä", "在哪里", "Missä sinä asut?"),
                ("mihin", "去哪里", "Mihin sinä menet?"),
                ("mitä", "什么（部分格，问对象）", "Mitä sinä opiskelet?"),
                ("mitä kieliä", "哪些语言（复数部分格）", "Mitä kieliä sinä puhut?"),
                ("kuinka monta", "多少个", "Kuinka monta tuolia on?"),
                ("millainen", "什么样的", "Millainen perhe sinulla on?"),
                ("milloin", "什么时候（第 3 讲）", "Milloin sinä heräät?"),
                ("kenen", "谁的（属格，第 9 讲）", "Kenen tämä kirja on?"),
            )
            + h3("1.8 例外与提醒")
            + p(
                "第一，<code>Venäjä</code>（俄罗斯）这类以 -jä 结尾的国名，来源格通常用 -lta/-ltä：<code>Olen kotoisin Venäjältä</code>。类似地 <code>maaseutu</code>、<code>työ</code> 等表示「面上 / 活动中」的名词也用 -lta。这不是新规则，只是 -sta 与 -lta 的分工，看到 -lta 时先想「从表面、从活动离开」。"
            )
            + p(
                "第二，<code>Minun nimi on …</code> 在标准语里更常说 <code>Minun nimeni on …</code>（加所有格后缀 -ni），但课程材料给的是不加后缀的口语版，两种都能听懂。第 9 讲会说明后缀的用法与口语简化。"
            )
            + p(
                "第三，<code>Olen kotoisin Kiinasta</code> 里国名首字母在句中最常见是小写 <code>kiinasta</code>，但作为专有名词书写时仍按习惯大写；芬兰语中<b>星期、月份、季节一律小写</b>（第 3 讲再次强调）。"
            )
            + cal(
                "warn",
                "高频错误 1",
                "说成 <code>Minä olen 25 vuosi</code>。年龄必须部分格：<code>Olen 25 vuotta</code>。同理 <code>kaksi vuotta</code>、<code>monta vuotta</code>。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "否定句忘掉部分格：<code>Minulla ei ole kissa</code> 应为 <code>Minulla ei ole kissaa</code>。只要句子里出现 <code>ei</code>，后面的名词宾语几乎都要检查一遍。",
            )
            + cal(
                "tip",
                "口语提示",
                "芬兰人实际说话时 <code>minä</code>、<code>sinä</code> 常省略，因为动词词尾已经标出人称：<code>Olen kotoisin Kiinasta</code>、<code>Asun Oulussa</code>。书面语保留主语更清楚。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("minä, sinä, hän", "我、你、他/她", "Personal pronouns in the singular."),
            ("me, te, he", "我们、你们、他们", "Personal pronouns in the plural."),
            ("mikä", "什么（问事物）", "Question word for things: Mikä sinun nimi on?"),
            ("kuka", "谁（问人）", "Question word for people: Kuka sinä olet?"),
            ("mistä", "从哪里", "Elative question word: Mistä sinä olet kotoisin?"),
            ("missä", "在哪里", "Inessive question word: Missä sinä asut?"),
            (
                "mitä",
                "什么（部分格）",
                "Partitive question word for objects: Mitä sinä opiskelet?",
            ),
            (
                "kuinka monta",
                "多少个",
                "How many; the counted noun is partitive singular.",
            ),
            ("yksi, kaksi, kolme", "一、二、三", "Basic numerals 1–3."),
            ("kymmenen, sata, tuhat", "十、百、千", "Tens, hundred and thousand."),
            ("-toista", "十几", "Suffix for 11–19: kaksitoista = 12."),
            ("-kymmentä", "几十", "Suffix for tens: kaksikymmentä = 20."),
            ("Minulla on …", "我有……", "Existential sentence: literally at-me is."),
            (
                "Minulla ei ole …",
                "我没有……",
                "Negative existential; the object takes the partitive.",
            ),
            ("vuotta", "岁（部分格）", "Olen 25 vuotta = I am 25 years old."),
            ("kotoisin", "来自", "Used with the elative: olen kotoisin Suomesta."),
        ),
        examples=(
            qa(
                "例 1　把 517 读成芬兰语，并说明每个部件的作用。",
                p(
                    "<b>解：</b>先拆位：517 = 500 + 17。500 是 <code>viisisataa</code>（viisi + sataa，sata 在复合数中变成 sataa）；17 是 <code>seitsemäntoista</code>（seitsemän + toista）。两段连写：<code>viisisataaseitsemäntoista</code>。"
                )
                + p(
                    "<b>思路迁移：</b>任何三位数都按「百位 + 十位 + 个位」拆，每一段先单独读准，再连写。若十位是 1x（11–19），该段用 <code>-toista</code>；若个位是 0，只读十位段。"
                ),
            )
            + qa(
                "例 2　把「我没有车，但我有一辆自行车」译成芬兰语。",
                p(
                    "<b>解：</b>否定部分：<code>Minulla ei ole autoa.</code>（auto → autoa，部分格）。肯定部分：<code>Minulla on pyörä.</code>（肯定句用原形）。连接：<code>mutta</code>。"
                )
                + p(
                    "合起来：<code>Minulla ei ole autoa, mutta minulla on pyörä.</code>"
                )
                + p(
                    "<b>要点：</b>同一个句型 <code>minulla on</code> 在否定时 <code>on</code> → <code>ei ole</code>，且只有宾语变格，<code>minulla</code> 本身不变。"
                ),
            )
            + qa(
                "例 3　回答「Kuinka monta opiskelijaa luokassa on?」，教室里有 18 人。",
                p(
                    "<b>解：</b>18 = <code>kahdeksantoista</code>。名词用部分格单数：<code>opiskelijaa</code>。完整答句：<code>Luokassa on kahdeksantoista opiskelijaa.</code>"
                )
                + p(
                    "<b>要点：</b>数词后面的名词永远不是复数形式，而是部分格单数。这一点与英语、汉语都不同，是本讲最需要形成条件反射的地方。"
                ),
            )
            + qa(
                "例 4　自我介绍模板填空：名字 Anna，22 岁，来自德国，住在拉赫蒂，学信息技术。",
                p(
                    "<b>解：</b><code>Minun nimi on Anna.</code> / <code>Olen kaksikymmentäkaksi vuotta.</code> / <code>Olen kotoisin Saksasta.</code> / <code>Asun Lahdessa.</code> / <code>Opiskelen tietotekniikkaa.</code>"
                )
                + p(
                    "<b>逐步核对：</b>年龄 → 部分格 <code>vuotta</code>；来源 → -sta，且 Saksa 不变形；居住 → -ssa，Lahti 的 t 变 d（<code>Lahdessa</code>）；学科 → 部分格 <code>tietotekniikkaa</code>，因为 <code>opiskella</code> 后面接部分格。"
                ),
            )
        ),
        practice=(
            ol(
                "把下列数字写成芬兰语单词：0、7、15、33、100、122、1000。",
                "用 <code>Minulla on …</code> / <code>Minulla ei ole …</code> 各造两句，说明家庭成员与宠物。",
                "把「你来自哪个国家？」「你住在哪里？」「你会说哪些语言？」三个问句写成芬兰语并各配一个答句。",
                "改错：<code>Minä olen 20 vuosi.</code> / <code>Minulla ei ole koira.</code> / <code>Minä puhun suomi.</code>",
                "回答 <code>Kuinka monta kuukautta vuodessa on?</code>，写出完整句子。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> <code>nolla, seitsemän, viisitoista, kolmekymmentäkolme, sata, satakaksikymmentäkaksi, tuhat</code>。33 是 30 + 3 连写；122 是 100 + 22 连写。"
                )
                + p(
                    "<b>2.</b> 示例：<code>Minulla on äiti ja isä.</code> / <code>Minulla on yksi sisko.</code> / <code>Minulla ei ole koiraa.</code> / <code>Minulla ei ole autoa.</code> 否定句逐句检查宾语是否部分格。"
                )
                + p(
                    "<b>3.</b> <code>Mistä maasta sinä olet kotoisin?</code> — <code>Olen kotoisin Kiinasta.</code> / <code>Missä sinä asut?</code> — <code>Asun Helsingissä.</code> / <code>Mitä kieliä sinä puhut?</code> — <code>Puhun kiinaa ja englantia.</code>"
                )
                + p(
                    "<b>4.</b> 三处都要改：<code>vuosi</code> → <code>vuotta</code>；<code>koira</code> → <code>koiraa</code>；<code>suomi</code> → <code>suomea</code>。改后：<code>Minä olen 20 vuotta.</code> / <code>Minulla ei ole koiraa.</code> / <code>Minä puhun suomea.</code>"
                )
                + p(
                    "<b>5.</b> <code>Vuodessa on kaksitoista kuukautta.</code> 注意「一年里」用 <code>vuodessa</code>（内格），月份数用部分格单数。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "数字 0–1000 的读写、<code>Minulla on / ei ole</code> 句型、年龄与数量的部分格、<code>-sta/-ssa</code> 两类地点后缀的区分。这些都是第一讲直接进入口语与听力题的考点。",
            )
            + cal(
                "warn",
                "易错 1",
                "否定句与数词后忘掉部分格：<code>ei ole kissa</code>、<code>kaksi koira</code> 都是错的。",
            )
            + cal(
                "warn",
                "易错 2",
                "把 <code>toista</code> 当成 20：<code>kaksitoista</code> 是 12。听到 22 应是 <code>kaksikymmentäkaksi</code>。",
            )
            + cal(
                "warn",
                "易错 3",
                "国名、城市名加格时不做辅音交替：<code>Lahti → Lahdessa</code>、<code>Turku → Turussa</code>。",
            )
            + cal(
                "tip",
                "进阶",
                "能主动区分 <code>-sta</code>（从内部出来）与 <code>-lta</code>（从表面 / 从活动离开），并解释 <code>Venäjältä</code> 为什么不用 -sta。",
            )
        ),
        checklist=(
            h2("口语与拼装清单")
            + h3("自我介绍六步")
            + st(
                "先报名字，再拼写：<code>Minun nimi on … , se kirjoitetaan …</code>",
                "年龄用部分格：<code>Olen … vuotta</code>",
                "来源用 -sta/-stä：<code>Olen kotoisin …sta</code>",
                "居住用 -ssa/-ssä，注意地名辅音交替",
                "语言用部分格：<code>Puhun …a ja …a</code>",
                "家庭用 <code>Minulla on …</code>，否定改 <code>ei ole + 部分格</code>",
            )
            + h3("读数字四步")
            + st(
                "拆成百位 / 十位 / 个位三段",
                "百位：sata → 200 用 kaksisataa",
                "十位：11–19 用 -toista，整十用 -kymmentä",
                "全部连写成一个词，不加空格",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "02_Tunti 1/1_PUHU UUDELLE PARILLE.html",
                "全篇 12 组问答",
                "自我介绍问句与答句模板、-sta/-ssa/-a 三类后缀、-ko/-kö 问句",
            ),
            (
                "02_Tunti 1/2_Numerot, bingo.docx",
                "数字列表",
                "0–1000 数字读写，含 122、175、312、517 等复合数",
            ),
            (
                "02_Tunti 1/3_PUHU PARILLE Kuinka monta_.html",
                "全篇 8 问",
                "Kuinka monta + 部分格单数、教室物品词汇",
            ),
            (
                "02_Tunti 1/4_PUHU PARILLE Onko sinulla_.html",
                "全篇 15 问",
                "存在句肯定/否定、部分格初现、家庭成员词汇",
            ),
            (
                "（补充）",
                "1.3、1.7",
                "疑问词总表与 <code>-lta</code> 与 <code>-sta</code> 的分工属衔接性拓展，原文只给例句",
            ),
            ("（跳过）", "—", "bingo 棋盘与图片页为课堂活动载体，无新增语言点"),
        ),
    )
)

LEC.append(
    L(
        slug="t2-weather-seasons-months",
        tzh="第 2 讲 · 天气、季节与月份",
        ten="Weather, Seasons and Months",
        keywords=[
            "weather",
            "adjective predicate",
            "partitive subject",
            "sataa",
            "season",
            "month",
            "adessive of time",
        ],
        files=[
            "03_Tunti 2/1_Milloin, Vuodenajat ja kuukaudet.pdf",
            "03_Tunti 2/2_Keskustele Kuukaudet.pdf",
            "03_Tunti 2/3_Millainen sää on.pdf",
            "03_Tunti 2/4_Sataa.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第二讲把话题从「我是谁」推到「外面怎么样、现在几月」。它看起来只是词汇课，实际上第一次系统展示了芬兰语的两个结构性习惯：<b>时间地点用「格」而不是介词</b>（talvella、tammikuussa），以及<b>形容词作谓语时可能要用部分格</b>（On sateista）。"
            )
            + p(
                "本讲之后，第 3 讲会把时间格细化到钟点与星期，第 4 讲再把这些时间短语用于谈计划。因此本讲的重点是先把「季节 -lla、月份 -ssa」这套记忆锚点打牢，后面只是往里加同类。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "用 <code>Millainen sää on?</code> 与 <code>Millainen ilma on?</code> 问天气，并给出五种以上天气答句",
                "解释并正确使用 <code>On aurinkoista</code> 与 <code>On aurinkoinen sää</code> 这两种结构",
                "说清 <code>sataa</code> 只以第三人称单数出现的原因，并搭配 <code>vettä / lunta / räntää / rakeita</code>",
                "把四季写成 -lla 形式、把十二个月写成 -ssa 形式，并用它们回答 <code>Milloin?</code>",
                "区分「天气形容词」与「天气名词」两类句子的构成，不混用词尾",
            )
        ),
        detail=(
            h3("2.1 本讲的三个话题与一条主线")
            + p(
                "Tunti 2 的四份材料分工很清楚：<code>1_Milloin, Vuodenajat ja kuukaudet</code> 给四季与十二个月的时间格形式；<code>2_Keskustele Kuukaudet</code> 是看图造句的口语活动；<code>3_Millainen sää on</code> 是天气问答卡；<code>4_Sataa</code> 专门讲一个动词的多义与惯用法。"
            )
            + p(
                "主线是：<b>芬兰语没有「在冬天」「在五月」这样的介词短语</b>，而是给名词换词尾。四季用 -lla（talvella、kesällä），月份用 -ssa（tammikuussa）。同一个「在……」，两类词用两个不同后缀，这是本讲最需要背下来的分工。"
            )
            + h3("2.2 天气问句与两套答句")
            + p(
                "问天气有两个几乎等价的问法：<code>Millainen sää tänään on?</code>（今天天气怎么样？）与 <code>Millainen ilma tänään on?</code>（今天天色怎么样？）。<code>sää</code> 偏「天气状况」，<code>ilma</code> 偏「天、空气」，日常可以互换。"
            )
            + p("回答时有两套结构，务必分清：")
            + tb(
                ("结构", "例句", "构成说明"),
                (
                    "形容词 + sää（名词在）",
                    "On aurinkoinen sää. / On sateinen sää. / On pilvinen sää.",
                    "sää 作主语，形容词用<b>主格</b>并与 sää 一致：aurinkoinen、sateinen、pilvinen、tuulinen、sumuinen",
                ),
                (
                    "省略主语 + 形容词部分格",
                    "On aurinkoista. / On sateista. / On pilvistä. / On tuulista. / On sumuista.",
                    "主语被省略，形容词用<b>部分格</b>：-inen → -ista/-istä",
                ),
                (
                    "固定短语",
                    "On hyvä sää. / On kaunis sää. / On lämmin sää. / On kuuma sää. / On kylmä sää.",
                    "品质形容词直接修饰 sää，用主格",
                ),
                (
                    "温度",
                    "On lämmin sää, +20 astetta. / On kuuma sää, +25 astetta. / On pakkasta, miinus 20 astetta.",
                    "零上直接用 <code>+ N astetta</code>；零下用 <code>On pakkasta</code> + <code>miinus N astetta</code>",
                ),
                (
                    "特殊天气名词",
                    "On helle. / On sumu. / On ukkosta ja salamoi.",
                    "helle = 酷暑；sumu = 雾；ukkonen 打雷时用部分格 ukkosta",
                ),
                (
                    "动词句",
                    "Aurinko paistaa. / Sataa vettä. / Tuulee vähän. / Tuulee paljon, on myrsky.",
                    "用动词直接描述动作，见 2.3",
                ),
            )
            + p(
                "为什么省略主语时形容词要变部分格？因为此时句子的意思是「（天气）是晴朗的（一种状态）」，被陈述的不是一个完整的、可数的个体，而是一种不可数的状态量，芬兰语用部分格标记这种「部分 / 不定量」的谓语。类似结构还有 <code>On kylmä</code>（很冷）、<code>On viileää</code>（有点凉）、<code>On lämmin</code>（暖和）。注意 <code>On kylmä</code> 与 <code>On kylmää</code> 都能听到，前者把「冷」当成一个整体状况，后者强调「冷的感觉弥漫着」，课程材料两种都给，考试一般两者都接受。"
            )
            + cal(
                "tip",
                "记忆钩子",
                "看到 <b>-inen</b> 结尾的天气形容词（aurinkoinen、sateinen、pilvinen、tuulinen、sumuinen），就想到它的部分格是 <b>-ista/-istä</b>：aurinkoista、sateista、pilvistä、tuulista、sumuista。有 sää 时用前者，无 sää 时用后者。",
            )
            + h3("2.3 sataa：一个只能用于第三人称的动词")
            + p(
                "芬兰语描述「下雨 / 下雪」不用「天」作主语，而用一个无人称动词 <code>sataa</code>。它的完整变位在材料里也给了：<code>minä sadan, sinä sadat, hän sataa, me sadamme, te sadatte, he satavat</code>。但材料同时指出：<b>实际只用第三人称单数，而且不加主语</b>，例如 <code>Ulkona sataa</code>（外面在下雨）。"
            )
            + p(
                "<code>sataa</code> 本身不说明「下什么」，要说明就得加<b>部分格宾语</b>："
            )
            + tb(
                ("表达", "含义", "格的使用"),
                ("Sataa.", "下雨 / 下雪（不指明）", "单独使用，凭窗看就知道是什么"),
                ("Sataa vettä.", "在下雨", "vesi → vettä（部分格）"),
                ("Sataa lunta.", "在下雪", "lumi → lunta（部分格）"),
                ("Sataa räntää.", "在下雨夹雪", "räntä → räntää"),
                ("Sataa rakeita.", "在下冰雹", "rae → rakeita（部分格复数）"),
                ("Sataa vettä ja lunta.", "雨夹雪（另一种说法）", "两个部分格并列"),
                (
                    "Sataa kissoja ja koiria.",
                    "下倾盆大雨（直译「下猫下狗」）",
                    "惯用语，仿英语",
                ),
                (
                    "Sataa ukkoja ja akkoja.",
                    "下大雨（旧说法，直译「下老头老太太」）",
                    "惯用语",
                ),
                ("Sataa puukkoja.", "下大雨（直译「下刀子」）", "惯用语"),
                ("Sataa rahaa.", "钱来得容易（直译「下钱」）", "惯用语"),
                ("Sataa tähdenlentoja.", "流星很多", "惯用语"),
                ("Sataa onnitteluja.", "收到一大堆祝贺", "惯用语"),
            )
            + p(
                "这条惯用语线索很有用：<code>sataa</code> 的语义核心是「从天上往下落」，所以凡是「大量涌来」的东西都能「下」。反过来说，看到 <code>Sataa + 部分格</code> 就要意识到这不是「下雨」而是「某物大量落下」。"
            )
            + cal(
                "warn",
                "不要造主语",
                "不能说 <code>Taivas sataa</code>（天空下雨）或 <code>Se sataa</code>（它下雨）。直接 <code>Sataa</code> 开头即可，这与英语 It is raining 的 it 不同。",
            )
            + h3("2.4 其他天气动词与固定搭配")
            + ul(
                "<code>Aurinko paistaa.</code> —— 太阳在照（paistaa 也可用于「烤肉」）。",
                "<code>Tuulee vähän.</code> —— 有点风；<code>Tuulee paljon, on myrsky.</code> —— 风很大，有暴风雨。",
                "<code>On pakkasta.</code> —— 天寒地冻（pakkasta 是部分格，固定搭配）。",
                "<code>On ukkosta ja salamoi.</code> —— 打雷又闪电（ukkonen 的 partial <code>ukkos</code>ta；salamoida 用于闪电）。",
                "<code>On helle.</code> —— 酷暑（芬兰夏季超过 25 度即称 helle）。",
                "<code>On sumu. / On sumuista.</code> —— 有雾 / 雾蒙蒙。",
                "<code>On viileää.</code> —— 凉爽（viileä 的部分格）。",
            )
            + p(
                "温度读法：<code>+20 astetta</code> 读作 <code>plus kaksikymmentä astetta</code>，<code>-20 astetta</code> 读作 <code>miinus kaksikymmentä astetta</code>。<code>astetta</code> 是 <code>aste</code> 的部分格单数，因为温度是量、不是可数个体。"
            )
            + h3("2.5 四季：为什么用 -lla")
            + p("四季的时间格一律是 <b>-lla/-llä</b>：")
            + tb(
                ("季节", "Milloin 形式", "英文"),
                ("talvi（冬）", "talvella", "in winter"),
                ("kevät（春）", "keväällä", "in spring"),
                ("kesä（夏）", "kesällä", "in summer"),
                ("syksy（秋）", "syksyllä", "in autumn"),
            )
            + p(
                "-lla 的本义是「在……表面上 / 在……这种活动里」。把季节理解成一段「时间表面」，就顺理成章地用 -lla。同理，一天中的时段也用 -lla：<code>aamulla</code>（早上）、<code>päivällä</code>（白天）、<code>illalla</code>（晚上）、<code>yöllä</code>（夜里）。而 <code>viikonloppuna</code> 例外地用 -na（第 3 讲详述）。"
            )
            + p(
                "材料里的示范段落正是把这些格串起来：<code>Kesällä on lämmin. Heinäkuussa minä olen mökillä ja uin joka päivä.</code>（夏天很暖。七月我在木屋，每天游泳。）注意 <code>mökillä</code> 也用 -lla，因为木屋被看成「待在上面的地方」。"
            )
            + h3("2.6 十二个月：为什么用 -ssa")
            + p(
                "十二个月一律用 <b>-ssa/-ssä</b>，而且月份词本身都以 <code>-kuu</code>（月）结尾："
            )
            + tb(
                ("月份", "Milloin 形式", "英文"),
                ("tammikuu", "tammikuussa", "in January"),
                ("helmikuu", "helmikuussa", "in February"),
                ("maaliskuu", "maaliskuussa", "in March"),
                ("huhtikuu", "huhtikuussa", "in April"),
                ("toukokuu", "toukokuussa", "in May"),
                ("kesäkuu", "kesäkuussa", "in June"),
                ("heinäkuu", "heinäkuussa", "in July"),
                ("elokuu", "elokuussa", "in August"),
                ("syyskuu", "syyskuussa", "in September"),
                ("lokakuu", "lokakuussa", "in October"),
                ("marraskuu", "marraskuussa", "in November"),
                ("joulukuu", "joulukuussa", "in December"),
            )
            + p(
                "月份用 -ssa 的理由与季节不同：月份被视为一个「容器」，事件发生在月份内部，所以是内格。这一点与第 1 讲的 <code>Lahdessa</code> 同源。<b>四季用 -lla、月份用 -ssa</b>，这条分工必须背成条件反射，因为考试里 <code>Milloin olet syntynyt?</code> 的标准答句就是 <code>Olen syntynyt huhtikuussa</code>（我四月出生）。"
            )
            + p(
                "顺带记住月份的构词逻辑，比死背十二个词省力：<code>tammi</code>（橡树年轮心材）、<code>helmi</code>（珍珠，二月雪珠）、<code>maalis</code>（三月融雪泥）、<code>huhti</code>（四月焚烧开荒）、<code>touko</code>（五月播种）、<code>kesä</code>（夏）、<code>heinä</code>（干草，七月割草）、<code>elo</code>（收获，八月）、<code>syys</code>（秋）、<code>loka</code>（泥泞，十月）、<code>marras</code>（冻土，十一月）、<code>joulu</code>（圣诞）。"
            )
            + h3("2.7 Milloin 问答与「做什么」的搭配")
            + p(
                "问「什么时候」用 <code>Milloin?</code>，回答直接把时间词放在句首或句尾，不需要介词：<code>Milloin sinä olet syntynyt? — Olen syntynyt tammikuussa.</code>；<code>Milloin on suomen tunti? — Tiistaina.</code>（星期用 -na，见第 3 讲）。"
            )
            + p(
                "把季节与活动连起来时，注意动词搭配：<code>Uin joka päivä</code>（我每天游泳）、<code>Pelaan ulkona sulkapalloa</code>（我在户外打羽毛球，<code>pelata</code> 后面接部分格 <code>sulkapalloa</code>）、<code>grillaamme</code>（我们烧烤）、<code>haravoin pihalla lehtiä</code>（我在院子里耙树叶，<code>haravoida</code> + 部分格复数 <code>lehtiä</code>）、<code>hiihdän ja laskettelen</code>（我滑雪和滑雪橇）、<code>käyn saunassa</code>（我去桑拿，<code>käydä</code> + -ssa）。"
            )
            + cal(
                "tip",
                "句型模板",
                "描述「某季节我做什么」用：<b>季节 -lla + 动词第一人称 + 宾语（部分格或总格）</b>。例：<code>Keväällä kävelen metsässä monta tuntia.</code>（春天我在森林里走好几个小时。）",
            )
            + h3("2.8 大小写与书写规范")
            + p(
                "芬兰语中<b>星期、月份、季节全部小写</b>：<code>maanantai</code>、<code>tammikuu</code>、<code>kesä</code>。句首才大写。这与英语 Monday / January / Summer 的习惯相反，写作题里写错会扣分。国名、城市名、语言名照常小写（<code>suomi</code>、<code>suomea</code>），只有标题、专名首字母大写。"
            )
            + cal(
                "warn",
                "高频错误 1",
                "<code>On sateinen.</code> 缺主语。要么 <code>On sateinen sää</code>，要么 <code>On sateista</code>。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "把季节也写成 -ssa：<code>kesässä</code> 是错的，应为 <code>kesällä</code>；把月份写成 -lla：<code>tammikuulla</code> 也是错的，应为 <code>tammikuussa</code>。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("sää", "天气", "Weather: Millainen sää on?"),
            (
                "ilma",
                "天、空气",
                "Air or weather; interchangeable with sää in small talk.",
            ),
            ("Millainen … on?", "……怎么样？", "What kind of … is it?"),
            (
                "aurinkoinen",
                "晴朗的",
                "Nominative adjective with sää: On aurinkoinen sää.",
            ),
            (
                "aurinkoista",
                "晴朗（部分格谓语）",
                "Partitive predicate without a subject: On aurinkoista.",
            ),
            (
                "sateinen / sateista",
                "下雨的",
                "Rainy; the -inen form agrees with sää, the -ista form stands alone.",
            ),
            ("pilvinen / pilvistä", "多云的", "Cloudy."),
            ("tuulinen / tuulista", "有风的", "Windy."),
            ("sumuinen / sumuista", "有雾的", "Foggy."),
            (
                "sataa",
                "下雨 / 下雪",
                "Impersonal verb, only 3rd person singular, no subject.",
            ),
            ("lumi → lunta", "雪（部分格）", "Sataa lunta = it is snowing."),
            ("vesi → vettä", "水（部分格）", "Sataa vettä = it is raining."),
            ("räntä → räntää", "雨夹雪", "Sataa räntää = it is sleeting."),
            ("rae → rakeita", "冰雹", "Sataa rakeita = it is hailing."),
            ("pakkasta", "零下、严寒", "On pakkasta = it is freezing."),
            ("helle", "酷暑", "On helle = it is very hot (over 25 °C)."),
            ("talvella, kesällä", "冬天、夏天", "Seasons take the adessive -lla."),
            ("tammikuussa", "一月（内格）", "Months take the inessive -ssa."),
        ),
        examples=(
            qa(
                "例 1　把「今天天气晴朗，气温 +18 度」说成两句芬兰语。",
                p(
                    "<b>解：</b>第一句用名词结构：<code>Tänään on aurinkoinen sää.</code> 也可以用省略主语的形容词结构：<code>Tänään on aurinkoista.</code> 第二句：<code>On plus kahdeksantoista astetta.</code>"
                )
                + p(
                    "<b>要点：</b>18 = <code>kahdeksantoista</code>（8 + toista）；<code>astetta</code> 是部分格，因为温度是量。"
                ),
            )
            + qa(
                "例 2　判断正误并改正：<code>Kesässä sataa paljon vettä.</code>",
                p(
                    "<b>解：</b>两处错。季节不用 -ssa，改为 <code>kesällä</code>。整句：<code>Kesällä sataa paljon vettä.</code>"
                )
                + p(
                    "<b>思路迁移：</b>看到「季节 + 格」先查是不是 -lla；看到 <code>sataa</code> 后面的名词先查是不是部分格（vettä 正确，lunta、räntää 同理）。"
                ),
            )
            + qa(
                "例 3　回答 <code>Milloin olet syntynyt?</code>，设定生日是 1999 年 11 月 3 日。",
                p(
                    "<b>解：</b>月份用 -ssa：<code>marraskuussa</code>。年份用 <code>vuonna 1999</code>（vuonna = vuosi 的样格，固定说法）。完整答句：<code>Olen syntynyt marraskuussa vuonna 1999.</code>"
                )
                + p(
                    "<b>要点：</b><code>olen syntynyt</code> 是「出生」的固定完成形式，作为整块记住即可，第 12 讲会说明它的构成来源。"
                ),
            )
            + qa(
                "例 4　把材料中的一句话拆开讲：<code>Syksyllä sataa usein vettä. Minä asun omakotitalossa.</code>",
                p(
                    "<b>解：</b>第一句：季节 -lla（syksyllä）+ 无人称动词（sataa）+ 频率副词（usein）+ 部分格宾语（vettä）。第二句：内格（omakotitalossa = 独栋房子里），因为「住在某建筑内部」用 -ssa。"
                )
                + p(
                    "<b>对比：</b>季节 -lla 与建筑 -ssa 在同一段里并存，正说明芬兰语的格由名词的语义类别决定，不由汉语的「在」决定。"
                ),
            )
        ),
        practice=(
            ol(
                "把四季与十二个月分别写成 -lla 与 -ssa 形式，各造一句 <code>Milloin …?</code> 的答句。",
                "用三种天气结构各写一句：名词句（sää）、省略主语句（部分格）、动词句（sataa / tuulee / paistaa）。",
                "翻译：「冬天下很多雪，我每天晚上去桑拿。」",
                "改错：<code>Kesässä on lämmin sää.</code> / <code>On sateinen.</code> / <code>Sataa lumi.</code> / <code>On pakkanen.</code>",
                "写一段 4 句的短文：说明你最喜欢的季节、那个季节的天气、你在那个季节做什么。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> 季节：<code>talvella, keväällä, kesällä, syksyllä</code>；月份：<code>tammikuussa … joulukuussa</code>。答句示例：<code>Kesällä minä uin järvessä.</code> / <code>Joulukuussa on paljon lunta.</code>"
                )
                + p(
                    "<b>2.</b> 名词句：<code>On tuulinen sää.</code> 部分格句：<code>On pilvistä.</code> 动词句：<code>Ulkona tuulee paljon.</code> 或 <code>Aurinko paistaa.</code>"
                )
                + p(
                    "<b>3.</b> <code>Talvella sataa paljon lunta, ja käyn saunassa joka ilta.</code> 注意 <code>lunta</code> 部分格、<code>joka ilta</code> 不加格（joka 后面的时间词用原形）。"
                )
                + p(
                    "<b>4.</b> <code>Kesässä</code> → <code>kesällä</code>；<code>On sateinen.</code> → <code>On sateinen sää.</code> 或 <code>On sateista.</code>；<code>Sataa lumi.</code> → <code>Sataa lunta.</code>；<code>On pakkanen.</code> → <code>On pakkasta.</code>"
                )
                + p(
                    "<b>5.</b> 示例：<code>Minun lempivuodenaika on syksy. Syksyllä on viileä ja sateista. Minä kävelen metsässä ja haravoin lehtiä. Illalla luen kirjaa kotona.</code> 自检每句的时间词是否用了正确的格。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "四季 -lla 与月份 -ssa 的形式、<code>Millainen sää on?</code> 的两套答句、<code>sataa + 部分格</code>。听力与口语都直接考这些短语。",
            )
            + cal(
                "warn",
                "易错 1",
                "季节用 -ssa、月份用 -lla，两个后缀互换是最常见的错误。",
            )
            + cal(
                "warn",
                "易错 2",
                "<code>sataa</code> 后面忘掉部分格：<code>sataa lumi</code>、<code>sataa vesi</code> 都错。",
            )
            + cal(
                "warn",
                "易错 3",
                "给 <code>sataa</code> 加主语：<code>Se sataa</code>、<code>Taivas sataa</code> 都不成立。",
            )
            + cal(
                "tip",
                "进阶",
                "能主动用 <code>Sataa kissoja ja koiria</code>、<code>Sataa rahaa</code> 这类惯用语解释「sataa 表示大量落下」的语义机制。",
            )
        ),
        checklist=(
            h2("天气与时间表达清单")
            + h3("说天气三步")
            + st(
                "选结构：有 sää 用主格形容词；无主语用部分格形容词；有动作动词直接用第三人称单数",
                "形容词部分格：-inen → -ista/-istä",
                "温度：plus / miinus + 数词 + astetta",
                "降水：sataa + vettä / lunta / räntää / rakeita",
            )
            + h3("说时间两步")
            + st(
                "季节与时段的词先换成 -lla：kesällä、illalla、aamulla",
                "月份换 -ssa：tammikuussa、huhtikuussa",
                "星期换 -na：maanantaina（第 3 讲）",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "03_Tunti 2/1_Milloin, Vuodenajat ja kuukaudet.pdf",
                "p1–p4",
                "四季 -lla、天气句型、十二个月 -ssa、季节活动段落",
            ),
            (
                "03_Tunti 2/2_Keskustele Kuukaudet.pdf",
                "p1",
                "看图造句任务：Mikä kuukausi / vuodenaika on? Mitä ihmiset tekevät?",
            ),
            ("03_Tunti 2/3_Millainen sää on.pdf", "p1", "天气问答卡标题与口语任务形式"),
            (
                "03_Tunti 2/4_Sataa.pdf",
                "p2–p6",
                "sataa 的变位与限定用法、部分格搭配、六条惯用语",
            ),
            (
                "（补充）",
                "2.2、2.5",
                "形容词谓语部分格的理据、-lla 与 -ssa 的语义分工属解释性拓展",
            ),
            (
                "（跳过）",
                "—",
                "3_Millainen sää on 的 p2–p12 为纯图片页，无文字语言点；图片素材不入讲义",
            ),
        ),
    )
)

LEC.append(
    L(
        slug="t3-clock-time-expression",
        tzh="第 3 讲 · 钟点、星期与 Milloin 时间格",
        ten="Telling the Time, Weekdays and Time Cases",
        keywords=[
            "clock",
            "traditional time",
            "half past",
            "quarter",
            "weekday",
            "essive -na",
            "ablative of time",
        ],
        files=[
            "04_Tunti 3/1_Kertaa kello ja päivät.docx",
            "04_Tunti 3/2_VASTAUKSET- Kello ja päivät.pdf",
            "04_Tunti 3/3_kello.pdf",
            "04_Tunti 3/4_Viikonpäivät jne.pdf",
            "04_Tunti 3/5_Milloin.pdf",
            "04_Tunti 3/6_Puhu Milloin_.html",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第三讲把第 2 讲的时间格补完整：季节用 -lla、月份用 -ssa，这一讲再加两类——<b>星期用 -na</b>、<b>钟点用 -lta/-ltä</b>。四类合起来，才算把 <code>Milloin?</code> 这个问句答全。"
            )
            + p(
                "同时它引入本课第一个「读法规则」：芬兰语有两套报时系统（传统与数字），传统系统的 <code>puoli</code>（半点）逻辑与汉语、英语都不同，是最容易在听力题里失分的地方，本讲会专门拆开讲。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "用三种问法问时间，并按传统与数字两种方式读出任意时刻",
                "解释 <code>puoli yksi</code> 为什么是 12:30，不把它读成 1:30",
                "把星期写成 -na 形式、把钟点写成 -lta 形式，并用它们回答 <code>Milloin?</code>",
                "在时间句里加时段限定（aamulla、illalla、yöllä）区分同名的十二小时制时刻",
                "说出日期与星期的书写规范，包括芬兰语不用大写这一点",
            )
        ),
        detail=(
            h3("3.1 三种问时间的说法")
            + p(
                "问「现在几点」有三种说法，语气与场景不同：<code>Mitä kello on?</code>（最常用）、<code>Paljonko kello on?</code>（口语，偏「多少」）、<code>Kuinka paljon kello on?</code>（更完整、略正式）。三者的答句结构相同，都以 <code>Kello on …</code> 或口语的 <code>Se on …</code> 开头。"
            )
            + p(
                "注意 <code>kello</code> 有两个意思：一是「钟、表」（名词），二是报时句里的固定成分（<code>Kello on viisi</code> = 五点了）。作为时间单位「小时」时它是 <code>tunti</code>：<code>kaksi tuntia</code> = 两小时。<b>报点用 kello，计时长用 tunti</b>。"
            )
            + h3("3.2 数字时间（digitaalinen aika）")
            + p(
                "数字时间按「小时 + 分钟」直接读，分钟读成两位数：<code>12.34</code> 读作 <code>Kello on kaksitoista kolmekymmentäneljä</code>；整点读作 <code>Kello on kolmetoista (nolla-nolla)</code>（13:00）。这种读法在火车站、机场、电视节目表里最常见。"
            )
            + tb(
                ("数字写法", "数字时间读法", "说明"),
                (
                    "13:00",
                    "Kello on kolmetoista (nolla-nolla).",
                    "整点直接读小时，可补 nolla-nolla",
                ),
                (
                    "21:17",
                    "Kello on kaksikymmentäyksi seitsemäntoista.",
                    "小时 + 分钟两个数",
                ),
                ("5:25", "Kello on viisi kaksikymmentäviisi.", "小时不加「零」"),
                (
                    "17:30",
                    "Kello on seitsemäntoista kolmenkymmentä.",
                    "分钟 30 读 kolmenkymmentä",
                ),
                (
                    "9:45",
                    "Kello on yhdeksän neljäkymmentäviisi.",
                    "分钟 45 读 neljäkymmentäviisi",
                ),
                (
                    "11:55",
                    "Kello on yksitoista viisikymmentäviisi.",
                    "分钟 55 读 viisikymmentäviisi",
                ),
            )
            + cal(
                "tip",
                "小时数的读法",
                "13–19 按 <code>kolmetoista … yhdeksäntoista</code>；20 以上按 <code>kaksikymmentäyksi</code> 这类复合数连写。注意 24 小时制里 21 读 <code>kaksikymmentäyksi</code>，不是 <code>yhdeksäntoista</code> 加别的。",
            )
            + h3("3.3 传统时间（perinteinen aika）：yli 与 vailla")
            + p(
                "传统系统以「下一个整点」或「上一个整点」为参照，用两个介词性词：<code>yli</code>（过）与 <code>vailla / vaille</code>（差）。规则如下："
            )
            + p(
                "<b>规则一（过半点之前）：</b>分钟 + <code>yli</code> + <b>当前小时</b>。<code>12:10</code> = <code>kymmenen yli kaksitoista</code>；<code>12:15</code> = <code>viisitoista yli kaksitoista</code>，也可说 <code>vartin yli kaksitoista</code>。"
            )
            + p(
                "<b>规则二（过半点之后）：</b>剩余分钟 + <code>vailla / vaille</code> + <b>下一个小时</b>。<code>12:40</code> = <code>kaksikymmentä vailla yksi</code>（差二十分一点）；<code>12:45</code> = <code>varttia vailla yksi</code> 或 <code>viisitoista vailla yksi</code>。"
            )
            + p(
                "<b>规则三（半点）：</b><code>puoli</code> + <b>下一个小时</b>。<code>12:30</code> = <code>puoli yksi</code>。<b>这是全课最反直觉的一条</b>：芬兰语的 <code>puoli yksi</code> 直译是「一半的一点」，意思是「朝着一点走了一半」，即 12:30，不是 1:30。"
            )
            + p(
                "<b>规则四（整点）：</b><code>Kello on (tasan) yksi</code>，<code>tasan</code> 表示「整」。"
            )
            + tb(
                ("时刻", "传统读法", "关键点"),
                ("12:00", "Kello on (tasan) kaksitoista.", "整点"),
                ("12:10", "kymmenen yli kaksitoista", "yli + 当前小时"),
                (
                    "12:15",
                    "viisitoista yli kaksitoista / vartin yli kaksitoista",
                    "vartti = 一刻钟",
                ),
                ("12:30", "puoli yksi", "puoli + 下一个小时"),
                ("12:40", "kaksikymmentä vailla yksi", "vailla + 下一个小时"),
                (
                    "12:45",
                    "varttia vailla yksi / viisitoista vailla yksi",
                    "两种说法都常见",
                ),
                ("11:55", "viisi vailla kaksitoista", "差五分十二点"),
                ("5:25", "kaksikymmentäviisi yli viisi", "yli + 当前小时"),
                ("9:45", "varttia vailla kymmenen", "差一刻十点"),
                ("17:30", "puoli kuusi", "puoli + kuusi = 5:30"),
                ("21:17", "seitsemäntoista yli yhdeksän", "yli + 当前小时"),
            )
            + cal(
                "warn",
                "puoli 的逻辑",
                "把 <code>puoli yksi</code> 理解成「十二点半」。凡是听到 <code>puoli</code>，先取后面那个数，<b>减一</b>，再想「那个小时的半点」。同理 <code>puoli kuusi</code> = 5:30，<code>puoli kymmenen</code> = 9:30。",
            )
            + p(
                "<code>vailla</code> 与 <code>vaille</code> 是同一词的两种形态，材料注明 <code>vailla = vaille</code>，两者都可使用；口语里 <code>vaille</code> 更常见。<code>vartti</code>（一刻钟）的部分格是 <code>varttia</code>，属格是 <code>vartin</code>，所以「一刻过」有两种说法：<code>vartin yli</code> 与 <code>varttia yli</code>。"
            )
            + h3("3.4 加时段限定：区分同名时刻")
            + p(
                "十二小时制里 12:30 与 00:30 都读 <code>puoli yksi</code>，靠时段词区分：<code>Kello on puoli yksi päivällä</code>（中午十二点半）／<code>Kello on puoli yksi yöllä</code>（夜里十二点半）。常用时段词："
            )
            + tb(
                ("时段词", "含义", "例句"),
                ("aamulla", "早上", "Kello on viisi aamulla."),
                ("päivällä", "白天 / 中午", "Kello on puoli yksi päivällä."),
                ("aamupäivällä", "上午", "Kello on kymmenen aamupäivällä."),
                ("iltapäivällä", "下午", "Kello on viisi iltapäivällä."),
                ("illalla", "晚上", "Kello on yhdeksän illalla."),
                ("yöllä", "夜里", "Kello on puoli yksi yöllä."),
            )
            + p(
                "这四个词全部是 -lla 形式，与第 2 讲的季节同理：把时段看作「时间表面」。"
            )
            + h3("3.5 时间单位与换算")
            + ul(
                "<code>sekunti</code> 秒；<code>minuutti</code> 分；<code>tunti</code> 小时；<code>vuorokausi / päivä</code> 一天；<code>viikko</code> 一周。",
                "<code>60 sekuntia = minuutti</code>；<code>60 minuuttia = tunti</code>；<code>24 tuntia = vuorokausi</code>；<code>7 päivää = viikko</code>。",
                "<code>kuukausi</code> 月；<code>vuosi</code> 年；<code>vuosikymmen</code> 十年。",
            )
            + p(
                "注意数量表达：<code>kaksi tuntia</code>、<code>kolme päivää</code>、<code>viisi minuuttia</code> —— 2 以上的数词后面接<b>部分格单数</b>，这与第 1 讲的 <code>kaksikymmentä vuotta</code> 一致。"
            )
            + h3("3.6 Milloin 的四类时间格")
            + p(
                "把这一讲与第 2 讲合起来看，<code>Milloin?</code> 的答句按名词类别分成四种后缀，这是本课程时间表达的总纲："
            )
            + tb(
                ("问什么", "用的格", "例子", "记忆锚点"),
                (
                    "钟点（几点）",
                    "-lta/-ltä",
                    "yhdeltä, kahdelta, kolmelta, kuudelta, kymmeneltä",
                    "「从某个钟点起」→ 从格",
                ),
                (
                    "星期（周几）",
                    "-na/-nä",
                    "maanantaina, tiistaina, keskiviikkona, torstaina, perjantaina, lauantaina, sunnuntaina",
                    "「作为那一天」→ 样格",
                ),
                (
                    "月份（几月）",
                    "-ssa/-ssä",
                    "tammikuussa … joulukuussa",
                    "「在月份内部」→ 内格",
                ),
                (
                    "季节（哪个季节）",
                    "-lla/-llä",
                    "keväällä, kesällä, syksyllä, talvella",
                    "「在时间表面」→ 上格",
                ),
                (
                    "一天中的时段",
                    "-lla/-llä",
                    "aamulla, päivällä, illalla, yöllä",
                    "同上",
                ),
                (
                    "周末 / 工作日",
                    "-na / -lla",
                    "viikonloppuna；arkena",
                    "viikonloppu 用 -na；arki 用 -na",
                ),
            )
            + p("钟点的 -lta 形式要逐个记住，因为会发生辅音交替与词形变化：")
            + tb(
                ("数字", "Milloin 形式", "备注"),
                ("1", "yhdeltä", "yksi 的特殊词干 yhde-"),
                ("2", "kahdelta", "kaksi → kahde-"),
                ("3", "kolmelta", "kolme + lta"),
                ("4", "neljältä", "neljä + ltä"),
                ("5", "viideltä", "viisi → viide-"),
                ("6", "kuudelta", "kuusi → kuude-"),
                ("7", "seitsemältä", "seitsemän + ltä"),
                ("8", "kahdeksalta", "kahdeksan + lta"),
                ("9", "yhdeksältä", "yhdeksän + ltä"),
                ("10", "kymmeneltä", "kymmenen + ltä"),
                ("11", "yhdeltätoista", "11 = yksi + toista，词干仍 yhde-"),
                ("12", "kahdeltatoista", "12 = kaksi + toista"),
            )
            + p(
                "三个问法在语义上略有差别：<code>Milloin syöt lounasta?</code>（什么时候吃午饭，可答钟点、也可答时段）、<code>Mihin aikaan syöt lounasta?</code>（几点吃，要求钟点）、<code>Monelta / Moneltako syöt lounasta?</code>（几点，最口语，答句就是 -lta 形式）。"
            )
            + h3("3.7 星期的写法与缩写")
            + p(
                "七个星期词与缩写：<code>maanantai</code>(MA)、<code>tiistai</code>(TI)、<code>keskiviikko</code>(KE)、<code>torstai</code>(TO)、<code>perjantai</code>(PE)、<code>lauantai</code>(LA)、<code>sunnuntai</code>(SU)。全部小写；缩写只在表格、课表里用，句子里要写全。"
            )
            + p(
                "问「今天星期几」用 <code>Mikä päivä nyt on?</code>，答 <code>Nyt on tiistai</code>（主格，因为是在「指认」哪一天）。问「星期几做某事」用 <code>Milloin …?</code> 或 <code>Minä päivänä …?</code>，答句用 -na：<code>Suomen tunti on tiistaina</code>。"
            )
            + p(
                "注意区分 <code>päivä</code> 的两个用法：<code>Mikä päivä on?</code>（今天星期几）与 <code>Minä päivänä?</code>（在哪一天）。前者问「哪一天（星期）」，后者问「具体哪一天」。"
            )
            + h3("3.8 日期与语序")
            + p(
                "日期写作「日. 月份的部分格」：<code>14. helmikuuta</code>（2 月 14 日），读作 <code>neljästoista helmikuuta</code>。月份在此用部分格，因为日期是「月的一部分」。年份用 <code>vuonna 1999</code>。完整日期：<code>3. marraskuuta 1999</code>。"
            )
            + p(
                "句子里时间词的位置比较自由：可以句首（<code>Maanantaina minä käyn salilla</code>）也可以句尾（<code>Minä käyn salilla maanantaina</code>）。句首位置通常用来强调时间，书面语更常见。"
            )
            + cal(
                "warn",
                "高频错误 1",
                "<code>puoli kolmetoista</code> 是错的。传统系统只用 1–12 的小时数，13 以上只出现在数字时间读法里。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "<code>kello viideltä</code> 与 <code>Kello on viisi</code> 混淆。前者是「五点时（做事）」，后者是「现在五点」。前者必带 -lta，后者不带。",
            )
            + cal(
                "tip",
                "听力策略",
                "听到 <code>yli</code> 就往回取当前小时，听到 <code>vailla / vaille</code> 或 <code>puoli</code> 就往前取下一个小时。先定方向，再算分钟，最后核对时段词。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            (
                "Mitä kello on?",
                "现在几点？",
                "What time is it? Also Paljonko kello on?",
            ),
            (
                "digitaalinen aika",
                "数字时间",
                "Digital reading: 12.34 = kaksitoista kolmekymmentäneljä.",
            ),
            (
                "perinteinen aika",
                "传统时间",
                "Traditional reading with yli, vailla and puoli.",
            ),
            ("yli", "过", "Minutes past the hour: viisi yli kuusi = 6:05."),
            (
                "vailla / vaille",
                "差",
                "Minutes to the next hour: kymmenen vailla seitsemän = 6:50.",
            ),
            ("vartti", "一刻钟", "Quarter of an hour: vartin yli / varttia vailla."),
            ("puoli", "半点（指向下一小时）", "puoli yksi = 12:30, not 1:30."),
            ("tasan", "整", "Kello on tasan yksi = exactly one o’clock."),
            (
                "aamulla, päivällä, illalla, yöllä",
                "早上、白天、晚上、夜里",
                "Parts of the day take -lla.",
            ),
            (
                "maanantaina",
                "周一（样格）",
                "Weekdays take -na: tiistaina, keskiviikkona.",
            ),
            (
                "yhdeltä, kahdelta",
                "一点、两点（从格）",
                "Clock time in answers to Milloin takes -lta.",
            ),
            ("kuukausi", "月", "Month; kuukaudessa = in a month."),
            ("vuorokausi", "一昼夜", "24 tuntia = vuorokausi."),
            (
                "viikonpäivä",
                "星期",
                "Weekday; the seven names are written in lower case.",
            ),
            ("tunti", "小时", "Hour as a duration: kaksi tuntia."),
            ("Mihin aikaan?", "几点？", "Asks for a clock time: Mihin aikaan syöt?"),
        ),
        examples=(
            qa(
                "例 1　把 17:30 用传统与数字两种方式读出来。",
                p(
                    "<b>解：</b>传统：<code>puoli kuusi</code>（朝着六点走了一半 → 5:30），若要限定可说 <code>puoli kuusi iltapäivällä</code>。数字：<code>Kello on seitsemäntoista kolmenkymmentä</code>。"
                )
                + p(
                    "<b>易错点：</b>不要读成 <code>puoli seitsemän</code>（那是 6:30），也不要读 <code>puoli seitsemäntoista</code>。"
                ),
            )
            + qa(
                "例 2　把 9:45 读成传统时间，并说明为什么用 vailla 而不是 yli。",
                p(
                    "<b>解：</b>45 分已经过了半点，按规则要往下一个整点（10 点）数差多少：差 15 分。所以是 <code>varttia vailla kymmenen</code> 或 <code>viisitoista vailla kymmenen</code>。"
                )
                + p(
                    "<b>判断口诀：</b>分钟 ≤ 30 用 <code>yli</code> + 当前小时；分钟 &gt; 30 用 <code>vailla</code> + 下一小时；正好 30 用 <code>puoli</code> + 下一小时。"
                ),
            )
            + qa(
                "例 3　回答 <code>Milloin sinä heräät?</code>，设定 6:40 起床。",
                p(
                    "<b>解：</b>6:40 的分钟大于 30，用 vailla 加下一个小时：差 20 分七点 → <code>Herään kaksikymmentä vailla seitsemän</code>。也可加时段：<code>Herään kaksikymmentä vailla seitsemän aamulla</code>。"
                )
                + p(
                    "<b>语法点：</b>答句的动词用第一人称（herään），时间短语放在句尾，<b>时间词本身不再加 -lta</b>，因为 vailla 结构已经表示「差多少到几点」。"
                ),
            )
            + qa(
                "例 4　把「星期二我在校园，从九点到十二点有芬兰语课」译成两句芬兰语。",
                p(
                    "<b>解：</b>第一句：<code>Tiistaina olen kampuksella.</code>（星期 -na，地点 -lla，kampusi → kampuksella 有 k→ks 的变化）。第二句：<code>Suomen tunti on yhdeksästä kahteentoista.</code>"
                )
                + p(
                    "<b>要点：</b>表示时间段「从几点到几点」用 <code>-sta … -hVn</code>（elative + illative）：<code>yhdeksästä</code>（从九点）、<code>kahteentoista</code>（到十二点）。这与单点时刻的 -lta 不同，材料正文只给了单点，属衔接性拓展。"
                ),
            )
        ),
        practice=(
            ol(
                "用传统时间读出：7:15、11:40、14:30、18:55、22:05。",
                "用数字时间读出：8:30、13:00、16:45、19:10。",
                "把七个星期写成 -na 形式，并用其中三个各造一句 <code>Milloin …?</code> 的答句。",
                "翻译：「我每天早上七点起床，晚上十一点睡觉。」",
                "改错：<code>Kello on puoli kolmetoista.</code> / <code>Kello on viisi yli kaksitoista</code>（想表达 11:55）/ <code>Menen nukkumaan kello yksitoista.</code>",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> 7:15 <code>vartin yli seitsemän</code>；11:40 <code>kaksikymmentä vailla kaksitoista</code>；14:30 <code>puoli kolme</code>（下午两点半）；18:55 <code>viisi vailla seitsemän</code>；22:05 <code>viisi yli kymmenen</code>（晚上）。"
                )
                + p(
                    "<b>2.</b> 8:30 <code>kahdeksan kolmenkymmentä</code>；13:00 <code>kolmetoista (nolla-nolla)</code>；16:45 <code>kuusitoista neljäkymmentäviisi</code>；19:10 <code>yhdeksäntoista kymmenen</code>。"
                )
                + p(
                    "<b>3.</b> <code>maanantaina, tiistaina, keskiviikkona, torstaina, perjantaina, lauantaina, sunnuntaina</code>。答句示例：<code>Minä urheilen maanantaina ja torstaina.</code> / <code>Suomen tunti on keskiviikkona.</code> / <code>Käyn salilla lauantaina.</code>"
                )
                + p(
                    "<b>4.</b> <code>Herään joka päivä seitsemältä aamulla ja menen nukkumaan yhdeltätoista illalla.</code> 注意两个钟点都用 -lta，「每天」用 <code>joka päivä</code>（joka 后不加格）。"
                )
                + p(
                    "<b>5.</b> 三处：<code>puoli kolmetoista</code> → <code>puoli yksi</code>（12:30）或按需 <code>puoli kaksi</code>；11:55 应说 <code>viisi vailla kaksitoista</code>；<code>kello yksitoista</code> → <code>yhdeltätoista</code>。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "传统时间的 <code>yli / vailla / puoli</code> 三件套、星期 -na 与钟点 -lta 的形式、<code>Milloin?</code> 四类时间格的分工。听力题几乎必出报时。",
            )
            + cal(
                "warn",
                "易错 1",
                "<code>puoli</code> 指向下一个小时：<code>puoli yksi</code> = 12:30，写反是最常见的失分点。",
            )
            + cal(
                "warn",
                "易错 2",
                "小时数超过 12 时仍用传统系统：<code>puoli neljätoista</code> 不成立。",
            )
            + cal(
                "warn",
                "易错 3",
                "星期写成 -ssa 或 -lla：<code>maanantaissa</code>、<code>maanantailla</code> 都错，应为 <code>maanantaina</code>。",
            )
            + cal(
                "tip",
                "进阶",
                "能用 <code>-sta … -hVn</code> 表达时间段（<code>yhdeksästä kahteentoista</code>），并解释它与单点 -lta 的语义差别。",
            )
        ),
        checklist=(
            h2("报时与时间格清单")
            + h3("读任意时刻四步")
            + st(
                "先判分钟段：≤ 30 用 yli，= 30 用 puoli，&gt; 30 用 vailla",
                "yli：分钟 + yli + 当前小时",
                "puoli：puoli + 下一小时",
                "vailla：差值 + vailla + 下一小时",
                "需要时补时段词 aamulla / päivällä / illalla / yöllä",
            )
            + h3("时间格四选一")
            + st(
                "钟点 → -lta：yhdeltä、kahdelta",
                "星期 → -na：tiistaina、viikonloppuna",
                "月份 → -ssa：huhtikuussa",
                "季节与时段 → -lla：kesällä、illalla",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "04_Tunti 3/1_Kertaa kello ja päivät.docx",
                "全篇 4 题",
                "传统与数字时间书写练习、星期缩写 MA–SU、六类 Milloin 问答",
            ),
            (
                "04_Tunti 3/2_VASTAUKSET- Kello ja päivät.pdf",
                "p1–p2",
                "12 组时刻的标准答案、星期全名、-lta/-na/-ssa 答句范例",
            ),
            (
                "04_Tunti 3/3_kello.pdf",
                "p2–p6",
                "三种问时间、数字时间、传统时间 yli/vailla/vartti/puoli、时段词、时间单位",
            ),
            (
                "04_Tunti 3/4_Viikonpäivät jne.pdf",
                "p2–p4",
                "七个星期、十二个月、四季、芬兰语不大写",
            ),
            (
                "04_Tunti 3/5_Milloin.pdf",
                "p2–p6",
                "Milloin 的四类答句：钟点 -lta、星期 -na、时段 -lla、月份 -ssa、季节 -lla",
            ),
            (
                "04_Tunti 3/6_Puhu Milloin_.html",
                "全篇",
                "口语问句模板：Milloin syöt / heräät / menet nukkumaan / urheilet",
            ),
            (
                "（补充）",
                "3.8",
                "日期写法与 <code>-sta … -hVn</code> 时间段表达为衔接性拓展，原文只给单点时刻",
            ),
            (
                "（跳过）",
                "—",
                "1_Kertaa kello ja päivät 的表格式空行属练习版面，无新增语言点",
            ),
        ),
    )
)

LEC.append(
    L(
        slug="t4-future-plans",
        tzh="第 4 讲 · 将来表达与周末计划",
        ten="Expressing the Future and Making Plans",
        keywords=[
            "present tense as future",
            "time expression",
            "tulla + maan",
            "going to",
            "illative",
            "adessive of place",
            "plan",
        ],
        files=[
            "05_Tunti 4/4_futuuri, korjattu.pdf",
            "05_Tunti 4/5_EXTRA, futuuri, korjattu.pptx",
            "05_Tunti 4/1_KOTITEHTÄVÄ (Tunti 3) Sanasto, Mitä teet viikonloppuna_/intro/Sanasto, mitä teet viikonloppuna.docx",
            "05_Tunti 4/3_PUHU PARILLE.html",
            "05_Tunti 4/6_KOTITEHTÄVÄ Mitä teet ensi viikolla_/intro/Kotitehtävä, ensi viikolla.docx",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第四讲回答一个初学者必问的问题：芬兰语的「将来时」在哪？答案是<b>没有独立的将来时</b>，将来由「现在时 + 时间词」共同表达。这一讲因此同时是语法课（时间副词系统）和句型课（<code>tulla + -maan</code>）。"
            )
            + p(
                "它还把第 3 讲的时间格真正用起来：<code>ensi viikolla</code>、<code>ensi maanantaina</code>、<code>viikonloppuna</code> 全部是前面学过的 -lla / -na 形式，只是前面多了一个 <code>ensi</code>（下一个）。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "解释为什么 <code>Huomenna ostan ruokaa</code> 已经是将来句，并列出十个以上的将来时间词",
                "用 <code>tulla + -maan/-mään</code> 结构表达「确定会做」的语气，并正确构造 -ma 形式",
                "回答 <code>Mitä teet illalla / huomenna / viikonloppuna / ensi viikolla?</code> 并给出两句以上计划",
                "区分移动动词搭配的地点格（<code>menen salille</code>、<code>menen kauppaan</code>、<code>käyn salilla</code>）",
                "用 <code>ajattelin</code>、<code>minun pitää</code> 等短语补充计划与义务的表达",
            )
        ),
        detail=(
            h3("4.1 芬兰语没有将来时")
            + p(
                "材料的第一句就是结论：<code>Finnish language doesn’t have a separate tense for future actions. Instead, we use the present tense.</code> 芬兰语只有现在时与过去时两套时间形式（过去时在本课程只以个别词形出现，见第 6、12 讲），将来完全靠现在时加时间状语。"
            )
            + p("同一句现在时可以指现在，也可以指将来，区别只在时间词：")
            + tb(
                ("句子", "含义", "时间指向"),
                ("Tänään ostan ruokaa.", "今天我买菜。", "现在 / 今天"),
                ("Huomenna ostan ruokaa.", "明天我将买菜。", "将来"),
                ("Ensi viikolla menen salille.", "下周我去健身房。", "将来"),
                (
                    "Illalla katson elokuvan.",
                    "晚上我要看一部电影。",
                    "将来（今天晚些）",
                ),
                ("Joka päivä käyn koulussa.", "我每天去学校。", "习惯性，跨现在与将来"),
            )
            + cal(
                "tip",
                "判断口诀",
                "看到动词是现在时，先不要译成「正在」。先找句子里有没有将来时间词；有就是将来，没有才是现在。反过来，写作时想说「将要」，只需要加时间词，不必造新形式。",
            )
            + h3("4.2 将来时间词系统")
            + p("下面是材料给出的将来时间词，全部可以直接放在句首或句尾：")
            + tb(
                ("时间词", "含义", "构成说明"),
                ("tänään", "今天", "时间副词，不变格"),
                ("huomenna", "明天", "-na 形式（样格），与星期同理"),
                ("myöhemmin", "稍后、以后", "比较级形式的副词"),
                ("ensi maanantaina", "下周一", "ensi + 星期 -na"),
                ("ensi viikolla", "下周", "ensi + viikko 的 -lla"),
                ("ensi vuonna", "明年", "ensi + vuosi 的 -na"),
                ("ensi kerralla", "下次", "ensi + kerta 的 -lla"),
                ("ensi viikonloppuna", "下个周末", "ensi + viikonloppu 的 -na"),
                ("jatkossa", "今后、往后", "jatko 的 -ssa，固定副词"),
                ("tulevaisuudessa", "在未来", "tulevaisuus 的 -ssa"),
                ("illalla", "晚上", "ilta 的 -lla"),
                ("viikonloppuna", "周末", "viikonloppu 的 -na"),
                ("ylihuomenna", "后天", "yli + huomenna"),
            )
            + p(
                "注意 <code>ensi</code> 与 <code>viime</code> 的对立：<code>ensi viikolla</code>（下周）／<code>viime viikolla</code>（上周）。<code>ensi</code> 本身不变格，格加在后面的名词上，这是「前修饰语不变、中心词变格」的典型例子（第 9 讲属格部分会再遇到同类结构）。"
            )
            + p(
                "还有一个细节：<code>huomenna</code> 与 <code>tänään</code> 是副词，不带格词尾；而 <code>ensi maanantaina</code>、<code>ensi viikolla</code> 是「修饰语 + 变格名词」的组合。写作时不要写成 <code>ensi viikko</code> 当时间状语，必须变格。"
            )
            + h3("4.3 tulla + -maan/-mään：强调式的将来")
            + p(
                "除了「现在时 + 时间词」，还有一种更有把握、更强调的将来表达：<b><code>tulla</code> 的现在时 + 主动作动词的 -maan/-mään 形式</b>。材料把它描述为 <code>more pressuring way to tell that something will happen</code>，即「肯定会、我保证会」。"
            )
            + p("结构分两步：")
            + st(
                "把 <code>tulla</code> 按人称变位：<code>tulen, tulet, tulee, tulemme, tulette, tulevat</code>",
                "把主动作动词变成 -ma/-mä 形式，再加 <code>-an/-än</code> 的 illative 词尾，得到 <code>-maan/-mään</code>",
                "主动作动词的人称由 <code>tulla</code> 承担，后面那个形式<b>不再变人称</b>",
            )
            + p("材料给的六个转换例子正好覆盖六类动词，可以当作构造模板：")
            + tb(
                ("原形", "-maan / -mään 形式", "构造过程"),
                ("ostaa", "ostamaan", "词干 osta- + maan"),
                ("juoda", "juomaan", "词干 juo- + maan（第二类去 -da）"),
                ("kävellä", "kävelemään", "词干 kävele- + mään（第三类加 -e）"),
                (
                    "haluta",
                    "haluamaan",
                    "词干 halua- + maan（第四类，注意不是 halaamaan）",
                ),
                ("tarvita", "tarvitsemaan", "词干 tarvitse- + maan（第五类加 -se）"),
                ("vanheta", "vanhenemaan", "词干 vanhene- + maan（第六类加 -ne）"),
                ("mennä", "menemään", "词干 mene- + mään"),
                ("tehdä", "tekemään", "词干 teke- + mään"),
            )
            + p(
                "例句：<code>Tulen ostamaan lahjan.</code>（我一定会买礼物。）／<code>Hän tulee tarvitsemaan lisää.</code>（他肯定会需要更多。）／<code>Me tulemme kävelemään paljon.</code>（我们一定会走很多路。）"
            )
            + cal(
                "warn",
                "两个常见错法",
                "一是 <code>Tulen ostaa</code>（把主动作留原形）；二是 <code>Minä tulen ostan</code>（给主动作也变了人称）。记住：<b>只有 tulla 变位，第二个动词永远是 -maan 形式</b>。",
            )
            + p(
                "语用提醒：这个结构语气偏重，日常对话里用得不多。多数情况单纯用现在时更自然：<code>Huomenna ostan lahjan</code> 已经足够。写作或口语考试里，一两句 <code>tulen … -maan</code> 能显示语法掌握度，但通篇使用会显得生硬。"
            )
            + h3("4.4 计划与安排的常用短语")
            + p("材料里的词汇表给了几个谈计划的高频短语，值得整块记住：")
            + ul(
                "<code>Mitä teet illalla?</code> —— 你晚上做什么？（<code>tehdä</code> 的第二人称单数 <code>teet</code>）",
                "<code>En mitään ihmeellistä.</code> —— 没什么特别的。（否定句 + 部分格 <code>mitään</code>）",
                "<code>ajattelin pysyä kotona</code> —— 我打算待在家（<code>ajattelin</code> 是「我想过 / 我打算」，过去形式但表委婉的现在意图）",
                "<code>minun pitää tehdä koulutehtäviä</code> —— 我得做课程作业（<code>pitää</code> 表义务，主语用属格 <code>minun</code>）",
                "<code>menen salille</code> —— 我去健身房（<code>sali</code> 的 -lle）",
                "<code>lähden kävelylle</code> —— 我出去散步（<code>kävely</code> 的 -lle）",
                "<code>menen baariin</code> —— 我去酒吧（<code>baari</code> 的 -hVn）",
                "<code>konserttiin</code> —— 去音乐会（illative）",
                "<code>kääntyä</code> —— 转弯；<code>Kuulostaapa hienolta!</code> —— 听起来不错啊！（<code>-pa</code> 加强语气）",
            )
            + p(
                "其中 <code>minun pitää + 动词原形</code> 是「必须」的最常用说法，与 <code>täytyy</code> 同义。注意主语用属格：<code>minun pitää</code>、<code>sinun pitää</code>、<code>hänen pitää</code>。"
            )
            + h3("4.5 移动动词与地点格：去、在、从")
            + p(
                "谈计划离不开「去哪」。芬兰语的移动动词对格很敏感，三个方向对应三类后缀："
            )
            + tb(
                ("方向", "格", "例子", "动词"),
                (
                    "去某地（进入）",
                    "-hVn / -Vn（illative）",
                    "menen kauppaan, menen salille, menen baariin, menen kotiin",
                    "mennä, lähteä, tulla",
                ),
                (
                    "在某地（内部）",
                    "-ssa/-ssä（inessive）",
                    "olen kaupassa, käyn salilla（注意 sali 用 -lla）",
                    "olla, käydä, asua",
                ),
                (
                    "在某地（表面 / 活动）",
                    "-lla/-llä（adessive）",
                    "olen salilla, olen mökillä, käyn salilla",
                    "olla, käydä",
                ),
                (
                    "从某地离开",
                    "-sta/-stä（elative）",
                    "tulen kaupasta, lähden kotoa",
                    "tulla, lähteä",
                ),
            )
            + p(
                "特别注意 <code>käydä</code>（去一下、访问）后面接 -ssa 或 -lla，表示「去某处办事 / 参加活动」：<code>käyn salilla</code>（我去健身）、<code>käyn kaupassa</code>（我去趟商店）、<code>käyn saunassa</code>（我去桑拿）。而 <code>mennä</code> 强调「去」这个动作本身，常用 illative：<code>menen kauppaan</code>。"
            )
            + p(
                "另外 <code>koti</code>（家）的 illative 是不规则的 <code>kotiin</code>，elative 是 <code>kotoa</code>：<code>Menen kotiin</code>（我回家）、<code>Tulen kotoa</code>（我从家里来）。这两个形式必须单独记。"
            )
            + h3("4.6 否定的将来与「不做」")
            + p(
                "否定式与现在时否定相同：<code>en</code> + 动词词干。<code>Huomenna en mene salille, minä lepään.</code>（明天我不去健身，我休息。）注意否定的宾语若出现，同样要部分格：<code>En osta ruokaa tänään.</code>"
            )
            + p(
                "材料里有一个很实用的否定答句 <code>En mitään ihmeellistä</code>：<code>mitään</code> 是 <code>mitä</code> 的部分格（否定句要求），<code>ihmeellistä</code> 是形容词部分格，与 <code>mitään</code> 一致。"
            )
            + h3("4.7 写作任务：用现在时写「下周」")
            + p(
                "材料的家庭作业要求写「下周我做什么」，每天两件事，明确要求 <code>Käytä preesensiä ilmaisemaan futuuria</code>（用现在时表达将来）。这类写作有三条硬要求："
            )
            + ol(
                "每天的时间词必须用 -na 形式：<code>maanantaina, tiistaina, keskiviikkona, torstaina, perjantaina, lauantaina, sunnuntaina</code>",
                "每天至少两个动词，且动词要按人称变位（第一人称单数 -n）",
                "若出现宾语，判断该用总格还是部分格（第 10 讲详述），拿不准时优先部分格",
            )
            + p(
                "示例段落：<code>Maanantaina minä menen kouluun ja opiskelen suomea. Tiistaina käyn salilla ja luen kirjaa. Keskiviikkona minä tapaan ystävän ja syömme pizzaa.</code>"
            )
            + cal(
                "warn",
                "高频错误 1",
                "用 <code>ensi viikko</code> 作时间状语（缺格）：应为 <code>ensi viikolla</code>。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "把 <code>tulla + -maan</code> 当成唯一将来式，所有句子都套：日常用现在时更自然，<code>tulen tekemään</code> 只在强调确定性时用。",
            )
            + cal(
                "tip",
                "口语提示",
                "口语里「将来」还常用 <code>meen</code>（menen）、<code>tuun</code>（tulen）、<code>teen</code>（teen）这类缩短形式，听力里听到不要当成新词。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("preesens", "现在时", "The present tense also expresses the future."),
            ("huomenna", "明天", "Tomorrow; an adverb, no case ending."),
            ("ensi viikolla", "下周", "ensi + viikko in the adessive."),
            ("ensi maanantaina", "下周一", "ensi + weekday in the essive."),
            ("myöhemmin", "稍后", "Later."),
            ("tulevaisuudessa", "在未来", "In the future."),
            ("jatkossa", "今后", "From now on; a fixed adverb."),
            (
                "tulla + -maan",
                "将要（强调）",
                "Tulen ostamaan = I will definitely buy.",
            ),
            (
                "ostamaan",
                "去买（-maan 形式）",
                "The -ma form of ostaa, used after tulla.",
            ),
            ("menemään", "去（-maan 形式）", "The -ma form of mennä."),
            (
                "ajattelin",
                "我打算",
                "ajattelin pysyä kotona = I was thinking of staying home.",
            ),
            (
                "minun pitää",
                "我必须",
                "Obligation with the genitive subject: minun pitää tehdä.",
            ),
            ("salille", "去健身房", "Allative of sali: menen salille."),
            ("kotiin", "回家", "Irregular illative of koti; kotoa = from home."),
            ("ostoksille", "去买东西", "mennä ostoksille = to go shopping."),
            ("konserttiin", "去音乐会", "Illative of konsertti."),
        ),
        examples=(
            qa(
                "例 1　把「明天我买菜，然后去健身房」译成芬兰语，并改用强调式重说一遍。",
                p(
                    "<b>解：</b>普通式：<code>Huomenna ostan ruokaa ja menen salille.</code> 强调式：<code>Huomenna tulen ostamaan ruokaa ja menemään salille.</code>"
                )
                + p(
                    "<b>要点：</b><code>ruokaa</code> 是部分格（买的是「一些食物」）；<code>salille</code> 是 -lle，因为 sali 被视为「活动场所」。强调式里两个主动作都变 -maan，只有 <code>tulen</code> 变位。"
                ),
            )
            + qa(
                "例 2　判断下列句子指现在还是将来，并说明依据：<code>Käyn joka päivä koulussa.</code> / <code>Ensi kerralla tulen ajoissa.</code> / <code>Illalla katson elokuvan.</code>",
                p(
                    "<b>解：</b>第一句是习惯性（跨现在与将来），依据是 <code>joka päivä</code>。第二句是将来，依据是 <code>ensi kerralla</code> 与强调式 <code>tulen</code>。第三句是将来（今晚），依据是 <code>illalla</code>。"
                )
                + p(
                    "<b>注意：</b><code>katson elokuvan</code> 用总格宾语（-n），表示「看完整部」；若说 <code>katson elokuvaa</code> 则是「在看、没看完」，这是第 10 讲的部分格与总格对立。"
                ),
            )
            + qa(
                "例 3　构造 <code>haluta</code> 的 -maan 形式并造句「我肯定会想要更多」。",
                p(
                    "<b>解：</b><code>haluta</code> 属第四类，词干是 <code>halua-</code>（不是 <code>hala-</code>），加 <code>-maan</code> 得 <code>haluamaan</code>。句：<code>Minä tulen haluamaan lisää.</code>"
                )
                + p(
                    "<b>易错点：</b>受 <code>halata</code>（拥抱 → halaan）干扰，容易写成 <code>halaamaan</code>，那是「来拥抱」的意思。"
                ),
            )
            + qa(
                "例 4　回答 <code>Mitä teet viikonloppuna?</code>，写三句，其中一句用 <code>pitää</code> 表义务。",
                p(
                    "<b>解：</b><code>Lauantaina minä käyn salilla ja tapaan ystäviä.</code> / <code>Sunnuntaina minun pitää tehdä koulutehtäviä.</code> / <code>Illalla katson elokuvan kotona.</code>"
                )
                + p(
                    "<b>核对：</b>星期 -na、<code>minun pitää</code> 主语属格、<code>koulutehtäviä</code> 部分格复数、<code>elokuvan</code> 总格。"
                ),
            )
        ),
        practice=(
            ol(
                "列出十个将来时间词，并用其中五个各造一句计划句。",
                "把下列动词变成 -maan/-mään 形式：ostaa、juoda、kävellä、tarvita、vanheta、mennä、tehdä。",
                "翻译：「下周我会开始学芬兰语，并且每天听芬兰广播。」",
                "改错：<code>Ensi viikko minä menen salille.</code> / <code>Huomenna minä tulen ostaa ruokaa.</code> / <code>Minä pitää tehdä kotitehtävät.</code>",
                "写一段 5 句的「下周计划」，每天至少一个动词，最后一句用否定式说明哪天不做什么。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> 示例十个：<code>tänään, huomenna, ylihuomenna, illalla, viikonloppuna, ensi viikolla, ensi maanantaina, ensi vuonna, myöhemmin, tulevaisuudessa</code>。造句：<code>Ensi viikolla minä aloitan uuden kurssin.</code>"
                )
                + p(
                    "<b>2.</b> <code>ostamaan, juomaan, kävelemään, tarvitsemaan, vanhenemaan, menemään, tekemään</code>。检查点：第四类 haluta/tarvita 类是否保留了原来的元音（tarvitse-）。"
                )
                + p(
                    "<b>3.</b> <code>Ensi viikolla minä aloitan suomen opiskelun ja kuuntelen suomalaista radiota joka päivä.</code> 第一句动作可用 <code>tulen aloittamaan</code> 强化；<code>joka päivä</code> 不加格。"
                )
                + p(
                    "<b>4.</b> 三处：<code>ensi viikko</code> → <code>ensi viikolla</code>；<code>tulen ostaa</code> → <code>tulen ostamaan</code>；<code>minä pitää</code> → <code>minun pitää</code>。"
                )
                + p(
                    "<b>5.</b> 示例：<code>Maanantaina minä menen kouluun ja opiskelen suomea. Tiistaina käyn salilla. Keskiviikkona tapaan ystävän. Torstaina minun pitää tehdä koulutehtäviä. Perjantaina en mene baariin, minä lepään kotona.</code>"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "「现在时表将来」这一原则、将来时间词的格（ensi viikolla / ensi maanantaina / viikonloppuna）、<code>tulla + -maan</code> 的构造。",
            )
            + cal(
                "warn",
                "易错 1",
                "<code>tulla + -maan</code> 里给第二个动词也变人称：<code>tulen ostamaan</code> 对，<code>tulen ostan</code> 错。",
            )
            + cal(
                "warn",
                "易错 2",
                "<code>ensi</code> 后面的名词忘变格：<code>ensi viikko</code>、<code>ensi kuukausi</code> 都缺格。",
            )
            + cal(
                "warn",
                "易错 3",
                "移动动词的格混淆：<code>menen salille</code>（去）与 <code>olen salilla</code>（在）不能互换。",
            )
            + cal(
                "tip",
                "进阶",
                "能说明 <code>tulen ostamaan</code> 与 <code>ostan</code> 的语用差别（承诺 / 确定性 vs 中性叙述），并在写作中按语境选择。",
            )
        ),
        checklist=(
            h2("谈计划清单")
            + h3("造句四步")
            + st(
                "先定时间词，并检查它的格：下周 -lla、周一 -na、周末 -na",
                "动词用现在时并按人称变位",
                "检查宾语：否定或部分动作 → 部分格；完整动作 → 总格",
                "需要强调确定性时改用 <code>tulen + -maan</code>",
            )
            + h3("移动三问")
            + st(
                "去哪 → illative：kauppaan、kotiin、baariin、salille",
                "在哪 → inessive / adessive：kaupassa、salilla、mökillä",
                "从哪来 → elative：kaupasta、kotoa",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "05_Tunti 4/4_futuuri, korjattu.pdf",
                "p1–p3",
                "现在时 = 将来、八个将来时间词、Tänään/Huomenna 对照",
            ),
            (
                "05_Tunti 4/5_EXTRA, futuuri, korjattu.pptx",
                "slide 2–3",
                "tulla + -maan/-mään 结构、六个动词转换、两句范例",
            ),
            (
                "05_Tunti 4/1_KOTITEHTÄVÄ … Sanasto, mitä teet viikonloppuna.docx",
                "全篇",
                "周末计划词汇：tehdä、ajattelin、pitää tehdä、mennä salille、lähteä kävelylle、konserttiin",
            ),
            (
                "05_Tunti 4/3_PUHU PARILLE.html",
                "全篇 7 问",
                "口语问句模板：Mitä tekee illalla / viikonloppuna、Missä opiskelevat",
            ),
            (
                "05_Tunti 4/6_KOTITEHTÄVÄ … ensi viikolla.docx",
                "全篇",
                "写作任务要求：用现在时表将来、星期 -na 逐日安排",
            ),
            (
                "（补充）",
                "4.5",
                "illative / inessive / adessive 三向对照表属归纳性拓展，原文只给例句",
            ),
            ("（跳过）", "—", "材料中的图片与对话插图不含语言点"),
        ),
    )
)

LEC.append(
    L(
        slug="t5-present-tense-vt1",
        tzh="第 5 讲 · 现在时与第一类动词",
        ten="Present Tense and Verb Type 1",
        keywords=[
            "personal pronoun",
            "conjugation",
            "verb type 1",
            "personal ending",
            "negative verb",
            "consonant gradation",
            "vowel harmony",
        ],
        files=[
            "06_Tunti 5/1_Fi2, preesens.pdf",
            "06_Tunti 5/2_Verbejä, tyyppi1.pdf",
            "06_Tunti 5/3_Astevaihtelu.pdf",
            "06_Tunti 5/4_KOTITEHTÄVÄ Kirjoita 10 lausetta_/intro/Kirjoita 10 lausetta, VT1.docx",
        ],
        overview=(
            h2("本节定位")
            + p(
                "从这一讲开始进入动词体系。Tunti 5 只做一件事：把第一类动词（-a/-ä 结尾）的现在时肯定式、否定式和辅音交替（astevaihtelu）讲透。第一类动词占芬兰语常用动词的绝大多数，掌握它就能开口说大部分日常动作。"
            )
            + p(
                "这一讲也是整套课程的方法论奠基：后面第 7 讲把六类动词一次讲完时，用的正是本讲的三个工具——<b>去词尾得词干</b>、<b>加人称词尾</b>、<b>判强弱级</b>。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "按六个主语人称正确变位任意第一类动词，并说明每个人称词尾的来源",
                "用 <code>ei</code> 的六个人称形式构成否定句，且不误用 <code>eivät</code> 搭配单数主语",
                "判断一个第一类动词在变位时是否发生辅音交替，以及哪个人称用强级",
                "背出 kk→k、pp→p、tt→t、k→∅、p→v、t→d 等主要交替对，并给例词",
                "解释为什么 <code>hän puhuu</code> 是两个 u 而 <code>minä puhun</code> 只有一个",
            )
        ),
        detail=(
            h3("5.1 人称代词与「动词要跟着变」")
            + p(
                "材料开篇就点明：<code>Finnish verbs don’t always look the same. We call this conjugation.</code> 芬兰语动词必须与人称一致，这一点与英语只有第三人称加 -s 不同，芬兰语六个人称各有词尾。"
            )
            + tb(
                ("人称", "单数", "复数"),
                ("第一人称", "minä = I", "me = we"),
                ("第二人称", "sinä = you", "te = you（复数 / 敬称）"),
                ("第三人称", "hän = she/he", "he = they"),
            )
            + p(
                "<code>hän</code> 不分性别，既可指她也可指他；<code>te</code> 既可指「你们」，也可用于对一位长辈或客户的敬称（类似法语 vous）。口语里 <code>hän</code> 常说成 <code>se</code>，<code>he</code> 常说成 <code>ne</code>，考试书面语仍用 hän / he。"
            )
            + h3("5.2 第一类动词的变位规则")
            + p(
                "规则只有一句：<b>去掉不定式末尾的 -a/-ä，得到词干，再加人称词尾</b>。材料写作 <code>–a/ä pois (-a/ä off)</code>。"
            )
            + p(
                "<code>puhua</code> → 词干 <code>puhu-</code>；<code>asua</code> → 词干 <code>asu-</code>；然后："
            )
            + tb(
                ("人称", "词尾", "puhua", "asua", "yrittää"),
                ("minä", "-n", "puhun", "asun", "yritän"),
                ("sinä", "-t", "puhut", "asut", "yrität"),
                ("hän", "长元音（词干元音双写）", "puhuu", "asuu", "yrittää"),
                ("me", "-mme", "puhumme", "asumme", "yritämme"),
                ("te", "-tte", "puhutte", "asutte", "yritätte"),
                ("he", "-vat / -vät", "puhuvat", "asuvat", "yrittävät"),
            )
            + p(
                "第三人称单数是唯一「不加辅音词尾」的人称，它靠<b>延长词干末元音</b>表示：<code>puhu + u</code> = <code>puhuu</code>，<code>asu + u</code> = <code>asuu</code>，<code>yritä + ä</code> = <code>yrittää</code>。这也解释了为什么 <code>hän</code> 后面常出现双元音。"
            )
            + p(
                "第三人称复数 <code>-vat/-vät</code> 的选择由<b>元音和谐</b>决定：词干里有 a、o、u 时用 -vat（puhuvat、asuvat、ostavat）；词干里只有 ä、ö、y 时用 -vät（yrittävät、kysyvät、ymmärtävät）。<code>e</code> 与 <code>i</code> 是中性的，看词干其他元音决定。"
            )
            + cal(
                "tip",
                "一句口诀",
                "「一 n 二 t，三拉长，四 mme，五 tte，六 vat/vät」。把六个人称词尾按顺序念熟，变位就不会漏。",
            )
            + h3("5.3 否定式：ei + 词干")
            + p(
                "材料给了否定式的「两个配料」：<b>否定动词 <code>ei</code> 的变位形式</b> + <b>动词词干</b>（不带人称词尾）。"
            )
            + tb(
                ("人称", "否定词", "puhua 否定", "asua 否定"),
                ("minä", "en", "en puhu", "en asu"),
                ("sinä", "et", "et puhu", "et asu"),
                ("hän", "ei", "ei puhu", "ei asu"),
                ("me", "emme", "emme puhu", "emme asu"),
                ("te", "ette", "ette puhu", "ette asu"),
                ("he", "eivät", "eivät puhu", "eivät asu"),
            )
            + p(
                "关键认识：<b>否定句里主动词永远只有一种形式（词干）</b>，人称信息全部由 <code>ei</code> 承担。所以 <code>ei puhu</code> 里的 <code>puhu</code> 与 <code>hän puhuu</code> 的长元音不同 —— 否定式不拉长。"
            )
            + p(
                "材料还给了一个非常实用的「反推词干」技巧：<b>先把动词变成肯定式第一人称单数，再去掉 -n</b>。<code>minä leikin</code> → <code>leiki</code> → <code>en leiki</code>。这样即使不确定词干，也能保证否定式正确。"
            )
            + p(
                "这个技巧之所以有效，是因为第一人称单数的词尾 -n 是唯一一个「纯粹外加」的辅音词尾，去掉它不会影响词干内部结构（包括已经发生的辅音交替）。"
            )
            + h3("5.4 辅音交替（astevaihtelu / KPT change）总则")
            + p(
                "材料对辅音交替的定义是：<code>Sometimes when Finnish words are conjugated or suffixes are added to them the word itself slightly changes.</code> 发生条件是词里含 <b>K、P、T</b> 这三个「危险字母」，或含其中一个的辅音组合。名词与动词都受影响。"
            )
            + p(
                "术语：<b>vahva = strong（强级）</b>、<b>heikko = weak（弱级）</b>。材料给的判据很直白：<code>In weak version of the verb core, there is less of K, P or T</code> —— 弱级里 K/P/T 更少或消失。"
            )
            + tb(
                ("交替对（强 → 弱）", "例词", "说明"),
                ("kk → k", "nukkua → nukun", "双写 k 变单 k"),
                ("pp → p", "kaappi → kaapin", "双写 p 变单 p"),
                ("tt → t", "tyttö → tytön", "双写 t 变单 t"),
                ("k → ∅", "jalka → jalan；Turku → Turussa", "k 直接消失"),
                ("p → v", "leipä → leivän；tavata → tapaan", "p 变 v；反向时 v → p"),
                ("t → d", "katu → kadun；Lahti → Lahdessa", "t 变 d"),
                ("nt → nn", "antaa → annan", "nt 变 nn"),
                ("nk → ng", "kenkä → kengän；Helsinki → Helsingissä", "nk 变 ng"),
                ("lt → ll", "ilta → illan", "lt 变 ll"),
                ("rt → rr", "ymmärtää → ymmärrän", "rt 变 rr"),
                ("mp → mm", "kampa → kamman", "mp 变 mm"),
                ("lk → l", "kulkea → kuljen", "lk 变 l"),
                ("rk → r", "arki → arjen", "rk 变 r"),
                ("ht → hd", "lähteä → lähden", "ht 变 hd"),
            )
            + h3("5.5 第一类动词里谁用强级、谁用弱级")
            + p(
                "这是本讲最重要的操作规则：<b>第一类动词变位时，hän 与 he 用强级，其余四个人称用弱级</b>（材料原文：<code>In verbtype 1, weak version of verb is used with all other pronouns but hän and he</code>）。"
            )
            + tb(
                ("人称", "nukkua 的变位", "级别"),
                ("minä", "nukun", "弱（kk → k）"),
                ("sinä", "nukut", "弱"),
                ("hän", "nukkuu", "强"),
                ("me", "nukumme", "弱"),
                ("te", "nukutte", "弱"),
                ("he", "nukkuvat", "强"),
            )
            + p(
                "为什么这样分？可以用音节结构解释：<code>-n</code>、<code>-t</code>、<code>-mme</code>、<code>-tte</code> 都以辅音开头，把词干音节「关住」（闭音节），闭音节要求弱级；而 hän 的词尾是元音延长、he 的词尾 -vat 以元音开头，音节保持开放，所以保留强级。这条解释同样适用于名词属格（第 9 讲）。"
            )
            + cal(
                "warn",
                "别把规则用反",
                "很多教材先说「第三人称强、其他人称弱」，学生容易背成「第三人称弱」。判断时记住 <b>hän/he 是开口音节 → 强级</b>，其余闭音节 → 弱级。",
            )
            + p(
                "否定式中主动词用词干，而词干本身通常就是弱级形式：<code>en nuku</code>、<code>et nuku</code>、<code>ei nuku</code>、<code>emme nuku</code>、<code>ette nuku</code>、<code>eivät nuku</code>。材料用 <code>katua</code> 示范了带交替的否定式：<code>katua → kadu</code>，故 <code>en kadu</code>、<code>et kadu</code>、<code>ei kadu</code>。"
            )
            + h3("5.6 第一类动词常用词表")
            + p(
                "材料的动词表列了 25 个第一类动词，是口语与写作的高频词库。下面按语义分组，并给出第一人称单数形式（便于直接造句）："
            )
            + tb(
                ("动词", "含义", "minä 形式", "备注"),
                ("puhua", "说、讲", "puhun", "puhua suomea"),
                ("sanoa", "说（某句话）", "sanon", "sanoa jotain"),
                ("kysyä", "问", "kysyn", "kysyä kysymys"),
                ("ymmärtää", "理解", "ymmärrän", "rt → rr 交替"),
                ("tietää", "知道", "tiedän", "t → d 交替"),
                ("asua", "住", "asun", "asua Lahdessa"),
                ("istua", "坐", "istun", "istua tuolilla"),
                ("seisoa", "站", "seison", "seisoa jonossa"),
                ("katsoa", "看", "katson", "katsoa elokuva / elokuvaa"),
                ("lukea", "读", "luen", "lukea kirjaa"),
                ("kirjoittaa", "写", "kirjoitan", "tt → t"),
                ("ostaa", "买", "ostan", "ostaa ruokaa"),
                ("maksaa", "付钱", "maksan", "maksaa kortilla"),
                ("odottaa", "等", "odotan", "odottaa bussia"),
                ("etsiä", "找", "etsin", "etsiä avainta"),
                ("harrastaa", "爱好、从事", "harrastan", "harrastaa tanssia"),
                ("matkustaa", "旅行", "matkustan", "matkustaa junalla"),
                ("rakastaa", "爱", "rakastan", "rakastaa sinua"),
                ("nauraa", "笑", "nauran", "nauraa ääneen"),
                ("itkeä", "哭", "itken", "itkeä ilosta"),
                ("tanssia", "跳舞", "tanssin", "tanssia tangoa"),
                ("laulaa", "唱歌", "laulan", "laulaa karaokea"),
                ("ajaa", "开车、骑", "ajan", "ajaa pyörällä"),
                ("saunoa", "洗桑拿", "saunon", "saunoa joka ilta"),
                ("kalastaa", "钓鱼", "kalastan", "kalastaa järvellä"),
                ("televisiota", "（看电视的搭配）", "—", "katsoa televisiota"),
            )
            + p(
                "最后一行 <code>televisiota</code> 不是动词，而是材料特意列出的搭配：<code>katsoa televisiota</code>（看电视），宾语用部分格，因为「看电视」被视为持续、非整体的活动。"
            )
            + p(
                "材料还给了两条写作要求：<code>Kirjoita 10 lausetta. Käytä jokaisessa lauseessa yhtä alla olevista verbeistä. Muista taivuttaa. Muista KPT-vaihtelu.</code>（写 10 句，每句用一个动词，记得变位与辅音交替。）范例是 <code>Me saunomme lauantaina.</code>（我们周六洗桑拿）——注意 <code>saunoa</code> 的 me 形式是 <code>saunomme</code>，不是 <code>saunomme</code> 之外的什么特殊形式，规则照常。"
            )
            + h3("5.7 元音和谐与前缀词尾的选择")
            + p(
                "芬兰语的词尾有前后两套：后元音版（a、o、u 类）与前元音版（ä、ö、y 类）。一个词内部通常只出现一套。规则是："
            )
            + ul(
                "词干里若有 a、o、u 中任意一个 → 词尾用后元音版：<code>-vat</code>、<code>-a</code>、<code>-ssa</code>。",
                "词干里只有 ä、ö、y（以及中性的 e、i）→ 词尾用前元音版：<code>-vät</code>、<code>-ä</code>、<code>-ssä</code>。",
                "例：<code>puhuvat</code>（有 u）、<code>yrittävät</code>（只有 ä/i）、<code>kysyvät</code>（只有 y）、<code>ymmärtävät</code>（ä）。",
            )
            + p(
                "这条规则解释了为什么 <code>yrittää</code> 的 hän 形式是 <code>yrittää</code>（ä + ä），而 <code>puhua</code> 是 <code>puhuu</code>（u + u）。复合词按最后一个构词成分决定和谐：<code>kirjoittaa</code>（o 为主）用后元音。"
            )
            + h3("5.8 拼写与发音细节")
            + ul(
                "双字母表示长音：<code>puhuu</code> 的两个 u 都要读长；<code>tulee</code> 的 ee 是长 e。",
                "ä 与 a 是不同音位：<code>yrittää</code> 与 <code>yrittää</code> 中的 ä 不能写成 a。",
                "ö 与 o 不同：<code>tyttö</code>、<code>kylmä</code>。",
                "y 是圆唇前元音，接近汉语「ü」但更松：<code>kysyä</code>、<code>yrittää</code>。",
            )
            + cal(
                "warn",
                "高频错误 1",
                "<code>hän puhu</code> 少一个 u。第三人称单数必须双写词干末元音。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "<code>he puhuu</code>。第三人称复数要 -vat/-vät：<code>he puhuvat</code>。",
            )
            + cal(
                "warn",
                "高频错误 3",
                "<code>minä puhuu</code>。第一人称单数是 -n：<code>puhun</code>。",
            )
            + cal(
                "tip",
                "自检三步",
                "写完一句变位句，按顺序查：① 人称词尾对不对；② 该弱化的词干有没有弱化（hän/he 除外）；③ 元音和谐是否前后一致。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("puhua", "说、讲", "Type 1 verb; stem puhu-."),
            ("puhun", "我说", "1st person singular ending -n."),
            ("puhuu", "他/她说", "3rd person singular lengthens the final vowel."),
            ("puhuvat", "他们说", "3rd person plural ending -vat."),
            (
                "en puhu",
                "我不说",
                "Negative: ei + verb stem, no personal ending on the verb.",
            ),
            ("astevaihtelu", "辅音交替", "Consonant gradation, the KPT change."),
            ("vahva aste", "强级", "Strong grade: more K, P or T."),
            ("heikko aste", "弱级", "Weak grade: less K, P or T."),
            ("kk → k", "双写 k 变单 k", "nukkua → nukun, but hän nukkuu."),
            ("pp → p", "双写 p 变单 p", "kaappi → kaapin."),
            ("tt → t", "双写 t 变单 t", "tyttö → tytön."),
            ("k → ∅", "k 消失", "jalka → jalan; Turku → Turussa."),
            ("p → v", "p 变 v", "leipä → leivän."),
            ("t → d", "t 变 d", "katu → kadun; Lahti → Lahdessa."),
            ("vartalo", "词干", "The stem that personal endings are attached to."),
            ("yrittää", "尝试", "Type 1 with tt → t: minä yritän."),
        ),
        examples=(
            qa(
                "例 1　变位 <code>ostaa</code>（买）的六个人称，并标出强弱级。",
                p(
                    "<b>解：</b>词干 <code>osta-</code>。minä <code>ostan</code>（弱，st 保留）、sinä <code>ostat</code>、hän <code>ostaa</code>（长元音）、me <code>ostamme</code>、te <code>ostatte</code>、he <code>ostavat</code>。"
                )
                + p(
                    "<b>说明：</b><code>ostaa</code> 不含 K/P/T 交替对，所以六个形式都没有强弱差别；但词尾规律完全一致。若换成 <code>maksaa</code>（付），hän 形式 <code>maksaa</code> 仍不交替，而 <code>lukea</code> 的 k 在 minä 形式 <code>luen</code> 中消失（k → ∅）。"
                ),
            )
            + qa(
                "例 2　把「我不喝咖啡，但我丈夫每天喝」译成芬兰语，注意否定式。",
                p(
                    "<b>解：</b><code>juoda</code> 属第二类，但否定式规则相同：<code>en juo</code>。整句：<code>Minä en juo kahvia, mutta minun mies juo kahvia joka päivä.</code>"
                )
                + p(
                    "<b>要点：</b>否定句主动词用词干 <code>juo</code>；宾语 <code>kahvia</code> 部分格（否定句要求）。肯定句 <code>juo kahvia</code> 也用部分格，因为咖啡是不可数名词（第 10 讲）。"
                ),
            )
            + qa(
                "例 3　判断 <code>ymmärtää</code> 在 he 形式里是否交替，并写出六个形式。",
                p(
                    "<b>解：</b>含 rt 组合，强级 rt、弱级 rr。he 用强级：<code>he ymmärtävät</code>（保持 rt）。其余人称弱化：<code>minä ymmärrän</code>、<code>sinä ymmärrät</code>、<code>me ymmärrämme</code>、<code>te ymmärrätte</code>。hän 用强级并拉长：<code>hän ymmärtää</code>。"
                )
                + p("<b>核对：</b>六个形式里，只有 hän 与 he 保留 rt，其余都是 rr。"),
            )
            + qa(
                "例 4　改错并说明理由：<code>He ei puhu suomea.</code> / <code>Minä puhuu suomea.</code> / <code>Hän nukun hyvin.</code>",
                p(
                    "<b>解：</b>第一句 <code>ei</code> 应改 <code>eivät</code>（he 对应 eivät）：<code>He eivät puhu suomea.</code> 第二句第一人称应为 <code>puhun</code>：<code>Minä puhun suomea.</code> 第三句第三人称应为 <code>nukkuu</code>：<code>Hän nukkuu hyvin.</code>"
                )
                + p(
                    "<b>共性：</b>三句都是人称与词尾不匹配。否定句要同时检查「否定词的人称」和「主动词用词干」两件事。"
                ),
            )
        ),
        practice=(
            ol(
                "变位 <code>nukkua</code>、<code>kirjoittaa</code>、<code>ymmärtää</code> 的六个人称，并标出强弱级。",
                "把下列句子改成否定句：<code>Minä asun Oulussa.</code> / <code>Hän ostaa ruokaa.</code> / <code>He puhuvat suomea.</code>",
                "写出下列动词的第一人称单数：<code>katsoa、lukea、odottaa、etsiä、ajaa、saunoa、tietää、ymmärtää</code>。",
                "翻译：「我们周六洗桑拿，然后看电视。」",
                "用五个第一类动词各写一句关于你日常生活的句子，至少两句含辅音交替。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> <code>nukkua</code>：nukun / nukut / nukkuu / nukumme / nukutte / nukkuvat（弱、弱、强、弱、弱、强）。<code>kirjoittaa</code>：kirjoitan / kirjoitat / kirjoittaa / kirjoitamme / kirjoitatte / kirjoittavat（tt 只在 hän/he 保留）。<code>ymmärtää</code>：ymmärrän / ymmärrät / ymmärtää / ymmärrämme / ymmärrätte / ymmärtävät。"
                )
                + p(
                    "<b>2.</b> <code>Minä en asu Oulussa.</code> / <code>Hän ei osta ruokaa.</code> / <code>He eivät puhu suomea.</code> 注意宾语在否定句里仍为部分格（ruokaa、suomea）。"
                )
                + p(
                    "<b>3.</b> <code>katson, luen, odotan, etsin, ajan, saunon, tiedän, ymmärrän</code>。<code>lukea → luen</code> 是 k → ∅ 交替；<code>tietää → tiedän</code> 是 t → d；<code>ymmärtää → ymmärrän</code> 是 rt → rr。"
                )
                + p(
                    "<b>4.</b> <code>Me saunomme lauantaina ja katsomme televisiota.</code> 两个动词都按 me 变位，<code>televisiota</code> 部分格。"
                )
                + p(
                    "<b>5.</b> 示例：<code>Minä juon kahvia aamulla.</code>（juoda 属第二类，仅示意）／<code>Minä luen kirjaa illalla.</code>（lukea，k → ∅）／<code>Hän puhuu suomea hyvin.</code>（puhua，强级 + 长元音）／<code>Me odotamme bussia.</code>／<code>He ymmärtävät minua.</code>（ymmärtää，强级）。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "第一类动词六个人称变位、<code>ei</code> 的六个人称与否定式词干、KPT 交替方向（hän/he 强、其余弱）。动词填空是本课程最稳定的题型。",
            )
            + cal(
                "warn",
                "易错 1",
                "<code>hän</code> 形式忘记双写词干末元音：<code>hän puhu</code>。",
            )
            + cal(
                "warn",
                "易错 2",
                "<code>he</code> 用 <code>ei</code> 而非 <code>eivät</code>：<code>he ei puhu</code> 错。",
            )
            + cal(
                "warn",
                "易错 3",
                "强弱级方向用反：把 <code>minä nukkuun</code> 当正确，或把 <code>hän nukuu</code> 当正确。",
            )
            + cal(
                "tip",
                "进阶",
                "能用「闭音节 → 弱级、开音节 → 强级」的音节原理解释交替方向，而不是死记「第三人称强」。",
            )
        ),
        checklist=(
            h2("第一类动词变位清单")
            + h3("变位五步")
            + st(
                "确认是 -a/-ä 结尾的第一类动词",
                "去掉 -a/-ä 得词干",
                "按人称加词尾：n / t / 长元音 / mme / tte / vat-vät",
                "判断有无 K/P/T 交替：除 hän、he 外都要弱化",
                "检查元音和谐：a o u 用后元音词尾，ä ö y 用前元音词尾",
            )
            + h3("否定两步")
            + st(
                "按人称选 en / et / ei / emme / ette / eivät",
                "主动词只留词干（可用「第一人称去 -n」反推）",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "06_Tunti 5/1_Fi2, preesens.pdf",
                "p2–p6",
                "人称代词表、第一类动词肯定变位、否定式 ei + 词干、去 -n 反推词干技巧",
            ),
            (
                "06_Tunti 5/2_Verbejä, tyyppi1.pdf",
                "p1",
                "25 个第一类动词词表，含 katsoa televisiota、ajaa pyörällä 等搭配",
            ),
            (
                "06_Tunti 5/3_Astevaihtelu.pdf",
                "p2–p5",
                "辅音交替定义、K/P/T 触发条件、nukkua 强弱对照、weak/strong 术语",
            ),
            (
                "06_Tunti 5/4_KOTITEHTÄVÄ … Kirjoita 10 lausetta, VT1.docx",
                "全篇",
                "写作要求：每句用一个动词、必须变位、必须体现 KPT",
            ),
            (
                "（补充）",
                "5.4、5.7",
                "14 组交替对与元音和谐规则表为归纳性拓展，原文只给 kk/pp/tt 与 nukkua 一例",
            ),
            ("（跳过）", "—", "preesens.pdf 的版面装饰与讲义封面不含语言点"),
        ),
    )
)

LEC.append(
    L(
        slug="t6-hobbies-partitive-object",
        tzh="第 6 讲 · 爱好、动名词与访谈任务",
        ten="Hobbies, Verbal Nouns and Interview Tasks",
        keywords=[
            "hobby",
            "harrastaa + partitive",
            "verbal noun -minen",
            "action noun",
            "interview question",
            "frequency adverb",
            "perfect participle",
        ],
        files=[
            "07_Tunti 6/1_harrastukset.pdf",
            "07_Tunti 6/2_PUHU PARILLE.html",
            "07_Tunti 6/3_FI2, haastattelu harrastukset.docx",
            "07_Tunti 6/4_Haastattelun tulokset.html",
            "07_Tunti 6/5_KOTITEHTÄVÄ Mitä he harrastavat_/intro/Mitä he harrastavat.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第六讲把动词与词汇接到「生活内容」上：你喜欢什么、小时候练过什么、以后想学什么。语法上它引出两条重要线索——<b><code>harrastaa</code> 后面接部分格宾语</b>，以及<b>把动作变成名词</b>（<code>elokuvan katsominen</code>、<code>musiikin kuuntelu</code>）。"
            )
            + p(
                "这一讲还第一次出现完成体形式 <code>olet harrastanut</code>。本课程不系统讲过去时与完成体，但这类形式在口语任务里反复出现，所以本讲把它作为「识别级」内容讲清构成，能听懂、能仿说即可。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "说出二十个以上爱好名词，并区分「运动项目」与「动作名词」两类表达",
                "用 <code>Harrastan + 部分格</code> 说出三个自己的爱好，并正确否定 <code>En harrasta …</code>",
                "回答现在、童年、未来三个时间层的爱好问句，并用 <code>olen harrastanut</code>、<code>haluan harrastaa</code> 作答",
                "把动词短语改写成名词短语（<code>katson elokuvaa</code> → <code>elokuvan katsominen</code>）",
                "用礼貌开场完成一次六人访谈，并汇报结果",
            )
        ),
        detail=(
            h3("6.1 爱好词汇：两类名词")
            + p("材料的爱好表混合了两类词，先分清类别，后面变格才不会乱：")
            + tb(
                ("类别", "例子", "特点"),
                (
                    "运动 / 游戏项目",
                    "jalkapallo（足球）, koripallo（篮球）, jääkiekko（冰球）, golf, tennis, sulkapallo（羽毛球）, keilaus（保龄球）",
                    "多为具体名词，作宾语时通常用部分格",
                ),
                (
                    "身体活动",
                    "pyöräily（骑车）, uinti（游泳）, hiihto（滑雪）, retkeily（徒步）, ulkoilu（户外活动）, kuntosali（健身房）",
                    "多为 -u/-y 或 -ilu 结尾的动作名词",
                ),
                (
                    "艺术 / 手工",
                    "tanssi（舞蹈）, teatteri（戏剧）, maalaus（绘画）, piirtäminen（画画）, käsityö（手工）, kokkaus（烹饪）",
                    "动作名词居多，也可指活动本身",
                ),
                (
                    "音乐",
                    "musiikki（音乐）, musiikin kuuntelu（听音乐）, pianon soitto（弹钢琴）, kitaran soitto（弹吉他）",
                    "「听 / 弹」用属格 + 动作名词",
                ),
                ("观看类", "elokuvan katsominen（看电影）", "属格 + -minen 结构"),
            )
            + p(
                "注意最后两类不是单个名词，而是「属格 + 动作名词」的短语：<code>musiikin kuuntelu</code> 直译是「音乐的听」，<code>pianon soitto</code> 是「钢琴的弹」，<code>elokuvan katsominen</code> 是「电影的看」。芬兰语用属格标出动作的对象。第 9 讲会讲属格，这里先当成固定短语记住。"
            )
            + h3("6.2 harrastaa + 部分格")
            + p(
                "材料的口语卡明确标注了答句格式：<code>Harrastan … + -a/-ä</code>，例 <code>Harrastan tanssia.</code>（我爱好跳舞）。这个 +a/-ä 就是部分格。原因与第 1 讲的「说语言」相同：爱好是一种持续、非整体的活动，宾语取部分格。"
            )
            + tb(
                ("爱好", "harrastaa 的宾语形式", "说明"),
                ("tanssi", "tanssia", "i 结尾 + a"),
                ("jalkapallo", "jalkapalloa", "o 结尾 + a"),
                ("uinti", "uintia", "i 结尾 + a"),
                ("hiihto", "hiihtoa", "o 结尾 + a"),
                ("judo", "judoa", "o 结尾 + a"),
                ("kuntosali", "kuntosalia", "i 结尾 + a"),
                ("valokuvaus", "valokuvausta", "us 结尾 + ta"),
                ("käsityö", "käsityötä", "ö 结尾 + tä"),
                ("musiikki", "musiikkia", "i 结尾 + a"),
                ("lukeminen", "lukemista", "-nen 结尾 → -sta"),
            )
            + p(
                "否定式：<code>En harrasta jalkapalloa.</code>（我不踢足球。）否定句里宾语本来就是部分格，所以词形不变，只是动词变成 <code>en harrasta</code>。"
            )
            + p(
                "与 <code>harrastaa</code> 常混用的还有 <code>pelata</code>（玩球类、游戏）与 <code>tehdä</code>（做）。区别在于：<code>harrastaa</code> 强调「长期爱好」，<code>pelata</code> 强调具体玩的行为：<code>Harrastan jalkapalloa</code>（我爱好足球）／<code>Pelaan jalkapalloa joka viikko</code>（我每周踢球）。两者后面都接部分格。"
            )
            + h3("6.3 三个时间层的爱好问句")
            + p(
                "材料的三问是本讲最值得背下来的句型组，因为它把现在、过去、将来放在一起："
            )
            + tb(
                ("问句", "含义", "答句模板"),
                ("Mitä harrastat (nyt)?", "你现在爱好什么？", "Harrastan … + 部分格"),
                (
                    "Mitä olet harrastanut lapsena?",
                    "你小时候练过什么？",
                    "Olen harrastanut … + 部分格",
                ),
                (
                    "Mitä haluat harrastaa tulevaisuudessa?",
                    "你将来想爱好什么？",
                    "Haluan harrastaa … + 部分格",
                ),
            )
            + p(
                "<code>lapsena</code> 是 <code>lapsi</code> 的样格（-na），意为「作为孩子时、小时候」；<code>tulevaisuudessa</code> 是「在未来」，第 4 讲已出现。这两个时间词分别把句子推向过去与将来。"
            )
            + p(
                "第二问的答句用了 <code>olen harrastanut</code>。这是<b>完成体</b>（perfect）形式：<code>olla</code> 的现在时 + 主动词的过去分词 <code>-nut/-nyt</code>。构成为：动词词干 + <code>-nut</code>（后元音）或 <code>-nyt</code>（前元音）。<code>harrastaa → harrastanut</code>、<code>tanssia → tanssinut</code>、<code>pelata → pelannut</code>。"
            )
            + cal(
                "tip",
                "识别级要求",
                "本课程不要求你主动变出所有完成体形式，但必须能听懂 <code>Olen harrastanut …</code>、<code>Oletko harrastanut …?</code>、<code>Olen asunut Suomessa kaksi vuotta</code> 这类句子，并仿说出 2–3 个常见动词的完成体（harrastanut、ollut、asunut、opiskellut）。",
            )
            + p(
                "第三问的 <code>haluat harrastaa</code> 是「情态动词 + 不定式」结构：<code>haluan</code>（我想要）后面直接接动词原形，不接 -maan 形式。<code>Haluan harrastaa judoa.</code>（我想练柔道。）注意与第 4 讲的 <code>tulen harrastamaan</code> 区分：<code>tulla</code> 后用 -maan，<code>haluta</code> 后用原形。"
            )
            + h3("6.4 把动作变成名词：三种手段")
            + p("材料里的爱好词大量是「动作名词」，掌握三种构词手段就能自己造：")
            + tb(
                ("手段", "例子", "构成"),
                (
                    "-minen（最通用）",
                    "elokuvan katsominen, piirtäminen, lukeminen, pelaaminen, uiminen",
                    "动词词干 + -minen；作主语或宾语时 -nen 变 -se-（katsomista）",
                ),
                (
                    "-u / -y（动作过程）",
                    "uinti, hiihto, pyöräily, retkeily, ulkoilu, tanssi, maalaus, kokkaus",
                    "常由动词词干加 -u/-y 或 -ilu/-aus 构成",
                ),
                (
                    "-us / -os（结果名词）",
                    "valokuvaus, ostos, kokemus",
                    "词干 + -us/-os",
                ),
                (
                    "复合短语（属格 + 名词）",
                    "musiikin kuuntelu, pianon soitto, elokuvan katsominen",
                    "对象用属格，动作名词在后",
                ),
            )
            + p(
                "最常见的还是 -minen。它的变格很规律：作主语时 <code>Elokuvan katsominen on hauskaa</code>（看电影很有趣）；作宾语时 -nen 变 -se- 再加部分格 <code>Harrastan elokuvan katsomista</code>（我爱好看电影）。"
            )
            + cal(
                "warn",
                "不要混用",
                "<code>Harrastan elokuvan katsominen</code> 是错的（宾语位置需要部分格 <code>katsomista</code>）；<code>Harrastan katsoa elokuvaa</code> 语法上能懂但不地道，规范说法是 <code>Harrastan elokuvan katsomista</code> 或直接用动词 <code>Katson elokuvia</code>。",
            )
            + h3("6.5 频率与程度副词")
            + p("谈爱好离不开频率，材料在阅读段落与练习里给了这些词：")
            + ul(
                "<code>usein</code> 经常；<code>joskus</code> 有时；<code>aina</code> 总是；<code>ei koskaan</code> 从不。",
                "<code>joka päivä</code> 每天；<code>joka viikko</code> 每周；<code>kerran viikossa</code> 一周一次；<code>kaksi kertaa viikossa</code> 一周两次。",
                "<code>paljon</code> 很多；<code>vähän</code> 一点；<code>tarpeeksi</code> 足够。",
            )
            + p(
                "注意 <code>kerran viikossa</code> 里 <code>viikossa</code> 是内格，表示「在一周之内（发生一次）」；<code>kertaa</code> 是 <code>kerta</code> 的部分格，因为前面有数词（第 10 讲规则）。"
            )
            + h3("6.6 访谈任务的完整脚本")
            + p(
                "材料的访谈作业要求采访六个人，并给了一段开场白：<code>Anteeksi, saanko kysyä kolme kysymystä? Tehtävä on minun suomen kurssille.</code>（打扰一下，我可以问三个问题吗？这是我芬兰语课的任务。）这句话本身就是很好的句型素材："
            )
            + ul(
                "<code>Anteeksi</code> —— 打扰一下（也可用于道歉）。",
                "<code>Saanko kysyä …?</code> —— 我可以问……吗？（<code>saada</code> 的第一人称 + -ko，礼貌请求）",
                "<code>Tehtävä on minun suomen kurssille</code> —— 任务是为我的芬兰语课（<code>kurssille</code> 是 -lle，表示「为……之用」）。",
            )
            + p(
                "正式提问前先确认对方身份：<code>Kuka sinä olet?</code>（你是谁？）。注意这里用 <code>kuka</code> 而不是 <code>mikä</code>，因为问的是人。若问名字则用 <code>Mikä sinun nimi on?</code>。"
            )
            + p(
                "汇报结果时把第三人称用起来：<code>Pernilla harrastaa ratsastusta.</code>（佩尼拉爱好骑马。）<code>Tomas ja Sadiq harrastavat jalkapalloa.</code>（两人用 <code>harrastavat</code>，复数主语配第三人称复数）。"
            )
            + h3("6.7 常见错误与自检")
            + cal(
                "warn",
                "高频错误 1",
                "<code>Harrastan tanssi.</code> 缺部分格。应为 <code>Harrastan tanssia.</code>",
            )
            + cal(
                "warn",
                "高频错误 2",
                "<code>Minun harrastus on jalkapallo.</code> 这句话语法上成立（「我的爱好是足球」），但课堂上更常用动词句。若用名词句，主语与表语都要主格，不要给表语加部分格。",
            )
            + cal(
                "warn",
                "高频错误 3",
                "<code>Haluan harrastaa judoa</code> 写对，但 <code>Haluan harrastamaan judoa</code> 是错的（<code>haluta</code> 后接原形，不接 -maan）。",
            )
            + cal(
                "tip",
                "口语加分",
                "访谈结束说一句 <code>Kiitos paljon vastauksista!</code>（非常感谢你的回答），其中 <code>vastauksista</code> 是 <code>vastaus</code> 的复数出格，属固定搭配，整句背下来即可。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("harrastaa", "爱好、从事", "Harrastan tanssia = I do dance as a hobby."),
            (
                "harrastus",
                "爱好（名词）",
                "A hobby as a thing: Minun harrastus on uinti.",
            ),
            ("tanssia", "跳舞（部分格）", "Partitive object required by harrastaa."),
            (
                "jalkapallo → jalkapalloa",
                "足球",
                "Ball games take the partitive as object.",
            ),
            ("uinti → uintia", "游泳", "Action noun; partitive uintia."),
            ("hiihto → hiihtoa", "滑雪", "Action noun in -to."),
            ("elokuvan katsominen", "看电影", "Genitive object + -minen verbal noun."),
            ("musiikin kuuntelu", "听音乐", "Genitive + action noun kuuntelu."),
            ("pianon soitto", "弹钢琴", "Genitive + soitto."),
            ("lapsena", "小时候", "Essive of lapsi: as a child."),
            ("tulevaisuudessa", "在未来", "Inessive of tulevaisuus."),
            (
                "olen harrastanut",
                "我（曾经）爱好过",
                "Perfect: olla + -nut participle.",
            ),
            ("haluan harrastaa", "我想爱好", "haluta takes the plain infinitive."),
            ("pelata", "玩（球类）", "Pelaan jalkapalloa kaksi kertaa viikossa."),
            ("usein, joskus", "经常、有时", "Frequency adverbs."),
            ("kerran viikossa", "一周一次", "kerran + viikossa (inessive)."),
        ),
        examples=(
            qa(
                "例 1　把「我小时候练过体操，现在爱好游泳，将来想学滑雪」说成三句芬兰语。",
                p(
                    "<b>解：</b><code>Olen harrastanut voimistelua lapsena.</code> / <code>Harrastan uintia nyt.</code> / <code>Haluan harrastaa hiihtoa tulevaisuudessa.</code>"
                )
                + p(
                    "<b>核对：</b>三句宾语都是部分格（voimistelua、uintia、hiihtoa）；三句动词分别是完成体、现在时、情态 + 原形。"
                ),
            )
            + qa(
                "例 2　把 <code>Katson elokuvaa illalla.</code> 改写成以动名词作宾语的句子。",
                p(
                    "<b>解：</b>对象 <code>elokuva</code> 变属格 <code>elokuvan</code>，动词 <code>katsoa</code> 变动名词 <code>katsominen</code>，作宾语时再变部分格 <code>katsomista</code>。整句：<code>Harrastan elokuvan katsomista illalla.</code>"
                )
                + p(
                    "<b>更自然：</b><code>Minun harrastus on elokuvien katsominen.</code>（我的爱好是看电影，复数对象用 <code>elokuvien</code>）。两种都可，关键是属格 + -minen 的结构不能丢。"
                ),
            )
            + qa(
                "例 3　回答 <code>Mitä sinä harrastat?</code>，要求用 <code>pelata</code> 与 <code>harrastaa</code> 各一句，并说明差别。",
                p(
                    "<b>解：</b><code>Harrastan jalkapalloa ja sählyä.</code>（我爱好足球和软式曲棍球）/ <code>Pelaan jalkapalloa kaksi kertaa viikossa.</code>（我一周踢两次足球。）"
                )
                + p(
                    "<b>差别：</b><code>harrastaa</code> 说「这是长期爱好」，<code>pelata</code> 说「具体在玩」，后者常配频率短语。两句的宾语都用部分格。"
                ),
            )
            + qa(
                "例 4　改错：<code>Minä harrastan valokuvausta ja minä haluan harrastamaan judoa.</code>",
                p(
                    "<b>解：</b>第一句正确（<code>valokuvaus → valokuvausta</code> 是 -us 结尾加 -ta）。第二句错在 <code>harrastamaan</code>，<code>haluan</code> 后要接原形：<code>Minä haluan harrastaa judoa.</code>"
                )
                + p(
                    "<b>规律：</b><code>haluta</code>、<code>osata</code>、<code>voida</code> 后接原形；<code>tulla</code>、<code>mennä</code>、<code>lähteä</code> 后接 -maan。这是两组情态 / 移动动词的分工。"
                ),
            )
        ),
        practice=(
            ol(
                "写出十个爱好名词的芬兰语，并给每个加上 <code>harrastaa</code> 所需的部分格形式。",
                "用现在、童年、将来三种时态各写一句关于自己的爱好。",
                "把下列句子改写成「属格 + 动名词」结构：<code>Kuuntelen musiikkia.</code> / <code>Soitan pianoa.</code> / <code>Piirrän kuvia.</code>",
                "翻译：「我每周游两次泳，但我不喜欢跑步。」",
                "写一段 5 句的访谈汇报：三个人各自爱好什么、频率如何、其中一人小时候练过什么。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> 示例：jalkapallo → jalkapalloa；uinti → uintia；hiihto → hiihtoa；tanssi → tanssia；kuntosali → kuntosalia；valokuvaus → valokuvausta；käsityö → käsityötä；musiikki → musiikkia；teatteri → teatteria；keilaus → keilausta。"
                )
                + p(
                    "<b>2.</b> 示例：<code>Harrastan uintia nyt.</code> / <code>Olen harrastanut tanssia lapsena.</code> / <code>Haluan harrastaa kiipeilyä tulevaisuudessa.</code>"
                )
                + p(
                    "<b>3.</b> <code>musiikin kuuntelu</code> / <code>pianon soitto</code> / <code>kuvien piirtäminen</code>（复数对象用 <code>kuvien</code>）。若作宾语则动名词再变部分格：<code>Harrastan musiikin kuuntelua.</code>"
                )
                + p(
                    "<b>4.</b> <code>Uin kaksi kertaa viikossa, mutta en pidä juoksemisesta.</code> 「不喜欢跑步」用 <code>pitää + -sta</code>（第 11 讲），<code>juokseminen</code> 的 -sta 形式是 <code>juoksemisesta</code>。"
                )
                + p(
                    "<b>5.</b> 示例：<code>Pernilla harrastaa ratsastusta kolme kertaa viikossa. Tomas pelaa jalkapalloa joka viikko. Sadiq on harrastanut judoa lapsena. He harrastavat myös ulkoilua.</code> 注意第三人称单数与复数动词的一致性。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "<code>harrastaa + 部分格</code>、三种时间层的问句与答句、属格 + <code>-minen</code> 的名词化结构。口语考试与写作都可能直接调用这些句型。",
            )
            + cal(
                "warn",
                "易错 1",
                "<code>Harrastan tanssi</code> 缺部分格，是最常见的一处丢分。",
            )
            + cal(
                "warn",
                "易错 2",
                "<code>haluan harrastamaan</code> 混用 -maan 与不定式。",
            )
            + cal(
                "warn",
                "易错 3",
                "<code>elokuvan katsominen</code> 里忘掉属格：<code>elokuva katsominen</code> 不成立。",
            )
            + cal(
                "tip",
                "进阶",
                "能主动用完成体说出 <code>Olen harrastanut … lapsena</code>，并解释 <code>-nut/-nyt</code> 与元音和谐的关系。",
            )
        ),
        checklist=(
            h2("谈爱好清单")
            + h3("三时问答")
            + st(
                "现在：<code>Mitä harrastat?</code> → <code>Harrastan + 部分格</code>",
                "童年：<code>Mitä olet harrastanut lapsena?</code> → <code>Olen harrastanut + 部分格</code>",
                "将来：<code>Mitä haluat harrastaa tulevaisuudessa?</code> → <code>Haluan harrastaa + 部分格</code>",
            )
            + h3("名词化三步")
            + st(
                "找出动作对象，变属格（elokuva → elokuvan）",
                "动词变 -minen / -u / -us 形式（katsoa → katsominen）",
                "整体作宾语时，-nen 变 -se- 再加部分格（katsomista）",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "07_Tunti 6/1_harrastukset.pdf",
                "p1",
                "二十余个爱好名词，含 elokuvan katsominen、musiikin kuuntelu、pianon soitto 三类名词化",
            ),
            (
                "07_Tunti 6/2_PUHU PARILLE.html",
                "全篇 3 问",
                "harrastaa + 部分格、三时间层问答模板、完成体 olen harrastanut",
            ),
            (
                "07_Tunti 6/3_FI2, haastattelu harrastukset.docx",
                "全篇",
                "访谈任务脚本：Anteeksi, saanko kysyä kolme kysymystä? 与三列表格",
            ),
            (
                "07_Tunti 6/4_Haastattelun tulokset.html",
                "全篇",
                "汇报结果的表格框架与第三人称表述",
            ),
            (
                "07_Tunti 6/5_KOTITEHTÄVÄ … Mitä he harrastavat.pdf",
                "p1–p2",
                "六人爱好填写练习，用于练习第三人称单数/复数",
            ),
            (
                "（补充）",
                "6.4、6.5",
                "三种名词化手段的分类与频率副词清单为归纳性拓展，原文只给词表",
            ),
            ("（跳过）", "—", "harrastukset.png 等插图不含语言点"),
        ),
    )
)

LEC.append(
    L(
        slug="t7-verb-types-1-6",
        tzh="第 7 讲 · 六类动词系统",
        ten="The Six Verb Types",
        keywords=[
            "verb type",
            "infinitive ending",
            "verb stem",
            "personal ending",
            "negative conjugation",
            "reverse gradation",
            "irregular verb",
        ],
        files=[
            "08_Tunti 7/1_verbit + astevaihtelu.docx",
            "08_Tunti 7/2_Verbityypit, pos+neg.pdf",
            "08_Tunti 7/3_PARITYÖ Mikä verbityyppi_.html",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第七讲是全课程语法密度最高的一讲：把芬兰语六类动词的识别、词干推导、肯定与否定变位一次讲完。前六讲只用到第一类（-a/-ä）与零散的第二、三、四类形式（<code>juoda</code>、<code>tulla</code>、<code>halata</code>），这一讲把它们整理成一张可查的表。"
            )
            + p(
                "材料明确写了三件事：类型按<b>不定式结尾</b>判定；每一类有固定的<b>去尾加词尾</b>规则；第三、四类要特别注意<b>辅音交替的方向与第一类不同</b>。把这三件事记牢，遇到生词也能现场推出变位。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "看到任意不定式，在 5 秒内判出它属于六类中的哪一类",
                "按类型规则推导词干，并写出六个人称的肯定形式",
                "写出六类动词的否定式，并说明为什么否定式只用一个词干",
                "解释第三、四类的交替方向与第一类「hän/he 强级」的差别",
                "处理 <code>olla</code>、<code>mennä</code>、<code>nähdä</code>、<code>tehdä</code> 等高频不规则动词",
            )
        ),
        detail=(
            h3("7.1 为什么要分类型：识别靠结尾")
            + p(
                "芬兰语动词不能像英语那样「加 -s / -ed」通用处理，因为不同结尾的动词要去掉不同的尾巴。材料的分类标准只有一条：<b>看不定式最后几个字母</b>。"
            )
            + tb(
                ("类型", "不定式结尾", "代表动词"),
                (
                    "第 1 类",
                    "-a / -ä（前面是元音）",
                    "lukea, puhua, sanoa, ostaa, kirjoittaa, kysyä, yrittää, tietää, ymmärtää",
                ),
                (
                    "第 2 类",
                    "-da / -dä",
                    "saada, juoda, tuoda, jäädä, tupakoida, syödä, luoda, imuroida",
                ),
                (
                    "第 3 类",
                    "-la/-lä, -ra/-rä, -na/-nä, -sta/-stä",
                    "olla, tulla, ajatella, kävellä, panna, mennä, surra, nousta, ratkaista, opiskella, kuunnella, pestä",
                ),
                (
                    "第 4 类",
                    "-ata/-ätä（也有 -uta, -ota, -eta, -itä）",
                    "avata, pelata, tavata, luvata, määrätä, kadota, halata, herätä, siivota",
                ),
                (
                    "第 5 类",
                    "-ita/-itä",
                    "tarvita, valita, mainita, häiritä, hallita, merkitä",
                ),
                (
                    "第 6 类",
                    "-eta/-etä（罕用）",
                    "vanheta, kylmetä, paeta, suureta, kyetä",
                ),
            )
            + p(
                "判断时的顺序很重要：先看是不是 <code>-da/-dä</code>（第 2 类），再看是不是 <code>-sta/-stä</code>（第 3 类），然后才看 <code>-ta/-tä</code>（第 4、5、6 类的分界）。因为 <code>nousta</code> 结尾是 -sta，属第 3 类，不能误判成第 4 类。"
            )
            + cal(
                "tip",
                "区分第 4、5、6 类",
                "<code>-ita/-itä</code> 前面通常是单元音 i（tarvita、valita、häiritä）→ 第 5 类；<code>-eta/-etä</code> 表示「变成……」（vanheta、kylmetä、paeta）→ 第 6 类；其余 <code>-ata/-ätä</code>（前面是 a/ä 或辅音）→ 第 4 类。",
            )
            + h3("7.2 词干推导规则")
            + p("材料对每一类都给了「Sääntö」（规则），可以直接抄成操作指令：")
            + tb(
                ("类型", "规则", "例：不定式 → 词干"),
                ("第 1 类", "去掉 -a / -ä", "puhua → puhu；yrittää → yritä"),
                ("第 2 类", "去掉 -da / -dä", "juoda → juo；syödä → syö"),
                (
                    "第 3 类",
                    "去掉 -la/-lä、-ra/-rä、-na/-nä、-sta/-stä，再加 -e",
                    "tulla → tule；mennä → mene；nousta → nouse",
                ),
                (
                    "第 4 类",
                    "去掉 -ta / -tä，再加 -a / -ä",
                    "halata → halaa；herätä → herää；tavata → tapaa",
                ),
                (
                    "第 5 类",
                    "去掉 -a / -ä，再加 -se",
                    "tarvita → tarvitse；valita → valitse",
                ),
                (
                    "第 6 类",
                    "去掉 -ta / -tä，再加 -ne",
                    "vanheta → vanhene；kylmetä → kylmene",
                ),
            )
            + p(
                "第 3 类的「加 -e」是本讲最容易被忽略的一步。以 <code>tulla</code> 为例：去掉 <code>-la</code> 得 <code>tul</code>，加 <code>-e</code> 得 <code>tule-</code>，然后加人称词尾得 <code>tulen, tulet, tulee, tulemme, tulette, tulevat</code>。如果不加 -e，就会写出 <code>tuln</code> 这种不存在的形式。"
            )
            + p(
                "第 4 类的「加 -a/-ä」同样容易漏：<code>halata</code> 去掉 <code>-ta</code> 得 <code>hala</code>，再加 <code>-a</code> 得 <code>halaa-</code>，故 <code>halaan</code>（我拥抱）。只写 <code>halan</code> 是错的。"
            )
            + h3("7.3 六类完整变位表")
            + p(
                "下面这张表把六类的肯定变位放在一起对照。注意每类的第三人称单数形态都不同：第 1、4 类是长元音，第 2 类不加长音，第 3、5、6 类是 <code>-ee</code>。"
            )
            + tb(
                (
                    "人称",
                    "puhua (1)",
                    "juoda (2)",
                    "tulla (3)",
                    "halata (4)",
                    "tarvita (5)",
                    "vanheta (6)",
                ),
                ("minä", "puhun", "juon", "tulen", "halaan", "tarvitsen", "vanhenen"),
                ("sinä", "puhut", "juot", "tulet", "halaat", "tarvitset", "vanhenet"),
                ("hän", "puhuu", "juo", "tulee", "halaa", "tarvitsee", "vanhenee"),
                (
                    "me",
                    "puhumme",
                    "juomme",
                    "tulemme",
                    "halaamme",
                    "tarvitsemme",
                    "vanhenemme",
                ),
                (
                    "te",
                    "puhutte",
                    "juotte",
                    "tulette",
                    "halaatte",
                    "tarvitsette",
                    "vanhenette",
                ),
                (
                    "he",
                    "puhuvat",
                    "juovat",
                    "tulevat",
                    "halaavat",
                    "tarvitsevat",
                    "vanhenevat",
                ),
            )
            + p("再补充材料里给的例词对照，方便按例类推：")
            + tb(
                ("动词", "minä", "hän", "he", "交替"),
                ("ommella (3)", "ompelen", "ompelee", "ompelevat", "ll → l"),
                ("kerrata (4)", "kertaan", "kertaa", "kertaavat", "rr → r"),
                (
                    "yrittää (1)",
                    "yritän",
                    "yrittää",
                    "yrittävät",
                    "tt → t 只在弱级人称",
                ),
                ("nukkua (1)", "nukun", "nukkuu", "nukkuvat", "kk → k 只在弱级人称"),
                ("olla (3)", "olen", "on", "ovat", "不规则，单独记"),
                ("mennä (3)", "menen", "menee", "menevät", "nn → n"),
                ("nousta (3)", "nousen", "nousee", "nousevat", "st → s"),
                ("pestä (3)", "pesen", "pesee", "pesevät", "st → s"),
                ("ajatella (3)", "ajattelen", "ajattelee", "ajattelevat", "tt → t"),
                ("surra (3)", "suren", "suree", "surevat", "rr → r"),
                ("panna (3)", "panen", "panee", "panevat", "nn → n"),
                ("opiskella (3)", "opiskelen", "opiskelee", "opiskelevat", "ll → l"),
                ("kuunnella (3)", "kuuntelen", "kuuntelee", "kuuntelevat", "nn → n"),
                ("tavata (4)", "tapaan", "tapaa", "tapaavat", "v → p"),
                ("luvata (4)", "lupaan", "lupaa", "lupaavat", "v → p"),
                ("kadota (4)", "katoan", "katoaa", "katoavat", "d → t"),
                ("siivota (4)", "siivoan", "siivoaa", "siivoavat", "不交替"),
                ("herätä (4)", "herään", "herää", "heräävät", "t → ∅"),
                ("valita (5)", "valitsen", "valitsee", "valitsevat", "se 词干"),
                ("häiritä (5)", "häiritsen", "häiritsee", "häiritsevät", "se 词干"),
                ("paeta (6)", "pakenen", "pakenee", "pakenevat", "ne 词干"),
                ("kylmetä (6)", "kylmenen", "kylmenee", "kylmenevät", "ne 词干"),
            )
            + h3("7.4 否定式：六类共用一套规则")
            + p(
                "材料把否定式的做法与肯定式并列给出，结论是<b>六类完全一样</b>：<code>ei</code> 的变位形式 + 词干。也就是说，只要词干推对了，否定式不需要额外规则。"
            )
            + tb(
                ("类型", "词干", "否定（minä）", "否定（hän）", "否定（he）"),
                ("1 puhua", "puhu", "en puhu", "ei puhu", "eivät puhu"),
                ("2 juoda", "juo", "en juo", "ei juo", "eivät juo"),
                ("3 tulla", "tule", "en tule", "ei tule", "eivät tule"),
                ("4 halata", "halaa", "en halaa", "ei halaa", "eivät halaa"),
                (
                    "5 tarvita",
                    "tarvitse",
                    "en tarvitse",
                    "ei tarvitse",
                    "eivät tarvitse",
                ),
                ("6 vanheta", "vanhene", "en vanhene", "ei vanhene", "eivät vanhene"),
            )
            + p(
                "否定动词的六个人称：<code>en, et, ei, emme, ette, eivät</code>。这是唯一需要死记的否定词形组，且与第 5 讲一致。"
            )
            + p(
                "材料还特别给了第 4 类的否定示范：<code>halata → halaa</code>，故 <code>en halaa, et halaa, ei halaa, emme halaa, ette halaa, eivät halaa</code>；<code>kerrata → kertaa</code>，故 <code>en kertaa</code> 等。注意这里否定式与第一人称肯定式同形（<code>halaan</code> 与 <code>halaa</code> 只差一个 n），不要混。"
            )
            + h3("7.5 反向交替：第三、四类的特别注意")
            + p(
                "材料在两处加了同一句提醒：<code>Muista käänteinen astevaihtelu! Infinitive is weak (heikko), conjugation strong (vahva)</code>（记得反向交替！不定式与变位的强弱关系与第一类相反）。它的实际含义是：<b>第三、四类的强级出现在不定式本身，变位形式反而取弱级</b>；而第一类恰好相反，强级只留给 hän 与 he。"
            )
            + tb(
                ("类型", "不定式形态", "变位形态（第一 / 第三人称）", "强弱关系"),
                (
                    "第 1 类 nukkua",
                    "nukkua（kk）",
                    "nukun（k）/ nukkuu（kk）",
                    "强级只在 hän/he",
                ),
                (
                    "第 3 类 tulla",
                    "tulla（ll）",
                    "tulen（l）/ tulee（l）",
                    "强级在不定式，变位取弱级",
                ),
                ("第 3 类 nousta", "nousta（st）", "nousen（s）/ nousee（s）", "同上"),
                ("第 3 类 mennä", "mennä（nn）", "menen（n）/ menee（n）", "同上"),
                (
                    "第 4 类 herätä",
                    "herätä（t）",
                    "herään（无 t）/ herää（无 t）",
                    "变位丢失 t，等同弱化",
                ),
                (
                    "第 4 类 tavata",
                    "tavata（v）",
                    "tapaan（p）/ tapaa（p）",
                    "变位反而出现强级 p",
                ),
            )
            + p(
                "为什么会有这种差别？因为第一类的词干在不定式里<b>看不到</b>交替信息（<code>nukkua</code> 的 kk 只在词干内部），要靠人称词尾的音节结构判断强弱；而第三、四类的不定式结尾本身就含交替对（<code>-lla</code>、<code>-sta</code>、<code>-ta</code>），去掉词尾时交替已经发生，变位形式直接继承交替后的结果。"
            )
            + cal(
                "warn",
                "实用建议",
                "不要试图用一条公式推出所有交替。正确做法是：<b>按规则推词干，遇到 K/P/T 就查例词表</b>。材料给的 <code>tulla / ommella / mennä / nousta / pestä / surra / panna / ajatella</code> 八个第三类例子基本覆盖了常见交替。",
            )
            + h3("7.6 高频不规则动词")
            + p("有几组动词形式特殊，必须整块记：")
            + tb(
                ("动词", "含义", "minä", "hän", "he", "说明"),
                ("olla", "是、在", "olen", "on", "ovat", "hän 形式不延长词干元音"),
                ("mennä", "去", "menen", "menee", "menevät", "第三类，nn → n"),
                ("tehdä", "做", "teen", "tekee", "tekevät", "词干 teke-，属第二类变体"),
                ("nähdä", "看见", "näen", "näkee", "näkevät", "hd → k"),
                ("käydä", "去一下、访问", "käyn", "käy", "käyvät", "d → ∅"),
                ("tietää", "知道", "tiedän", "tietää", "tietävät", "第一类，t → d"),
                (
                    "ymmärtää",
                    "理解",
                    "ymmärrän",
                    "ymmärtää",
                    "ymmärtävät",
                    "第一类，rt → rr",
                ),
                (
                    "tupakoida",
                    "吸烟",
                    "tupakoin",
                    "tupakoi",
                    "tupakoivat",
                    "第二类 -oida",
                ),
            )
            + p(
                "特别提醒 <code>olla</code>：<code>hän on</code> 只有一个 o，与其他第一类动词的「双写词干元音」完全不同；<code>he ovat</code> 也不是 <code>ovat</code> 之外的什么形式。这两处是笔试题的高频陷阱。"
            )
            + h3("7.7 分类练习的解题流程")
            + p(
                "材料的配对作业给了一串动词要求归入六类：<code>HÄIRITÄ, HALATA, SYÖDÄ, UNOHTAA, SUURETA, ASUA, NOUSTA, HERÄTÄ, PELATA, TARVITA, TUODA, SANOA, PANNA, TUPAKOIDA, LAKATA, KANTAA, YMMÄRTÄÄ, SURRA, VANHETA, VALITA, VISKATA, OSTAA, KÄVELLÄ, KYETÄ, RAKASTAA, HALLITA, LYÖDÄ, OPISKELLA, JUODA, PAETA, MERKITÄ, PURRA, SIIVOTA, PESTÄ, PUHUA, LUODA</code>。"
            )
            + st(
                "读结尾：-da/-dä → 第 2 类（syödä, tuoda, juoda, lyödä, luoda, tupakoida）",
                "结尾 -sta/-stä → 第 3 类（nousta, pestä）；-la/-lä、-ra/-rä、-na/-nä → 第 3 类（olla 类、surra、purra、panna）",
                "结尾 -ita/-itä → 第 5 类（häiritä, tarvita, valita, hallita, merkitä）",
                "结尾 -eta/-etä → 第 6 类（suureta, vanheta, paeta, kyetä）",
                "其余 -ata/-ätä、-ota、-uta → 第 4 类（halata, herätä, pelata, lakata, viskata, siivota）",
            )
            + p(
                "注意几个容易误判的：<code>unohtaa</code> 结尾是 -aa（第一类）；<code>kantaa</code> 也是第一类；<code>opiskella</code>、<code>kävellä</code> 是第三类；<code>sanoa</code>、<code>asua</code>、<code>ostaa</code>、<code>rakastaa</code>、<code>puhua</code> 是第一类。"
            )
            + cal(
                "warn",
                "高频错误 1",
                "把 <code>tarvita</code> 当第四类：<code>en tarvia</code> 错，应为 <code>en tarvitse</code>。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "第三类忘加 -e：<code>en tul</code>、<code>hän tullee</code> 都错。",
            )
            + cal(
                "tip",
                "考试策略",
                "变位题先写「类型 + 词干」两个标注，再写六个形式。即使某个形式写错，标注正确也能拿到步骤分。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            (
                "verbityyppi",
                "动词类型",
                "Six verb types defined by the infinitive ending.",
            ),
            ("infinitiivi", "不定式", "The dictionary form: puhua, juoda, tulla."),
            ("vartalo", "词干", "The stem that endings are added to."),
            ("-a / -ä", "第一类结尾", "Type 1: drop -a/-ä, e.g. puhua → puhu-."),
            ("-da / -dä", "第二类结尾", "Type 2: drop -da/-dä, e.g. juoda → juo-."),
            (
                "-la / -na / -ra / -sta",
                "第三类结尾",
                "Type 3: drop the ending and add -e, e.g. tulla → tule-.",
            ),
            (
                "-ata / -ätä",
                "第四类结尾",
                "Type 4: drop -ta/-tä and add -a/-ä, e.g. halata → halaa-.",
            ),
            (
                "-ita / -itä",
                "第五类结尾",
                "Type 5: drop -a/-ä and add -se, e.g. tarvita → tarvitse-.",
            ),
            (
                "-eta / -etä",
                "第六类结尾",
                "Type 6: drop -ta/-tä and add -ne, e.g. vanheta → vanhene-.",
            ),
            ("juon", "我喝", "Type 2: juoda → juo- + n."),
            ("tulen", "我来", "Type 3: tulla → tule- + n."),
            ("tarvitsen", "我需要", "Type 5: tarvita → tarvitse- + n."),
            ("vanhenen", "我变老", "Type 6: vanheta → vanhene- + n."),
            (
                "käänteinen astevaihtelu",
                "反向交替",
                "Types 3 and 4: the infinitive carries the strong grade.",
            ),
            (
                "olla → on, ovat",
                "是（第三人称）",
                "Irregular: no lengthened vowel, no -vat.",
            ),
            ("eivät", "他们不", "Negative verb for the 3rd person plural."),
        ),
        examples=(
            qa(
                "例 1　判断并变位：<code>opiskella</code>（学习）属于哪一类？写出六个人称。",
                p(
                    "<b>解：</b>结尾 <code>-lla</code>，属第 3 类。去 <code>-la</code> 加 <code>-e</code> 得词干 <code>opiskele-</code>。六个人称：<code>opiskelen, opiskelet, opiskelee, opiskelemme, opiskelette, opiskelevat</code>。"
                )
                + p(
                    "<b>交替：</b><code>ll → l</code>，所以变位形式只有一个 l，不定式有两个 l。否定：<code>en opiskele</code>。"
                ),
            )
            + qa(
                "例 2　把 <code>tavata</code> 与 <code>herätä</code> 变位，并说明两者交替方向为何不同。",
                p(
                    "<b>解：</b><code>tavata</code>（第 4 类）→ 词干 <code>tapaa-</code>：<code>tapaan, tapaat, tapaa, tapaamme, tapaatte, tapaavat</code>，其中 v → p 是「变位出现强级」。<code>herätä</code>（第 4 类）→ 词干 <code>herää-</code>：<code>herään, heräät, herää, heräämme, heräätte, heräävät</code>，其中 t 完全消失。"
                )
                + p(
                    "<b>说明：</b>同类动词也可能走向不同方向，所以第 4 类的交替必须按词记。材料用 <code>halata → halaan</code>、<code>kerrata → kertaan</code> 两组示范了「丢 t」与「rr → r」两种。"
                ),
            )
            + qa(
                "例 3　判断对错：<code>Hän ei tarvitse</code> 与 <code>Hän ei tarvitsee</code>；<code>He ei opiskele</code>。",
                p(
                    "<b>解：</b>第一组 <code>Hän ei tarvitse</code> 正确，否定式用词干，不加第三人称的元音延长（<code>tarvitsee</code> 是肯定式）。第三句错在 <code>ei</code>：<code>he</code> 对应 <code>eivät</code>，应为 <code>He eivät opiskele</code>。"
                )
                + p(
                    "<b>核心：</b>否定式只有两层结构——否定词负责人称，主动词只负责词干。任何「主动词也变人称」的写法都错。"
                ),
            )
            + qa(
                "例 4　把「我们明天不去学校，我们在家学习」译成芬兰语。",
                p(
                    "<b>解：</b><code>Huomenna me emme mene kouluun, me opiskelemme kotona.</code>"
                )
                + p(
                    "<b>核对：</b><code>mennä</code> 第三类，否定 <code>emme mene</code>；<code>opiskella</code> 第三类，肯定 me 形式 <code>opiskelemme</code>；<code>kouluun</code> 是 illative（去某处）；<code>kotona</code> 是 essive（在家，固定说法）。"
                ),
            )
        ),
        practice=(
            ol(
                "判断类型并写出词干：<code>puhua、juoda、mennä、halata、tarvita、vanheta、nousta、valita、paeta、siivota</code>。",
                "变位 <code>tulla</code>、<code>tarvita</code>、<code>vanheta</code> 的六个人称（肯定与否定各一组）。",
                "改错：<code>Minä tarvia apua.</code> / <code>Hän ei tul.</code> / <code>He ei puhu.</code> / <code>Me opiskellemme.</code>",
                "翻译：「他不会说芬兰语，但他每天都在学。」",
                "从材料配对作业里选 12 个动词，按六类分组（每类至少一个）。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> puhua（1，puhu-）、juoda（2，juo-）、mennä（3，mene-）、halata（4，halaa-）、tarvita（5，tarvitse-）、vanheta（6，vanhene-）、nousta（3，nouse-）、valita（5，valitse-）、paeta（6，pakene-）、siivota（4，siivoa-）。"
                )
                + p(
                    "<b>2.</b> <code>tulla</code>：tulen / tulet / tulee / tulemme / tulette / tulevat；en / et / ei / emme / ette / eivät tule。<code>tarvita</code>：tarvitsen / tarvitset / tarvitsee / tarvitsemme / tarvitsette / tarvitsevat；en tarvitse 等。<code>vanheta</code>：vanhenen / vanhenet / vanhenee / vanhenemme / vanhenette / vanhenevat；en vanhene 等。"
                )
                + p(
                    "<b>3.</b> <code>tarvia</code> → <code>tarvitsen</code>；<code>ei tul</code> → <code>ei tule</code>；<code>He ei puhu</code> → <code>He eivät puhu</code>；<code>opiskellemme</code> → <code>opiskelemme</code>。"
                )
                + p(
                    "<b>4.</b> <code>Hän ei puhu suomea, mutta hän opiskelee sitä joka päivä.</code> 注意 <code>sitä</code> 是 <code>se</code> 的部分格（指代 suomea）。"
                )
                + p(
                    "<b>5.</b> 示例：1 类 puhua、ostaa；2 类 juoda、tuoda；3 类 mennä、nousta；4 类 halata、herätä；5 类 tarvita、valita；6 类 vanheta、paeta。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "六类识别 + 词干推导 + 六人称变位 + 否定式。变位填空（如 <code>PILATA</code>、<code>mennä</code>、<code>ostaa</code>）是本课程最固定的题型。",
            )
            + cal(
                "warn",
                "易错 1",
                "第三类忘加 -e、第四类忘加 -a：<code>en tul</code>、<code>hän hala</code>。",
            )
            + cal(
                "warn",
                "易错 2",
                "把 <code>-sta</code> 结尾的动词判成第四类：<code>nousta</code> 是第三类。",
            )
            + cal(
                "warn",
                "易错 3",
                "<code>olla</code> 的 hän / he 形式：<code>on</code>、<code>ovat</code>，既不延长也不加 -vat。",
            )
            + cal(
                "tip",
                "进阶",
                "能用「不定式结尾本身含交替信息」解释第三、四类为何与第一类方向相反，而不是死记例词。",
            )
        ),
        checklist=(
            h2("六类动词操作清单")
            + h3("判类型三步")
            + st(
                "先查 -da/-dä → 第 2 类",
                "再查 -la/-lä、-ra/-rä、-na/-nä、-sta/-stä → 第 3 类",
                "然后按 -ita（5 类）、-eta（6 类）、-ata（4 类）、其余 -a/-ä（1 类）分流",
            )
            + h3("写形式三步")
            + st(
                "按类型规则得词干（第 3 类加 -e，第 5 类加 -se，第 6 类加 -ne，第 4 类加 -a/-ä）",
                "加人称词尾：n / t / 长元音或 -ee / mme / tte / vat-vät",
                "否定式只留词干，人称交给 en / et / ei / emme / ette / eivät",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "08_Tunti 7/1_verbit + astevaihtelu.docx",
                "全篇",
                "六类定义与规则、第三类加 -e、第四类加 -a、反向交替提醒、LAULAA/ANTAA/SYÖDÄ/LUODA/TULLA/KUUNNELLA/HERÄTÄ/LEIKATA/MAINITA/HÄIRITÄ/KYLMETÄ 练习表",
            ),
            (
                "08_Tunti 7/2_Verbityypit, pos+neg.pdf",
                "p2–p4",
                "六类代表动词、六类肯定与否定完整变位（含 ommella、kerrata、halata、vanheta）",
            ),
            (
                "08_Tunti 7/3_PARITYÖ Mikä verbityyppi_.html",
                "全篇 36 词",
                "分类练习词表与操作指令",
            ),
            (
                "（补充）",
                "7.3、7.6",
                "不规则动词表（olla、tehdä、nähdä、käydä、tietää）为归纳性拓展，原文只在例句中出现",
            ),
            (
                "（跳过）",
                "—",
                "1_verbit 中的手写填空横线为练习版面，答案已在讲义表格中给出",
            ),
        ),
    )
)

LEC.append(
    L(
        slug="t8-food-shopping",
        tzh="第 8 讲 · 食物词汇与购物场景",
        ten="Food Vocabulary and Shopping",
        keywords=[
            "food",
            "groceries",
            "plural partitive",
            "genitive plural",
            "inessive",
            "adessive",
            "quantity",
        ],
        files=[
            "09_Tunti 8/1_Kotitehtävä (Tunti 7) Sanasto/intro/Ruokaostoksilla.docx",
            "09_Tunti 8/3_PUHU PARILLE Ruokaostoksilla.html",
            "09_Tunti 8/4_Ruokasanasto2022.pdf",
            "09_Tunti 8/5_Ruokakuvat.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第八讲是词汇量最大的一讲，也是第一次把「格」放进真实场景里用：在商店里问「鸡蛋在哪」，答句要用内格（<code>kylmäaltaassa</code>）；说「两袋胡萝卜」要用部分格复数（<code>porkkanoita</code>）；说「蔬菜货架」要用属格复数（<code>vihannesten</code>）。"
            )
            + p(
                "它同时为第 9、10 讲的格系统做预备：本讲出现的 <code>kananmunat</code>（主格复数）、<code>porkkanoita</code>（部分格复数）、<code>perunoiden</code>（属格复数）正好是三种复数形式的样本，先见词形，再学规则。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "说出六类以上食物词汇共四十个词，并区分可数名词与不可数名词",
                "在商店里用 <code>Missä teillä on …?</code> 问位置，并听懂 <code>kylmäaltaassa</code>、<code>samassa hyllyssä</code> 这类答句",
                "为可数名词造出主格复数、部分格复数、属格复数三种形式",
                "正确使用 <code>ostoksilla</code>、<code>kaupassa</code>、<code>kassalla</code> 等购物场景固定说法",
                "读懂乳制品包装上的 <code>rasvaton / kevyt / laktoositon</code> 等标记",
            )
        ),
        detail=(
            h3("8.1 食物词汇：按类别记")
            + p(
                "材料的词汇表与厨房图词表加起来约七十个词。按类别分组记忆，比按字母背效率高得多。"
            )
            + tb(
                ("类别", "词汇", "中文"),
                (
                    "水果 hedelmä",
                    "banaani, omena, appelsiini, sitruuna, päärynä, viinirypäle",
                    "香蕉、苹果、橙子、柠檬、梨、葡萄",
                ),
                (
                    "浆果 marja",
                    "mansikka, kirsikka, vadelma, mustikka, puolukka, lakka/hilla",
                    "草莓、樱桃、覆盆子、蓝莓、越橘、云莓",
                ),
                (
                    "蔬菜 kasvis / vihannes",
                    "sipuli, valkosipuli, porkkana, peruna, paprika, tomaatti, kurkku, salaatti",
                    "洋葱、大蒜、胡萝卜、土豆、彩椒、番茄、黄瓜、生菜",
                ),
                (
                    "面包与糕点",
                    "patonki, ruisleipä, vaalea leipä, karjalanpiirakka, sämpylä, pulla, kakku, piirakka, munkki, keksi",
                    "法棍、黑麦面包、白面包、卡累利阿派、小圆面包、甜面包、蛋糕、派、甜甜圈、饼干",
                ),
                (
                    "米面与粥",
                    "puuro, keitto, spagetti/makaroni, riisi, jauho",
                    "粥、汤、意面、米、面粉",
                ),
                (
                    "肉与鱼",
                    "makkara, nakki, naudanliha, sianliha, kana/broileri, kala, jauheliha, kinkku",
                    "香肠、小香肠、牛肉、猪肉、鸡肉、鱼、肉馅、火腿",
                ),
                (
                    "乳制品",
                    "maito, juusto, voi, margariini, jogurtti, rahka, kermavaahto, viili, piimä, kananmuna",
                    "牛奶、奶酪、黄油、人造黄油、酸奶、凝乳、奶油、酸牛奶、酪乳、鸡蛋",
                ),
                (
                    "饮料",
                    "vesi, mehu, kahvi, tee, olut, siideri, limsa, kaakao, punaviini, valkoviini, kivennäisvesi",
                    "水、果汁、咖啡、茶、啤酒、苹果酒、汽水、可可、红葡萄酒、白葡萄酒、矿泉水",
                ),
                (
                    "调味与甜食",
                    "sokeri, suola, pippuri, öljy, ketsuppi, hillo, suklaa, karkki, jäätelö",
                    "糖、盐、胡椒、油、番茄酱、果酱、巧克力、糖果、冰淇淋",
                ),
                (
                    "餐具",
                    "lasi, servetti, lautanen, lusikka, haarukka, veitsi, kuppi, muki, kulho",
                    "杯子、餐巾、盘子、勺子、叉子、刀、茶杯、马克杯、碗",
                ),
                (
                    "厨房",
                    "jääkaappi, kylmäallas, hylly, kassa",
                    "冰箱、冷藏柜、货架、收银台",
                ),
            )
            + p(
                "三个上位词要会区分：<code>hedelmä</code>（水果）、<code>marja</code>（浆果）、<code>kasvis / vihannes</code>（蔬菜）。<code>herkku</code> 是「美味 / 珍馐」，<code>leivonnainen</code> 是「糕点类」，两个词在食品包装上常见。"
            )
            + h3("8.2 可数与不可数：决定用哪种格")
            + p("食物名词分两类，这直接决定「买 / 吃」时用哪种形式：")
            + tb(
                ("类型", "例子", "常见形式"),
                (
                    "可数（能一个个数）",
                    "kananmuna, porkkana, peruna, omena, sämpylä, pizza",
                    "单数主格 / 部分格单数 / 部分格复数：kananmuna, kananmunaa, kananmunia",
                ),
                (
                    "不可数（液体、粉末、糊状）",
                    "vesi, maito, kahvi, tee, riisi, jauho, sokeri, öljy, jäätelö, liha",
                    "通常只用部分格单数：vettä, maitoa, riisiä, jauhoa",
                ),
            )
            + p(
                "所以「我喝水」是 <code>Juon vettä</code>，「我吃一个鸡蛋」是 <code>Syön kananmunan</code>（总格，整颗吃完），「我吃些鸡蛋」是 <code>Syön kananmunia</code>（部分格复数）。这三句的差别正是第 10 讲要展开的「部分格与总格对立」。"
            )
            + h3("8.3 购物对话：逐句拆解")
            + p("材料的购物场景是一段真实对话，每句都有可复用的句型：")
            + tb(
                ("原句", "中文", "语法点"),
                ("Hei anteeksi!", "你好，打扰一下！", "口语招呼 + 礼貌打断"),
                (
                    "Missä teillä on kananmunat?",
                    "你们这儿鸡蛋放在哪？",
                    "<code>teillä</code> 是 <code>te</code> 的 -lla 形式，表「你们店里」；<code>kananmunat</code> 主格复数",
                ),
                (
                    "Ne ovat kylmäaltaassa.",
                    "它们在冷藏柜里。",
                    "<code>ne</code> 指复数物；<code>kylmäallas → kylmäaltaassa</code>（内格，ssa 前有 t→∅ 类变化）",
                ),
                (
                    "Tarvitsetko jotain muuta?",
                    "还需要别的吗？",
                    "<code>tarvita</code> 第五类 + <code>-ko</code>；<code>jotain</code> 部分格",
                ),
                (
                    "Ei mitään, kiitos.",
                    "不用了，谢谢。",
                    "<code>mitään</code> 否定句里的部分格",
                ),
                (
                    "Missä porkkanat ovat?",
                    "胡萝卜在哪？",
                    "复数主语配 <code>ovat</code>",
                ),
                (
                    "Ne ovat samassa hyllyssä.",
                    "在同一个货架上。",
                    "<code>hylly → hyllyssä</code>（内格）",
                ),
                (
                    "Missä jäätelö on?",
                    "冰淇淋在哪？",
                    "不可数名词用单数 <code>on</code>",
                ),
                (
                    "Jäätelö on kylmäaltaassa.",
                    "冰淇淋在冷藏柜里。",
                    "单数主语配 <code>on</code>",
                ),
                (
                    "Kiitos tuhannesti!",
                    "万分感谢！",
                    "<code>tuhannesti</code> 是 <code>tuhat</code> 的副词化形式",
                ),
                ("Mukavaa iltaa!", "晚上愉快！", "祝愿句用部分格 <code>iltaa</code>"),
            )
            + p(
                "这段对话有两个观察值得记住。第一，<b>复数主语用 <code>ovat</code>，单数主语用 <code>on</code></b>，即使问的是「在哪」也一样：<code>Missä kananmunat ovat?</code> / <code>Missä jäätelö on?</code>。第二，<code>teillä</code>（你们这儿）与 <code>minulla</code>（我这儿）同属 -lla 系列，表示「在某人 / 某店这里」，这是第 1 讲存在句的延伸。"
            )
            + h3("8.4 三种复数形式：主格、部分格、属格")
            + p("材料在词表里特意标出了三种复数，用括号提示词形：")
            + tb(
                ("单数", "主格复数", "部分格复数", "属格复数"),
                ("kananmuna", "kananmunat", "kananmunia", "kananmunien"),
                ("porkkana", "porkkanat", "porkkanoita", "porkkanoiden"),
                ("peruna", "perunat", "perunoita", "perunoiden"),
                ("vihannes", "vihannokset", "vihannoksia", "vihannesten"),
                ("omena", "omenat", "omenoita", "omenoiden"),
                ("sämpylä", "sämpylät", "sämpylöitä", "sämpylöiden"),
            )
            + p("三条规律可以先记住：")
            + ol(
                "<b>主格复数</b>：单数词干 + <code>-t</code>（kananmuna → kananmunat）。这是最规则的一种。",
                "<b>部分格复数</b>：以 a/ä 结尾的词常变 <code>-oita/-öitä</code>（porkkana → porkkanoita），以 i 结尾常加 <code>-eja</code>（tuoli → tuoleja），以 o/ö/u/y 结尾常加 <code>-ja/-jä</code>（koulu → kouluja）。",
                "<b>属格复数</b>：常见 <code>-(j)en</code>、<code>-den</code>、<code>-ten</code> 三种（perunoiden、vihannesten、kananmunien）。",
            )
            + p(
                "材料在 Ruokaostoksilla 词表里用括号标注了这些形式，是有意提醒：<b>在商店里说话，最常用的是部分格复数</b>（<code>Ostan porkkanoita</code>），而不是主格复数。主格复数只用于「这些胡萝卜（作为整体主语）」：<code>Porkkanat ovat tuoreita</code>（胡萝卜是新鲜的）。"
            )
            + h3("8.5 购物场景的地点格")
            + p(
                "在店里描述位置，几乎全用内格 -ssa/-ssä，因为商品在容器、柜子、货架「里面」："
            )
            + ul(
                "<code>kaupassa</code> —— 在商店里（<code>kauppa → kaupassa</code>，pp → p）。",
                "<code>kylmäaltaassa</code> —— 在冷藏柜里（<code>kylmäallas → kylmäaltaassa</code>）。",
                "<code>hyllyssä</code> —— 在货架上（<code>hylly → hyllyssä</code>）。",
                "<code>samassa hyllyssä</code> —— 在同一个货架上。",
                "<code>vieressä</code> —— 在旁边（后置词用法，需属格：<code>maidon vieressä</code>）。",
                "<code>kassalla</code> —— 在收银台（<code>kassa</code> 用 -lla，因为「在柜台前」是表面关系）。",
                "<code>täällä</code> —— 在这里（副词）。",
            )
            + p(
                "注意 <code>kassalla</code> 与 <code>kassassa</code> 的差别：前者是「在收银台那儿（结账）」，后者字面是「在收银机里面」，日常只用前者。这类「建筑 / 设施用 -lla」的习惯与第 4 讲的 <code>salilla</code> 一致。"
            )
            + h3("8.6 购物相关动词与短语")
            + tb(
                ("短语", "含义", "说明"),
                (
                    "ruokaostoksilla",
                    "在买食品",
                    "<code>ostoksilla</code> 是复数 adessive，固定说法",
                ),
                (
                    "mennä ostoksille",
                    "去买东西",
                    "-lle 表方向：<code>hän menee ostoksille</code>",
                ),
                (
                    "käydä salilla",
                    "去健身房",
                    "<code>hän käy salilla</code>，注意 <code>käydä</code> 后接 -lla",
                ),
                ("kuitenkin", "然而、还是", "转折副词"),
                ("hänelle", "给他 / 她", "<code>hän</code> 的 -lle 形式"),
                ("vieras", "客人", "名词；也可作形容词「陌生的」"),
                ("tietää", "知道", "<code>hän ei tiedä</code> 否定式"),
                (
                    "missä asiat ovat",
                    "东西在哪里",
                    "<code>asiat</code> 复数主语 + <code>ovat</code>",
                ),
                ("kananmunat", "鸡蛋（复数）", "主格复数"),
                (
                    "vihannes (vihannesten)",
                    "蔬菜（属格复数）",
                    "用于「蔬菜货架」等复合表达",
                ),
                ("vieressä", "在旁边", "需属格修饰：<code>kananmunien vieressä</code>"),
                ("Ei mitään!", "没什么 / 不用谢", "否定句固定答语"),
                ("Tarvitsetko jotain muuta?", "还需要别的吗？", "店员标准问句"),
                ("Kiitos tuhannesti!", "万分感谢", "口语强化感谢"),
                ("Mukavaa iltaa!", "晚上愉快", "告别祝愿"),
            )
            + p(
                "这段词表里还有两个语法点值得单独看：<code>käydä salilla</code> 与 <code>mennä ostoksille</code> 展示了同一动词族的方向对立（-lla 表「在某活动 / 场所」，-lle 表「朝某活动去」）；<code>vieressä</code> 则要求前面的名词用属格，属第 9 讲的后置词搭配。"
            )
            + h3("8.7 乳制品标签与饮食标记")
            + p("材料在乳制品栏给了四个包装常用词，购物时非常实用：")
            + ul(
                "<code>rasvaton</code> —— 脱脂（fat free）。",
                "<code>kevyt</code> —— 低脂（low fat）。",
                "<code>täysmaito</code> —— 全脂奶。",
                "<code>laktoositon</code> —— 无乳糖。",
            )
            + p(
                "第 11 讲还会补充餐厅菜单上的饮食标记 <code>G / VL / L / M / V</code>，本讲先记住这四个乳制品词即可，它们都以 <code>-ton/-tön</code>（「无……」）或形容词形式出现。"
            )
            + h3("8.8 常见错误")
            + cal(
                "warn",
                "高频错误 1",
                "数量后接主格复数：<code>kaksi kananmunat</code> 错，应为 <code>kaksi kananmunaa</code>（2 以上接部分格单数）。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "把不可数名词变复数：<code>maitoja</code> 在商店里几乎不用，说「一些牛奶」是 <code>maitoa</code>。",
            )
            + cal(
                "warn",
                "高频错误 3",
                "<code>Missä kananmunat on?</code> 单复数不一致，应为 <code>ovat</code>。",
            )
            + cal(
                "tip",
                "场景记忆",
                "把这段对话当模板背：问位置 → <code>Missä X on / ovat?</code>；答位置 → <code>X on / ovat + 内格</code>；被问还需什么 → <code>Ei mitään, kiitos</code>。三句就能完成一次购物。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("ruoka", "食物", "Food; partitive ruokaa after eating verbs."),
            (
                "ruokaostoksilla",
                "在买食品",
                "Doing grocery shopping; ostoksilla is a fixed plural adessive.",
            ),
            ("hedelmä", "水果", "Fruit as a category."),
            ("marja", "浆果", "Berry; mansikka, mustikka, vadelma."),
            ("vihannes", "蔬菜", "Vegetable; genitive plural vihannesten."),
            ("maito", "牛奶", "Uncountable: maitoa."),
            ("leipä", "面包", "leipää in the partitive."),
            ("kananmuna", "鸡蛋", "kananmunat (nom. pl.), kananmunia (part. pl.)."),
            ("porkkana", "胡萝卜", "porkkanoita in the partitive plural."),
            ("peruna", "土豆", "perunoiden in the genitive plural."),
            ("jäätelö", "冰淇淋", "jäätelöä, partitive only."),
            ("kylmäallas", "冷藏柜", "kylmäaltaassa = in the cold cabinet."),
            (
                "hylly",
                "货架",
                "hyllyssä (inside the shelf) or hyllyllä (on the shelf).",
            ),
            ("kassa", "收银台", "kassalla = at the checkout."),
            ("ostos", "购物、购买物", "mennä ostoksille = to go shopping."),
            ("laktoositon", "无乳糖", "Lactose free; G, VL, L, M, V are diet labels."),
            ("rasvaton", "脱脂", "Fat free; kevyt = low fat."),
        ),
        examples=(
            qa(
                "例 1　把「我在商店买胡萝卜、土豆和鸡蛋」译成芬兰语，宾语用部分格复数。",
                p(
                    "<b>解：</b><code>Minä ostan kaupassa porkkanoita, perunoita ja kananmunia.</code>"
                )
                + p(
                    "<b>核对：</b>porkkana → porkkanoita（a → oita）；peruna → perunoita；kananmuna → kananmunia（a → ia，因为词干以 n 结尾的复合词按 muna 变化）。三个宾语都是部分格复数，因为买的是「一些」，不是全部库存。"
                ),
            )
            + qa(
                "例 2　回答「Missä juusto on?」，设定奶酪在冷藏柜第二层。",
                p(
                    "<b>解：</b><code>Juusto on kylmäaltaassa.</code> 若要更具体：<code>Juusto on kylmäaltaan toisella hyllyllä.</code>（奶酪在冷藏柜第二层货架上。）"
                )
                + p(
                    "<b>语法点：</b><code>kylmäaltaan</code> 是属格（修饰 hylly），<code>hyllyllä</code> 是 -lla，因为「在某一层货架的表面」用上格；而「在货架内部空间」用 <code>hyllyssä</code>。两种说法都对，取决于把货架看成面还是空间。"
                ),
            )
            + qa(
                "例 3　比较 <code>Ostan kaksi porkkanaa</code> 与 <code>Ostan kaksi porkkanaa ja yhden sipulin</code> 的格。",
                p(
                    "<b>解：</b>两句的 <code>porkkanaa</code> 都是部分格单数，因为数词 2 后面接部分格单数。第二句的 <code>sipulin</code> 是总格（属格形），因为数词 1 后面接主格 / 总格，不用部分格。"
                )
                + p(
                    "<b>规则：</b>1 → 主格（或总格宾语 <code>-n</code>）；2 以上 → 部分格单数；不定量 → 部分格。这是第 10 讲的核心之一。"
                ),
            )
            + qa(
                "例 4　改错：<code>Missä on kananmunat? Ne on kylmäaltaassa.</code>",
                p(
                    "<b>解：</b>两处：<code>kananmunat</code> 是复数，谓语应为 <code>ovat</code>；答句同样。改后：<code>Missä kananmunat ovat? Ne ovat kylmäaltaassa.</code>"
                )
                + p(
                    "<b>延伸：</b>若问单个物品 <code>Missä maito on?</code>，答 <code>Se on kylmäaltaassa</code>（<code>se</code> 指单数物）。代词的数必须跟名词一致。"
                ),
            )
        ),
        practice=(
            ol(
                "把下列食物按「水果 / 蔬菜 / 乳制品 / 肉鱼 / 主食」分类，各写出至少四个芬兰语词。",
                "写出 <code>porkkana</code>、<code>peruna</code>、<code>kananmuna</code>、<code>omena</code> 的主格复数、部分格复数、属格复数。",
                "翻译对话：「打扰一下，牛奶在哪里？」「在冷藏柜里，奶酪旁边。」「谢谢！」",
                "改错：<code>Ostan kolme porkkanat.</code> / <code>Missä jäätelö ovat?</code> / <code>Juon maito.</code>",
                "写一段 5 句的购物清单说明：你要买什么、各买多少、为什么。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> 水果：omena, banaani, appelsiini, päärynä；蔬菜：porkkana, peruna, sipuli, tomaatti；乳制品：maito, juusto, jogurtti, voi；肉鱼：kana, kala, makkara, jauheliha；主食：leipä, riisi, makaroni, puuro。"
                )
                + p(
                    "<b>2.</b> porkkana：porkkanat / porkkanoita / porkkanoiden；peruna：perunat / perunoita / perunoiden；kananmuna：kananmunat / kananmunia / kananmunien；omena：omenat / omenoita / omenoiden。"
                )
                + p(
                    "<b>3.</b> <code>Anteeksi, missä maito on?</code> — <code>Se on kylmäaltaassa, juuston vieressä.</code> — <code>Kiitos!</code> 注意 <code>juuston</code> 属格（后置词 vieressä 要求）。"
                )
                + p(
                    "<b>4.</b> <code>kolme porkkanat</code> → <code>kolme porkkanaa</code>；<code>jäätelö ovat</code> → <code>jäätelö on</code>（不可数）；<code>Juon maito</code> → <code>Juon maitoa</code>。"
                )
                + p(
                    "<b>5.</b> 示例：<code>Minä menen kauppaan. Ostan maitoa, leipää ja kuusi kananmunaa. Ostan myös porkkanoita ja perunoita. En osta karkkia, koska se on kallista. Kaikki maksaa noin kaksikymmentä euroa.</code>"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "食物词汇（尤其乳制品、蔬菜、面包类）、三种复数形式、<code>Missä … on / ovat</code> 的单复数一致、部分格复数的用法。",
            )
            + cal(
                "warn",
                "易错 1",
                "数量后接主格：<code>kaksi omenat</code> 错，应为 <code>kaksi omenaa</code>。",
            )
            + cal(
                "warn",
                "易错 2",
                "不可数名词加复数：<code>maitoja</code>、<code>vesiä</code> 在购物语境下不自然。",
            )
            + cal("warn", "易错 3", "<code>Missä kananmunat on?</code> 单复数不一致。")
            + cal(
                "tip",
                "进阶",
                "能说出 <code>hyllyssä</code> 与 <code>hyllyllä</code> 的语义差别（空间内 vs 表面上），并解释 <code>kassalla</code> 为何用 -lla。",
            )
        ),
        checklist=(
            h2("购物场景清单")
            + h3("问与答")
            + st(
                "问位置：<code>Missä X on?</code>（单数）/ <code>Missä X:t ovat?</code>（复数）",
                "答位置：<code>X on / X:t ovat + 内格</code>（kylmäaltaassa、hyllyssä）",
                "被问还需什么：<code>Ei mitään, kiitos</code> 或 <code>Kyllä, kiitos</code>",
            )
            + h3("数量与格")
            + st(
                "1 个 → 主格 / 总格：yhden sipulin",
                "2 个以上 → 部分格单数：kaksi porkkanaa",
                "不确定多少 → 部分格复数：porkkanoita",
                "不可数 → 部分格单数：maitoa、jauhoa",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "09_Tunti 8/1_Kotitehtävä … Ruokaostoksilla.docx",
                "全篇 26 词条",
                "购物对话关键词：ruokaostoksilla、ostoksille、kuitenkin、vieressä、kylmäallas、kassa、tarvitsetko jotain muuta",
            ),
            (
                "09_Tunti 8/3_PUHU PARILLE Ruokaostoksilla.html",
                "全篇 6 问",
                "对话理解题：Jutta 做什么、东西在哪里、谁帮忙",
            ),
            (
                "09_Tunti 8/4_Ruokasanasto2022.pdf",
                "p1–p4",
                "食物词汇全表：水果、浆果、蔬菜、面包糕点、肉鱼、乳制品及四个乳制品标签、餐具",
            ),
            (
                "09_Tunti 8/5_Ruokakuvat.pdf",
                "p1–p2",
                "厨房与冰箱词表：jääkaappi、kylmäallas 相关词、饮料与调味品",
            ),
            (
                "（补充）",
                "8.4",
                "三种复数的规律化总结属归纳性拓展，原文只以括号形式给出词形",
            ),
            (
                "（跳过）",
                "—",
                "Ruokakuvat 与 Ruokasanasto 的图片本身不含语言点，仅作词汇索引",
            ),
        ),
    )
)

LEC.append(
    L(
        slug="t9-nominative-genitive",
        tzh="第 9 讲 · 格系统与属格",
        ten="The Case System and the Genitive",
        keywords=[
            "case system",
            "nominative",
            "genitive",
            "possessive suffix",
            "genitive plural",
            "colloquial genitive",
            "consonant gradation",
        ],
        files=[
            "10_Tunti 9/2_Nominatiivi, genetiivi ja partitiivi.pdf",
            "10_Tunti 9/3_Genetiivi.pdf",
            "10_Tunti 9/8_KOTITEHTÄVÄ Täydennä genetiivi/intro/Genetiivi.docx",
            "13_Kertaa/1_Kertaus FI2.pdf",
            "13_Kertaa/2_Vastaukset, Kertaus FI2.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第九讲第一次把「格」当成系统讲。前面八讲已经零散用过 -sta、-ssa、-lla、-na、-lta、-hVn，这一讲先用一张总表把它们归位，再把主格与属格讲透——尤其是属格里的<b>辅音交替方向</b>，这是从第 5 讲延续下来的同一套机制。"
            )
            + p(
                "属格之所以重要，是因为它不只表示「谁的」：<code>Annan mies</code>（安娜的丈夫）、<code>suomen tunti</code>（芬兰语课）、<code>kahvin vieressä</code>（咖啡旁边）、<code>elokuvan katsominen</code>（看电影）都是属格。第 6 讲的名词化结构在这里得到解释。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "说出芬兰语主要格的数量与分工，并给每个格一个例词",
                "为主格单数造出属格单数，正确处理元音结尾、辅音结尾与辅音交替三种情况",
                "背出六个人称代词的属格形式，并说出对应的口语缩短形式",
                "为主格单数造出属格复数（-en / -den / -ten 三类）",
                "在正式语体里加所有格后缀（kirjani、kirjasi、kirjamme），并知道口语通常不加",
            )
        ),
        detail=(
            h3("9.1 芬兰语的格：为什么必须系统学")
            + p(
                "材料第一句就给了一个数字：<code>In Finnish language, we have 15 noun cases.</code> 十五个格听起来可怕，但它们的构造高度规则：绝大多数格 = <b>词干 + 格词尾</b>，而词干本身只有强、弱两种形态。"
            )
            + tb(
                ("格", "问什么", "词尾", "例：talo（房子）", "例：kirja（书）"),
                (
                    "nominatiivi 主格",
                    "kuka? mikä?",
                    "—（单数）；-t（复数）",
                    "talo",
                    "kirja",
                ),
                ("genetiivi 属格", "kenen? minkä?", "-n", "talon", "kirjan"),
                (
                    "akkusatiivi 宾格",
                    "kenet? minkä?",
                    "-n（单数同属格）",
                    "talon",
                    "kirjan",
                ),
                (
                    "partitiivi 部分格",
                    "ketä? mitä?",
                    "-a/-ä, -ta/-tä, -tta/-ttä",
                    "taloa",
                    "kirjaa",
                ),
                ("essiivi 样格", "minä?（作为什么）", "-na/-nä", "talona", "kirjana"),
                (
                    "translatiivi 转变格",
                    "miksi?（变成什么）",
                    "-ksi",
                    "taloksi",
                    "kirjaksi",
                ),
                ("inessiivi 内格", "missä?", "-ssa/-ssä", "talossa", "kirjassa"),
                ("elatiivi 出格", "mistä?", "-sta/-stä", "talosta", "kirjasta"),
                ("illatiivi 入格", "mihin?", "-hVn / -Vn", "taloon", "kirjaan"),
                ("adessiivi 上格", "millä?", "-lla/-llä", "talolla", "kirjalla"),
                ("ablatiivi 离格", "miltä?", "-lta/-ltä", "talolta", "kirjalta"),
                ("allatiivi 向格", "mille?", "-lle", "talolle", "kirjalle"),
                ("abessiivi 缺格", "ilman mitä?", "-tta/-ttä", "talotta", "kirjatta"),
                (
                    "komitatiivi 伴随格",
                    "minkä kanssa?",
                    "-ine-（仅复数）",
                    "taloineen",
                    "kirjoineen",
                ),
                (
                    "instruktiivi 工具格",
                    "millä keinolla?",
                    "-in（多复数）",
                    "taloin",
                    "kirjoin",
                ),
            )
            + p(
                "本课程重点在五个格：<b>主格、属格、部分格</b>（本讲与第 10 讲）、<b>内格 / 出格</b>（第 1、8 讲）、<b>上格 / 向格 / 从格</b>（第 2、3、4 讲）。其余格只作识别，不必主动产出。"
            )
            + cal(
                "tip",
                "学习顺序建议",
                "先把「问什么」背熟：missä（在哪）→ -ssa；mistä（从哪）→ -sta；mihin（去哪）→ -hVn；millä（用什么 / 在哪表面）→ -lla；kenen（谁的）→ -n。问题词与词尾一一对应，比背十五个名字有用。",
            )
            + h3("9.2 主格：词典形式与复数 -t")
            + p(
                "主格单数就是词典里的形式：<code>kissa</code>、<code>opiskelija</code>、<code>kirja</code>。主格复数加 <code>-t</code>：<code>kissat</code>、<code>opiskelijat</code>、<code>kirjat</code>。材料指出主格用来回答大部分基本问题："
            )
            + tb(
                ("问句", "答句", "说明"),
                ("Mikä se on?", "Se on kirja.", "问事物用 mikä"),
                ("Kuka asuu täällä?", "Täällä asuu opiskelija.", "问人用 kuka"),
                ("Mitkä nämä ovat?", "Nämä ovat kirjat.", "复数用 mitkä"),
                (
                    "Ketkä asuvat täällä?",
                    "Täällä asuvat opiskelijat.",
                    "复数人称 ketkä",
                ),
            )
            + p(
                "两句答句的语序值得注意：<code>Täällä asuu opiskelija</code> 把地点放句首、动词居中、主语在末——这是芬兰语常见的「存在句」语序，主语是新的信息。若主语是人称代词则语序正常：<code>Hän asuu täällä</code>。"
            )
            + h3("9.3 属格单数的构成")
            + p("属格词尾是 <b>-n</b>，意为「……的」。构成分三种情况：")
            + tb(
                ("情况", "规则", "例子"),
                (
                    "元音结尾",
                    "直接加 -n",
                    "kissa → kissan；Ella → Ellan；tyttö → tytön",
                ),
                (
                    "辅音结尾",
                    "先加 -i-，再加 -n",
                    "Jasmin → Jasminin；Eliot → Eliotin；Oscar → Oscarin",
                ),
                (
                    "含 K/P/T（强弱交替）",
                    "强级词干变弱级，再加 -n",
                    "kukka → kukan；kuppi → kupin；paita → paidan",
                ),
            )
            + p("材料给的交替例子很典型，可以当作一组必背样本：")
            + tb(
                ("主格（强）", "属格（弱）", "交替"),
                ("kukka", "kukan", "kk → k"),
                ("kuppi", "kupin", "pp → p"),
                ("tyttö", "tytön", "tt → t"),
                ("paita", "paidan", "t → d"),
                ("kenkä", "kengän", "nk → ng"),
                ("kampa", "kamman", "mp → mm"),
                ("räntä", "rännän", "nt → nn"),
                ("kerta", "kerran", "rt → rr"),
                ("ilta", "illan", "lt → ll"),
                ("lakka", "lakan", "kk → k"),
                ("hattu", "hatun", "tt → t"),
                ("tauko", "tauon", "k → ∅"),
                ("kipu", "kivun", "p → v"),
            )
            + p(
                "为什么属格一定取弱级？因为属格词尾 <code>-n</code> 是辅音，它把词干最后一个音节「关住」变成闭音节，闭音节要求弱级 —— 这与第 5 讲第一类动词「minä 形式弱化」是同一条机制。<b>属格 = 弱级 + n</b>，这个公式能解释绝大多数名词。"
            )
            + cal(
                "warn",
                "别忘交替",
                "最常见的错误是只加 -n 而不弱化：<code>kukkan</code>、<code>kuppin</code>、<code>paytan</code> 类写法都错。看到词里有 k、p、t 就先问「要不要弱化」。",
            )
            + h3("9.4 人称代词的属格")
            + p("代词属格单独记，因为它们不规则：")
            + tb(
                ("主格", "属格", "中文"),
                ("minä", "minun", "我的"),
                ("sinä", "sinun", "你的"),
                ("hän", "hänen", "他 / 她的"),
                ("me", "meidän", "我们的"),
                ("te", "teidän", "你们的"),
                ("he", "heidän", "他们的"),
            )
            + p(
                "例句：<code>Minun tietokone on uusi.</code>（我的电脑是新的。）<code>Sinun kirja on painava.</code>（你的书很重。）<code>Meidän luokka on kylmä.</code>（我们的教室很冷。）注意属格修饰语<b>不加格变化</b>，格加在被修饰的名词上：<code>minun kirja</code> 作宾语时是 <code>minun kirjan</code>（若用总格）。"
            )
            + p(
                "疑问代词也有属格：<code>kuka → kenen</code>（谁的），<code>mikä → minkä</code>。问句 <code>Kenen tämä koira on?</code>（这只狗是谁的？）答 <code>Se on minun koira.</code>／<code>Se on minun.</code>（省略名词时属格单独作表语）。"
            )
            + h3("9.5 口语形式：mun、sun、meiän")
            + p("材料专门用一页讲口语缩短形式，这在真实对话里极其常见：")
            + tb(
                ("书面", "口语", "例句"),
                ("minun", "mun", "Mun tietokone on uusi."),
                ("sinun", "sun", "Sun kirja on painava."),
                ("meidän", "meiän", "Meiän luokka on kylmä."),
                ("teidän", "teiän", "Teiän auto on hieno."),
                ("hänen", "sen", "Sen kirja on tässä."),
                ("heidän", "heiän / niiden", "Niiden talo on iso."),
            )
            + p(
                "口语里 <code>hän</code> 常说 <code>se</code>，<code>he</code> 常说 <code>ne</code>，所以 <code>sen</code>、<code>niiden</code> 既是代词主格的口语形式，也是属格。考试书面语要写 <code>hänen</code>、<code>heidän</code>，听力里要能听懂 <code>mun</code>、<code>sun</code>。"
            )
            + h3("9.6 正式语体的所有格后缀")
            + p(
                "书面语（尤其正式文本）会在名词上再加一个与 owner 一致的后缀，此时代词可以不写："
            )
            + tb(
                ("人称", "后缀", "例句"),
                ("minä", "-ni", "Minun tietokoneeni on uusi. / Tietokoneeni on uusi."),
                ("sinä", "-si", "Sinun kirjasi on painava. / Kirjasi on painava."),
                ("hän", "-nsa / -nsä", "Hänen kirjansa on uusi."),
                ("me", "-mme", "Meidän luokkamme on kylmä."),
                ("te", "-nne", "Teidän autonne on hieno."),
                ("he", "-nsa / -nsä", "Heidän talonsa on iso."),
            )
            + p(
                "材料给的三个例句正是 <code>Minun tietokoneeni on uusi</code>、<code>Sinun kirjasi on painava</code>、<code>Meidän luokkamme on kylmä</code>。注意加了后缀后，<code>minun</code> 仍可保留（强调），也可省略。"
            )
            + p(
                "口语里几乎不用后缀，所以第 1 讲的口语卡写的是 <code>Minun nimi on …</code> 而不是 <code>Minun nimeni on …</code>。两种都对，语境不同。"
            )
            + h3("9.7 属格复数")
            + p(
                "复数属格有三种常见词尾，材料给的是 <code>-(j)en</code>，并提到 <code>-den</code>："
            )
            + tb(
                ("类型", "词尾", "例子", "适用"),
                (
                    "-(j)en",
                    "-en / -jen",
                    "kirjojen, koirien, opiskelijoiden（按 i 结尾加 -en）",
                    "最常见",
                ),
                (
                    "-den",
                    "-den",
                    "perunoiden, omenoiden, tyttöjen 的变体 tyttöden（少用）",
                    "a/ä 结尾的复数常两可",
                ),
                (
                    "-ten",
                    "-ten",
                    "lasten, vihannesten, miesten",
                    "部分旧词与 -nen 结尾词",
                ),
            )
            + p(
                "三类之间不是随机：以 <code>-nen</code> 结尾的词多用 <code>-sten</code>（nainen → naisten，vihannes → vihannesten）；以 <code>-i</code> 结尾多用 <code>-jen</code>（kirja → kirjojen，koska 复数词干 kirjo- + en）；其余常可用 <code>-den</code> 或 <code>-jen</code>（perunoiden / perunojen 后者少用）。"
            )
            + p(
                "用法：<code>kirjojen hinnat</code>（书的价格）、<code>opiskelijoiden mielipiteet</code>（学生的意见）、<code>lasten vaatteet</code>（儿童服装）。复数属格作前置修饰，被修饰名词用主格或按句法变格。"
            )
            + h3("9.8 属格的四种典型用法")
            + ol(
                "<b>表示拥有</b>：<code>Tämä salkku on Timon.</code>（这个公文包是蒂莫的。）",
                "<b>作前置修饰（谁的 / 什么的）</b>：<code>Annan mies</code>（安娜的丈夫）、<code>meidän ystävä</code>（我们的朋友）、<code>suomen tunti</code>（芬兰语课）、<code>talon katto</code>（房子的屋顶）。",
                "<b>作后置词的宾语</b>：<code>kahvin vieressä</code>（咖啡旁边）、<code>pöydän alla</code>（桌子下面）、<code>sinun kanssa</code>（和你一起）。",
                "<b>作动作名词的对象</b>：<code>elokuvan katsominen</code>（看电影）、<code>musiikin kuuntelu</code>（听音乐）—— 第 6 讲的结构在这里得到解释。",
            )
            + p(
                "注意属格修饰语本身不变格，变化落在中心词上：<code>Annan miehen</code>（安娜的丈夫，作宾语）、<code>Annan miehelle</code>（给安娜的丈夫）。这条「前修饰语不变、中心词变格」的规则在第 4 讲的 <code>ensi viikolla</code> 已经出现过。"
            )
            + h3("9.9 常见错误")
            + cal(
                "warn",
                "高频错误 1",
                "忘掉辅音交替：<code>kukkan</code>、<code>kuppin</code>。属格必须弱化。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "辅音结尾的名字不加 -i-：<code>Oscarn</code> 错，应为 <code>Oscarin</code>；<code>Jasminn</code> 错，应为 <code>Jasminin</code>。",
            )
            + cal(
                "warn",
                "高频错误 3",
                "把口语形式写进正式作文：<code>mun kirja</code> 在考试作文里应写 <code>minun kirjani</code> 或 <code>minun kirja</code>。",
            )
            + cal(
                "tip",
                "自检口诀",
                "写属格前问三句：① 词尾是元音还是辅音？② 词里有没有 k/p/t？③ 有没有 -nen 结尾（→ -sen）？三问过完再落笔。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("sijamuoto", "格", "Case; Finnish has 15 noun cases."),
            ("nominatiivi", "主格", "Dictionary form; plural adds -t."),
            ("genetiivi", "属格", "Possession; ending -n: kissan, Annan."),
            ("partitiivi", "部分格", "Partial quantity; -a/-ä, -ta/-tä, -tta/-ttä."),
            ("inessiivi", "内格", "-ssa/-ssä: talossa, Lahdessa."),
            ("elatiivi", "出格", "-sta/-stä: talosta, Suomesta."),
            ("illatiivi", "入格", "-hVn: taloon, kauppaan, kotiin."),
            ("adessiivi", "上格", "-lla/-llä: talolla, salilla."),
            ("allatiivi", "向格", "-lle: talolle, salille."),
            ("essiivi", "样格", "-na/-nä: lapsena, maanantaina."),
            ("translatiivi", "转变格", "-ksi: aamiaiseksi, taloksi."),
            ("kenen?", "谁的？", "Genitive question word: Kenen tämä koira on?"),
            (
                "minun, sinun, hänen",
                "我的、你的、他/她的",
                "Genitive forms of the personal pronouns.",
            ),
            (
                "mun, sun, meiän",
                "我的、你的、我们的（口语）",
                "Colloquial genitive forms.",
            ),
            ("kirjojen", "书的（属格复数）", "Genitive plural in -(j)en."),
            ("kirjani", "我的书", "Possessive suffix -ni in formal written Finnish."),
            (
                "naisen",
                "女人的（属格）",
                "-nen words use the -se- stem: nainen → naisen.",
            ),
        ),
        examples=(
            qa(
                "例 1　写出 <code>kissa、kuppi、paita、kenkä、ilta</code> 的属格，并标明交替。",
                p(
                    "<b>解：</b>kissa → <code>kissan</code>（无交替）；kuppi → <code>kupin</code>（pp → p）；paita → <code>paidan</code>（t → d）；kenkä → <code>kengän</code>（nk → ng）；ilta → <code>illan</code>（lt → ll）。"
                )
                + p(
                    "<b>思路：</b>先看有无 k/p/t，有就取弱级词干，再加 -n。无交替时直接加 -n。"
                ),
            )
            + qa(
                "例 2　把「蒂莫的公文包是新的，安娜的书很重」译成芬兰语。",
                p(
                    "<b>解：</b><code>Timon salkku on uusi.</code> / <code>Annan kirja on painava.</code>"
                )
                + p(
                    "<b>要点：</b><code>Timo → Timon</code>（元音结尾直接加 n）；<code>Anna → Annan</code>。属格修饰语在前，中心词 <code>salkku</code>、<code>kirja</code> 用主格作主语。"
                ),
            )
            + qa(
                "例 3　把「学生们对书的价格有意见」改写成一句芬兰语，需用属格复数。",
                p(
                    "<b>解：</b><code>Opiskelijoilla on mielipide kirjojen hinnoista.</code>"
                )
                + p(
                    "<b>拆解：</b><code>opiskelijoilla</code>（学生，-lla 表「有」的主语）＋ <code>on</code> ＋ <code>mielipide</code>（意见）＋ <code>kirjojen</code>（书的，属格复数）＋ <code>hinnoista</code>（关于价格，出格）。整句结构是 <code>X:llä on mielipide Y:stä</code>。"
                ),
            )
            + qa(
                "例 4　改错：<code>Minun ystävä on kotoisin Saksasta.</code> 在正式书面语中应如何写？口语中呢？",
                p(
                    "<b>解：</b>正式：<code>Minun ystäväni on kotoisin Saksasta.</code> 或省略代词 <code>Ystäväni on kotoisin Saksasta.</code> 口语：<code>Mun ystävä on kotoisin Saksasta.</code>"
                )
                + p(
                    "<b>说明：</b>原句在口语里可以接受，但正式文本应加 <code>-ni</code>。这是「同一句话两套语体」的典型例子，考试按文体要求选择。"
                ),
            )
        ),
        practice=(
            ol(
                "写出下列词的属格：<code>kukka、hattu、tauko、kipu、kampa、räntä、kerta、Jasmin、Oscar、Martin</code>。",
                "写出六个人称代词的属格，并各造一句 <code>… on uusi / painava / kylmä</code> 的判断句。",
                "把下列短语译成芬兰语：安娜的丈夫、我们的老师、芬兰语课、咖啡旁边、学生的意见（属格复数）。",
                "给 <code>kirja、koira、opiskelija、nainen、peruna</code> 造属格复数。",
                "改错：<code>kukkan on kaunis</code> / <code>Oscarn kirja</code> / <code>minun kirja</code>（正式语体）",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> kukan（kk→k）、hatun（tt→t）、tauon（k→∅）、kivun（p→v）、kamman（mp→mm）、rännän（nt→nn）、kerran（rt→rr）、Jasminin（加 i）、Oscarin（加 i）、Martinin（加 i）。"
                )
                + p(
                    "<b>2.</b> minun / sinun / hänen / meidän / teidän / heidän。例句：<code>Minun puhelin on uusi.</code> / <code>Sinun laukku on painava.</code> / <code>Meidän luokka on kylmä.</code>"
                )
                + p(
                    "<b>3.</b> <code>Annan mies</code> / <code>meidän opettaja</code> / <code>suomen tunti</code> / <code>kahvin vieressä</code> / <code>opiskelijoiden mielipide</code>。"
                )
                + p(
                    "<b>4.</b> <code>kirjojen</code>、<code>koirien</code>、<code>opiskelijoiden</code>、<code>naisten</code>（-nen → -sten）、<code>perunoiden</code>。"
                )
                + p(
                    "<b>5.</b> <code>kukka on kaunis</code> → <code>kukan</code> 需弱化：<code>kukan on kaunis</code> 仍不完整，正确句如 <code>Kukan väri on kaunis</code>；<code>Oscarn</code> → <code>Oscarin</code>；<code>minun kirja</code> → <code>minun kirjani</code>。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "属格单数的三种情况（元音、辅音 + i、辅音交替）、六个人称代词属格、属格复数的三种词尾、<code>Kenen?</code> 问答。",
            )
            + cal(
                "warn",
                "易错 1",
                "属格忘弱化：<code>kukkan</code>、<code>kuppin</code>。",
            )
            + cal(
                "warn",
                "易错 2",
                "辅音结尾名字不加 -i-：<code>Oscarn</code>、<code>Jasminn</code>。",
            )
            + cal(
                "warn",
                "易错 3",
                "口语与书面语混用：作文里出现 <code>mun</code>、<code>sen</code>。",
            )
            + cal(
                "tip",
                "进阶",
                "能用「闭音节 → 弱级」解释属格为何弱化，并把它与第一类动词 minä 形式的弱化联系起来。",
            )
        ),
        checklist=(
            h2("属格操作清单")
            + h3("写属格单数四步")
            + st(
                "看词尾：元音结尾直接加 -n；辅音结尾先加 -i- 再加 -n",
                "看词内是否有 k/p/t，有则取弱级词干",
                "看是否 -nen 结尾：→ -sen（nainen → naisen）",
                "落笔后回读一遍，确认没有多写辅音",
            )
            + h3("写属格复数三步")
            + st(
                "-nen 结尾 → -sten（naisten、vihannesten）",
                "i 结尾 → -jen（kirjojen、koirien）",
                "其余 → -den 或 -jen（perunoiden、opiskelijoiden）",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "10_Tunti 9/2_Nominatiivi, genetiivi ja partitiivi.pdf",
                "p2–p6",
                "三格定义、主格单复数与四个基本问句、属格 -n 与复数 -(j)en、部分格用法预览、12 词三格对照表、代词三格表",
            ),
            (
                "10_Tunti 9/3_Genetiivi.pdf",
                "p2–p6",
                "15 格说明、属格三种构成、辅音交替例词、代词属格、口语形式 mun/sun/meiän、所有格后缀",
            ),
            (
                "10_Tunti 9/8_KOTITEHTÄVÄ … Genetiivi.docx",
                "全篇 11 行",
                "属格填空练习：minä、Jessica、hän、Paavo、te、sinä、Artur、he、me、koira、kuka",
            ),
            (
                "13_Kertaa/1_Kertaus FI2.pdf",
                "p3",
                "属格与部分格混合复习：minä、hän、kahvi、tyttö、Jemina、Oscar",
            ),
            (
                "13_Kertaa/2_Vastaukset, Kertaus FI2.pdf",
                "p3",
                "属格答案：hänen、kahvin、tytön、Jeminan、Oscarin 及例句",
            ),
            (
                "（补充）",
                "9.1、9.7",
                "15 格总表与属格复数三类词尾的归纳属拓展，原文只提到 15 个格与 -(j)en",
            ),
            ("（跳过）", "—", "练习表格中的空行为作答版面"),
        ),
    )
)

LEC.append(
    L(
        slug="t10-partitive",
        tzh="第 10 讲 · 部分格的构成与用法",
        ten="The Partitive: Formation and Use",
        keywords=[
            "partitive",
            "partitive singular",
            "partitive plural",
            "object case",
            "negative sentence",
            "number + partitive",
            "uncountable noun",
        ],
        files=[
            "10_Tunti 9/2_Nominatiivi, genetiivi ja partitiivi.pdf",
            "10_Tunti 9/4_KATSO videot Partitiivi.html",
            "10_Tunti 9/5_RuokaaJuomaa.pdf",
            "10_Tunti 9/6_Puhu parille Mitä syöt_ (partitiivi).html",
            "10_Tunti 9/7_Partitiivin muodostus.docx",
            "13_Kertaa/5_PartitiiviLauseita.docx",
            "13_Kertaa/6_PartitiiviLauseitaVASTAUKSET.docx",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第十讲是全课程语法上最重要的一讲。部分格（partitiivi）在前面九讲里已经反复出现：<code>vuotta</code>（年龄）、<code>vettä</code>（喝水）、<code>tanssia</code>（爱好）、<code>porkkanoita</code>（买胡萝卜）、<code>ei ole kissaa</code>（没有猫）。这一讲把这些散点收成一套完整规则。"
            )
            + p(
                "它也是芬兰语区别于其他欧洲语言最明显的地方：<b>宾语不只有一种形式</b>。同一个动作，做完与没做完，宾语要用不同的格（<code>katson elokuvan</code> / <code>katson elokuvaa</code>）。这一点直接决定句子的意思，不只是「语法细节」。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "按五条主规则为任意单数名词造出部分格，并处理 -nen、vesi、pieni 等特殊词",
                "按三条规律为常见名词造出部分格复数",
                "说出部分格五大用法：数词后、否定句、部分格动词后、monta 后、不可数名词",
                "区分「部分格宾语」与「总格宾语」在意义上的差别，并按语境选择",
                "把一个打乱的词串组成正确的芬兰语部分格句（考试固定题型）",
            )
        ),
        detail=(
            h3("10.1 部分格到底表示什么")
            + p(
                "材料用一句话概括：<code>Partitive case has a meaning 「part of」 something</code>，例 <code>（osa） leipää</code> = 一块 / 一些面包。所以部分格的核心语义是「一部分、不定量、未完成」。"
            )
            + p("由此推出两条使用逻辑：")
            + ol(
                "<b>量上的一部分</b>：一块面包、一些水、两个鸡蛋 —— 都不是「全部」。",
                "<b>动作上未完成</b>：正在看、看着、看了一会儿 —— 动作没有走到终点。",
            )
            + p(
                "这两条逻辑覆盖了本讲所有用法。凡是句子里出现「不确定多少」或「没做完」，宾语几乎都用部分格。"
            )
            + h3("10.2 部分格单数：五条主规则")
            + p(
                "材料把构成规则按词尾分成五组，逐组给了大量填空例词。下面把规则与例词一并列出（例词即练习题的标准答案）："
            )
            + tb(
                ("规则", "条件", "例词 → 部分格", "说明"),
                (
                    "规则一",
                    "词尾是元音（e 除外）",
                    "kynä → kynää；auto → autoa；läppäri → läppäriä；kirja → kirjaa；kinkku → kinkkua；ruoka → ruokaa；maito → maitoa；leipä → leipää；pizza → pizzaa；jäätelö → jäätelöä；raha → rahaa",
                    "直接加 -a / -ä；注意元音和谐",
                ),
                (
                    "规则二",
                    "词尾是 e",
                    "vene → venettä；tietokone → tietokonetta；huone → huonetta；vaate → vaatetta；perhe → perhettä",
                    "加 -tta / -ttä",
                ),
                (
                    "规则三",
                    "词尾是 i",
                    "bussi → bussia；pankki → pankkia；lasi → lasia；äiti → äitiä；lehti → lehteä；lahti → lahtea；poski → poskea；järvi → järveä",
                    "一般加 -a/-ä；部分词 i → e 再加 -a/-ä",
                ),
                (
                    "规则四",
                    "词尾是辅音",
                    "avain → avainta；puhelin → puhelinta；tulostin → tulostinta；lounas → lounasta；sormus → sormusta；pakastin → pakastinta；selain → selainta",
                    "加 -ta / -tä",
                ),
                (
                    "规则五",
                    "短词（单音节）",
                    "maa → maata；tee → teetä；yö → yötä；työ → työtä",
                    "加 -ta / -tä，避免出现三个相同元音",
                ),
            )
            + p(
                "规则三的 i → e 需要单独注意：<code>lehti → lehteä</code>、<code>järvi → järveä</code>、<code>lahti → lahtea</code>、<code>poski → poskea</code>。判据不完全可推，但有一条经验：<b>i 前面的音节含 a、e、ä 等前元音时更容易变成 e</b>；<code>bussi</code>、<code>pankki</code>、<code>lasi</code> 这类则保留 i。"
            )
            + p(
                "规则五的存在是为了避免三个相同元音连排：<code>maa + a</code> 若写成 <code>maaa</code> 不可读，所以改用 <code>-ta</code> 得 <code>maata</code>。同理 <code>tee → teetä</code>、<code>yö → yötä</code>。"
            )
            + h3("10.3 特殊词尾与例外")
            + p("材料专门列了「Erikoiset tapaukset」（特殊情况），这些必须整块记：")
            + tb(
                ("类型", "例词 → 部分格", "说明"),
                (
                    "-nen 结尾",
                    "punainen → punaista；nainen → naista；sininen → sinistä；virolainen → virolaista",
                    "-nen 变 -sta / -stä",
                ),
                (
                    "-si 结尾的旧词",
                    "vesi → vettä；vuosi → vuotta；kuusi（六）→ kuutta；kuukausi → kuukautta",
                    "去掉 -si，按词干加 -ta/-ttä",
                ),
                (
                    "i 脱落",
                    "pieni → pientä；suuri → suurta；kuori → kuorta",
                    "i 去掉后加 -ta/-tä",
                ),
                (
                    "人名",
                    "David → Davidia；Hamad → Hamadia；Susan → Susania；Alex → Alexia；Mirjam → Mirjamia；Martin → Martinia；Marjut → Marjutia",
                    "辅音结尾的人名先加 -i- 再加 -a/-ä",
                ),
            )
            + p(
                "-nen 结尾的规律与第 9 讲属格一致：<code>-nen</code> 的词在变格时整体换成 <code>-se-</code> 词干（nainen → naise-），部分格就是 <code>naista</code>，属格是 <code>naisen</code>。记住「-nen → -se-」这一个动作，两类格都能推。"
            )
            + p(
                "人名规则值得单拎出来：<code>David</code> 结尾是辅音 d，直接加 -a 会得到不可读的 <code>Davida</code>？实际上芬兰语的处理是<b>先加 i</b>：<code>Davidia</code>、<code>Hamadia</code>、<code>Susania</code>。这与第 9 讲属格「辅音结尾加 i 再加 n」是同一个思路。"
            )
            + h3("10.4 部分格复数：三条主要规律")
            + p("材料给出的是三条最常用规律，并强调「由主格结尾决定」：")
            + tb(
                ("主格词尾", "部分格复数词尾", "例词"),
                (
                    "o, ö, u, y",
                    "-ja / -jä",
                    "koulu → kouluja；työ → töitä（例外，见下）；halo → haloja",
                ),
                (
                    "i",
                    "-eja / -ejä",
                    "tuoli → tuoleja；bussi → busseja；pankki → pankkeja",
                ),
                (
                    "a, i, in",
                    "-ia / -iä",
                    "koira → koiria；kirja → kirjoja（a → o + ja）；kissa → kissoja",
                ),
                ("e", "-ita / -itä", "huone → huoneita；vaate → vaatteita"),
                ("-nen", "-sia / -siä", "nainen → naisia；punainen → punaisia"),
            )
            + p(
                "材料原文只给了前三行（o/ö/u/y → -ja；i → -eja；a/i/in → -ia），后两行是同类词的类推结果，用来补齐实际会遇到的 <code>huoneita</code>、<code>naisia</code>。"
            )
            + p(
                "注意 <code>a → o + ja</code> 这一小步：<code>kirja → kirjoja</code>、<code>kissa → kissoja</code>、<code>koira → koiria</code>（这里 a 直接变 i + a）。同样是 a 结尾，词干不同结果不同，所以复数部分格也要按词记，遇到新词先查再写。"
            )
            + h3("10.5 部分格的五大用法")
            + p("材料列出的用法条目是这一讲最该背下来的清单，每条都配了例句：")
            + tb(
                ("用法", "例句", "说明"),
                (
                    "① 数词 + 具体名词",
                    "kaksi koiraa；kolme munaa；kaksi porkkanaa",
                    "2 以上接部分格<b>单数</b>，不是复数",
                ),
                (
                    "② 否定动词 + 具体名词",
                    "Minulla ei ole koiraa.；Tarja ei osta tietokonetta.",
                    "否定句宾语一律部分格",
                ),
                (
                    "③ 部分格动词",
                    "Rakastan sinua.；Katson koiraa.；Etsin opettajaa.",
                    "这类动词的宾语习惯用部分格",
                ),
                ("④ monta（许多）", "Monta koiraa.", "monta 后面接部分格单数"),
                (
                    "⑤ 不可数名词",
                    "Juon vettä.；Haluan teetä.",
                    "液体、粉末、物质用部分格",
                ),
            )
            + p(
                "第 ③ 条需要一份动词清单，材料在复习题里给了足够的样本：<code>auttaa</code>（帮助）、<code>rakastaa</code>（爱）、<code>etsiä</code>（找）、<code>katsoa</code>（看）、<code>odottaa</code>（等）、<code>kuunnella</code>（听）、<code>lukea</code>（读）、<code>pelata</code>（玩）、<code>ostaa</code>（买，否定时）、<code>syödä</code>（吃，部分时）。这些动词的共同点是：动作可以「没完」，或对象本身是「一部分」。"
            )
            + p(
                "第 ② 条的否定规则要连带注意主语：<code>Minulla ei ole koiraa</code> 里 <code>minulla</code> 不变，只有宾语变。而 <code>Tarja ei osta tietokonetta</code> 里 <code>tietokone → tietokonetta</code>，是 e 结尾加 -tta 的规则二。"
            )
            + h3("10.6 部分格宾语与总格宾语的对立")
            + p(
                "这是芬兰语语法的核心机制，也是材料没有明说但反复示范的差别。看两组对照："
            )
            + tb(
                ("句子", "含义", "宾语的格"),
                ("Katson elokuvan.", "我要看完这部电影（整部）。", "总格 -n"),
                ("Katson elokuvaa.", "我正在看电影（没看完）。", "部分格 -a"),
                ("Ostan leivän.", "我买（一整个）面包。", "总格 -n"),
                ("Ostan leipää.", "我买些面包。", "部分格 -a"),
                ("Syön omenan.", "我把一个苹果吃掉。", "总格 -n"),
                ("Syön omenaa.", "我在吃苹果（吃着一部分）。", "部分格 -a"),
                ("Juon maidon.", "我把（那杯）牛奶喝完。", "总格 -n"),
                ("Juon maitoa.", "我喝（一些）牛奶。", "部分格 -a"),
            )
            + p(
                "判断口诀：<b>结果完整 → 总格；过程未完 / 数量不定 → 部分格</b>。此外三种情况<b>永远</b>用部分格：否定句、数词 2 以上、不可数名词。这三条是硬规则，不需要判断语感。"
            )
            + cal(
                "warn",
                "最容易被扣分的地方",
                "把「我喝牛奶」写成 <code>Juon maidon</code>。牛奶不可数，必须是 <code>Juon maitoa</code>。同理 <code>Syön leipää</code>（吃面包）比 <code>Syön leivän</code>（吃掉一整个）更常用于日常描述。",
            )
            + h3("10.7 造句练习：语序不变、动词变位、宾语部分格")
            + p(
                "材料的复习题给了 11 组词，要求「用语序不变、动词变位、宾语用部分格」造出句子。这正好是考试题型，下面给出全部标准答案并标注操作步骤："
            )
            + tb(
                ("给定词", "标准答案", "关键操作"),
                (
                    "Minä – auttaa – naapuri",
                    "Minä autan naapuria.",
                    "auttaa 第一类，naapuri → naapuria",
                ),
                (
                    "Sinä – syödä – kana – ja – riisi",
                    "Sinä syöt kanaa ja riisiä.",
                    "syödä 第二类；两个宾语都部分格",
                ),
                (
                    "Juoda – sinä – olut?",
                    "Juotko sinä olutta?",
                    "疑问句动词加 -ko，olut → olutta",
                ),
                (
                    "He – rakastaa – jäätelö",
                    "He rakastavat jäätelöä.",
                    "rakastaa 第一类，he → -vat",
                ),
                (
                    "Sanna – etsiä – avain",
                    "Sanna etsii avainta.",
                    "etsiä 第一类，avain → avainta",
                ),
                (
                    "Tarja – ei ostaa – tietokone",
                    "Tarja ei osta tietokonetta.",
                    "否定式 + e 结尾 -tta",
                ),
                (
                    "Te – katsoa – puhelin",
                    "Te katsotte puhelinta.",
                    "katsoa 第一类，puhelin → puhelinta",
                ),
                (
                    "Me – odottaa – bussi",
                    "Me odotamme bussia.",
                    "odottaa 第一类，bussi → bussia",
                ),
                (
                    "Minä – ei kuunnella – musiikki",
                    "Minä en kuuntele musiikkia.",
                    "kuunnella 第三类，musiikki → musiikkia",
                ),
                (
                    "Te – lukea – lehti",
                    "Te luette lehteä.",
                    "lukea 第一类，lehti → lehteä（i → e）",
                ),
                (
                    "He – ei pelata – jalkapallo",
                    "He eivät pelaa jalkapalloa.",
                    "pelata 第四类，否定 eivät pelaa",
                ),
            )
            + p(
                "最后一行值得单独说明：<code>pelata</code> 属第四类，词干 <code>pelaa-</code>，否定式是 <code>eivät pelaa</code>（不是 <code>pelata</code>）。<code>jalkapallo → jalkapalloa</code> 是 o 结尾加 -a。"
            )
            + st(
                "读词串，找出主语 → 定动词 → 判动词类型 → 变位",
                "找出宾语，按规则造部分格（元音 / e / i / 辅音 / 短词）",
                "检查是否否定句或数词，若是则确认部分格",
                "检查语序与原文一致，疑问句记得给动词加 -ko/-kö",
            )
            + h3("10.8 常见错误汇总")
            + cal(
                "warn",
                "高频错误 1",
                "数词后接主格：<code>kolme muna</code> 错，应为 <code>kolme munaa</code>。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "e 结尾忘加 -tta：<code>huonea</code> 错，应为 <code>huonetta</code>。",
            )
            + cal(
                "warn",
                "高频错误 3",
                "-nen 结尾按普通词处理：<code>naista</code> 对，<code>naisena</code> 式的类推错；<code>punainen → punaista</code>。",
            )
            + cal(
                "warn",
                "高频错误 4",
                "不可数名词用总格：<code>Juon maidon</code>、<code>Ostan leivän</code>（若只想说「买些面包」）。",
            )
            + cal(
                "tip",
                "终极自检",
                "写完宾语问一句：这个动作「做完了吗」「数量确定吗」。两个都是「是」才用总格，否则用部分格。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("partitiivi", "部分格", "The case of partial or indefinite quantity."),
            ("osa", "部分", "osa leipää = a piece of bread."),
            ("kaksi koiraa", "两只狗", "Numbers 2+ take the partitive singular."),
            (
                "ei ole koiraa",
                "没有狗",
                "A negative sentence always takes the partitive object.",
            ),
            (
                "Juon vettä",
                "我喝水",
                "Uncountable nouns stay in the partitive singular.",
            ),
            ("monta", "许多", "monta koiraa — partitive singular after monta."),
            ("huonetta", "房间（部分格）", "Words ending in -e take -tta/-ttä."),
            ("avainta", "钥匙（部分格）", "Words ending in a consonant take -ta/-tä."),
            ("naista", "女人（部分格）", "-nen words take -sta/-stä."),
            ("vettä", "水（部分格）", "Irregular: vesi → vettä."),
            ("pientä", "小的（部分格）", "The i drops: pieni → pientä."),
            (
                "porkkanoita",
                "胡萝卜（部分格复数）",
                "a → oita in the partitive plural.",
            ),
            ("tuoleja", "椅子（部分格复数）", "i → eja in the partitive plural."),
            ("koiria", "狗（部分格复数）", "a → ia in the partitive plural."),
            (
                "katsomista",
                "看（动名词部分格）",
                "-minen becomes -mista when it is an object.",
            ),
            (
                "kokonaisobjekti",
                "总格宾语",
                "Total object -n: Katson elokuvan = I watch the whole film.",
            ),
        ),
        examples=(
            qa(
                "例 1　给 <code>huone、avain、vesi、punainen、pieni</code> 造部分格，并说明各自适用哪条规则。",
                p(
                    "<b>解：</b>huone → <code>huonetta</code>（规则二：e 结尾加 -tta）；avain → <code>avainta</code>（规则四：辅音结尾加 -ta）；vesi → <code>vettä</code>（特殊：-si 去掉，双写 t）；punainen → <code>punaista</code>（-nen → -sta）；pieni → <code>pientä</code>（i 脱落加 -tä）。"
                )
                + p(
                    "<b>思路：</b>先看词尾类别，再查特殊表。<code>vesi</code> 与 <code>pieni</code> 不属五条主规则，必须靠记忆表。"
                ),
            )
            + qa(
                "例 2　把「我买了三个鸡蛋和两袋牛奶」译成芬兰语。",
                p(
                    "<b>解：</b><code>Ostin kolme munaa ja kaksi maitoa.</code> 若用现在时：<code>Ostan kolme munaa ja kaksi maitoa.</code>"
                )
                + p(
                    "<b>要点：</b>数词 3 与 2 后面都接部分格单数（munaa、maitoa）。<code>maito</code> 本身不可数，部分格 <code>maitoa</code> 兼有「一些牛奶」的意思。"
                ),
            )
            + qa(
                "例 3　比较 <code>Luen kirjaa</code> 与 <code>Luen kirjan</code>，说明语境差别。",
                p(
                    "<b>解：</b><code>Luen kirjaa</code> = 我在读一本书（读着，没读完）；<code>Luen kirjan</code> = 我把这本书读完（读完或承诺读完）。"
                )
                + p(
                    "<b>语法：</b>前者部分格宾语，后者总格宾语。回答「你在做什么」用前者；回答「你今天要完成什么」用后者。"
                ),
            )
            + qa(
                "例 4　改错：<code>Minä en osta tietokone.</code> / <code>Syön kaksi omenat.</code> / <code>Juon vesi.</code>",
                p(
                    "<b>解：</b>三处都要部分格：<code>Minä en osta tietokonetta.</code>（否定）／<code>Syön kaksi omenaa.</code>（数词）／<code>Juon vettä.</code>（不可数）。"
                )
                + p(
                    "<b>共性：</b>三条不同的规则指向同一个结果——部分格。考试里只要看到否定、数词、物质名词，先写部分格再考虑别的。"
                ),
            )
        ),
        practice=(
            ol(
                "为下列词造部分格单数：<code>talo、huone、bussi、avain、vesi、nainen、pieni、David、työ</code>。",
                "为下列词造部分格复数：<code>koulu、tuoli、koira、kirja、huone、nainen</code>。",
                "把 11 组词串中的任意 5 组造成完整句子（语序不变）。",
                "翻译：「我没有车，但我有很多朋友，我每天喝咖啡、读报纸。」",
                "判断该用部分格还是总格，并说明理由：<code>Katson (elokuva)</code>（正在看）/ <code>Ostan (leipä)</code>（买一整个）/ <code>Juon (maito)</code>（喝一些）。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> taloa、huonetta、bussia、avainta、vettä、naista、pientä、Davidia、työtä。逐项核对：e → -tta；辅音 → -ta；-si 特殊；-nen → -sta；i 脱落；人名加 i。"
                )
                + p(
                    "<b>2.</b> kouluja、tuoleja、koiria、kirjoja、huoneita、naisia。注意 kirja → kirjoja 是 a → o + ja，koira → koiria 是 a → i + a。"
                )
                + p(
                    "<b>3.</b> 示例：<code>Minä autan naapuria.</code> / <code>Sinä syöt kanaa ja riisiä.</code> / <code>Juotko sinä olutta?</code> / <code>He rakastavat jäätelöä.</code> / <code>Sanna etsii avainta.</code>"
                )
                + p(
                    "<b>4.</b> <code>Minulla ei ole autoa, mutta minulla on monta ystävää. Juon kahvia ja luen lehteä joka päivä.</code> 三个部分格：autoa（否定）、ystävää（monta 后单数）、kahvia 与 lehteä（不可数 / 部分动作）。"
                )
                + p(
                    "<b>5.</b> 正在看 → 部分格 <code>elokuvaa</code>；买一整个 → 总格 <code>leivän</code>；喝一些 → 部分格 <code>maitoa</code>。"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "部分格单数五条规则 + -nen / vesi / pieni 特殊表、部分格复数三条规律、五大用法、部分格与总格的对立。造句与填空都会直接考。",
            )
            + cal(
                "warn",
                "易错 1",
                "e 结尾忘加 -tta：<code>huonea</code>、<code>perhea</code>。",
            )
            + cal("warn", "易错 2", "数词后接主格或复数：<code>kaksi koirat</code>。")
            + cal("warn", "易错 3", "把不可数名词写成总格：<code>Juon maidon</code>。")
            + cal("warn", "易错 4", "否定句忘部分格：<code>En osta tietokone</code>。")
            + cal(
                "tip",
                "进阶",
                "能解释 -nen 词干 -se- 的机制（nainen → naise- → naista / naisen），并据此推出属格与部分格两种形式。",
            )
        ),
        checklist=(
            h2("部分格操作清单")
            + h3("造部分格单数五步")
            + st(
                "看词尾：元音（非 e）→ +a/-ä；e → +tta/-ttä；i → +a/-ä（部分 i→e）；辅音 → +ta/-tä；单音节短词 → +ta/-tä",
                "查特殊表：-nen → -sta；vesi/vuosi/kuusi/kuukausi；pieni/suuri/kuori",
                "人名辅音结尾先加 -i-（David → Davidia）",
                "检查元音和谐：a/o/u 用后元音，ä/ö/y 用前元音",
            )
            + h3("判断用不用部分格三问")
            + st(
                "是否否定句？是 → 部分格",
                "是否数词 2 以上或 monta？是 → 部分格单数",
                "动作是否完成、数量是否确定？否 → 部分格；是 → 总格",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "10_Tunti 9/2_Nominatiivi, genetiivi ja partitiivi.pdf",
                "p4",
                "部分格定义、单数词尾 -a/-ä 与特殊 -ta/-tta、复数三条规律、五大用法（数词、否定、动词、monta、不可数）",
            ),
            (
                "10_Tunti 9/4_KATSO videot Partitiivi.html",
                "全篇 4 个视频任务",
                "四条教学视频主题：Minulla ei ole、Verbi + partitiivi、Numero + partitiivi、Ruoka + partitiivi",
            ),
            (
                "10_Tunti 9/5_RuokaaJuomaa.pdf",
                "p1",
                "食品饮料的部分格对照表：vettä、maitoa、mehua、kahvia、teetä、limsaa、leipää、keittoa、salaattia、keksiä、pullaa、piirakkaa",
            ),
            (
                "10_Tunti 9/6_Puhu parille Mitä syöt_ (partitiivi).html",
                "全篇 4 问",
                "餐食问答中的部分格宾语：Syön leipää / jogurttia / salaattia / pizzaa",
            ),
            (
                "10_Tunti 9/7_Partitiivin muodostus.docx",
                "全篇 5 组 30 余词",
                "单数部分格五条规则与全部填空答案、-nen / -si / i 脱落 / 人名特殊表",
            ),
            (
                "13_Kertaa/5_PartitiiviLauseita.docx",
                "全篇 11 组",
                "造句题型：语序不变、动词变位、宾语部分格",
            ),
            (
                "13_Kertaa/6_PartitiiviLauseitaVASTAUKSET.docx",
                "全篇 11 句",
                "11 句标准答案，本讲义 10.7 节全部采用",
            ),
            (
                "（补充）",
                "10.4、10.6",
                "复数部分格后两行与部分格/总格对立的系统解释属拓展，原文只给零散例句",
            ),
            ("（跳过）", "—", "空白练习表格与图片页"),
        ),
    )
)

LEC.append(
    L(
        slug="t11-likes-meals-restaurant",
        tzh="第 11 讲 · 喜好表达、餐食与餐厅场景",
        ten="Likes, Meals and Eating Out",
        keywords=[
            "pitää + -sta",
            "tykätä + -sta",
            "elative",
            "translative -ksi",
            "allative -lle",
            "allergy",
            "conditional",
            "relative clause",
        ],
        files=[
            "11_Tunti 10/1_Pidätkö.pdf",
            "11_Tunti 10/2_PUHU PARILLE.html",
            "11_Tunti 10/3_Ateriat ja allergiat.pdf",
            "11_Tunti 10/4_PUHU PARILLE Mitä syöt_.html",
            "11_Tunti 10/5_Ystävänpäivä .pdf",
            "12_Tunti 11/1_KOTITEHTÄVÄ Sanasto, ravintolassa/intro/Sanasto, Ravintolassa.docx",
            "12_Tunti 11/3_Pizzeriamenu.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "第十一讲把「吃」这条线索收口：先讲喜好的表达（<code>pidätkö kahvista?</code>），再讲餐食与过敏（<code>Olen allerginen kalalle</code>），最后进餐厅（<code>Saisinko …?</code>、<code>Pääruoaksi otan …</code>）。三块内容共用两个格：<b>-sta/-stä</b>（喜好）与 <b>-lle</b>（过敏）。"
            )
            + p(
                "这一讲还引入两类此前未系统出现的材料：餐厅条件式礼貌用语（<code>haluaisit</code>、<code>Saisinko</code>）与《Ystävänpäivä》文化短文里的关系从句（<code>joka talvella lämmittää</code>）。两者都按「识别 + 仿说」要求，不要求主动变形。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "用 <code>pidätkö / tykkäätkö + -sta</code> 问答喜好，并正确否定",
                "为常见食物与抽象名词造出 -sta/-stä 形式，说明它与部分格的区别",
                "用 <code>aamiaiseksi / lounaaksi / illalliseksi / iltapalaksi</code> 说清「吃什么当某餐」",
                "用 <code>Olen allerginen + -lle</code>、<code>En voi syödä + 部分格</code> 说明饮食限制",
                "在餐厅完成点单对话，并读懂芬兰语菜单的加料与饮品栏",
            )
        ),
        detail=(
            h3("11.1 pitää 与 tykätä：两个「喜欢」")
            + p(
                "材料把两个动词并列讲，因为它们意思几乎相同、搭配的格也相同，但变位类型不同：<code>pitää</code> 属第一类，<code>tykätä</code> 属第四类。"
            )
            + tb(
                ("人称", "pitää（喜欢）", "tykätä（喜欢，口语更常用）"),
                ("minä", "pidän", "tykkään"),
                ("sinä", "pidät", "tykkäät"),
                ("hän", "pitää", "tykkää"),
                ("me", "pidämme", "tykkäämme"),
                ("te", "pidätte", "tykkäätte"),
                ("he", "pitävät", "tykkäävät"),
            )
            + p(
                "<code>pitää</code> 的第三人称 <code>pitää</code> 只有一个 t（不是 pitaa 也不是 pittaa）；<code>tykätä</code> 的第三人称 <code>tykkää</code> 是三个 k 两个 ä，拼写要准。"
            )
            + p("两个动词后面都接 <b>-sta/-stä</b>：")
            + tb(
                ("问句", "肯定答句", "否定答句"),
                ("Pidätkö kahvista?", "Joo, pidän kahvista.", "Ei, en pidä kahvista."),
                ("Pidätkö teestä?", "Joo, pidän teestä.", "Ei, en pidä teestä."),
                ("Pidätkö kalasta?", "Joo, pidän kalasta.", "Ei, en pidä kalasta."),
                (
                    "Pidätkö musiikista?",
                    "Joo, pidän musiikista.",
                    "Ei, en pidä musiikista.",
                ),
                (
                    "Tykkäätkö suklaasta?",
                    "Joo, tykkään suklaasta.",
                    "Ei, en tykkää suklaasta.",
                ),
                (
                    "Tykkäätkö kissoista vai koirista?",
                    "Tykkään kissoista.",
                    "En tykkää kummastakaan.",
                ),
                ("Pidätkö minusta?", "Joo, pidän sinusta.", "—"),
                ("Pidätkö hänestä?", "Joo, pidän hänestä.", "—"),
            )
            + p(
                "注意人称代词的 -sta 形式不规则：<code>minä → minusta</code>、<code>sinä → sinusta</code>、<code>hän → hänestä</code>、<code>me → meistä</code>、<code>te → teistä</code>、<code>he → heistä</code>。这是本讲最容易写错的一组。"
            )
            + h3("11.2 -sta/-stä 格的构成")
            + p(
                "-sta/-stä 是出格（elatiivi），本义是「从……里面出来」。构成规则比部分格简单：<b>取词干，加 -sta/-stä</b>。难点在于词干本身可能要变。"
            )
            + tb(
                ("主格", "-sta 形式", "说明"),
                ("kahvi", "kahvista", "i 结尾直接用词干"),
                ("tee", "teestä", "ee + stä（前元音和谐）"),
                ("kala", "kalasta", "a 结尾 + sta"),
                ("musiikki", "musiikista", "kk → k 弱化"),
                ("suklaa", "suklaasta", "长元音保留"),
                ("kissa", "kissasta", "无交替"),
                ("koira", "koirasta", "无交替"),
                ("vesi", "vedestä", "si → de（特殊词干）"),
                ("kuppi", "kupista", "pp → p"),
                ("tyttö", "tytöstä", "tt → t"),
                ("paita", "paidasta", "t → d"),
                ("olut", "oluesta", "辅音结尾：ut → ue"),
                ("jalkapallo", "jalkapallosta", "复合词整体加词尾"),
            )
            + p(
                "为什么喜欢用 -sta 而不是部分格？语义解释是：喜欢被视为「从某物那里获得愉悦」，所以用「从」的格。这个解释能帮你记住搭配，不必每次靠背。"
            )
            + cal(
                "warn",
                "最高频错误",
                "<code>Pidän kahvi</code>、<code>Tykkään kala</code> 都错。这两个动词后面<b>必须</b>有 -sta/-stä，不能接主格或部分格。这是本讲丢分最多的一处。",
            )
            + p(
                "与部分格的分工要清楚：<code>Haluan kahvia</code>（我想要一些咖啡，部分格）／<code>Pidän kahvista</code>（我喜欢咖啡，出格）。同一名词因动词不同而换格，这是芬兰语搭配的典型现象。"
            )
            + h3("11.3 餐食词汇与 -ksi 格")
            + p("材料列出五餐：")
            + tb(
                ("餐", "含义", "「作为某餐吃」的形式", "时间"),
                ("aamiainen", "早餐", "aamiaiseksi", "aamulla"),
                ("lounas", "午餐", "lounaaksi", "päivällä / kello 11–12"),
                ("välipala", "加餐、点心", "välipalaksi", "iltapäivällä"),
                ("päivällinen / illallinen", "晚餐", "illalliseksi", "illalla"),
                ("iltapala", "夜宵", "iltapalaksi", "myöhään illalla"),
            )
            + p(
                "问「你早餐吃什么」是 <code>Mitä syöt aamiaiseksi?</code>，答 <code>Syön aamiaiseksi leipää ja jogurttia</code>。这里的 <code>-ksi</code> 是转变格（translatiivi），表示「变成、作为」——把食物「变成」这一餐。"
            )
            + p(
                "同类结构还有 <code>Pääruoaksi otan kalaa</code>（主菜我要鱼）、<code>Jälkiruoaksi otan jäätelöä</code>（甜点我要冰淇淋）。<code>-ksi</code> 与 <code>-sta</code> 的差别在于：前者表角色 / 结果，后者表来源。"
            )
            + p(
                "材料还提到芬兰人的用餐习惯：<code>Generally Finns eat their meals earlier than in southern countries. Breakfast, lunch and dinner are quite large and energy rich. Evening snack is often times very light.</code> 这句话可作为口试里「比较饮食文化」的素材。"
            )
            + h3("11.4 过敏与特殊饮食：-lle 与部分格")
            + p(
                "材料的问句是 <code>Onko sinulla erikoisruokavalio?</code>（你有特殊饮食吗？）与 <code>Onko sinulla allergioita?</code>（你有过敏吗？）。答法有三套："
            )
            + tb(
                ("句型", "例句", "语法"),
                ("Minulla on …", "Minulla on keliakia.", "疾病名作主格宾语"),
                (
                    "En voi syödä + 部分格",
                    "En voi syödä lihaa / kalaa / tomaattia / sitruunaa / pähkinää.",
                    "情态动词 voida + 部分格宾语",
                ),
                (
                    "Olen allerginen + -lle",
                    "Olen allerginen kalalle / tomaatille / sitruunalle / pähkinälle.",
                    "形容词 + 向格 -lle",
                ),
                ("Olen …", "Olen kasvissyöjä. / Olen vegaani.", "身份名词作表语"),
                (
                    "Ei, minulla ei ole.",
                    "Ei, minulla ei ole allergioita.",
                    "否定句 + 部分格复数",
                ),
            )
            + p(
                "-lle 的构成要注意词干变化：<code>kala → kalalle</code>、<code>tomaatti → tomaatille</code>（tt → t）、<code>pähkinä → pähkinälle</code>、<code>sipuli → sipulille</code>、<code>maito → maidolle</code>（t → d）、<code>kana → kanalle</code>。"
            )
            + p("材料还给了包装上的饮食缩写，阅读菜单必用：")
            + ul(
                "<code>G</code> = gluteeniton（无麸质）；<code>VL</code> = vähälaktoosinen（低乳糖）；<code>L</code> = laktoositon（无乳糖）；<code>M</code> = maidoton（无奶）；<code>V</code> = vegaaninen（纯素）。"
            )
            + p(
                "特殊饮食的词汇：<code>keliakia</code>（乳糜泻）、<code>laktoosi-intoleranssi</code>（乳糖不耐）、<code>kasvissyöjä</code>（素食者）、<code>vegaani</code>（纯素者）。"
            )
            + h3("11.5 餐厅：从进店到点单")
            + p("材料的餐厅词汇按对话顺序排列，可以直接当脚本用：")
            + tb(
                ("服务员 / 顾客用语", "中文", "语法点"),
                (
                    "Syömään tulossa?",
                    "来吃饭吗？",
                    "口语省略问句，<code>tulossa</code> 是 essive",
                ),
                (
                    "Voit valita pöydän.",
                    "你可以选桌子。",
                    "<code>voida</code> 第二人称 + 原形",
                ),
                ("Tässä ruokalista.", "这是菜单。", "<code>tässä</code> 固定说法"),
                (
                    "Voinko tuoda jotain juotavaa?",
                    "要我拿点喝的吗？",
                    "<code>voida + -ko</code>；<code>juotavaa</code> 部分格",
                ),
                (
                    "Mitä haluaisit syödä?",
                    "你想吃什么？",
                    "条件式 <code>haluaisit</code>，礼貌",
                ),
                (
                    "Saisinko …?",
                    "我可以要……吗？",
                    "条件式 <code>saada</code>，最常用礼貌请求",
                ),
                ("Pääruoaksi otan …", "主菜我要……", "<code>-ksi</code> 表角色"),
                ("kala → kalaa", "鱼", "部分格，因为「一些鱼」"),
                ("uuniperuna → uuniperunaa", "烤土豆", "部分格"),
                ("kasviskeitto → kasviskeittoa", "蔬菜汤", "部分格"),
                ("talon viini", "店选葡萄酒（house wine）", "属格 + 名词"),
                (
                    "kuiva valkoviini",
                    "干白葡萄酒",
                    "<code>kuiva → kuivaa</code>（部分格）",
                ),
            )
            + p(
                "这里出现了本课程第一个条件式（conditional）语境：<code>haluaisit</code>、<code>Saisinko</code>、<code>Voinko</code>。条件式词尾是 <code>-isi-</code>，插在词干与人称词尾之间：<code>halua- + isi + t → haluaisit</code>、<code>saa- + isi + n + ko → saisinko</code>。"
            )
            + cal(
                "tip",
                "只要求识别与仿说",
                "本课程不要求你系统变位条件式，但必须会用这三个固定礼貌说法：<code>Saisinko …?</code>（我可以要……吗）、<code>Mitä haluaisit …?</code>（你想要什么）、<code>Voisitko …?</code>（你能……吗）。餐厅与商店场景直接用。",
            )
            + h3("11.6 菜单读法：加料与饮品")
            + p(
                "材料的菜单是「Suzan pizza ja kebab」，先给一句总说明：<code>Kaikkiin pizzoihin kuuluu pizzamauste ja valkosipuli.</code>（所有披萨都含披萨香料与大蒜。）注意 <code>kuulua</code>（属于、包含）后接 illative：<code>kaikkiin pizzoihin</code>。"
            )
            + p(
                "<code>Lisätäytteet</code>（加料）栏的词汇：<code>ananas</code>（菠萝）、<code>aurinkokuivattu tomaatti</code>（日晒番茄）、<code>fetajuusto</code>（菲达奶酪）、<code>herkkusieni</code>（蘑菇）、<code>ilmakuivattu kinkku</code>（风干火腿）、<code>jauheliha</code>（肉馅）、<code>kana</code>（鸡肉）、<code>katkarapu</code>（虾）、<code>kebabliha</code>（烤肉）、<code>kinkku</code>（火腿）、<code>mozzarella</code>、<code>oliivi</code>（橄榄）、<code>paprika</code>（彩椒）、<code>pepperoni</code>、<code>punasipuli</code>（红洋葱）、<code>salami</code>、<code>sinihomejuusto</code>（蓝纹奶酪）、<code>tomaatti</code>、<code>tonnikala</code>（金枪鱼）。"
            )
            + p(
                "<code>Juomat</code>（饮品）栏：<code>Vesi 1 e</code>、<code>Kivennäisvesi 2,50 e</code>、<code>Coca-Cola 2,50 e</code>、<code>Fanta 2,50 e</code>、<code>Olut 5 e</code>、<code>Siideri 6 e</code>。价格读法：<code>2,50 e</code> 读 <code>kaksi euroa viisikymmentä</code> 或 <code>kaksi viisikymmentä</code>；<code>e</code> 是 <code>euro</code> 的缩写。"
            )
            + p(
                "点单完整示范：<code>Anteeksi, saisinko pizzan? Pääruoaksi otan pizzan ja juomaksi otan vettä.</code> 注意 <code>juomaksi</code>（作为饮料）同样是 -ksi。"
            )
            + h3("11.7 Ystävänpäivä：文化短文与关系从句")
            + p(
                "材料最后一篇是《Ystävänpäivä》（2 月 14 日）的文化介绍，信息点很密集："
            )
            + ul(
                "在芬兰，这一天献给<b>朋友</b>而不是恋人：<code>Suomessa ystävänpäivä on omistettu ystäville, ei rakastavaisille</code>。",
                "这一节日很新，1980 年代才开始流行：<code>Juhla on uusi – sen juhlinta alkoi 80-luvulla</code>。",
                "如今一些年轻伴侣也按国际的浪漫方式庆祝。",
                "它也是热门的求婚日：<code>Se on suosittu päivä kosia</code>（<code>kosia</code> = 求婚）。",
                "传统：卡片、短信、小礼物、外出吃饭、看电影。卡片数量仅次于圣诞。",
            )
            + p("材料给了一组高价值短语，可以直接用于口语考试：")
            + tb(
                ("短语", "中文", "语法点"),
                (
                    "Minä rakastan sinua.",
                    "我爱你。",
                    "<code>rakastaa</code> + 部分格 <code>sinua</code>",
                ),
                (
                    "Minä tykkään sinusta.",
                    "我喜欢你。",
                    "<code>tykätä</code> + <code>sinusta</code>",
                ),
                (
                    "Minä pidän sinusta.",
                    "我喜欢你。",
                    "<code>pitää</code> + <code>sinusta</code>",
                ),
                ("Minä välitän sinusta.", "我在乎你。", "<code>välittää</code> + 出格"),
                (
                    "Olet tärkeä / rakas / ihana.",
                    "你很重要 / 亲爱的 / 可爱。",
                    "形容词作表语用主格",
                ),
                (
                    "Olet paras ystäväni.",
                    "你是我最好的朋友。",
                    "<code>paras</code> 最高级 + 所有格后缀",
                ),
                (
                    "Kiitos ystävyydestä!",
                    "谢谢你的友谊！",
                    "<code>ystävyys → ystävyydestä</code>",
                ),
                (
                    "Mennäänkö naimisiin?",
                    "我们结婚吧？",
                    "被动式 <code>mennään</code> + <code>-ko</code>",
                ),
            )
            + p("短文里的儿歌有两句关系从句，是很好的识别素材：")
            + p(
                "<code>Minun ystäväni on kuin villasukka, joka talvella lämmittää.</code>（我的朋友像一只毛袜，在冬天温暖我。）<code>minun ystäväni on kuin niityn kukka, joka saa minut hymyilemään.</code>（我的朋友像一朵草地上的花，让我微笑。）"
            )
            + p(
                "这里的关系代词是 <code>joka</code>（谁 / 哪个），后面动词用第三人称单数：<code>joka … lämmittää</code>、<code>joka saa</code>。<code>kuin</code> 表「像」；<code>niityn kukka</code> 是属格修饰（草地的花）；<code>saa minut hymyilemään</code> 是「使役 + -maan」结构（让我笑起来）。"
            )
            + p(
                "材料还列了 <code>hellittelynimet</code>（昵称）：<code>rakas / rakkaani</code>、<code>kulta / kultanen / kultsi</code>、<code>muru / murunen</code>、<code>nuppu</code>、<code>ihana</code>、<code>hani / beibi</code>。构词上最常见的是 <code>-nen</code> 与 <code>-liini</code> 两个后缀：<code>Noora → Nooranen / Nooraliini</code>、<code>Tomi → Tominen / Tomiliini</code>。"
            )
            + p(
                "材料还提醒：<code>Monet suomalaiset eivät käytä hellittelynimiä paljon tai julkisesti.</code>（很多芬兰人不多用、尤其不在公开场合用昵称。）这是文化差异，口试里可以用来对比。"
            )
            + h3("11.8 常见错误")
            + cal(
                "warn",
                "高频错误 1",
                "<code>pidän kahvi</code> / <code>tykkään kala</code> 缺 -sta。",
            )
            + cal(
                "warn",
                "高频错误 2",
                "代词 -sta 形式写错：<code>minä → minusta</code>（不是 minusta 之外的 minusta），<code>hän → hänestä</code>（不是 hänstä）。",
            )
            + cal(
                "warn",
                "高频错误 3",
                "<code>Olen allerginen kala</code> 缺 -lle：应为 <code>Olen allerginen kalalle</code>。",
            )
            + cal(
                "warn",
                "高频错误 4",
                "<code>Mitä syöt aamiainen</code> 缺 -ksi：应为 <code>aamiaiseksi</code>。",
            )
            + cal(
                "tip",
                "记忆卡",
                "把三组搭配写成卡片：<b>pitää/tykätä + sta</b>、<b>allerginen + lle</b>、<b>syön … + ksi</b>。三组各配三个名词，考前一天只背这九张。",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("pitää", "喜欢", "Type 1; requires -sta/-stä: pidän kahvista."),
            ("tykätä", "喜欢（口语）", "Type 4: tykkään, tykkäät, tykkää."),
            ("kahvista", "咖啡（出格）", "Pidän kahvista = I like coffee."),
            ("minusta", "我（出格）", "Pidätkö minusta? — Do you like me?"),
            ("aamiainen", "早餐", "aamiaiseksi = as breakfast."),
            ("lounas", "午餐", "lounaaksi = for lunch."),
            ("illallinen", "晚餐", "illalliseksi = for dinner."),
            ("iltapala", "夜宵", "iltapalaksi = for supper."),
            ("erikoisruokavalio", "特殊饮食", "Onko sinulla erikoisruokavalio?"),
            ("keliakia", "乳糜泻", "Minulla on keliakia."),
            ("laktoosi-intoleranssi", "乳糖不耐", "Minulla on laktoosi-intoleranssi."),
            ("allerginen", "过敏的", "Olen allerginen kalalle (allative)."),
            ("kasvissyöjä", "素食者", "Olen kasvissyöjä."),
            ("vegaani", "纯素者", "Olen vegaani."),
            ("ruokalista", "菜单", "Tässä ruokalista."),
            ("Saisinko …?", "我可以要……吗？", "Conditional polite request with -isi-."),
            ("pääruoka", "主菜", "Pääruoaksi otan kalaa."),
            ("joka", "关系代词", "villasukka, joka talvella lämmittää."),
        ),
        examples=(
            qa(
                "例 1　回答 <code>Pidätkö kalasta?</code> 与 <code>Tykkäätkö suklaasta?</code>，一肯一否。",
                p(
                    "<b>解：</b><code>Joo, pidän kalasta.</code> / <code>Ei, en tykkää suklaasta.</code>"
                )
                + p(
                    "<b>核对：</b>两个答句都保留 -sta；否定式 <code>en pidä</code>、<code>en tykkää</code> 后仍接 -sta，不能换成部分格。"
                ),
            )
            + qa(
                "例 2　把「我早餐吃面包和酸奶，午餐吃沙拉和鸡肉」译成芬兰语。",
                p(
                    "<b>解：</b><code>Syön aamiaiseksi leipää ja jogurttia. Syön lounaaksi salaattia ja kanaa.</code>"
                )
                + p(
                    "<b>语法：</b>餐食用 -ksi；食物宾语用部分格（不可数或「一些」）。四个部分格：leipää、jogurttia、salaattia、kanaa。"
                ),
            )
            + qa(
                "例 3　把「我对坚果过敏，所以我不能吃巧克力」译成芬兰语。",
                p(
                    "<b>解：</b><code>Olen allerginen pähkinälle, joten en voi syödä suklaata.</code>"
                )
                + p(
                    "<b>要点：</b><code>pähkinä → pähkinälle</code>（-lle）；<code>en voi syödä</code> 后接部分格 <code>suklaata</code>；<code>joten</code> = 所以。"
                ),
            )
            + qa(
                "例 4　在餐厅点单：主菜要烤土豆配鱼，饮料要水。写出两句。",
                p(
                    "<b>解：</b><code>Pääruoaksi otan uuniperunaa ja kalaa.</code> / <code>Juomaksi otan vettä.</code>"
                )
                + p(
                    "<b>更礼貌：</b><code>Saisinko uuniperunaa ja kalaa? Ja vielä vettä, kiitos.</code> 条件式 <code>Saisinko</code> 比 <code>Otan</code> 更客气，两者都能用。"
                ),
            )
        ),
        practice=(
            ol(
                "变位 <code>pitää</code> 与 <code>tykätä</code> 的六个人称，并各造一句喜欢 / 不喜欢的句子。",
                "为下列词造 -sta/-stä 形式：<code>kahvi、tee、kala、musiikki、suklaa、kissa、olut、vesi</code>。",
                "把五餐名称写成 -ksi 形式，并用其中三个造句（<code>Mitä syöt …?</code>）。",
                "翻译：「我不吃鱼，因为我对鱼过敏；但我喜欢蔬菜汤。」",
                "写一段 6 句的餐厅对话：服务员问候、给菜单、问想吃什么、顾客点主菜与饮料、道谢。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> pitää：pidän / pidät / pitää / pidämme / pidätte / pitävät；tykätä：tykkään / tykkäät / tykkää / tykkäämme / tykkäätte / tykkäävät。例句：<code>Pidän kahvista, mutta en pidä teestä.</code>"
                )
                + p(
                    "<b>2.</b> kahvista、teestä、kalasta、musiikista、suklaasta、kissasta、oluesta、vedestä。注意 olut → oluesta（辅音结尾）、vesi → vedestä（si → de）。"
                )
                + p(
                    "<b>3.</b> aamiaiseksi、lounaaksi、välipalaksi、illalliseksi、iltapalaksi。例句：<code>Mitä syöt lounaaksi? — Syön lounaaksi keittoa ja leipää.</code>"
                )
                + p(
                    "<b>4.</b> <code>En syö kalaa, koska olen allerginen kalalle. Mutta pidän kasviskeittosta.</code> 注意 <code>kasviskeitto → kasviskeitosta</code>（tt → t）。"
                )
                + p(
                    "<b>5.</b> 示例：<code>Hyvää iltaa! Syömään tulossa? — Kyllä, kiitos. — Voit valita pöydän. Tässä ruokalista. Mitä haluaisit syödä? — Pääruoaksi otan kalaa ja uuniperunaa. — Voinko tuoda jotain juotavaa? — Saisinko vettä, kiitos.</code>"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "<code>pitää / tykätä + -sta</code>、<code>-ksi</code> 的餐食表达、<code>allerginen + -lle</code>、餐厅礼貌用语 <code>Saisinko</code>。口语考试几乎必问喜好与饮食。",
            )
            + cal(
                "warn",
                "易错 1",
                "喜欢动词后接主格或部分格：<code>pidän kahvi</code>、<code>tykkään kahvia</code>。",
            )
            + cal(
                "warn",
                "易错 2",
                "代词出格写错：<code>minusta</code>、<code>hänestä</code>。",
            )
            + cal(
                "warn",
                "易错 3",
                "<code>aamiainen</code> 不变 -ksi：<code>syön aamiainen</code>。",
            )
            + cal(
                "tip",
                "进阶",
                "能解释 -sta 与部分格在同一名词上的不同含义（<code>pidän kahvista</code> vs <code>haluan kahvia</code>），并在口语中正确切换。",
            )
        ),
        checklist=(
            h2("喜好、餐食与点单清单")
            + h3("说喜好三步")
            + st(
                "选动词：pitää（书面）或 tykätä（口语）",
                "按人称变位：pidän / tykkään …",
                "宾语加 -sta/-stä，否定也保留",
            )
            + h3("点单四步")
            + st(
                "进店：<code>Syömään tulossa?</code> → <code>Kyllä, kiitos</code>",
                "要菜单：<code>Saisinko ruokalistan?</code>",
                "点主菜：<code>Pääruoaksi otan + 部分格</code>",
                "点饮料：<code>Juomaksi otan + 部分格</code>",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "11_Tunti 10/1_Pidätkö.pdf",
                "p2–p5",
                "pitää（第一类）与 tykätä（第四类）变位、+ -sta/-stä 搭配、八组问答、代词出格",
            ),
            (
                "11_Tunti 10/2_PUHU PARILLE.html",
                "全篇 12 问",
                "口语问答卡：kahvi、tee、suklaa、kala、musiikki、kissat vai koirat",
            ),
            (
                "11_Tunti 10/3_Ateriat ja allergiat.pdf",
                "p2–p3",
                "五餐词汇与用餐习惯、特殊饮食、En voi syödä + 部分格、Olen allerginen + -lle、G/VL/L/M/V 标记",
            ),
            (
                "11_Tunti 10/4_PUHU PARILLE Mitä syöt_.html",
                "全篇 6 问",
                "餐食问答模板与过敏问答",
            ),
            (
                "11_Tunti 10/5_Ystävänpäivä .pdf",
                "p2–p11",
                "情人节文化差异、八条情感短语、昵称与 -nen/-liini 后缀、关系从句 joka、两句谚语",
            ),
            (
                "12_Tunti 11/1_KOTITEHTÄVÄ … Sanasto, Ravintolassa.docx",
                "全篇 16 条",
                "餐厅词汇与句型：ruokalista、pöytä、juotavaa、talon viini、Saisinko、Pääruoaksi otan",
            ),
            (
                "12_Tunti 11/3_Pizzeriamenu.pdf",
                "p1–p2",
                "菜单读法：pizzamauste、19 种加料、6 种饮品与价格",
            ),
            (
                "（补充）",
                "11.5、11.7",
                "条件式 -isi- 的构成与 joka 从句的结构说明属拓展，原文只给用法例句",
            ),
            ("（跳过）", "—", "菜单图片与情人节插图不含语言点"),
        ),
    )
)

LEC.append(
    L(
        slug="t12-review-exam",
        tzh="第 12 讲 · 复习与考试题型",
        ten="Revision and Exam Formats",
        keywords=[
            "revision",
            "exam format",
            "conjugation drill",
            "listening task",
            "oral presentation",
            "passive",
            "perfect tense",
            "common errors",
        ],
        files=[
            "13_Kertaa/1_Kertaus FI2.pdf",
            "13_Kertaa/2_Vastaukset, Kertaus FI2.pdf",
            "13_Kertaa/4_KUUNTELE Milloin juna (train) lähtee_.html",
            "13_Kertaa/5_PartitiiviLauseita.docx",
            "13_Kertaa/6_PartitiiviLauseitaVASTAUKSET.docx",
            "14_Kokeet_Exams/1_Finnish 2, presentation, korjattu.docx",
            "14_Kokeet_Exams/2_Esimerkki, vappu.pdf",
        ],
        overview=(
            h2("本节定位")
            + p(
                "最后一讲不再引入新语法，而是把十一讲的内容按考试形态重组。材料的复习卷（Kertaus FI2）与考试说明（Kokeet/Exams）正好给出两条线：一条是<b>知识点回扫</b>（时间、日常话题、格、动词），一条是<b>题型训练</b>（变位填空、格转换、造句、听力、口试演示）。"
            )
            + p(
                "本讲还处理一个现实问题：课程里出现过几个「超出本课语法范围但必须认识」的形式——完成体（<code>olet syntynyt</code>、<code>olet harrastanut</code>）、被动式（<code>syödään</code>、<code>mennään</code>）、条件式（<code>haluaisit</code>、<code>Saisinko</code>）、从句（<code>joka</code>、<code>vaikka</code>）。它们不进入产出考点，但会出现在听力与阅读里，这一讲集中说明构成，避免考场上「见过但认不出」。"
            )
            + p("学完本节你应当能够：")
            + ck(
                "按六个板块自测整门课：时间表达、日常话题、动词变位、格系统、词汇、口语任务",
                "完成变位填空、格转换、造句三类笔试题，并说出每类题的检查顺序",
                "在听力中区分数字时间与传统时间，抓住 <code>yli / vailla / puoli</code> 三个关键词",
                "按考试要求准备 5–10 分钟芬兰语演示，并用六个固定问句组织内容",
                "识别完成体、被动式、条件式、关系从句四类「超纲但常见」的形式，不误判为生词",
            )
        ),
        detail=(
            h3("12.1 复习地图：六个板块")
            + p(
                "材料的复习卷把整门课压成三页，结构非常清楚：Ajanilmaukset（时间表达）、Arkielämä（日常生活：爱好、计划、饮食）、Kielioppi（语法：属格与部分格、动词变位）。按这三块再加词汇、听力、口试，就是完整的复习地图。"
            )
            + tb(
                ("板块", "要复习什么", "对应讲次", "自测方式"),
                (
                    "时间表达",
                    "kello、viikonpäivät、kuukaudet、vuodenajat、Milloin 的四类格",
                    "第 2、3 讲",
                    "说出任意时刻的两种读法，写出四季与十二个月的时间格",
                ),
                (
                    "日常话题",
                    "自我介绍、爱好、计划、饮食与过敏",
                    "第 1、4、6、8、11 讲",
                    "对每个话题连续说 5 句不卡",
                ),
                (
                    "动词",
                    "六类变位、否定式、KPT",
                    "第 5、7 讲",
                    "任取一词写出 12 个形式（肯定 6 + 否定 6）",
                ),
                (
                    "格系统",
                    "主格、属格、部分格、地点格",
                    "第 1、8、9、10 讲",
                    "同一名词写出四种格形式",
                ),
                (
                    "词汇",
                    "食物、爱好、家庭、天气、餐厅",
                    "第 2、6、8、11 讲",
                    "按类别默写，每类 10 词",
                ),
                (
                    "口语任务",
                    "访谈、演示、餐厅对话",
                    "第 6、11、12 讲",
                    "录音 2 分钟，回听找三处错误",
                ),
            )
            + h3("12.2 时间表达总复习")
            + p(
                "时间部分是考试最容易拿分也最容易丢分的区块，因为它全是固定形式。四张表必须能默写："
            )
            + tb(
                ("问题", "答案格式", "例子"),
                (
                    "Mitä kello on?（数字）",
                    "小时 + 分钟两个数",
                    "Kello on seitsemäntoista kolmenkymmentä.",
                ),
                (
                    "Mitä kello on?（传统）",
                    "yli / vailla / puoli 结构",
                    "puoli kuusi / kaksikymmentä vailla seitsemän",
                ),
                ("Mikä päivä nyt on?", "主格", "Nyt on tiistai."),
                ("Milloin …?（星期）", "-na", "tiistaina"),
                ("Mikä kuukausi nyt on?", "主格", "Nyt on huhtikuu."),
                ("Milloin …?（月份）", "-ssa", "huhtikuussa"),
                ("Mikä vuodenaika nyt on?", "主格", "Nyt on kesä."),
                ("Milloin …?（季节）", "-lla", "kesällä"),
                ("Milloin …?（钟点）", "-lta", "seitsemältä"),
                ("Milloin …?（时段）", "-lla", "aamulla / illalla"),
            )
            + p(
                "材料的复习答案给了七个示范答句，可以直接背：<code>Kello on kaksikymmentä vailla kymmenen.</code>／<code>Kello on puoli neljä.</code>／<code>Nyt on tiistai.</code>／<code>Nyt on huhtikuu.</code>／<code>Syön lounasta yhdeltä.</code>／<code>Suomen tunti on tiistaina.</code>／<code>Olen syntynyt huhtikuussa.</code>"
            )
            + h3("12.3 动词复习：PILATA 与课文填空")
            + p(
                "复习卷的第一道变位题是 <code>PILATA</code>（破坏）。它属第四类（-ata），词干 <code>pilaa-</code>，标准答案如下："
            )
            + tb(
                ("人称", "肯定", "否定"),
                ("minä", "pilaan", "en pilaa"),
                ("sinä", "pilaat", "et pilaa"),
                ("hän", "pilaa", "ei pilaa"),
                ("me", "pilaamme", "emme pilaa"),
                ("te", "pilaatte", "ette pilaa"),
                ("he", "pilaavat", "eivät pilaa"),
            )
            + p("第二道是短文填空，讲 Matti 与 Minna 去购物。标准答案与动词类型如下：")
            + tb(
                ("原文空格", "答案", "动词类型与要点"),
                (
                    "Matti ja Minna ___ (mennä) kauppaan.",
                    "menevät",
                    "第三类 mennä；复数主语 → -vat",
                ),
                ("He ___ (ostaa) munkkeja.", "ostavat", "第一类；复数 → -vat"),
                (
                    "He ___ (ostaa, neg.) karkkia",
                    "eivät osta",
                    "复数否定用 eivät + 词干",
                ),
                ("vaikka Minna ___ (tahtoa).", "tahtoo", "第一类 tahtoa，第三人称单数"),
                (
                    "Kotona Minna ___ (kastella) kukat.",
                    "kastelee",
                    "第三类 kastella，ll → l",
                ),
                (
                    "Hän ___ (valita) sopivat kukat.",
                    "valitsee",
                    "第五类 valita，-se 词干",
                ),
                ("Minä ___ (tulla) heille vieraaksi.", "tulen", "第三类 tulla，ll → l"),
                ("He ___ (siivota) yhdessä.", "siivoavat", "第四类；复数 → -vat"),
                (
                    "Matti ___ (imuroida) ja Minna ___ (pestä) ikkunat.",
                    "imuroi / pesee",
                    "imuroida 第二类；pestä 第三类 st → s",
                ),
            )
            + p(
                "这段填空几乎覆盖了全部考点：六类动词里出现了 1、2、3、4、5 类，肯定与否定，单数与复数主语。做完后按「类型 → 词干 → 人称 → 弱化」四步逐格核对，比整体重读有效。"
            )
            + h3("12.4 格系统总复习")
            + p(
                "把三格放在一起对照，是最有效的复习方式。材料在复习卷里要求「写属格 + 造句」「写部分格」两类练习："
            )
            + tb(
                ("主格", "属格", "部分格", "复习卷答案"),
                ("minä", "minun", "minua", "Hän on minun ystävä."),
                ("hän", "hänen", "häntä", "Kissa on hänen."),
                ("kahvi", "kahvin", "kahvia", "Sokeri on kahvin vieressä."),
                ("tyttö", "tytön", "tyttöä", "Kirja on tytön."),
                ("Jemina", "Jeminan", "Jeminaa", "Se on Jeminan talo."),
                ("Oscar", "Oscarin", "Oscaria", "Olen Oscarin ystävä."),
            )
            + p(
                "部分格填空题的原文是购物清单：<code>Ostan kaupasta 3 munaa, 2 porkkanaa, öljyä, sokeria ja jauhoa. Aion leipoa porkkanakakkua.</code> 六个答案分别对应：数词后部分格单数（munaa、porkkanaa）、不可数（öljyä、sokeria、jauhoa）、以及「打算烤一个胡萝卜蛋糕」的部分格宾语（porkkanakakkua，因为 aion + 动词表示意图，宾语取部分格）。"
            )
            + p(
                "第 9、10 讲的两套规则在这里合流：属格看「谁的」，部分格看「多少 / 是否完成」。复习时建议做一张 4×6 的表，把六个高频名词的四种形式一次写全。"
            )
            + h3("12.5 听力题型：两种时间读法")
            + p(
                "材料的听力练习（KUUNTELE: Milloin juna lähtee?）分两组：前三题用数字时间，后三题用传统时间。这正是第 3 讲的两套系统："
            )
            + tb(
                ("题型", "题干", "选项特征", "解题要点"),
                (
                    "数字时间",
                    "Juna Helsinkiin lähtee …",
                    "8.30 / 9.00 / 9.30",
                    "听「小时 + 分钟」两个数，注意 8.30 读 kahdeksan kolmenkymmentä",
                ),
                (
                    "数字时间",
                    "Juna Ouluun lähtee …",
                    "14.15 / 14.55 / 15.05",
                    "区分 neljätoista viisitoista 与 neljätoista viisikymmentäviisi",
                ),
                (
                    "数字时间",
                    "Juna Riihimäelle lähtee …",
                    "19.34 / 19.45 / 19.54",
                    "末位数字是关键：neljä / viisi",
                ),
                (
                    "传统时间",
                    "Bussi Tampereelle lähtee …",
                    "puoli 9 / 20 yli 9 / 20 vaille 9",
                    "puoli 9 = 8.30；yli 与 vaille 方向相反",
                ),
                (
                    "传统时间",
                    "Bussi Vaasaan lähtee …",
                    "10 yli 10 / 15 yli 10 / 20 yli 10",
                    "只差分钟数，听清 kymmenen / viisitoista / kaksikymmentä",
                ),
                (
                    "传统时间",
                    "Bussi Lappeenrantaan lähtee …",
                    "20 vaille 7 / puoli kahdeksan / 20 yli 7",
                    "puoli kahdeksan = 7.30，与两个 7 点选项要分清",
                ),
            )
            + p(
                "听力策略：<b>先判断题干用的是哪种读法</b>（数字时间会出现「点」的停顿，传统时间会出现 yli / vailla / puoli 这些词），再定位关键数字。不要试图记住整句，只抓「小时」「分钟方向」两个信息。"
            )
            + h3("12.6 口试与演示题型")
            + p(
                "材料的考试说明是一份 5–10 分钟双人或三人演示任务，主题限定在芬兰饮食："
            )
            + ul(
                "形式：小组制作幻灯片（可用 Powerpoint），每人必须参与准备与演讲。",
                "语言：<b>必须用芬兰语讲</b>，幻灯片上可加英文辅助，但芬兰语是主体。",
                "难度要求：<code>Don’t try to overdo this. It’s enough to tell the main things in Finnish</code>——说清要点即可，不追求复杂句。",
                "评分：1–5 分，按个人给分；两人贡献相当通常同分。",
                "场合：只对同组约十名同学与老师演讲。",
            )
            + p(
                "六个主题（早餐、午餐、晚餐、圣诞、复活节）都配了同一组问句，这组问句就是演示的提纲："
            )
            + tb(
                ("问句", "中文", "语法点"),
                (
                    "Milloin suomalaiset syövät aamiaista?",
                    "芬兰人什么时候吃早餐？",
                    "时间格",
                ),
                ("Missä suomalaiset syövät aamiaista?", "他们在哪里吃？", "地点格"),
                (
                    "Kenen kanssa he syövät?",
                    "他们和谁一起吃？",
                    "<code>kenen</code> 属格 + <code>kanssa</code>",
                ),
                (
                    "Mitä aamiaistapoja suomalaisilla on?",
                    "芬兰人有哪些早餐习惯？",
                    "<code>suomalaisilla on</code>（-lla 表拥有）",
                ),
                (
                    "Mitä suomalaiset syövät aamiaiseksi?",
                    "他们早餐吃什么？",
                    "-ksi 餐食格",
                ),
                (
                    "Onko tämä erilainen sinun maassa?",
                    "这在你的国家不一样吗？",
                    "比较句 + <code>sinun maassa</code>",
                ),
            )
            + p(
                "材料还给了一份范例演示《Suomalainen vappuruoka》（芬兰五一二节食物），可以直接当模板："
            )
            + ul(
                "开场：<code>Suomalaiset juhlivat vappua toukokuun alussa, ensimmäinen päivä toukokuuta.</code>",
                "定位：<code>Vappu on työläisten ja opiskelijoiden juhla.</code>（劳动者与学生的节日）",
                "时间地点人物：<code>Suomalaiset syövät vappuruokaa kotona, ravintolassa ja ulkona piknikillä. … perheen ja ystävien kanssa.</code>",
                "吃什么：<code>Vappuna suomalaiset juovat simaa. He syövät tippaleipiä ja munkkeja. … myös perunasalaattia, makkaraa ja grilliruokaa.</code>",
                "对比：<code>Minun kotimaassa …</code>（在我的国家……）",
                "收束：给出资料来源。",
            )
            + p(
                "这份范例里出现了一个新形式：<code>Mitä syödään?</code>（人们吃什么？）。这是<b>被动式</b>（passiivi），词尾 <code>-an/-än</code> 加在词干上：<code>syödä → syödään</code>、<code>mennä → mennään</code>、<code>ostaa → ostetaan</code>。被动式在口语里也用来表示「我们」，如 <code>Mennäänkö naimisiin?</code>（我们结婚吧？）。"
            )
            + cal(
                "tip",
                "识别级要求",
                "被动式只要求听懂与仿说固定句（<code>Mitä syödään?</code>、<code>Mennään!</code>、<code>Suomessa puhutaan suomea</code>），不要求系统变位。",
            )
            + h3("12.7 写作题型")
            + p(
                "材料的两次写作任务分别是「用现在时写下周计划」与「用指定动词写十句」。评分点是三条："
            )
            + ol(
                "时间词与格是否正确（ensi viikolla、maanantaina）。",
                "动词是否按人称变位、是否体现 KPT 交替。",
                "宾语是否用对格（部分格 / 总格 / -sta 等搭配）。",
            )
            + p(
                "复习卷的写作部分还给了一组「填动词」练习，答案已在 12.3 列出。写作时建议先写骨架（时间 + 主语 + 动词 + 宾语），再回头补形容词与副词，这样不容易漏格。"
            )
            + h3("12.8 超纲但常见：四类形式的识别")
            + p(
                "以下五类形式在本课程材料里出现过，但不属于产出考点。考场上只要能认出、能猜出意思即可："
            )
            + tb(
                ("形式", "例子", "构成", "识别线索"),
                (
                    "完成体 perfect",
                    "Olen syntynyt huhtikuussa. Olen harrastanut tanssia. Oletko naimisissa?",
                    "<code>olla</code> 现在时 + <code>-nut/-nyt</code> 分词",
                    "看到 <code>olen / olet / on</code> + 以 -nut/-nyt 结尾的词",
                ),
                (
                    "过去时 imperfekti",
                    "Mitä söit tänään? Piirsin kuvan. Hän kävi salilla.",
                    "词干 + <code>-i-</code> + 人称词尾：söit、piirsin、kävi",
                    "动词里插入 i 且不是现在时形式，时间词多为 tänään、eilen、lapsena",
                ),
                (
                    "被动式 passive",
                    "Mitä syödään? Mennäänkö naimisiin? Suomessa puhutaan suomea.",
                    "词干 + <code>-an/-än</code>（部分动词 -daan/-dään）",
                    "无人称、主语缺失，动词却带 -an/-ään",
                ),
                (
                    "条件式 conditional",
                    "Mitä haluaisit syödä? Saisinko kahvia?",
                    "词干 + <code>-isi-</code> + 人称词尾",
                    "出现 <code>-isi-</code>，语气礼貌",
                ),
                (
                    "从句",
                    "… vaikka Minna tahtoo. … villasukka, joka talvella lämmittää.",
                    "<code>vaikka</code>（虽然）、<code>joka</code>（关系代词）、<code>että</code>（that）",
                    "句中出现连词后接完整小句",
                ),
            )
            + p(
                "<code>Olen syntynyt</code> 是最值得单独记的一个：它是「出生」的固定说法，字面是「我被生出」，所以用完成体 + 被动分词。同理 <code>Oletko naimisissa?</code> 用 -ssa 表状态（「处于已婚之中」）。"
            )
            + p(
                "过去时（imperfekti）在本课程里只以个别词形出现，最典型的是第 9 讲的访谈问句 <code>Mitä söit tänään aamiaiseksi?</code>（你今天早餐吃了什么）与《Ystävänpäivä》里的 <code>Piirsin kuvan</code>（我画了一幅画）。构成方式是「词干 + <code>-i-</code> + 人称词尾」，与现在时的区别只在插入的 <code>-i-</code>。复习时只需能把这些形式与现在时形式区分开，不必系统变位。"
            )
            + h3("12.9 常见错误总表")
            + p("把十一讲出现过的错误集中列一遍，考前只看这一张表：")
            + tb(
                ("错误", "正确", "所属讲次"),
                (
                    "<code>Olen 20 vuosi</code>",
                    "<code>Olen 20 vuotta</code>",
                    "第 1 讲：年龄用部分格",
                ),
                (
                    "<code>Minulla ei ole koira</code>",
                    "<code>Minulla ei ole koiraa</code>",
                    "第 1、10 讲：否定句部分格",
                ),
                (
                    "<code>Kesässä sataa</code>",
                    "<code>Kesällä sataa</code>",
                    "第 2 讲：季节 -lla",
                ),
                (
                    "<code>On sateinen.</code>",
                    "<code>On sateinen sää. / On sateista.</code>",
                    "第 2 讲：主语或部分格",
                ),
                (
                    "<code>puoli kolmetoista</code>",
                    "<code>puoli yksi</code>",
                    "第 3 讲：传统时间只用 1–12",
                ),
                (
                    "<code>ensi viikko</code>",
                    "<code>ensi viikolla</code>",
                    "第 4 讲：时间状语要变格",
                ),
                (
                    "<code>tulen ostaa</code>",
                    "<code>tulen ostamaan</code>",
                    "第 4 讲：tulla + -maan",
                ),
                (
                    "<code>hän puhu</code>",
                    "<code>hän puhuu</code>",
                    "第 5 讲：第三人称延长元音",
                ),
                (
                    "<code>he ei puhu</code>",
                    "<code>he eivät puhu</code>",
                    "第 5、7 讲：eivät",
                ),
                ("<code>en tul</code>", "<code>en tule</code>", "第 7 讲：第三类加 -e"),
                (
                    "<code>Harrastan tanssi</code>",
                    "<code>Harrastan tanssia</code>",
                    "第 6 讲：harrastaa + 部分格",
                ),
                (
                    "<code>kaksi porkkanat</code>",
                    "<code>kaksi porkkanaa</code>",
                    "第 8、10 讲：数词 + 部分格单数",
                ),
                ("<code>kukkan</code>", "<code>kukan</code>", "第 9 讲：属格弱化"),
                (
                    "<code>huonea</code>",
                    "<code>huonetta</code>",
                    "第 10 讲：e 结尾 -tta",
                ),
                (
                    "<code>pidän kahvi</code>",
                    "<code>pidän kahvista</code>",
                    "第 11 讲：pitää + -sta",
                ),
                (
                    "<code>Olen allerginen kala</code>",
                    "<code>Olen allerginen kalalle</code>",
                    "第 11 讲：-lle",
                ),
            )
            + h3("12.10 考前 48 小时安排")
            + st(
                "第一天上午：默写四季、十二个月、七个星期的时间格，各三遍",
                "第一天下午：任取十个动词，写出肯定与否定共 12 个形式",
                "第一天晚上：六个高频名词的四种格形式 + 十个食物词的部分格",
                "第二天上午：做一遍复习卷的变位、格、造句三题，错题标注原因",
                "第二天下午：录音两分钟自我介绍 + 两分钟「我的爱好与饮食」，回听找错",
                "考前 1 小时：只看 12.9 错误总表与 12.2 时间表，不做新题",
            )
        ),
        kws=tb(
            ("Suomi", "中文", "English 说明"),
            ("kertaus", "复习", "Revision sheet Kertaus FI2."),
            ("koe, kokeet", "考试", "Exam; Kokeet/Exams folder."),
            ("taivuttaa", "变位", "Taivuta verbit = conjugate the verbs."),
            ("täydennä", "填空", "Täydennä verbit = fill in the verbs."),
            ("preesens", "现在时", "Present tense; also used for the future."),
            ("pilata", "破坏", "Type 4 drill verb: pilaan, pilaa, pilaavat."),
            ("siivota", "打扫", "Type 4: siivoan, siivoaa, siivoavat."),
            ("imuroida", "吸尘", "Type 2: imuroin, imuroi, imuroivat."),
            ("kuunnella", "听", "Type 3: kuuntelen, kuuntelee."),
            ("passiivi", "被动式", "Impersonal form: syödään, mennään, puhutaan."),
            ("syödään", "人们吃", "Mitä syödään? — What do people eat?"),
            ("olen syntynyt", "我出生", "Perfect with the passive participle."),
            ("konditionaali", "条件式", "haluaisit, saisinko — stem + -isi-."),
            (
                "imperfekti",
                "过去时",
                "Mitä söit tänään? Piirsin kuvan — stem + -i- + ending.",
            ),
            ("esitelmä", "演示、报告", "5–10 minute oral presentation in Finnish."),
            ("vailla, puoli", "差、半点", "Keywords that decide the listening answer."),
            ("kokonaisobjekti", "总格宾语", "Katson elokuvan vs katson elokuvaa."),
            ("vaikka", "虽然", "Subordinating conjunction: …, vaikka Minna tahtoo."),
        ),
        examples=(
            qa(
                "例 1　把 <code>PILATA</code> 的 12 个形式写出，并说明为什么词干是 <code>pilaa-</code>。",
                p(
                    "<b>解：</b>pilaan / pilaat / pilaa / pilaamme / pilaatte / pilaavat；en / et / ei / emme / ette / eivät pilaa。"
                )
                + p(
                    "<b>词干推导：</b><code>pilata</code> 结尾 -ata，属第四类。去 <code>-ta</code> 得 <code>pila</code>，按规则再加 <code>-a</code> 得 <code>pilaa-</code>。若忘加这一步，就会写出 <code>pilan</code> 这种错形。"
                ),
            )
            + qa(
                "例 2　听力判断：听到 <code>Kello on kaksikymmentä vaille seitsemän</code>，是几点？属于哪种读法？",
                p(
                    "<b>解：</b>差二十分七点 = 6:40。属于传统读法（含 <code>vailla</code>）。数字读法会说 <code>kuusi neljäkymmentä</code>。"
                )
                + p(
                    "<b>迁移：</b>听到 <code>vailla / vaille</code> 就往前取下一个小时，再减分钟。若听到 <code>puoli seitsemän</code>，则是 6:30。"
                ),
            )
            + qa(
                "例 3　按演示模板，用四句话介绍「芬兰人什么时候、在哪、和谁吃早餐，早餐吃什么」。",
                p(
                    "<b>解：</b><code>Suomalaiset syövät aamiaista yleensä seitsemältä tai kahdeksalta.</code> / <code>He syövät aamiaista kotona keittiössä.</code> / <code>He syövät aamiaista perheen kanssa.</code> / <code>He syövät aamiaiseksi puuroa, leipää ja kahvia.</code>"
                )
                + p(
                    "<b>语法核对：</b>时间用 -lta；地点用 -ssa；<code>perheen kanssa</code> 属格 + 后置词；餐食用 -ksi；食物用部分格。四句正好覆盖演示提纲的前四问。"
                ),
            )
            + qa(
                "例 4　识别并解释：<code>Mitä syödään? — Syödään tippaleipiä ja munkkeja.</code>",
                p(
                    "<b>解：</b><code>syödään</code> 是被动式（词干 syö- + -dään），意为「人们吃 / 大家吃」，不是「我被吃」。答句同用被动，宾语部分格复数。"
                )
                + p(
                    "<b>要点：</b>被动式的宾语仍遵循部分格规则（<code>tippaleipiä</code>、<code>munkkeja</code>），因为说的是不定量的食物。"
                ),
            )
        ),
        practice=(
            ol(
                "写出 <code>PILATA</code>、<code>siivota</code>、<code>imuroida</code> 的肯定六人称。",
                "把复习卷短文填空的十个空格写出答案并标注动词类型。",
                "写出 <code>minä、hän、kahvi、tyttö、Jemina、Oscar</code> 的属格，并各造一句。",
                "把购物清单句的部分格补全：<code>Ostan 3 ___ (muna), 2 ___ (porkkana), ___ (öljy), ___ (sokeri), ___ (jauho). Aion leipoa ___ (porkkanakakku).</code>",
                "用六个演示问句写一段 6 句的口头稿（主题：芬兰午餐），并标出每句用的格。",
            )
            + det(
                "答案与思路",
                p(
                    "<b>1.</b> pilata：pilaan / pilaat / pilaa / pilaamme / pilaatte / pilaavat。siivota：siivoan / siivoat / siivoaa / siivoamme / siivoatte / siivoavat。imuroida：imuroin / imuroit / imuroi / imuroimme / imuroitte / imuroivat。"
                )
                + p(
                    "<b>2.</b> menevät（3）、ostavat（1）、eivät osta（1 否定复数）、tahtoo（1）、kastelee（3）、valitsee（5）、tulen（3）、siivoavat（4）、imuroi（2）、pesee（3）。"
                )
                + p(
                    "<b>3.</b> minun / hänen / kahvin / tytön / Jeminan / Oscarin。例句：<code>Hän on minun ystävä.</code> / <code>Kissa on hänen.</code> / <code>Sokeri on kahvin vieressä.</code> / <code>Kirja on tytön.</code> / <code>Se on Jeminan talo.</code> / <code>Olen Oscarin ystävä.</code>"
                )
                + p(
                    "<b>4.</b> <code>munaa, porkkanaa, öljyä, sokeria, jauhoa, porkkanakakkua</code>。前两个是数词后部分格单数，中间三个不可数，最后一个是 <code>aion leipoa</code> 的部分格宾语。"
                )
                + p(
                    "<b>5.</b> 示例：<code>Suomalaiset syövät lounasta yhdeltätoista tai kahdeltatoista（时间 -lta）. He syövät lounasta työpaikan ruokalassa（地点 -ssa）. He syövät kollegoiden kanssa（属格 + kanssa）. Suomalaisilla on tapana syödä lämmintä ruokaa（拥有 -lla）. He syövät lounaaksi keittoa, salaattia ja leipää（餐食 -ksi + 部分格）. Tämä voi olla erilainen sinun maassa（比较）.</code>"
                ),
            )
        ),
        exam=(
            cal(
                "exam",
                "必考",
                "三类笔试题：变位填空（12 个形式）、格转换（属格 / 部分格）、造句（语序不变 + 动词变位 + 部分格）；听力两种时间读法；口试 5–10 分钟芬兰语演示。这五项覆盖全课程。",
            )
            + cal(
                "warn",
                "易错 1",
                "变位题只写形式不检查弱化：<code>pilan</code>、<code>kukkan</code>、<code>en tul</code> 三类错形都出在「少一步」。",
            )
            + cal(
                "warn",
                "易错 2",
                "造句题改动词序。题目明确要求 <code>Don’t change the word order</code>，只能变位与变格。",
            )
            + cal(
                "warn",
                "易错 3",
                "听力里把 <code>puoli</code> 指向的小时听反，或把 <code>vailla</code> 当成 <code>yli</code>。",
            )
            + cal(
                "tip",
                "进阶",
                "能在演示中主动使用 <code>-ksi</code>（餐食）、<code>-lla</code>（拥有）、属格 + <code>kanssa</code>（和谁）三种结构各两次，并至少出现一次被动式 <code>syödään</code>，语言层次立刻上一个档。",
            )
        ),
        checklist=(
            h2("考前总清单")
            + h3("两天复习路线")
            + st(
                "第一天：时间表（四季 / 月份 / 星期 / 钟点）默写三遍",
                "第一天：十个动词 × 12 形式，逐格核对弱化",
                "第二天：复习卷三题重做，错题写原因",
                "第二天：录音两分钟，回听标出三处错误",
                "考前 1 小时：只看错误总表与时间表",
            )
            + h3("交卷前五分钟自检")
            + st(
                "每个名词：格对不对？要不要弱化？",
                "每个动词：人称词尾、否定词、KPT 三项都过了吗？",
                "每个宾语：否定 / 数词 / 不可数 → 部分格？",
                "每个时间词：-na / -ssa / -lla / -lta 选对了吗？",
            )
        ),
        mapping=tb(
            ("源文件", "位置", "覆盖知识点"),
            (
                "13_Kertaa/1_Kertaus FI2.pdf",
                "p1–p3",
                "时间表达自测、日常话题问答（爱好 / 计划 / 饮食 / 过敏）、属格与部分格练习、PILATA 变位、短文填空",
            ),
            (
                "13_Kertaa/2_Vastaukset, Kertaus FI2.pdf",
                "p1–p3",
                "全部标准答案：七个时间答句、属格六词与例句、六个部分格、PILATA 12 形式、短文十个动词",
            ),
            (
                "13_Kertaa/4_KUUNTELE Milloin juna lähtee_.html",
                "全篇 6 题",
                "数字时间与数字/传统混合听力题型、车站与巴士场景词汇",
            ),
            (
                "13_Kertaa/5_PartitiiviLauseita.docx",
                "全篇 11 组",
                "造句题型要求：语序不变、动词变位、宾语部分格",
            ),
            (
                "13_Kertaa/6_PartitiiviLauseitaVASTAUKSET.docx",
                "全篇 11 句",
                "11 句标准答案（本讲义第 10 讲已逐句采用）",
            ),
            (
                "14_Kokeet_Exams/1_Finnish 2, presentation, korjattu.docx",
                "全篇",
                "演示任务要求：5–10 分钟、必须芬兰语、1–5 分、六组主题问句",
            ),
            (
                "14_Kokeet_Exams/2_Esimerkki, vappu.pdf",
                "p2–p5",
                "范例演示结构与句型：Milloin / Missä / Kenen kanssa / Mitä syödään、被动式、对比段",
            ),
            (
                "（补充）",
                "12.8",
                "四类超纲形式的构成说明属识别性拓展，原文只出现用法例句，未给变位表",
            ),
            ("（跳过）", "—", "复习卷空白答题行、演示幻灯片中的图片与链接"),
        ),
    )
)

emit(
    cid="34583",
    order=9,
    name_zh="K200DJ99 芬兰语2",
    name_en="Finnish 2",
    source_dir="K200DJ99 芬兰语2",
    summary="LUT 芬兰语第二级课程，按 11 次课推进：从自我介绍与数字起步，依次覆盖现在时与六类动词、辅音交替、时间表达、将来表达、爱好与食物词汇，最后落到属格与部分格两大格系统及餐厅、节日等真实场景；考核为变位填空、格转换、造句、听力与 5–10 分钟芬兰语演示。",
    lectures=LEC,
)
