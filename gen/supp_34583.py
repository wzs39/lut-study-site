# -*- coding: utf-8 -*-
"""芬兰语 2 · 补充讲：食物访谈作业（只追加 1 讲，不改动已有讲次）"""

import os
import sys
import json
import io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, code, chips  # noqa: E402

CID = "34583"
PATH = os.path.join(SITE, "content", CID + ".json")

data = json.load(io.open(PATH, encoding="utf-8"))

overview = (
    h2("本节定位")
    + p(
        "第 9 讲讲「喜好、餐食与餐厅」，这一讲把配套的真实作业 <b>FI2, haastattelu ruoka</b>（食物访谈）拆开："
        "它表面上只是「去问六个人三个问题」，实际上一次练了<b>过去时、部分格宾语、变成格、所有格</b>四套语法。"
    )
    + p("学完本节你应当能够：")
    + ck(
        "用芬兰语完整走完一次访谈：开场、提问、追问、致谢",
        "正确说出「我今天早饭吃了……」并解释为什么用部分格",
        "把 aamiainen 变成 aamiaiseksi，说明 -ksi 的作用",
        "把六份回答汇总成一段口头或书面报告",
        "在访谈中听懂并记录人名、食物名与喜好表达",
    )
    + p(
        "与前后讲的衔接：第 8 讲食物词汇 + 第 10 讲部分格 + 第 11 讲喜好表达，在本讲合流；作业里的句式也是考试口试的模板。"
    )
)

