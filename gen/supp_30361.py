# -*- coding: utf-8 -*-
"""30361 软件工程基础 · 补遗一讲：项目文档模板、Honor Code 与案例讨论题"""

import os, sys, json, io

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, pre, code, chips

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "30361"
PATH = os.path.join(SITE, "content", CID + ".json")
kw = K  # 术语表：10–16 条，列数与 genlib.K 一致


def qa(title, *bodies):
    """本脚本内的 qa：允许一次传多个段落，内部拼成一个 body。"""
    from genlib import qa as _qa

    return _qa(title, chr(10).join(str(b) for b in bodies))


LEC = L(
    slug="supp-project-docs",
    tzh="补遗 · 项目文档模板、Honor Code 与案例讨论题",
    ten="Project Templates, the Honor Code, and the Case Discussion Questions",
    keywords=[
        "project proposal",
        "status report",
        "stakeholder",
        "user group",
        "reflection",
        "iteration",
        "honor code",
        "plagiarism",
        "academic integrity",
        "case study method",
        "waterfall to agile",
        "code of conduct",
        "peer review",
    ],
    files=[
        "Project Proposal Template.docx",
        "Project Status Report Template.docx",
        "Project Proposal Ventura.pdf",
        "Ventura status report.pdf",
        "Honor code.html",
        "Feedback comments.html",
        "Online text.html",
        "Week 1 Exercise Sessions.html",
        "Week 3 Exercise Sessions.html",
        "Week 4 Exercise Sessions.html",
        "Week 5 Exercise Sessions.html",
        "Week 10 Case Study.html",
        "Week 11 Case Study.html",
        "Week 12 Case Study.html",
    ],
    # ------------------------------------------------------------------ overview
    overview="\n".join(
        [
            h2("本节定位"),
            p(
                "前 13 讲把 SDLC 模型、过程、需求、建模、架构、测试、演化、项目管理、质量与配置管理都讲完了，"
                "也讲过案例研究（IBM、Sasken、EXCEED、Catalise）。但课程项目这条线一直缺三块："
                "<b>文档模板</b>（提案与状态报告的章节结构与每节要回答的问题）、"
                "<b>两份真实范例</b>（Ventura 的提案与状态报告，以及助教给它的反馈）、"
                "<b>规则层</b>（Honor Code 与各周习题课的案例讨论安排）。"
            ),
            p(
                "这三块决定的是「分数怎么拿」而不是「概念懂不懂」：同样的知识，写进模板的对应小节、"
                "按 Honor Code 的口径独立完成、在案例讨论里讲出有证据的立场，分数才会到位。"
                "本讲把它们逐条拆开，并把范例的优点与问题都点出来——范例是用来学的，不是用来抄的。"
            ),
            p("学完本讲你能够："),
            ck(
                "能够默写 Proposal 与 Status Report 的章节顺序，并说出每一节要回答哪几个问题；",
                "能够把「利益相关者」与「用户组」分开写，各给 5–10 条并说明为什么不能复用同一批描述；",
                "能够按「日期 / 动机 / 描述 / 影响」四要素写一条需求变更记录；",
                "能够指出 Ventura 两份文档里哪些地方做得好、哪些地方会被扣分（含原文自身的编号与日期不一致）；",
                "能够说出 Honor Code 的五条落地要求、七类违规与两条后果；",
                "能够把六次案例讨论的题目归到「过程模型 / 质量诊断 / 分布式协作 / 伦理 / 需求对齐」五类问题上。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ detail
    detail="\n".join(
        [
            h2("一、两份模板：章节结构与每节要回答的问题"),
            p(
                "模板不是格式装饰，它其实是评分清单的骨架：评审按节找答案，缺一节就等于缺一块分。"
                "两份模板的封面字段完全一样：学校与学院（LUT School of Engineering Science）、课程名与编号"
                "（模板上印的是 CT60A4002 Software Engineering）、文档类型（Project work: Group Project Proposal / "
                "Group Project Status Report）、学期（模板印 Fall 2023）、应用名（Application X）、日期、"
                "组名或组号、作者列表（学号、姓名、邮箱）。"
            ),
            h3("1.1 Proposal：四节，一节一个问题组"),
            p(
                "目录只有四节：1 Introduction、2 Customer Needs、3 Team、4 References。"
                "节数少，但每节下面挂着若干必答问题，模板是把问题直接印在正文位置上的，回答时逐条对应即可。"
            ),
            ul(
                "<b>Introduction</b>：在做什么应用？它长什么样？为什么做、满足什么需求？新在哪里？"
                "项目的商业目标与其他目标可能是什么？",
                "<b>Customer Needs → Stakeholders</b>：团队之外的<b>主要客户</b>是谁？"
                "次级利益相关者有哪些？他们各自想要什么、为什么想要？",
                "<b>Customer Needs → Needs</b>：选了哪个客户问题来解决？应用提供什么用户收益？"
                "这个收益如何支撑客户期望的整体体验？你怎么知道客户真的得到了这个收益？",
                "<b>Team</b>：成员的背景？有没有与软件开发相关的实习或工作经历？"
                "每个人在这个项目里计划承担什么角色？",
                "<b>References</b>：项目里用到的参考文献列表。",
            ),
            p(
                "这一节的结构值得注意：模板把「Stakeholders」和「Needs」分成两个小标题，"
                "而不是笼统写「客户需求」。前者问「谁在乎」，后者问「解决什么、给谁什么好处、怎么验证」。"
                "两份 Ventura 文档在这两个小标题下的写法差异，正好对应评分反馈里被扣分的那一项（见第二节）。"
            ),
            h3("1.2 Status Report：七节加一个附录"),
            p(
                "目录：1 Introduction、2 Project Goals、3 Stakeholders、4 User Groups、5 Application Description、"
                "6 Team、7 References，外加 Appendix 1 Reflection。相比提案，多了 Project Goals、User Groups、"
                "Application Description 三节，并要求把 Goals、Stakeholders、User Groups 写成<b>表格</b>。"
            ),
            ul(
                "<b>1 Introduction</b> 分两块：Overview（与提案同样的四个问题，外加「描述客户期望的整体体验」）"
                "与 Project Status（这一迭代原计划做什么、实际完成了什么、相对提案有哪些重大变更——"
                "每条变更要给出<b>日期、动机、描述、影响</b>）；",
                "<b>2 Project Goals</b>：商业目标与其他目标列进表，可加一段引言；要求「像真实项目那样评估目标」；",
                "<b>3 Stakeholders</b>：写明有哪些利益相关者、各自角色（客户、用户、客户方的技术人员的等），"
                "要求识别 <b>5–10 个</b>；",
                "<b>4 User Groups</b>：识别不同用户组并描述它们对应用的需求与要求，同样 <b>5–10 个</b>；",
                "<b>5 Application Description</b>：介绍应用与主要挑战、概括设计理由、简述系统的外部交互；",
                "<b>6 Team</b>：背景（含「团队里有人做过类似的东西吗」）、角色（本迭代各人担任什么、各自贡献了什么）；",
                "<b>7 References</b>：参考文献；",
                "<b>Appendix 1 Reflection</b>：什么做得好？什么不好？没达成的目标卡在哪？怎么克服？下一迭代打算改什么？",
            ),
            p("模板还给三张表的表头与示例行，照抄表头就不会漏字段："),
            tb(
                ("表", "列", "模板示例行"),
                (
                    "Goals",
                    "ID ｜ Date ｜ Goal ｜ Description of the goal ｜ Notes",
                    "Example 01 ｜ 1.10.2021 ｜ Profits ｜ 靠高级会员付费与应用内广告带来利润 ｜ 第一年利润目标 40000€",
                ),
                (
                    "Stakeholders",
                    "ID ｜ Date ｜ Stakeholder ｜ Description and role of the stakeholder ｜ Notes",
                    "E 01 ｜ 1.11.2021 ｜ 应用的使用者 ｜ 日常生活中使用这个应用 ｜ 重要群体",
                ),
                (
                    "User Groups",
                    "ID ｜ Date ｜ User group ｜ Description and role ｜ Notes",
                    "E 01 ｜ 1.11.2021 ｜ 高级用户 ｜ 付费后获得额外权益 ｜ 3,99 €/月；E 02 ｜ 学生 ｜ 用于与同伴沟通",
                ),
            ),
            cal(
                "tip",
                "模板里的两个提示很关键",
                "① Goals 表要求「evaluate your goals, as you would do in a real project」——写目标时要带可检验的判据（时间、数值），"
                "不是写成口号；② Stakeholders 与 User Groups 都用「E 01」式编号，说明这两张表是<b>平行</b>的两套清单，不是同一批人写两遍。",
            ),
            h3("1.3 模板与 Final Report 的关系"),
            p(
                "<code>Project Final Report</code> 目录下放的仍是 Proposal 与 Status Report 两份模板（同一文件），"
                "外加一份 Final Report Template；前者已在前 13 讲引用，本讲只补尚未引用的 Proposal 与 Status Report 两份。"
                "这说明三份文档共用同一套封面与引用节，写作时可以把 Proposal 的 Introduction、Team、References 直接延续下来，"
                "只需要把状态更新到最新迭代。"
            ),
            h2("二、Ventura 范例：值得学的地方与被扣分的地方"),
            p(
                "<code>Project Proposal Ventura.pdf</code>（8 页）与 <code>Ventura status report.pdf</code>（12 页）"
                "是第 1 组 2026 年秋季的真实提交，随状态报告一起放出了助教的 <code>Feedback comments</code>。"
                "这样一组「文档 + 反馈」是整门课里最有用的材料：它把评分标准具体化成了几条可对照的意见。"
            ),
            h3("2.1 提案做对了什么"),
            ul(
                "<b>「新在哪里」写成了四条可对照的差异</b>：视频即路演（不用 30 页没人读的 deck）、"
                "档案是活的（视频 + 创始人履历 + 实时进展放在一页，随公司成长更新）、不需要熟人引荐（让投资人看到自己圈子之外的创始人）、"
                "一个产品覆盖完整漏斗（Discover → Watch → Engage → Close 在一处完成）。四条都是可验证的产品差异，不是形容词。",
                "<b>利益相关者分了五类并逐类说明「想要什么、为什么」</b>：投资人、导师与创业教练、加速器与孵化器、"
                "大学与创业组织、平台管理员。每一类的「为什么」都落回它的工作场景，而不是重复「他们想用这个应用」。",
                "<b>团队分节写到人</b>：五人各自的专业与经验，再逐人写「计划承担的角色」（设计/UML/需求、演示/UI/计划、"
                "需求分析与文档、需求规格与计划、演示与客户满意度）。这让评审能判断分工是否覆盖了全部工作。",
            ),
            h3("2.2 提案自身的问题"),
            ul(
                "封面课程编号是 <b>CT60A4002</b>，而同一项目的状态报告封面写 <b>CT60A4050</b>；同一课程的两份文档编号不一致，"
                "读者无法判断哪一个是本课程。",
                "日期写作 <b>10/13/2026</b>：按芬兰习惯 <code>DD/MM/YYYY</code> 读是无效日期（没有 13 月），"
                "只能按美式 <code>MM/DD/YYYY</code> 理解；而状态报告写的是 12/11/2026，两份文档的日期体系不统一。",
                "References 只有一条（产品官网），对一个讲了市场、竞品与商业目标的项目来说明显偏少——"
                "反馈里也专门提醒「In the final project don't forget to include more references」。",
                "Customer Needs 把模板的问题原样当小标题，其中「How will the benefit support the customer's desired overall "
                "experience?」出现在答句之前、与上下文断开，看起来像漏排的小标题。",
            ),
            h3("2.3 状态报告做对了什么"),
            ul(
                "<b>变更表四要素齐全</b>：两处变更都写了日期、动机、描述与影响。"
                "「Investment Ask Filter」22/10/2026，动机是让投资人按愿意投的金额筛，"
                "影响写明「下一迭代要为此多分配时间」；「Share Feature」01/11/2026，动机是让投资人把路演转给同行，"
                "影响写明「属于 Feed 标签页，需在第二迭代落地」。这正是模板要求的写法。",
                "<b>Goals 表带数值目标</b>：四行 LE01–LE04，从「上线时 1500 个创业公司与投资人注册」到"
                "「扩张到新客户群」，每行附利润目标区间（25 000€ 起，逐级到 5M–10M€），符合「像真实项目那样评估目标」。",
                "<b>Stakeholders 与 User Groups 各自成表且条目够数</b>：利益相关者 S01–S09，用户组 E01–E06，"
                "数量都在模板要求的 5–10 区间内，且用户组逐条写了「他们需要什么功能」（例如加速器需要 Saved 区快速看进展）。",
            ),
            h3("2.4 状态报告的问题"),
            ul(
                "<b>机器翻译痕迹导致语义不通</b>：Application Description 里出现「The Russian news is to reduce screening "
                "friction」、「our minpages」、「ammunition the experience」这类句子，母语读者读不出原意。"
                "这是最容易被判「表达不清」的一类问题，且与内容质量无关，纯属交付前没过一遍语言。",
                "<b>Goals 四行的 Date 全是 14.11.2026</b>，而 14.11.2026 正是状态报告的提交日期。"
                "反馈直接点了这一点：表里的日期应当是<b>未来的目标截止日</b>，不是报告写完的那一天。",
                "<b>Stakeholders 与 User Groups 的内容被复用</b>：反馈原文「User groups and stakeholders are also actually "
                "different, watch out on that detail in the final project. They've been reused which is not accurate.」，"
                "并因此只给了 0.5/1。",
                "<b>目录把作者名写进标题</b>（1 INTRODUCTION (Rucha) 等），属于内部协作痕迹没有清掉；"
                "另有 Develope、Spesifying 这类拼写错误。",
                "<b>Reflection 泛泛且自相矛盾</b>：第一问答「我们团队合作得很好、彼此沟通」，第三问却把未达成的目标归因于"
                "「misunderstandings and poor communication」。反馈的评语是「answers to Appendix 1 are generic, and "
                "contradicting」，给了 0.75/1.5。",
            ),
            h3("2.5 从反馈反推评分关注点"),
            p(
                "<code>Feedback comments.html</code> 只有五段，但每一段都能反推出一条评分关注点："
            ),
            tb(
                ("反馈原文要点", "扣分", "说明什么"),
                (
                    "与竞争者比较不足",
                    "0.5/1",
                    "「新在哪里」必须对着竞品说，不能只描述自己",
                ),
                (
                    "用户组与利益相关者被复用、区分不清",
                    "0.5/1",
                    "两张表是两套人：谁受影响 vs 谁使用",
                ),
                (
                    "Reflection 泛泛且自相矛盾",
                    "0.75/1.5",
                    "反思要具体到事件，且前后不能互相打脸",
                ),
                (
                    "Goals 表的日期用了提交日期",
                    "—（提示）",
                    "日期是目标截止日，不是写作日",
                ),
                (
                    "Application Description 与真实原型做得好",
                    "表扬",
                    "有可运行原型会显著加分",
                ),
                ("References 太少", "—（提示）", "最终报告要补文献"),
            ),
            p(
                "要注意反馈末尾那句括注：<b>「8.25/10 - this score is just for visual purposes and is not a part of grading」</b>。"
                "也就是说这个分数只是给学生看的参考，不计入正式评分；正式评分由助教按功能清单另行给出。"
                "读反馈时应该把注意力放在「哪一项为什么只给了一半分」，而不是那个总分。"
            ),
            h2("三、Honor Code：五条落地要求、七类违规、两条后果"),
            p(
                "<code>Honor code.html</code> 是课程要求所有人接受的学术诚信承诺，原文说明它是改编自斯坦福大学的版本。"
                "承诺本身只有两句，但落地条款才是可执行的规则。"
            ),
            p(
                "两条承诺：不在考试中给予或接受帮助；不在课堂作业、报告准备或任何被教师用作评分依据的工作中"
                "给予或接受未经允许的帮助。并且「每人要做好自己那一份，同时主动确保他人也遵守守则的精神与字面」。"
            ),
            p("落地五条（原文 In practice, this means that）："),
            ul(
                "所有作业必须自己完成，不得与他人合作或求助，除非<b>明确允许或要求</b>；",
                "必须阅读并理解学校的 AI 政策，或就其中不清楚的地方寻求澄清，并按政策规定<b>申报 AI 的使用</b>；",
                "必须自己写作业、自己做测验，在提交自己的答案之前不得与他人讨论；",
                "有些活动要求协作；若某任务需要小组完成，会单独说明；",
                "必须为使用的所有来源标注引用，<b>包括课程教材</b>。",
            ),
            p(
                "七类被认定为违规的行为（原文举例）：未经允许的合作；抄袭（plagiarism，定义为「使用他人的原创工作——"
                "无论是代码、公式、想法、语言、研究、策略、写作还是其他形式——而不给出合理恰当的出处或致谢」）；"
                "未经教师知情同意就修改并重新提交测验或考试以求重新评分；在带回家完成的考试中给予或接受未经允许的帮助；"
                "把别人的工作当成自己的；在「一个理性人应当知道该帮助不被允许」的情形下仍给予或接受帮助；"
                "抄别人的答卷或让别人抄自己的。"
            ),
            p(
                "两条后果：<b>课程不及格，并失去此前已获得的全部分数</b>；以及接受学校处理学术违规的官方机构所施加的"
                "一切处罚。注意第一条的措辞是「losing all points awarded so far」——不是这一项作业零分，而是整门课的分数清零。"
            ),
            cal(
                "warn",
                "AI 政策必须申报",
                "原文把「阅读并理解学校的 AI 政策、按规定申报使用」写成了硬性要求，原文还给出了学校 AI 政策页的入口。"
                "这与 30352 的 HowToUseAI 是同一件事的两面：那门课禁止用 AI 写最终解答，这门课要求申报使用。"
                "共同点是——用了就要说，不说就是违规。",
            ),
            h2("四、习题课与案例讨论：时间、方法与题目"),
            h3("4.1 三种周次形态"),
            p(
                "各周的 <code>Exercise Sessions</code> 页面并不都是同一种东西，混着看会误判："
            ),
            ul(
                "<b>第 1 周</b>是纯时间表页：给出四个时段（周一 14:00–16:00 线上；周三 10:00–26:00 在教室 M19_D247；"
                "周五 10:00–12:00 同教室；周五 12:00–14:00 在 Zoom），主题只有两项——项目启动（Project initiation）"
                "与示例项目（附 <code>Example_project1.pdf</code>）。注意「10:00–26:00」是原文的笔误，世上没有 26 点。",
                "<b>第 3、4、5 周</b>是「习题课 + 案例」：先说明本周用案例法，再给本周案例摘要与 3–7 个讨论题，"
                "并附该案例的 PDF；",
                "<b>第 10、11、12 周</b>换成 <code>Case Study</code> 页面，结构相同但案例更长、讨论题更偏决策。",
            ),
            h3("4.2 案例法三步"),
            p("原文对 Case Study Method 的解释在每周页面上都重复一遍，三步是固定的："),
            st(
                "案例阅读与准备（Case reading and preparation）：案例是对某位组织领导者所面对真实情境的详细描述，"
                "除背景信息外还含一个必须做出的关键决策；材料<b>故意不完整</b>，任务是分析信息并决定「你会怎么做」；",
                "小组案例讨论（Group case discussion）：课上把想法带到一个背景各异的小组里讨论，从别人的视角补自己的盲区；",
                "全班理解性讨论（Comprehension case discussion）：在小组之后与全班讨论最佳行动方案，"
                "要求积极倾听、站在案例主角的位置上说明理由。",
            ),
            p(
                "阅读指南八条（原文 Case reading guidelines），可压成四步执行：先读首尾两节锁定核心情境；"
                "快速扫其余小节与图表，知道信息在哪而不必记住每个细节；先看讨论题再带着问题做笔记；"
                "最后形成「有证据支撑的立场」——原文特意强调「there is usually no objectively correct answer to a case, "
                "and the best solution is the one with the strongest evidence to back it up」。"
            ),
            h3("4.3 六个案例与讨论题的主题"),
            tb(
                ("周", "案例", "讨论题在问什么"),
                (
                    "第 3 周",
                    "IBM：迭代式软件开发方法",
                    "关键需求在产品周期很晚才提出——团队能不能满足？该不该做？做了能不能不延期？",
                ),
                (
                    "第 4 周",
                    "Telerik：Scrums, Sprints, Spikes and Poker",
                    "组织文化的关键因素？敏捷是软件设计工具还是组织设计工具？员工需要什么技能？能否随规模持续？增长会带来什么挑战？",
                ),
                (
                    "第 5 周",
                    "Pearson SuccessMaker",
                    "五年路线图的挑战？开发方法如何影响对市场的响应？从瀑布转敏捷的收益与代价？什么情形适合哪种？该不该从 Scrum 转 Kanban？用什么度量？",
                ),
                (
                    "第 10 周",
                    "EXCEED：提升交付的生产率与可靠性",
                    "客户投诉的性质？先解决哪些问题？系统测试过程是否如所称受控？网络延迟是不是欠产的主因？",
                ),
                (
                    "第 11 周",
                    "Catalise：Move Fast, but without Bias",
                    "主角想坚持什么价值立场？各方各冒什么风险？利益相关者之间如何对齐？为修正算法偏见而推迟发布要付什么代价？",
                ),
                (
                    "第 12 周",
                    "Sasken：为先进移动市场开发产品",
                    "如何为海外市场做出功能完整的产品？如何在时间与质量间维持过程纪律？如何管理变化且不清晰的需求？如何满足挑剔客户的质量标准？分布式团队怎么沟通协调？",
                ),
            ),
            p("把这 18 个问题归一下类，会发现只有五种问法，考试与讨论都能套："),
            ol(
                "<b>过程模型选择</b>（瀑布 / 迭代 / 敏捷 / Scrum vs Kanban）：什么情形用哪种，切换的代价是什么；",
                "<b>质量与生产率诊断</b>（EXCEED）：投诉 → 数据 → 用质量工具（因果图、帕累托、控制图）找主因，而不是接受第一个解释；",
                "<b>分布式与跨文化协作</b>（Sasken）：时区、语言、需求在远方演化时的沟通机制；",
                "<b>伦理与偏见</b>（Catalise）：算法对群体不公平时，发布速度与责任怎么权衡；",
                "<b>需求与客户对齐</b>（IBM、Pearson）：交付的东西与客户想要的之间的落差怎么在过程中被发现。",
            ),
            h3("4.4 一份能拿分的讨论发言长什么样"),
            p(
                "按上面的三步与八条指南，发言的结构应当固定：先用一句话给出立场（「我会推迟两周而不是按期发布」），"
                "再用案例里的具体事实支撑（哪一页的哪个数据、哪个人物说过什么），"
                "然后主动说出反方最强的理由并回应它，最后给出可执行的下一步与判断成败的指标。"
                "只说立场不说证据，是这类讨论里最常见的低分回答；只说事实不给立场，同样拿不到分。"
            ),
            h2("五、Feedback comments：五类常见反馈与改法"),
            p(
                "把 <code>Feedback comments.html</code> 的五段话拆成「反馈类型」，就是一份可自查的清单："
            ),
            tb(
                ("反馈类型", "典型评语", "改法"),
                (
                    "对比不足",
                    "Compare the application to competitors (0.5/1)",
                    "在「新在哪里」里逐条对着竞品写差异，并注明竞品名与来源",
                ),
                (
                    "角色混淆",
                    "User groups and stakeholders ... have been reused (0.5/1)",
                    "利益相关者写「谁受影响、谁出钱、谁维护」；用户组写「谁每天用它、用它做什么」；两表人不同、描述不同",
                ),
                (
                    "反思泛化或自相矛盾",
                    "answers to Appendix 1 are generic, and contradicting (0.75/1.5)",
                    "每条反思绑一个具体事件（某次会议、某次延期），并检查前后归因是否冲突",
                ),
                (
                    "日期口径错",
                    "make sure the dates in the table reflect actual future target deadlines",
                    "Goals 表的日期写目标截止日；报告日期写在封面",
                ),
                (
                    "引用太少",
                    "don't forget to include more references",
                    "每个外部论断配一条来源，教材也算",
                ),
            ),
            p(
                "这张表的价值在于：它把「写得好不好」翻译成了「哪一项拿了几分、为什么」。"
                "写完文档后拿它逐行对照一遍，比再读一遍模板更有效。"
            ),
            h2("六、重复副本与行政页"),
            p("这一批文件里有三类需要标注清楚，不然会误以为漏读了内容："),
            ul(
                "<b>模板的重复副本</b>：<code>Project Proposal Template.docx</code> 在三个目录各有一份"
                "（Proposal、Status Report、Final Report 的 intro/files 下），内容完全一致，只是首行的路径标记不同；"
                "<code>Project Status Report Template.docx</code> 有两份（Status Report 与 Final Report 目录）。"
                "所以去重后只有 2 份模板。",
                "<b>行政页</b>：第 1 周的 <code>Exercise Sessions</code> 页面只有时间与主题，是排课信息；"
                "<code>Online text.html</code> 是小组提交视频的留言页（一句问候加一个视频链接），"
                "既不含评分信息也不含知识点。",
                "<b>「不考」标注</b>：本课源文件里没有出现「not in exam」这类字样；唯一与「不计分」有关的是反馈里"
                "「this score is just for visual purposes and is not a part of grading」，指的是那个 8.25/10 的展示分，"
                "不是指某份材料不考。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ keywords
    kws=kw(
        (
            "project proposal",
            "项目提案",
            "Four sections: Introduction, Customer Needs, Team, References.",
        ),
        ("status report", "状态报告", "Seven sections plus Appendix 1 Reflection."),
        (
            "stakeholder",
            "利益相关者",
            "Who is affected, who pays, who maintains; 5-10 of them.",
        ),
        (
            "user group",
            "用户组",
            "Who uses the application and what they need; 5-10 of them.",
        ),
        ("primary customer", "主要客户", "The customer outside the team."),
        (
            "reflection",
            "反思",
            "What went well, what did not, and what you will change next iteration.",
        ),
        ("iteration", "迭代", "The status report covers one iteration of the project."),
        (
            "goal evaluation",
            "目标评估",
            "Goals carry dates and numbers, as in a real project.",
        ),
        ("honor code", "荣誉守则", "An adaptation of the Stanford honor code."),
        ("plagiarism", "抄袭", "Using another person's work without proper credit."),
        (
            "academic integrity",
            "学术诚信",
            "Violations fail the course and lose all points awarded so far.",
        ),
        (
            "case study method",
            "案例教学法",
            "Read and prepare, discuss in groups, then discuss with the whole class.",
        ),
        (
            "waterfall to agile",
            "从瀑布转敏捷",
            "Compare benefits, downsides and suitable market conditions.",
        ),
        (
            "Kanban",
            "看板方法",
            "The decision in the Pearson case: stay with Scrum or move to Kanban.",
        ),
        (
            "evidence-based position",
            "有证据的立场",
            "There is usually no single correct answer; the best one has the strongest evidence.",
        ),
    ),
    # ------------------------------------------------------------------ examples
    examples="\n".join(
        [
            qa(
                "例 1 · 把 Proposal 的「Customer Needs」写成合格答案",
                p(
                    "情形：模板在 Customer Needs 下印了六个问题（主要客户、次级利益相关者、他们想要什么与为什么、"
                    "选哪个客户问题、给什么用户收益、如何支撑期望体验、怎么知道客户得到了收益）。"
                    "怎样组织成一段能得分的文字？"
                ),
                p(
                    "<b>解：</b>先按模板的两个小标题分层，每层用「名单 + 逐条理由」的结构，最后单独收一句验证方式。"
                ),
                p(
                    "<b>Stakeholders 层</b>：先点明团队之外的主要客户是谁（一句话，具体到角色，不要写「所有用户」），"
                    "再列次级利益相关者 3–6 类，每类后面跟一句「他们想要什么、为什么」——"
                    "理由要落回他们的工作场景，例如「导师想知道项目当前卡在哪，否则给不出针对性建议」。"
                ),
                p(
                    "<b>Needs 层</b>：先写「我们选择解决哪个客户问题」，用一句可检验的话（谁在什么情形下遇到什么障碍）；"
                    "再写「用户收益是什么」，收益要能对应上面的问题；"
                    "然后写「这个收益如何支撑客户期望的整体体验」——把收益接到客户的完整流程上，而不是孤立的功能；"
                    "最后写「怎么知道客户得到了收益」，给出可观察的判据（例如「创业公司收到投资人主动预约」）。"
                ),
                p(
                    "<b>为什么这样写能得分</b>：模板的六个问题在评分时是逐条对答案的，"
                    "分层写作让评审一眼看到「主要客户 / 次级 / 问题 / 收益 / 体验 / 验证」六个点都在。"
                    "反过来，把六个问题混成一段散文，即使内容都对，评审也容易漏读。"
                ),
                p(
                    "<b>常见失误</b>：把「用户收益」写成功能清单（「可以上传视频」是功能，不是收益）；"
                    "「怎么知道」一栏写「用户会反馈」——那不是判据。"
                ),
            ),
            qa(
                "例 2 · 一条符合模板的变更记录",
                p(
                    "情形：项目进行到一半，团队决定给 Feed 页加一个「按投资金额筛选」的功能。"
                    "状态报告里这条变更该怎么写？"
                ),
                p(
                    "<b>解：</b>模板要求四要素：日期、动机、描述、影响。照着填四格即可，每格一句话、不混内容。"
                ),
                p(
                    "<b>日期</b>：决定采纳的那一天（Ventura 写的是 22/10/2026），不是写报告的那一天。"
                ),
                p(
                    "<b>动机</b>：为什么现在改——「让投资人按自己愿意投的金额筛选，不必看完整个路演再判断是否匹配」。"
                    "动机要写<b>用户侧的理由</b>，不要写「客户提了」或「我们觉得更好」。"
                ),
                p(
                    "<b>描述</b>：改了什么——「在 Feed 增加一个按 investment ask 过滤的筛选项」。一句话说清范围，"
                    "不要展开实现细节（那是设计文档的事）。"
                ),
                p(
                    "<b>影响</b>：对计划、进度、其他需求的影响——「下一迭代要为筛选功能多分配时间」。"
                    "这一格最容易被写成「无影响」，而实际上任何变更都有影响；写「无」通常意味着没想清楚。"
                ),
                p(
                    "<b>对照检查</b>：Ventura 的第二条变更（01/11/2026 的 Share Feature）四要素同样齐全，"
                    "影响一栏写的是「属于 Feed 标签页，需在第二迭代落地」——把变更挂回到迭代计划上，这就是「影响」该有的写法。"
                ),
            ),
            qa(
                "例 3 · 反馈说「stakeholders 与 user groups 被复用」，怎么改",
                p(
                    "情形：状态报告里利益相关者表与用户组表写的是同一批人、同一套描述，助教各扣一半分。"
                ),
                p("<b>解：</b>先把两张表的<b>判定问题</b>分开，再按问题重写描述。"),
                p(
                    "利益相关者问的是「谁与这个项目有利益关系」——包括不出钱也不直接使用的人："
                    "出资方、客户的 IT 部门、平台管理员、监管或合规方、合作机构。"
                    "描述写「它与项目的关系 + 它关心什么」，例如「客户方的技术人员：负责把应用接入内部系统，关心接口与数据格式」。"
                ),
                p(
                    "用户组问的是「谁坐在屏幕前用它、用它完成什么」——按使用场景与熟练度分："
                    "新用户与重度用户、个人用户与团队用户、内部用户与外部用户。描述写「使用场景 + 对功能的要求」。"
                ),
                p(
                    "两张表允许出现同一个组织，但<b>描述的角度必须不同</b>：同一家公司在利益相关者表里是「出钱的客户」，"
                    "在用户组表里是「每天用后台审核内容的运营人员」。"
                ),
                p(
                    "<b>自查方法</b>：把两张表的描述并排看，如果有任意一行<b>逐字相同</b>，就说明被复用了。"
                    "Ventura 的反馈正是这样被抓出来的。"
                ),
            ),
            qa(
                "例 4 · 三个情形是否违反 Honor Code",
                p(
                    "情形 A：与同学一起把习题讨论到双方都懂，然后各自写答案提交。"
                    "情形 B：把自己写好的代码发给同学参考，同学改了几个变量名后提交。"
                    "情形 C：用 AI 解释一段报错，自己按解释改了代码，并在提交时按学校政策申报了使用。"
                ),
                p("<b>解：</b>逐条对照守则的五条落地要求与七类违规。"),
                p(
                    "<b>情形 A</b>：原文要求「必须自己写作业、自己做测验，在提交自己的答案之前不得与他人讨论」，"
                    "除非明确允许合作。所以「先讨论再各自写」在未获允许时属于<b>未经允许的合作</b>，是违规；"
                    "正确做法是各自先独立写完提交，之后再讨论。"
                ),
                p(
                    "<b>情形 B</b>：两方都违规。给代码的一方构成「给予未经允许的帮助」（且在理性人应当知道不被允许的情形下），"
                    "提交的一方构成抄袭（使用他人工作而不给出出处、并表示为自己的）。"
                    "改改变量名不构成「自己的作品」，这一点与现代码查重工具的存在是同一件事。"
                ),
                p(
                    "<b>情形 C</b>：不违规。原文要求「阅读并理解学校的 AI 政策，并按政策申报使用」，"
                    "本例既用于理解与查错、也做了申报，属于允许范围。"
                    "但若把 AI 生成的大段代码直接提交且不申报，就同时踩了「抄袭」与「未申报 AI 使用」两条。"
                ),
                p(
                    "<b>要点：</b>判断违规不看「有没有用工具」，看两件事——<b>是否申报</b>、<b>最终产物是不是自己写的</b>。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ practice
    practice="\n".join(
        [
            p(
                "<b>练习 1</b>　按顺序默写 Status Report 的七个正文章节名与附录名，并说明哪三节要求写成表格、各要几条。"
            ),
            det(
                "参考答案与思路",
                p(
                    "1 Introduction、2 Project Goals、3 Stakeholders、4 User Groups、5 Application Description、"
                    "6 Team、7 References，外加 Appendix 1 Reflection。"
                    "其中 2、3、4 三节用表格：Goals 表列为 ID/Date/Goal/Description/Notes；"
                    "Stakeholders 与 User Groups 各要求 5–10 条。"
                ),
            ),
            p(
                "<b>练习 2</b>　Ventura 状态报告里四个目标的日期都写成 14.11.2026。这条为什么会被反馈点名？应该怎么改？"
            ),
            det(
                "参考答案与思路",
                p(
                    "14.11.2026 是状态报告的提交日。Goals 表的 Date 语义是「这个目标的目标截止日」，"
                    "写成写作日会让四个目标看起来「当天到期」，无法评估进度。"
                    "改法：按每个目标的实际计划给未来日期（例如上线目标 2027 春季、扩张目标再往后），"
                    "并在 Notes 里保留数值判据（注册数、利润区间）。"
                ),
            ),
            p(
                "<b>练习 3</b>　用一句话说明「利益相关者」与「用户组」的区别，并举一个同时出现在两表中但描述不同的例子。"
            ),
            det(
                "参考答案与思路",
                p(
                    "利益相关者是「与项目有利益关系的人或组织」（谁受影响、谁出钱、谁维护）；"
                    "用户组是「实际使用应用并完成某类任务的人」（谁用、用来做什么）。"
                    "例：某大学既是利益相关者（出资并希望扶持本校创业），也是用户组（就业服务中心的人员每天用它筛项目）。"
                    "两处描述的角度不同，不算复用。"
                ),
            ),
            p(
                "<b>练习 4</b>　把「我会推迟发布以修正算法偏见」写成一段 4 句话的案例讨论发言，要求含立场、证据、反方、指标。"
            ),
            det(
                "参考答案与思路",
                p(
                    "第 1 句立场：我会推迟发布，先修正对女性误诊率偏高的问题。"
                    "第 2 句证据：案例里已有数据表明该工具对女性的误诊更频繁，而产品定位是医疗辅助判断，"
                    "错误代价由患者承担。第 3 句反方：推迟会错过窗口期、影响融资与团队士气，"
                    "回应是把修正范围限定在可验证的子集并在发布说明中披露限制。"
                    "第 4 句指标：上线后按性别分层的误诊率差距、以及召回率不低于当前版本。"
                    "（评分看的是结构与证据，不是立场本身。）"
                ),
            ),
            p(
                "<b>练习 5</b>　Honor Code 对违规的后果有两条，其中哪一条最容易被低估？为什么？"
            ),
            det(
                "参考答案与思路",
                p(
                    "「Fail the course, losing all points awarded so far」——整门课不及格并失去此前所有得分。"
                    "学生常以为只是该项作业零分，实际是一次违规把整门课的积累清零，"
                    "再加上学校纪律机构的处罚。低估的原因是把课程作业当成彼此独立的评分项。"
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
                    "① 两份模板的章节名与顺序（Proposal 四节；Status Report 七节 + Appendix 1）；"
                    "② 状态报告里变更记录的四要素（日期 / 动机 / 描述 / 影响）；"
                    "③ Stakeholders 与 User Groups 各自 5–10 条且含义不同；"
                    "④ Reflection 的五个问题；"
                    "⑤ Honor Code 的五条落地要求与两类后果（含「失去此前全部得分」）；"
                    "⑥ 案例法的三个阶段名称。"
                ),
            ),
            cal(
                "warn",
                "易错",
                p(
                    "① 把 Stakeholders 与 User Groups 写成同一批人、同一段话（真实提交里就被扣了一半分）；"
                    "② Goals 表的日期写提交日而不是目标截止日；"
                    "③ 变更记录只写「改了什么」，漏掉动机与影响；"
                    "④ Reflection 前后矛盾（先说沟通好、再怪沟通差）；"
                    "⑤ References 只有一条产品官网；"
                    "⑥ 把「AI 用了但没申报」当成小事——它同时构成抄袭与未申报两条；"
                    "⑦ 把案例讨论答成「只讲事实」或「只给立场」，两者都拿不到分。"
                ),
            ),
            cal(
                "tip",
                "进阶",
                p(
                    "① 用「五类问题」给任意案例定位：先判它属于过程模型、质量诊断、分布式协作、伦理还是需求对齐，"
                    "再决定搬哪套框架（质量工具、沟通机制、偏见评估、需求追踪）；"
                    "② 变更表的「影响」一栏写成「对迭代计划的影响」，把变更挂回计划；"
                    "③ 状态报告的 Introduction 与提案共用同一段 Overview，只更新 Project Status，能保证两份文档口径一致；"
                    "④ 引用格式统一（教材也算来源），并在正文里让每条引用都能对应到一个论断。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ checklist
    checklist="\n".join(
        [
            p("提交两份文档之前，按顺序过一遍；每条都能在模板或反馈里找到出处："),
            st(
                "封面：课程编号与学期在两份文档里一致（Ventura 的 4002/4050 不一致就是反例）；",
                "日期：封面写提交日，Goals 表写目标截止日，全篇统一 DD/MM/YYYY 或 MM/DD/YYYY 一种；",
                "章节：Proposal 四节／Status Report 七节 + 附录，名字与顺序不改；",
                "Stakeholders 与 User Groups：各 5–10 条，逐行比对，确保没有逐字相同的描述；",
                "Goals 表：每条带可检验的判据（时间、数值），不只写目标名；",
                "变更记录：每条都有日期、动机、描述、影响四格；",
                "Application Description：应用是什么、主要挑战、设计理由、外部交互四点齐；",
                "Reflection：五问逐条答，每条绑一个具体事件，前后不自相矛盾；",
                "References：每个外部论断有来源，教材也算；",
                "语言与痕迹：过一遍机器翻译痕迹、拼写（Develope/Spesifying 这类）、目录里的作者名；",
                "合规：所有协作者与 AI 使用都按 Honor Code 申报。",
            ),
            cal(
                "tip",
                "交付前 10 分钟的自查",
                "只看三处：两张表有没有重复描述、Goals 表的日期是不是未来、Reflection 前后有没有打架。"
                "助教反馈里扣分的三项，恰好就是这三处。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ mapping
    mapping="\n".join(
        [
            p(
                "下表把这 14 组文件（实体副本 17 份，其中模板的 5 份副本是同一内容）逐一对到章节与覆盖内容，并标注重复副本与行政页。"
            ),
            tb(
                ("文件", "章节 / 页", "覆盖内容与备注"),
                (
                    "Project Proposal Template.docx",
                    "封面 + 四节（1 Introduction / 2 Customer Needs / 3 Team / 4 References）",
                    "提案的章节结构与每节必答问题；Customer Needs 分 Stakeholders 与 Needs 两层",
                ),
                (
                    "Project Status Report Template.docx",
                    "封面 + 七节 + Appendix 1（docx，无页码）",
                    "状态报告结构；Goals / Stakeholders / User Groups 三张表的表头与示例行；Reflection 五问",
                ),
                (
                    "Project Proposal Ventura.pdf",
                    "p1–p8",
                    "真实提案范例：四节齐全；novelty 四条、利益相关者五类、团队分工到人；问题见 2.2（课程号 4002、10/13/2026、引用仅一条）",
                ),
                (
                    "Ventura status report.pdf",
                    "p1–p12",
                    "真实状态报告范例：变更表四要素齐全、Goals 四行带利润目标、S09/E06 两表齐；问题见 2.4（机翻痕迹、日期全为 14.11.2026、两表复用、目录带作者名）",
                ),
                (
                    "Feedback comments.html",
                    "整页（反馈）",
                    "五段反馈：对比 0.5/1、角色混淆 0.5/1、Reflection 0.75/1.5、Goals 日期提示、引用提示；8.25/10 不计入评分",
                ),
                (
                    "Week 1 Exercise Sessions.html",
                    "整页（行政页）",
                    "四个答疑时段与两项主题（项目启动、示例项目）；「周三 10:00–26:00」为原文笔误",
                ),
                (
                    "Week 3 Exercise Sessions.html",
                    "整页",
                    "案例法三步与八条阅读指南；IBM 迭代开发案例与三个讨论题",
                ),
                (
                    "Week 4 Exercise Sessions.html",
                    "整页",
                    "Telerik 敏捷转型案例与五个讨论题（文化、敏捷是设计还是组织工具、技能、可持续性、增长挑战）",
                ),
                (
                    "Week 5 Exercise Sessions.html",
                    "整页",
                    "Pearson SuccessMaker 案例与七个讨论题（路线图、方法对市场响应、收益与代价、Scrum 转 Kanban、度量）",
                ),
                (
                    "Week 10 Case Study.html",
                    "整页",
                    "EXCEED 案例与四个讨论题（投诉性质、优先级、测试是否受控、网络延迟）",
                ),
                (
                    "Week 11 Case Study.html",
                    "整页",
                    "Catalise（Catalisten 抑郁筛查工具）与四个伦理讨论题（价值立场、风险、对齐、延迟代价）",
                ),
                (
                    "Week 12 Case Study.html",
                    "整页",
                    "Sasken 离岸开发案例与五个讨论题（海外功能、过程纪律、需求变化、质量标准、分布式沟通）",
                ),
                (
                    "Online text.html",
                    "整页（行政页）",
                    "小组提交视频的留言页，一句问候加一个视频链接，无评分与知识点内容",
                ),
                (
                    "Project Proposal / Status Report Template 的重复副本",
                    "—",
                    "Proposal 模板在 Proposal、Status Report、Final Report 三个目录各一份（共 3 份，内容一致）；Status Report 模板在 Status Report 与 Final Report 目录各一份（共 2 份）",
                ),
                (
                    "—（本课对照）",
                    "—",
                    "本课源文件无「不考」字样；唯一与「不计分」相关的是反馈中 8.25/10「just for visual purposes and is not a part of grading」，指展示分而非材料",
                ),
            ),
            cal(
                "tip",
                "怎么用这张表",
                "写提案看第 1、3 行（模板 + 真实提案）；写状态报告看第 2、4 行；交前自查看第 5 行（反馈）；"
                "案例讨论前一晚看第 8–13 行（当周的案例与讨论题），把每个问题各写一句立场加一条证据。",
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