detail = (
    h3("1. 作业原文与任务结构")
    + p("原文只有四行，但每一行都含语法点：")
    + p(
        "<code>Haastattele kuutta ihmistä, käytä kysymyksiä alla.</code>（访谈六个人，使用下面的问题。）"
    )
    + p(
        "<code>Aloita: ”Anteeksi, saanko kysyä kolme kysymystä? Tehtävä on minun suomen kurssille.”</code>"
    )
    + p(
        "<code>Kuka sinä olet? | Mitä söit tänään aamiaiseksi? | Mikä on sinun lempiruoka?</code>"
    )
    + tb(
        ("要求", "含义", "考察点"),
        ("kuutta ihmistä", "六个人（partitive）", "数字后的名词用 partitive"),
        (
            "käytä kysymyksiä",
            "使用这些问题（partitive 复数）",
            "käytä 是 käyttää 的命令式",
        ),
        ("kolme kysymystä", "三个问题", "数字 + partitive 单数"),
        ("Tehtävä on … kurssille", "作业是……课程的", "-lle 表示「为……而做」"),
    )
    + h3("2. 开场句逐词拆解")
    + tb(
        ("词/短语", "原形", "语法说明"),
        ("Anteeksi", "anteeksi", "对不起 / 打扰一下，固定词"),
        ("saanko", "saada（得到、可以）", "第一人称疑问式 -nko：saanko = 我可以……吗"),
        ("kysyä", "kysyä（问）", "saada 后接动词原形（不定式）"),
        ("kolme", "kolme（三）", "数词，后面名词用 partitive 单数"),
        ("kysymystä", "kysymys（问题）", "partitive：kysymys → kysymystä"),
        ("Tehtävä", "tehtävä（任务、作业）", "由 tehdä 派生的 -va 名词"),
        ("on", "olla", "系动词"),
        ("minun", "minä（属格）", "「我的」"),
        ("suomen", "suomi（属格）", "suomen kurssi = 芬兰语课程"),
        ("kurssille", "kurssi（向格 -lle）", "为课程而做 → 用 -lle"),
    )
    + cal(
        "tip",
        "一句话记住",
        "「May I ask three questions?」= <code>Saanko kysyä kolme kysymystä?</code>；"
        "「for my Finnish course」= <code>minun suomen kurssille</code>，两个格一个都不能省。",
    )
    + h3("3. 问题一：Kuka sinä olet?（你是谁）")
    + p(
        "这是身份问句，回答用 <code>Minä olen + 名字/身份</code>。注意 <code>kuka</code> 问人，<code>mikä</code> 问物；"
        "问名字也可以说 <code>Mikä sinun nimesi on?</code>（你的名字是什么），因为名字被视为「物」。"
    )
    + tb(
        ("问", "答", "说明"),
        ("Kuka sinä olet?", "Minä olen Zishuo.", "直接给名字"),
        ("Kuka sinä olet?", "Minä olen opiskelija.", "给身份"),
        (
            "Mikä sinun nimesi on?",
            "Minun nimeni on Zishuo.",
            "名字用 mikä + 所有格后缀",
        ),
    )
    + cal(
        "warn",
        "易错",
        "<code>Minä olen opiskelija</code> 中 opiskelija 是主格（表语），不要加 partitive；"
        "只有在「我正在学某专业」时才用 <code>Opiskelen + partitive</code>。",
    )
    + h3("4. 问题二：Mitä söit tänään aamiaiseksi?（你今天早饭吃了什么）")
    + p("这一句是整份作业的语法核心，含三件事：")
    + st(
        "<b>过去时</b>：<code>syödä</code>（吃）的过去式是 <code>söin, söit, söi, söimme, söitte, söivät</code>。"
        "问「你吃了」用 <code>söit</code>。",
        "<b>部分格宾语</b>：<code>Mitä</code> 本身就是 <code>mikä</code> 的 partitive；回答时食物若是不可数或「吃了一部分」，"
        "也要用 partitive：<code>Minä söin puuroa.</code>（我吃了（一些）粥）。",
        "<b>变成格 -ksi</b>：<code>aamiainen → aamiaiseksi</code>，表示「当作早饭」。"
        "同理 <code>lounaaksi</code>（当作午饭）、<code>päivälliseksi</code>（当作晚饭）。",
    )
    + tb(
        ("问句成分", "原形", "作用"),
        ("Mitä", "mikä", "什么（partitive，因为吃的是「部分」）"),
        ("söit", "syödä", "第二人称单数过去时"),
        ("tänään", "tänään", "今天（时间副词，不变格）"),
        ("aamiaiseksi", "aamiainen", "-ksi：作为早饭"),
    )
    + p("典型回答：")
    + ul(
        "<code>Minä söin aamiaiseksi puuroa ja join kahvia.</code>（早饭我吃了粥、喝了咖啡。）",
        "<code>Minä söin vain leipää ja juustoa.</code>（我只吃了面包和奶酪。）",
        "<code>En syönyt aamiaista.</code>（我没吃早饭。）——否定句里宾语也用 partitive。",
    )
    + cal(
        "warn",
        "易错",
        "否定句 <code>En syönyt</code> 用动词过去分词 <code>syönyt</code>，不是 <code>söin</code>；"
        "这是否定过去时的固定搭配（en + 过去分词）。",
    )
    + h3("5. 问题三：Mikä on sinun lempiruoka?（你最喜欢的食物是什么）")
    + p(
        "<code>lempi-</code> 是「最喜欢的」前缀，可拼在任何名词前：<code>lempiruoka</code>（最喜欢的食物）、"
        "<code>lempielokuva</code>（最喜欢的电影）、<code>lempiväri</code>（最喜欢的颜色）。"
    )
    + p("回答两种写法：")
    + tb(
        ("写法", "例句", "结构"),
        ("主语式", "Minun lempiruokani on sushi.", "所有格后缀 -ni 加在 lempiruoka 后"),
        ("话题式", "Lempiruokani on sushi.", "省略 minun，更自然"),
        (
            "口语式",
            "Mun lemppari on sushi.",
            "puhekieli：minun → mun，lempi → lemppari",
        ),
    )
    + p(
        "若想说「我喜欢吃……」，用 <code>Tykkään + partitive</code>：<code>Tykkään sushista.</code>"
        "（注意 tykätä 要求 elative -sta/-stä，不是 partitive）。"
    )
    + h3("6. 食物与餐次词汇（访谈必备）")
    + tb(
        ("Suomi", "中文", "English"),
        ("aamiainen", "早餐", "breakfast"),
        ("lounas", "午餐", "lunch"),
        ("päivällinen", "晚餐", "dinner"),
        ("välipala", "加餐 / 零食", "snack"),
        ("ruoka", "食物", "food"),
        ("juoma", "饮料", "drink"),
        ("puuro", "粥", "porridge"),
        ("leipä", "面包", "bread"),
        ("juusto", "奶酪", "cheese"),
        ("kahvi", "咖啡", "coffee"),
        ("tee", "茶", "tea"),
        ("maito", "牛奶", "milk"),
        ("hedelmä", "水果", "fruit"),
        ("vihannes", "蔬菜", "vegetable"),
        ("liha", "肉", "meat"),
        ("kala", "鱼", "fish"),
        ("kana", "鸡肉", "chicken"),
        ("riisi", "米饭", "rice"),
        ("pasta", "意面", "pasta"),
        ("keitto", "汤", "soup"),
        ("salaatti", "沙拉", "salad"),
        ("vesi", "水", "water"),
    )
    + cal(
        "tip",
        "格的变化",
        "这些食物多是不可数名词，作宾语时用 partitive："
        "<code>syön leipää</code>、<code>juon kahvia</code>、<code>ostan maitoa</code>。"
        "可数的单个食物才用主格：<code>syön omenan</code>（吃一个苹果）。",
    )
    + h3("7. 访谈流程与记录表")
    + p("作业要求访谈六个人，并把回答填进表格。表格三列正好对应三个问题：")
    + tb(
        (
            "Kuka sinä olet?",
            "Mitä söit tänään aamiaiseksi?",
            "Mikä on sinun lempiruoka?",
        ),
        ("Anna", "puuroa ja kahvia", "lohikeitto"),
        ("Mikko", "leipää ja juustoa", "pizza"),
        ("Liisa", "en syönyt aamiaista", "sushi"),
    )
    + p(
        "记录时只写关键词即可（puuroa、kahvia），汇报时再补成完整句。这样既快又不会因为拼写卡住而冷场。"
    )
    + p(
        "访谈礼仪（口语考试也会看）：先眼神接触说 <code>Anteeksi</code>，说明来意，问完说 <code>Kiitos paljon!</code>，"
        "若对方反问，用 <code>Minä opiskelen suomea.</code> 回答。"
    )
    + h3("8. 从表格到报告：Haastattelun tulokset")
    + p("访谈后通常要口头汇报或写一段总结。结构是「人数 → 多数/少数 → 有趣发现」：")
    + ul(
        "<code>Minä haastattelin kuusi ihmistä.</code>（我访谈了六个人。）",
        "<code>Suurin osa söi aamiaiseksi puuroa tai leipää.</code>（多数人早饭吃粥或面包。）",
        "<code>Kaksi ihmistä ei syönyt aamiaista.</code>（两个人没吃早饭。）",
        "<code>Suosituin lempiruoka oli sushi.</code>（最受欢迎的喜欢的食物是寿司。）",
    )
    + p(
        "注意 <code>suurin osa</code>（大多数）作主语时动词用第三人称单数；<code>kaksi ihmistä</code> 也用单数动词，"
        "因为芬兰语数词短语整体视为单数。"
    )
    + cal(
        "warn",
        "易错",
        "「两个人没吃」不能说 <code>Kaksi ihmistä eivät syöneet</code>（口语可听到，但标准写法是 "
        "<code>Kaksi ihmistä ei syönyt</code>）。考试写作用单数。",
    )
    + h3("9. 与「爱好访谈」的对照")
    + p(
        "同一门课还有一份 <code>FI2, haastattelu harrastukset</code>（爱好访谈），结构完全一样："
        "开场句相同，问题换成 <code>Mitä sinä harrastat?</code>（你有什么爱好）、<code>Milloin sinä harrastat?</code>（什么时候做）、"
        "<code>Miksi sinä harrastat sitä?</code>（为什么做）。"
    )
    + p(
        "把两份作业放在一起看，会发现模板是固定的：<b>开场 → 三个疑问词问句 → 记录 → 汇报</b>。"
        "掌握这个模板，口试任何主题都能套。"
    )
)

kws = tb(
    ("Suomi / English", "中文", "说明 / 例句"),
    ("haastattelu / interview", "访谈", "Haastattele kuutta ihmistä."),
    ("aamiainen / breakfast", "早餐", "aamiaiseksi（作为早饭）"),
    ("lounas / lunch", "午餐", "lounaaksi"),
    ("päivällinen / dinner", "晚餐", "päivälliseksi"),
    ("lempiruoka / favourite food", "最喜欢的食物", "Minun lempiruokani on sushi."),
    ("syödä / to eat", "吃", "söin, söit, söi"),
    ("juoda / to drink", "喝", "join, joit, joi"),
    ("partitiivi / partitive", "部分格", "söin puuroa"),
    ("translatiivi / translative", "变成格", "aamiaiseksi"),
    ("kielto / negation", "否定", "en syönyt"),
    ("tykätä / to like", "喜欢", "Tykkään sushista."),
    ("harrastus / hobby", "爱好", "Mitä sinä harrastat?"),
    ("suurin osa / most", "大多数", "Suurin osa söi puuroa."),
    ("haastatella / to interview", "访谈（动词）", "Minä haastattelin kuusi ihmistä."),
    ("puhekieli / colloquial Finnish", "口语", "mun, sä, lemppari"),
    ("tehtävä / assignment", "作业", "Tehtävä on minun kurssille."),
)

examples = (
    h2("例题 1：完整访谈对话")
    + qa(
        "把三个问题串成一段真实对话，并标出每句的语法点。",
        p(
            "<b>A：</b><code>Anteeksi, saanko kysyä kolme kysymystä? Tehtävä on minun suomen kurssille.</code>"
            "（saanko = saada + -nko；kolme kysymystä = 数词 + partitive）"
        )
        + p("<b>B：</b><code>Joo, tietenkin.</code>（当然可以。）")
        + p(
            "<b>A：</b><code>Kuka sinä olet?</code> <b>B：</b><code>Minä olen Anna.</code>"
        )
        + p(
            "<b>A：</b><code>Mitä söit tänään aamiaiseksi?</code> <b>B：</b><code>Minä söin puuroa ja join kahvia.</code>"
            "（söit 过去时；puuroa、kahvia 部分格）"
        )
        + p(
            "<b>A：</b><code>Mikä on sinun lempiruoka?</code> <b>B：</b><code>Minun lempiruokani on lohikeitto.</code>"
            "（-ni 所有格后缀）"
        )
        + p("<b>A：</b><code>Kiitos paljon!</code>"),
    )
    + h2("例题 2：改正三个错句")
    + qa(
        "<code>Mitä sinä syöt tänään aamiaiseksi?</code> / <code>Minä söin puuro.</code> / <code>Minun lempiruoka on sushi.</code>",
        p(
            "第一句问的是「今天早饭吃了什么」，已经发生，要用过去时 <code>söit</code>，不是现在时 <code>syöt</code>。"
        )
        + p(
            "第二句 <code>puuro</code> 是不可数食物，作宾语要用 partitive：<code>puuroa</code>。"
        )
        + p(
            "第三句缺所有格后缀：<code>Minun lempiruokani on sushi.</code>（或去掉 minun：<code>Lempiruokani on sushi.</code>）"
        ),
    )
    + h2("例题 3：汇报六人结果")
    + qa(
        "六人中四人早饭吃粥，两人没吃；最喜欢的食物是披萨。写两句汇报。",
        p("<code>Suurin osa (neljä ihmistä) söi aamiaiseksi puuroa.</code>")
        + p(
            "<code>Kaksi ihmistä ei syönyt aamiaista, ja suosituin lempiruoka oli pizza.</code>"
        )
        + p(
            "要点：<code>suurin osa</code> 与数词短语都配单数动词；<code>suosituin</code> 是 superlative（最受欢迎的）。"
        ),
    )
)

practice = (
    h2("练习")
    + p("1. 变位：syödä 与 juoda 的过去时六个人称。")
    + det(
        "答案与思路",
        p(
            "<code>söin, söit, söi, söimme, söitte, söivät</code>；"
            "<code>join, joit, joi, joimme, joitte, joivat</code>。"
        ),
    )
    + p("2. 把 aamiainen、lounas、päivällinen 变成「作为……餐」的形式。")
    + det(
        "答案与思路",
        p(
            "<code>aamiaiseksi, lounaaksi, päivälliseksi</code>；-nen 词尾变 -se-，其余加 -ksi。"
        ),
    )
    + p("3. 翻译：今天早饭我喝了一杯咖啡，吃了一个苹果。")
    + det(
        "答案与思路",
        p(
            "<code>Tänään minä join aamiaiseksi kahvia ja söin omenan.</code>"
            "咖啡不可数用 partitive，苹果可数用主格宾格（omenan）。"
        ),
    )
    + p("4. 否定改写：<code>Minä söin aamiaista.</code> → 否定句。")
    + det(
        "答案与思路",
        p(
            "<code>Minä en syönyt aamiaista.</code>（en + 过去分词 syönyt，宾语仍 partitive）。"
        ),
    )
    + p("5. 写一句汇报：三个人喜欢鱼，两个人喜欢肉，一个人喜欢沙拉。")
    + det(
        "答案与思路",
        p(
            "<code>Kolme ihmistä pitää kalasta, kaksi lihasta ja yksi salaatista.</code>"
            "注意 pitää 要求 elative -sta/-stä。"
        ),
    )
)

exam = (
    h2("考点与难点")
    + cal(
        "exam",
        "必考",
        ul(
            "syödä / juoda 的过去时变位",
            "aamiainen → aamiaiseksi（-ksi 变成格）",
            "食物宾语的 partitive（puuroa、kahvia、leipää）",
            "否定过去时 en + 过去分词",
            "lempiruoka 的所有格写法",
        ),
    )
    + cal(
        "warn",
        "易错",
        ul(
            "现在时与过去时混用（söit vs syöt）",
            "不可数名词误用主格（söin puuro）",
            "否定句仍用 söin（应为 en syönyt）",
            "数词短语配复数动词（应为单数）",
            "tykätä / pitää 后误用 partitive（应为 elative）",
        ),
    )
    + cal(
        "tip",
        "进阶",
        p(
            "能区分 <code>syön omenan</code>（吃一整个苹果）与 <code>syön omenaa</code>（吃苹果，一部分），"
            "并解释「部分格表示动作未完成或不指整个对象」——这是口试拿高分的关键。"
        ),
    )
)

checklist = h2("方法清单") + st(
    "开场三件套：Anteeksi + saanko kysyä + 说明来意",
    "问句用疑问词开头，动词放句末（Kuka sinä olet?）",
    "时间词 tänään 放动词后，不需变格",
    "食物宾语先判断可数/不可数，再选主格或 partitive",
    "报告前先数人数，再写「多数/少数」句，动词用单数",
    "交作业前核对每个 ä/ö 与格尾（-ksi / -ssa / -sta）",
)

mapping = (
    h2("源文件对应")
    + tb(
        ("补充文件", "位置", "覆盖内容"),
        (
            "FI2, haastattelu ruoka.docx",
            "Tunti 9",
            "第 1–7 节：任务要求、三个问题、词汇与记录表",
        ),
        (
            "FI2, haastattelu harrastukset.docx",
            "Tunti 6",
            "第 9 节：同模板的爱好访谈对照",
        ),
        ("Haastattelun tulokset.html", "Tunti 6", "第 8 节：汇报结构与句型"),
        ("菜单与食物图片", "Tunti 9", "仅用于确认词汇范围，无可抽取文字"),
        ("练习空白表格", "Tunti 9", "记录表格式，不构成知识点"),
    )
    + p(
        "<b>重复副本</b>：<code>FI2, haastattelu ruoka.docx</code> 与 <code>1_FI2, haastattelu ruoka.docx</code> 内容一致，按 md5 去重。"
        "<b>拓展</b>：第 6 节词汇表与第 8 节汇报句型为补充背景，不改变作业原有要求。"
    )
)

lec = L(
    slug="supp-interview-task",
    tzh="补充 · 食物访谈作业（haastattelu ruoka）",
    ten="Food Interview Assignment",
    keywords=[
        "haastattelu",
        "aamiainen",
        "lempiruoka",
        "translatiivi",
        "partitiivi",
        "syödä",
        "negation",
        "tykätä",
        "suurin osa",
        "puhekieli",
    ],
    files=[
        "FI2, haastattelu ruoka.docx",
        "FI2, haastattelu harrastukset.docx",
        "Haastattelun tulokset.html",
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
