# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import (L, emit, h2, h3, p, ul, ol, ck, st, tb, K, cal, badge, qa, det, pre, code, chips)

LEC = []

# ============================================================ 1
LEC.append(L(
 slug='l01-course-and-se-overview',
 tzh='第 1 讲 · 课程导论与软件工程概览',
 ten='Course Introduction and Introduction to Software Engineering',
 keywords=['software engineering', 'generic product', 'customized product', 'maintainability', 'dependability', 'software process activity', 'application type', 'code of ethics', 'ACM/IEEE', 'heterogeneity'],
 files=['07_Week 1/1_SE - Lecture 0 - 2026.pdf', '08_Week 2/2_SE - Lecture 1 - 2026.pdf', '08_Week 2/1_Why Software Is Easting The World.pdf'],
 overview=(h2('本节定位')
  + p('这是全课的第一讲，把两件事合并起来讲：一是这门课怎么组织、怎么评分、项目要交付什么（原 Lecture 0）；二是软件工程这门学科的基本框架——软件是什么、好软件有哪些属性、软件工程的定义、软件生产的四项基本活动、影响软件的一般问题、以及工程师的职业伦理（原 Lecture 1）。最后一节用 Andreessen 的《Why Software Is Eating the World》说明：为什么在软件已经渗入一切行业的今天，仍然需要「工程化」地做软件。')
  + p('本节是后面所有内容的地基。第 2、3 讲谈过程模型与过程活动，本质是把这里的「四项基本活动」展开成可执行的流程；第 4 至 6 讲分别展开需求、建模、体系结构；第 7 至 10 讲谈测试、演化、项目管理、质量与配置管理。')
  + p('学完本节你应当能够：')
  + ck('用 IEEE 2010 的定义准确说出软件工程是什么，并指出它与「写程序」的区别',
     '区分通用产品（generic product）与定制产品（customized product），并判断需求规格由谁拥有',
     '说出好软件的四个本质属性，并解释为什么可维护性最关键',
     '把任意一个软件系统归入八种应用类型之一，并说明理由',
     '在具体情境中识别违反 ACM/IEEE 伦理准则的行为，并指出对应的原则条款',
     '解释软件生产的四项基本活动，以及它们在不同过程模型中如何被重新编排')),
 detail=(h3('1.1 这门课怎么组织、怎么算分')
  + p('课程是 6 ECTS。按芬兰学制，1 ECTS 对应 27 小时工作量，因此全课约 6 × 27 = 162 小时；课程跨度约 14 周，平均每周约 10 小时。课件的建议很直接：<b>每周持续投入，不要期末突击</b>。')
  + p('评分结构（Lecture 0 与 Lecture 1 的幻灯片一致）如下：')
  + tb(('考核项', '占比', '说明'),
       ('每周个人作业 + 同伴评审（3:1）', '20%', '11 次个人作业，周一 10:00 前提交；同伴评审周日 23:59 前提交'),
       ('每周课堂小测', '10%', '随堂测验，基于教材第 10 版全球版'),
       ('出勤加分', '5%', '课堂参与'),
       ('每周校内练习', '10%', 'Exercise Sessions，案例讨论与小组任务'),
       ('课程项目（报告 + 演示）', '25%', '三次提交：项目提案、状态报告 + 5 分钟 pitch、终期报告 + 7 分钟 pitch'),
       ('客座讲座', '5%', 'Guest Lecture'),
       ('期末考试', '30%', '闭卷笔试（pen and paper）'))
  + p('幻灯片另有一条容易被忽略的硬性规定：<b>课程项目与期末考试各需至少 50 分</b>（表中标 * 的两项）。也就是说，总分再高，项目或期末不及格仍然不能通过。评分等级为 5 = 85–100%、4 = 75–84%、3 = 65–74%、2 = 55–64%、1 = 45–54%、0 = 0–44%。')
  + p('课程项目只写<b>需求规格说明书</b>，不要求写代码。课件原话是：')
  + p('“The purpose of the project is to create requirements specification document for a software product … You do not need to code/develop anything.”（项目的目的是产出一份软件产品的需求规格说明书……你不需要写任何代码。）')
  + p('教材是 Ian Sommerville 的《Software Engineering》第 10 版全球版，所有小测与练习都基于该版本；Moodle 每周另配阅读与视频材料。')
  + h3('1.2 软件是什么')
  + p('课件给出的定义是：')
  + p('“Computer programs and associated documentation. Software products that may be developed for a particular customer or may be developed for a general market.”（计算机程序及与之相关的文档。软件产品既可以是为特定客户开发的，也可以是为通用市场开发的。）')
  + p('这句话有两个要点。第一，<b>软件 = 程序 + 文档</b>，不是只有可执行文件；第二，软件产品按「为谁开发」分成两类，这一点直接决定需求由谁说了算（见 1.3）。')
  + p('软件按用途可分为五种：')
  + tb(('类型', '作用', '例子'),
       ('系统软件 system software', '管理硬件、提供运行平台', '操作系统、设备管理程序'),
       ('应用软件 application software', '完成用户的具体任务', '办公软件、订票系统'),
       ('中间件 middleware', '连接不同系统、屏蔽异构性', '应用服务器、消息队列'),
       ('驱动软件 driver software', '让操作系统控制具体硬件', '打印机驱动、显卡驱动'),
       ('编程软件 programming software', '辅助开发与调试', '汇编器、编译器、调试器、解释器'))
  + p('课件还补充了一个有趣的观点：软件具有「自然性」（naturalness）——它由人在各种约束下写成，因而和自然语言一样具有重复性与可预测性（Hindle 等，《On the naturalness of software》，Communications of the ACM，2016）。这不是考点，但它解释了为什么代码补全、代码克隆检测这类技术能奏效。')
  + h3('1.3 通用产品与定制产品：规格归谁所有')
  + p('这是本节最容易被低估、但在项目与考试中反复出现的区分。')
  + tb(('维度', '通用产品 generic products', '定制产品 customized products'),
       ('定义', '独立系统，卖给任何愿意购买的客户', '受特定客户委托、满足其自身需求'),
       ('例子', '图形软件、项目管理工具、CAD、牙医预约系统', '嵌入式控制系统、空管软件、交通监控系统'),
       ('规格由谁拥有', '开发者（developer）拥有「软件该做什么」的规格', '客户（customer）拥有规格'),
       ('变更由谁决定', '开发者决定是否以及如何变更', '客户决定需要哪些变更'))
  + p('课件原文：“The specification of what the software should do is owned by the software developer and decisions on software change are made by the developer.”（通用产品的规格归开发者所有，变更决策由开发者做出。）定制产品则相反：规格归客户，变更也由客户决定。')
  + cal('warn', '常见误解', '很多同学把「定制产品」理解成「界面可以定制」或「可以配置」。这里的定制指的是<b>由一个特定客户委托、为其自身业务专门开发</b>，因此需求来源单一、验收标准由该客户掌握。SaaS 产品即使允许换主题，只要规格由厂商拥有，仍然是通用产品。')
  + h3('1.4 好软件的四个本质属性')
  + p('课件列出四个 essential attributes，并且给出了英文定义，考试常要求逐条解释：')
  + tb(('属性', '英文定义（课件原句）', '中文解释'),
       ('可维护性 maintainability', 'Software should be written in such a way so that it can evolve to meet the changing needs of customers.', '软件应能被修改以适应用户需求变化。课件强调这是 critical attribute，因为业务环境变化使软件变更不可避免。'),
       ('可靠性与安全性 dependability and security', 'Software dependability includes a range of characteristics including reliability, security and safety. Dependable software should not cause physical or economic damage in the event of system failure.', '包含可靠性、安全性（security）与功能安全（safety）。系统失效时不得造成人身或经济损失，恶意用户不得访问或破坏系统。'),
       ('效率 efficiency', 'Software should not make wasteful use of system resources such as memory and processor cycles.', '不浪费内存与处理器周期，包括响应速度、处理时间、内存占用等。'),
       ('可接受性 acceptability', 'Software must be acceptable to the type of users for which it is designed. This means that it must be understandable, usable and compatible with other systems that they use.', '对目标用户而言可理解、可使用，并与其使用的其他系统兼容。'))
  + p('为什么可维护性被放在第一位？因为软件成本的大头在投入使用之后。课件反复强调：“software costs more to maintain than it does to develop”（维护比开发更贵），第 8 讲会用 2 到 100 倍这个量级再展开。')
  + cal('tip', '记忆方法', '四个属性可以记成「改得动、靠得住、跑得省、用得顺」：maintainability 改得动，dependability & security 靠得住，efficiency 跑得省，acceptability 用得顺。')
  + h3('1.5 软件工程的定义')
  + p('课件给了两个定义，考试可能要求同时写出并比较：')
  + p('Definition 1：“[SE is] the establishment and use of sound engineering principles in order to obtain economically software that is reliable and works efficiently on real machines.”（建立并使用可靠的工程原则，以便经济地获得在真实机器上可靠、高效运行的软件。）')
  + p('Definition 2（IEEE）：“Software engineering: (1) The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software. (2) The study of approaches as in (1).”（把系统化、守纪律、可度量的方法应用于软件的开发、运行与维护，即把工程用于软件；以及对上述方法的研究。）')
  + p('IEEE 定义里有三个形容词值得拆开：<b>systematic</b>（有章法，不是凭灵感）、<b>disciplined</b>（守纪律，按既定流程执行）、<b>quantifiable</b>（可度量，能用数据说话）。第 10 讲的质量度量、第 9 讲的估算，都是「quantifiable」的具体化。')
  + p('课件还给出一个更贴近实践的四段式定义：软件工程<b>满足客户需求</b>，<b>通过应用系统化、可度量的过程</b>，<b>进行软件产品与服务的开发与演化</b>，<b>并受资源及其他外部约束的限制</b>。这四段正好对应四个驱动力（见 1.6）。')
  + p('最后是「工程学科」的完整表述：')
  + p('“Software engineering is an engineering discipline that is concerned with all aspects of software production from the early stages of system specification through to maintaining the system after it has gone into use.”（软件工程是一门工程学科，关注从系统规格的早期阶段直到系统投入使用后维护的软件生产的所有方面。）')
  + p('课件对这句话作了两点解释：<b>engineering discipline</b> 指在组织与财务约束下，用恰当的理论与方法解决问题；<b>all aspects of software production</b> 指不只是技术开发过程，还包括项目管理，以及支撑软件生产的工具与方法的开发。')
  + cal('warn', '易错', '把软件工程等同于「编程」是最常见的错误。编程只是 development 活动的一部分；规格、验证、演化，以及项目管理、配置管理、质量管理，都属于软件工程。')
  + h3('1.6 四个驱动力：改一个，动全身')
  + p('课件用一张图说明项目的四个力：<b>客户与用户</b>（customers, users）、<b>约束与情境</b>（constraints, context）、<b>产品与技术</b>（products, technology）、<b>过程与团队</b>（processes, teams）。关键结论是：')
  + p('“A significant change related to any one of them affects all aspects of a project.”（其中任何一个发生显著变化，都会影响项目的所有方面。）')
  + p('四者的关系可以记成一句话：<b>需求驱动、约束施压、产品被构建、过程去满足</b>。例如客户临时要求支持离线模式（需求变），会牵动技术选型（产品与技术）、排期与人力（过程与团队），并可能触碰合同与法规（约束与情境）。第 12 讲 IBM 案例中「开发末期插入 4000 万美元需求」就是这条规律的教科书式演示。')
  + h3('1.7 软件工程的历史坐标')
  + p('课件用一条时间轴把软件工程史串起来，理解这条线有助于解释「为什么会有今天这些方法」：')
  + tb(('年代', '标志事件', '意义'),
       ('1942', 'Konrad Zuse 的 Plankalkül', '第一个高级程序设计语言'),
       ('1947', 'Kathleen Booth 的 ARC2 汇编语言', '汇编语言出现，机器指令可被符号化表达'),
       ('1950–1960', 'AUTOCODE（Glennie, 1952）、FORTRAN（Backus, 1957）、ALGOL（Perlis, 1958）、COBOL（Hopper, 1959）、LISP（McCarthy, 1959）', '高级语言家族成型，后来的 Pascal、Ada、C、Java 都源自 ALGOL 一脉'),
       ('1960–1970', '软件危机（software crisis）：复杂度上升、成本超支、交付延期；结构化程序设计（Böhm & Jacopini, 1966）', '「写程序」第一次被当作需要工程方法的问题'),
       ('1970–1980', '软件危机延续；面向对象（OOP）引入；通过 SSADM 推广 SDLC', '过程模型与结构化方法成为主流'),
       ('1980–1990', '美国国防部 1985 年采用瀑布模型；Python（van Rossum, 1989）', '瀑布成为官方标准流程'),
       ('1990–2000', 'XP（Beck）、Ruby（Matsumoto, 1993）、PHP（Lerdorf, 1994）、Scrum（Schwaber, 1995）、Java（Gosling, 1995）、JavaScript（Eich, 1995）、UML（Booch, 1997）；互联网兴起', '轻量方法与面向对象建模同时爆发'),
       ('2000–2010', 'Y2K 问题；轻量方法；敏捷宣言（2001，17 位实践者）', '敏捷从边缘实践变成行业主流'),
       ('2010–2020', 'SOA、云计算、AI4SE 与 SE4AI、LLM', '软件既是被工程化的对象，也成为工程化的工具'),
       ('2020–2030', '「你有机会塑造 SE 的版图」', '课件把这一段留给学生'))
  + p('注意「软件危机」出现两次（1960s 与 1970s），说明它不是一次事件，而是一种长期状态：需求越来越复杂，而方法跟不上。第 2 讲的所有过程模型，都是对这场危机的不同回应。')
  + h3('1.8 软件生产的四项基本活动')
  + p('这是全课出现频率最高的四个词，必须能背出英文并解释：')
  + tb(('活动', '英文定义（课件原句）', '产出'),
       ('软件规格 software specification', 'Customers and engineers define the software that is to be produced and the constraints on its operation.', '需求文档 / SRS'),
       ('软件开发 software development', 'The software is designed and programmed.', '设计文档 + 可执行系统'),
       ('软件验证 software validation', 'The software is checked to ensure that it is what the customer requires.', '测试报告、缺陷记录'),
       ('软件演化 software evolution', 'The software is modified to reflect changing customer and market requirements.', '新版本、补丁'))
  + p('关键的一句话是：这四项活动<b>存在于所有软件过程中</b>，区别只在于它们如何被编排。瀑布模型把它们排成顺序，增量开发把它们交织在一起（第 3 讲详述）。')
  + h3('1.9 影响软件的一般问题与应用类型')
  + p('课件列出四个 general issues：')
  + ul('<b>异构性 heterogeneity</b>：系统要在包含不同计算机与移动设备的网络上以分布式方式运行。',
       '<b>业务与社会变化 business and social change</b>：新兴经济体发展与新技术出现，使业务与社会变化极快，必须能改旧软件、快速造新软件。',
       '<b>安全与信任 security and trust</b>：软件与生活各方面交织，必须可被信任。',
       '<b>规模 scale</b>：从可穿戴设备中的极小嵌入式系统，到服务全球的互联网级云系统。')
  + p('因为问题多样，课件强调「软件工程多样性」：<b>没有一套放之四海皆准的技术</b>；方法与工具的选择取决于应用类型、客户需求、团队背景。')
  + p('八种应用类型（考试常以「给一个系统，判断属于哪类」的形式出现）：')
  + tb(('应用类型', '英文要点', '典型例子'),
       ('独立应用 stand-alone applications', '在本机运行，包含全部功能，不需联网', 'PC 上的图像处理软件'),
       ('交互式事务型应用 interactive transaction-based applications', '在远端执行，用户通过终端访问', '电子商务网站'),
       ('嵌入式控制系统 embedded control systems', '控制和管理硬件设备；数量上可能多于任何其他类型', '家电控制器、汽车 ECU'),
       ('批处理系统 batch processing systems', '大批量处理输入、生成对应输出', '工资结算、账单生成'),
       ('娱乐系统 entertainment systems', '主要供个人娱乐', '游戏、流媒体播放器'),
       ('建模与仿真系统 systems for modeling and simulation', '由科学家与工程师开发，模拟物理过程或情境，含大量相互作用的独立对象', '气象模拟、流体仿真'),
       ('数据采集系统 data collection systems', '用传感器从环境采集数据并送往其他系统处理', '环境监测网'),
       ('系统的系统 systems of systems', '由若干其他软件系统组合而成', '智慧城市平台'))
  + h3('1.10 职业伦理：不只是守法')
  + p('课件明确指出：软件工程涉及的责任超出技术技能；工程师必须以诚实、负责任的方式行事，才能被当作专业人士尊重；伦理行为「more than simply upholding the law」，还要遵循一套道德上正确的原则。')
  + p('四项专业责任：')
  + tb(('责任', '英文表述', '含义'),
       ('保密 confidentiality', 'Respect the confidentiality of employers or clients irrespective of whether a formal confidentiality agreement has been signed.', '即使没有签保密协议，也应尊重雇主与客户的机密。'),
       ('胜任力 competence', 'Should not misrepresent their level of competence; should not knowingly accept work which is not within their competence.', '不夸大自己的能力；不明知超出能力仍接下工作。'),
       ('知识产权 intellectual property rights', 'Be aware of local laws governing patents, copyright; ensure the IP of employers and clients is protected.', '了解专利、版权等地方法律，保护雇主与客户的知识产权。'),
       ('计算机误用 computer misuse', 'Should not use technical skills to misuse other people’s computers.', '从上班时间打游戏到传播病毒，都属于误用。'))
  + p('ACM/IEEE 软件工程职业道德准则包含八项原则，按对象排列，非常好记：')
  + ol('<b>Public</b>：与公众利益保持一致。',
       '<b>Client and Employer</b>：以客户与雇主的最佳利益行事，但须与公众利益一致。',
       '<b>Product</b>：确保产品及其修改达到可能的最高专业标准。',
       '<b>Judgment</b>：在专业判断中保持正直与独立。',
       '<b>Management</b>：管理者应支持并推广合乎伦理的开发与维护管理方式。',
       '<b>Profession</b>：增进职业的正直与声誉，与公众利益一致。',
       '<b>Colleagues</b>：公平对待同事并给予支持。',
       '<b>Self</b>：终身学习，并推动职业实践的伦理取向。')
  + p('课件还解释了准则的必要性（rationale）：计算在商业、工业、政府、医疗、教育、娱乐与社会中居于核心且日益重要的地位；软件工程师因此有大量「行善或致害」的机会，所以必须承诺让软件工程成为有益且受尊重的职业。准则分「短版」（aspirations，高层抱负）与「长版」（clauses，具体条款）：没有抱负，条款会变成琐碎的法律条文；没有条款，抱负会变成空洞的口号。')
  + cal('exam', '必考提醒', '八项原则的顺序（Public → Client and Employer → Product → Judgment → Management → Profession → Colleagues → Self）本身就是考点，常以「第 3 项是什么」「哪一项涉及终身学习」的形式出现。')
  + h3('1.11 为什么软件在「吞噬世界」')
  + p('Andreessen 2011 年的文章是本讲的拓展阅读，用来回答一个朴素的问题：既然软件无处不在，为什么还要强调「工程化」？')
  + p('他的核心论断是：我们正处在一场技术与经济的巨变中，软件公司正在接管大片经济领域；从电影到农业到国防，越来越多业务由软件运行、以在线服务交付。原因不是商业模式，而是<b>技术条件终于齐备</b>：宽带用户从十年前的约 5000 万增至 20 亿以上，未来十年至少 50 亿人将拥有智能手机；而启动成本急剧下降——2000 年在 Loudcloud 上运行一个基础互联网应用约需每月 15 万美元，今天在 Amazon 云上运行同样的应用约需每月 1500 美元。')
  + p('他给的证据后来大多成了常识：Borders 2001 年把线上业务交给 Amazon，最终破产，而全球最大书店 Amazon 本质是一家软件公司；Netflix 击溃 Blockbuster；音乐、游戏、摄影、招聘、电信、汽车、零售物流（Wal-Mart、FedEx）、金融、农业、国防，都在被软件重写；医疗与教育在他看来是下一批。')
  + p('但他也列出三项挑战：一是所有新公司都在经济逆风中创建；二是大量劳动者缺乏参与软件革命所需的教育与技能，而企业又极度缺人；三是新公司必须证明自己的价值——建立文化、取悦客户、建立竞争优势。')
  + p('把这篇与 1.4、1.5 连起来看，结论很清楚：<b>软件越重要、规模越大、可靠性要求越高，「靠手艺写代码」就越不够用</b>。这正是软件工程存在的理由。')),
 kws=K(('software engineering', '软件工程', 'The application of a systematic, disciplined, quantifiable approach to the development, operation and maintenance of software.'),
       ('generic product', '通用产品', 'Stand-alone system marketed and sold to any customer; the developer owns the specification.'),
       ('customized product', '定制产品', 'Software commissioned by a specific customer; the customer owns the specification.'),
       ('maintainability', '可维护性', 'Software can evolve to meet changing customer needs.'),
       ('dependability', '可靠性（含安全）', 'Reliability, security and safety; no physical or economic damage on failure.'),
       ('acceptability', '可接受性', 'Understandable, usable and compatible with other systems the users rely on.'),
       ('software specification', '软件规格', 'Defining what the system should do and the constraints on its operation.'),
       ('software validation', '软件验证', 'Checking that the software is what the customer requires.'),
       ('software evolution', '软件演化', 'Modifying software to reflect changing customer and market requirements.'),
       ('heterogeneity', '异构性', 'Systems must operate as distributed systems across different types of device and network.'),
       ('embedded control system', '嵌入式控制系统', 'Software that controls and manages hardware devices; numerically the most common type.'),
       ('system of systems', '系统的系统', 'A system composed of a number of other software systems.'),
       ('confidentiality', '保密', 'Respect client confidentiality even without a signed agreement.'),
       ('computer misuse', '计算机误用', 'Using technical skills to misuse other people’s computers, from trivial to serious.')),
 examples=(qa('例 1　判断产品类型与规格归属',
   p('情境：某医疗器械公司委托一家软件公司，为其新型输液泵开发控制软件；同一家软件公司另有面向所有医院销售的排班系统。请判断两者的产品类型，并说明需求规格与变更由谁决定。')
   + p('<b>分析：</b>先看「为谁开发」。输液泵控制软件是为一个特定客户（医疗器械公司）专门开发、满足其自身产品需求，属于<b>定制产品</b>；排班系统是打包销售给任何愿意购买的医院，属于<b>通用产品</b>。')
   + p('再看规格归属。定制产品的规格由客户拥有，客户决定需要哪些变更——课件原句是 “The specification of what the software should do is owned by the customer”。通用产品的规格由开发者拥有，由开发者决定是否变更。')
   + p('最后看后果：定制产品的验收标准写在合同与 SRS 里，需求变更要走变更单（第 4 讲）；通用产品要做市场调研、自己判断哪些功能值得做，需求来自产品经理而非单一客户。'))
  + qa('例 2　把系统归入应用类型',
   p('情境：某城市在地铁站、公交站部署了数千个传感器，实时采集客流与环境数据，汇总到中心平台做拥堵预测，并把预测结果推送给另一个调度系统。请归类并说明理由。')
   + p('<b>分析：</b>第一步看数据来源——系统通过一组传感器从环境中采集数据，这是 data collection system 的定义特征；第二步看输出——数据被送往其他系统处理，而不是直接面向终端用户；第三步看整体结构——它由采集子系统、分析子系统、调度接口组合而成，符合 systems of systems 的「由若干其他软件系统组成」。')
   + p('因此最准确的描述是：<b>以数据采集系统为核心的系统的系统</b>。若题目只允许选一个，选 data collection systems，并把「与其他系统集成」作为补充说明。')
   + p('<b>通用思路：</b>先判「数据/事件由谁产生」，再判「是否有硬件控制」，再判「是否由多个独立系统组合」，最后判「是否面向个人娱乐」。四步足以覆盖八类。'))
  + qa('例 3　伦理判断：客户要求「先上线，缺陷以后再说」',
   p('情境：你负责的定制产品已通过内部测试，但你知道一个边界条件下会导致数据丢失。客户要求按期上线，并说「出了问题我们自己承担」。你该怎么做？请用 ACM/IEEE 原则说明。')
   + p('<b>分析：</b>第一步识别受影响方——用户（病患、乘客等最终使用者）、客户、雇主、公众。第二步匹配原则：<b>Product</b> 要求产品达到最高专业标准，明知有数据丢失缺陷仍交付不符合；<b>Public</b> 要求与公众利益一致，若缺陷可能造成人身或经济损失，公众利益优先；<b>Judgment</b> 要求保持专业判断的独立，不能因商业压力放弃技术判断；<b>Client and Employer</b> 要求以客户最佳利益行事——短期上线未必是客户的最佳利益，声誉与法律责任才是。')
   + p('第三步给出行动：书面记录缺陷、影响范围与复现条件；提出可选方案（限制功能上线、加临时校验、灰度发布、延期）；把决定提交给有权限的人并留痕；若被要求隐瞒，则援引 Professional 与 Public 两条原则拒绝。')
   + p('<b>注意：</b>「客户说他们承担」不能免除工程师的责任，这是课件所说 ethical behaviour is more than upholding the law 的具体含义。'))
  + qa('例 4　算一算工作量',
   p('情境：课程为 6 ECTS。若你每周只能投入 6 小时，14 周共投入多少小时？与课程要求相差多少？')
   + p('<b>解：</b>课程要求 6 × 27 = 162 小时。你的投入为 6 × 14 = 84 小时。差额 162 − 84 = 78 小时，仅达要求的 84/162 ≈ 52%。')
   + p('<b>结论：</b>每周约需 10 小时（162 ÷ 14 ≈ 11.6，课件取整为 10）。这类计算题的关键是先统一口径——ECTS 是「工作量」而非「课时」。'))),
 practice=(ol('软件工程与计算机科学、系统工程的区别是什么？请各用一句话说明，并举一个例子。',
         '判断：通用产品的需求规格由客户拥有。（对/错，说明理由）',
         '某银行要在每天夜间批量处理上百万笔交易并生成对账单，应归入哪种应用类型？若该银行要求「处理失败时不得产生重复扣款」，这属于四属性中的哪一个（或哪几个）？',
         '写出软件生产的四项基本活动，并说明在瀑布模型中它们的排列方式。',
         '情境设计：你所在的团队要为一家医院开发预约系统，客户提出「下个月必须上线」。请列出至少三项你会用来判断「该不该答应」的工程依据（提示：从四属性、驱动力、过程活动角度）。')
   + det('参考答案与思路',
    p('<b>1.</b> 计算机科学关注算法与计算的理论基础（如复杂度、可计算性）；软件工程关注在约束下经济地生产可靠软件的全部活动（含管理）；系统工程关注包含硬件、软件、人员与流程的整体系统。例子：证明排序下界属 CS；为医院排班系统定需求与测试计划属 SE；设计机场行李系统（传送带 + 软件 + 人员）属系统工程。')
    + p('<b>2.</b> 错。通用产品的规格由<b>开发者</b>拥有，变更也由开发者决定；定制产品才由客户拥有规格。')
    + p('<b>3.</b> 批处理系统（batch processing systems）。「不得重复扣款」首先是可靠性/正确性问题（dependability），同时涉及数据一致性；若失败会造成经济损失，则 dependability 的定义（不得造成经济损失）直接命中。')
    + p('<b>4.</b> specification → development → validation → evolution，瀑布模型把它们排成严格顺序，且每个阶段完成后才进入下一阶段，阶段之间没有反馈路径（第 2 讲详述其代价）。')
    + p('<b>5.</b> 可用的依据包括：需求是否已明确到可验收（否则规格活动无法完成）；上线日期与验证活动所需时间是否冲突（验证不可跳过）；系统的 dependability 要求（医疗场景失效代价高，不能以「先上线」妥协）；团队能力与资源约束（competence 与 constraints）；变更由谁决策（定制产品由客户决策，但工程判断必须独立）。'))),
 exam=(cal('exam', '必考', '软件工程的定义（IEEE 2010 三个形容词）、好软件四属性、四项基本活动、通用/定制产品差异、八种应用类型、ACM/IEEE 八项原则。这些是选择题与简答题的高频点。')
  + cal('warn', '易错 1', '把 validation 与 verification 混为一谈。本讲只出现 validation（确认做的是客户要的东西）；verification（是否按规格做对）在第 7 讲才系统对比。')
  + cal('warn', '易错 2', '把「可维护性」解释成「系统能正常运行」。可维护性指的是<b>能被修改以适应用户需求变化</b>，与「能跑」无关。')
  + cal('warn', '易错 3', '认为伦理只与「违法」有关。课件明确说 ethical behaviour is more than simply upholding the law。')
  + cal('tip', '进阶', '能用一个具体案例把「四个驱动力」串起来（需求变 → 技术选型变 → 排期变 → 合同与法规受触碰），是简答题拿满分的关键；第 12 讲的 IBM 案例可以整段引用。')),
 checklist=(h2('分析一个软件系统的清单')
  + st('判定产品类型：为特定客户开发（定制）还是面向市场销售（通用）',
       '判定规格归属与变更决策权：客户还是开发者',
       '判定应用类型：本机／事务型／嵌入式／批处理／娱乐／仿真／采集／系统的系统',
       '对照四属性逐条评估：可维护、可靠安全、效率、可接受',
       '对照四项活动检查项目是否覆盖规格、开发、验证、演化',
       '识别四个驱动力中当前最不稳定的一项，评估其对排期与范围的影响',
       '做一次伦理扫描：保密、胜任力、知识产权、计算机误用，以及八项原则中受影响最大的两三项')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('07_Week 1/1_SE - Lecture 0 - 2026.pdf', 'p1–p7', '课程人员、教学目标、每周讲座与作业形式、6 ECTS 工作量'),
   ('07_Week 1/1_SE - Lecture 0 - 2026.pdf', 'p8–p15', '模块日程、评分结构与等级、作业截止、课程项目目的与教材'),
   ('07_Week 1/1_SE - Lecture 0 - 2026.pdf', 'p16–p25', '软件的经济现实、软件失败的两类原因、两个软件工程定义、四个驱动力'),
   ('08_Week 2/2_SE - Lecture 1 - 2026.pdf', 'p5–p10', '软件定义、软件类型、通用与定制产品、规格归属'),
   ('08_Week 2/2_SE - Lecture 1 - 2026.pdf', 'p11–p15', '四个本质属性、IEEE 定义、软件工程史、工程学科与「所有方面」'),
   ('08_Week 2/2_SE - Lecture 1 - 2026.pdf', 'p16–p22', '四项过程活动、四个一般问题、多样性、八种应用类型'),
   ('08_Week 2/2_SE - Lecture 1 - 2026.pdf', 'p23–p32', '职业伦理、四项专业责任、ACM/IEEE 八项原则与准则依据'),
   ('08_Week 2/2_SE - Lecture 1 - 2026.pdf', 'p33–p34', 'Key points 汇总'),
   ('08_Week 2/1_Why Software Is Easting The World.pdf', 'p1–p6', '软件重塑经济的论据、启动成本下降、三类挑战（拓展阅读）'),
   ('（跳过）07_Week 1/3_Honor code', '全篇', '课程诚信政策（考试纪律），属行政页，未纳入讲义'),
   ('（拓展）', '—', '软件吞噬世界的成本对比（15 万美元/月 → 1500 美元/月）与 Borders/Amazon 案例属背景补充，不构成考点'),
   ('（跳过）07_Week 1/2_Exercise Sessions', '全篇', '练习课时间地点与项目启动安排，属行政页'))))

# ============================================================ 2
LEC.append(L(
 slug='l02-sdlc-models-and-agile',
 tzh='第 2 讲 · SDLC 模型、瀑布、螺旋、V 模型与敏捷',
 ten='Software Development Life Cycle Models and Agile Methods',
 keywords=['SDLC', 'waterfall model', 'spiral model', 'V-model', 'iterative model', 'RAD', 'agile manifesto', 'extreme programming', 'refactoring', 'pair programming', 'Scrum', 'sprint', 'product backlog', 'velocity', 'scaling agile'],
 files=['09_Week 3/1_SE - Lecture 2 - 2026.pdf'],
 overview=(h2('本节定位')
  + p('上一讲把软件生产拆成四项基本活动；这一讲回答「这些活动按什么顺序、以什么节奏组织」。课件一口气讲了七种模型：瀑布、螺旋、V 模型、迭代、RAD、快速软件开发（RSD）与敏捷（XP、Scrum），最后给出「如何选模型」的判据表。信息量是全课最大的一讲。')
  + p('本讲是第 3 讲（过程活动与过程改进）的前置：先有「模型」这张地图，才能理解过程活动为什么在不同模型里被排成不同顺序。第 11 讲的敏捷实践课会把这里的 Scrum 与 XP 落到具体仪式与度量上。')
  + p('学完本节你应当能够：')
  + ck('说出 SDLC 的定义与目标，并列出瀑布模型的六个阶段及各阶段产出',
     '对比瀑布、螺旋、V 模型、迭代、RAD 的适用条件与主要风险',
     '准确复述敏捷宣言四条价值观与五条原则，并指出「右侧也有价值」的含义',
     '列出 XP 的十余项实践，并解释重构、测试先行、结对编程各自解决什么问题',
     '说清 Scrum 的三个阶段、三个角色、三个产物与一个仪式，并用 velocity 做简单排期',
     '针对给定项目（需求稳定性、风险、团队规模、客户参与度）选出合适模型并给出理由')),
 detail=(h3('2.1 SDLC 是什么')
  + p('课件定义：SDLC 是「a structured process that is used to design, develop, and test good-quality software」，据课件说法最早由 Winston N. Boyce 提出。它把软件开发的整个过程一步步定义清楚，目标是交付<b>高质量、可维护、满足用户需求</b>的软件，并为每个阶段规定计划，使各阶段能高效执行，从而在给定时间内以低成本交付。')
  + p('幻灯片只写了「SDLC is a collection of these six stages」，没有逐一列出六个阶段名称（原图在 PDF 中）。按经典划分，六个阶段是：规划与可行性、需求分析、设计、实现（编码）、测试、部署与维护。答题时若被要求写六阶段，用这六个即可，并注明「课件以图示呈现」。')
  + p('要区分两个词：<b>SDLC</b> 是「生命周期」——有哪些阶段；<b>SDLC model</b> 是「模型」——这些阶段如何排列、是否迭代、如何反馈。同一套阶段可以排出完全不同的模型。')
  + h3('2.2 瀑布模型的六个阶段')
  + p('瀑布模型用于大型、复杂项目，特征是「结构化、顺序化」（structured, sequential）。典型适用条件：需求已明确定义、目标清晰、规模大、周期长。')
  + tb(('阶段', '关键活动', '产出/要点'),
       ('1 需求 Requirements', '可行性研究（理解问题、列出候选方案、比较利弊后选定）；需求分析与规格', 'SRS 文档；分析要消除<b>不完整性</b>（incompleteness，遗漏）与<b>不一致性</b>（inconsistency，相互矛盾）；SRS 作为开发团队与客户之间的<b>合同</b>，未来争议以 SRS 为准'),
       ('2 设计 Design', '把 SRS 转换为可用编程语言实现的形式；高层设计 HLD、详细设计 LLD、总体体系结构', '软件设计文档 SDD'),
       ('3 开发 Development', '按设计编写各模块代码；单元测试；增量式集成', '可运行模块；集成后的部分系统；每步集成后都要测试'),
       ('4 测试 Testing', '系统测试：alpha（开发团队自己做）、beta（友好客户做）、acceptance（交付后客户做，决定接受或拒绝）', '测试报告与验收结论'),
       ('5 部署 Deployment', '部署到客户真实环境验证性能；全面测试确保满足需求、无缺陷；UAT 由最终用户验证', '上线系统；有时含用户培训'),
       ('6 维护与演化 Maintenance and evolution', '维护占总工作量约 60%；三类维护', '纠错性 corrective、完善性 perfective、适应性 adaptive'))
  + p('三类维护必须能区分：<b>corrective</b> 修开发阶段未发现的错误；<b>perfective</b> 按客户要求增强功能；<b>adaptive</b> 把软件移植到新环境（新平台、新操作系统）。第 8 讲会把它扩展成三类并讨论其成本占比。')
  + p('瀑布的优点（课件七条）：易懂；阶段逐个处理；每阶段定义清晰；里程碑明确；文档完备；强化好习惯（define-before-design、design-before-code）；对小项目与需求明确的项目有效。')
  + p('瀑布的缺点：<b>没有反馈路径</b>（no feedback path）、难以容纳变更请求、阶段不可重叠、灵活性有限、干系人参与有限、缺陷发现晚、开发周期长。这七条要能对应到具体后果：缺陷发现晚 → 返工成本高；无反馈 → 需求错了只能一路错到底。')
  + p('适用场景：需求已被充分理解、几乎不期待变更、中小规模、可预测、法规合规要求严格、客户偏好线性顺序、资源有限。典型应用：大型软件开发项目、<b>安全关键系统</b>（航空航天、医疗）、政府与国防项目、需求明确且稳定的项目。')
  + cal('exam', '必考', '「为什么安全关键系统适合瀑布」是经典简答题：因为这类系统的失效后果严重，必须把验证与文档前置、把变更纳入严格控制，而瀑布的阶段性评审与完备文档正好满足这一需求。')
  + h3('2.3 螺旋模型')
  + p('螺旋模型由 Barry Boehm 提出，是瀑布与迭代的结合，最大特点是<b>支持风险处理</b>（risk handling）。它的阶段数不固定，由项目经理根据项目风险动态决定——这也意味着项目经理在螺旋模型中角色极重。每一圈螺旋都是一次完整的开发周期：从需求收集与分析，到设计、实现、测试、维护。')
  + p('四个象限（必须能按顺序说出）：')
  + ol('<b>确定目标并识别备选方案</b>：每圈开始时从客户收集需求，明确并细化目标，提出该阶段的可行方案。',
       '<b>识别并消解风险</b>：评估所有方案、选出最优；识别该方案的风险并用最佳策略消解；本象限结束时为最优方案建立<b>原型</b>。',
       '<b>开发下一版本产品</b>：开发已识别的功能并测试验证；本象限结束时得到软件的下一个版本。',
       '<b>评审并为下一圈做计划</b>：客户评估已开发的版本；随后开始下一阶段的计划。')
  + p('优点：每圈都做风险分析与处理；适合大型复杂项目；需求可在后期变更并被准确纳入；客户满意度高；迭代增量、灵活；强调风险管理；改善沟通；提升质量。')
  + p('缺点：比其他模型复杂；昂贵，不适合小项目；过度依赖风险分析（没有经验丰富的专家就会失败）；阶段数未知导致<b>时间估算困难</b>；多次迭代与评审耗时；资源密集。')
  + p('适用：需要频繁发布；适合先做原型；需要评估风险与成本；中高风险项目；需求复杂且含糊；任何时刻都可能修改；因经济优先级变化而不宜一次性长期承诺的项目。')
  + h3('2.4 V 模型与迭代模型')
  + p('V 模型又称<b>验证与确认模型</b>（Verification and Validation model），过程按 V 字形顺序执行：左侧自顶向下逐层细化（需求 → 概要设计 → 详细设计 → 编码），右侧自底向上逐层验证（单元测试 → 集成测试 → 系统测试 → 验收测试）。其核心思想是「每个开发阶段都有一个对应的测试阶段」（association of a testing phase for each corresponding development stage）。')
  + tb(('左侧开发阶段', '右侧对应测试', '验证的问题'),
       ('需求分析', '验收测试 acceptance testing', '系统是否满足用户需要'),
       ('概要设计（体系结构）', '系统测试 system testing', '各组件集成的系统是否满足需求'),
       ('详细设计', '集成测试 integration testing', '模块间接口与交互是否正确'),
       ('编码', '单元测试 unit testing', '最小单元是否正确'))
  + p('课件只给了 V 模型的定义与图形，上表的「阶段—测试」对应关系是按 V 模型的标准含义补足的（第 12 讲 EXCEED 案例正是 V 过程：测试用例与需求、概设、详设同步开发）。')
  + p('迭代模型把瀑布的顺序步骤与迭代设计的灵活性结合：允许在每个阶段做改进与变更，而不是等到项目末才改。它与增量开发的区别在于：迭代强调「反复重做同一部分直到正确」，增量强调「一块一块地交付」。')
  + h3('2.5 RAD 与快速软件开发')
  + p('RAD（Rapid Application Development）由 IBM 在 1980 年代提出，是<b>增量过程模型</b>，开发周期极短。使用前提很苛刻：需求已被完全理解，且采用<b>基于构件</b>（component-based）的构建方式。')
  + p('四个基本阶段：')
  + ol('<b>需求规划 Requirements Planning</b>：用需求获取技术（头脑风暴、任务分析、表单分析、用户场景、FAST——Facilitated Application Development Technique 等），并制定描述关键数据、获取方法与处理方式的结构化计划。',
       '<b>用户描述 User Description</b>：收集用户反馈，用开发工具构建原型；即对第一阶段收集的数据做复核与验证，并识别数据属性。',
       '<b>构建 Construction</b>：细化原型并交付；用强大的自动化工具把流程与数据模型转成可工作的产品，完成所有修改与增强。',
       '<b>切换 Cutover</b>：测试不同团队开发的独立模块之间的所有接口；用自动化工具与子部件降低测试难度；随后由用户做验收测试。')
  + p('快速软件开发（RSD）的背景：快速开发与交付已成为最重要的需求，因为业务需求变化快，实际上不可能产出一套稳定的需求；计划驱动开发对某些系统必要，但满足不了这种业务需求。敏捷方法因此在 1990 年代末出现，目标是<b>大幅缩短交付可用软件的时间</b>。')
  + h3('2.6 敏捷：宣言与原则')
  + p('敏捷开发的特征（课件五条）：规格、设计与实现相互交织；系统以一系列版本或增量开发，干系人参与增量的规格与评估；频繁交付新版本供评估；广泛使用工具支持（如自动化测试工具）；<b>最少文档</b>，聚焦可工作的代码。')
  + p('敏捷方法出现的原因：对 1980、1990 年代设计方法的「开销」不满。这些方法：聚焦代码而非设计；基于迭代；意图快速交付可工作软件并快速演化。目标是减少过程开销、快速响应需求变化而不过度返工。')
  + p('敏捷宣言（2001）四条价值观，原文必须能背：')
  + ul('<b>Individuals and interactions</b> over processes and tools（个体与互动 高于 流程与工具）',
       '<b>Working software</b> over comprehensive documentation（可工作的软件 高于 详尽文档）',
       '<b>Customer collaboration</b> over contract negotiation（客户协作 高于 合同谈判）',
       '<b>Responding to change</b> over following a plan（响应变化 高于 遵循计划）')
  + p('紧接的一句最关键：“That is, while there is value in the items on the right, we value the items on the left more.”（右侧项也有价值，但我们更看重左侧项。）这句话是「敏捷不是不要文档、不要计划」的原文依据，简答题常考。')
  + p('五条原则：')
  + tb(('原则', '英文要点', '含义'),
       ('客户参与 customer involvement', 'Customers should be closely involved throughout the development process; their role is to provide and prioritize requirements and evaluate iterations.', '客户全程深度参与，负责提供并排序需求、评估每次迭代。'),
       ('增量交付 incremental delivery', 'The software is developed in increments with the customer specifying the requirements to be included in each increment.', '由客户指定每个增量包含哪些需求。'),
       ('人重于过程 people not process', 'The skills of the development team should be recognized and exploited; team members should be left to develop their own ways of working.', '认可并发挥团队技能，不用规定性流程束缚成员。'),
       ('拥抱变化 embrace change', 'Expect requirements to change and design the system to accommodate these changes.', '预期需求会变，并在设计中预留容纳变化的能力。'),
       ('保持简单 maintain simplicity', 'Focus on simplicity in both the software and the process; actively work to eliminate complexity.', '软件与过程都要简单，主动消除复杂性。'))
  + p('适用性：一是在软件公司开发面向销售的中小型产品（几乎所有软件产品与 App 现在都用敏捷）；二是组织内部的定制系统开发，且客户明确承诺参与、外部规则与法规很少。')
  + h3('2.7 极限编程 XP')
  + p('XP 是 1990 年代末极具影响力的敏捷方法，采取「极端」的迭代做法：')
  + ul('新版本可能<b>每天构建多次</b>；',
       '每 <b>2 周</b>向客户交付一个增量；',
       '每次构建都必须运行<b>所有测试</b>，只有测试全部通过，构建才被接受。')
  + p('十余项实践（课件分两页列出，考试常考「下列哪项不是 XP 实践」）：')
  + tb(('实践', '英文说明', '要点'),
       ('增量规划 incremental planning', 'Requirements are recorded on story cards; stories for a release are chosen by time available and relative priority; developers break stories into tasks.', '故事卡 → 发布内容 → 开发任务；时间是硬约束，优先级决定取舍。'),
       ('小规模发布 small releases', 'The minimal useful set of functionality that provides business value is developed first; releases are frequent.', '先交付最小可用功能，再逐步叠加。'),
       ('简单设计 simple design', 'Enough design is carried out to meet current requirements and no more.', '只为当前需求做足够的设计，不预先过度设计。'),
       ('测试先行 test-first development', 'An automated unit test framework is used to write tests before the functionality is implemented.', '先写测试再写实现。'),
       ('重构 refactoring', 'Developers refactor continuously as soon as code improvements are found.', '持续改善代码结构，保持简单可维护。'),
       ('结对编程 pair programming', 'Developers work in pairs, checking each other’s work.', '两人一台机器，互为评审。'),
       ('集体所有 collective ownership', 'Pairs work on all areas of the system; anyone can change anything.', '避免知识孤岛，全员对全部代码负责。'),
       ('持续集成 continuous integration', 'As soon as a task is complete it is integrated; after any integration all unit tests must pass.', '任务完成即集成，集成后测试必须全绿。'),
       ('可持续节奏 sustainable pace', 'Large amounts of overtime are not acceptable.', '长期加班会降低代码质量与中期生产率。'),
       ('现场客户 on-site customer', 'A representative of the end user is available full time; the customer is a member of the team.', '客户是团队成员，负责把需求带进来。'))
  + p('XP 与敏捷原则的对应关系（课件总结）：增量开发 ← 小而频繁的发布；客户参与 ← 客户全职嵌入；人重于过程 ← 结对、集体所有、避免长时间加班；支持变化 ← 定期发布；保持简单 ← 持续重构。')
  + p('现实提醒：XP 偏技术，难以与多数组织的管理实践整合，因此「原教旨 XP」并不广泛使用；真正被广泛借用的核心实践是：<b>用户故事做规格、重构、测试先行、结对编程</b>。')
  + h3('2.8 三项核心技术实践：故事、重构、测试先行')
  + p('<b>用户故事（user stories）</b>：在 XP 中客户是团队一员，负责需求决策；需求以故事或场景表达，写在卡片上；开发团队把故事拆成实现任务，任务是排期与成本估算的基础；客户根据优先级与排期估算挑选下个发布要做的故事。')
  + p('<b>重构（refactoring）</b>：传统观点是「为变化而设计」，值得花时间预判变化以降后期成本；XP 认为变化无法可靠预判，因此不预判，而是<b>持续改进代码</b>，使变化真的到来时更容易实现。团队在没有立即需求时也主动寻找并实施改进：这提升了可理解性，从而减少文档需求；因为结构清晰，变更更容易。但有些变更需要<b>体系结构级重构</b>，代价高得多。')
  + p('<b>测试先行 / 测试驱动开发（test-first / test-driven development）</b>：测试在 XP 中处于中心地位，每次变更后都测试。XP 测试的特征：测试先行；从场景出发增量开发测试；用户参与测试的开发与验证；用自动化测试框架在每次构建时运行全部组件测试。')
  + p('TDD 的具体做法：测试写成<b>程序</b>而非数据，因而可自动执行；测试自身包含「是否正确执行」的检查；通常依赖 JUnit 之类框架；新增功能时自动运行全部新旧测试，从而检查新功能是否引入错误。测试先行的价值在于：<b>写测试的过程就是澄清需求的过程</b>。')
  + p('测试先行的三个已知问题（高频考点）：程序员偏爱写代码不爱写测试，可能走捷径写出不完整的测试（不检查所有可能的异常）；有些测试很难增量编写，例如复杂界面中的「显示逻辑」与屏幕间工作流；<b>很难判断一组测试是否完备</b>——系统测试再多，也可能没有覆盖全。')
  + p('测试自动化（test automation）：测试在工作任务实现之前就被写成可执行组件；这些组件应独立、能模拟输入提交、能检查输出是否符合规格；自动化框架让「写可执行测试、提交一批测试执行」变得容易；因此任何时候都能快速跑一遍测试，新代码引入的问题能被立即发现。')
  + p('结对编程（pair programming）：两人同机共同开发；动态配对，使所有人彼此合作过；它形成<b>非正式评审</b>——每行代码至少被两人看过；促进重构（全队都能从改进中获益）；促进集体所有权与知识扩散，降低人员离职带来的项目风险。课件特别指出：没有证据表明结对必然低效，反而有一些证据显示一对程序员比两个各自为战的程序员更高效。')
  + p('客户在测试中的角色：帮助下个发布要实现的用户故事编写<b>验收测试</b>；随开发推进写测试，从而验证新代码正是客户需要的。但现实困难是：担任客户角色的人时间有限，无法全职投入；他们可能认为「提供需求已经够了」，不愿参与测试。')
  + h3('2.9 Scrum：角色、仪式、产物')
  + p('Scrum 是敏捷方法，但它的关注点是<b>管理迭代开发</b>，而不是具体技术实践。三个阶段：')
  + ol('<b>初始阶段（outline planning）</b>：确立项目总体目标，设计软件体系结构。',
       '<b>一系列冲刺周期（sprint cycles）</b>：每个周期开发系统的一个增量。',
       '<b>项目收尾阶段（project closure）</b>：完成必要文档（系统帮助、用户手册），评估经验教训。')
  + p('术语表（课件原文分两页，必须能英中对照）：')
  + tb(('术语', '定义'),
       ('Development team 开发团队', '自组织（self-organizing）的开发小组，不超过 7 人；负责开发软件与其他必要项目文档。'),
       ('Potentially shippable product increment 潜在可交付的产品增量', '一次冲刺交付的软件增量；理想状态下它已处于完成状态，无需再测试即可并入最终产品；实践中并不总能做到。'),
       ('Product backlog 产品待办列表', 'Scrum 团队要处理的「待办」清单；可以是功能定义、软件需求、用户故事，或架构定义、用户文档等补充任务。'),
       ('Product owner 产品负责人', '识别产品特性或需求、为其排优先级，并持续审视产品待办列表，确保项目持续满足关键业务需要；可以是一个人，也可以是一个小组。'),
       ('Scrum（daily meeting）', 'Scrum 团队的每日会议，回顾进展并确定当天要优先做的工作；理想情况下是全员参加的简短面对面会议。'),
       ('ScrumMaster', '确保 Scrum 过程被遵循，并指导团队有效使用 Scrum；负责与公司其他部分对接，确保团队不被外部干扰；<b>Scrum 开发者坚持认为 ScrumMaster 不应被视为项目经理</b>。'),
       ('Sprint 冲刺', '一次开发迭代，通常 2–4 周。'),
       ('Velocity 速率', '团队在一个冲刺内可完成的产品待办工作量的估计；理解速率有助于估计一个冲刺能覆盖多少内容，也是衡量绩效改进的基准。'))
  + p('团队协作方式：ScrumMaster 是<b>促进者</b>（facilitator）——安排每日会议、跟踪待办、记录决策、对照待办度量进展、与团队外的客户和管理层沟通。全队参加简短的每日会议（Scrum），成员分享信息、说明上次会议以来的进展、出现的问题、以及次日计划。')
  + p('Scrum 的收益：产品被拆成可管理、可理解的块；不稳定的需求不会阻塞进展；全队对所有事情可见，沟通改善；客户看到增量按时交付并获得反馈；客户与开发者之间建立信任，形成「大家都预期项目会成功」的正向文化。')
  + h3('2.10 规模化敏捷与多团队 Scrum')
  + p('敏捷在小中型、可共处一地（co-located）的团队中被证明有效；其成功很大程度来自「大家在一起」带来的沟通改善。规模化就是要改造敏捷方法，以应对多个团队、可能分布在不同地点的大型长期项目。')
  + p('两个方向要区分：<b>scaling up</b> 指用敏捷开发小型团队做不了的大型系统；<b>scaling out</b> 指把敏捷引入到有多年软件开发经验的大型组织。规模化时必须保持敏捷的基本要素：灵活规划、频繁发布、持续集成、测试驱动开发、良好的团队沟通。')
  + p('多团队 Scrum 的四个做法：<b>角色复制</b>（每个团队各有自己的 Product Owner 与 ScrumMaster）；<b>产品架构师</b>（各团队选出架构师，协作设计与演化整体体系结构）；<b>发布对齐</b>（各团队发布日对齐，使系统可演示且完整）；<b>Scrum of Scrums</b>（每日由各团队代表开会讨论进展与计划）。')
  + h3('2.11 敏捷的现实问题与选型')
  + p('课件列出三类实际障碍：')
  + ul('<b>合同</b>：敏捷的非正式性与大公司常用的法律化合同定义不兼容；多数定制系统合同基于「规格」，而规格前置恰好排除了敏捷所依赖的「规格与开发交织」；按时间计费的合同又常被法务视为高风险，因为交付内容无法保证。',
       '<b>维护</b>：敏捷最适合新软件开发，而大公司的软件成本主要来自维护既有系统；若敏捷要成功，必须能支持维护。两个关键问题：以最少文档为特征的敏捷开发出的系统是否可维护？敏捷能否有效用于响应客户变更请求的演化？此外，原开发团队若无法保留，问题会加剧（缺文档、客户参与难维持、团队连续性难保持）。',
       '<b>分布式与大型系统</b>：大型系统通常是若干独立通信系统的集合，由不同团队（常在不同地点、时区）开发；大型系统是「brownfield」——与大量既有系统交互，很多需求与这些交互有关，不适合灵活增量；集成类项目中很大一部分工作是系统配置而非原创编码；大型系统还受外部法规约束、采购与开发周期长、干系人多样，无法让所有干系人都参与开发。')
  + p('组织层面的阻力：没有敏捷经验的项目经理不愿承担新方法的风险；大型组织的质量程序与标准往往与敏捷不兼容；敏捷在技能水平较高的团队效果最好，而大组织技能分布很宽；长期使用传统系统工程流程的组织可能存在文化抵触。')
  + p('「敏捷 vs 计划驱动」的判断因素（课件分三组）：')
  + tb(('维度', '偏向敏捷', '偏向计划驱动'),
       ('系统规模', '小型、可共处一地的团队', '大型、多团队、分布式'),
       ('系统类型', '无需大量前期分析的系统', '需要大量前期分析、详细设计的系统'),
       ('预期寿命', '较短', '长寿命系统需要文档把开发者意图传给支持团队'),
       ('外部监管', '监管少', '受监管的系统通常要提交详细文档作为安全案例'),
       ('人员技能', '技能水平较高', '把详细设计翻译成代码的较低技能即可'),
       ('团队组织', '同地协作', '分布式团队可能需要设计文档'),
       ('支撑工具', '有可视化与分析工具即可少文档', '缺少设计文档时必须有 IDE 支持'),
       ('组织文化', '能接受非正式流程', '以详细文档为常态的工程组织'))
  + h3('2.12 如何选 SDLC 模型')
  + p('课件给出八组判据，每组都是「什么情况选什么」，考试常用「给情境选模型」的方式考：')
  + tb(('判据', '选择'),
       ('需求清晰、不易变', 'Waterfall 或 V-Model'),
       ('需求不清或易演化', 'Agile 或 Iterative'),
       ('小项目、简单', 'Waterfall 或 RAD'),
       ('大型、复杂、需要灵活性', 'Agile、Spiral 或 DevOps'),
       ('高风险、不确定性大', 'Spiral'),
       ('低风险', 'Waterfall'),
       ('团队有迭代开发经验', 'Agile 或 Scrum'),
       ('团队需要结构化指引', 'Waterfall 或 V-Model'),
       ('需要频繁客户反馈', 'Agile、Scrum 或 RAD'),
       ('初始规划后客户参与很少', 'Waterfall 或 V-Model'),
       ('时间与预算固定', 'Waterfall 或 V-Model'),
       ('时间与预算可调整', 'Agile 或 Spiral'),
       ('需要快速发布', 'Agile 或 RAD'),
       ('没有紧迫截止日期', 'Waterfall 或 V-Model'),
       ('需要长期持续更新与支持', 'Agile 或 DevOps'),
       ('几乎不需要维护', 'Waterfall 或 V-Model'),
       ('干系人希望持续参与', 'Agile 或 Scrum'),
       ('干系人只在大里程碑参与', 'Waterfall 或 V-Model'))
  + p('课件的结语值得记住：SDLC 是让软件开发更有序、更优化的框架；「No software model is the best it depends of varied situations」——没有最好的模型，只有适合情境的模型。')),
 kws=K(('SDLC', '软件开发生命周期', 'A structured process used to design, develop and test good-quality software.'),
       ('waterfall model', '瀑布模型', 'Plan-driven, sequential phases with no feedback path.'),
       ('SRS', '软件需求规格说明书', 'The document that serves as a contract between developers and customers.'),
       ('spiral model', '螺旋模型', 'Iterative model combining waterfall and iterative development with explicit risk handling; four quadrants per loop.'),
       ('V-model', 'V 模型', 'Verification and validation model; each development stage has a corresponding test stage.'),
       ('iterative model', '迭代模型', 'Repeats development steps so improvements can be made at every stage.'),
       ('RAD', '快速应用开发', 'Incremental model with very short cycles; needs fully understood requirements and component-based construction.'),
       ('agile manifesto', '敏捷宣言', 'Four value statements; the items on the right still have value.'),
       ('extreme programming', '极限编程', 'Agile method with builds several times a day, two-week increments and all tests on every build.'),
       ('refactoring', '重构', 'Continuous code improvement to keep the design simple and changes cheap.'),
       ('test-first development', '测试先行开发', 'Write an automated test before implementing the functionality.'),
       ('pair programming', '结对编程', 'Two developers at one machine, providing continuous informal review.'),
       ('Scrum', 'Scrum', 'Agile method focused on managing iterative development; three phases, sprints of 2–4 weeks.'),
       ('product backlog', '产品待办列表', 'The list of to-do items the Scrum team must tackle.'),
       ('sprint', '冲刺', 'A development iteration, usually 2–4 weeks.'),
       ('velocity', '速率', 'Estimate of how much backlog effort a team can cover in one sprint.')),
 examples=(qa('例 1　三种项目，三种模型',
   p('情境 A：某国防项目，需求已在合同中冻结，需通过严格评审与文档审查，交付周期 3 年。<br>情境 B：某初创公司要做一款面向消费者的 App，市场窗口 6 个月，需求每周都在变。<br>情境 C：某银行核心系统替换，涉及 12 个既有系统对接，法规审查严格，团队分布在三个国家。<br>请分别为 A、B、C 选模型并说明理由与主要风险。')
   + p('<b>分析：</b>先抓三个判据——需求稳定性、风险与不确定性、团队与干系人结构。')
   + p('<b>A：瀑布（或 V 模型）。</b>需求冻结、法规与安全关键、评审驱动，正符合瀑布「阶段清晰、里程碑明确、文档完备」的优势；V 模型更合适，因为每个开发阶段都有对应测试，验证与确认被显式绑定。主要风险是「无反馈路径」：一旦某阶段理解错误，缺陷会晚发现。缓解手段是把评审做扎实、在需求阶段引入原型验证关键假设。')
   + p('<b>B：敏捷（Scrum + XP 实践）。</b>需求快速变化、需要快速交付可用软件、客户可深度参与，符合敏捷适用条件；用 2 周冲刺、产品待办列表排序、每冲刺交付潜在可交付增量。主要风险是「规模化成瘾」：早期架构若完全不设计，后期重构代价高——课件提醒体系结构重构非常昂贵，所以应在初始阶段做一次 outline planning 定架构。')
   + p('<b>C：混合，以计划驱动为骨架 + 迭代交付。</b>大型 brownfield 系统、外部监管、分布式团队、众多既有接口，都不适合纯敏捷；但完全瀑布又无法应对 12 个系统的接口不确定性。可行方案是：总体用螺旋模型做风险驱动的前期（接口风险最大），实施阶段用迭代增量交付，并用 Scrum of Scrums 做跨团队协调、发布对齐。主要风险是「阶段数不可预知导致时间估算困难」（螺旋的固有缺点）。')
   + p('<b>通用思路：</b>先判需求稳定性 → 再判风险高低 → 再判规模与分布 → 最后判监管与合同形式。四步之后，模型基本只剩一个候选。'))
  + qa('例 2　按 XP 规则设计一个迭代节奏',
   p('情境：一个 6 人团队采用 XP，客户要求「随时可演示、随时可发布」。请给出一天与两周内的构建、测试、集成安排，并说明每条安排对应哪项 XP 实践。')
   + p('<b>解：</b>')
   + p('① 每日多次构建：开发者完成任务即集成到主干，触发自动构建；对应 <b>continuous integration</b> 与 XP 的「新版本可能每天构建多次」。')
   + p('② 每次构建运行全部单元测试与验收测试，全绿才算通过；对应 <b>test-first development</b> 与「所有测试必须在每次构建时运行」。')
   + p('③ 两人结对完成每个任务，代码每行至少两人看过；对应 <b>pair programming</b> 与 <b>collective ownership</b>。')
   + p('④ 发现可改进结构立即重构，不夹带新功能；对应 <b>refactoring</b> 与 <b>simple design</b>。')
   + p('⑤ 两周一个增量交付客户，增量内容由客户按优先级从故事卡中挑选；对应 <b>incremental planning</b> 与 <b>small releases</b>。')
   + p('⑥ 不安排长期加班；对应 <b>sustainable pace</b>。')
   + p('⑦ 客户代表全程在团队中，负责写验收测试与挑选故事；对应 <b>on-site customer</b>。')
   + p('<b>检查：</b>这套安排是否满足「每次构建都被测试验证」？是——②保证了这一点。是否满足「增量只做最小有用功能」？是——⑤由客户按业务价值挑选。'))
  + qa('例 3　用 velocity 做排期',
   p('情境：某 Scrum 团队过去三个冲刺完成的故事点数为 21、24、18。产品待办列表剩余 150 点。若每冲刺固定 2 周，问：预计还需几个冲刺？若客户要求 8 周内交付，团队应如何回应？')
   + p('<b>解：</b>先算速率。取平均 velocity = (21 + 24 + 18) ÷ 3 = 63 ÷ 3 = 21 点/冲刺。剩余 150 点 ÷ 21 ≈ 7.14，向上取整为 <b>8 个冲刺</b>。')
   + p('8 个冲刺 × 2 周 = 16 周，远多于客户要求的 8 周（即 4 个冲刺，约 4 × 21 = 84 点）。团队不应承诺 150 点，而应：① 按优先级把待办列表裁到约 84 点以内；② 明确告知「范围可减、日期不减」——这正是敏捷计划的原则（见第 9 讲：若功能无法在时限内完成，缩减范围，绝不完全延长交付日期）；③ 把剩余项放入后续发布。')
   + p('<b>注意：</b>velocity 是「估计」而非承诺，第一次冲刺的数值最不可靠；用三点估算或规划扑克可以提高可信度（第 11 讲）。'))
  + qa('例 4　敏捷合同的困境',
   p('情境：客户法务坚持「固定总价 + 固定范围 + 固定交付日」，而你方希望采用 Scrum。请指出冲突点，并给出两种可行的合同结构。')
   + p('<b>分析：</b>冲突点在于：Scrum 的规格与开发交织，范围在开发中才逐步确定；固定总价固定范围要求范围前置，二者直接矛盾。课件原文指出：多数定制系统合同基于规格，而这「precludes interleaving specification and development」。')
   + p('<b>方案一：按工作量计费（time and materials）+ 范围弹性。</b>合同约定团队规模、时间盒与单价，范围由产品待办列表动态排序；风险是客户法务认为「交付内容无法保证」。缓解：设置「最小可交付功能集」作为合同附件，并约定每冲刺演示与验收。')
   + p('<b>方案二：固定范围、浮动日期（或固定日期、浮动范围）。</b>用故事点与 velocity 建立可核查的进度指标，合同约定「按优先级交付，日期固定、范围按速率调整」；第 12 讲 Pearson 案例正是用 velocity 与故事点把承诺变得可衡量。')
   + p('<b>结论：</b>合同形式不是技术问题而是风险分配问题；答题时应同时指出「谁承担范围不确定的风险」这一本质。'))),
 practice=(ol('列出瀑布模型六个阶段的名称与各阶段主要产出。',
         '螺旋模型的四个象限分别做什么？为什么说它的「阶段数不确定」既是优点也是缺点？',
         '敏捷宣言说「右侧项也有价值」，请用两个例子说明敏捷项目中仍然需要文档与计划。',
         'XP 的「简单设计」与传统的「为变化而设计」是否矛盾？请说明理由。',
         '某 5 人团队要做校内二手交易平台，需求不稳定、客户就是学生代表。请选模型，并列出你会采用的三项具体实践。',
         'ScrumMaster 与项目经理的区别是什么？请从职责与权力两个角度回答。')
   + det('参考答案与思路',
    p('<b>1.</b> 需求（SRS）→ 设计（SDD：HLD/LLD/体系结构）→ 开发（代码、单元测试、增量集成）→ 测试（alpha/beta/acceptance）→ 部署（上线、UAT、培训）→ 维护与演化（corrective/perfective/adaptive）。')
    + p('<b>2.</b> ①确定目标与备选方案；②识别并消解风险（结束时产出原型）；③开发下一版本；④客户评审并计划下一圈。阶段数由项目经理按风险决定：优点是「按风险投入、不为低风险阶段浪费一圈」，缺点是「开始时无法确定要几圈，因而时间与成本难估算」。')
    + p('<b>3.</b> 文档：架构决策记录、用户手册、监管所需的安全案例——这些无法靠「可工作的软件」替代；计划：发布计划与冲刺计划仍存在，只是粒度更细、可调整。敏捷反对的是「详尽且一旦写成就不再更新的文档」与「不可调整的长期计划」。')
    + p('<b>4.</b> 不矛盾，但取向不同。为变化而设计是「预判并预留扩展点」，成本前置且可能预判错误；简单设计是「只满足当前需求，等变化真的发生再重构」，成本后置但依赖重构能力。XP 的选择建立在「变化不可可靠预判」这一判断上，因此把赌注押在重构而非预设计上。')
    + p('<b>5.</b> 选 Scrum（或 XP 简化版）：需求不稳、客户可参与、团队小。三项实践示例：2 周冲刺 + 每冲刺演示；产品待办列表按价值排序，客户代表任 Product Owner；持续集成 + 单元测试（XP 借用到 Scrum 中）。')
    + p('<b>6.</b> 职责：ScrumMaster 确保过程被遵循、移除障碍、保护团队免受外部干扰、促进会议；项目经理对范围、进度、预算、资源负责并向管理层汇报。权力：ScrumMaster 对「团队怎么做」有引导权但无命令权，不能分配任务；项目经理通常有任务分配与资源调度权。课件特别强调 ScrumMaster 不应被视为项目经理。'))),
 exam=(cal('exam', '必考', '瀑布六阶段与三类维护、瀑布优缺点、螺旋四象限、敏捷宣言四条、XP 实践清单、Scrum 术语（尤其 product backlog / sprint / velocity / ScrumMaster）、选型判据表。')
  + cal('warn', '易错 1', '把「敏捷 = 不做文档、不做计划」。宣言原文明确「右侧项也有价值」，课件也指出敏捷是最少文档而非零文档。')
  + cal('warn', '易错 2', '把 V 模型说成「瀑布的另一种画法」。V 模型的关键是每个开发阶段有对应测试阶段，强调验证与确认的对称性。')
  + cal('warn', '易错 3', '把 velocity 当成承诺或产能上限。它是「估计」，且随团队与内容变化。')
  + cal('warn', '易错 4', '把 ScrumMaster 当项目经理。课件原句：Scrum developers are adamant that the ScrumMaster should not be thought of as a project manager。')
  + cal('tip', '进阶', '能说出「为什么 XP 原版不流行但仍影响深远」——技术性过强、难与管理实践整合，但 user stories、refactoring、TDD、pair programming 被广泛借用。这个判断能显著提升论述题层次。')),
 checklist=(h2('选模型与设计迭代的清单')
  + st('判需求稳定性：能否在开工前冻结（能→瀑布/V；不能→迭代/敏捷）',
       '判风险：是否有高不确定性需要每圈消解（是→螺旋）',
       '判规模与分布：单团队同地（敏捷）／多团队异地（混合 + Scrum of Scrums）',
       '判监管与合同：是否需要前置规格与安全案例（是→计划驱动骨架）',
       '判客户参与度：能否全职嵌入（能→XP/Scrum；不能→计划驱动 + 里程碑评审）',
       '定节奏：冲刺长度（2–4 周）、构建频率（每日多次）、测试门槛（全绿才合并）',
       '定度量：velocity、故事点、缺陷密度、构建时长',
       '写清「范围可减、日期不减」的交付规则，并让客户签字确认')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p5–p7', 'SDLC 定义、目标、六阶段、七种模型清单'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p8–p15', '瀑布六阶段细节、SRS 合同作用、三类系统测试、三类维护、优缺点、适用与应用'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p16–p21', '螺旋模型四象限、优缺点、适用条件'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p22–p25', 'V 模型、迭代模型、RAD 四阶段'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p26–p32', '快速软件开发背景、敏捷特征、敏捷宣言、五条原则、适用性'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p33–p48', 'XP 定义与发布节奏、十余项实践、XP 与敏捷原则对应、用户故事、重构、测试先行、测试自动化问题、结对编程'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p49–p58', '敏捷项目管理、Scrum 三阶段与术语、冲刺周期、团队协作、收益、规模化'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p59–p69', '合同与计费问题、敏捷与维护、系统/人员/组织因素、大型系统、多团队 Scrum、组织阻力'),
   ('09_Week 3/1_SE - Lecture 2 - 2026.pdf', 'p70–p73', '选型判据八组、key takeaway'),
   ('（补充）', '—', 'V 模型「阶段—测试」对应表按标准含义补足；课件仅给定义与图形'),
   ('（跳过）09_Week 3/2_Exercise Sessions', '全篇', 'IBM 案例讨论说明页（讨论题与阅读指南），案例本身已并入第 12 讲'),
   ('（补充）', '—', 'SDLC 六阶段名称按经典划分补足；课件仅写「a collection of these six stages」'))))
# ============================================================ 3
LEC.append(L(
 slug='l03-process-activities-and-improvement',
 tzh='第 3 讲 · 软件过程、过程活动与过程改进',
 ten='Software Processes, Process Activities and Process Improvement',
 keywords=['software process', 'process model', 'plan-driven process', 'incremental development', 'integration and configuration', 'COTS', 'prototype', 'incremental delivery', 'process improvement', 'CMMI', 'SPICE', 'process metric'],
 files=['10_Week 4/1_SE - Lecture 3 - 2026.pdf'],
 overview=(h2('本节定位')
  + p('第 2 讲讲了「有哪些模型」，这一讲把镜头拉近到模型内部：一个软件过程由哪些活动组成、活动之间有哪些产物与角色、当变化来临时过程如何应对，最后讨论组织如何系统地改进自己的过程（SPI）。这一讲是「从项目视角看过程」转向「从组织视角看过程」的桥梁。')
  + p('与前后讲的衔接：第 2 讲的过程模型是本讲的三种基本过程模型的理论来源；本讲的「四项活动」在第 4 至 8 讲逐一展开；本讲末尾的过程改进与度量，直接通向第 10 讲的质量管理与配置管理。')
  + p('学完本节你应当能够：')
  + ck('用「活动 + 顺序 + 产物 + 角色 + 前后条件」完整描述一个软件过程',
     '区分计划驱动过程与敏捷过程，并说明现实中为什么大多数过程是混合的',
     '比较瀑布、增量开发、集成与配置三种过程模型的适用条件与风险',
     '解释变更代价的两个降低手段：变更预期（change anticipation）与变更容忍（change tolerance）',
     '说明原型与增量交付各自降低哪一类风险，以及各自的局限',
     '为一个组织设计一套可度量的过程改进方案，并选择归纳式或规范式方法')),
 detail=(h3('3.1 软件过程是什么')
  + p('课件定义：“A structured set of activities required to develop a software system.”（开发一个软件系统所需的一组结构化活动。）所有软件过程都包含四项活动：')
  + ul('<b>规格 specification</b>：定义系统应该做什么；',
       '<b>设计与实现 design and implementation</b>：定义系统的组织方式并实现系统；',
       '<b>验证 validation</b>：检查系统是否做了客户想要的事；',
       '<b>演化 evolution</b>：根据变化的客户需求修改系统。')
  + p('而「过程模型」（process model）是过程的<b>抽象表示</b>：它从某个特定视角描述过程。课件原句：“A software process model is an abstract representation of a process. It presents a description of a process from some particular perspective.”同一过程可以画出多个模型，取决于你关心什么（时间？角色？产物？风险？）。')
  + h3('3.2 过程描述里有什么')
  + p('描述与讨论过程时，我们通常谈活动及其顺序（例如「定义数据模型」「设计用户界面」）。但完整的过程描述还应包含：')
  + tb(('要素', '英文', '说明'),
       ('产物', 'products', '过程活动的产出，如 SRS、设计文档、测试报告'),
       ('角色', 'roles', '参与者的职责，如产品负责人、架构师、测试工程师'),
       ('前置条件', 'pre-conditions', '活动开始前必须为真的事实，如「需求已基线化」'),
       ('后置条件', 'post-conditions', '活动完成后必须为真的事实，如「所有单元测试通过」'))
  + p('这四个要素是「过程可执行」的关键：没有产物就无法检查，没有角色就无人负责，没有前后条件就无法判断活动是否真的完成。第 13 讲的课程项目计划书要求写「检查点（checkpoints）与评审内容」，本质就是给阶段补上前置与后置条件。')
  + h3('3.3 计划驱动与敏捷：不是二选一')
  + p('课件定义：<b>计划驱动过程</b>（plan-driven processes）指所有过程活动都事先计划好，并按计划度量进展；<b>敏捷过程</b>（agile processes）指规划是增量的，过程可较容易地改变以反映变化的客户需求。')
  + p('紧接着是一句极重要的判断：“In practice, most practical processes include elements of both plan-driven and agile approaches. There are no right or wrong software processes.”（实践中大多数过程同时包含计划驱动与敏捷要素；软件过程没有对错之分。）')
  + cal('exam', '必考', '「没有对错的软件过程」这一判断常被用来反驳「瀑布过时」「敏捷是唯一正确」的绝对化表述。答题时要落到「是否适合当前项目的需求稳定性、风险、监管与团队」。')
  + h3('3.4 三种基本过程模型')
  + tb(('模型', '特征', '可能是计划驱动或敏捷'),
       ('瀑布模型 the waterfall model', '计划驱动；规格与开发是分离而独立的阶段', '计划驱动'),
       ('增量开发 incremental development', '规格、开发、验证相互交织', '两者皆可'),
       ('集成与配置 integration and configuration', '系统由既有的可配置构件组装而成', '两者皆可'))
  + p('课件的关键补充：实践中大多数大型系统使用的过程都同时包含这三种模型的要素。例如：总体按瀑布分阶段立项与验收，内部按增量开发交付，部分模块直接集成商用构件。')
  + h3('3.5 增量开发的收益与代价')
  + p('收益三条：')
  + ol('容纳客户需求变化的成本降低——需要重做的分析与文档远少于瀑布；',
       '更容易获得客户对已完成工作的反馈——客户可以对着演示评论，看到已经实现了多少；',
       '更快速地向客户交付并部署有用软件——客户能比瀑布更早使用并获得价值。')
  + p('代价两条（高频考点）：')
  + ul('<b>过程不可见</b>（the process is not visible）：管理者需要定期可交付物来衡量进展；如果系统开发很快，为每个版本都产出反映其状态的文档并不经济，于是「进展」变得难以从外部观察。',
       '<b>系统结构退化</b>（structure tends to degrade）：除非投入时间与金钱做重构，频繁变更会侵蚀软件结构；结构一旦变坏，后续变更越来越难、越来越贵。')
  + p('第 2 讲的「保持简单 + 持续重构」与这里呼应：增量开发的代价必须用重构来偿还，否则「增量」会变成「技术债复利」。')
  + h3('3.6 集成与配置：以复用为基础')
  + p('该模型基于软件复用：系统由既有构件或应用系统集成而成，这类现成系统常被称为 <b>COTS</b>（Commercial-off-the-shelf，商用现货）。被复用的元素可以被配置，以适配用户需求的行为与功能。课件指出：复用现在是构建许多类型业务系统的标准做法。')
  + p('优点：更少的从零开发 → 成本与风险降低；更快的交付与部署。')
  + p('缺点：<b>需求妥协不可避免</b>，系统可能并不满足用户真实需要；<b>失去对复用元素演化的控制</b>——构件供应商的升级节奏不由你决定。')
  + cal('warn', '易错', '「复用一定更好」是错误直觉。复用降低的是开发成本与风险，换来的是需求妥协与演化失控；当系统差异化正是竞争力来源时，复用可能损害产品。')
  + h3('3.7 四项过程活动的内部结构')
  + p('课件强调：真实的过程是技术、协作与管理活动的交织序列；四项基本活动在不同过程中被<b>不同地组织</b>——瀑布里排成序列，增量开发里相互交织。')
  + p('<b>软件规格</b>：确定需要哪些服务，以及系统运行与开发的约束。需求工程过程包括三步：需求获取与分析（干系人要求或期望什么）、需求规格（详细定义需求）、需求验证（检查需求的有效性）。第 4 讲会完整展开。')
  + p('<b>设计与实现</b>：把系统规格转换为可执行系统的过程。设计是「设计一个能实现规格的软件结构」，实现是「把这个结构翻译成可执行程序」。二者密切相关、可以交织。课件另有一张「设计过程的一般模型」图（原 PDF 为图），其要点是：设计从体系结构设计开始，逐层细化到构件设计与接口设计，并与需求反复核对。')
  + p('实现有两条路径：开发一个或多个程序；或配置一个应用系统（configuring an application system）。对多数系统而言，设计与实现是交织活动。')
  + p('<b>软件验证</b>：验证与确认（V&amp;V）旨在表明系统符合其规格并满足客户需求；包括检查与评审过程以及系统测试。系统测试用从规格与真实数据导出的测试用例来执行系统。课件明确指出：<b>测试是最常用的 V&amp;V 活动</b>。')
  + p('<b>软件演化</b>：软件天生灵活、可以改变；当业务环境变化导致需求变化时，支撑业务的软件必须演化。过去「开发」与「演化/维护」之间有明确分界，但随着全新系统越来越少，这条分界越来越不重要——这也是第 8 讲的主题。')
  + h3('3.8 应对变化：让返工变便宜')
  + p('变化在所有大型软件项目中都不可避免，来源至少三类：业务变化带来新的或改变的需求；新技术带来改进实现的可能性；平台变化要求应用改动。变化导致<b>返工</b>（rework），因此变化成本包含两部分：返工的成本 + 实现新功能的成本。')
  + p('降低返工成本有两个思路，必须能区分：')
  + tb(('手段', '英文', '做法', '典型技术'),
       ('变更预期', 'change anticipation', '在过程里安排能「提前发现」可能变化的活动，使重大返工发生前就预见到变化', '系统原型、原型化需求验证'),
       ('变更容忍', 'change tolerance', '把过程设计成「变化发生时能以较低成本被容纳」', '增量交付、可配置架构、自动化回归测试'))
  + p('课件给出两个具体技术：<b>系统原型</b>（快速开发系统或其一部分，以检查客户需求与设计决策的可行性，支持变更预期）与<b>增量交付</b>（把增量交付给客户评论与试用，同时支持变更规避与变更容忍）。')
  + h3('3.9 原型：为学习而建')
  + p('原型定义：“A prototype is an initial version of a system used to demonstrate concepts and try out design options.”（用于演示概念、试验设计选项的系统初始版本。）')
  + p('原型的收益（课件五条）：改善系统可用性；更贴近用户真实需要；改善设计质量；改善可维护性；减少开发工作量。')
  + p('要理解「原型」的两种用法（这是课件图示的要点，也是常见考点）：<b>抛弃型原型</b>（throw-away prototype）用于澄清需求后丢弃，不进入产品；<b>演化型原型</b>（evolutionary prototype）逐步演化为最终系统。前者适合验证不确定性，后者要承担「原型代码质量差却上线」的风险。')
  + cal('warn', '易错', '把原型当成「先做一个简化版产品」。原型的目的是<b>学习</b>（验证需求或设计选项），不是交付；若把抛弃型原型直接当产品，会继承其粗糙的结构与缺失的非功能属性。')
  + h3('3.10 增量交付：按优先级分批交付')
  + p('增量交付不是一次性交付整个系统，而是把开发与交付拆成若干增量，每个增量交付部分功能。用户需求被排优先级，<b>优先级最高的进入早期增量</b>。')
  + p('关键规则：一旦某个增量的开发开始，该增量的需求就被<b>冻结</b>；但后续增量的需求可以继续演化。这条规则解决了「既要稳定又要灵活」的矛盾：冻结当前、放开未来。')
  + p('优点：每个增量都交付客户价值，功能更早可用；早期增量充当原型，帮助引出后续增量的需求；整体项目失败的风险更低；优先级最高的服务通常获得最多测试。')
  + p('问题：多数系统需要一套被各部分共用的基础设施，而<b>识别所有增量都需要的公共设施很难</b>；此外，迭代过程的本质是「规格与软件一起发展」，这与许多组织的采购模型冲突——在这些组织里，完整系统规格是开发合同的一部分。')
  + h3('3.11 过程改进：从「救火」到「改流程」')
  + p('课件的出发点很现实：无论大型、中型、小型还是初创软件公司，通常在开发与交付中都会遇到问题——缺文档、不遵循流程、缺过程治理、团队间缺集成与协作、缺需求可追溯性、缺技术管理等等。这些问题的后果是项目失败：进度、成本、质量三方面。')
  + p('SPI（software process improvement）可被视为软件开发项目中的<b>再工程或变更管理</b>过程：识别开发生命周期中的低效环节并加以解决，从而得到更好的过程。课件另一定义：过程改进意味着<b>理解现有过程</b>并<b>改变这些过程</b>，以提高产品质量和／或降低成本与开发时间。')
  + p('动机（课件列了八条，可归为四组）：')
  + tb(('动机', '说明'),
       ('标准化与过程一致性', '建立与组织目标、战略对齐的、标准且实用的开发过程'),
       ('成本降低', '通过改进过程消除问题、冗余与缺陷来改善项目成本'),
       ('竞争优势', '例如通过 CMMI 认证，可凭「基于标准方法的成熟过程」获得更多销售机会'),
       ('达成目标、缩短上市时间', '组织目标、项目交付、质量标准、有价值的产品、专业文档都是 SPI 的产出'),
       ('提升客户满意度', '按时、按规格、高质量交付会提升满意度并改善销售'),
       ('工作满意度', '员工因产出高质量产品、清楚知道自己该做什么而获得满足感，减少因不成熟过程引发的冲突与救火'),
       ('自动化与自治', '引入工具实现自动化、提升质量与一致性，并让不同员工承担不同角色'),
       ('已被证明的成效', '成功实施的 SPI 项目有大量证据支持其价值'))
  + h3('3.12 过程改进循环与度量')
  + p('课件给出「过程改进循环」图（原 PDF 为图），其四步可概括为：<b>度量现状 → 分析原因 → 实施改变 → 再度量验证</b>，并循环往复。它与 PDCA 同构，关键在于「以数据开头、以数据收尾」。')
  + p('过程度量（process measurement）的两条原则：')
  + ul('尽可能收集<b>定量</b>的过程数据；但在组织没有清晰定义过程标准时这很难——你不知道该测什么，因此<b>可能必须先定义过程，才可能度量</b>。',
       '过程度量应当用于<b>评估改进效果</b>；但这不意味着「度量驱动改进」。改进的驱动因素应是<b>组织目标</b>。')
  + p('过程度量指标（process metrics）三类：')
  + tb(('类别', '含义', '例子'),
       ('时间', '完成过程活动所需时间', '日历时间；完成某活动或过程的工作量'),
       ('资源', '过程或活动所需资源', '总工作量（人日）'),
       ('事件次数', '特定事件发生次数', '发现的缺陷数'))
  + p('SPI 方法分两大类：<b>归纳式</b>（inductive，自下而上）与<b>规范式</b>（prescriptive，自上而下），多数方法都是循环的、含四个主要步骤。')
  + tb(('类别', '代表方法', '思路'),
       ('规范式 prescriptive', 'CMMI（Capability Maturity Model Integration）、SPICE（Software Process Improvement and Capability dEtermination）', '由外部成熟度模型给出「应该达到什么」，组织对照差距逐级提升'),
       ('归纳式 inductive', 'QIP（Quality Improvement Paradigm）、iFLAP（improvement framework utilizing lightweight assessment and improvement planning）', '从团队自身实践出发，轻量评估后制定改进计划'))
  + p('课件在「能力成熟度等级」页只放了图，并列出需要自行阅读的主题：Kanban、Crystal、CMMI、SPICE。CMMI 的五个成熟度等级是：初始级（initial）、已管理级（managed）、已定义级（defined）、量化管理级（quantitatively managed）、优化级（optimizing）；SPICE（ISO/IEC 15504）用 0–5 的能力等级描述单个过程的能力。这部分课件要求自学，考试若出现通常只考「五级名称与顺序」或「CMMI 属规范式、QIP 属归纳式」。')),
 kws=K(('software process', '软件过程', 'A structured set of activities required to develop a software system.'),
       ('process model', '过程模型', 'An abstract representation of a process from some particular perspective.'),
       ('product', '产物', 'The outcome of a process activity, e.g. a requirements document.'),
       ('role', '角色', 'The responsibilities of the people involved in the process.'),
       ('pre-condition', '前置条件', 'A statement that must be true before an activity is enacted.'),
       ('post-condition', '后置条件', 'A statement that must be true after an activity is enacted or a product produced.'),
       ('plan-driven process', '计划驱动过程', 'All process activities are planned in advance and progress is measured against the plan.'),
       ('incremental development', '增量开发', 'Specification, development and validation are interleaved.'),
       ('integration and configuration', '集成与配置', 'The system is assembled from existing configurable components.'),
       ('COTS', '商用现货', 'Commercial-off-the-shelf system reused and configured rather than built.'),
       ('change anticipation', '变更预期', 'Process activities that anticipate possible changes before significant rework.'),
       ('change tolerance', '变更容忍', 'The process is designed so changes can be accommodated at low cost.'),
       ('prototype', '原型', 'An initial version used to demonstrate concepts and try out design options.'),
       ('incremental delivery', '增量交付', 'Delivering part of the functionality in each increment, highest priority first.'),
       ('process improvement', '过程改进', 'Understanding existing processes and changing them to raise quality or cut cost and time.'),
       ('process metric', '过程度量', 'Quantitative data on time, resources or event occurrences in a process.')),
 examples=(qa('例 1　区分变更预期与变更容忍',
   p('情境：某团队做了三件事：① 在需求阶段用可点击原型与客户确认关键流程；② 把系统拆成可独立部署的六个服务，任一服务可单独升级；③ 建立自动化回归测试，每次提交都跑。请判断各属于变更预期还是变更容忍，并说明理由。')
   + p('<b>分析：</b>先抓定义。变更预期是「在重大返工前提前发现变化」，手段是让不确定性尽早暴露；变更容忍是「变化发生时以低成本容纳」，手段是结构与流程上的可替换性。')
   + p('① 属<b>变更预期</b>：原型让客户在看到具体界面后提出真实需求，把「需求理解错误」这类返工提前到编码之前。')
   + p('② 属<b>变更容忍</b>：服务化把变更的影响范围限制在单个服务内，架构本身容纳变化。')
   + p('③ 属<b>变更容忍</b>：自动化回归测试让「改一处、坏三处」能被立即发现，从而降低每次变化的代价。')
   + p('<b>检查：</b>三者是否互相替代？不。预期降低「变化发生的概率与规模」，容忍降低「变化发生后的代价」，二者互补。'))
  + qa('例 2　增量交付与原型，选哪个',
   p('情境：某政务系统必须在 4 个月内上线「企业注册」功能，但「税务申报」部分需求尚不明确，客户也无法说清。团队规模 8 人。请给出交付策略并说明理由。')
   + p('<b>分析：</b>两个部分的不确定性不同：注册功能需求明确、有明确上线日期；申报功能需求不清。这决定了两者应使用不同的不确定性处理手段。')
   + p('<b>策略：</b>整体采用<b>增量交付</b>：把需求排优先级，把「企业注册」作为第一个增量，冻结其需求并在 4 个月内交付；「税务申报」作为后续增量，需求继续演化。对申报部分先用<b>原型</b>做变更预期——把原型给税务窗口人员试用，暴露「他们说不清但一看就知道不对」的需求。')
   + p('<b>理由：</b>增量交付解决「何时交付价值」与「范围冻结」的问题；原型解决「需求无法言说」的问题。两者组合正是课件所说的「早期增量本身充当原型，帮助引出后续增量的需求」。')
   + p('<b>风险与对策：</b>公共设施（登录、权限、审计日志）会被两个增量共用，若在第一个增量里只为注册设计，第二个增量会被迫改造——所以在增量 1 就要识别并实现公共设施，这正是课件指出的增量交付首要问题。'))
  + qa('例 3　为一家公司设计 SPI 方案',
   p('情境：某 60 人软件公司连续三个项目延期，客户投诉缺陷多；公司没有统一的过程文档，各团队各写各的；管理层想「上个 CMMI 三级」。请给出一个务实的过程改进方案。')
   + p('<b>分析：</b>先诊断，再选方法，再定度量，最后定节奏。')
   + p('<b>诊断：</b>症状是「延期 + 缺陷多 + 无统一过程」。可能的根因是：无过程基线（不知道正常水平）、无需求可追溯性（变更无法评估影响）、无缺陷度量（无法定位高缺陷模块）。')
   + p('<b>方法选择：</b>直接冲 CMMI 三级风险高——CMMI 是规范式（自上而下），需要大量过程资产与证据。务实做法是<b>先归纳后规范</b>：先用 iFLAP 之类轻量方法在 1–2 个团队试点（自下而上，成本低、阻力小），把「需求基线 + 变更单 + 缺陷记录」三件事做起来；等有数据、有共识后，再对照 CMMI 二级（已管理级）的要求补齐项目管理制度。')
   + p('<b>度量设计：</b>按课件三类指标各取一个——时间（需求从提出到基线化的日历时间）、资源（每个需求的人日）、事件（每千行代码缺陷数、变更请求数）。关键原则：度量用于<b>评估改进</b>，改进的驱动是组织目标（按期交付、降低缺陷），不是「把数字做好看」。')
   + p('<b>节奏：</b>按「度量 → 分析 → 改变 → 再度量」循环，每季度一轮；每轮只改一两个环节，避免一次改太多导致无法归因。')
   + p('<b>注意：</b>课件提醒「在过程未定义前无法度量」——所以第一步不是收集数据，而是把「需求基线化」这个活动定义清楚（产物、角色、前后条件）。'))
  + qa('例 4　复用构件的取舍',
   p('情境：某公司要做一套医院排班系统，市场上已有成熟的排班引擎可授权使用（COTS）。但医院要求「按科室自定义排班规则，且规则需支持护士工会的复杂条款」。请分析复用该引擎的利弊，并给出建议。')
   + p('<b>分析：</b>用课件的两条缺点逐一检验。')
   + p('<b>需求妥协：</b>COTS 引擎的规则模型是固定的，工会条款这类高度定制的规则很可能无法表达，或只能通过外部脚本绕行。妥协的代价是「系统不完全满足真实需要」，而这恰恰是排班系统的核心价值。')
   + p('<b>演化失控：</b>工会条款会随劳资协议变化，而引擎升级节奏由供应商决定；若供应商停止支持或修改规则模型，医院将被迫跟随。')
   + p('<b>收益：</b>排班算法的核心（约束求解、冲突检测）极其复杂，自研成本与风险高；复用可显著缩短上市时间。')
   + p('<b>建议：</b>分层决策——核心求解引擎复用，规则表达层自研（把工会条款翻译成引擎可执行的约束）；合同中约定源码托管（escrow）与规则模型的扩展接口，以缓解演化失控。这是「部分复用 + 关键差异化自研」的典型折中。'))),
 practice=(ol('写出软件过程的四项基本活动，并说明「过程模型」与「软件过程」的区别。',
         '增量开发的两大问题是什么？分别给出一种缓解手段。',
         '判断：集成与配置模型中，需求妥协是可以完全避免的。（对/错，说明理由）',
         '某团队在每个增量开始后仍允许修改该增量的需求，结果每个增量都延期。请指出违反了哪条规则，并说明正确做法。',
         '设计三个过程度量指标，分别对应时间、资源、事件三类，并说明它们能回答什么管理问题。',
         'CMMI 与 QIP 分别属于规范式还是归纳式？各自的优缺点是什么？')
   + det('参考答案与思路',
    p('<b>1.</b> 规格、设计与实现、验证、演化。软件过程是现实中的一组活动；过程模型是对它的抽象表示，从一个特定视角描述它，因此同一过程可以有多个模型。')
    + p('<b>2.</b> ①过程不可见——缓解：设定轻量的固定交付节奏（如每两周演示 + 一页进展说明），用可运行的增量代替厚文档作为进展证据；②结构退化——缓解：持续重构、把重构排进每个增量、用自动化测试保护重构。')
    + p('<b>3.</b> 错。课件明确「requirements compromises are inevitable」：复用构件的功能边界决定了系统能做什么，需求必须向构件让步。')
    + p('<b>4.</b> 违反了「增量开始后需求冻结，只有后续增量的需求可继续演化」。正确做法：把新需求排入后续增量的待办列表；若必须插入当前增量，则等量移除其他内容（范围不变），否则日期必然滑动。')
    + p('<b>5.</b> 时间：需求从提出到基线化的中位天数——回答「我们的规格活动是否成为瓶颈」；资源：每个需求从设计到验收的人日——回答「单位功能的成本是否在改善」；事件：每千行代码的缺陷数——回答「质量是否在提升、哪个模块最危险」。')
    + p('<b>6.</b> CMMI 属规范式（外部模型给出目标等级，组织对照差距改进）；QIP 属归纳式（从团队自身数据与经验出发）。规范式优点是标准、可比、利于投标；缺点是文档负担重、易形式主义。归纳式优点是贴合实际、阻力小；缺点是难以横向比较、易停留在局部优化。'))),
 exam=(cal('exam', '必考', '软件过程与过程模型的定义、四项活动、三种过程模型的特征与适用、增量开发的两大问题、变更预期与变更容忍的区分、原型的定义与收益、增量交付的冻结规则、SPI 的定义与两类方法。')
  + cal('warn', '易错 1', '把「变更预期」与「变更容忍」对调。记法：预期 = 提前看见（原型），容忍 = 事后能扛（增量交付、可配置架构）。')
  + cal('warn', '易错 2', '认为增量交付 = 增量开发。增量开发是「分批构建」，增量交付是「分批交给用户使用」；前者可以一次交付，后者必然多次交付。')
  + cal('warn', '易错 3', '把过程度量当成 KPI 考核工具。课件明确：度量用于评估改进，改进的驱动是组织目标，不是度量本身。')
  + cal('tip', '进阶', '能指出「增量交付与采购模型冲突」的根源：合同把完整规格作为交付物，而增量交付要求规格与软件共同演化。这条冲突在第 2 讲（敏捷合同）与第 12 讲（IBM 案例）会再次出现，是三处互证的考点。')),
 checklist=(h2('描述与改进一个过程的清单')
  + st('写出过程包含的活动，并标注顺序与并行关系',
       '为每个活动定义产物（可检查的交付物）',
       '为每个活动指定角色（谁负责、谁批准）',
       '写出前置条件与后置条件（怎样才算开始、怎样才算完成）',
       '标注哪些活动用于「变更预期」、哪些用于「变更容忍」',
       '选出三类度量各一个（时间、资源、事件），并写明采集方式',
       '按「度量 → 分析 → 改变 → 再度量」设定改进循环与复盘节奏',
       '评估是否需要规范式模型（CMMI/SPICE）；若需要，先补齐二级（已管理级）的项目管理证据')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('10_Week 4/1_SE - Lecture 3 - 2026.pdf', 'p4–p7', '软件过程定义、四项活动、过程模型、过程描述要素（产物/角色/前后条件）、计划驱动与敏捷'),
   ('10_Week 4/1_SE - Lecture 3 - 2026.pdf', 'p8–p13', '增量开发、收益与问题、集成与配置、COTS、复用优缺点'),
   ('10_Week 4/1_SE - Lecture 3 - 2026.pdf', 'p14–p23', '四项活动的内部结构：需求工程过程、设计与实现、验证与确认、演化'),
   ('10_Week 4/1_SE - Lecture 3 - 2026.pdf', 'p24–p31', '应对变化、返工成本、变更预期与变更容忍、原型、增量交付及其优缺点'),
   ('10_Week 4/1_SE - Lecture 3 - 2026.pdf', 'p32–p43', '过程改进的动因、SPI 定义、改进循环、度量与指标、归纳式与规范式方法、CMMI/SPICE'),
   ('10_Week 4/1_SE - Lecture 3 - 2026.pdf', 'p44', '自学任务：Kanban、Crystal、CMMI、SPICE'),
   ('（跳过）', '—', '本周无纯图片或行政页需跳过'),
   ('（补充）', '—', 'CMMI 五级名称与 SPICE 能力等级按标准定义补足；课件仅给图并要求自学'))))
# ============================================================ 4
LEC.append(L(
 slug='l04-requirements-engineering',
 tzh='第 4 讲 · 需求工程',
 ten='Requirements Engineering',
 keywords=['requirements engineering', 'functional requirement', 'non-functional requirement', 'domain requirement', 'stakeholder', 'elicitation', 'ethnography', 'scenario', 'use case', 'requirements validation', 'requirements management', 'traceability', 'SRS'],
 files=['11_Week 5/1_SE - Lecture 4 - 2026.pdf'],
 overview=(h2('本节定位')
  + p('需求工程是整门课最「贵」的一讲：课件给出一个量化结论——交付后再修一个需求错误的成本，可能是修一个实现错误的 <b>100 倍</b>。因此这一讲不只是概念，而是一套「把错误挡在编码之前」的方法：如何找对人、如何问出真需求、如何写得可验证、如何验证写对了、如何管理后续变更。')
  + p('与前后的衔接：第 3 讲把「规格」列为四项活动之一，本讲把它展开；第 5 讲的建模（用例图、顺序图）是需求表达的工具；第 13 讲的课程项目正是产出一份需求规格说明书，本讲与第 12 讲的写作规范直接服务于它。')
  + p('学完本节你应当能够：')
  + ck('区分用户需求与系统需求，并说明两类文档的读者差异',
     '把一条需求正确归类为功能需求、非功能需求或领域需求',
     '把一个模糊的「目标（goal）」改写成可验证的非功能需求',
     '为给定项目设计访谈与观察（民族志）方案，并指出访谈的三个典型问题',
     '对一份需求规格做五维检查（validity, consistency, completeness, realism, verifiability）',
     '描述需求变更管理的三个阶段，并说明可追溯性在其中的作用')),
 detail=(h3('4.1 需求工程是什么')
  + p('课件定义：“The process of establishing the services that a customer requires from a system and the constraints under which the system operates and developed.”（确立客户需要系统提供哪些服务，以及系统运行与开发所受约束的过程。）而在该过程中产生的「系统服务的描述与约束」，就是<b>系统需求</b>（system requirements）。')
  + p('课件另给一个更工程化的定义：需求工程是在系统设计的每个阶段对需求进行<b>形式化与定义</b>的过程，包括客户需求、设计需求与测试需求；它是对软件系统需求进行定义、创建与验证的<b>系统而严格</b>的方法，目的是确保软件满足用户需要，并按时、按预算、按质量交付。')
  + h3('4.2 一条需求可以有多抽象')
  + p('课件指出：需求可以是「高层抽象的服务陈述或系统约束」，也可以是「详细的数学化功能规格」。这不是失误，而是因为需求有<b>双重功能</b>：')
  + ul('它可能是<b>投标</b>的基础——因此必须开放给不同承包商作不同解释；',
       '它可能是<b>合同本身</b>的基础——因此必须被详细定义；',
       '这两种陈述都叫「需求」。')
  + p('Davis 的经典表述把这件事说透了：')
  + p('“If a company wishes to let a contract for a large software development project, it must define its needs in a sufficiently abstract way that a solution is not pre-defined … Once a contract has been awarded, the contractor must write a system definition for the client in more detail so that the client understands and can validate what the software will do. Both of these documents may be called the requirements document for the system.”（若公司要为大型项目招标，必须以足够抽象的方式定义需求，使方案不被预先锁定……中标后，承包方必须为客户写出更详细的系统定义，使客户理解并能验证软件将做什么。这两份文件都可以称为该系统的需求文档。）')
  + p('这段话解释了为什么同一项目会有「招标用需求」与「合同用需求」两套文本，也解释了为什么第 13 讲的项目模板要求「需求要可验收」——课程项目模拟的是合同后的详细规格。')
  + h3('4.3 用户需求与系统需求')
  + tb(('类型', '英文定义', '读者', '形式'),
       ('用户需求 user requirements', 'Statements in natural language plus diagrams of the services the system provides and its operational constraints. Written for customers.', '客户、最终用户、业务方', '自然语言 + 图，避免技术细节'),
       ('系统需求 system requirements', 'A structured document setting out detailed descriptions of the system’s functions, services and operational constraints. Defines what should be implemented so may be part of a contract.', '开发者、测试、架构师、合同方', '结构化文档，含详细功能与非功能约束'))
  + p('课件用一张「不同需求类型的读者」图说明：用户需求写给客户看，系统需求写给技术方看，两者不能混写。混写的典型后果是「客户看不懂技术条款，开发看不懂业务意图」。')
  + h3('4.4 干系人')
  + p('干系人定义：“Any person or organization who is affected by the system in some way and so who has a legitimate interest.”（以某种方式受系统影响、因而具有正当利益的任何个人或组织。）课件列了四类：最终用户（end users）、系统管理者（system managers）、系统所有者（system owners）、外部干系人（external stakeholders）。')
  + cal('warn', '易错', '干系人 ≠ 用户。系统所有者出钱、系统管理者运维、外部干系人（监管机构、工会、合作伙伴）可能从不使用系统，但能一票否决。第 13 讲的评分明确要求「识别重要干系人群体」，只写「用户」会失分。')
  + h3('4.5 敏捷与需求')
  + p('课件如实呈现了敏捷对需求的挑战：许多敏捷方法认为「产出详细系统需求是浪费时间」，因为需求变化太快，需求文档总是过时；敏捷通常采用<b>增量式需求工程</b>，用「用户故事」表达需求。这对业务系统是实用的，但对「需要交付前分析的系统」或「多个团队共同开发的系统」是有问题的。')
  + p('为什么有问题？因为交付前分析（如安全关键系统的危害分析）必须在实现前完成；多团队开发需要共享的、稳定的接口定义。用户故事粒度太小、太口语化，无法承担这两类任务。这一点在第 12 讲 Sasken 案例（客户要求「完整产品」而非「增量故事」）中会具体呈现。')
  + h3('4.6 功能需求、非功能需求、领域需求')
  + tb(('类型', '英文定义', '例子'),
       ('功能需求 functional requirements', 'Statements of services the system should provide, how the system should react to particular inputs and how the system should behave. May state what the system should not do.', '系统应向用户开具发票；系统应拒绝超过信用额度的订单'),
       ('非功能需求 non-functional requirements', 'Constraints on the services or functions offered by the system such as timing constraints, constraints on the development process, standards. Often apply to the system as a whole rather than individual features.', '响应时间不超过 2 秒；必须使用公司指定的 IDE；须符合 WCAG 2.1 AA'),
       ('领域需求 domain requirements', 'Constraints on the system from the domain of operation.', '医疗系统须符合病历保存年限法规；航空系统须符合 ARINC 653 分区要求'))
  + p('功能需求的细节：它描述功能或系统服务，取决于软件类型、预期用户、系统使用场景；功能性的<b>用户需求</b>可以是高层陈述（「系统应支持排班」），但功能性的<b>系统需求</b>必须详细描述服务（「系统应在 3 秒内为 200 名护士生成满足最大连续工时 5 小时的排班，冲突时给出替代方案」）。')
  + h3('4.7 完整性与一致性：原则上要求，实践中做不到')
  + p('课件明确：原则上需求应既<b>完整</b>（complete，包含所有需要设施的说明）又<b>一致</b>（consistent，设施描述之间无冲突或矛盾）。但实践中，由于系统与环境的复杂性，<b>不可能</b>产出完整且一致的需求文档。')
  + p('这句话的考试价值在于：它解释了为什么需求管理（4.13）是必需的，也解释了为什么「需求文档必须完美才能开工」是伪命题。工程答案是：接受不完整，但用可追溯性与变更控制来管理不完整。')
  + h3('4.8 非功能需求为什么更关键')
  + p('非功能需求定义系统属性与约束（响应时间、存储要求、I/O 设备能力、系统表示等）；过程需求也可被规定（指定 IDE、编程语言或开发方法）。课件给出一个强判断：<b>非功能需求可能比功能需求更关键；若不满足，系统可能变得无用</b>。')
  + p('原因是功能可以被绕过，而非功能不能。用户发现少了某个功能，会用 Excel 补上；但系统不可靠或太慢，用户就完全无法达成目标（第 10 讲会以「主观质量主要由非功能特性决定」再次论证）。')
  + p('非功能需求对架构的影响：它们往往影响<b>整体体系结构</b>而非单个构件。例如为满足性能要求，你可能必须把系统组织成「最小化构件间通信」的形式。此外，一条非功能需求（如安全需求）可能<b>派生出一批功能需求</b>（需要哪些服务来实现安全），也可能<b>限制既有需求</b>（某些功能因安全策略被禁止）。')
  + p('非功能需求的三种分类：')
  + tb(('分类', '英文', '含义', '例子'),
       ('产品需求', 'product requirements', '规定交付的产品必须以某种方式表现', '响应时间、可用性、内存占用'),
       ('组织需求', 'organisational requirements', '源于组织的政策与流程', '必须使用公司指定的开发流程与工具、必须遵循文档模板'),
       ('外部需求', 'external requirements', '源于系统及其开发过程之外的因素', '法规、会计标准、互操作标准'))
  + h3('4.9 目标与可验证需求')
  + p('非功能需求很难精确陈述，不精确的需求难以验证。课件区分两个词：')
  + ul('<b>目标 goal</b>：用户的总体意图，如「易用」。',
       '<b>可验证的非功能需求 verifiable non-functional requirement</b>：使用某种可被客观测试的度量来陈述。')
  + p('目标是开发者理解用户意图的有用信息，但不能作为验收标准。改写方法：给目标加上「度量 + 条件 + 判定阈值」。例如「易用」→「新用户在无培训情况下，5 分钟内完成首次下单，成功率 ≥ 90%（可用性测试，n ≥ 20）」。')
  + cal('tip', '技巧', '把目标变成可验证需求的三步：① 找出可观测的量（时间、比例、次数、容量）；② 加上测量条件（在什么负载、什么设备、什么用户群）；③ 给出阈值与判定方式。三步缺一，验收时就会吵架。')
  + h3('4.10 需求工程的四个通用活动')
  + p('不同应用领域、不同人员、不同组织的过程差异很大，但所有过程都有若干通用活动：<b>需求获取</b>（elicitation）、<b>需求分析</b>（analysis）、<b>需求验证</b>（validation）、<b>需求管理</b>（management）。实践中它们是<b>迭代交织</b>的，课件用「需求工程过程的螺旋视图」表示：每一圈都从获取开始，经分析、规格，再进入下一轮。')
  + h3('4.11 需求获取与分析')
  + p('获取（elicitation，也叫 requirements discovery）指技术人员与客户合作，了解应用领域、系统应提供哪些服务、系统的运行约束。参与者可能包括最终用户、管理者、维护工程师、领域专家、工会等。')
  + p('五个典型问题（高频考点）：')
  + ol('干系人<b>并不知道自己真正想要什么</b>；',
       '干系人用<b>自己的术语</b>表达需求；',
       '不同干系人的需求可能<b>相互冲突</b>；',
       '组织与政治因素会影响系统需求；',
       '需求在分析过程中<b>还会变化</b>——新干系人出现、业务环境变化。')
  + p('获取过程的四个活动：')
  + tb(('活动', '英文', '做什么'),
       ('需求发现', 'requirements discovery', '与干系人互动，发现其需求；领域需求也在此阶段被发现'),
       ('分类与组织', 'requirements classification and organisation', '把相关需求分组，组织成连贯的簇'),
       ('排优先级与协商', 'prioritisation and negotiation', '排定优先级，解决需求冲突'),
       ('需求规格', 'requirements specification', '把需求文档化，并输入螺旋的下一轮'))
  + h3('4.12 获取技术：访谈、民族志、场景')
  + p('<b>访谈（interviewing）</b>是最常用的技术。类型有二：<b>封闭式</b>（closed，基于预先确定的问题清单）与<b>开放式</b>（open，与干系人自由探讨各种议题）。实践中通常是二者的混合。')
  + p('访谈的实践要点：适合获得「干系人做什么、如何与系统交互」的总体理解；访谈者必须<b>不带先入之见</b>；要主动用「建议某些需求」的方式引导用户开口，而不是只问「你想要什么」——因为用户往往说不出抽象需求，但能对具体建议作出反应。')
  + p('访谈的三个问题：领域专家使用的语言，需求工程师听不懂；访谈<b>不适合获取领域需求</b>——工程师不理解专业术语，而有些领域知识太熟悉，人们觉得「不值得说」或根本说不出来。')
  + p('<b>民族志（ethnography）</b>：社会科学家花相当长时间观察并分析人们实际如何工作。优点是人们不必解释或陈述自己的工作；能观察到重要的社会与组织因素；研究表明<b>实际工作总比简单系统模型所暗示的更丰富、更复杂</b>。')
  + p('民族志能发现两类需求：来自「人们实际怎么做」（而非流程文件说应该怎么做）的需求；来自「协作与对他人活动的感知」（awareness）的需求——知道别人在做什么，会改变我们做事的顺序与方式。')
  + p('局限：民族志适合理解<b>现有</b>过程，<b>无法识别应该新增哪些功能</b>。补救办法是<b>聚焦民族志</b>（focused ethnography）：把民族志与原型结合——原型开发产生的未解问题，正好聚焦民族志分析的方向。另一个问题是它研究的是既有实践，而这些实践可能有已失去意义的历史包袱。')
  + p('<b>故事与场景（stories and scenarios）</b>：场景与用户故事是「系统如何被使用」的真实例子；因为它们基于具体情境，干系人能把自己代入并评论。')
  + p('场景是用户故事的<b>结构化形式</b>，应包含五要素：')
  + ol('起始情境的描述（starting situation）；',
       '正常事件流的描述（normal flow of events）；',
       '可能出什么错的描述（what can go wrong）；',
       '其他并发活动的信息（concurrent activities）；',
       '场景结束时状态的描述（state when the scenario finishes）。')
  + h3('4.13 需求规格：怎么写')
  + p('规格是把用户需求与系统需求写进需求文档的过程。用户需求必须让没有技术背景的最终用户与客户看懂；系统需求更详细、可含更多技术信息；需求可能是开发合同的一部分，因此必须尽可能完整。')
  + p('五种表示法（课件表格）：')
  + tb(('表示法', '说明', '适用与局限'),
       ('自然语言 natural language', '用编号句子书写，每句表达一条需求', '表达力强、直观、通用；但易歧义'),
       ('结构化自然语言 structured natural language', '在标准表单或模板上书写，每个字段提供需求某一方面的信息', '一致性较好；对业务需求有时过于僵化'),
       ('设计描述语言 design description languages', '类似编程语言但更抽象，通过定义系统的操作模型来规定需求', '现在很少使用；对接口规格仍有用'),
       ('图形表示 graphical notations', '图形模型 + 文字注释定义功能需求；常用 UML 用例图与顺序图', '直观、便于沟通；细节需文字补充'),
       ('数学规格 mathematical specifications', '基于有限状态机、集合等数学概念', '无歧义、可减少需求文档中的模糊；但客户难懂，成本高'))
  + p('<b>需求与设计不可分</b>：原则上需求说「做什么」，设计说「怎么做」；实践中二者不可分——体系结构可能被设计用来组织需求；系统可能与其他系统互操作而产生设计需求；为满足非功能需求而选用特定架构可能本身就是领域需求；这些也可能来自监管要求。')
  + p('自然语言规格的写作指南（课件五条，考试常考）：')
  + ul('发明一种标准格式，并对所有需求统一使用；',
       '语言用法一致：<b>shall</b> 表示强制需求，<b>should</b> 表示期望需求；',
       '用文本高亮标出需求的关键部分；',
       '避免计算机行话；',
       '为每条需求加入<b>理由（rationale）</b>，说明它为什么必要。')
  + p('结构化规格（structured specifications）：限制写作者的自由度，用标准方式书写需求。它对某些类型需求很有效，但对业务系统需求有时过于僵化。表单式规格（form-based）的字段包括：功能或实体的定义；输入及其来源；输出及其去向；计算所需信息及其他被使用的实体；要采取的动作；前置与后置条件（如适用）；函数的副作用（如有）。')
  + h3('4.14 用例（use cases）')
  + p('用例是 UML 中的一种场景：它识别交互中的<b>参与者</b>（actors）并描述交互本身。一组用例应描述与系统的<b>所有可能交互</b>；形式是「高层图形模型 + 更详细的表格描述」；UML 顺序图可用于补充细节，展示系统中事件处理的顺序。')
  + p('用例表的标准字段（第 13 讲项目模板完全采用这套字段）：ID、名称与版本、参与者、前置条件、描述、异常、结果、其他需求。第 12 讲的 EXCEED 与第 13 讲的示例项目都用这套表格。')
  + h3('4.15 软件需求文档')
  + p('软件需求文档（SRS）是「对系统开发者所要求内容」的<b>正式陈述</b>；应同时包含用户需求的定义与系统需求的规格。')
  + p('课件有一句加粗的警告：<b>它不是设计文档</b>。“It is NOT a design document. As far as possible, it should set out WHAT the system should do rather than HOW it should do it.”（它应尽可能说明系统该做什么，而不是怎么做。）')
  + cal('exam', '必考', '「SRS 不是设计文档」几乎年年出现。判卷要点：能否指出 SRS 写 WHAT、设计文档写 HOW，并给出一个「把 HOW 写进 SRS」的反例（如「用 Redis 缓存会话」属于设计决策，应写成「会话数据在服务重启后 30 分钟内不得丢失」）。')
  + h3('4.16 需求验证')
  + p('验证关注「需求是否定义了客户真正想要的系统」。为什么重要？因为需求错误代价极高：交付后修一个需求错误，可能是修一个实现错误的 <b>100 倍</b>。')
  + p('五维检查（必须能背）：')
  + tb(('检查项', '英文', '问的问题'),
       ('有效性', 'Validity', '系统是否提供了最支持客户需要的功能？'),
       ('一致性', 'Consistency', '需求之间是否存在冲突？'),
       ('完整性', 'Completeness', '客户要求的所有功能是否都包含？'),
       ('现实性', 'Realism', '在给定预算与技术下，这些需求能实现吗？'),
       ('可验证性', 'Verifiability', '需求能被检查吗（是否有客观判据）？'))
  + p('三种验证技术：<b>需求评审</b>（对需求做系统的人工分析）、<b>原型</b>（用可执行模型检查需求）、<b>测试用例生成</b>（为需求开发测试，以检查其可测试性）。第三种最容易被忽略：写不出测试，说明需求不可验证。')
  + h3('4.17 需求变更与需求管理')
  + p('需求必然变化，课件给了四个原因：系统安装后业务与技术环境总会变；付钱的人与使用的人很少是同一批人；大型系统用户群多样，需求与优先级可能冲突甚至矛盾；最终需求是折中，而经验表明「对不同用户的支持力度」常常需要重新平衡。')
  + p('需求管理（requirements management）是在需求工程过程与系统开发过程中管理变化需求的过程。新需求会在开发中以及投入使用后出现。你需要：跟踪每条需求；维护依赖需求之间的<b>链接</b>（以便评估变更影响）；建立正式的变更提案流程，并把提案与系统需求关联。')
  + p('变更管理的三个阶段：')
  + ol('<b>问题分析与变更规格</b>：分析问题或变更提案是否有效；把分析结果反馈给提出者，提出者可能给出更具体的提案，或撤回请求。',
       '<b>变更分析与成本核算</b>：利用<b>可追溯性信息</b>（traceability）与对系统需求的一般知识评估变更影响；分析完成后，决定是否继续该变更。',
       '<b>变更实现</b>：修改需求文档，必要时修改系统设计与实现。理想情况下文档的组织方式应使变更易于实施。')
  + p('注意第一阶段与第二阶段的区别：第一阶段判断「这个变更请求是否成立」，第二阶段判断「实施它要付什么代价」。两者都通过才进入实现。')),
 kws=K(('requirements engineering', '需求工程', 'Establishing the services a customer requires and the constraints on operation and development.'),
       ('system requirements', '系统需求', 'A structured document with detailed descriptions of functions, services and constraints; may be part of a contract.'),
       ('user requirements', '用户需求', 'Natural language statements plus diagrams, written for customers.'),
       ('functional requirement', '功能需求', 'Services the system should provide and how it reacts to particular inputs.'),
       ('non-functional requirement', '非功能需求', 'Constraints on services or functions: timing, process, standards.'),
       ('domain requirement', '领域需求', 'Constraints derived from the domain of operation.'),
       ('stakeholder', '干系人', 'Any person or organisation affected by the system with a legitimate interest.'),
       ('elicitation', '需求获取', 'Technical staff working with customers to find out the domain, services and constraints.'),
       ('ethnography', '民族志', 'Observing how people actually work to discover requirements.'),
       ('scenario', '场景', 'A structured user story with starting situation, normal flow, what can go wrong, concurrent activities and final state.'),
       ('use case', '用例', 'A UML scenario identifying actors and the interaction itself.'),
       ('requirements validation', '需求验证', 'Demonstrating that the requirements define the system the customer really wants.'),
       ('verifiability', '可验证性', 'Whether a requirement can be checked objectively.'),
       ('traceability', '可追溯性', 'Links between requirements used to assess the impact of change.'),
       ('requirements management', '需求管理', 'Managing changing requirements during RE and development.'),
       ('SRS', '软件需求规格说明书', 'The official statement of what is required; WHAT, not HOW.')),
 examples=(qa('例 1　把三条需求正确归类',
   p('情境：某医院预约系统的需求如下。① 患者可在 App 上选择科室、医生与时段并确认预约。② 系统在早 8:00–10:00 高峰期的预约请求响应时间不超过 1.5 秒（95 分位）。③ 系统须符合《电子病历管理规范》关于预约记录保存 15 年的要求。请分类并说明理由。')
   + p('<b>分析：</b>先问「它约束的是行为还是属性」。① 描述系统提供什么服务、如何响应输入 → <b>功能需求</b>。② 描述系统作为一个整体的性能约束 → <b>非功能需求</b>（产品需求中的性能子类）。③ 约束来自医疗业务领域法规，不是用户提出也不是技术选择 → <b>领域需求</b>。')
   + p('<b>进一步：</b>② 是可验证的（有度量、有负载条件、有分位数）；如果把 ② 写成「系统应快速响应」，那就是目标（goal）而非可验证需求，验收时无法判定。')
   + p('<b>通用思路：</b>功能需求看「做什么」，非功能需求看「多快、多稳、多安全、受什么流程约束」，领域需求看「这个行业的规则从哪来」。'))
  + qa('例 2　把目标改写成可验证需求',
   p('情境：客户说「这个系统要非常好用，护士看一眼就会」。请改写为可验证的非功能需求，并说明验证方式。')
   + p('<b>解：</b>第一步找可观测的量——「会用」可以操作化为「在无培训条件下完成核心任务的成功率与耗时」。第二步加条件——任务是什么、用户是谁、样本多大。第三步给阈值与判定方式。')
   + p('改写结果：「在无培训条件下，20 名未使用过本系统的注册护士中，至少 18 名（90%）能在 3 分钟内完成『为一名患者改约到下周二下午』这一任务，且无需求助；测试在真实设备（10 英寸平板）上进行，采用可用性测试脚本，记录任务完成率与耗时。」')
   + p('<b>验证方式：</b>可用性测试（形成性测试用于改进，总结性测试用于验收）；若未达标，则记录失败点并迭代界面。')
   + p('<b>注意：</b>不要把它写成「界面应简洁美观」——那是目标，不是需求；也不要把实现方案（「用大按钮」）写进需求，那是设计。'))
  + qa('例 3　设计访谈与观察方案',
   p('情境：你要为某快递公司的分拣中心开发一套「异常件处理」系统。调度主管说「我们流程很标准，你按流程文档写就行」。请设计获取方案，并指出只做访谈会漏掉什么。')
   + p('<b>分析：</b>「流程很标准」本身是风险信号——课件指出实际工作总比流程文档所暗示的更丰富。')
   + p('<b>方案：</b>① <b>开放式访谈</b>调度主管与一线分拣员，先问「昨天最难处理的一件是什么」，用具体事件代替抽象流程；② <b>封闭式访谈</b>质控与 IT，核对异常代码表、系统接口与报表口径；③ <b>民族志观察</b>一个完整班次（含交接班），记录实际动作、口头沟通、便签与临时表格；④ 用<b>场景</b>把观察到的典型情形写成五要素剧本，回读给分拣员确认；⑤ 用<b>原型</b>（异常件登记界面）做聚焦民族志，让操作员在真实节奏下试用。')
   + p('<b>只做访谈会漏掉：</b>① 人们「说不出来」的隐性规则（例如某类破损件必须先拍照再上报，因为理赔需要）；② 协作与感知类需求（分拣员通过看邻台是否堆货来判断是否叫人）；③ 实际工作中的绕行做法（用纸单兜底）；④ 语言差异导致的误解（「滞留件」「疑难件」「问题件」在不同班组含义不同）。')
   + p('<b>结论：</b>访谈拿「意图」，观察拿「事实」，场景拿「共识」，原型拿「反应」。四者组合才构成完整获取。'))
  + qa('例 4　五维检查与变更影响分析',
   p('情境：需求文档中有三条：R1「系统应支持导出报表」；R2「所有报表导出必须在 1 秒内完成」；R3「报表格式须符合财政局 2024 年第 7 号文」。另有新提案「增加按科室维度导出」。请做验证检查，并分析变更影响。')
   + p('<b>验证：</b><b>有效性</b>——R1 未说明哪些报表、给谁用，无法判断是否支持客户需要；<b>一致性</b>——R2 的「1 秒」对「全量年度报表」可能不现实，与 R1 的范围模糊共同构成潜在冲突；<b>完整性</b>——缺「无数据时如何导出」「权限不足时如何处理」；<b>现实性</b>——R2 在现有数据库上可能不可达；<b>可验证性</b>——R2 可验证（有度量），但缺测量条件（数据量、并发数）。')
   + p('<b>变更影响：</b>借助可追溯性，从「按科室维度导出」追溯到：报表生成服务（R1）、性能约束（R2，新增维度可能破坏 1 秒指标）、格式规范（R3，需确认新维度是否在规范允许的列范围内）、数据模型（是否已有科室字段与权限模型）。')
   + p('<b>结论：</b>该提案技术上可行但会触碰 R2；应在变更分析阶段给出「新增维度后的性能实测」，再决定是放宽 R2 还是优化查询。这正是「变更分析与成本核算」阶段的作用。'))),
 practice=(ol('用户需求与系统需求的区别是什么？各举一例。',
         '判断：非功能需求只影响单个构件，不影响整体架构。（对/错，说明理由）',
         '写出场景的五要素，并用其中三要素描述「患者在 App 上改约」的正常流程。',
         '访谈为什么不适合获取领域需求？给出两种补救手段。',
         '把「系统应安全」改写为两条可验证的非功能需求。',
         '某需求在开发中期被提出变更。请按变更管理的三阶段写出你的处理步骤。')
   + det('参考答案与思路',
    p('<b>1.</b> 用户需求用自然语言 + 图，写给客户看，避免技术细节（「护士应能在一个屏幕上看到本班次全部患者」）；系统需求是结构化文档，写给技术方，可含详细约束（「该屏幕在 200 名患者、10 英寸设备上首屏渲染 ≤ 800 ms」）。')
    + p('<b>2.</b> 错。课件明确：非功能需求常影响整体体系结构而非单个构件，例如为满足性能须最小化构件间通信；一条安全需求还可能派生出一批功能需求。')
    + p('<b>3.</b> 五要素：起始情境、正常事件流、可能出错之处、并发活动、结束状态。示例：起始——患者已登录且有一个未来 7 天内的预约；正常流——进入「我的预约」→ 选择该预约 → 点「改约」→ 选择新时段 → 确认；结束——旧预约被取消、新预约生成、双方收到通知。')
    + p('<b>4.</b> 因为工程师不懂专业术语，且部分领域知识过于熟悉，从业者认为不值得说或说不清。补救：请领域专家参与并充当翻译；用民族志观察实际工作；用原型引出对具体方案的反应。')
    + p('<b>5.</b> 例：「系统在检测到未授权访问尝试后 60 秒内锁定该账户并通知所有者」；「系统对静态存储的患者数据使用 AES-256 加密，密钥轮换周期不超过 90 天」。两条都有度量或可检查的机制。')
    + p('<b>6.</b> ①问题分析与变更规格：确认提案是否成立、范围与验收标准，反馈给提出者；②变更分析与成本核算：用可追溯性找出受影响需求、设计、测试，估算工作量与风险，决定是否实施；③变更实现：更新需求文档与基线，同步修改设计、代码与测试用例，并记录变更日志。'))),
 exam=(cal('exam', '必考', '需求工程定义、用户/系统需求差异、功能/非功能/领域三类、五维验证（validity/consistency/completeness/realism/verifiability）、场景五要素、SRS 不是设计文档、需求错误 100 倍成本、变更管理三阶段。')
  + cal('warn', '易错 1', '把「完整性 / 一致性」当成必须达到的目标。课件明确：由于复杂性，完整且一致的需求文档在实践中不可能产出。')
  + cal('warn', '易错 2', '把民族志当成万能。它只能理解现有实践，无法识别应新增的功能；必须与原型结合（focused ethnography）。')
  + cal('warn', '易错 3', '把「目标」当需求写进 SRS。「易用」「高性能」不可验收，必须转成度量 + 条件 + 阈值。')
  + cal('warn', '易错 4', '把用例写成「功能列表」。用例必须有参与者、前置条件、异常与结果；没有异常路径的用例通常是不完整的。')
  + cal('tip', '进阶', '能解释「需求双重功能」与「敏捷用户故事」的张力：招标要抽象、合同要详细，而用户故事既不够抽象（绑定具体交互）也不够详细（缺异常与约束），因此多团队与安全关键场景仍需系统需求文档。')),
 checklist=(h2('写与查需求的清单')
  + st('找全干系人：用户、管理者、所有者、外部（监管/工会/合作方）',
       '选获取手段：访谈（意图）+ 观察（事实）+ 场景（共识）+ 原型（反应）',
       '分类每条需求：功能 / 非功能（产品·组织·外部）/ 领域',
       '把每个目标改写成可验证需求：度量 + 条件 + 阈值',
       '写场景五要素，确保有异常路径与并发活动',
       '用用例表写清参与者、前置条件、异常、结果',
       '做五维验证：有效性、一致性、完整性、现实性、可验证性',
       '为每条需求建立追溯链接（需求 ↔ 设计 ↔ 测试）',
       '按「问题分析 → 变更分析 → 变更实现」三阶段处理变更，并记录基线')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p4–p9', '需求工程定义、需求的双重功能、Davis 抽象论述、用户需求与系统需求、读者差异'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p10–p12', '干系人类型、敏捷与需求、功能/非功能/领域需求'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p13–p19', '功能需求细节、完整性与一致性、非功能需求的重要性与实现影响、三类分类、目标与可验证需求'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p20–p34', 'RE 四个活动、获取的五个问题、获取过程四活动、访谈与问题、民族志与聚焦民族志、故事与场景'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p35–p42', '需求规格、五种表示法、需求与设计不可分、自然语言规格与写作指南、结构化与表单式规格、用例'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p43–p50', 'SRS 定义与「不是设计文档」、需求验证与 100 倍成本、五维检查、三种验证技术、变更原因、需求管理与三阶段'),
   ('11_Week 5/1_SE - Lecture 4 - 2026.pdf', 'p51–p52', '结论与要点'),
   ('（跳过）11_Week 5/2_Exercise Sessions', '全篇', 'Pearson 案例讨论说明页，案例本身已并入第 11 讲'),
   ('（补充）', '—', '非功能需求的具体度量示例与指标写法属于应用性补充，不引入新考点'))))

# ============================================================ 5
LEC.append(L(
 slug='l05-system-modelling',
 tzh='第 5 讲 · 系统建模与 UML',
 ten='System Modeling and UML',
 keywords=['system modeling', 'UML', 'context model', 'interaction model', 'use case diagram', 'sequence diagram', 'class diagram', 'generalization', 'state machine', 'model-driven engineering', 'MDA', 'CIM', 'PIM', 'PSM'],
 files=['12_Week 6/1_SE - Lecture 5 - 2026.pdf'],
 overview=(h2('本节定位')
  + p('需求讲完「要什么」，建模讲「怎么把它说清楚」。系统建模是用抽象模型从不同视角描述系统，今天几乎都用 UML 表示。这一讲给出四个视角（外部、交互、结构、行为）、五类常用图，以及一种把模型变成代码的激进思路——模型驱动工程（MDE/MDA）。')
  + p('与前后衔接：本讲的用例图与顺序图是第 4 讲需求表达工具的具体化；类图与状态图为第 6 讲的体系结构设计与第 7 讲的测试提供输入；第 13 讲的项目要求「用例图 + 用例表」，正是本讲的直接应用。')
  + p('学完本节你应当能够：')
  + ck('说出系统建模的定义与建模的三种用途（讨论、文档化、代码生成），并指出各用途对模型正确性/完整性的要求',
     '区分四个建模视角，并为给定问题选出合适的视角',
     '为给定场景画/描述用例图与顺序图，写清参与者、边界与消息顺序',
     '用类图表达类、关联与泛化，并说明泛化如何帮助管理复杂性',
     '用状态机描述一个对象对事件的响应，区分状态、事件与迁移',
     '解释 MDE 与 MDA 的差别，说出 CIM/PIM/PSM 三层模型及 MDA 采用受限的三个原因')),
 detail=(h3('5.1 系统建模是什么')
  + p('课件定义：“System modeling is the process of developing abstract models of a system, with each model presenting a different view or perspective of that system.”（开发系统的抽象模型，每个模型呈现该系统的一个不同视图或视角。）')
  + p('课件补充：今天「系统建模」几乎等于「用某种图形符号表示系统」，而这些符号几乎都基于 UML（Unified Modeling Language）。建模的作用是帮助分析人员理解系统功能，并作为与客户沟通的工具。')
  + p('模型有两种对象：')
  + tb(('模型对象', '用途', '阶段'),
       ('现有系统的模型 models of the existing system', '澄清现有系统做什么，作为讨论其优缺点的基础，进而引出新系统需求', '需求工程'),
       ('新系统的模型 models of the new system', '向其他干系人解释拟议需求；用于讨论设计方案、记录实现', '需求工程与设计'),
       ('可生成实现的模型', '在模型驱动工程中，可从模型生成完整或部分的系统实现', '设计到实现'))
  + h3('5.2 四个建模视角')
  + tb(('视角', '英文', '建什么', '常用图'),
       ('外部视角', 'external perspective', '系统的上下文或环境', '上下文模型（系统边界图）'),
       ('交互视角', 'interaction perspective', '系统与环境之间、或系统构件之间的交互', '用例图、顺序图'),
       ('结构视角', 'structural perspective', '系统的组织，或系统所处理数据的结构', '类图、构件图'),
       ('行为视角', 'behavioral perspective', '系统的动态行为及对事件的响应', '活动图、状态图'))
  + cal('tip', '记忆方法', '四视角可以对应四个问句：它和谁相邻（外部）、它和谁说话（交互）、它由什么组成（结构）、它随时间怎么变（行为）。')
  + h3('5.3 为什么要 UML')
  + p('课件先讲动机：软件工程师不断寻求自动化生产软件、提升质量、降低成本与上市时间的技术，包括构件技术、可视化编程、模式与框架，以及管理系统规模与复杂度的手段。')
  + p('另一类问题是要解决反复出现的架构难题：物理分布、并发、复制、安全、负载均衡、容错。课件指出，为万维网开发虽然简化了一些事情，却<b>加剧</b>了这些架构难题。UML 正是为回应这些需求而设计的。')
  + p('UML 设计的六个主要目标（给干系人提供）：')
  + ol('可立即使用、富有表现力的可视化建模语言，以便开发并交换有意义的模型；',
       '可扩展、可特化的机制，用于扩展核心概念；',
       '独立于特定编程语言与开发过程的通道；',
       '理解建模语言的形式基础；',
       '对更高层开发概念（协作、框架、模式、构件）的支持；',
       '整合最佳实践的基础。')
  + p('为什么 UML 图这么多？课件解释：因为我们从许多不同视角看系统，而开发中有许多角色不同的干系人——分析师、设计者、编码者、测试者、QA、客户、技术文档作者。每种角色关心不同的视图。')
  + h3('5.4 两类 UML 图')
  + tb(('类别', '英文', '定义', '包含'),
       ('结构图', 'structure diagrams', '展示系统及其各部分在不同抽象与实现层次上的静态结构，以及它们之间的关系；表达系统的有意义概念，可含抽象概念、现实世界概念与实现概念', '类图、构件图、部署图、对象图、包图'),
       ('行为图', 'behavior diagrams', '展示系统中对象的动态行为，可描述为随时间发生的一系列系统变化', '活动图、用例图、顺序图、状态图、通信图'))
  + p('课件重点介绍五类图：')
  + tb(('图', '英文', '展示什么'),
       ('活动图', 'activity diagrams', '一个过程或数据处理中涉及的活动（可用于业务流程建模）'),
       ('用例图', 'use case diagrams', '系统与其环境之间的交互'),
       ('顺序图', 'sequence diagrams', '参与者与系统之间、系统构件之间的交互（含时间顺序）'),
       ('类图', 'class diagrams', '系统中的对象类以及类之间的关联'),
       ('状态图', 'state diagrams', '系统如何对内部与外部事件作出反应'))
  + h3('5.5 模型的三类用途与正确性要求')
  + p('这是本节最容易被简化、但考试很爱考的一张对照：')
  + tb(('用途', '对模型的要求', '原因'),
       ('促进对现有或拟议系统的讨论', '<b>不完整、不正确也可以</b>', '模型的角色是支持讨论，争论过程本身产生价值'),
       ('记录现有系统', '应准确表示系统，但<b>不必完整</b>', '文档化的目的是让人理解关键结构，不是穷举'),
       ('作为可生成实现的详细系统描述', '<b>必须既正确又完整</b>', '生成器不会替你补全缺失的语义'))
  + p('一句话记法：<b>讨论可以错，文档要准，生成要全</b>。')
  + h3('5.6 系统边界与上下文模型')
  + p('系统边界（system boundary）用来界定什么在系统内、什么在系统外；上下文模型展示被使用或依赖于本系统的其他系统。关键判断是：<b>边界的位置对系统需求有深刻影响</b>。')
  + p('课件还给出一个很「社会学」的提醒：确定系统边界是<b>政治判断</b>（political judgment）——可能存在压力，要求把边界划得使某个部门的 influence 或 workload 增大或减小。这一点在答题时可以显著提升深度：边界不是技术事实，而是组织权力的投影。')
  + p('上下文模型的局限：它只展示环境中的其他系统，<b>不展示本系统在环境中如何被使用</b>。要展示后者，需要<b>过程模型</b>（process model）——过程模型揭示被开发的系统如何在更广的业务流程中被使用，可用 UML 活动图来定义业务流程模型。')
  + h3('5.7 交互模型')
  + p('课件给出三条理由：建模<b>用户交互</b>有助于识别用户需求；建模<b>系统与系统交互</b>能暴露可能出现的通信问题；建模<b>构件交互</b>帮助判断拟议的系统结构是否可能交付所需的性能与可靠性。工具是用例图与顺序图。')
  + p('<b>用例建模</b>：用例最初用于支持需求获取，后被纳入 UML。每个用例代表一个涉及与系统外部交互的<b>离散任务</b>；参与者（actor）可以是人，也可以是其他系统；用例既用图给出概览，也用更详细的文本形式描述。图中要画出<b>系统边界</b>，参与者位于边界之外。')
  + p('<b>顺序图</b>：UML 的一部分，用于建模参与者与系统内对象之间的交互；展示某个用例或用例实例中发生的交互<b>顺序</b>。参与者与对象列在图的顶部，并从它们向下画虚线（生命线）；对象之间的交互用带注释的箭头表示。')
  + cal('warn', '易错', '用例图<b>不表达顺序</b>，顺序图才表达顺序。把「先登录再下单」画进用例图是常见错误；正确做法是用例图只画参与者与用例的关联，顺序用顺序图或活动图表达。')
  + h3('5.8 结构模型与类图')
  + p('结构模型展示系统的组织：由哪些构件组成、构件之间什么关系。它可以是<b>静态模型</b>（展示设计时的结构），也可以是<b>动态模型</b>（展示运行时的组织）。结构模型通常在讨论与设计体系结构时创建。')
  + p('类图用于面向对象的系统建模：展示系统中的类以及类之间的<b>关联</b>（association）。对象类可理解为一类系统对象的通用定义；关联是类之间的链接，表明它们之间存在某种关系。在早期建模中，对象通常代表现实世界中的事物（患者、处方、医生）。')
  + p('<b>泛化（generalization）</b>是管理复杂性的日常技术：我们不必学习遇到的每个实体的细节，而是把它们归入更一般的类，学习这些类的特征，从而推断同类成员具有某些共同特征。类图中的泛化用空心三角箭头指向父类。')
  + h3('5.9 行为模型：数据驱动与事件驱动')
  + p('行为模型是系统执行时动态行为的模型，展示系统响应环境刺激时「发生了什么」或「应该发生什么」。刺激有两类：<b>数据</b>（到达并需被处理的数据）与<b>事件</b>（触发系统处理的事件，事件可能带数据，也可能不带）。')
  + tb(('类型', '适用系统', '建模方式', '例子'),
       ('数据驱动建模 data-driven modeling', '以数据处理为主、外部事件处理较少的业务系统', '展示处理输入数据并生成输出的动作序列；适合在需求分析中展示端到端处理', '工资结算、保单生成'),
       ('事件驱动建模 event-driven modeling', '实时系统，数据处理极少', '基于「系统有有限个状态、事件可引起状态迁移」的假设', '电话交换机：摘机 → 拨号音'))
  + p('<b>状态机模型</b>：建模系统对外部与内部事件的响应行为；展示系统对刺激的响应，常用于实时系统建模；把<b>系统状态画成节点、事件画成节点之间的弧</b>；事件发生时，系统从一个状态迁移到另一个状态。UML 中的状态图（statecharts）是状态机模型的表示法。')
  + h3('5.10 模型驱动工程 MDE')
  + p('MDE 是一种开发方式：<b>模型而非程序</b>是开发过程的主要产出；在硬件/软件平台上执行的程序由模型<b>自动生成</b>。支持者认为这提升了软件工程的抽象层次，使工程师不必再关心编程语言细节或执行平台的具体特性。')
  + p('<b>MDA</b>（Model-Driven Architecture）是更一般的 MDE 的前身：一种以模型为中心的软件设计与实现方法，使用 UML 模型的一个子集描述系统；在不同抽象层次上创建模型，理论上可以从高层的<b>平台无关模型</b>生成可工作程序而无需人工干预。')
  + p('三层模型（必须能区分）：')
  + tb(('模型', '英文', '描述什么', '别名/说明'),
       ('计算无关模型', 'CIM（computation independent model）', '系统中重要的领域抽象', '也称领域模型 domain model'),
       ('平台无关模型', 'PIM（platform independent model）', '系统的运行方式，不涉及实现', '通常用 UML 描述静态结构与对内外事件的响应'),
       ('平台相关模型', 'PSM（platform specific model）', '由 PIM 转换而来，针对每个应用平台各有一份', '理论上可有多层 PSM，每层增加平台相关细节'))
  + p('MDA 采用受限的三个原因：需要专门工具支持在层次间转换模型；工具可得性有限，组织可能需要改造与定制工具以适配自身环境；对于用 MDA 开发的长寿命系统，公司不愿自建工具，也不愿依赖可能倒闭的小公司。')
  + p('MDA 与敏捷的关系：MDA 的开发者声称它支持迭代开发，因而可用于敏捷；但「大量前期建模」与敏捷宣言的基本理念矛盾，敏捷开发者对 MDE 感到不适。课件给出一个条件性结论：<b>若转换能完全自动化、能从 PIM 生成完整程序，那么原则上 MDA 可用于敏捷过程，因为不再需要单独编码</b>。')),
 kws=K(('system modeling', '系统建模', 'Developing abstract models, each presenting a different view of the system.'),
       ('UML', '统一建模语言', 'A standard graphical notation; structure diagrams and behaviour diagrams.'),
       ('context model', '上下文模型', 'Shows the other systems in the environment of the system being developed.'),
       ('process model', '过程模型（业务）', 'Shows how the system is used in broader business processes; often an activity diagram.'),
       ('system boundary', '系统边界', 'Defines what is inside and outside the system; a political judgment.'),
       ('use case diagram', '用例图', 'Shows interactions between a system and its environment; actors outside the boundary.'),
       ('sequence diagram', '顺序图', 'Shows the sequence of interactions among actors and objects during a use case.'),
       ('class diagram', '类图', 'Shows object classes and the associations between them.'),
       ('association', '关联', 'A link between classes indicating some relationship.'),
       ('generalization', '泛化', 'Placing entities into more general classes to manage complexity.'),
       ('state machine model', '状态机模型', 'States as nodes, events as arcs; a statechart in UML.'),
       ('data-driven modeling', '数据驱动建模', 'Models the sequence of actions processing input data into output.'),
       ('event-driven modeling', '事件驱动建模', 'Models how the system responds to external and internal events.'),
       ('model-driven engineering', '模型驱动工程', 'Models, not programs, are the principal outputs; programs are generated.'),
       ('MDA', '模型驱动架构', 'Model-focused design using a subset of UML; CIM, PIM, PSM.'),
       ('PIM', '平台无关模型', 'Models the operation of the system without reference to its implementation.')),
 examples=(qa('例 1　为问题选视角与图',
   p('情境：某团队要做一个「图书馆自助借还」系统。四个问题：① 系统要与学校的统一身份认证、短信网关、财务系统对接，接口边界在哪？② 学生借书时，系统与自助机、后台服务之间按什么顺序交互？③ 系统里有哪些主要对象，它们之间什么关系？④ 一本书从「在架」到「借出」再到「丢失赔偿」，状态如何变化？请为每个问题选视角与图。')
   + p('<b>分析：</b>逐题抓关键词——「边界/对接」是外部视角；「按什么顺序」是交互视角；「有哪些对象/关系」是结构视角；「状态如何变化」是行为视角。')
   + p('① <b>外部视角 + 上下文模型</b>：画出系统边界，边界外放统一身份认证、短信网关、财务系统，标注数据流向。注意课件提醒：边界位置是政治判断，若把「短信通知」划进系统内，就要承担短信失败的责任。')
   + p('② <b>交互视角 + 顺序图</b>：参与者「学生」、对象「自助机界面」「借阅服务」「库存服务」「通知服务」，按时间顺序画消息：扫码 → 校验身份 → 查询可借 → 创建借阅记录 → 更新库存 → 发送凭条。')
   + p('③ <b>结构视角 + 类图</b>：Book、Copy（馆藏副本）、Loan、Member、Fine；关联：Member 1—* Loan，Loan *—1 Copy，Copy *—1 Book。')
   + p('④ <b>行为视角 + 状态图</b>：状态 InShelf、OnLoan、Overdue、Lost、Damaged；事件 borrow、return、renew、reportLost、payFine；迁移带守卫条件（如 renew 仅在未逾期时允许）。')
   + p('<b>检查：</b>四个模型是否互相矛盾？例如类图里 Copy 有状态字段，状态图的状态集合必须与之一致——这是一致性检查的典型做法。'))
  + qa('例 2　写一个用例与顺序图',
   p('情境：在线课程平台，学生可以「申请延期提交作业」。请写一个用例表，并描述对应的顺序图。')
   + p('<b>用例表：</b>ID：UC-7；名称与版本：申请作业延期，v1；参与者：学生（主要）、教师（次要）；前置条件：学生已登录、已选修该课程、作业未截止或截止未超过 7 天；描述：学生在作业页点击「申请延期」→ 选择新截止日期并填写理由 → 提交；系统校验新日期不超过课程结束日 → 生成申请单并通知教师；异常：新日期超过课程结束日则拒绝并提示；理由为空则拒绝；同一作业已有待审申请则提示不可重复提交；结果：生成一条状态为「待审」的延期申请，教师收到通知；其他需求：需网络连接；通知在 30 秒内送达。')
   + p('<b>顺序图：</b>顶部列 Student、AssignmentPage、ExtensionService、NotificationService、Teacher。消息顺序：① Student → AssignmentPage：requestExtension(newDate, reason)；② AssignmentPage → ExtensionService：validate(newDate, reason)；③ ExtensionService → ExtensionService：checkCourseEnd(newDate)（自调用，表示内部校验）；④ ExtensionService → AssignmentPage：OK / Error；⑤ AssignmentPage → ExtensionService：createRequest()；⑥ ExtensionService → NotificationService：notify(teacher, requestId)；⑦ NotificationService → Teacher：sendNotification()。')
   + p('<b>要点：</b>顺序图只画「成功路径」不够，专业做法是用 alt 片段画异常分支（校验失败时直接返回错误，不创建申请）。'))
  + qa('例 3　泛化与状态机的一致性',
   p('情境：某停车场系统有 Vehicle、Car、Truck、Motorcycle 四类对象；车位有 Free、Occupied、Reserved、OutOfService 四个状态。请说明类图中的泛化关系，并写出一个状态迁移表（至少 5 条迁移）。')
   + p('<b>泛化：</b>Car、Truck、Motorcycle 都泛化为 Vehicle；Vehicle 拥有公共属性（车牌、入场时间）与公共操作（assignSpace、calculateFee），子类特化费率计算（Truck 按轴数、Motorcycle 按次）。这样费率规则变化时只改子类，不改公共逻辑——这正是「管理复杂性」的含义。')
   + p('<b>状态迁移表：</b>')
  + tb(('当前状态', '事件', '守卫条件', '下一状态', '动作'),
       ('Free', 'reserve', '会员预约', 'Reserved', '锁定车位 15 分钟'),
       ('Reserved', 'arrive', '15 分钟内', 'Occupied', '开始计费'),
       ('Reserved', 'timeout', '超过 15 分钟', 'Free', '释放并通知'),
       ('Occupied', 'leave', '费用已结清', 'Free', '结束计费、抬杆'),
       ('Occupied', 'markFault', '设备故障', 'OutOfService', '停止计费并派单'),
       ('OutOfService', 'repairDone', '维修完成', 'Free', '恢复可用'))
  + p('<b>检查：</b>是否有「不可达状态」或「无法退出的状态」？OutOfService 必须有出口（repairDone），否则车位永久失效——这是状态机建模的常见缺陷。'))
  + qa('例 4　CIM/PIM/PSM 分层',
   p('情境：某保险公司要用 MDA 生成理赔系统。请分别举例说明 CIM、PIM、PSM 三层的内容，并说明为什么该公司可能最终放弃 MDA。')
   + p('<b>CIM：</b>「理赔案件」「保单」「受益人」「免赔额」等领域概念及其业务规则（如「同一事故 24 小时内仅可立案一次」）。这是业务人员能读懂的领域模型。')
   + p('<b>PIM：</b>用 UML 描述系统静态结构与行为——ClaimService 的接口、Claim 的状态机（Submitted → UnderReview → Approved/Rejected → Paid），不涉及 Java 还是 C#、不涉及数据库类型。')
   + p('<b>PSM：</b>针对 Java EE 平台生成 ClaimServiceBean、JPA 实体、消息队列配置；若还要支持 .NET 平台，则另有一份 PSM。')
   + p('<b>为什么可能放弃：</b>① 需要专门的模型转换工具，且要定制到公司环境；② 工具供应商多为小公司，长寿命系统不愿依赖；③ 生成的代码在性能与可维护性上未必达标，最后仍需手写；④ 保险业规则频繁变化，维护模型的成本可能高于维护代码。这正是课件所说「工具可得性有限 + 组织不愿依赖小公司」的现实版本。'))),
 practice=(ol('系统建模的四个视角是什么？各举一个 UML 图。',
         '判断：用于讨论的模型必须完整且正确。（对/错，说明理由）',
         '上下文模型与过程模型的区别是什么？为什么需要过程模型？',
         '用例图能否表达「先登录再下单」的顺序？如果不能，应改用什么图？',
         '写出状态图中「状态」「事件」「迁移」的定义，并说明守卫条件（guard）的作用。',
         'MDE 与 MDA 的关系是什么？CIM、PIM、PSM 各描述什么？')
   + det('参考答案与思路',
    p('<b>1.</b> 外部（上下文模型/系统边界图）、交互（用例图、顺序图）、结构（类图）、行为（状态图、活动图）。')
    + p('<b>2.</b> 错。课件明确：作为讨论手段时，模型不完整、不正确也可以，因为其作用是支持讨论；只有作为「可生成实现的详细描述」时才必须既正确又完整。')
    + p('<b>3.</b> 上下文模型只展示环境中的其他系统，不展示本系统如何被使用；过程模型展示系统在更广业务流程中的使用方式（常用活动图），因此能揭示跨系统的业务顺序与职责边界。')
    + p('<b>4.</b> 不能。用例图只表达参与者与用例的关联，不表达时序；时序用顺序图（或活动图）表达。')
    + p('<b>5.</b> 状态是系统在某一时刻的情形；事件是触发处理的外部或内部刺激；迁移是事件导致的从一状态到另一状态的变化。守卫条件是对迁移是否允许的布尔约束（如「仅当未逾期」），使同一事件在不同条件下走向不同状态。')
    + p('<b>6.</b> MDA 是 MDE 的前身与一个具体流派：MDE 泛指以模型为主要产出、自动生成程序；MDA 特指用 UML 子集 + CIM/PIM/PSM 分层转换。CIM 描述领域抽象，PIM 描述与平台无关的运行方式，PSM 描述特定平台上的实现细节。'))),
 exam=(cal('exam', '必考', '系统建模定义、四视角、五类图的分工、模型三类用途与正确性要求、系统边界（含政治判断）、用例与顺序图的区别、类图关联与泛化、状态机三要素、MDE/MDA 与 CIM/PIM/PSM。')
  + cal('warn', '易错 1', '把用例图当流程图用。用例图不表达顺序与分支。')
  + cal('warn', '易错 2', '认为「模型越完整越好」。完整性要求取决于用途：讨论用模型追求「够用」，代码生成用模型才追求「完整」。')
  + cal('warn', '易错 3', '把上下文模型与过程模型混为一谈。前者答「系统与谁相邻」，后者答「系统在业务流程中怎么被用」。')
  + cal('warn', '易错 4', 'MDA 三层顺序写反。记法：CIM（业务）→ PIM（逻辑）→ PSM（平台），越往下越具体。')
  + cal('tip', '进阶', '能指出「UML 图多」的根本原因不是语言冗余，而是干系人角色多样；并举例说明同一系统对分析师（用例）、编码者（类图）、测试者（状态图）需要不同视图。')),
 checklist=(h2('建模的清单')
  + st('明确建模目的：讨论 / 文档化 / 生成代码（决定正确性与完整性要求）',
       '选视角：外部 → 交互 → 结构 → 行为',
       '画系统边界，并把边界外的系统/角色列全（注意边界的组织含义）',
       '用用例图列出参与者与离散任务，每个用例配一张表（前置、异常、结果）',
       '用顺序图表达关键用例的时序，务必画异常分支（alt）',
       '用类图表达对象、关联与泛化，标注多重性',
       '用状态图表达对象生命周期，检查不可达状态与无出口状态',
       '做一致性检查：图与图之间的名称、状态、关系必须对得上')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('12_Week 6/1_SE - Lecture 5 - 2026.pdf', 'p3–p6', '学习目标、系统建模定义、现有/新系统模型、四个视角'),
   ('12_Week 6/1_SE - Lecture 5 - 2026.pdf', 'p7–p13', 'UML 的动机与设计目标、干系人角色、结构图与行为图'),
   ('12_Week 6/1_SE - Lecture 5 - 2026.pdf', 'p14–p17', '五类图、模型三类用途与正确性要求、系统边界与政治判断、过程模型'),
   ('12_Week 6/1_SE - Lecture 5 - 2026.pdf', 'p18–p23', '交互模型、用例建模、顺序图、结构模型、类图与关联、泛化'),
   ('12_Week 6/1_SE - Lecture 5 - 2026.pdf', 'p24–p27', '行为模型、数据驱动与事件驱动、状态机模型'),
   ('12_Week 6/1_SE - Lecture 5 - 2026.pdf', 'p28–p32', 'MDE、MDA、CIM/PIM/PSM、MDA 采用受限的原因、与敏捷的关系'),
   ('（跳过）', '—', '本周无纯图片或行政页需跳过'),
   ('（补充）', '—', 'UML 图清单中的构件图/部署图/对象图/包图按 UML 标准补足；课件只列五类重点图'))))
# ============================================================ 6
LEC.append(L(
 slug='l06-architectural-design',
 tzh='第 6 讲 · 软件体系结构设计',
 ten='Software Architectural Design',
 keywords=['architectural design', 'architecture in the small', 'architecture in the large', 'box and line diagram', 'architectural view', 'architectural pattern', 'MVC', 'layered architecture', 'repository architecture', 'client-server', 'pipe and filter', 'application architecture'],
 files=['13_Week 7/1_SE - Lecture 6 - 2026.pdf'],
 overview=(h2('本节定位')
  + p('需求说「做什么」，体系结构说「整体怎么组织」。这一讲回答四个问题：架构设计决策如何影响非功能属性；用什么视图来描述架构；有哪些经过验证的架构模式（MVC、分层、仓库、客户-服务器、管道-过滤器）；以及一类系统的通用架构（应用架构）。')
  + p('与前后衔接：第 5 讲的类图与构件图是描述架构的符号；本讲的「性能/安全/可用性/可维护性」与第 7 讲的非功能测试、第 10 讲的质量属性直接对应；第 12 讲的 IBM 案例（RAD 与 WAS 的接口依赖）与 Pearson 案例（服务化与团队结构）都是架构决策的现实版本。')
  + p('学完本节你应当能够：')
  + ck('说明架构设计为什么是需求工程与设计之间的关键环节',
     '针对给定非功能需求（性能、安全、安全（safety）、可用性、可维护性）选择相应的架构策略',
     '说出逻辑、开发、进程、物理、场景五种视图各自回答什么问题',
     '用「名称—描述—何时使用—优点—缺点」五段式描述五种架构模式',
     '判断一个业务系统适合分层架构还是仓库架构，并说明理由',
     '说明应用架构（application architecture）的五种用途')),
 detail=(h3('6.1 什么是体系结构设计')
  + p('课件定义：“Architectural design is concerned with understanding how a software system should be organized and designing the overall structure of that system.”（体系结构设计关注理解软件系统应如何组织，并设计该系统的整体结构。）')
  + p('它的特殊地位在于：<b>架构设计是设计与需求工程之间的关键连接</b>，因为它识别系统中的主要结构构件以及它们之间的关系。其产出是一个<b>架构模型</b>，把系统描述为一组相互通信的构件。')
  + p('课件还给出一个与敏捷有关的现实判断：普遍认为敏捷过程的早期阶段应设计<b>整体系统架构</b>；原因是<b>重构体系结构的代价很高</b>，因为它影响系统中太多构件。这与 XP「简单设计」并不矛盾——XP 反对的是过度预设计，不是反对有一次总体架构决策。')
  + h3('6.2 小架构与大架构')
  + tb(('层次', '英文', '关注对象', '问题'),
       ('程序内架构', 'architecture in the small', '单个程序', '单个程序如何分解为构件'),
       ('企业级架构', 'architecture in the large', '包含其他系统、程序、程序构件的复杂企业系统', '这些企业系统分布在不同的计算机上，而这些计算机可能由不同公司拥有和管理'))
  + p('两者的差别不只是规模，而是<b>治理边界</b>：程序内架构你可以决定一切；企业级架构中，你只能决定自己那一块，其他系统的升级节奏、接口稳定性、故障责任都不由你控制。')
  + h3('6.3 显式架构的三个好处')
  + ul('<b>干系人沟通</b>：架构可作为系统干系人讨论的焦点；',
       '<b>系统分析</b>：使「系统能否满足其非功能需求」的分析成为可能；',
       '<b>大规模复用</b>：架构可在一系列系统中复用，并可发展<b>产品线架构</b>（product-line architectures）。')
  + h3('6.4 盒线图：最常用，也最受批评')
  + p('简单、非正式的框图（box and line diagrams）是记录软件架构最常用的方法。但它受到批评：缺乏语义（lack semantics），不显示实体之间关系的<b>类型</b>，也不显示实体的可见属性；它过于抽象，既不说明构件关系的性质，也不说明子系统的外部可见属性。')
  + p('然而课件给出平衡结论：盒线图对<b>与干系人沟通</b>和<b>项目计划</b>仍然有用。这与第 5 讲「模型用途决定要求」是同一条原则：用于讨论的图不必精确，用于生成的图必须完整。')
  + p('架构模型的两类用途：一是促进对系统设计的讨论（高层视图不杂糅细节，干系人能理解抽象视图，从而不被细节干扰）；二是记录已设计的架构（目标是产出完整的系统模型，显示不同构件、它们的接口与连接）。')
  + h3('6.5 架构设计与系统特征')
  + p('架构设计是创造性过程，因系统类型而异；但有一批<b>跨所有设计过程的共同决策</b>，它们影响系统的非功能特征。课件给出五组「特征 → 策略」的对应，这是本节最高频的考点：')
  + tb(('系统特征', '架构策略（课件原句要点）', '解释'),
       ('性能 performance', 'Localise critical operations and minimise communications. Use large rather than fine-grain components.', '把关键操作局部化、最小化通信；用大粒度构件而非细粒度构件，减少跨构件调用次数'),
       ('安全 security', 'Use a layered architecture with critical assets in the inner layers.', '分层架构，把关键资产放在内层；外层被攻破时内层仍有保护'),
       ('功能安全 safety', 'Localise safety-critical features in a small number of sub-systems.', '把安全关键功能集中到少数子系统，便于验证与认证'),
       ('可用性 availability', 'Include redundant components and mechanisms for fault tolerance.', '冗余构件 + 容错机制'),
       ('可维护性 maintainability', 'Use fine-grain, replaceable components.', '细粒度、可替换构件，便于局部修改'))
  + cal('warn', '注意矛盾', '性能要「大粒度」，可维护性要「细粒度」——这两个策略方向相反。这正说明架构设计是<b>权衡</b>：先确定本项目最重要的两三个质量属性，再据此取舍。第 10 讲会以「质量属性冲突」再次强调这一点。')
  + h3('6.6 架构复用与模式')
  + p('同一领域的系统往往有相似的架构，反映该领域的核心概念；<b>应用产品线</b>（application product lines）围绕一个核心架构构建，用变体满足特定客户需求。系统架构可围绕一个或多个<b>架构模式</b>（也称风格 style）设计：模式捕捉架构的本质，并可以以不同方式实例化。')
  + p('课件的模式描述采用统一的五段式：NAME / Description / When used / Advantages / Disadvantages。答题时按这五段写，结构分基本就稳了。')
  + h3('6.7 MVC 模式')
  + tb(('项', '内容'),
       ('名称', 'MVC（Model-View-Controller）'),
       ('描述', '把表示与交互从系统数据中分离。系统分为三个逻辑构件：Model 管理数据及对数据的操作；View 定义并管理数据如何呈现给用户；Controller 管理用户交互，并把交互传给 View 与 Model。'),
       ('何时使用', '有多种方式查看与操作同一份数据时；未来对交互与呈现的需求未知时。'),
       ('优点', '数据可以独立于其表示而变化，反之亦然；支持以不同方式呈现同一数据，一处表示的修改会体现在所有表示中。'),
       ('缺点', '当数据模型与交互都很简单时，会引入额外代码与复杂度。'))
  + p('MVC 的本质是「一份数据、多种视图、一个控制器」。它解决的是「表示与数据耦合」问题，而不是「性能」问题；因此在高并发场景中，MVC 本身不提供任何性能优势。')
  + h3('6.8 分层架构')
  + p('分层架构用于建模子系统之间的接口：把系统组织成一组层（或抽象机器），每层提供一组服务。它支持在不同层中<b>增量开发子系统</b>；当某层接口变化时，只有相邻层受影响。缺点是：把系统这样分层常常是<b>人为的</b>（often artificial）。')
  + tb(('项', '内容'),
       ('名称', 'LAYERED ARCHITECTURE'),
       ('描述', '把系统组织成层，每层关联一组相关功能。一层向其<b>上层</b>提供服务，因此最底层代表贯穿系统使用的核心服务。'),
       ('何时使用', '在既有系统之上构建新设施时；开发分散在多个团队、每个团队负责一层功能时；需要多级安全（multi-level security）时。'),
       ('优点', '只要接口保持，整层可以被替换；每层可提供冗余设施以提高可靠性。'),
       ('缺点', '实践中很难在层间做干净分离，高层可能不得不直接与低层交互；性能可能成为问题，因为一个服务请求在每层都要被解释一次（multiple levels of interpretation）。'))
  + h3('6.9 仓库架构')
  + p('子系统必须交换数据，有两条路：共享数据放在中央数据库或仓库中，供所有子系统访问；或每个子系统维护自己的数据库并显式传递数据。当需要共享大量数据时，<b>仓库模型最常用</b>，因为它是高效的数据共享机制。')
  + tb(('项', '内容'),
       ('名称', 'REPOSITORY'),
       ('描述', '系统中所有数据由一个中央仓库管理，所有系统构件都可访问；构件之间不直接交互，只通过仓库交互。'),
       ('何时使用', '系统产生大量需长期保存的信息时；数据驱动系统中「数据进入仓库触发动作或工具」时。'),
       ('优点', '构件相互独立，不需要知道其他构件存在；一个构件做的修改可传播到所有构件；数据集中管理，一致性容易保证。'),
       ('缺点', '仓库是<b>单点故障</b>，仓库出问题影响整个系统；所有通信都经由仓库可能低效；把仓库分布到多台计算机上可能很困难。'))
  + h3('6.10 客户-服务器架构')
  + p('客户-服务器是分布式系统模型，展示数据与处理如何分布在一组构件上；它可以在单台计算机上实现。组成是：一组提供特定服务（打印、数据管理）的独立服务器；一组调用这些服务的客户；以及允许客户访问服务器的网络。')
  + tb(('项', '内容'),
       ('名称', 'CLIENT-SERVER'),
       ('描述', '把系统功能组织成服务，每个服务由独立服务器提供；客户是这些服务的使用者，通过访问服务器来使用它们。'),
       ('何时使用', '需要从多个位置访问共享数据库中的数据时；由于服务器可复制，也用于系统负载可变时。'),
       ('优点', '服务器可分布到网络上；通用功能可对所有客户可用，不需要每个服务都实现一遍。'),
       ('缺点', '每个服务都是单点故障，易受拒绝服务攻击或服务器故障影响；性能不可预测，因为它同时取决于网络与系统；若服务器由不同组织拥有，可能有管理问题。'))
  + h3('6.11 管道-过滤器架构')
  + p('功能变换把输入处理成输出，这类架构可称为管道-过滤器模型（如 UNIX shell）。变体非常常见：当变换是顺序的，就是<b>批顺序模型</b>（batch sequential model），广泛用于数据处理系统。它<b>不太适合交互式系统</b>。')
  + tb(('项', '内容'),
       ('名称', 'PIPE AND FILTER'),
       ('描述', '把数据处理组织成：每个处理构件（过滤器）是离散的，执行一种数据变换；数据像在管道中一样从一个构件流到另一个构件处理。'),
       ('何时使用', '数据处理应用中，输入分阶段处理并生成相关输出时。'),
       ('优点', '易理解，支持变换复用；工作流风格匹配许多业务流程的结构；通过增加变换来演化很直接；可实现为顺序或并发系统。'),
       ('缺点', '通信的变换之间必须就<b>数据传输格式</b>达成一致；每个变换必须解析其输入、反解析其输出为约定格式；这增加系统开销，并可能使使用不兼容数据结构的变换无法复用。'))
  + h3('6.12 架构视图')
  + p('设计架构时要问两个问题：哪些视图或视角有用？用什么符号描述架构模型？关键前提是：<b>每个架构模型只展示系统的一个视图或视角</b>。')
  + p('表示法之争：有人认为 UML 适合描述与记录系统架构；<b>架构描述语言</b>（ADLs）已被开发出来，但并未被广泛使用。')
  + p('五种视图（课件逐一介绍，必须能对上「视图—回答的问题」）：')
  + tb(('视图', '英文', '回答什么问题', '内容要点'),
       ('逻辑视图', 'logical view', '系统向用户提供哪些服务（功能需求）', '把系统分解为一组关键抽象，多来自问题域，以对象或对象类的形式表示；是功能的蓝图（如空管系统的逻辑视图）'),
       ('开发视图', 'development view', '软件在开发环境中如何组织', '关注实际的软件模块组织：软件被打包成可由一个或少数开发者开发的块（程序库、子系统）；关注子系统分解'),
       ('进程视图', 'process view', '运行时并发与分布如何安排', '考虑性能、可用性等非功能需求；处理并发与分布、系统完整性、容错，以及逻辑视图中的主要抽象落在哪个控制线程上执行'),
       ('物理视图', 'physical view', '软件如何映射到硬件节点', '主要考虑可用性、可靠性（容错）、性能（吞吐）、可扩展性；软件运行在一组计算机或处理节点（nodes）组成的网络上'),
       ('场景视图', 'scenarios', '用具体用例把各视图串起来', '用若干场景（如一次本地通话的选路阶段）验证架构能否支撑真实使用'))
  + h3('6.13 应用架构')
  + p('应用系统是为满足组织需要而设计的。由于业务有许多共同点，其应用系统也往往有<b>共同架构</b>，反映应用需求。<b>通用应用架构</b>（generic application architecture）是某一类软件系统的架构，可被配置与适配，以构建满足特定需求的系统。')
  + p('应用架构的五种用途：作为架构设计的起点；作为设计检查清单；作为组织开发团队工作的方式；作为评估构件可复用性的手段；作为讨论应用类型的词汇表。')
  + p('信息系统架构：信息系统有一个通用架构，可组织为分层架构；它们是<b>基于事务的系统</b>，因为与这些系统的交互通常涉及数据库事务。层包括：用户界面、用户通信、信息检索、系统数据库。')
  + p('另一种更常见的四层划分（课件后一页）：')
  + tb(('层', '职责'),
       ('表示层 Presentation Layer', '负责用户与软件系统的交互'),
       ('应用/业务层 Application/Business Layer', '处理与完成功能需求相关的方面'),
       ('领域层 Domain Layer', '负责算法与程序构件'),
       ('基础设施/持久化/数据库层 Infrastructure/Persistence/Database Layer', '负责处理数据与数据库'))
  + p('注意两层「分层」说法的差别：前者按「界面—通信—检索—数据库」的技术栈切分，后者按「表示—业务—领域—基础设施」的职责切分。答题时先说明采用哪一种切分口径，再展开。')),
 kws=K(('architectural design', '体系结构设计', 'Understanding how a system should be organised and designing its overall structure.'),
       ('architecture in the small', '程序内架构', 'Architecture of individual programs: how one program is decomposed.'),
       ('architecture in the large', '企业级架构', 'Architecture of complex enterprise systems including other systems, possibly owned by different companies.'),
       ('box and line diagram', '盒线图', 'Informal block diagram; lacks semantics but useful for communication and planning.'),
       ('architectural pattern', '架构模式', 'A stylised description of good design practice tried in different environments.'),
       ('MVC', '模型-视图-控制器', 'Separates presentation and interaction from system data.'),
       ('layered architecture', '分层架构', 'Layers of related functionality; each layer provides services to the layer above.'),
       ('repository architecture', '仓库架构', 'All data managed in a central repository; components interact only through it.'),
       ('client-server', '客户-服务器', 'Services delivered by separate servers; clients access them over a network.'),
       ('pipe and filter', '管道-过滤器', 'Each processing component performs one transformation; data flows between them.'),
       ('application architecture', '应用架构', 'A generic architecture for a type of software system, configurable for specific requirements.'),
       ('architectural view', '架构视图', 'Logical, development, process, physical and scenario views; each shows one perspective.'),
       ('single point of failure', '单点故障', 'One component whose failure brings down the whole system, e.g. a repository or a server.')),
 examples=(qa('例 1　按非功能需求选策略',
   p('情境：某证券行情系统要求：① 行情推送端到端延迟 < 100 ms；② 交易指令必须防止越权；③ 系统全年可用性 99.99%；④ 策略模块需每周更新并可独立上线。请为每条需求给出架构策略。')
   + p('<b>分析：</b>逐条对应课件的「特征 → 策略」表。')
   + p('① 性能 → <b>局部化关键操作、最小化通信、使用大粒度构件</b>。具体做法：把行情解析与推送放在同一进程内，避免跨进程序列化；用批量推送代替逐条推送。')
   + p('② 安全 → <b>分层架构、关键资产在内层</b>。具体做法：把指令校验与签名放在最内层，外层网关只做限流与鉴权；即使外层被攻破，内层仍需独立授权。')
   + p('③ 可用性 → <b>冗余构件 + 容错机制</b>。具体做法：推送服务双活、数据库主备 + 自动切换、关键链路熔断降级。')
   + p('④ 可维护性 → <b>细粒度、可替换构件</b>。具体做法：策略模块做成独立服务/插件，定义稳定接口，支持灰度与回滚。')
   + p('<b>冲突提示：</b>①要「大粒度」，④要「细粒度」——两者在同一系统里冲突。可行解是分层处理：行情链路用大粒度，策略模块用细粒度，并在架构文档中明确这条权衡。'))
  + qa('例 2　MVC 与分层，选哪个',
   p('情境：某高校要做「教师工作量统计」系统：数据来自教务、科研、人事三个库；同一份数据要给教师看（明细）、给院长看（汇总）、给人事看（报表导出）。请选架构模式并说明理由。')
   + p('<b>分析：</b>先抓「同一份数据的多种表示」这个特征——这是 MVC 的典型适用条件；再抓「多来源数据 + 事务一致性」——这是仓库架构的适用条件。两者并不互斥：系统整体可用仓库，表示层用 MVC。')
   + p('<b>方案：</b>总体采用<b>仓库架构</b>：建立中央工作量数据仓库，从三个源系统抽取、清洗、汇总；各前端不直接连源库，只读仓库。表示层采用 <b>MVC</b>：Model 是工作量数据与聚合逻辑，View 分别是教师明细页、院长看板、人事报表，Controller 处理筛选与导出请求。')
   + p('<b>理由：</b>仓库避免三套口径不一致（数据集中、可一致管理），并使前端与源系统解耦；MVC 使三种视图共享同一模型，修改一处表示不影响其他。')
   + p('<b>风险：</b>仓库是单点故障，且抽取任务失败会导致数据陈旧——需加监控与重跑机制；这正是仓库模式「缺点」栏的内容。'))
  + qa('例 3　管道-过滤器还是客户-服务器',
   p('情境：某银行每晚要处理百万级交易流水：解析 → 反洗钱规则匹配 → 计费 → 汇总 → 生成报表。另有柜员需要实时查询单笔交易状态。请判断两类需求分别适合什么架构。')
   + p('<b>分析：</b>批处理链路是「顺序变换、输入分阶段处理、生成相关输出」——正是管道-过滤器的定义场景（顺序时称批顺序模型）。实时单笔查询是「从多个位置访问共享数据」——正是客户-服务器的适用条件。')
   + p('<b>方案：</b>批处理链路用<b>管道-过滤器</b>：每个过滤器只做一种变换，中间结果用约定格式（如 Avro/Parquet）落盘；新增反欺诈规则时只需插入一个过滤器，符合「通过增加变换来演化很直接」的优点。实时查询用<b>客户-服务器</b>：查询服务作为服务器，柜员终端作为客户。')
   + p('<b>注意管道-过滤器的代价：</b>相邻过滤器必须就数据格式达成一致，每个过滤器都要解析输入、反解析输出，开销不小；若某一步骤需要全局状态（如跨笔交易的关联分析），纯管道模型会很别扭，需要引入共享存储。'))
  + qa('例 4　用五种视图描述一个架构',
   p('情境：请用逻辑、开发、进程、物理、场景五种视图描述一个「在线考试系统」，每个视图写两句话。')
   + p('<b>逻辑视图：</b>系统由 Exam、Question、AnswerSheet、Grading、Proctor 等关键抽象组成；Exam 聚合 Question，AnswerSheet 关联 Exam 与 Student。它回答「系统向用户提供哪些服务」。')
   + p('<b>开发视图：</b>代码分为 exam-core、grading-engine、web-api、web-ui 四个模块，分别由 2–3 人小组开发；grading-engine 以独立库形式被 web-api 依赖。它回答「开发环境里如何分包」。')
   + p('<b>进程视图：</b>web-api 多实例部署于负载均衡之后；grading-engine 作为独立进程消费阅卷队列，支持水平扩容；考试进行中禁止重启 web-api。它回答「并发与分布如何安排」。')
   + p('<b>物理视图：</b>web-api 与数据库部署在主数据中心，阅卷集群部署在可弹性伸缩的云区域；数据库跨可用区主备。它回答「软件映射到哪些节点」。')
   + p('<b>场景视图：</b>场景「考试开始前 5 分钟 3000 名学生同时进入」：负载均衡 → web-api 扩容 → 题库缓存预热 → 数据库连接池打满告警。它用具体用例验证其他四个视图能否支撑真实负载。')
   + p('<b>要点：</b>五个视图不是五份文档，而是同一架构的五个投影；写完后要检查它们是否矛盾（例如进程视图说「多实例」，逻辑视图就不能假设单例状态）。'))),
 practice=(ol('为什么说架构设计是需求工程与设计之间的关键连接？',
         '写出五种「系统特征 → 架构策略」的对应关系。',
         '分层架构的两条主要缺点是什么？为什么说「分层常常是人为的」？',
         '仓库架构与客户-服务器架构在「单点故障」上的表现有何不同？',
         'MVC 的三个构件各负责什么？什么情况下不宜用 MVC？',
         '应用架构的五种用途是什么？')
   + det('参考答案与思路',
    p('<b>1.</b> 因为架构设计识别系统的主要结构构件及其关系，从而把「需求（尤其非功能需求）」翻译成「结构决策」；它同时为详细设计与需求验证提供依据，因此是两者的连接点。')
    + p('<b>2.</b> 性能 → 局部化关键操作、最小化通信、大粒度构件；安全 → 分层并把关键资产放内层；功能安全 → 把安全关键功能集中到少数子系统；可用性 → 冗余 + 容错；可维护性 → 细粒度可替换构件。')
    + p('<b>3.</b> ①很难做干净分离，高层可能被迫直接访问低层；②性能受损，因为请求在每层都被解释一次。说它「人为」是因为业务本身未必是层状的，分层往往是为了组织开发与安全而强加的结构。')
    + p('<b>4.</b> 仓库的单点故障是「数据层」的：仓库一坏，所有构件都失效；客户-服务器的单点故障是「每个服务各自」的：一个服务坏，只影响该服务，但该服务完全不可用，且易受拒绝服务攻击。前者影响面更广，后者更易被针对性攻击。')
    + p('<b>5.</b> Model 管理数据及操作；View 定义并管理数据如何呈现；Controller 管理用户交互并转发给 View 与 Model。数据模型与交互都很简单时不宜用，因为会引入不必要的代码与复杂度。')
    + p('<b>6.</b> 架构设计起点、设计检查清单、组织团队工作的方式、评估构件可复用性的手段、讨论应用类型的词汇表。'))),
 exam=(cal('exam', '必考', '体系结构设计的定义与「关键连接」地位、五种特征-策略对应、五种视图的分工、五种模式的五段式描述（尤其 MVC 与分层）、应用架构的五种用途。')
  + cal('warn', '易错 1', '把「安全 security」与「功能安全 safety」的策略混用。前者靠分层与内层保护，后者靠把安全关键功能集中到少数子系统。')
  + cal('warn', '易错 2', '认为分层架构总能提高性能。相反，多层解释会拖慢请求；分层换来的是可替换性与可维护性。')
  + cal('warn', '易错 3', '把「盒线图没有语义」当成「盒线图没用」。课件明确它在沟通与项目计划中仍有用。')
  + cal('warn', '易错 4', '认为每个架构模型应展示系统的全部视图。课件明确：每个模型只展示一个视图。')
  + cal('tip', '进阶', '能用「性能要大粒度、可维护要细粒度」这一对矛盾说明架构设计的权衡本质，并给出「分层处理不同链路」的解法，是论述题的高分点。')),
 checklist=(h2('做架构决策的清单')
  + st('列出最重要的 2–3 个质量属性（不要试图全优）',
       '为每个属性选策略：性能（局部化/大粒度）、安全（分层/内层）、安全（集中）、可用性（冗余）、可维护性（细粒度）',
       '选模式并写出五段式：名称、描述、何时使用、优点、缺点',
       '画五种视图，每个视图只回答自己的问题',
       '检查视图间一致性（多实例 vs 单例状态、层数 vs 部署节点）',
       '标注单点故障与故障影响面',
       '记录被否决的方案与理由（架构决策记录）',
       '用 2–3 个场景走查架构，验证它能否支撑真实负载')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('13_Week 7/1_SE - Lecture 6 - 2026.pdf', 'p4–p9', '架构设计定义与关键连接地位、敏捷与架构、程序内/企业级架构、显式架构的三好处、盒线图'),
   ('13_Week 7/1_SE - Lecture 6 - 2026.pdf', 'p10–p13', '设计决策、架构复用与产品线、五种特征-策略对应、架构视图的表示法（UML 与 ADL）'),
   ('13_Week 7/1_SE - Lecture 6 - 2026.pdf', 'p14–p23', '逻辑视图、开发视图、进程视图、物理视图、场景视图'),
   ('13_Week 7/1_SE - Lecture 6 - 2026.pdf', 'p24–p36', '模式的定义、MVC、分层、仓库、客户-服务器、管道-过滤器（五段式）'),
   ('13_Week 7/1_SE - Lecture 6 - 2026.pdf', 'p37–p41', '应用架构定义与五种用途、信息系统分层、四层职责划分'),
   ('（跳过）', '—', '本周无纯图片或行政页需跳过'),
   ('（补充）', '—', '分层「人为性」的具体解释与视图一致性检查属应用性补充'))))

# ============================================================ 7
LEC.append(L(
 slug='l07-testing-and-quality',
 tzh='第 7 讲 · 软件测试与质量管理',
 ten='Software Testing and Quality Management',
 keywords=['verification', 'validation', 'defect testing', 'inspection', 'unit testing', 'component testing', 'interface testing', 'system testing', 'test-driven development', 'release testing', 'acceptance testing', 'equivalence partitioning', 'stress testing', 'software quality management'],
 files=['16_Week 10/1_SE - Lecture 7 - 2026.pdf', '19_Week 13/3_Exercise Session 3 (1).pdf'],
 overview=(h2('本节定位')
  + p('这一讲回答两个问题：怎么知道软件「做对了」（测试），以及怎么保证「持续做对」（质量管理）。测试部分是全课实践性最强的内容：从单元测试到发布测试、从等价类划分到压力测试、从 TDD 到验收测试。质量部分给出 SQM 的定义与度量的作用，为第 10 讲的质量标准与配置管理铺垫。')
  + p('与前后衔接：第 3 讲把「验证」列为四项活动之一，本讲展开；第 5 讲的状态图与用例是设计测试用例的输入；第 12 讲 EXCEED 案例是「系统测试效率低下」的真实诊断；本讲的等价类划分与接口错误分类是期末考试的高频计算/分析题。')
  + p('学完本节你应当能够：')
  + ck('区分验证（verification）与确认（validation），并说明两者各自回答的问题',
     '区分「确认测试」与「缺陷测试」，并解释「成功的测试」在两种语境下的不同含义',
     '为给定输入域设计等价类划分，并写出边界用例',
     '列出四种接口类型与三类接口错误，并给出一个具体例子',
     '描述 TDD 的循环步骤与四项收益，并说明它为何不保证测试完备',
     '区分开发测试、发布测试、用户测试（alpha/beta/acceptance）的目的与执行者')),
 detail=(h3('7.1 测试要做什么、不能做什么')
  + p('课件开篇的定义很克制：“Testing is intended to show that a program does what it is intended to do and to discover program defects before it is put into use.”（测试旨在表明程序做了它该做的事，并在投入使用前发现缺陷。）')
  + p('做法是：用<b>人工数据</b>（artificial data）执行程序，检查运行结果中的错误、异常，或获取程序非功能属性的信息。')
  + p('最关键的一句判断是：测试可以揭示错误的<b>存在</b>，但不能证明错误的<b>不存在</b>（“Can reveal the presence of errors not their absence.”）。这就是为什么测试永远不能等同于「正确性证明」，也是为什么需要把测试看作更广的 V&amp;V 过程的一部分——V&amp;V 还包括静态验证技术（评审、检查、形式化分析）。')
  + h3('7.2 测试的两个目标，导出两种测试')
  + p('课件给出两个目标，并明确它们导出两种完全不同的测试：')
  + tb(('目标', '导出', '测试用例设计', '「成功」的含义'),
       ('向开发者与客户证明软件满足其需求', '确认测试 validation testing', '用例反映系统的<b>预期使用</b>', '测试成功 = 系统按预期工作'),
       ('发现软件行为不正确、不期望或不符合规格的情形', '缺陷测试 defect testing', '用例被设计来<b>暴露缺陷</b>', '测试成功 = 让系统出错并暴露缺陷'))
  + p('对定制软件，第一个目标意味着「需求文档中的每条需求至少有一个测试」；对通用产品，意味着「产品发布中包含的所有功能及其组合都有测试」。第二个目标关注崩溃、与其他系统的不良交互、错误计算、数据损坏等。')
  + cal('exam', '必考', '「成功的测试」在两种语境下含义相反：确认测试里「通过」是成功；缺陷测试里「让系统失败」才是成功。这是最经典的陷阱题。')
  + p('课件还给出一个「程序测试的输入-输出模型」：测试用例是输入 + 期望输出；执行后比较实际输出与期望输出；差异即缺陷线索。这个模型看似简单，实际难点在于「输入空间无限、期望输出难以判定」。')
  + h3('7.3 验证与确认')
  + p('课件用两句口号区分：')
  + ul('<b>Verification</b>：“Are we building the product right?”（我们是否把产品<b>做对</b>了？）软件应符合其规格。',
       '<b>Validation</b>：“Are we building the right product?”（我们是否在做<b>对的产品</b>？）软件应做用户真正需要的事。')
  + p('V&amp;V 的目标是建立「适用于目的」（fit for purpose）的信心。信心水平取决于三件事：')
  + ul('<b>软件用途</b>：软件对组织越关键，所需信心越高；',
       '<b>用户期望</b>：用户对某类软件可能期望很低（例如免费工具），于是「够用」即可；',
       '<b>市场环境</b>：早上市可能比多找几个缺陷更重要。')
  + p('最后一条很现实：V&amp;V 的强度不是纯技术决策，而是商业决策。答题时能指出这一点，往往能加分。')
  + h3('7.4 检查与测试：互补而非对立')
  + tb(('手段', '英文', '做什么', '类型'),
       ('软件检查', 'software inspections', '分析系统的<b>静态表示</b>以发现问题', '静态验证 static verification'),
       ('软件测试', 'software testing', '执行并观察产品行为', '动态验证 dynamic verification'))
  + p('课件明确：二者互补，不是对立的技术，V&amp;V 过程中都应使用。检查能检查「是否符合规格」，但<b>不能</b>检查「是否符合客户真实需求」；检查<b>不能</b>检查性能、可用性等非功能特性。')
  + p('检查的做法：由人检查源表示，目的是发现异常与缺陷；不需要执行系统，因此可在实现之前使用；可应用于系统的任何表示（需求、设计、配置数据、测试数据）；已被证明是发现程序错误的有效技术。')
  + p('检查的三个优势（高频考点）：')
  + ol('测试中错误会<b>掩盖</b>（mask）其他错误；检查是静态过程，不必担心错误之间的相互作用；',
       '不完整的版本可以低成本地被检查；若程序不完整，测试需要专门搭建测试夹具（test harness）才能测可用部分；',
       '除寻找缺陷外，检查还能评估更广的质量属性：是否符合标准、可移植性、可维护性。')
  + h3('7.5 三个阶段：开发测试、发布测试、用户测试')
  + tb(('阶段', '英文', '谁做', '目的'),
       ('开发测试', 'development testing', '开发团队', '开发过程中发现 bug 与缺陷'),
       ('发布测试', 'release testing', '独立的测试团队', '在交付用户前测试完整版本'),
       ('用户测试', 'user testing', '用户或潜在用户', '在用户自己的环境中测试'))
  + h3('7.6 开发测试：单元、构件、系统')
  + p('开发测试包含开发团队执行的所有测试活动，分三层，重点各不相同：')
  + tb(('层次', '对象', '关注点'),
       ('单元测试 unit testing', '单个程序单元或对象类', '对象或方法的功能'),
       ('构件测试 component testing', '若干单元集成的复合构件', '构件<b>接口</b>'),
       ('系统测试 system testing', '系统中部分或全部构件集成后作为整体', '构件之间的<b>交互</b>'))
  + p('单元测试是在隔离状态下测试单个构件，属缺陷测试过程。单元可以是：对象内的单个函数或方法；含多个属性与方法的对象类；带定义接口的复合构件。')
  + p('对象类测试的完整覆盖包含三件事：测试与对象相关的<b>所有操作</b>；设置并查询<b>所有属性</b>；让对象经历<b>所有可能状态</b>。课件提醒：<b>继承使对象类测试更难设计</b>，因为要测的信息不局限在一个类中（父类行为、子类覆盖、多态分派都要考虑）。')
  + p('自动化单元测试：尽可能自动化，使测试无需人工干预即可运行与检查。使用测试自动化框架编写与运行测试；框架提供通用测试类，你继承它来创建具体测试用例，然后运行所有已实现的测试并报告结果。')
  + p('自动化测试的三个组成部分（必须能背）：')
  + ol('<b>setup</b>：用测试用例（输入与期望输出）初始化系统；',
       '<b>call</b>：调用被测试的对象或方法；',
       '<b>assertion</b>：比较调用结果与期望结果；断言为真则测试成功，为假则失败。')
  + h3('7.7 测试策略：划分与准则')
  + p('两种策略：')
  + ul('<b>划分测试 partition testing</b>：识别具有共同特征、应以相同方式处理的输入组，从每组中各选测试；',
       '<b>基于准则的测试 guideline-based testing</b>：用测试准则选择用例，这些准则反映「程序员在开发构件时常犯何种错误」的经验。')
  + p('<b>等价类划分</b>（equivalence partitioning，也称 ECP，equivalence class partitioning）：输入数据与输出结果常落入不同的类，同一类的所有成员行为等价；每个这样的类是一个<b>等价分区</b>或<b>域</b>；测试用例应从每个分区中各取。它属于<b>黑盒测试</b>：把输入域划分为数据类，据此类推导测试用例。')
  + cal('tip', '技巧', '等价类划分的正确姿势是「先分有效类与无效类，再对每个类取一个代表值，最后补边界值」。只取「正常值」是常见失分点——无效类（负数、超长字符串、空值）往往才是缺陷所在。')
  + h3('7.8 构件测试与接口测试')
  + p('软件构件常是由多个交互对象组成的复合构件；你通过定义的构件接口访问这些对象的功能。因此测试复合构件应聚焦于「构件接口是否按其规格行事」——可以假定构件内各对象的单元测试已完成。')
  + p('接口测试的目标：发现因接口错误或对接口的错误假设而导致的缺陷。四种接口类型：')
  + tb(('接口类型', '英文', '含义', '例子'),
       ('参数接口', 'parameter interfaces', '数据从一个方法或过程传给另一个', '函数调用传参'),
       ('共享内存接口', 'shared memory interfaces', '一块内存在过程或函数间共享', '共享缓冲区、全局状态'),
       ('过程接口', 'procedural interfaces', '子系统封装一组过程供其他子系统调用', 'SDK、库 API'),
       ('消息传递接口', 'message passing interfaces', '子系统向其他子系统请求服务', 'REST 调用、消息队列'))
  + p('三类接口错误：')
  + tb(('错误', '英文', '定义', '例子'),
       ('接口误用', 'interface misuse', '调用构件在使用接口时出错', '参数顺序传反、单位不一致（毫秒当秒）'),
       ('接口误解', 'interface misunderstanding', '调用构件对被调用构件的行为嵌入了错误假设', '假设返回列表有序、假设失败时抛异常（实际返回 null）'),
       ('时序错误', 'timing errors', '被调用与调用构件速度不同，读到过期信息', '生产者写入频率高于消费者读取，读到半写状态'))
  + h3('7.9 系统测试')
  + p('系统测试在开发中整合构件、创建系统版本，然后测试整合后的系统。焦点是<b>构件之间的交互</b>：检查构件是否兼容、是否正确交互、是否在正确的时间通过接口传递正确的数据。系统测试测试的是系统的<b>涌现行为</b>（emergent behaviour）——只有把部件组合起来才会出现的行为（如死锁、竞态、端到端延迟）。')
  + h3('7.10 测试驱动开发 TDD')
  + p('TDD 是把测试与编码<b>交织</b>的开发方式：测试先于代码编写，「通过测试」是开发的关键驱动；你增量地开发代码，同时为该增量写测试；在当前增量通过测试之前，不进入下一个增量。TDD 最初作为 XP 等敏捷方法的一部分出现，但<b>也可用于计划驱动过程</b>。')
  + p('TDD 循环五步（必须能按序写出）：')
  + ol('识别所需的功能增量——通常应当很小，几行代码即可实现；',
       '为该功能写一个测试，并实现为自动化测试；',
       '运行该测试以及所有其他已实现的测试——此时功能未实现，新测试必然失败；',
       '实现功能并重新运行测试；',
       '所有测试通过后，进入下一块功能。')
  + p('TDD 的四项收益：')
  + ul('<b>代码覆盖率</b>：你写的每段代码都至少有一个相关测试，因此所有代码至少被一个测试覆盖；',
       '<b>回归测试</b>：回归测试套件随程序开发增量建立；',
       '<b>简化调试</b>：测试失败时问题位置显而易见——只需检查并修改新写的代码；',
       '<b>系统文档</b>：测试本身是一种文档，描述代码应该做什么。')
  + p('但要记住第 2 讲的问题清单：程序员可能写不完整的测试；界面与工作流的测试难以增量编写；<b>测试集的完备性难以判断</b>。TDD 保证「写了的代码被测」，不保证「该测的都测了」。')
  + h3('7.11 发布测试')
  + p('发布测试针对「打算在开发团队之外使用的某个系统发布版本」。其首要目标是<b>说服系统的供应方相信它足够好用</b>：必须表明系统交付了规定的功能、性能与可靠性，并且在正常使用中不会失败。')
  + p('发布测试通常是<b>黑盒测试</b>：测试只从系统规格导出。它与系统测试的重要差别有两条：')
  + ul('应由<b>未参与开发</b>的独立团队负责；',
       '开发团队的系统测试以<b>发现缺陷</b>为目的（缺陷测试）；发布测试的目的是<b>确认系统满足需求、足够好用</b>（确认测试）。')
  + p('性能测试属于发布测试的一部分，用于测试系统的涌现属性（性能、可靠性）。测试应反映系统的<b>使用剖面</b>（profile of use）；通常规划一系列测试，负载逐步增加直到性能不可接受。<b>压力测试</b>（stress testing）是性能测试的一种：故意让系统过载，以测试其失效行为。')
  + h3('7.12 用户测试')
  + p('用户测试（或客户测试）是用户/客户对系统测试提供输入与建议的阶段。即使做了充分的系统测试与发布测试，用户测试仍然必要——因为<b>用户工作环境的影响</b>对系统的可靠性、性能、可用性、健壮性有很大作用，而这些无法在测试环境中复制。')
  + tb(('类型', '英文', '谁在哪测', '适用'),
       ('alpha 测试', 'alpha testing', '软件的用户与开发团队一起，在<b>开发者场所</b>测试', '通用产品与定制系统均可'),
       ('beta 测试', 'beta testing', '把软件发布给用户，让其在真实环境试用并向开发者报告问题', '通用产品常用'),
       ('验收测试', 'acceptance testing', '客户测试系统，决定是否从开发者手中接受并部署到客户环境', '主要针对定制系统'))
  + p('敏捷与验收测试：在敏捷方法中，用户/客户是开发团队的一员，负责判断系统可接受性；测试由用户/客户定义，并与其他测试集成——变更时自动运行；因此<b>没有独立的验收测试过程</b>。主要问题是：嵌入的用户是否「典型」，能否代表所有干系人的利益。')
  + h3('7.13 软件质量管理 SQM')
  + p('课件定义：SQM 是确保软件在功能、可靠性、用户满意度方面达到最高标准的系统化过程；是对软件开发生命周期、部署与维护各方面进行监督与改进的守纪律方法，以确保最终产品达到或超过用户期望。它涵盖关注功能、性能、可靠性、用户满意度的过程、标准与实践。')
  + p('SQM 强调<b>持续改进</b>：把质量改进融入开发过程直到达到期望；目标是营造「质量是团队每个人责任」的工作环境。它的重要性在于帮助识别并纠正错误，而这对项目有效实施至关重要——「软件质量就是产品满足你需要的程度的度量」。')
  + p('SQM 度量（metrics）是用于评估开发、部署、维护各方面的定量测量，提供客观数据以评价产品、过程与团队的质量。度量以可执行的洞察揭示产品、过程与项目的健康状况，使你能够：制定更好的策略指导项目生命周期；识别所有需要关注的领域；做出由策略与业务信息驱动的决策。')
  + h3('7.14 质量维度与测试类型（练习课补充）')
  + p('第 13 周练习课给出两张对照表，考试可能直接引用：')
  + tb(('质量维度', '说明'),
       ('功能性 functionality', '软件是否按需求正确、完整地工作'),
       ('可靠性 reliability', '在不同条件下持续运行的能力；低错误率'),
       ('可维护性 maintainability', '代码易读、易改、易扩展'),
       ('性能 performance', '响应时间、吞吐量、资源利用率'),
       ('可用性 usability', '界面友好、操作简单'),
       ('安全性 security', '防止数据泄露与未授权访问'))
  + tb(('测试类型', '目的'),
       ('单元测试 unit testing', '测试最小功能单元的正确性'),
       ('集成测试 integration testing', '验证模块之间的接口与交互'),
       ('系统测试 system testing', '检查整个系统是否满足需求'),
       ('验收测试 acceptance testing', '确认软件满足用户或客户需要'),
       ('回归测试 regression testing', '确保代码变更不引入新缺陷'))
  + p('练习课还要求讨论「哪些测试可自动化、哪些更适合人工」：回归、单元、接口通常可自动化；探索性测试、可用性测试、验收中的业务判断更适合人工。这个判断在第 11 讲的 CI 流水线设计中会再次使用。')),
 kws=K(('verification', '验证', 'Are we building the product right? Conform to specification.'),
       ('validation', '确认', 'Are we building the right product? Do what the user really requires.'),
       ('defect testing', '缺陷测试', 'Test cases designed to expose defects; a successful test makes the system fail.'),
       ('software inspection', '软件检查', 'Static analysis of representations by people, without executing the system.'),
       ('unit testing', '单元测试', 'Testing individual components in isolation; a defect testing process.'),
       ('component testing', '构件测试', 'Testing composite components, focusing on component interfaces.'),
       ('interface misuse', '接口误用', 'A calling component makes an error in using the interface, e.g. wrong parameter order.'),
       ('interface misunderstanding', '接口误解', 'The caller embeds incorrect assumptions about the called component’s behaviour.'),
       ('timing error', '时序错误', 'Components operate at different speeds and out-of-date information is accessed.'),
       ('system testing', '系统测试', 'Testing integrated components; focus on interactions and emergent behaviour.'),
       ('test-driven development', '测试驱动开发', 'Tests written before code; passing tests drives development.'),
       ('release testing', '发布测试', 'Black-box testing of a release by an independent team to show it is good enough for use.'),
       ('stress testing', '压力测试', 'Deliberately overloading the system to test its failure behaviour.'),
       ('acceptance testing', '验收测试', 'Customers decide whether to accept the system for deployment.'),
       ('equivalence partitioning', '等价类划分', 'Dividing the input domain into classes that behave equivalently; pick one test per class.'),
       ('software quality management', '软件质量管理', 'A systematic process ensuring software meets standards of functionality, reliability and satisfaction.')),
 examples=(qa('例 1　等价类划分与边界值',
   p('情境：某函数接收「年龄」参数（整数，允许 0–120），用于保险报价；小于 18 岁需监护人确认，18–65 为成人费率，66 及以上为老年费率。请设计等价类与测试用例。')
   + p('<b>分析：</b>先分有效类与无效类，再按业务规则把有效域细分，最后补边界。')
   + p('<b>有效等价类：</b>E1 = 0–17（未成年）；E2 = 18–65（成人）；E3 = 66–120（老年）。<b>无效等价类：</b>I1 = 负数；I2 = 121 及以上；I3 = 非整数（如 3.5）；I4 = 非数字（如空、字母）。')
   + p('<b>代表值：</b>E1 取 10；E2 取 30；E3 取 80；I1 取 −1；I2 取 121；I3 取 17.5；I4 取「abc」。共 7 个用例。')
   + p('<b>边界值（必须补）：</b>−1、0、17、18、65、66、120、121。边界最容易出错，因为实现常用 &lt; 与 ≤ 混淆。')
   + p('<b>期望输出要写清：</b>E1 应返回「需监护人确认」并给出未成年费率；E2 成人费率；E3 老年费率；无效类应抛出明确错误而非静默返回默认值。'))
  + qa('例 2　三类接口错误的识别',
   p('情境：某支付服务调用风控服务。① 风控接口签名为 check(userId, amount, currency)，调用方写成 check(amount, userId, currency)；② 调用方假设「风控返回 false 时一定抛异常」，实际是返回「code = RISK」；③ 风控侧每 200 ms 刷新一次黑名单，支付侧在请求开始时读取黑名单快照，但请求排队 1 秒后才执行。请分别归类。')
   + p('<b>解：</b>① 参数顺序传反 → <b>接口误用 interface misuse</b>（调用方使用接口时出错）。')
   + p('② 对返回契约的错误假设 → <b>接口误解 interface misunderstanding</b>（对被调用方行为嵌入了错误假设）。这类错误往往在集成测试才暴露，因为单元测试里 mock 的行为是调用方自己设想的。')
   + p('③ 快照过期 → <b>时序错误 timing error</b>（两侧速度/时序不同，读到过期信息）。')
   + p('<b>对策：</b>① 用具名参数或 DTO 替代长参数列表；② 契约测试（consumer-driven contract test）+ 明确文档；③ 在请求执行时而非入队时读取黑名单，或用版本号校验。'))
  + qa('例 3　TDD 循环与它的边界',
   p('情境：要实现「密码强度校验」：长度 ≥ 12，含大写、小写、数字、符号中至少三类，不得包含用户名。请写出 TDD 的前三轮循环，并说明哪一类测试不适合用 TDD 增量编写。')
   + p('<b>第一轮：</b>写测试「长度 11 的密码应被判为弱」→ 运行，失败（功能未实现）→ 实现最小逻辑（长度检查）→ 重跑，通过。')
   + p('<b>第二轮：</b>写测试「长度 12 但只含小写的密码应被判为弱」→ 失败 → 增加字符类别计数 → 通过。')
   + p('<b>第三轮：</b>写测试「包含用户名（不区分大小写）的强密码应被判为弱」→ 失败 → 增加用户名比对 → 通过。')
   + p('<b>收益对应：</b>每轮都留下一个回归测试（回归测试增量建立）；失败时只需看新写的代码（简化调试）；测试本身就是「密码规则」的可执行文档（系统文档）；每段实现代码都有测试（覆盖率）。')
   + p('<b>不适合增量编写：</b>复杂界面的「显示逻辑」与屏幕间工作流——因为难以在界面未成形时写出稳定的断言；这类测试更适合在界面稳定后用端到端测试或人工探索性测试补足。这正是课件列出的 TDD 问题之一。'))
  + qa('例 4　设计发布测试与用户测试',
   p('情境：某公司要把一套「药店库存与处方核对」系统卖给连锁药店（通用产品）。请设计发布测试与用户测试方案，并说明各自不能替代什么。')
   + p('<b>发布测试（独立团队，黑盒，从规格导出）：</b>① 功能覆盖：规格中每条需求至少一个用例，含处方核对的正例与反例（药物相互作用、剂量超限、重复用药）；② 非功能：在典型药店网络（4G 备份链路）下的响应时间；③ 性能与压力：模拟 200 家门店同时在早高峰下单，负载逐步增加至性能不可接受，记录失效行为；④ 可靠性：连续运行 7 天，检查内存泄漏与数据一致性。')
   + p('<b>用户测试：</b>alpha——选 3 家合作药店，在开发者场所模拟真实柜台流程，观察药师操作；beta——向 30 家门店发布候选版本，收集问题报告；验收——由连锁总部按合同条款逐项验收（可用性、数据迁移、报表口径）。')
   + p('<b>不能替代什么：</b>发布测试不能替代用户测试——药店的柜台空间、网络抖动、药师的工作习惯无法在测试环境复制（课件原句：these cannot be replicated in a testing environment）；用户测试也不能替代发布测试——用户不会系统覆盖规格，也测不出压力下的失效行为。'))),
 practice=(ol('「测试可以揭示错误的存在，但不能证明错误的不存在」——这句话对工程实践有什么含义？',
         '确认测试与缺陷测试对「成功」的定义有何不同？各举一个用例设计思路。',
         '软件检查的三个优势是什么？检查不能发现哪两类问题？',
         '自动化单元测试的三个组成部分是什么？请用「登录函数」举例说明。',
         '写出 TDD 的五步循环，并说明它与「先写代码后补测试」在调试成本上的差异。',
         '某系统要在 1000 台设备上运行，设备的屏幕尺寸、系统版本、网络状况各异。请说明你会如何组合开发测试/发布测试/用户测试，并指出压力测试在这个场景中的作用。')
   + det('参考答案与思路',
    p('<b>1.</b> 含义是：测试只能提供「未发现缺陷」的证据，不能提供「无缺陷」的证明。工程含义有三：①测试必须与静态检查、评审结合（V&amp;V 而非只有测试）；②测试要充分性论证（覆盖需求、覆盖等价类、覆盖风险），而不是「跑通了就行」；③发布决策是基于风险的判断，不是基于「测试全绿」的保证。')
    + p('<b>2.</b> 确认测试：成功 = 系统按预期工作（用例反映真实使用）；缺陷测试：成功 = 系统出错并暴露缺陷（用例刻意攻击边界、异常、并发）。前者像「验收演练」，后者像「找茬」。')
    + p('<b>3.</b> ①静态过程不受错误相互掩盖影响；②不完整版本也能低成本检查（不必搭测试夹具）；③能评估更广的质量属性（标准符合性、可移植性、可维护性）。不能发现：是否符合客户真实需求（只能查规格一致性）；非功能特性（性能、可用性）。')
    + p('<b>4.</b> setup（准备输入与期望输出，如用户名「alice」、密码「Secret123!」、期望返回 token）、call（调用 login(user, pwd)）、assertion（断言返回非空且含过期时间）。')
    + p('<b>5.</b> 识别增量 → 写自动化测试 → 运行（必然失败）→ 实现 → 重跑至通过。差异：先写代码后补测试时，测试失败可能来自多处改动，定位成本高；TDD 失败通常只来自刚写的几行代码。但 TDD 不保证完备性。')
    + p('<b>6.</b> 开发测试：单元 + 构件接口测试，配合设备矩阵的自动化脚本；发布测试：独立团队做黑盒功能与性能，覆盖主流机型与弱网；用户测试：beta 分发到真实门店，收集真实网络与操作问题。压力测试作用：验证「大量设备同时上报」时的失效行为（是降级、排队还是崩溃），从而决定是否需要限流与本地缓存。'))),
 exam=(cal('exam', '必考', '验证与确认的两句口号、两种测试对「成功」的定义、检查与测试的互补、三层开发测试的关注点、等价类划分（含边界）、三类接口错误、TDD 五步与四收益、发布测试与系统测试的两点差别、alpha/beta/acceptance 的区别。')
  + cal('warn', '易错 1', '把「缺陷测试成功」理解为「测试通过」。恰恰相反，缺陷测试的成功是让系统失败。')
  + cal('warn', '易错 2', '认为检查可以替代测试。检查不能验证非功能特性，也不能验证客户真实需求。')
  + cal('warn', '易错 3', '把发布测试交给开发团队做。课件明确应由未参与开发的独立团队负责，且目的从「找缺陷」转为「确认足够好」。')
  + cal('warn', '易错 4', '等价类只取有效类。无效类与边界值才是缺陷高发区。')
  + cal('tip', '进阶', '能把「测试不能证明无缺陷」与「V&amp;V 信心取决于用途/期望/市场」连起来，说明发布决策本质是风险决策，这是论述题的高分点。')),
 checklist=(h2('测试设计与评审的清单')
  + st('先明确测试目的：确认（证明满足需求）还是缺陷（暴露问题）',
       '按层分配：单元（功能）→ 构件（接口）→ 系统（交互与涌现行为）',
       '对每个输入做等价类划分：有效类 + 无效类 + 边界值',
       '对每个接口检查三类错误：误用、误解、时序',
       '为每个自动化测试写全 setup / call / assertion',
       '确认回归套件可在每次构建时全量运行',
       '安排独立团队做发布测试（黑盒、从规格导出）',
       '安排用户测试：alpha（开发者场所）、beta（真实环境）、验收（客户决策）',
       '用压力测试确认过载时的失效行为可控')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('16_Week 10/1_SE - Lecture 7 - 2026.pdf', 'p4–p9', '测试的定义与局限、两个目标、确认测试与缺陷测试、V 与 V 的区别、信心的三个来源'),
   ('16_Week 10/1_SE - Lecture 7 - 2026.pdf', 'p10–p13', '检查与测试的互补、检查的适用与优势'),
   ('16_Week 10/1_SE - Lecture 7 - 2026.pdf', 'p14–p23', '三个阶段、开发测试三层、单元测试与对象类测试、自动化测试三部分、划分与准则、等价类划分'),
   ('16_Week 10/1_SE - Lecture 7 - 2026.pdf', 'p24–p28', '构件测试、接口测试四类型、三类接口错误、系统测试与涌现行为'),
   ('16_Week 10/1_SE - Lecture 7 - 2026.pdf', 'p29–p39', 'TDD 定义、五步、四收益、发布测试、性能与压力测试、用户测试三类型、敏捷验收测试'),
   ('16_Week 10/1_SE - Lecture 7 - 2026.pdf', 'p40–p42', 'SQM 定义、持续改进、度量及其作用'),
   ('19_Week 13/3_Exercise Session 3 (1).pdf', 'p2–p5', '质量六维度、五类测试的目的、版本控制定义（集中式 SVN / 分布式 Git）'),
   ('（跳过）19_Week 13/2_Exercise Session 7.pptx', '全篇', '复习课行政页（点名、提交链接、同伴评审规则），未纳入讲义'),
   ('（补充）', '—', '边界值分析与压力测试的具体做法属应用性补充'))))
# ============================================================ 8
LEC.append(L(
 slug='l08-evolution-and-maintenance',
 tzh='第 8 讲 · 软件演化、维护与遗留系统',
 ten='Software Evolution and Maintenance',
 keywords=['software evolution', 'Lehman’s law', 'servicing', 'phase-out', 'legacy system', 'reverse engineering', 'reengineering', 'refactoring', 'bad smell', 'maintenance prediction', 'change prediction', 'emergency repair'],
 files=['17_Week 11/1_SE - Lecture 8 - 2026.pdf'],
 overview=(h2('本节定位')
  + p('前面七讲讲的是「把系统造出来」，这一讲讲「系统造出来之后的几十年」。课件给出一个残酷的事实：大型公司软件预算的大部分花在改变与演化既有软件上，而不是开发新软件。因此这一讲的核心不是技术，而是<b>经济学</b>：为什么旧系统改起来贵、什么时候该修、什么时候该换、怎么用重构延缓衰败。')
  + p('与前后衔接：第 3 讲的「演化」是四项活动之一，本讲展开；第 6 讲的架构决策决定后续演化的难易；第 10 讲的配置管理是演化的基础设施；第 12 讲的 Sasken 案例展示了「需求持续演化 + 离岸团队」如何放大维护难度。')
  + p('学完本节你应当能够：')
  + ck('陈述 Lehman 第一定律，并解释它对项目预算的含义',
     '说明遗留系统的六个组成要素，并解释为什么它不只是软件',
     '用「质量 × 业务价值」四象限为遗留系统选择处置策略',
     '区分三类维护，并说明为什么维护成本通常是开发的 2–100 倍',
     '区分再工程（reengineering）与重构（refactoring）的时机与目的',
     '识别五种典型代码坏味道，并给出对应重构手法')),
 detail=(h3('8.1 变化是常态：Lehman 第一定律')
  + p('课件开篇引用 Lehman 的软件演化第一定律：')
  + p('“Software must continually change, or it becomes progressively less useful.”（软件必须持续变化，否则会逐渐变得不那么有用。）')
  + p('这句话不是修辞，而是预算现实：组织在软件系统上有巨额投资，这些系统是关键的商业资产；要维持这些资产对业务的价值，就必须不断修改与更新。课件明确指出：<b>大型公司软件预算的大部分用于改变与演化既有软件，而不是开发新软件</b>。')
  + p('软件为什么会变？课件列了六个来源：软件被使用后出现新需求；业务环境变化；错误必须修复；新的计算机与设备被加入系统；技术变化（包括 AI 进入软件工程）；系统的性能或可靠性需要提升。对所有组织而言，关键问题是<b>如何实施并管理对既有系统的改变</b>。')
  + h3('8.2 生命周期的三个阶段')
  + p('课件用「开发与演化的螺旋模型」表示：系统投入使用后，每一圈都是「提出变更 → 分析影响 → 实现 → 发布」的循环。生命周期后段可分三段：')
  + tb(('阶段', '英文', '定义', '特征'),
       ('演化', 'evolution', '系统处于运行使用中，随着新需求被提出并实现而演化', '仍在增加新功能'),
       ('服务', 'servicing', '软件仍然有用，但所做的改变仅限于维持其可运行', '<b>不增加新功能</b>'),
       ('淘汰', 'phase-out', '软件可能仍在使用，但不再做任何改变', '只等替代或下线'))
  + p('这三个阶段的划分直接决定维护预算的分配：演化阶段要投入功能开发；服务阶段只需投入纠错与适配；淘汰阶段应尽量不再投入，把资源转向替代方案。')
  + h3('8.3 演化过程由什么决定')
  + p('课件指出，软件演化过程取决于三件事：被维护软件的类型；所使用的开发过程；参与人员的技能与经验。')
  + p('<b>变更提案是系统演化的驱动力</b>（proposals for change are the driver for system evolution）。变更提案应与受影响的构件建立链接，从而可以估算变更的成本与影响——这正是第 4 讲「可追溯性」在演化阶段的价值。变更识别与演化贯穿系统的整个生命周期。')
  + p('变更实现（change implementation）是开发过程的一次迭代：设计、实现并测试对系统的修订。它的第一阶段可能是<b>程序理解</b>（program understanding），尤其当原开发者不负责此次变更时。在程序理解阶段，你必须弄清程序如何组织、如何交付功能、拟议变更可能如何影响程序。')
  + cal('warn', '易错', '很多同学把「维护」理解为「只改 bug」。维护包含三类活动，其中功能增强往往占最大工作量；而「程序理解」是维护的第一步，也是最容易被低估的成本。')
  + h3('8.4 紧急变更与紧急修复过程')
  + p('紧急变更可能不得不在不走完整个软件工程过程的情况下实施，典型情形有三种：严重系统故障必须修复以恢复normal运行；系统环境的改变（如操作系统升级）产生了意外影响；业务变化要求极快响应（如竞争对手发布产品）。')
  + p('紧急修复过程（emergency repair process）的要点是：先止血（回滚、打补丁、关闭功能），再做根因分析，最后把修复纳入正常变更流程并补测试。课件以图呈现该过程（原 PDF 为图）。答题时的关键判断是：<b>紧急修复允许跳过评审与文档，但不允许跳过「事后补齐」</b>，否则技术债会以复利增长。')
  + h3('8.5 敏捷与演化：无缝，但有交接问题')
  + p('敏捷方法基于增量开发，因此从开发到演化的过渡是<b>无缝</b>的：演化只是基于频繁发布的开发过程的延续；自动化回归测试在变更时尤其有价值；变更可以表达为额外的用户故事。')
  + p('但「交接」会出问题，两个方向都要能说：')
  + ul('开发用敏捷、演化团队不熟悉敏捷且偏好计划驱动：演化团队期望详细文档来支撑维护，而敏捷过程不产出这类文档；',
       '开发用计划驱动、演化团队偏好敏捷：演化团队可能要从零建立自动化测试，而既有代码可能从未按敏捷期望被重构与简化。')
  + h3('8.6 遗留系统：不只是软件')
  + p('遗留系统（legacy systems）是依赖「已不再用于新系统开发的语言与技术」的较老系统；可能依赖较老的硬件（如大型机），并伴随遗留的流程与规程。')
  + p('课件强调：遗留系统不只是软件系统，而是更广的<b>社会技术系统</b>（socio-technical systems），包含硬件、软件、库与其他支撑软件，以及业务流程。')
  + p('六个组成要素：')
  + tb(('要素', '英文', '说明'),
       ('硬件', 'hardware', '常依赖过时硬件'),
       ('支撑软件', 'support software', '依赖可能已过时或不再受支持的支撑软件（操作系统、中间件、编译器）'),
       ('应用软件', 'application software', '通常由多个交付业务服务的程序组成'),
       ('应用数据', 'application data', '由应用系统处理，常在不同数据库中不一致或重复'),
       ('业务流程', 'business processes', '为达成业务目标而设，可能受遗留系统限制'),
       ('业务策略与规则', 'business policies and rules', '定义业务运作，可能与遗留系统的使用交织在一起'))
  + cal('exam', '必考', '「遗留系统是社会技术系统」是本节最容易被忽略的定义句。答题时若只写「老代码」，会丢掉「业务流程、业务规则、数据」这些关键维度，也难以解释为什么替换风险高。')
  + h3('8.7 为什么替换难、改也难')
  + p('替换遗留系统风险高、成本高，因此企业继续使用它们。风险高的四个原因：')
  + ol('缺乏完整的系统规格；',
       '系统与业务流程紧密集成；',
       '嵌入在遗留系统中的业务规则没有被文档化；',
       '新软件开发可能延期或超预算。')
  + p('改遗留系统昂贵的原因（六条）：')
  + ul('没有一致的编程风格；',
       '使用过时的编程语言，掌握该语言的人很少；',
       '系统文档不足；',
       '系统结构退化；',
       '程序优化（如手工汇编级优化）使其难以理解；',
       '数据错误、重复与不一致。')
  + h3('8.8 遗留系统的四种处置策略')
  + p('依赖遗留系统的组织必须选择演化策略：完全废弃系统并修改业务流程使其不再需要；继续维护；通过再工程改造以提升可维护性；用新系统替换。所选策略应取决于<b>系统质量</b>与<b>业务价值</b>。')
  + tb(('质量 / 价值', '低业务价值', '高业务价值'),
       ('低质量', '<b>废弃</b>（scrap）', '<b>再工程或替换</b>（若市场上有合适系统）'),
       ('高质量', '<b>用 COTS 替换、废弃或维护</b>', '<b>正常维护继续运行</b>'))
  + p('业务价值评估要听取多方视角：系统最终用户、业务客户、直线经理、IT 经理、高层管理者；访谈不同干系人并汇总结果。评估时看四点：系统的使用情况（偶尔用或少数人用 → 价值低）；所支撑的业务流程（迫使使用低效流程 → 价值低）；系统可靠性（不可靠且直接影响业务客户 → 价值低）；系统输出（业务依赖其输出 → 价值高）。')
  + p('系统质量评估看三方面：业务流程评估（业务流程对当前业务目标的支持程度）；环境评估（系统环境的有效性与其维护成本）；应用评估（应用软件系统本身的质量）。')
  + p('定量测量可用于评估应用质量，课件给三个指标：变更请求数量（累计值越高，质量越低）；系统使用的不同用户界面数量（界面越多，越可能存在不一致与冗余）；系统处理的数据量（文件数、数据库规模越大，数据中的不一致与错误越多；清理旧数据非常昂贵耗时）。')
  + h3('8.9 维护：定义与三类')
  + p('维护是「在程序投入使用后修改程序」。该词主要用于定制软件；通用软件产品则说「演化出新版本」。维护通常<b>不涉及对系统架构的重大改变</b>；变更通过修改既有构件与增加新构件实现。')
  + tb(('类型', '英文', '做什么', '例子'),
       ('纠错性维护', 'fault repairs', '修改系统以修复 bug/漏洞、纠正未满足需求的缺陷', '修复结算金额舍入错误'),
       ('环境适配', 'environmental adaptation', '让软件在不同于初始实现的环境中运行', '迁移到新操作系统、新硬件'),
       ('功能增加与修改', 'functionality addition and modification', '修改系统以满足新需求', '增加导出 Excel 功能'))
  + p('课件用饼图给出维护工作量分布（原 PDF 为图，考试不要求具体百分比）；理解要点是：三类维护中<b>功能增加与修改通常占用最多工作量</b>，纠错占比相对较小。这解释了为什么「维护 = 改 bug」是错误直觉。')
  + h3('8.10 维护成本与预测')
  + p('维护成本的五个判断：')
  + ul('通常大于开发成本（视应用不同，为 <b>2 到 100 倍</b>）；',
       '受技术与非技术因素共同影响；',
       '随软件被维护而<b>上升</b>——维护会侵蚀软件结构，使后续维护更难；',
       '老化软件的支持成本高（旧语言、旧编译器）；',
       '在维护阶段给系统增加新功能，通常比在开发阶段增加同样功能更贵。')
  + p('维护预测（maintenance prediction）关注「系统的哪些部分可能出问题、维护成本高」。课件的因果链值得背：变更的接受程度取决于受影响构件的<b>可维护性</b>；实施变更会<b>降低</b>系统可维护性；维护成本取决于变更数量，而变更成本取决于可维护性。这是一个正反馈回路——越改越难改。')
  + p('变更预测（change prediction）需要理解系统与其环境的关系：<b>紧耦合</b>系统在环境变化时就需要变更。影响因素有三：系统接口的数量与复杂度；本质上易变的系统需求数量；系统被使用的业务流程。')
  + h3('8.11 再工程与重构')
  + p('<b>再工程</b>（reengineering）是「在不改变功能的前提下，重构或重写遗留系统的部分或全部」。它适用于「大型系统中部分（而非全部）子系统需要频繁维护」的情形。再工程投入额外工作量使系统更易维护：系统可能被重构与重新文档化。')
  + p('再工程的两个优势：<b>降低风险</b>（新软件开发有高风险——开发问题、人员问题、规格问题）；<b>降低成本</b>（再工程成本常显著低于开发新软件）。')
  + p('再工程的典型手段（课件以图呈现，此处按标准含义展开）：源代码翻译（转成新语言）、逆向工程（从代码恢复设计与规格）、程序结构改善（去除 goto、结构化控制流）、程序模块化（把紧耦合代码拆成模块）、数据再工程（清理与规范化数据）。')
  + p('<b>重构</b>（refactoring）是「改进程序以延缓因变更导致的结构退化」，可理解为<b>预防性维护</b>（preventative maintenance）：修改程序以改善结构、降低复杂度、使其更易理解；重构时<b>不应增加功能</b>，而应专注于程序改进。')
  + p('两者的区别（高频考点）：')
  + tb(('维度', '再工程 reengineering', '重构 refactoring'),
       ('时机', '系统已被维护一段时间、维护成本上升之后', '开发与演化的全过程，持续进行'),
       ('范围', '常涉及整个系统或子系统，用自动化工具处理', '通常是局部代码结构'),
       ('手段', '源代码翻译、逆向工程、模块化、数据再工程', '提取函数、内联、重命名、搬移、以多态替换条件'),
       ('是否改变功能', '不改变功能', '不增加功能，只改进结构'),
       ('目的', '把遗留系统变成更易维护的新系统', '避免结构与代码退化推高维护成本'))
  + h3('8.12 代码坏味道')
  + p('课件列出五种「坏味道」（bad smells）与对应处理：')
  + tb(('坏味道', '英文', '问题', '处理'),
       ('重复代码', 'duplicate code', '同一逻辑散落多处，改一处漏一处', '用单一函数或方法消除重复'),
       ('长方法', 'long methods', '方法过长，难以理解与测试', '拆成更短的方法'),
       ('switch 语句', 'switch statements', '重复的 switch 难以扩展', '在面向对象语言中用多态替换'),
       ('数据泥团', 'data clumping', '同一组数据反复一起出现', '封装成对象'),
       ('投机泛化', 'speculative generality', '为「将来可能用到」而加的泛化', '删除不必要的泛化'))
  + p('这五种味道对应的重构手法，是代码评审（第 10 讲）最常用的检查项。')
  + h3('8.13 AI 与软件演化')
  + p('课件的第四节讨论 AI 对演化的影响，给了三个判断：')
  + ul('AI 的整合正在驱动大规模企业转型，各行业公司都在改变其构建、组织与现代化软件系统的方式；',
       'AI 把日常维护、重构与文档的负担从人转移到机器；',
       '组织意识到遗留架构与碎片化数据无法支撑现代 AI 工作负载，因此系统正在向「AI-ready」演化——不是把 AI 当作一个功能，而是改造架构与数据。')
  + p('课件用 Lehman 的三条定律对照「传统现实」与「AI 转型」：')
  + tb(('Lehman 定律', '传统现实', 'AI 转型'),
       ('持续变化定律 Law of Continuing Change', '保持软件更新需要大量人工工程努力与缓慢的发布周期', 'AI 降低持续更新的摩擦，使代码库能更顺畅地吸收变化'),
       ('复杂性递增定律 Law of Increasing Complexity', '复杂性不可避免地增长；重构常被忽视，因为它不交付新功能', 'AI 扫描代码库、识别反模式、廉价地完成复杂结构清理——自动化的重构'),
       ('熟悉度守恒 Conservation of Familiarity', '增长受人的认知极限约束——团队能理解多少代码', 'AI 文档与语义检索扩展团队对庞大遗留仓库的理解（认知放大）'))
  + p('课件最后给出一段很重要的价值判断：转型不可避免但渐进；一个常见误解是「传统基础不再重要」，现实恰恰相反——新工程师必须严格掌握传统最佳实践（扎实的架构、严谨的设计模式、调试直觉、系统约束）；AI 是强大的放大器，但无法替代人的判断：决定哪些代码应该存在、系统如何安全扩展、架构边界应划在哪里。掌握基础并拥抱 AI 速度的人，会成为「桥梁工程师」（bridge engineer）。')),
 kws=K(('software evolution', '软件演化', 'The stage where the system is in operational use and evolves as new requirements are implemented.'),
       ('Lehman’s first law', 'Lehman 第一定律', 'Software must continually change, or it becomes progressively less useful.'),
       ('servicing', '服务阶段', 'The software remains useful but only changes required to keep it operational are made.'),
       ('phase-out', '淘汰阶段', 'The software may still be used but no further changes are made.'),
       ('legacy system', '遗留系统', 'Older socio-technical system relying on obsolete languages, hardware and processes.'),
       ('socio-technical system', '社会技术系统', 'Hardware, software, libraries, business processes and rules taken together.'),
       ('corrective maintenance', '纠错性维护', 'Repairing faults not discovered during development.'),
       ('adaptive maintenance', '适应性维护', 'Adapting software to a new environment such as a new OS or platform.'),
       ('perfective maintenance', '完善性维护', 'Adding or modifying functionality to satisfy new requirements.'),
       ('maintenance prediction', '维护预测', 'Assessing which parts may cause problems and have high maintenance costs.'),
       ('change prediction', '变更预测', 'Predicting how many changes are needed from coupling to the environment.'),
       ('reengineering', '再工程', 'Restructuring or rewriting part or all of a legacy system without changing functionality.'),
       ('refactoring', '重构', 'Program improvements that slow degradation; preventative maintenance.'),
       ('bad smell', '代码坏味道', 'Symptoms such as duplicate code, long methods, switch statements.'),
       ('emergency repair', '紧急修复', 'Fixing a serious fault outside the normal process, followed by root cause analysis.')),
 examples=(qa('例 1　四象限决策',
   p('情境：某集团有四套系统：A 是 1998 年的工资系统，仍在用但每年只改两次，代码质量尚可；B 是 2005 年的订单系统，业务核心、每天处理 10 万单，但代码混乱、无人懂原语言；C 是 2010 年的内部会议室预订系统，使用人数少、流程低效；D 是 2003 年的报表系统，质量尚可但业务已迁到新数据仓库。请分别给出处置策略。')
   + p('<b>分析：</b>先做两维评估——业务价值（是否被业务依赖、使用频率、是否影响客户）与系统质量（结构、文档、语言、数据一致性），再落四象限。')
   + p('<b>A：高质量 + 高价值 → 正常维护继续运行。</b>改动频率低、质量尚可，替换的收益不足以抵消风险。')
   + p('<b>B：低质量 + 高价值 → 再工程或替换。</b>业务核心不能停，因此优先评估「再工程」（保留业务规则、改善结构与文档）与「替换」的成本；若市场有合适系统且迁移风险可控，则替换。切忌「推倒重写」而不做业务规则挖掘。')
   + p('<b>C：低质量 + 低价值 → 废弃。</b>先改业务流程使其不再需要，再下线系统；继续维护是纯浪费。')
   + p('<b>D：高质量 + 低价值 → 用 COTS 替换、废弃或维护。</b>业务已迁走，优先废弃；若仍有少量报表需求，用现成 BI 工具替代，避免为少量需求维护一套系统。')
   + p('<b>注意：</b>四象限是决策起点而非终点；还要看「替换的时间窗口」与「数据迁移成本」，这两项常是真正决定成败的因素。'))
  + qa('例 2　判断维护类型与成本动因',
   p('情境：某系统上线后发生四件事：① 客户报表金额少了一分钱，排查发现是浮点舍入；② 公司把服务器从 Windows 迁到 Linux，程序无法启动；③ 财务要求新增「按项目维度分摊」功能；④ 系统换了新的短信服务商，接口协议变化。请分类，并说明哪一类通常成本最高、为什么。')
   + p('<b>解：</b>① <b>纠错性维护</b>（fault repair）：修复开发阶段未发现的缺陷。② <b>环境适配</b>（environmental adaptation）：迁移到新平台。③ <b>功能增加与修改</b>（functionality addition）：满足新需求。④ 也是<b>环境适配</b>：外部依赖的接口协议变化属于运行环境变化。')
   + p('<b>成本：</b>③ 通常成本最高，因为它要求理解既有设计、改动数据结构与界面、更新测试与文档，且可能触碰架构约束；课件指出在维护阶段增加功能比在开发阶段增加同样功能更贵。')
   + p('<b>为什么维护越来越贵：</b>每次变更都侵蚀结构（维护预测的因果链），可维护性下降使下一次变更更贵；此外老语言人才稀缺、文档不足、数据不一致都会叠加成本。'))
  + qa('例 3　再工程还是重构',
   p('情境：某银行的核心账务模块有 200 万行 COBOL，每年有 300 次变更请求，维护成本已占 IT 预算 40%；同期一个小的对账工具只有 5000 行 Java，结构尚可但方法过长。请分别为两者选择手段。')
   + p('<b>分析：</b>判断依据是「范围 + 时机 + 是否改变功能」。核心账务模块已被维护多年、成本高、范围大、语言过时 → <b>再工程</b>：先逆向工程恢复业务规则与设计，再做源代码翻译与模块化，最后补文档与自动化回归测试；不改变功能，因此可用「新旧并行对账」验证等价性。')
   + p('<b>对账工具：</b>范围小、结构尚可、问题局部 → <b>重构</b>：拆分长方法、消除重复代码、以多态替换 switch；不增加功能，持续进行。')
   + p('<b>为什么不能反过来：</b>对 200 万行 COBOL 做手工重构不现实（缺人、缺测试、风险高），必须借助工具与分阶段迁移；对 5000 行 Java 做「再工程」是过度投入——它不需要逆向工程与语言翻译。'))
  + qa('例 4　Lehman 定律与 AI',
   p('情境：某公司引入 AI 编码助手后，变更频率提高了 3 倍，但线上缺陷率也上升。请用 Lehman 定律与课件观点解释这一现象，并给出治理建议。')
   + p('<b>分析：</b>用三条定律逐一对照。')
   + p('<b>持续变化：</b>AI 降低了变更摩擦，使代码库能吸收更多变化——这是收益，但变化越快，结构退化越快。')
   + p('<b>复杂性递增：</b>若 AI 生成代码未被重构与审查，复杂性会加速累积；课件说 AI 能「廉价地做结构清理」，但前提是团队真的把重构纳入流程，而不是只追功能。')
   + p('<b>熟悉度守恒：</b>团队对代码的理解速度没有同比提升；AI 生成的代码若无人真正理解，认知负荷反而上升，缺陷率随之上升。')
   + p('<b>治理建议：</b>① 把「AI 生成代码」纳入与人工代码相同的评审与测试门槛（check before check-in、never break the build）；② 用自动化重构与静态分析定期清理坏味道；③ 限制单人单次变更规模，保持可审查性；④ 建立「谁能解释这段代码」的责任制，避免熟悉度赤字。')
   + p('<b>结论：</b>AI 是放大器而非替代品；课件原文强调 human judgment 在「哪些代码该存在、系统如何安全扩展、架构边界在哪」上不可替代。'))),
 practice=(ol('陈述 Lehman 第一定律，并解释它为什么意味着「维护预算必然占大头」。',
         '演化、服务、淘汰三阶段的区别是什么？各阶段的预算应如何分配？',
         '遗留系统的六个组成要素是什么？为什么说它是社会技术系统？',
         '替换遗留系统的四个风险与修改遗留系统的六个原因分别是什么？',
         '再工程与重构的区别（至少三点）。',
         '写出五种代码坏味道及其处理方式。')
   + det('参考答案与思路',
    p('<b>1.</b> 软件必须持续变化，否则逐渐失去用处。因为业务环境、技术平台、用户需求持续变化，系统不更新就会与业务脱节；而既有系统是巨额投资，维持其价值只能靠持续修改，因此预算大头在演化而非新建。')
    + p('<b>2.</b> 演化：增加新功能，投入功能开发预算；服务：只做维持运行的必要修改，投入纠错与适配的最小预算；淘汰：不再修改，预算转向替代方案与数据迁移。')
    + p('<b>3.</b> 硬件、支撑软件、应用软件、应用数据、业务流程、业务策略与规则。因为它的价值与风险都嵌在业务流程与规则中，而不只在代码里；替换系统等于替换流程，因此风险远高于「换一套软件」。')
    + p('<b>4.</b> 替换风险：缺完整规格、与业务流程紧耦合、业务规则未文档化、新开发可能延期超预算。修改困难：编程风格不一致、语言过时且人才稀缺、文档不足、结构退化、程序优化难懂、数据错误重复不一致。')
    + p('<b>5.</b> 时机（再工程在维护成本上升后，重构持续进行）；范围（再工程常涉及整系统/子系统并用工具，重构多局部）；手段（再工程含逆向工程、语言翻译、数据再工程，重构是提取/内联/重命名/多态替换）；二者都不改变功能，但再工程是「一次性改善可维护性」，重构是「预防性日常维护」。')
    + p('<b>6.</b> 重复代码 → 提取单一函数；长方法 → 拆短；switch → 多态；数据泥团 → 封装对象；投机泛化 → 删除。'))),
 exam=(cal('exam', '必考', 'Lehman 第一定律、演化/服务/淘汰、遗留系统六要素、四象限策略、三类维护、维护成本 2–100 倍、再工程 vs 重构、五种坏味道、紧急修复的三类触发情形。')
  + cal('warn', '易错 1', '把「维护」等同于「修 bug」。维护包含纠错、适配、功能增强三类，功能增强往往工作量最大。')
  + cal('warn', '易错 2', '把再工程与重构当成同义词。再工程是「不改功能地重构或重写部分/全部遗留系统」，重构是「持续的小步结构改进」。')
  + cal('warn', '易错 3', '认为「质量高就该保留」。四象限里「高质量 + 低业务价值」也可能应废弃或用 COTS 替换。')
  + cal('warn', '易错 4', '认为 AI 让基础不重要。课件明确相反：架构、设计模式、调试直觉、系统约束仍是判断力的来源。')
  + cal('tip', '进阶', '能画出「变更 → 结构退化 → 可维护性下降 → 下次变更更贵」的正反馈回路，并用它解释为什么「维护成本随维护而上升」，是论述题的高分点。')),
 checklist=(h2('遗留系统处置的清单')
  + st('确认系统处于演化、服务还是淘汰阶段',
       '评估业务价值：使用频率、支撑流程、可靠性、输出依赖',
       '评估系统质量：流程、环境、应用三方面 + 三个定量指标',
       '落四象限，得到初步策略（废弃/维护/再工程/替换）',
       '若选再工程：先逆向工程恢复业务规则，再做结构改善与数据清理',
       '若选替换：评估规格缺失、流程耦合、规则未文档化、新开发延期四类风险',
       '为紧急变更建立「止血 → 根因 → 补齐测试与文档」的闭环',
       '把重构纳入日常：定期扫描五种坏味道并修复')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('17_Week 11/1_SE - Lecture 8 - 2026.pdf', 'p4–p8', 'Lehman 第一定律、软件变化的六个来源、演化的重要性、开发与演化的螺旋、演化/服务/淘汰'),
   ('17_Week 11/1_SE - Lecture 8 - 2026.pdf', 'p9–p16', '演化过程的决定因素、变更提案与可追溯、变更实现与程序理解、紧急变更与紧急修复、敏捷与演化、交接问题'),
   ('17_Week 11/1_SE - Lecture 8 - 2026.pdf', 'p17–p27', '遗留系统定义与社会技术属性、六要素、替换风险、修改困难、四种策略与四象限、业务价值与质量评估、三个定量指标'),
   ('17_Week 11/1_SE - Lecture 8 - 2026.pdf', 'p28–p35', '维护定义、三类维护、工作量分布、维护成本、维护预测与变更预测、再工程定义与优势'),
   ('17_Week 11/1_SE - Lecture 8 - 2026.pdf', 'p36–p39', '再工程手段、重构定义、再工程与重构的区别、五种坏味道'),
   ('17_Week 11/1_SE - Lecture 8 - 2026.pdf', 'p40–p42', 'AI 与演化、AI-ready、Lehman 三定律对照表、基础功与桥梁工程师'),
   ('（跳过）', '—', '本周无纯图片或行政页需跳过'),
   ('（补充）', '—', '再工程的五种具体手段按标准含义展开；课件以图呈现'))))
# ============================================================ 9
LEC.append(L(
 slug='l09-project-management-and-planning',
 tzh='第 9 讲 · 软件项目管理与计划',
 ten='Software Project Management and Planning',
 keywords=['project management', 'success criteria', 'risk management', 'project risk', 'product risk', 'business risk', 'risk planning', 'contingency plan', 'people management', 'Maslow', 'project planning', 'plan-driven development', 'agile planning', 'release planning', 'effort estimation', 'planning poker'],
 files=['18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'What we do and dont know about software development effort estimation. .pdf'],
 overview=(h2('本节定位')
  + p('前八讲谈「怎么把软件做好」，这一讲谈「怎么把项目管住」：在预算与工期的约束下按时交付、控制风险、带好团队、做出可执行的计划。课件把管理活动归为五类（风险管理、人员管理、项目计划、报告、提案写作），重点展开前三类，并对比计划驱动与敏捷两种计划方式。最后用 Jørgensen 的实证综述补充「估算为什么总是不准」。')
  + p('与前后的衔接：第 2 讲的「敏捷项目管理」在此落地为 release/iteration planning；第 3 讲的「过程度量」是本讲风险监控与进度衡量的基础；第 13 讲的项目计划书（任务、进度、检查点、成本、风险、质量、变更、组织）直接套用本讲的结构。')
  + p('学完本节你应当能够：')
  + ck('说出项目管理的定义与四条成功标准',
     '按「项目风险 / 产品风险 / 业务风险」对风险分类，并完成识别、分析、计划、监控四步',
     '为一个风险写出避免、最小化、应急三套策略',
     '区分提案阶段、启动阶段、开发过程中的计划，各自的精度与用途',
     '对比计划驱动与敏捷计划的差异，写出 release planning 与 iteration planning 的分工',
     '说明估算的七条已知结论与三条未知，并解释「赢家的诅咒」')),
 detail=(h3('9.1 项目管理管什么')
  + p('课件定义：软件项目管理关注「确保软件按时、按进度、并符合开发与采购组织的需求被交付」所涉及的活动。英文原句是：“Concerned with activities involved in ensuring that software is delivered on time and on schedule and in accordance with the requirements of the organisations developing and procuring the software.”为什么需要它？因为软件开发总是受组织设定的<b>预算与进度约束</b>。')
  + p('四条成功标准（可用于验收一个项目）：')
  + ol('在约定时间把软件交付给客户；',
       '把总体成本控制在预算内；',
       '交付满足客户期望的软件；',
       '维持一个连贯、运作良好的开发团队。')
  + p('注意第四条：团队状态也是成功标准。一个「按时交付但团队散了」的项目，在课件标准下并不完全成功。')
  + h3('9.2 软件项目管理的三个特殊性')
  + tb(('特殊性', '英文', '含义', '管理含义'),
       ('产品无形', 'the product is intangible', '软件看不见摸不着，管理者无法通过「看工地」判断进展', '必须用可交付物、度量与演示代替「目视检查」'),
       ('多为一次性项目', 'many projects are one-off', '大型项目与以往项目总有不同，经验丰富者也难预判问题', '不能简单套用历史模板，要重新做风险识别'),
       ('过程多变且组织特定', 'processes are variable and organization specific', '仍无法可靠预测某个过程何时会导致问题', '需要用度量与复盘逐步建立本地基线'))
  + p('影响项目管理的因素（六个）：公司规模、软件客户、软件规模、软件类型、组织文化、软件开发过程。课件结论：这些因素意味着不同组织的项目经理可能以很不同的方式工作。')
  + h3('9.3 五类管理活动')
  + tb(('活动', '英文', '内容'),
       ('风险管理', 'risk management', '评估可能影响项目的风险、监控风险，并在问题出现时采取行动'),
       ('人员管理', 'people management', '选人、建立能带来有效团队绩效的工作方式'),
       ('项目计划', 'project planning', '计划、估算、排期，并把人员分配到任务'),
       ('报告', 'reporting', '向客户与公司管理层报告进展'),
       ('提案写作', 'proposal writing', '项目第一阶段可能是写提案以赢得合同，描述项目目标与实施方式'))
  + h3('9.4 风险管理：为什么软件特别需要')
  + p('风险管理是「识别风险并制定计划以最小化其对项目影响」的过程：“Risk management is concerned with identifying risks and drawing up plans to minimise their effect on a project.”课件指出软件风险管理重要，是因为软件开发内在的<b>不确定性</b>，来源包括：需求定义松散；客户需求变化导致需求变更；开发所需时间与资源难以估算；个体技能差异。')
  + p('管理者的任务是：预期风险、理解风险对项目/产品/业务的影响、采取措施避免风险。')
  + p('风险分类有两个维度：<b>风险类型</b>（技术、组织等）与<b>受影响对象</b>：')
  + tb(('类别', '英文', '影响', '例子'),
       ('项目风险', 'project risks', '影响进度或资源', '关键人员离职导致进度延误'),
       ('产品风险', 'product risks', '影响软件质量或性能', '采用未验证的框架导致性能不达标'),
       ('业务风险', 'business risks', '影响开发或采购软件的组织', '客户预算被削减 20%'))
  + h3('9.5 风险管理四步')
  + ol('<b>风险识别</b>（risk identification）：识别项目、产品与业务风险；可由团队活动完成，也可基于项目经理个人经验；可用常见风险清单（checklist）识别。',
       '<b>风险分析</b>（risk analysis）：评估每个风险的概率与严重性。概率可分为 very low / low / moderate / high / very high；后果可分为 catastrophic / serious / tolerable / insignificant。',
       '<b>风险计划</b>（risk planning）：为每个风险制定管理策略——避免（avoidance，降低发生概率）、最小化（minimization，降低影响）、应急计划（contingency plan，风险发生时的应对方案）。',
       '<b>风险监控</b>（risk monitoring）：定期评估每个已识别风险是变得更可能还是更不可能，并评估其影响是否变化；每个关键风险应在管理进展会议上讨论。')
  + p('风险识别清单的五类：技术风险、组织风险、人员风险、需求风险、估算风险。这五类可以直接作为项目计划书风险表的分类框架（第 13 讲）。')
  + p('课件的「what-if」问题很适合训练风险思维：')
  + ul('如果几名工程师同时病倒怎么办？',
       '如果经济下行导致项目预算削减 20% 怎么办？',
       '如果某开源软件性能不达标，而唯一熟悉它的专家离职了怎么办？',
       '如果供应并维护软件构件的公司倒闭了怎么办？',
       '如果客户未能按预期交付修订后的需求怎么办？')
  + cal('tip', '技巧', '写风险表时，一个风险只写一条「原因—事件—影响」链，例如「唯一熟悉 Kafka 的工程师离职（原因）→ 消息链路无人能改（事件）→ 支付对账延迟上线（影响）」。这样概率与严重性才有可评估的对象。')
  + h3('9.6 人员管理')
  + p('课件开篇的判断很直接：人是组织最重要的资产；管理任务本质上是「面向人的」；缺乏对人的理解，管理不会成功；<b>人员管理不善是项目失败的重要贡献因素</b>。')
  + p('四条人员管理原则：')
  + tb(('原则', '英文', '含义'),
       ('一致性', 'consistency', '团队成员应被以可比的方式对待，无偏袒与歧视'),
       ('尊重', 'respect', '成员技能不同，这些差异应被尊重'),
       ('包容', 'inclusion', '让所有成员参与，确保其观点被考虑'),
       ('诚实', 'honesty', '对项目哪些顺利、哪些不顺，始终诚实'))
  + p('<b>激励</b>是管理者的重要职责：激励意味着组织工作与工作环境，使人愿意有效工作。若人没有被激励，就不会对工作感兴趣，会做得慢、更易出错、也不会为团队与组织的更大目标做贡献。')
  + p('课件用 Maslow 需求层次解释软件团队的激励落点：在软件团队中，基本生理与安全需求通常不是问题，因此重点在：')
  + tb(('层次', '在软件团队中的落点', '管理动作'),
       ('生理', '公平薪酬、舒适工作条件、充分休息；提供必要的工具、设备与技术', '保证资源到位'),
       ('安全', '清晰期望、一致反馈、工作安全感；明确的计划、时间线与风险管理', '减少不确定性带来的焦虑'),
       ('归属', '正向团队文化、协作、开放沟通、团建；认可贡献', '让人感到被重视与连结'),
       ('尊重', '成长机会、认可与奖励成就、建设性反馈；授权任务与责任', '提升自我评价'),
       ('自我实现', '挑战性任务、鼓励创新、职业发展机会；持续学习的文化', '让人发挥潜能'))
  + p('课件同时提醒：需求层次「几乎肯定是过度简化」。因此还要考虑<b>人格类型</b>：')
  + ul('<b>任务导向</b>（task-oriented）：被工作本身激励——软件工程师中常见；',
       '<b>互动导向</b>（interaction-oriented）：被同事的存在与行动激励；',
       '<b>自我导向</b>（self-oriented）：主要被个人成功与认可激励。')
  + h3('9.7 项目计划：把工作拆开并预判问题')
  + p('项目计划是「把工作拆成部分、分配给团队成员、预判可能出现的问题并准备初步解决方案」。项目开始时制定的计划用于向团队与客户沟通工作将如何完成，并帮助评估进展。')
  + p('三个计划时机，精度与用途不同：')
  + tb(('阶段', '已知信息', '目的'),
       ('提案阶段 proposal stage', '只有概要需求', '为定价提供信息；项目定价需估算开发成本，考虑人员、硬件、软件成本'),
       ('启动阶段 startup phase', '更了解需求，但无设计与实现信息', '做出足以决定预算与人员的计划；作为资源分配的基础；定义项目监控机制；<b>敏捷开发也需要启动计划</b>以便分配资源'),
       ('开发过程中 periodically', '已获得经验与进展信息', '按经验修订进度、成本估算与风险'))
  + h3('9.8 计划驱动开发：优点与代价')
  + p('计划驱动（plan-based）开发是「开发过程被详细计划」的方式，基于工程项目管理技术，是管理大型软件项目的传统方式。项目计划记录：要做的工作、谁来做、开发进度、工作产物。管理者用计划支持决策并衡量进展。')
  + p('支持理由：早期计划使组织性问题（人员可用性、其他项目冲突）被细致考虑；潜在问题与依赖在项目开始前就被发现，而不是开工后才发现。')
  + p('反对理由：许多早期决策必须被修订，因为软件开发与使用环境会变化。')
  + p('项目计划的七个部分（考试常考「计划应包含什么」）：')
  + ol('引言（introduction）；',
       '项目组织（project organization）；',
       '风险分析（risk analysis）；',
       '硬件与软件资源需求（hardware and software resource requirements）；',
       '工作分解（work breakdown）；',
       '项目进度（project schedule）；',
       '监控与报告机制（monitoring and reporting mechanisms）。')
  + p('计划过程是<b>迭代</b>的：启动阶段创建初始计划，随项目推进不断修订；业务目标变化也会导致所有项目重新计划。')
  + p('计划假设要「现实而非乐观」：项目中总会出现各种问题导致延期，因此初始假设与排期必须把意外问题计入；计划中应包含<b>应急余量</b>（contingency），使事情出错时交付进度不被严重打乱。')
  + p('风险缓解（risk mitigation）：若开发工作出现可能导致重大延误的严重问题，需要启动风险缓解行动以降低项目失败风险；同时必须<b>重新计划</b>，这可能涉及与客户重新协商约束与交付物，并建立新的、与客户达成一致的完成时间表。')
  + h3('9.9 敏捷计划')
  + p('敏捷开发是迭代方法，软件以增量交付。与计划驱动不同，<b>增量的功能不预先计划</b>，而是在开发中决定：一个增量包含什么，取决于进展与客户优先级。客户优先级与需求会变，因此灵活的、能容纳变化的计划才合理。')
  + p('两个层次的计划：')
  + tb(('层次', '英文', '时间跨度', '决定什么'),
       ('发布计划', 'release planning', '向前看数月', '一次系统发布应包含哪些特性'),
       ('迭代计划', 'iteration planning', '短期，通常 2–4 周', '下一次增量做什么'))
  + p('软件交付规则（必须记住）：每个项目迭代结束时总要交付一个软件增量；<b>若增量包含的功能无法在允许时间内完成，则缩减工作范围；交付日期绝不延长</b>。这条规则是敏捷承诺的核心机制。')
  + p('敏捷计划的困难：依赖客户参与与可用性，而客户代表常要优先处理其他工作，无法参加计划活动（planning game）；部分客户熟悉传统项目计划，难以投入敏捷计划过程。')
  + p('适用性：敏捷计划适合小型、稳定的开发团队，大家可以坐在一起讨论要实现的故事；团队很大、地理分布、成员频繁变动时，让所有人参与协作计划实际上不可能。')
  + h3('9.10 AI 与软件项目管理')
  + p('课件的第四节给出四个变化方向：')
  + tb(('方向', '具体表现'),
       ('增强的计划与估算', '智能排期（分析历史数据、技能与资源可用性生成更现实的进度）；预测性分析（在延期、超支、资源短缺发生前预警）'),
       ('任务自动化与效率', '自动化的进度跟踪与状态更新、报告与文档生成、按技能与容量自动分配任务、用 NLP 做会议摘要与转写；AI 辅助编码（如 Copilot）、标记缺陷、自动化部分测试'),
       ('改进的风险与资源管理', '主动风险缓解（扫描项目文档、历史数据甚至外部市场状况，发现人可能忽略的风险；模拟 what-if 场景测试应急计划）；优化资源分配（实时可见的资源利用，匹配人与任务，平衡负载，防止倦怠或闲置）'),
       ('项目经理角色转变', '从管理者到战略者（重复任务自动化后，专注于干系人管理、教练团队、解决复杂冲突、推动创新）；数据驱动决策（用 AI 洞察与实时数据分析替代直觉与手工计算）'))
  + h3('9.11 估算：我们知道的与不知道的')
  + p('Jørgensen 的实证综述是本周阅读材料，它回答一个项目管理中最痛的问题：为什么估算总是不准？')
  + p('开篇的事实：大量证据表明软件项目存在成本与工作量超支倾向，平均约 <b>30%</b>；把 1980 年代的估算精度与近期调查相比，精度<b>没有明显改善</b>；估算方法也没有大变——尽管有大量形式化估算模型研究，<b>主导方法仍是专家估算</b>（expert estimation）。')
  + p('七条有充分证据支持的结论：')
  + ol('<b>没有「最好的」估算模型或方法</b>：不同研究里赢家各不相同；核心关系（如工作量与规模的关系）随情境而变，影响最大的变量也在变。因此公司应建立<b>自己的</b>估算模型，而不是指望通用模型在本地准确。',
       '<b>客户对低价的偏好是超支的主因</b>：在价格竞争激烈的情境（投标）中，低估尤其明显；在非价格竞争情境（内部开发）没有这种倾向，甚至相反。推论：低估的提案更容易中标，于是「赢家的诅咒」发生。',
       '<b>最小—最大区间太窄</b>：诸如 90% 置信区间，系统性偏窄，无法反映真实不确定性；PERT（三点估算）等方法仍假设人能给出可靠的最值。建议用<b>历史估算误差</b>来设定区间，而不是凭专家判断。',
       '<b>估算容易被误导，且很难从被误导中恢复</b>：所有估算都需要专家判断，而专家判断极易被<b>锚定</b>（estimation anchors）影响——在估算前或估算中知道预算、客户期望、可用时间，估算就会不自觉靠近这些锚；带倾向性的措辞（「这个又小又简单的项目要多少钱？」）也会误导。目前没有可靠方法中和这些偏差，唯一可行的是<b>不让估算者接触误导性信息</b>。',
       '<b>相关的历史数据与检查清单能提高精度</b>：当历史数据相关、清单按公司定制时，活动不易被遗漏，风险余量更可能被加入，经验更可能被复用；用类似项目做<b>类比估算</b>（analogy / reference class estimation）尤其有效。但许多公司两者都不用。',
       '<b>组合独立估算能提高精度</b>：不同来源估算的平均值通常比多数单个估算更准；关键假设是<b>独立性</b>（来源在专长、背景、估算过程上不同）。类似 Delphi 的过程——如<b>规划扑克</b>（Planning Poker），开发者同时亮出各自独立得出的估算——在软件估算中特别有用。群体过程还因知识共享而增值；「群体思维」与群体更高风险偏好的负面效应在软件估算中未被证实。',
       '<b>估算可能有害</b>：估算不仅预测未来，也经常影响未来。过低估算导致质量下降、后期返工、失败风险上升；过高估算则按<b>帕金森定律</b>（Parkinson’s law：工作会膨胀以填满可用时间）降低生产率。因此要问「是否真的需要估算」；若不需要或可推迟，等到信息更多时再估算更安全。敏捷只规划下一个冲刺或发布，正是避免过早估算之害的方式。')
  + p('三条「我们不知道」：')
  + ul('如何准确估算<b>超大型复杂项目</b>：赌注更大，但相关经验与历史数据更少；这类项目的活动常涉及业务流程变更与复杂干系人互动，极难估算；',
       '如何度量<b>软件规模与复杂度</b>以支持准确估算：多年研究提出的度量都不够好，能准确估算的情境似乎很少；',
       '如何度量并预测<b>生产率</b>：即使有了规模与复杂度，还要预测个人或团队的生产率；开发者与团队之间的生产率差异常常大得惊人；除「真实编程测试」（trialsourcing）外没有好方法。此外，我们甚至不知道软件项目是<b>规模经济</b>还是<b>规模不经济</b>：多数实证研究支持规模经济，而实践者通常相信规模不经济，且研究结果很可能是分析方法造成的假象。')
  + p('综述给出的六条可执行建议：建立并使用贴合本地情境的简单模型，并与专家估算结合；用历史估算误差设定最小—最大区间；避免接触误导性与无关信息；使用按本组织定制的检查清单；使用保证估算独立性的结构化群体过程；避免基于高度不完整信息的早期估算。')),
 kws=K(('project management', '项目管理', 'Ensuring software is delivered on time, on schedule and in accordance with requirements.'),
       ('success criteria', '成功标准', 'Agreed time, budget, customer expectations, coherent team.'),
       ('intangible product', '无形产品', 'Software cannot be seen or touched, so progress cannot be judged by looking at it.'),
       ('project risk', '项目风险', 'Risk affecting the schedule or resources.'),
       ('product risk', '产品风险', 'Risk affecting the quality or performance of the software.'),
       ('business risk', '业务风险', 'Risk affecting the organisation developing or procuring the software.'),
       ('risk planning', '风险计划', 'Avoidance, minimisation and contingency strategies for each risk.'),
       ('contingency plan', '应急计划', 'What to do if the risk actually arises.'),
       ('people management', '人员管理', 'Choosing people and establishing ways of working that lead to effective performance.'),
       ('Maslow’s hierarchy', '需求层次', 'Physiological, safety, belonging, esteem, self-actualisation needs.'),
       ('project plan', '项目计划', 'Resources, work breakdown and schedule; seven standard sections.'),
       ('plan-driven development', '计划驱动开发', 'The development process is planned in detail before work starts.'),
       ('release planning', '发布计划', 'Looks ahead several months and decides the features in a release.'),
       ('effort estimation', '工作量估算', 'Predicting effort; expert estimation still dominates practice.'),
       ('planning poker', '规划扑克', 'A Delphi-like process where estimators reveal independent estimates simultaneously.'),
       ('winner’s curse', '赢家的诅咒', 'The most optimistic bid wins, leading to overruns and lower quality.')),
 examples=(qa('例 1　写一张风险表',
   p('情境：某 5 人团队要在 4 个月内为一所学校做「选课与排课」系统，客户是教务处，学校 IT 只提供一台旧服务器，团队中只有一人懂排课算法。请识别 5 个风险，给出类别、概率、严重性、原因与应对。')
   + p('<b>分析：</b>先按五类清单扫一遍（技术、组织、人员、需求、估算），再为每个风险写「原因—事件—影响」。')
  + tb(('风险', '类别', '概率 / 严重性', '原因', '应对'),
       ('排课算法专家离职或病假', '项目风险（人员）', '中 / 严重', '单点知识，无备份', '避免：结对 + 文档化算法决策；应急：外部顾问名单'),
       ('旧服务器性能不足，排课计算超时', '产品风险（技术）', '高 / 严重', '硬件老旧，算法复杂度高', '最小化：先做性能原型验证；应急：申请云资源或降低排课频次'),
       ('教务处需求在开发中期大改（如增加走班制）', '产品风险（需求）', '高 / 严重', '政策变化；客户未参与早期评审', '避免：每两周演示 + 需求基线；应急：用范围置换而非延期'),
       ('开发工作量低估（4 个月实际需 6 个月）', '项目风险（估算）', '高 / 严重', '新团队、无历史数据', '避免：用类比估算 + 规划扑克；应急：砍可选功能'),
       ('学校 IT 无法提供接口文档', '业务风险（组织）', '中 / 可容忍', '对方运维人力不足', '最小化：提前约定接口清单与责任人；应急：用数据导入导出兜底'))
  + p('<b>要点：</b>每条风险都要有「应对」，且应对要区分避免（降概率）与应急（降影响）；只有「注意一下」不算风险计划。'))
  + qa('例 2　规划扑克的正确做法',
   p('情境：团队 6 人要用规划扑克估算一个用户故事「学生可在线申请缓考」。请写出流程，并说明为什么不能先说出「大概 5 天」再让大家出牌。')
   + p('<b>流程：</b>① 产品负责人朗读故事并说明验收标准，团队提问澄清；② 每人私下选一张牌（斐波那契数列：1、2、3、5、8、13…），<b>同时</b>亮牌；③ 若数值差异大，请最大与最小者各说明理由（尤其是低值者的隐含假设与高值者看到的风险）；④ 澄清后重新出牌；⑤ 重复至收敛，取共识值；⑥ 记录该故事的估算与讨论要点（作为后续类比估算的依据）。')
   + p('<b>为什么不能先说数字：</b>因为那会成为<b>估算锚点</b>。Jørgensen 指出，人在估算前或估算中知道预算、期望或其他数值，会不自觉地把估算拉向该值；且一旦被锚定，很难通过讨论完全恢复。同时亮牌保证估算<b>独立</b>，而独立估算的平均值通常比单个估算更准。')
   + p('<b>常见错误：</b>让最资深的人先出牌（锚定）；只取平均而不讨论分歧（丢掉分歧背后的信息）；把故事点当工时（故事点是相对度量）。'))
  + qa('例 3　估算区间与承诺',
   p('情境：团队历史数据显示，过去 10 个项目的实际工作量相对估算的中位偏差为 +35%，且偏差分布很宽（−10% 到 +120%）。本次估算为 200 人日。客户要求「给出 90% 把握的上限」。请给出一个务实的回答，并说明为什么不能用「200 × 1.1」。')
   + p('<b>分析：</b>先看历史：中位偏差 +35% 说明系统性低估；分布很宽说明不确定性大。用历史误差设定区间，而不是用专家的乐观判断（这正是 Jørgensen 的建议）。')
   + p('<b>计算：</b>若按中位偏差校正，期望值约为 200 × 1.35 = 270 人日；90% 上限应取历史分布的高分位，而不是中位数。若历史上有 1/10 的项目超过 +120%，则 90% 上限至少应覆盖 200 × 2.2 = 440 人日这一量级。')
   + p('<b>为什么不能用 200 × 1.1：</b>因为 1.1 是一个「乐观的、凭感觉的」缓冲，既没有覆盖系统性低估（+35%），也没有覆盖尾部风险（+120%）；PERT 式三点估算同样常给出过窄区间。')
   + p('<b>回答方式：</b>「按历史数据，50% 把握约 270 人日，90% 把握约 440 人日；若必须承诺一个日期，建议以 270 为计划值，并把范围裁剪到 270 能覆盖的部分。」这既诚实又可执行。'))
  + qa('例 4　敏捷计划与「日期不减」',
   p('情境：某团队 2 周一个冲刺，velocity 约 30 点。发布计划承诺 6 个冲刺交付 12 个特性（共 200 点）。到第 3 个冲刺末，只完成 70 点，客户要求「加人赶工，日期不变」。请给出你的处理方案。')
   + p('<b>分析：</b>先算现实：3 个冲刺完成 70 点 → velocity ≈ 23 点/冲刺，而非 30。剩余 3 个冲刺可完成约 69 点，合计约 139 点，距 200 点差 61 点。')
   + p('<b>处理：</b>① 按「范围可减、日期不减」原则，与客户按优先级裁剪约 60 点（约 3–4 个低优先级特性），把发布内容调整为 140 点左右；② 「加人」在敏捷里通常短期降低 velocity（新人需要带教、沟通成本上升），不应作为主要手段；③ 分析 velocity 下降原因（是否技术债、是否故事拆分过大、是否环境不稳定），并在回顾中改进；④ 把被裁剪的特性移入下一次发布，并明确新的发布计划。')
   + p('<b>考点：</b>这道题同时考 velocity 计算、范围/日期权衡、以及「加人不能线性加速」的工程常识（《人月神话》的经验，课件未直接提，但逻辑一致）。'))),
 practice=(ol('项目管理的四条成功标准是什么？为什么「团队状态」也算成功标准？',
         '风险分类的两个维度是什么？各举一例。',
         '为一个「关键供应商倒闭」的风险写出避免、最小化、应急三套策略。',
         'Maslow 的五层需求分别对应软件团队的什么管理动作？',
         '计划驱动的项目计划包含哪七个部分？为什么计划必须是迭代的？',
         'release planning 与 iteration planning 的区别是什么？「范围可减、日期不减」的含义是什么？')
   + det('参考答案与思路',
    p('<b>1.</b> 按时交付、成本在预算内、满足客户期望、维持连贯且运作良好的团队。因为项目是由人完成的；若交付后团队瓦解、知识流失，组织长期交付能力受损，下一项目会为此付出代价。')
    + p('<b>2.</b> 维度一：风险类型（技术、组织等）；维度二：受影响对象（项目/产品/业务）。例：技术类项目风险「采用新框架导致开发延期」；组织类业务风险「客户预算被削减」。')
    + p('<b>3.</b> 避免：合同中要求源码托管（escrow）与至少 5 年支持承诺；最小化：把该构件的接口封装在适配层，便于替换；应急：预先评估两个替代供应商并保留迁移脚本。')
    + p('<b>4.</b> 生理——保证工具、设备、环境；安全——清晰期望、一致反馈、明确计划与风险管理；归属——协作文化、开放沟通、认可贡献；尊重——成长机会、奖励、建设性反馈、授权；自我实现——挑战性任务、创新空间、职业发展。')
    + p('<b>5.</b> 引言、项目组织、风险分析、资源需求、工作分解、项目进度、监控与报告机制。因为信息随项目推进而增加，业务目标也会变化，计划不修订就会迅速失真。')
    + p('<b>6.</b> 发布计划看数月、决定一次发布包含哪些特性；迭代计划看 2–4 周、决定下一增量。含义是：当功能做不完时，减内容而不推迟交付日；这样交付节奏可预测，范围成为变量。'))),
 exam=(cal('exam', '必考', '四条成功标准、三个特殊性、三类风险、风险管理四步、七段项目计划、release/iteration planning、范围可减日期不减、估算的 30% 平均超支与七条结论。')
  + cal('warn', '易错 1', '把「风险」写成「问题」。风险是尚未发生的事件；已发生的是问题，进入问题管理而非风险管理。')
  + cal('warn', '易错 2', '把「避免」与「最小化」混用。避免降低发生概率，最小化降低影响。')
  + cal('warn', '易错 3', '认为敏捷不需要计划。课件明确：敏捷也需要启动计划以分配资源，只是增量功能不预先计划。')
  + cal('warn', '易错 4', '把估算区间当成承诺。区间表达不确定性；承诺需要范围与日期的显式权衡。')
  + cal('tip', '进阶', '能引用「赢家的诅咒」解释为什么投标越低越容易中标却越容易失败，并提出「客户少看价格多看能力」的对策，是本讲最能体现深度的一笔。')),
 checklist=(h2('做项目计划的清单')
  + st('写清四条成功标准，并与客户确认优先级（时间/成本/范围/质量）',
       '按五类清单识别风险，每条写「原因—事件—影响」',
       '为每个风险标概率与严重性，并写避免/最小化/应急三套策略',
       '做工作分解，标注依赖与检查点（前置/后置条件）',
       '估算用两种独立方法交叉验证（类比 + 规划扑克）',
       '用历史误差设定最小—最大区间，不用感觉设缓冲',
       '选计划方式：计划驱动（详细前置）或敏捷（release + iteration）',
       '约定交付规则：范围可减、日期不减；变更走范围置换',
       '定义监控与报告机制：进度、velocity、缺陷、风险复评节奏')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'p4–p8', '项目管理定义、四条成功标准、三个特殊性、六个影响因素、五类管理活动'),
   ('18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'p9–p16', '风险管理定义与不确定性来源、三类风险、四步流程、识别清单、分析与计划、what-if、监控'),
   ('18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'p17–p23', '人员管理原则、激励、Maslow 五层、三种人格类型'),
   ('18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'p24–p35', '项目计划定义与三阶段、定价、计划驱动优缺点、七段计划、迭代计划过程、现实假设与应急、风险缓解与重新计划'),
   ('18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'p36–p40', '敏捷计划、release/iteration planning、交付规则、困难与适用性'),
   ('18_Week 12/1_SE - Lecture 9 - 2026.pdf', 'p41–p44', 'AI 与项目管理四个方面'),
   ('What we do and dont know about software development effort estimation. .pdf', 'p1–p4', '30% 平均超支、专家估算主导、七条已知结论、三条未知、六条建议、赢家的诅咒'),
   ('（跳过）', '—', '本周无纯图片或行政页需跳过'),
   ('（补充）', '—', '风险表示例与 velocity 计算属应用性练习，不引入新考点'))))
# ============================================================ 10
LEC.append(L(
 slug='l10-quality-and-configuration-management',
 tzh='第 10 讲 · 软件质量与配置管理',
 ten='Software Quality and Configuration Management',
 keywords=['quality management', 'quality plan', 'fitness for purpose', 'quality attribute', 'product standard', 'process standard', 'quality culture', 'configuration management', 'version management', 'system building', 'change management', 'release management', 'branch', 'merge', 'rebase'],
 files=['19_Week 13/1_SE - Lecture 10 - 2026.pdf', '19_Week 13/3_Exercise Session 3 (1).pdf'],
 overview=(h2('本节定位')
  + p('这是 Module 2 的收官讲，把两个看似不同的主题放在一起：<b>质量</b>（产品做得好不好）与<b>配置管理</b>（在不断变化中，你怎么知道现在到底是哪个版本）。二者的连接点是「变更」：质量体系约束变更的质量，配置管理记录并控制变更本身。')
  + p('与前后衔接：第 7 讲给出了 SQM 的定义与度量，本讲展开为组织级/项目级框架、质量标准与质量计划；第 8 讲的演化与重构依赖版本管理与构建；第 11 讲的 CI 流水线是本讲「系统构建」的工程化实现。')
  + p('学完本节你应当能够：')
  + ck('说出质量管理的三个层面（组织、项目执行、项目质量计划）与质量团队的独立性要求',
     '写出一份质量计划的五个组成部分，并解释为什么它必须简短',
     '列出常用质量属性，并说明质量属性之间为什么必然冲突',
     '区分产品标准与过程标准，各举三例',
     '说出配置管理的四项活动，并解释为什么敏捷「不可能」离开配置管理工具',
     '设计分支策略与合并/变基方案，并说明冲突与回滚的处理方式')),
 detail=(h3('10.1 质量管理管三个层面')
  + p('软件质量管理关注「确保软件产品达到所需质量水平」。课件给出三个主要关注点：')
  + ol('<b>组织层面</b>：建立一套组织过程与标准的框架，使之能产出高质量软件；',
       '<b>项目层面（执行）</b>：应用具体的质量过程，并检查这些计划的过程是否被遵循；',
       '<b>项目层面（计划）</b>：为项目建立质量计划，阐明项目的质量目标，并定义将使用哪些过程与标准。')
  + p('质量管理活动应提供对开发过程的<b>独立检查</b>：检查项目交付物是否与组织标准及目标一致。因此<b>质量团队应独立于开发团队</b>，以便对软件采取客观视角、在不被开发问题影响的情况下报告质量。')
  + cal('exam', '必考', '「质量团队必须独立于开发团队」是常考点。独立性不是组织政治，而是保证报告的客观性——如果质量人员向项目经理汇报且绩效由进度决定，质量报告必然被软化。')
  + h3('10.2 质量计划')
  + p('质量计划阐明期望的产品质量、如何评估这些质量，并定义最重要的质量属性；它应定义质量评估过程，说明应应用哪些组织标准，必要时定义新的标准。')
  + p('质量计划的五个组成部分：产品介绍（product introduction）、产品计划（product plans）、过程描述（process descriptions）、质量目标（quality goals）、风险与风险管理（risks and risk management）。')
  + p('课件对篇幅有一条很实用的要求：<b>质量计划应当简短</b>——“If they are too long, no-one will read them.”（太长就没人看。）这句话可直接用于论述题：质量体系的失败往往不是缺文档，而是文档没人读。')
  + h3('10.3 质量管理的范围')
  + p('质量管理对大型复杂系统尤其重要：质量文档是进展的记录，并在开发团队更替时支撑开发的连续性。对较小系统，质量管理需要更少文档，应聚焦于建立<b>质量文化</b>；使用敏捷开发时，技术也必须演化。')
  + h3('10.4 软件质量的两种定义')
  + p('最简单的定义：质量意味着产品<b>符合其规格</b>（meet its specification）。但对软件系统，这有问题：')
  + ul('客户的质量要求（效率、可靠性）与开发者的质量要求（可维护性、可复用性）之间存在<b>张力</b>；',
       '有些质量要求难以无歧义地规定；',
       '软件规格通常<b>不完整且常常不一致</b>。')
  + p('因此关注点可能应转向「<b>适用于目的</b>」（fitness for purpose）而非「符合规格」。课件的六个检查问题很好地说明了「适用于目的」的含义：')
  + ol('软件是否已被恰当测试？',
       '软件是否足够可靠、可以投入使用？',
       '软件在正常使用中的性能是否可接受？',
       '软件是否可用（usable）？',
       '软件结构是否良好、是否可理解？',
       '开发过程中是否遵循了编程与文档标准？')
  + h3('10.5 非功能特性决定主观质量')
  + p('课件给出一条经验判断：软件的<b>主观质量</b>很大程度上取决于其<b>非功能特性</b>。这反映真实的用户体验——如果软件功能不是用户期望的，用户往往会绕过它、找别的办法完成目标；但如果软件不可靠或太慢，用户实际上<b>无法</b>达成目标。')
  + p('这句话与第 4 讲「非功能需求可能比功能需求更关键」是同一判断的两种表述，可以互相引用。')
  + p('常用质量属性（课件列了 15 个）：安全性（safety）、可理解性（understandability）、可移植性（portability）、安全性（security）、可测试性（testability）、可用性（usability）、可靠性（reliability）、适应性（adaptability）、可复用性（reusability）、韧性（resilience）、模块化（modularity）、效率（efficiency）、健壮性（robustness）、复杂性（complexity）、可学习性（learnability）。')
  + p('质量冲突不可避免：任何系统都不可能对所有属性最优——例如提高健壮性可能损失性能。因此质量计划必须定义「对本软件最重要的质量属性」，并包含质量评估过程的定义：一种约定的、判断某质量（如可维护性或健壮性）是否存在于产品中的方式。')
  + cal('warn', '易错', '把「质量高」当成一个单一维度。质量是多属性向量，且属性之间冲突；说「这个系统质量很高」而不说明在哪些属性上、以什么为代价，是不专业的表述。')
  + h3('10.6 过程质量与产品质量')
  + p('开发产品的质量受生产过程质量的影响。这在软件开发中很重要，因为有些产品质量属性难以评估（例如可维护性）。但课件也提醒：软件过程与产品质量之间的关系<b>非常复杂且理解不足</b>——个人技能与经验的应用尤其重要；外部因素（应用的新颖性、需要加速的开发进度）可能损害产品质量。')
  + p('「基于过程的质量」（process-based quality）的逻辑是：如果过程被定义为能产出高质量产品的过程，并且过程被遵循、被度量、被改进，那么产品质量就有了间接保证。这也是 CMMI/SPICE 类模型的立论基础（第 3 讲）。')
  + h3('10.7 质量文化')
  + p('质量管理者应致力于建立<b>质量文化</b>：让所有对软件开发负责的人都承诺达到高产品质量；鼓励团队为自己工作的质量负责，并开发新的质量改进方法；支持关注质量「无形方面」的人；鼓励所有成员的专业行为。')
  + p('为什么文化重要？因为质量体系能约束「可检查的动作」，但无法约束「没写下来的偷懒」。第 11 讲 Telerik 案例中「每个人都对产品有 ownership」正是质量文化的组织版本。')
  + h3('10.8 标准：产品标准与过程标准')
  + p('标准定义产品或过程所需的属性，在质量管理中作用重要。标准可以是国际、国家、组织或项目标准。它的三个作用：封装最佳实践（避免重复过去的错误）；提供「在特定情境中质量意味着什么」的框架（即该组织对质量的看法）；提供连续性（新员工通过理解所用标准来理解组织）。')
  + tb(('类别', '英文', '适用对象', '例子'),
       ('产品标准', 'product standards', '被开发的软件产品', '设计评审表单、需求文档结构、方法头格式、Java 编程风格、项目计划格式、变更请求表单'),
       ('过程标准', 'process standards', '开发过程中应遵循的过程', '设计评审的组织方式、新代码提交构建的流程、版本发布流程、项目计划审批流程、变更控制流程、测试记录流程'))
  + p('标准的三个问题（很现实）：可能被工程师认为不相关、不过时；常涉及过多官僚式填表；若没有工具支持，维护与标准相关的文档就要做大量枯燥的填表工作。')
  + h3('10.9 敏捷中的质量管理')
  + p('敏捷开发中的质量管理是<b>非正式的、而非基于文档的</b>：它依赖建立质量文化，让所有团队成员对软件质量有责任感并采取行动维持质量。敏捷社区从根本上反对标准式方法与质量过程所带来的官僚开销。')
  + p('三条「共享好实践」（shared good practice，可直接作为代码评审清单）：')
  + ol('<b>Check before check-in</b>：程序员有责任在代码提交到构建系统之前，与其他成员组织自己的代码评审；',
       '<b>Never break the build</b>：成员不应提交导致系统失败的代码；开发者必须针对整个系统测试自己的改动，并确信其按预期工作；',
       '<b>Fix problems when you see them</b>：若程序员发现他人代码中的问题或不清晰之处，可以直接修复，而不是转回给原作者。')
  + p('评审在敏捷中通常是非正式的：Scrum 在每个迭代完成后有<b>冲刺评审</b>（sprint review），可讨论质量问题；XP 用<b>结对编程</b>保证代码持续被另一名成员检查。')
  + p('敏捷质量管理在大型系统中的三个局限：为外部客户开发大系统时，最少文档的敏捷质量管理可能不实际——大客户有自己的质量过程，会要求以兼容方式报告进展；多个地理分布、可能来自不同公司的团队参与开发时，非正式沟通不实际；长寿命系统的开发团队会变化，没有文档，新成员可能无法理解开发。')
  + h3('10.10 配置管理：在不断变化中保持可辨识')
  + p('软件系统在开发与使用中持续变化。配置管理（CM）是「管理变化中的软件系统的策略、过程与工具」。为什么需要它？因为很容易失去对「每个系统版本里到底包含哪些变更与构件版本」的追踪；对团队项目，CM 是控制不同开发者所做变更所必需的。')
  + p('四项配置管理活动：')
  + tb(('活动', '英文', '做什么'),
       ('版本管理', 'version management', '跟踪系统构件的多个版本，确保不同开发者对构件的修改不互相干扰'),
       ('系统构建', 'system building', '把程序构件、数据与库组装起来，编译成可执行系统'),
       ('变更管理', 'change management', '跟踪来自客户与开发者的变更请求，核算变更的成本与影响，决定是否实施'),
       ('发布管理', 'release management', '为对外发布准备软件，并跟踪已发布给客户使用的系统版本'))
  + p('注意「变更管理」在三个语境中的不同含义：第 4 讲是<b>需求</b>变更管理（变更提案与追溯），本讲是<b>配置</b>变更管理（变更请求、成本、影响、是否实施），第 13 讲的项目计划里是<b>项目</b>变更管理（计划偏差的纠正）。三者共享「记录—评估—决策—实施」的骨架。')
  + h3('10.11 敏捷与配置管理')
  + p('敏捷开发中构件与系统每天被修改多次，<b>没有 CM 工具是不可能做到的</b>。典型流程是：构件的权威版本保存在共享的项目仓库中；开发者把它们复制到自己的工作区；修改代码后用构建工具在自己机器上构建新系统并测试；满意后把修改过的构件送回项目仓库。')
  + p('这条流程解释了为什么「分支/合并策略」在敏捷中不是可选项：多人高频修改同一仓库，冲突是常态而非例外。')
  + h3('10.12 版本控制与分支策略（练习课补充）')
  + p('练习课给出的定义：版本控制是管理源代码与文档变更的系统；它记录每次修改的历史，支持协作开发、分支管理与回滚操作，从而提高可维护性与开发效率。常见系统分两类：<b>集中式</b>（如 SVN）与<b>分布式</b>（如 Git）。')
  + tb(('维度', '集中式 centralized（SVN）', '分布式 distributed（Git）'),
       ('仓库位置', '单一中央服务器保存全部历史', '每个克隆都是完整仓库，含全部历史'),
       ('离线工作', '受限（需连服务器）', '可完全离线提交，之后推送'),
       ('分支成本', '较高（常靠目录复制）', '极低（分支只是指针）'),
       ('权限控制', '集中、细粒度', '以仓库/分支为单位，较弱'),
       ('典型风险', '服务器单点故障', '历史分散，需要约定推送与评审流程'))
  + p('分支规划（branch planning）：主分支（main/master）应始终可发布；功能分支（feature branch）从主分支切出，完成后经评审合并；修复分支用于紧急缺陷；发布分支用于冻结与打补丁。关键约定是「主分支永远绿」——这与敏捷的「Never break the build」是同一条纪律。')
  + p('合并策略：<b>merge</b> 保留分支历史与真实分叉，产生合并提交；<b>rebase</b> 把提交「重放」到目标分支之上，得到线性历史，但会改写提交哈希。经验规则是：<b>共享分支上用 merge，未推送的本地分支上可用 rebase 整理历史</b>；对已推送的公共分支做 rebase 会破坏他人的历史。')
  + p('冲突处理与回滚：冲突应「小步、频繁」地解决——频繁从主分支同步可把冲突控制在几行之内；回滚优先用「反向提交」（revert）而不是改写历史（reset --hard），因为后者会让协作者的历史分叉。这些是工程约定，考试通常考「merge 与 rebase 的区别及适用场景」。')
  + h3('10.13 AI 与软件质量管理')
  + p('课件的最后一节把 AI 对质量管理的影響分成三块。第一块是从「被动测试」走向「预测性工程」的四种能力：')
  + ul('<b>自动化测试生成</b>：生成式 AI 把用户故事与代码库转成单元与端到端测试脚本，大幅削减手工编写工作；',
       '<b>自愈式自动化</b>：AI 实时检测 UI 与布局变化，自动修复失效的测试定位器，无需人工干预；',
       '<b>预测性缺陷分析</b>：机器学习分析提交历史与代码复杂度，在缺陷进入生产前标记高风险模块；',
       '<b>智能优化</b>：AI 根据最近代码变更决定跑哪些测试用例，加速 CI/CD 反馈回路。')
  + p('第二块是它对质量管理「三个主要关注点」的重塑：组织标准（如 ISO 9001 扩展到 AI 治理、数据隐私与偏差标准，如 ISO/IEC 42001）；动态最佳实践（AI 监控跨项目遥测，持续更新编码标准、标记架构反模式）；持续过程审计（AI 以自动检查 CI/CD 流水线与拉取请求的合规性，替代人工把关）；自适应项目质量计划（质量计划从静态文档变成「活蓝图」，根据历史数据动态调整测试覆盖与风险优先级）。')
  + p('第三块是收益与新风险的权衡：已有文献显示 AI 驱动分析把缺陷检出率提高 <b>30%–50%</b>，同时减少误报与维护成本；系统综述确认 LLM 测试生成与 ML 预测能达到比传统自动化更高的代码覆盖率；但存在「代码质量悖论」——若不加约束，AI 生成的代码可能增加代码变动率、重复与安全漏洞（高出 23.7% 到 2.74 倍）。课件的共识是：AI 是质量保证的强大「力量倍增器」，但严格的人工监督与成熟的治理仍不可或缺。')),
 kws=K(('quality management', '质量管理', 'Ensuring that the required level of quality is achieved in a software product.'),
       ('quality plan', '质量计划', 'Sets out desired product qualities, how they are assessed, and which standards apply.'),
       ('fitness for purpose', '适用于目的', 'Quality judged by whether the software serves its purpose, not merely by specification conformance.'),
       ('quality attribute', '质量属性', 'Safety, security, reliability, usability, maintainability, efficiency, testability, etc.'),
       ('quality conflict', '质量冲突', 'Improving one attribute, e.g. robustness, may degrade another, e.g. performance.'),
       ('quality culture', '质量文化', 'Everyone responsible for development is committed to high product quality.'),
       ('product standard', '产品标准', 'Applies to the software product, e.g. document structure, coding style.'),
       ('process standard', '过程标准', 'Defines the process to be followed, e.g. review conduct, change control.'),
       ('configuration management', '配置管理', 'Policies, processes and tools for managing changing software systems.'),
       ('version management', '版本管理', 'Tracking multiple versions of components and preventing interference between developers.'),
       ('system building', '系统构建', 'Assembling components, data and libraries and compiling an executable system.'),
       ('release management', '发布管理', 'Preparing software for external release and tracking released versions.'),
       ('branch', '分支', 'An independent line of development; feature branches merge back to main.'),
       ('merge', '合并', 'Combines histories and creates a merge commit; used on shared branches.'),
       ('rebase', '变基', 'Replays commits onto another base for a linear history; rewrites hashes.'),
       ('technical debt', '技术债', 'Short-term shortcuts that raise the cost of future change.')),
 examples=(qa('例 1　写一份质量计划的骨架',
   p('情境：某 6 人团队为医院开发预约系统，合同要求「符合医院信息安全规范，且上线后 6 个月内缺陷修复响应不超过 4 小时」。请写出质量计划的五个部分，并各给一句具体内容。')
   + p('<b>解：</b>')
  + tb(('部分', '内容示例'),
       ('产品介绍', '面向患者与导诊台的预约系统，含挂号、改约、取消、通知四个核心流程；首批上线 3 个科室。'),
       ('产品计划', 'M1 完成需求基线；M2 完成核心流程与安全加固；M3 通过发布测试与验收；上线后进入 6 个月保障期。'),
       ('过程描述', '需求评审 → 设计评审 → 代码评审（check before check-in）→ 自动化回归（每次提交）→ 独立发布测试 → 验收测试。'),
       ('质量目标', 'P0 缺陷零遗留；关键流程响应 ≤ 1.5 s（95 分位）；安全规范逐条核查通过；缺陷修复响应 ≤ 4 h。'),
       ('风险与风险管理', '风险：安全规范条款理解偏差；措施：邀请医院信息安全负责人参加设计评审并签字确认。'))
  + p('<b>要点：</b>质量目标必须可度量（分位数、时限、条款清单），否则无法评估；质量计划要与合同条款对齐，而不是另起一套。'))
  + qa('例 2　两种质量观的取舍',
   p('情境：某通用软件产品完全符合其规格文档，但用户抱怨「太慢、经常崩」。产品经理说「我们符合规格，质量没问题」。请用本讲的两种质量观分析，并给出改进方向。')
   + p('<b>分析：</b>「符合规格」是开发视角的质量；「适用于目的」是用户视角的质量。该产品在第一种意义上合格，在第二种意义上不合格。')
   + p('<b>为什么会出现这种分裂：</b>课件指出三个原因——客户与开发者的质量要求存在张力（开发者关注可维护性，客户关注效率与可靠性）；部分质量要求难以无歧义规定（「快」没有阈值）；规格本身不完整、常不一致（遗漏了性能与故障恢复）。')
   + p('<b>改进方向：</b>① 把「快」「稳」写成可验证的非功能需求（响应时间分位数、可用性目标、故障恢复时间）；② 把非功能特性纳入发布测试与验收标准（第 7 讲的性能与压力测试）；③ 在质量计划中明确「本项目最重要的三个质量属性」，并接受其他属性的妥协；④ 建立用户反馈到需求变更的通道（第 4 讲的变更管理）。')
  + p('<b>结论：</b>「符合规格」是必要条件，「适用于目的」才是充分条件；质量计划应同时覆盖两者。'))
  + qa('例 3　分支策略与合并方案',
   p('情境：某团队 8 人，用 Git，两周一个冲刺，每天多次提交；有 3 个功能并行开发，另有 1 个紧急线上缺陷要修。主分支必须随时可发布。请设计分支策略，并说明合并与回滚规则。')
   + p('<b>设计：</b>① <code>main</code> 保护分支，只接受通过评审与 CI 的合并，始终可发布；② 每个功能一个 <code>feature/xxx</code> 分支，从 main 切出，小步提交，每日从 main 同步（merge 或 rebase 本地未推送部分）；③ 紧急缺陷从 main 切 <code>hotfix/xxx</code>，修复后同时合并回 main 并打标签发布；④ 每个冲刺末从 main 切 <code>release/x.y</code> 用于冻结与回归，只接受缺陷修复。')
  + p('<b>合并规则：</b>功能分支合并到 main 用 <b>merge</b>（保留上下文与评审记录，且不破坏他人历史）；开发者在自己<b>未推送</b>的分支上可用 <b>rebase</b> 整理提交，使评审更清晰。禁止对已推送的 main 做 rebase。')
  + p('<b>冲突与回滚：</b>冲突通过「每日同步 + 小 PR」控制在几行内；回滚线上问题时用 <code>revert</code> 生成反向提交（保留审计轨迹），而不是 <code>reset --hard</code> 改写公共历史；发布版本用 tag 标记，回滚即回到上一个 tag。')
  + p('<b>与配置管理四活动的对应：</b>分支与保护规则 = 版本管理；CI 构建 = 系统构建；PR 评审与变更单 = 变更管理；tag 与发布分支 = 发布管理。'))
  + qa('例 4　敏捷质量体系在大客户项目中的改造',
   p('情境：某 30 人团队用 Scrum 为一家银行开发信贷审批系统。银行要求每季度提交质量报告、提供需求到测试的追溯矩阵、并通过外部审计。团队的「非正式质量文化」被打回。请给出改造方案。')
   + p('<b>分析：</b>这正是课件指出的三个局限中的两个——大客户有自己的质量过程并要求兼容报告；系统受外部监管。非正式做法不足以满足证据要求。')
   + p('<b>方案：</b>① 保留敏捷内核（冲刺、评审、结对、CI），但在每个冲刺的 Definition of Done 中加入「追溯矩阵更新」「质量指标快照」；② 用工具自动生成追溯矩阵（需求 ID ↔ 提交 ↔ 测试用例 ↔ 测试结果），把「文档负担」转成「流水线副产品」；③ 把冲刺评审的纪要、缺陷趋势、覆盖率作为季度质量报告的素材，避免另做一套；④ 对审计关注的过程标准（评审记录、变更控制）保留最小但完整的证据链；⑤ 质量角色独立于开发（向质量负责人而非项目经理汇报），以满足独立性要求。')
  + p('<b>结论：</b>敏捷与合规不是二选一；关键是让「证据」由流程自动产生，而不是事后补文档。'))),
 practice=(ol('质量管理的三个层面是什么？质量团队为什么必须独立？',
         '质量计划的五个部分是什么？为什么课件要求它必须简短？',
         '「符合规格」与「适用于目的」的差别是什么？各有什么困难？',
         '写出至少八个质量属性，并给出一对相互冲突的属性及原因。',
         '产品标准与过程标准各举三例。标准有哪三个常见问题？',
         '配置管理的四项活动是什么？敏捷为什么离不开配置管理工具？')
   + det('参考答案与思路',
    p('<b>1.</b> 组织层面（过程与标准框架）、项目层面（执行质量过程并检查遵循）、项目层面（制定质量计划）。独立是为了客观报告质量，不受开发进度与开发问题的压力影响。')
    + p('<b>2.</b> 产品介绍、产品计划、过程描述、质量目标、风险与风险管理。太长就没人读，质量体系会退化为「抽屉里的文档」。')
    + p('<b>3.</b> 符合规格 = 按写下来的要求做（困难：规格本身不完整、不一致，且难有无歧义表述）；适用于目的 = 真正满足使用需要（困难：需要理解用户真实场景，且「目的」会随业务变化）。')
    + p('<b>4.</b> 安全性、可靠性、可用性、效率、可维护性、可测试性、可移植性、可复用性、健壮性、可理解性。冲突例：健壮性 vs 效率——增加校验、重试与冗余会带来额外开销；性能 vs 可维护性——大粒度构件快但难替换，细粒度可替换但通信开销大（第 6 讲）。')
    + p('<b>5.</b> 产品标准：需求文档结构、方法头格式、Java 编程风格；过程标准：设计评审的组织、变更控制流程、版本发布流程。问题：被认为不相关/过时；官僚式填表过多；缺工具支持时维护成本高。')
    + p('<b>6.</b> 版本管理、系统构建、变更管理、发布管理。因为敏捷每天多次修改构件与系统，没有仓库、构建与版本追踪就无法协调多人修改，也无法知道「当前构建里是哪一版」。'))),
 exam=(cal('exam', '必考', '质量管理的三个层面与独立性、质量计划五部分、fitness for purpose、质量属性冲突、产品/过程标准区分、敏捷三条共享好实践、配置管理四活动、merge 与 rebase。')
  + cal('warn', '易错 1', '把「质量 = 符合规格」当成唯一标准。课件明确指出规格不完整、不一致，因此要引入适用于目的。')
  + cal('warn', '易错 2', '把「质量团队独立」理解成「质量团队可以不做技术判断」。独立性是报告路径的独立，不是专业上的隔离。')
  + cal('warn', '易错 3', '把配置管理的「变更管理」与需求变更管理混为一谈。前者管构件与构建版本，后者管需求基线。')
  + cal('warn', '易错 4', '认为 AI 能替代人工监督。课件明确：AI 是力量倍增器，但严格人工监督与成熟治理仍不可或缺。')
  + cal('tip', '进阶', '能指出「质量体系的成本不在写文档，而在维护一套没人读的文档」，并提出「让证据由流水线自动产生」的解法，是本讲最能体现工程判断的一笔。')),
 checklist=(h2('质量与配置管理清单')
  + st('确定本项目最重要的 2–3 个质量属性，其余明确妥协',
       '为每个质量目标写可度量判据（分位数、时限、条款清单）',
       '写质量计划五部分，控制在一到两页',
       '确认质量报告的路径独立于开发进度压力',
       '选定产品标准（文档结构、编码风格）与过程标准（评审、变更、发布）',
       '把三条敏捷好实践写进团队公约：check before check-in、never break the build、fix problems when you see them',
       '建立仓库与分支策略：main 保护、feature 短生命周期、hotfix 独立、release 冻结',
       '约定合并规则（共享分支 merge、本地未推送可 rebase）与回滚规则（revert 优先）',
       '让追溯矩阵与质量指标由 CI 自动生成，而不是事后补文档')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('19_Week 13/1_SE - Lecture 10 - 2026.pdf', 'p4–p8', '质量管理三个关注点、质量活动的独立检查、质量计划结构与简短要求、范围与文化'),
   ('19_Week 13/1_SE - Lecture 10 - 2026.pdf', 'p9–p16', '质量的两种定义与困难、适用于目的的六问、非功能特性、质量属性清单与冲突、过程与产品质量、质量文化'),
   ('19_Week 13/1_SE - Lecture 10 - 2026.pdf', 'p17–p23', '标准的定义与层级、产品/过程标准对照、标准的问题、敏捷质量管理、三条共享好实践、评审、大系统局限'),
   ('19_Week 13/1_SE - Lecture 10 - 2026.pdf', 'p24–p26', '配置管理定义与必要性、四项活动、敏捷与 CM 的工作流'),
   ('19_Week 13/1_SE - Lecture 10 - 2026.pdf', 'p27–p29', 'AI 与 SQM：测试生成、自愈、预测缺陷、智能优化；三个关注点的重塑；收益与风险'),
   ('19_Week 13/3_Exercise Session 3 (1).pdf', 'p4–p5', '版本控制定义、集中式与分布式、分支规划、合并策略、冲突与回滚（练习课要求）'),
   ('（跳过）19_Week 13/2_Exercise Session 7.pptx', '全篇', '复习课行政页，未纳入讲义'),
   ('（跳过）19_Week 13/2_Exercise Session 7.pptx', '全篇', '复习课行政页，未纳入讲义'),
   ('（补充）', '—', 'merge/rebase 的具体规则与 revert 优先原则属工程约定补充'))))

# ============================================================ 11
LEC.append(L(
 slug='l11-agile-practices-workshop',
 tzh='第 11 讲 · 习题课：Scrum、冲刺、探针与规划扑克的实践',
 ten='Agile Practices in Action: Scrum, Sprints, Spikes, Poker and CI',
 keywords=['daily scrum', 'sprint backlog', 'burn-down chart', 'spike', 'planning poker', 'feature-driven development', 'velocity', 'story point', 'Kanban', 'WIP limit', 'continuous integration', 'technical testing debt', 'subcutaneous test', 'flash-cut'],
 files=['10_Week 4/2_Exercise Sessions/data/Scrums, Sprints, Spikes and Poker.pdf', '11_Week 5/2_Exercise Sessions/data/Pearsons Successmaker.pdf', 'Enabling Agile Testing Through Continuous Integration.pdf'],
 overview=(h2('本节定位')
  + p('前几讲把敏捷讲成了「模型与原则」，这一讲把它落成「每天怎么过、每个冲刺怎么开、估算怎么做、集成分支怎么管」。三份材料各提供一个视角：Telerik 案例给出一个把敏捷做成「组织设计」的公司；Pearson 案例给出一次从瀑布到敏捷的「闪切」及其成长阵痛；CI 经验报告给出测试人员如何用持续集成把测试塞进开发循环。')
  + p('这一讲是第 2 讲（Scrum/XP 术语）、第 7 讲（TDD 与测试分层）、第 10 讲（构建与版本管理）三者的交汇处，也是第 12 讲案例研究的分析工具箱。')
  + p('学完本节你应当能够：')
  + ck('描述一个冲刺从计划到回顾的完整仪式链，并说清每个仪式的产出',
     '用 burn-down chart 与 velocity 判断团队进展，并解释故事点为何是相对度量',
     '设计并主持一轮规划扑克，说明「同时亮牌」与「讨论离群值」的作用',
     '对比 Scrum 与 Kanban 的适用条件，说明 WIP 限制与吞吐量的含义',
     '画出并解释一条 CI 流水线（从代码提交到测试报告的每一步）',
     '解释「技术测试债」与「皮下测试」的含义，并说明它们与 CI 的关系')),
 detail=(h3('11.1 为什么要有这一讲')
  + p('敏捷宣言与 Scrum 术语都很容易背，但真实团队卡住的往往不是定义，而是细节：每日站会开成汇报会、冲刺计划会开成讨价还价、估算变成拍脑袋、集成变成每两周一次的痛苦合并。这一讲用三个真实组织把这些细节摊开。')
  + p('三个案例的分工：<b>Telerik</b> 展示「敏捷作为组织设计」——物理空间、团队结构、人力资本政策如何支撑敏捷；<b>Pearson</b> 展示「转型」——瀑布的具体失败、闪切的执行、以及 Scrum 与 Kanban 的选择；<b>CI 经验报告</b> 展示「工程实践」——测试如何通过持续集成嵌入开发循环。')
  + h3('11.2 一个冲刺的完整仪式链')
  + tb(('仪式', '英文', '参与者', '产出'),
       ('冲刺计划', 'sprint planning', '产品负责人 + 团队', '冲刺目标、冲刺待办列表（sprint backlog）、任务拆分'),
       ('每日站会', 'daily scrum', '团队（ScrumMaster 主持，管理者可旁听但不得替团队决策）', '当天计划、障碍清单'),
       ('开发与集成', 'development & integration', '团队', '可工作的增量、通过测试的构建'),
       ('冲刺评审', 'sprint review', '团队 + 干系人', '对增量的反馈、待办列表调整'),
       ('回顾', 'retrospective', '团队', '改进项（下个冲刺执行）'))
  + p('Telerik 的每日站会只有约 <b>15 分钟</b>：成员报告昨天的开发、当前目标与遇到的问题；站会旁边是「scrum board」（任务板）。Pearson 的案例补充了一个关键细节：<b>站会时所有人站着</b>，目的是让人简洁、把会议控制在 15 分钟内；并且「除团队成员外，任何人不得参与团队层面的决策」——管理者可以旁听，但不能替团队决定当天怎么做。')
  + cal('warn', '易错', '把每日站会开成「向经理汇报进度」。站会的目的是团队<b>自我协调</b>：谁需要帮助、今天怎么分工、什么阻碍了进展。一旦变成汇报，团队就会开始「表演忙碌」，障碍也不会被暴露。')
  + h3('11.3 冲刺、待办列表与燃尽图')
  + p('Telerik 的项目通常以 <b>1–2 周</b>为一个冲刺；从产品待办列表（product backlog）中选入某冲刺的软件特性称为<b>冲刺待办列表</b>（sprint backlog）。冲刺的配套工具是<b>燃尽图</b>（burn-down chart）：描绘该冲刺中「还剩多少工作要完成」，张贴在团队工作区，<b>每天更新</b>。开发以迭代方式持续，直到产品功能完整。')
  + p('燃尽图的读法：横轴是时间（天），纵轴是剩余工作量（故事点或任务数）；理想线是从左上到右下的直线；实际线若长期高于理想线，说明进度落后；若出现「阶跃式下降」，说明任务被批量完成而不是持续流动——后者常是任务拆分过大或集成不及时的信号。')
  + p('Pearson 案例给出另一种度量：<b>velocity</b> 由「把每个用户故事折算成标准的工作量单位（story points），再统计每个冲刺完成了多少点」得到。课件特别指出，velocity 的作用是帮助团队估计「一个冲刺能覆盖多少」，并作为衡量绩效改进的基准。')
  + cal('exam', '必考', '故事点是<b>相对</b>度量，不是工时；velocity 是<b>估计</b>，不是承诺。把两者混用会导致「点 = 人日」的隐性换算，最终退化为工时估算。')
  + h3('11.4 探针与规划扑克')
  + p('<b>探针（spike）</b>：若开发者对某个特性没有把握，可以先实现一个<b>基础原型</b>（basic prototype），以便更多地了解该特性以及它应如何被正确开发。探针的本质是「用最小成本买信息」，其产出通常是知识而非可交付功能；因此它应当有时间盒（例如 1–3 天），结束时必须给出结论：可行/不可行、预估范围、风险清单。')
  + p('<b>规划扑克（planning poker）</b> 是 Telerik 的估算方式，也是 Jørgensen 综述推荐的「保证独立性的结构化群体过程」。Telerik 的做法：决定下一阶段要做的特性后，请每位开发者估算所需时间；用一套写有不同天数的特制扑克牌；每人选一张<b>面朝下</b>放在桌上；所有人选完后<b>同时翻开</b>；开发者讨论各自的估算并解释选择，尤其是估值最低与最高的人；过程重复若干轮，理想情况下估算收敛。其哲学是「让开发者以合理的方式达成共识」。')
  + p('为什么这些细节重要：同时亮牌保证<b>独立性</b>（避免锚定）；讨论离群值是把「隐性假设」变成「共享知识」；多轮收敛避免「取平均」掩盖分歧。Jørgensen 指出，独立估算的平均值通常比多数单个估算更准，而群体过程还能因知识共享而增值。')
  + h3('11.5 Telerik：把敏捷做成组织设计')
  + p('背景：Telerik 2002 年由四位大学毕业生在索菲亚创立，做 Microsoft .NET 的 UI 控件；2011 年已是全球领先的 .NET UI 控件供应商，400 多名员工、9 个地点、3 个大洲；2012 年控件产品线超过 160 个产品，10 万多家组织在 94 个国家使用。2006 年起全面采用敏捷开发。')
  + p('组织设计的关键特征：')
  + tb(('维度', '做法', '作用'),
       ('团队结构', '每队 7–10 人，混合分析、设计、编程专长；每队有 team leader（通常是资深技术员工）与独立的 unit manager（履行项目经理职能，保证进度并负责跨团队沟通）', '团队对「开发、交付、支持自己的产品」负全责，产生 ownership；unit manager 承担对外协调，让技术 leader 专注团队'),
       ('物理空间', '开放式办公、簇状工作区、专门的团队协作与晨会区域；无高管独立办公室；两位联席 CEO 在不同团队区域办公并每 6–9 个月轮换', '缩短沟通路径，管理者「在前线」获得信息'),
       ('自主权', '团队被赋予高度自主与决策权', '与「人重于过程」原则一致'),
       ('人力资本', '只招有学位、英语流利、具备相关技能者；招聘广告甚至写入「Alpha Geek behavior」；入职配 coach（领域专家）、mentor（资深员工）与 team leader；离职率 5%，行业平均接近 75%', '高技能 + 低流动是敏捷能运转的前提'),
       ('发布节奏', '多数产品线每年 3 个发布日（前三季度各一次），具体日期由高管与 team leader 根据工作量、节假日确定', '给客户可预期的节奏，同时保留调整空间'))
  + p('团队使用的具体实践：每日 scrum；结对编程（一人写、一人评论建议，提升生产率并减少错误）；重构（持续改善设计以提升可读性、可维护性、可扩展性）；设计模式（复用经过验证的设计，加快开发并获得健壮设计）；测试驱动开发（每几行代码就被充分测试）；特性驱动开发（FDD，按特性增量迭代，用规划扑克估算）；冲刺与探针；以客户为导向的支持（电话、邮件、博客、问卷、投票、支持反馈）；短周期（产品 3–9 个月，团队同时负责修错、扩展功能与客户支持）。')
  + p('课件给出一组很有用的经验数字：CEO 估计「约 6 个月让一个团队达到生产力阶段，12 个月让产品上市，18 个月让产品获得 traction」；公司只做项目计划，不做更长期的业务战略。')
  + p('案例末尾的张力：公司快速扩张（新增澳大利亚办公室），创始人担心「作为成功关键的文化与团队过程能否在地理扩张中被复制」。这正好对应第 2 讲的 scaling out 问题：敏捷的成功很大程度来自「大家在一起」，一旦分布式，非正式沟通的优势会消失。')
  + cal('tip', '分析角度', '回答「敏捷是软件设计工具还是组织设计工具」时，最有力的论证是 Telerik：它同时改了流程（scrum、TDD、结对）、结构（7–10 人全职能团队、team leader + unit manager）、空间（开放簇状、无高管办公室）与人力政策（招聘、导师、低流动）。四者缺一，敏捷就退化为「每天开个站会」。')
  + h3('11.6 Pearson：一次闪切与它的成长阵痛')
  + p('背景：Pearson 数字学习部门的 SuccessMaker 是帮助中小学生学数学与阅读的软件；2005 年开始一次重大升级（从客户端-服务器转向互联网交付，并全面重做教学内容），投入约 3000 万美元；但上线 6–8 个月后市场接受度差，早期采用者抱怨「不满足任何需求」。')
  + p('瀑布失败的具体机制（案例列得很清楚）：')
  + ul('<b>开发团队驱动一切决策</b>，而非产品管理；开发与客户之间几乎没有直接沟通，导致许多「用心良苦」的功能完全偏离需求；',
       '<b>需求在周期开始时被正式文档冻结</b>，而大部分软件在印度离岸开发，美印团队间误解常见；受合同约束，开发中期修改功能要么昂贵要么不可能；',
       '<b>多年路线图承诺</b>：功能被单独预算并写进业务单元战略计划，任何变更都被视为负面的「scope creep」（范围蔓延）；这使内部规划容易，却几乎不投入精力去确认「承诺的功能是否真的满足客户需要」。')
  + p('转型的执行（闪切 flash-cut）：周五还在瀑布，周一就 100% 敏捷；时机选在第二版发布到制造（刻盘）之后；部分成员因不适应而离职。课件强调这「既是流程变革，也是文化变革」。')
  + p('培训分三阶段（这个结构很适合答题）：① 讲清敏捷方法的<b>底层理由</b>，确保所有人理解核心原则；② 讲<b>如何在敏捷框架内工作</b>，讨论具体工作实践；③ 聚焦 SuccessMaker 团队，请成员说出「为什么敏捷在我们这里行不通」，主动回应这些担忧——教练指出，若不主动处理，残留的疑虑会在数周甚至数月后以行为形式表现出来。')
  + p('组织与角色的调整：先把离岸开发全部转回内部（在亚利桑那招聘开发者），因为敏捷要求几乎每日的紧密协作；开发与 QA 原本是两个独立自治团队，转为<b>合并</b>并互相交叉培训；产品管理从「被动救火」变为<b>驱动</b>开发与特性优先级；每个团队设 scrum master 帮助移除障碍；开发团队按 Release 3 拆成四个组（两个 Java 组、一个报表与课程逻辑组、一个 Flash 动画组）。')
  + p('成长阵痛（案例的核心冲突）：')
  + ul('<b>QA 的角色危机</b>：过去 QA 不接触开发，只等代码完成，按独立于详细需求文档的测试用例检查，发现缺陷只负责「报回去」；新模式下没有需求文档，整个团队（开发 + QA）共同对「冲刺结束时交付可工作代码」负责，职责边界模糊，QA 感到「缺少问责与可追踪性」，并试图把瀑布做法带回来；',
       '<b>管理者的越位</b>：scrum 允许管理者参加每日站会，但规定「除团队成员外，任何人不得参与团队层面的决策」；案例中管理者越来越多地介入任务管理，产品副总不得不反复提醒「团队要自我管理日常计划」；',
       '<b>velocity 下降</b>：Release 3 的前几个冲刺 velocity 显著下降；副总认为这与团队「回归瀑布习惯」同时发生，并非巧合；关键开发者因此建议从 Scrum 改为 Kanban。')
  + p('转型的量化结果（可作为「敏捷收益」的论据）：代码库减半，功能数增加最多 75%，新功能受客户好评；开发团队规模缩小至少三分之一（主要通过取消离岸团队）。')
  + p('仍存在的问题：只有软件开发团队转了敏捷，内容团队等仍用瀑布；端到端集成测试与测试完全自动化仍是「进行中」，需要时仍会退化为「迷你瀑布」；产品负责人能准确规划「每个开发团队两个冲刺」，希望随着成熟度提高规划到三到四个迭代，但这要求 velocity 更稳定、迭代目标更可预测；团队对「自己的 velocity 是多少」理解不一致，难以向客户承诺发布；<b>上下文切换</b>（context switching）——同一迭代内从一个特性切到另一个特性，导致反复熟悉系统构件、velocity 下降，需要建立「特性与系统构件的映射」；维护发布仍不顺畅。')
  + h3('11.7 Scrum 还是 Kanban')
  + p('案例把两种方法的差别讲得很清楚：')
  + tb(('维度', 'Scrum', 'Kanban'),
       ('节奏', '时间盒（timebox）：固定长度冲刺，每冲刺交付一批', '无时间盒：持续流动，按需拉取'),
       ('限制对象', '限制「一个冲刺内承诺多少」', '限制「每一步在制品数量」（WIP limit）'),
       ('核心度量', 'velocity（每冲刺完成的故事点）', 'throughput（单位时间完成的特性数）与周期时间'),
       ('承诺时点', '冲刺计划时承诺冲刺内容', '把承诺推迟到特性真正进入开发时'),
       ('看板', '任务板（scrum board）', 'Kanban 板：可视化工作流与队列'),
       ('来源', '敏捷软件开发', '精益制造 / 丰田生产系统（TPS），JIT 的「拉动」系统'))
  + p('Kanban 的原始含义：日语「看板」即「signboard」；下游工序需要更多部件时，通过看板卡向上游「拉取」，因此是<b>拉动系统</b>（pull system）；除卡片外，Kanban 还包括对生产流的分析与优化，通过限制系统与各工序的<b>在制品</b>来减少浪费（muda，無駄），提升整体吞吐。软件 Kanban 把这些原则用于「用户故事创建 → 开发 → 测试 → 部署」等步骤，用每步的 WIP 限制来优化整体流程，并聚焦系统瓶颈。')
  + p('决策建议（答题框架）：若团队的问题是「承诺不准、节奏不稳」，Scrum 的时间盒与 velocity 更有帮助；若问题是「某一步骤长期堵塞（如测试排队）、需求到达不均匀、维护与插单频繁」，Kanban 的 WIP 限制与流动度量更合适。案例中的团队 velocity 下降伴随「回归瀑布习惯」，此时换方法可能只是换症状，真正要解决的是 QA 角色与自管理；这也是副总「想守住自己熟悉的方法」的合理之处，但他需要以数据（周期时间、在制品、缺陷逃逸率）而不是偏好来做决定。')
  + h3('11.8 持续集成：让测试进入开发循环')
  + p('CI 经验报告的作者是一位做了八年瀑布测试的测试人员，2007 年转入敏捷团队。他最初两个冲刺仍用传统测试方法（测试计划、澄清需求、写用例、用例评审），结果每个迭代都时间不够、覆盖不足；「技术测试债」（technical testing debt）以「每个冲刺末要跑的手工回归测试」的形式累积，而 team 根本没时间跑。')
  + p('他总结出七项必须落地的敏捷测试实践：')
  + ol('定义并执行「刚好够」的验收测试（just-enough acceptance tests），让客户为团队定义外部质量，并让所有人相信故事在冲刺末是完整可用的；',
       '尽可能自动化接近 100% 的验收测试，防止手工回归集不断膨胀形成技术测试债；',
       '用 xUnit 框架 + 应用 API 做「皮下测试」（subcutaneous test），比 GUI 自动化更少脆弱、更易开发与维护回归套件；',
       '每次构建（至少每天）运行回归套件中的全部验收测试，快速反馈「既有功能是否被新代码破坏」；',
       '冲刺内为所有新代码开发单元测试，提升内部质量，并使「刚好够」的验收测试成为可能；',
       '每次构建运行全部单元测试，快速反馈单元级回归；',
       '每天多次构建，使最新代码与变更在整个工作日都被测试与演练，也让开发者更频繁集成、更快发现集成问题。')
  + p('他们的问题：没有任何自动化框架；构建过程需要三次才能无错通过；没有单元与功能测试自动化。')
  + p('解决方案是 CI。课件引用 Martin Fowler 的定义：')
  + p('“a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily – leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible.”（团队成员频繁集成各自的工作，通常每人至少每天集成一次，从而每天有多次集成；每次集成都由自动化构建（含测试）验证，以尽快发现集成错误。）')
  + p('CI 的典型事件链（这是「画流水线」题的標準答案骨架）：检测仓库变更 → 取最新源码 → 编译（解释型语言则做 lint 等检查）→ 编译失败即停止 → 运行单元测试 → 失败即停止 → 部署到测试环境 → 运行自动化验收测试 → 失败即停止 → 发布构建到公共位置 → 通知团队并生成报告（跑了哪些测试、多少、构建号、结果链接）。')
  + p('该团队的具体实现（可作为「落地细节」的例证）：两台物理机 + 两台虚拟机，一台物理机托管构建虚拟机、另一台托管测试虚拟机；工具包括 Automated Build Studio（构建与 CI）、STAF（跨机远程命令）、Visual Studio 2008（编译）、Surround（源码仓库）、VBScript（重置测试虚拟机）、三个 C# 辅助程序（Test Distributor / Test Runner / Test Results Processor）、NUnit（单元与验收测试框架）。')
  + p('用 Fowler 的十项实践做前后对比，可以看到 CI 的成熟度模型：单一源码仓库；自动化构建；构建自测试；每人每天提交；每次提交都在集成机上构建主干；保持构建快速（他们的构建 10–15 分钟，并指出「重构要尽早做」）；在类生产环境的克隆中测试（用干净的虚拟机测试客户端）；让任何人容易获得最新可执行版本（统一构建输出位置 + 构建邮件附链接）；让所有人看到发生了什么（Web 界面 + 邮件状态）；自动化部署。')
  + p('作者的三条复盘经验值得记住：① 让测试与开发<b>并行</b>，打破了测试与开发之间传统的割裂关系；② 「自动化接近 100% 验收测试」听起来可怕，但「皮下测试 + xUnit」让它变得可行，代价是测试人员要写更多代码、学习产品 API；③ 说服开发者「自动化测试是好主意」不难，难的是让他们愿意经历搭建 CI 的「痛苦驼峰」——在小团队里没有「额外时间」，作者只能用午休、晚上与周末做概念验证，等构建能自动触发、测试虚拟机自动启动后，开发者才被吸引并同意把剩余任务排进冲刺待办。')),
 kws=K(('daily scrum', '每日站会', 'A short stand-up meeting, about 15 minutes, to share progress, plans and obstacles.'),
       ('sprint backlog', '冲刺待办列表', 'The features selected from the product backlog for one sprint.'),
       ('burn-down chart', '燃尽图', 'Shows work remaining in a sprint, updated daily in the team area.'),
       ('spike', '探针', 'A basic prototype built to learn about a feature and how to develop it.'),
       ('planning poker', '规划扑克', 'Estimators choose cards face down and reveal simultaneously, then discuss outliers.'),
       ('story point', '故事点', 'A relative measure of effort used to size user stories.'),
       ('velocity', '速率', 'Story points completed per sprint; an estimate, not a commitment.'),
       ('feature-driven development', '特性驱动开发', 'Incremental development organised around features chosen to give the client extra functionality.'),
       ('Kanban', '看板', 'A pull system with work-in-progress limits and no timebox; uses throughput.'),
       ('WIP limit', '在制品限制', 'A cap on items in progress at a step, used to expose and relieve bottlenecks.'),
       ('continuous integration', '持续集成', 'Integrating at least daily, with every integration verified by an automated build including tests.'),
       ('technical testing debt', '技术测试债', 'Accumulated manual regression tests the team has no time to run.'),
       ('subcutaneous test', '皮下测试', 'Acceptance tests automated through the application API with an xUnit framework rather than the GUI.'),
       ('flash-cut', '闪切', 'Immediate, complete switch from one methodology to another.'),
       ('context switching', '上下文切换', 'Moving between features within an iteration, which reduces velocity.'),
       ('just-enough acceptance test', '刚好够的验收测试', 'Acceptance tests defined by the customer to confirm a story is complete and functional.')),
 examples=(qa('例 1　主持一轮规划扑克',
   p('情境：团队 5 人估算故事「学生可在 App 上查看本学期课表并导出为日历文件」。前三位分别出 3、5、8，第四位出 21。请写出你的主持步骤，并分析 21 可能反映什么。')
   + p('<b>步骤：</b>① 让产品负责人读完故事与验收标准（含支持的日历格式、时区处理、课表数据来源），团队提问；② 五人同时亮牌；③ 请出 21 的人先说明理由（通常是他看到了别人没看到的复杂性）；④ 再请出 3 的人说明其假设（可能假设课表数据已有现成 API）；⑤ 澄清后重投；⑥ 若仍分歧，取共识或拆小故事；⑦ 记录估算与关键假设。')
   + p('<b>21 可能反映：</b>课表数据分散在三个系统且无统一 API；需要处理跨时区与夏令时；日历格式（ICS）的重复规则复杂；权限与隐私（谁能看谁的课表）。这些恰恰是「出低值者看不到的风险」。')
   + p('<b>要点：</b>先请高值者发言是刻意的——它把风险摆到桌面上，避免团队被低值锚定。这与 Jørgensen 的「避免锚定」建议一致。'))
  + qa('例 2　spike 还是直接排期',
   p('情境：团队要在冲刺中实现「离线模式下提交表单，恢复网络后自动同步」。无人做过离线冲突合并。请判断是否应该做 spike，并给出 spike 的验收标准。')
   + p('<b>判断：</b>应当做 spike。理由：存在<b>技术不确定性</b>（冲突合并策略、本地存储容量、同步顺序），若直接排进冲刺，很可能到冲刺末才发现方案不可行，导致承诺失败。探针的作用正是「用最小成本买信息」。')
   + p('<b>spike 设计：</b>时间盒 2 天；目标只验证一件事——「两人同时离线修改同一条记录，恢复后能否以可接受的方式合并」；产出是「可行/不可行 + 推荐策略 + 预估范围 + 风险清单」，<b>不要求生产级代码</b>。')
   + p('<b>验收标准：</b>① 有一个可运行的演示（两个客户端、一个服务端）；② 记录三种冲突场景的结果；③ 给出对正式故事的估算（例如 8 点还是 13 点）；④ 明确未解决的风险（如大数据量下的存储上限）。')
   + p('<b>常见错误：</b>把 spike 做成「半个正式实现」并直接上线——探针代码通常缺少错误处理、测试与性能考量。'))
  + qa('例 3　设计一条 CI 流水线',
   p('情境：某团队做 Java Web 应用，仓库用 Git，测试用 JUnit，部署到 Kubernetes。要求「每次提交 15 分钟内给出反馈」。请设计流水线阶段与失败策略。')
   + p('<b>流水线：</b>')
  + tb(('阶段', '动作', '时长目标', '失败策略'),
       ('触发', '监听 main 与 PR 分支的 push', '即时', '—'),
       ('构建', '拉取源码、编译、静态检查（lint/格式）', '≤ 3 min', '失败即停止并通知提交者'),
       ('单元测试', '运行全部单元测试（并行分片）', '≤ 5 min', '失败即停止；标记该提交不可合并'),
       ('打包', '生成制品并打版本号/提交哈希', '≤ 1 min', '失败即停止'),
       ('部署到测试环境', '用干净环境部署（等价于生产镜像）', '≤ 2 min', '失败即停止并回滚环境'),
       ('验收测试', 'API 级（皮下）验收测试 + 少量端到端', '≤ 4 min', '失败即停止；保留日志与截图'),
       ('发布与通知', '制品归档到公共位置；邮件/IM 通知结果与链接', '即时', '—'))
  + p('<b>关键设计判断：</b>① 快速失败——把最便宜、最快的检查放前面；② 环境洁净——每次用干净容器/虚拟机，避免「上次残留」造成的假通过；③ 测试分层——大量皮下测试 + 少量端到端，兼顾速度与信心；④ 保持构建快（案例中 10–15 分钟，并指出「重构要尽早做」）；⑤ 失败必须阻断合并（never break the build）。')
  + p('<b>与课件对应：</b>这条流水线正是 Fowler 十项实践中「自动化构建、构建自测试、每次提交构建主干、保持构建快、在类生产环境克隆中测试、自动化部署、让所有人看到」的组合。'))
  + qa('例 4　Scrum 还是 Kanban',
   p('情境：某运维团队负责 20 个内部系统，工作内容是「修故障 + 小改动 + 临时请求」，每天插入的新请求平均 6 个，测试环节经常排队 3 天。团队试过两周冲刺，但冲刺目标几乎每次都被插单打断。请给出建议与度量方案。')
   + p('<b>分析：</b>症状匹配 Kanban 的适用条件：需求到达不均匀、插单频繁、某一环节（测试）长期堵塞。Scrum 的时间盒与冲刺承诺在这种环境下会不断被破坏，团队挫败感强。')
   + p('<b>建议：</b>改用 Kanban：① 可视化工作流（待办 → 开发 → 代码评审 → 测试 → 发布）；② 为每列设 WIP 限制，尤其把「测试」列的 WIP 压到团队能消化的数量，让排队显性化；③ 把承诺推迟到「进入开发」时（Kanban 的这一特性正好适配插单）；④ 设立「 expedite 通道」但限制同时只允许一个紧急项。')
  + p('<b>度量：</b>用 throughput（每周完成项数）与 cycle time（从进入到完成的中位时间）；用累积流量图（cumulative flow diagram）看哪一列在变宽（即瓶颈）；不要用 velocity（那是 Scrum 的度量）。')
  + p('<b>何时回 Scrum：</b>若后续工作转为「有明确版本目标的产品开发」，且插单减少、团队稳定，Scrum 的时间盒与冲刺评审更利于聚焦与干系人对齐。方法可以换，但换方法必须由数据驱动，而不是由「不顺手」驱动。'))),
 practice=(ol('写出一个冲刺的五个仪式及各自产出。',
         '燃尽图长期高于理想线说明什么？出现阶跃式下降又说明什么？',
         '规划扑克为什么要同时亮牌？为什么要先请估值最高的人发言？',
         '什么情况下应该做 spike？spike 的产出是什么，不应是什么？',
         'Scrum 与 Kanban 在「限制什么」上的根本差别是什么？',
         '写出 CI 事件链的八个步骤，并说明「快速失败」如何体现。')
   + det('参考答案与思路',
    p('<b>1.</b> 冲刺计划（冲刺目标与冲刺待办）；每日站会（当天计划与障碍）；开发与集成（可工作增量）；冲刺评审（干系人反馈与待办调整）；回顾（改进项）。')
    + p('<b>2.</b> 长期高于理想线 = 进度落后于计划（可能估算偏低或障碍未清除）。阶跃式下降 = 任务被批量完成而非持续流动，常见于任务拆分过大、集成不及时、或「冲刺末突击」。')
    + p('<b>3.</b> 同时亮牌保证估算独立，避免第一个人说出来后形成锚定；先请最高值发言是为了把「别人没看到的风险」先摆上桌，避免团队被低值锚定。')
    + p('<b>4.</b> 存在技术不确定性、且直接排期可能导致冲刺承诺失败时应做 spike。产出是知识（可行/不可行、方案建议、估算范围、风险清单），不应是生产级功能。')
    + p('<b>5.</b> Scrum 限制「一个时间盒内承诺多少」（时间盒 + 冲刺范围）；Kanban 限制「每一步的在制品数量」（WIP limit），不设时间盒，按吞吐与周期时间度量。')
    + p('<b>6.</b> 检测变更 → 取源码 → 编译/静态检查 → 单元测试 → 部署测试环境 → 验收测试 → 发布制品 → 通知与报告。「快速失败」体现在：任何阶段失败立即停止，且最便宜最快的检查排在最前。'))),
 exam=(cal('exam', '必考', '冲刺仪式链、燃尽图读法、故事点与 velocity 的性质、规划扑克规则、spike 的用途、Scrum 与 Kanban 的差别、CI 定义（Fowler 原句）与事件链、皮下测试与技术测试债。')
  + cal('warn', '易错 1', '把故事点当工时。故事点是相对度量，跨团队不可比。')
  + cal('warn', '易错 2', '把每日站会当汇报会。它是团队自我协调的机制，管理者旁听但不决策。')
  + cal('warn', '易错 3', '认为 CI 就是「有个构建服务器」。CI 的核心是「频繁集成 + 每次集成都由含测试的自动化构建验证」。')
  + cal('warn', '易错 4', '把 Kanban 当成「没有节奏的 Scrum」。Kanban 用 WIP 限制与流动度量替代时间盒与 velocity。')
  + cal('tip', '进阶', '能用 Telerik 的「流程 + 结构 + 空间 + 人力政策」四件套论证「敏捷是组织设计」，并用 Pearson 的 QA 角色危机说明「只改流程不改角色定义会导致回退」，是本讲最高阶的答法。')),
 checklist=(h2('运行敏捷实践的清单')
  + st('冲刺计划：只承诺 velocity 能覆盖的范围，并把故事拆到 1–2 天粒度',
       '每日站会：站着、15 分钟、只谈昨天/今天/障碍，管理者不替团队决策',
       '看板/任务板：每列设 WIP 限制，阻塞项标红并当天处理',
       '估算：先澄清验收标准，再用规划扑克同时亮牌，讨论离群值后重投',
       '不确定性高时先开 spike（时间盒 1–3 天），产出结论与估算而非功能',
       '每日多次构建，每次构建跑全部单元测试，合并前跑验收测试',
       '验收测试走 API（皮下测试），尽量自动化，避免手工回归债',
       '冲刺评审请真实干系人看增量，回顾只产出 1–2 个可执行改进项',
       '度量用 velocity（Scrum）或 throughput/cycle time（Kanban），不用来考核个人')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('10_Week 4/2_Exercise Sessions/data/Scrums, Sprints, Spikes and Poker.pdf', 'p1', 'Telerik 背景、每日 scrum 与 scrum board、敏捷管理哲学'),
   ('10_Week 4/2_Exercise Sessions/data/Scrums, Sprints, Spikes and Poker.pdf', 'p2–p6', '保加利亚软件业、Telerik 历史与规模、工作环境、产品与技术、敏捷方法的价值与批评'),
   ('10_Week 4/2_Exercise Sessions/data/Scrums, Sprints, Spikes and Poker.pdf', 'p7–p10', '团队规模与角色、七项具体实践（scrum、结对、重构、设计模式、TDD、FDD 与规划扑克、冲刺与探针）、客户支持、发布节奏、人力资本'),
   ('10_Week 4/2_Exercise Sessions/data/Scrums, Sprints, Spikes and Poker.pdf', 'p11–p15', '奖项、Telerik 价值观、招聘文案（组织文化证据）'),
   ('11_Week 5/2_Exercise Sessions/data_Pearsons Successmaker.pdf', 'p1–p8', 'SuccessMaker 背景、瀑布失败机制、闪切与三段培训、团队重组、QA 角色危机、管理者越位、velocity 下降、成果与遗留问题、上下文切换、Scrum 与 Kanban'),
   ('11_Week 5/2_Exercise Sessions/data_Pearsons Successmaker.pdf', 'p9–p13', '瀑布小结、敏捷十二原则与 Scrum 概述、Kanban 的定义与度量'),
   ('Enabling Agile Testing Through Continuous Integration.pdf', 'p1–p3', '测试人员转型、技术测试债、七项敏捷测试实践、问题诊断、CI 定义与事件链、实现布局与工具'),
   ('（跳过）10_Week 4/2 与 11_Week 5/2 的 Exercise Sessions 页面', '全篇', 'Telerik 与 Pearson 两份案例讨论说明页，讨论题已并入 11.3–11.7'),
   ('（拓展）', '—', 'Kanban 源自丰田生产系统与精益制造的「拉动」与 muda 概念，属背景拓展'),
   ('Enabling Agile Testing Through Continuous Integration.pdf', 'p4–p6', 'Fowler 十项实践前后对比、七项实践验收、复盘经验（并行测试、皮下测试、痛苦驼峰）'))))
# ============================================================ 12
LEC.append(L(
 slug='l12-case-studies',
 tzh='第 12 讲 · 案例研究：IBM、Sasken、EXCEED 与 Catalise',
 ten='Case Studies: IBM, Sasken, EXCEED and Ethical AI at Catalise',
 keywords=['iterative development', 'code freeze', 'back out', 'late requirement', 'offshore development', 'value network', 'product maturity', 'defect rate', 'root cause analysis', 'V-process', 'test automation', 'data bias', 'precision', 'recall', 'ethical AI'],
 files=['16_Week 10/2_Case Study/data/IBM.pdf', 'Sasken.pdf', '16_Week 10/2_Case Study/data/EXCEED.pdf', '17_Week 11/2_Case Study/data/Move Fast, but without Bias - A.pdf'],
 overview=(h2('本节定位')
  + p('这一讲把四个真实组织放在一起，用同一套分析框架检验前面十讲的概念：需求变更（第 4 讲）、迭代与阶段（第 2、3 讲）、质量与度量（第 7、10 讲）、分布式团队与过程纪律（第 8 讲）、伦理（第 1 讲）。案例课的目的不是「知道这几家公司发生了什么」，而是练出一种可迁移的判断：面对不完整信息，如何给出有证据支撑的立场。')
  + p('四个案例的互补性：IBM 考「迭代末期的范围决策」；Sasken 考「离岸产品开发的过程纪律与质量体系」；EXCEED 考「用数据区分相关与因果」；Catalise 考「速度与伦理的冲突」。')
  + p('学完本节你应当能够：')
  + ck('用案例法三步（阅读准备、小组讨论、全班讨论）分析一个管理决策，并给出有证据的立场',
     '解释 IBM 六周迭代的节奏安排，并分析「末期插入需求」的三种选项与代价',
     '说明 Sasken 案例中「产品成熟度、过程纪律、质量、离岸协作、文化差异」如何相互作用',
     '用 EXCEED 的测试与网络数据判断「低生产率」的多种可能原因，并指出哪些是相关而非因果',
     '分析 AI 产品中的数据偏差、精确率与召回率的取舍，并援引 ACM/IEEE 原则给出行动方案',
     '从四个案例中提炼三条跨案例的规律，并用证据支持')),
 detail=(h3('12.1 案例法：没有标准答案，但有证据标准')
  + p('课件的案例课采用三步法：')
  + ol('<b>案例阅读与准备</b>：案例是对某组织领导所面对真实情境的详细描述，除背景信息外，还包含一个<b>必须做出的关键决策</b>；你的任务是分析所给信息（这些信息是<b>故意不完整</b>的），判断你会怎么做。',
       '<b>小组讨论</b>：把想法带到一个背景多样的小组，讨论发现，从不同视角理解案例。',
       '<b>全班讨论</b>：在小范围讨论后，准备在与全班讨论时修正自己的想法；要求主动倾听与参与，设身处地考虑「如果我是案例主角」，并解释推理。')
  + p('八条阅读指南（可直接作为考试答题的步骤清单）：先读案例的首尾两节定位核心情境；快速扫读其他章节与图表，知道信息在哪而不背细节；先看讨论题并记下初读得到的要点（核心情境、主角目标、重大不确定性）；列出「要理解情境、达成目标还缺哪些关键信息」；边读边标记与清单对应的信息；仔细分析这些信息如何帮助理解主要问题；目标是形成一个有充分支持的立场（案例通常没有客观正确答案，最好的方案是证据最强的方案）；随着新信息出现，不断问「它如何改变我对主要问题的理解」，并考虑替代观点。')
  + h3('12.2 IBM：迭代末期的范围决策')
  + p('情境：2010 年 11 月，IBM Rational 产品开发负责人 John Lalonde 收到 WebSphere 产品开发负责人 Neil Mayor 的请求：为一个客户需求在 Rational 产品中增加一项功能，使 WebSphere 能交付某个特性。该客户需求潜在带来 <b>4000 万美元</b>收入（WebSphere 3000 万 + Rational 1000 万），但提出得<b>非常晚</b>——两个产品的开发周期都已进入<b>最后几个迭代</b>。')
  + p('背景：IBM 2010 年营收 998 亿美元、利润 148 亿美元，五大业务板块（全球技术服务、全球商业服务、软件、系统与技术、全球融资）。软件板块毛利率约 80%，竞争激烈。RAD（Rational Application Developer）与 WAS（WebSphere Application Server）高度互相依赖，IBM 总在同一天发布两者的大版本，但它们由<b>独立业务单元</b>管理，预算、人员、资源各自独立。RAD 2005 年由收购的 Rational 平台与 IBM 自有平台合并而成；两者都由美洲、亚洲、欧洲的数百名开发者开发。')
  + p('IBM 的迭代方法（关键细节）：项目周期 3–15 个月；RAD 这次是 18 个月（2009-06-25 起），与 WAS 同在 2010-12-22 发布；<b>每个迭代 6 周 = 4 周计划/设计/实现 + 2 周测试</b>；前 4 周内架构师与开发者写设计文档，后段开发者写代码，测试者用设计文档开发测试计划与场景，测试计划需干系人批准；2 周测试期内修缺陷；<b>若某缺陷在本次迭代内无法修复且导致某特性不可用，则把该特性的全部代码整体回退（back out）</b>，缺陷修复与该特性推迟到下一迭代；所有特性完成并测试后进入<b>代码冻结</b>（code freeze），此后不得新增代码。')
  + p('这个「回退」规则是案例的技术核心：它保证「任何迭代交付的特性都像可发布一样完整」，代价是可能浪费已完成的代码，并把压力转移到下一迭代的计划与设计团队。')
  + p('案例对瀑布的批评也值得引用：支持者认为瀑布迫使团队彻底理解需求、把设计定死，从而省时省钱；反对者认为不可能在进入下一阶段前把当前阶段做到完美——设计阶段无法预见实现阶段的困难，需求会演化，且测试只能在实现完全结束后才开始，导致缺陷发现极晚、极难修。')
  + p('三个选项（答题时必须都摆出来）：')
  + tb(('选项', '做法', '收益', '代价与风险'),
       ('接受需求', '申请在最后迭代写代码，开发该功能', '拿下 4000 万美元；避免客户流向 Oracle/HP 等竞品', '可能破坏质量、延误发布（IBM 对客户有发布日承诺）；末期改动可能引入回归缺陷'),
       ('做原型子集', '交付只含部分功能的原型，完整功能后续交付', '降低延期与缺陷风险；挽回部分收入', '需说服客户接受原型并等待；客户若拒绝则可能丢掉 4000 万'),
       ('拒绝或推迟', '不在本版本做，排入下一版本', '保护质量与发布日', '直接损失收入；客户关系与 2015 路线图受影响'))
  + p('分析框架：先算「不做的代价」（4000 万 + 客户终身价值 + 竞品替代风险），再算「做的代价」（末期改动的回归风险 × 发布延误的合同违约风险），最后看「有没有第三条路」（原型、功能开关、灰度、只在特定配置下提供）。课件没有给答案，但给了判断所需的全部数字与约束——这正是案例法的训练目标。')
  + h3('12.3 Sasken：离岸产品开发的三重压力')
  + p('情境：Sasken 是印度的通信软件公司（1989 年成立，2009 年约 3300 人，21 项美国专利），为全球无线设备厂商提供研发外包。2006 年，它受日本一家领先手机厂商委托，为高端手机开发<b>高级多媒体播放器</b>；项目在班加罗尔离岸中心执行，而日本是当时全球最先进的移动服务市场。')
  + p('为什么难：日本市场在手机功能与服务上领先世界（iMode 1999 年即提供常驻互联网接入；2001 年 10 月即商用 3G；2006 年日本手机市场销售额 112 亿美元、4730 万部）；日本运营商以「价值网络」（value network）方式与设备商、内容商、平台商紧密协作，<b>接口规范由运营商制定并持续升级</b>，这与西方以标准委员会为中心的松散模式不同。Sasken 必须满足这些由运营商层层传递下来的接口与质量标准。')
  + p('两个项目的对比（这是案例最有教学价值的结构）：')
  + tb(('维度', 'codec 项目（2001 起）', 'media player 项目（2007 起）'),
       ('技术层次', '多媒体子系统<b>底层</b>（codec/driver 层）', '多媒体子系统<b>上层</b>（应用、控制器、协议栈）'),
       ('规格明确度', '协议/软件层次的下层定义得相对清楚；Sasken 已有可移植的 RCI 架构，软件成熟稳定', '上层规格常常不如下层明确'),
       ('主要挑战', '按客户性能目标做定制（编解码速度、内存占用）', '功能完整性与规格理解；流媒体与 DRM；媒体传输协议移植'),
       ('结果', '质量与时间完全可控；客户随后追加多个芯片平台的移植订单', '挑战大得多，暴露了产品成熟度、过程纪律、需求演化、质量与协作的全部问题'))
  + p('五个压力源（可作为分析框架）：')
  + ol('<b>产品成熟度</b>：产品开发地点应靠近用户所在地；离用户与市场远，就难以完整构想特性并纳入架构。团队可能「漏掉重要功能却不自知」，而客户期望的是<b>完整产品</b>，并把「基础功能集」视为理所当然——对 Sasken 团队而言，客户眼中的基础功能往往变成「定制与变更请求」，导致周期与工作量上升。日本市场还领先 1–2 年，进一步加剧了这种差距。',
       '<b>过程纪律</b>：客户频繁修改需求却仍期望不延期，团队容易通过压缩评审与测试来缩短周期；在短周期里做的许多变更叠加严格接口约束，会使实现逐渐偏离原设计，使后续修改越来越贵，并降低可维护性、可移植性与可复用性。过程管理要求：使用公司成熟过程并按情境裁剪；使用配置管理系统与集中缺陷库；度量、分析并采取纠正措施。',
       '<b>需求演化</b>：欧美客户习惯以详尽书面协议明确需求；日本客户偏好<b>隐性、持续协商</b>的协议，且常在产品发布前才签约，供应商需前期投入并承担质量与时间风险。',
       '<b>质量</b>：日本项目缺陷率中位数为 <b>0.020</b>，欧洲 0.225、印度 0.263、美国 0.400（每千行代码的缺陷密度口径）。缺陷分「测试缺陷」（实验室内发现并修复）与「现场缺陷」（客户在运行现场报告），后者是重要的可靠性度量。缺陷从运营商 → 客户测试团队 → Sasken 测试团队逐级下传，修复反向回流；<b>所有现场缺陷修完前产品不被接受，且每一层测试都接受修复后，测试请求才算关闭</b>；客户还要求详细的根因分析报告与预防措施。',
       '<b>离岸协作与文化</b>：Sasken 在日本派驻测试工程师作为联络（而非传统由销售市场人员组成的 bridgehead），他们有目标测试设施；但完整的测试平台因运营商对客户的限制条款无法提供给印度团队，因此印度团队常需「想象」缺陷场景才能修，导致多次往返。缺陷登记从简单表格膨胀为含解决时间、迭代次数的度量表，客户用它做跟踪分析，但团队认为交换笨重的表格效率低。语言与文化的直接后果是：邮件沟通易误解；客户希望有位能流利说日语、且文化契合的日本本地项目经理；日本工作时长显著更长（每周 60 小时以上者约占非农业劳动力 12%）；Sasken 团队偏年轻（许多人首次做产品开发），客户项目经理则有 20–25 年经验，期望极高。')
  + p('商业模式的反差也值得注意：Sasken 起家于产品开发，但服务业务已占收入 90% 以上，其中 90% 以上是「时间与材料」（time and materials）计费——资源按人天计费，投入与支出极小，因而「主动的项目管理」需求不明显；而产品开发是<b>固定价格</b>，必须靠有效管理与监控才能在预算内完成并取得正回报。这解释了为什么产品项目对项目经理的要求远高于服务项目。')
  + p('结局：2008 年 5 月，含音频、视频、流媒体的播放器在客户捆绑手机上上线；2008 年 8 月，约 25 名工程师继续开发与支持 codec，另 25 人支持播放器；Sasken 把这段经验复用到欧美客户项目。项目经理的总结很精辟：「日本在移动多媒体与互联网应用上总比世界其他地方领先 1–2 年，因此为日本客户开发产品很有挑战——必须在最严格的质量管理下使用最新技术，并具备随需求变化的敏捷性；但这段经验让我们后来能复用到欧美客户。」')
  + h3('12.4 EXCEED：用数据区分相关与因果')
  + p('情境：2017 年 2 月，Exceed Communications（2013 年成立，36 人，总部中东 + 班加罗尔离岸中心）的总经理 Karamath 收到客户 H&K 的升级投诉：某软件包的系统测试进展缓慢，且测试阶段发现多个缺陷。该客户投诉频率明显高于其他客户。项目按<b>时间与材料</b>计费，客户密切监控人员规模与生产率；开发采用 <b>V 过程模型</b>（需求 → 概设 → 详设 → 编码 → 单元/集成/系统/验收测试，测试用例与各设计文档同步开发）。项目 2016 年 8 月启动，2017 年 2 月处于客户测试环境的系统测试阶段；前期因需求收集延误而滞后，开发阶段已追回。')
  + p('数据：系统测试用例执行统计按每 2 小时窗口记录，共 20 个工作日 × 5 个窗口 = 100 个观测。我们可算出的基本统计是：<b>均值约 82.3 个用例/2 小时，最小 72、最大 92</b>；按日平均，最低的三天是 1 月 12 日（76.6）、1 月 17 日（79.2）、1 月 31 日（79.2），最高为 2 月 2 日（84.4）。网络响应时间在 210–236 毫秒之间波动。')
  + p('团队会上给出的一堆「同样合理」的原因：测试数据难找（需复杂 SQL 才能定位可测数据）；开发团队常在 11 点才部署修复后的新包（约定是 9 点前），压缩了上午的测试窗口；测试机内存不足；访问客户测试环境有网络延迟；测试是手工的、无法复用（重测失败场景要重新录入数据），而上一项目有自动化、客户可能期待同样标准；非正式议论还包括「板球系列赛分散注意力」「主管早退时离岸成员会放松」。')
  + p('分析要点（这是案例的核心训练）：')
  + ul('均值 82.3、极差 20（约 24%）说明波动<b>存在但不大</b>；「某几天低」不足以证明「过程失控」，需要看<b>是否超出正常波动范围</b>（如控制图的上下限），而不是凭印象挑出最低的三天；',
       '网络延迟 210–236 ms 的波动幅度很小，且与测试用例执行的波动未必同步——「相关」不等于「因果」；要证明因果，需要把同一时段、同一包版本、同一测试集下的执行数与网络指标配对分析；',
       '「11 点才部署」是一条<b>可验证的机制性原因</b>：它直接减少上午可用窗口，可用「首次部署时间 vs 当日上午执行数」的散点图验证；',
       '「手工测试导致重测成本高」是<b>结构性原因</b>：它不解释日间波动，但解释整体生产率水平；两类原因要分开处理；',
       '「注意力分散」属观察性证据，不能作为管理决策的主要依据，但在 1 对 1 沟通中可作为线索。')
  + p('课件给出的质量工具正是为此准备的：因果图（鱼骨图）用于把众多原因归类（人、机、料、法、环、测）；帕累托图用于挑出贡献最大的 20%；控制图用于区分「正常波动」与「异常波动」；五个为什么用于追根因。案例要求「系统地筛选众多问题与原因，找出最佳行动」，而不是「把所有原因都改一遍」。')
  + p('测试自动化的决策必须带商业论证：自动化投入高，但能消除重测的数据录入开销、提高回归频率；对时间与材料合同，客户是否愿意为自动化付费、自动化后人力如何计费，都是必须先谈清的问题——这正是「不能没有商业论证就推荐自动化」的含义。')
  + h3('12.5 Catalise：速度、偏差与伦理')
  + p('情境：Catalise 是一家用语音分析诊断精神疾病的初创公司。其产品 Catalisence 通过分析语音模式诊断精神分裂症，被约 <b>40%</b> 的美国精神健康诊所采用，带来超过 3 亿美元风投，并吸引医院与大学合作。新任高级产品经理 Taylor 接手 Catalisten——一款通过语音诊断<b>重度抑郁障碍（MDD）</b>的 AI 产品，预计是公司未来数年最赚钱的产品；CEO 要求提前发布以抢在竞品之前。')
  + p('问题：Taylor 审查测试结果时发现，AI 把<b>女性</b>语音样本误判为 MDD 的比例为 <b>19%</b>，而男性仅 <b>2.1%</b>。假阳性诊断会导致不必要的治疗与费用，而女性本就更容易被过度诊断 MDD 并被过度处方精神药物。首席 AI 工程师 Eduardo 说，若要修正女性假阳性率，至少要多花 <b>6 周</b>，会得罪 CEO 并可能危及竞争优势，劝 Taylor「放过这个问题」。')
  + p('根因（案例给出的两个拐点）：')
  + ol('<b>数据准备阶段</b>：团队难以编出男女样本均衡的训练集——可获取的患者数据源中男性比例显著更高；又因防泄密被隔离，数据科学家无法向健康系统或研究伙伴索取更好的数据。团队首席数据科学家曾在工作流聊天中确认数据存在性别偏差，并指出样本中女性 MDD 比例高于平均，警告「若用这些数据训练，模型会更倾向过度诊断女性」；但时任临时产品负责人 Eduardo 因时间压力指示继续使用该数据集，并承诺在测试与验证阶段解决。',
       '<b>测试与验证阶段</b>：工程师确认女性假阳性率更高，随后在聊天中就是否优先 <b>precision</b> 还是 <b>recall</b> 发生激烈争论。precision 回答「模型做出预测时，这个预测有多可能正确」，= 真阳性 ÷ 全部阳性，假阳性少则高；recall 回答「模型识别真实病例的能力有多好」，= 真阳性 ÷（真阳性 + 假阴性），假阴性少则高。二者常相互张力：优先 precision → 更保守、假阳性低但漏诊多；优先 recall → 覆盖更多病例但误诊多。产品当时是<b>高 recall</b>：正确诊断了所有 MDD 病例，也把一些没有 MDD 的人诊断为 MDD。')
  + p('争论的两方立场（都要能复述）：支持高 recall 的工程师认为「确保所有需要治疗的人都得到治疗」是好事，而且对生意有利——诊所客户会看到诊断量上升，从而带来更多诊疗与处方收入；反对者指出，误诊（尤其对女性）会导致不必要用药，影响情绪稳定、社会互动甚至法律权利。Eduardo 的最终决定是维持高 recall，并写下这段话（原句）：“Let’s not draw any more attention to the 19% false-positive rate for women … Any fallout effect from the false-positive discrepancy isn’t our problem. It’s in the hands of our customers who write the prescriptions … Our job is to get this product to market as fast as we can.”（不要再让人注意女性 19% 的假阳性率……这一差异带来的任何后果不是我们的问题，而在开处方的客户手里……我们的工作就是尽快把产品推向市场。）随后写道：「不要再让人注意女性 19% 的假阳性率。假阳性差异带来的任何后果不是我们的问题，而是在开处方的客户手里——他们知道所有技术都有风险。我们的工作就是尽快把产品推向市场。」')
  + p('AI 产品开发流程（案例图 1 的六步，可作为答题骨架）：界定问题（UX 研究访谈用户，形成问题陈述）→ 收集与准备数据（选择与问题陈述匹配的数据集，注意不要被种族、性别等类别偏斜；清洗缺失与错误；标注以平衡类别分布）→ 设计模型（AI 工程师写模型代码）→ 训练模型（让模型在清洗标注后的数据上发现模式，逐步形成预测）→ 测试与验证（用更接近真实世界脏数据的数据集测试，精度下降就回到补充训练数据）→ 部署。这个流程的关键含义是：<b>偏差在第一步和第二步就被引入，之后每一步都只能缓解而不能免费消除</b>。')
  + p('伦理分析（用第 1 讲的框架）：')
  + tb(('原则', '在本案中的含义'),
       ('Public', '女性患者会被不必要地用药，涉及人身健康与法律权利，公众利益优先于上市速度'),
       ('Client and Employer', '看似「为公司好」的快速上市，实际会带来声誉与法律风险；真正的最佳利益是可持续的产品'),
       ('Product', '明知 19% vs 2.1% 的偏差仍发布，不符合「达到最高专业标准」'),
       ('Judgment', '工程师与产品经理应保持专业判断的独立，不因 CEO 压力放弃技术结论'),
       ('Profession', '若公开后被揭露「知情仍发布」，损害整个 AI 医疗产品行业的信任'))
  + p('行动方案（Taylor 可以做的，按成本从低到高）：① 用数据说话——把「19% vs 2.1%」换算成绝对人数（如每 1000 名女性使用者多出多少误诊、多少不必要的处方与费用），并附文献支持；② 提出「有条件发布」——限定适用人群（如仅用于男性或作为「辅助提示」而非诊断）、在界面标注置信度与局限、要求临床复核；③ 提出「分期修复」——先修数据重采样与阈值调整（可能只需数天），再排 6 周的完整修正；④ 升级到有权限的人（首席医疗官、合规/法务），并书面留痕；⑤ 准备「不发布」的替代方案与时间表，供决策者比较。')
  + p('案例留下的问题（也是考试可能问的）：「如果你要说服首席产品官推迟发布，你会怎么做？」好的答案不是「坚持伦理」，而是「把伦理翻译成商业语言」：误诊导致的诉讼与监管风险、被媒体揭露后的信任崩塌、以及「先修偏差再发布」其实可能只需数周而非六周。')
  + h3('12.6 跨案例的三条规律')
  + p('把四个案例放在一起，可以提炼出三条反复出现的规律，考试时用它们做「综合」最有说服力：')
  + ol('<b>变更的成本取决于它发生的位置，而不是它的金额。</b>IBM 的 4000 万美元需求之所以难，不是因为钱多，而是因为它出现在最后迭代；Sasken 的「基础功能」之所以变成变更请求，是因为它出现在离用户最远的地方；EXCEED 的投诉之所以难处理，是因为它出现在系统测试阶段。',
       '<b>过程纪律不是官僚，而是让不确定性可承受的机制。</b>IBM 用「回退整个特性 + 代码冻结」保证迭代交付质量；Sasken 用配置管理、集中缺陷库、根因分析报告维持高标准的客户信任；EXCEED 的困境恰恰是缺少自动化与可复现的测试数据，使波动无法被解释。',
       '<b>伦理不是附加项，而是需求的一部分。</b>Catalise 的偏差本质是「非功能需求（公平性、安全性）没有被写进规格」；一旦写进去，它就会像性能或可靠性一样，成为架构与测试的对象，而不是发布前的道德辩论。')
  + p('这三条也正好回扣第 1 讲的四属性、第 3 讲的变更代价、第 4 讲的非功能需求——案例课的价值就在于让你看到：这些抽象词在真实组织里长什么样。')),
 kws=K(('iterative development', '迭代开发', 'Development in iterations so evolving requirements can be accommodated.'),
       ('code freeze', '代码冻结', 'A stage where no new code may be added, protecting a stable system before release.'),
       ('back out', '整体回退', 'Removing all code for a feature that cannot be fixed within the iteration.'),
       ('value network', '价值网络', 'Closely tied operators, vendors, content and platform providers with operator-specified interfaces.'),
       ('product maturity', '产品成熟度', 'The completeness, modularity and quality a client expects as the baseline feature set.'),
       ('defect density', '缺陷密度', 'Defects per thousand lines of code; Japan 0.020 vs US 0.400 in the cited study.'),
       ('field defect', '现场缺陷', 'A problem reported from the operational site, an important reliability measure.'),
       ('root cause analysis', '根因分析', 'Reports explaining how a bug was resolved and how recurrence is prevented.'),
       ('V-process', 'V 过程', 'Test cases developed alongside requirements, high-level and detailed design.'),
       ('control chart', '控制图', 'Distinguishes normal variation from abnormal variation over time.'),
       ('pareto chart', '帕累托图', 'Ranks causes so the few contributing most can be addressed first.'),
       ('data bias', '数据偏差', 'Skewed training data leading to systematically different error rates across groups.'),
       ('precision', '精确率', 'True positives divided by all positives; higher when false positives are low.'),
       ('recall', '召回率', 'True positives divided by true positives plus false negatives.'),
       ('ethical AI', '伦理 AI', 'Developing AI products consistent with public interest, professional standards and human judgment.')),
 examples=(qa('例 1　IBM 的决策备忘录',
   p('情境：假设你是 Lalonde。请用不超过 200 字写一份给 Mayor 的决策备忘录，说明你的选择与条件。')
   + p('<b>示例：</b>「我接受该需求，但以三个条件为前提：① 只做可通过功能开关隔离的最小实现，默认关闭，避免影响既有路径；② 在最后迭代只投入两名资深开发者，其余人力继续保障发布；③ 若在测试窗口内无法修复相关缺陷，按既有规则整体回退，功能推迟到下一版本，届时由双方共同向客户说明。理由是：4000 万美元收入与客户终身价值高于末期改动的可控风险；但质量与 12 月 22 日发布承诺不可让。请 WebSphere 侧确认其功能可在同一开关下与我们同步启用。」')
   + p('<b>分析要点：</b>① 明确「接受」而非模糊表态；② 用功能开关把「末期改动」的风险隔离；③ 保留课件中已有的「回退」规则作为兜底，使决策可逆；④ 指出跨产品同步（RAD 与 WAS 同一天发布）这一组织约束；⑤ 给出「不做」时的沟通责任人。')
   + p('<b>评分点：</b>是否引用了案例的具体约束（6 周迭代、2 周测试、代码冻结、同日发布、独立业务单元），而不是只谈「质量很重要」。'))
  + qa('例 2　Sasken 的根因树',
   p('情境：客户投诉「播放器在特定运营商网络上流媒体卡顿」。请用鱼骨图的六个分支（人、机、料、法、环、测）各写一条可能原因，并指出你会优先验证哪两条。')
   + p('<b>鱼骨：</b>人——团队年轻、缺乏日本运营商网络配置经验；机——印度侧无完整目标测试平台，无法复现运营商网络条件；料——流媒体分片与码率参数来自客户规格，但规格版本可能滞后；法——缺陷仅用表格登记，缺少可复现的抓包与日志规范；环——跨国网络时延与日本本地网络差异；测——测试用例未覆盖弱网切换（Wi-Fi ↔ 移动网）。')
   + p('<b>优先验证：</b>① 「机/环」——先在客户日本测试设施上复现，确认是否只在特定网络出现；② 「测」——检查用例是否覆盖网络切换与码率自适应，因为这是流媒体卡顿最常见的触发条件。')
   + p('<b>为什么这两条：</b>它们最可能同时解释「特定运营商」与「卡顿」两个限定词；而「人年轻」虽真实，却不能解释为什么只在某网络出现——这就是「相关 vs 因果」的判断。'))
  + qa('例 3　EXCEED 的数据判断',
   p('情境：用本讲给出的统计（均值 82.3、最小 72、最大 92、日最低 76.6），判断「系统测试过程是否失控」，并写出你的论证。')
   + p('<b>论证：</b>① 全样本 100 个窗口的均值为 82.3，日间均值在 76.6–84.4 之间，极差约 10%；单窗口极差 20（72–92），约 24%。② 若把这 100 个点画成控制图，先按 ±2σ 估算正常波动范围（σ 约 5–6，则下限约 70–72），可以看到最低点 72 仍在范围内，<b>没有明显超出正常波动的证据</b>。③ 因此「过程失控」的结论<b>不成立</b>；但「整体水平是否达到客户期望」是另一个问题——这需要与合同约定的生产率基线比较，而不是与团队自己的历史比。')
   + p('<b>进一步：</b>要检验「11 点部署」这一机制性原因，应做「首次部署时间」与「当日上午（9:00 与 11:00 窗口）执行数」的配对分析；要检验网络延迟，应做「响应时间」与「执行数」的同步相关分析，并注意 210–236 ms 的波动幅度本身很小。')
   + p('<b>结论写法：</b>「数据显示波动在正常范围内，因此优先处理结构性原因（手工测试导致的整体水平偏低、部署时间不稳定），而不是把某几天的低值当作异常去追责。」这既回应了客户的「进展缓慢」，也避免了错误归因。'))
  + qa('例 4　Catalise 的说服方案',
   p('情境：你是 Taylor。请写出说服首席产品官 Darnell 推迟发布的三分钟陈述（要点式），要求包含数据、风险、方案与请求。')
   + p('<b>陈述要点：</b>')
  + ol('<b>数据</b>：女性假阳性 19%、男性 2.1%；换算为每 1000 名女性使用者约多出 170 例误诊，按现行诊疗路径意味着不必要的处方与随访成本；已有文献指出女性本就存在被过度诊断的风险，产品会放大这一偏差。',
       '<b>风险</b>：三类——患者健康（不必要用药）、法律与监管（歧视性偏差的诉讼与审查）、商业（一旦被媒体或研究者揭露，「知情仍发布」会摧毁医院合作伙伴与 3 亿美元融资所依赖的信任）。',
       '<b>方案</b>：分三档——A 立即修数据与阈值（预计 1–2 周，可显著缩小差距）；B 有条件发布（仅作辅助提示、强制临床复核、界面标注置信区间与适用人群）；C 完整修复（6 周，含重新采样与再验证）。',
       '<b>请求</b>：批准 A + B 组合，把完整修复排入下一版本；同时请首席医疗官共同签署发布标准，避免后续争议。')
  + p('<b>为什么这样组织：</b>它把伦理问题翻译成「健康—法律—商业」三重风险，并给出「不必等六周」的可行路径——这正是案例课要求的「有证据支撑的立场」，而不是道德表态。'))),
 practice=(ol('案例法三步是什么？为什么案例通常没有客观正确答案？',
         'IBM 的迭代为什么是「4 周 + 2 周」？「整体回退特性」这条规则解决了什么问题、代价是什么？',
         'Sasken 案例中，「产品成熟度」与「需求演化」如何共同推高成本？',
         'EXCEED 案例中，哪两条原因属于「机制性原因」、哪两条属于「结构性原因」？为什么这个区分重要？',
         '写出 precision 与 recall 的定义，并说明在医疗诊断场景中优先哪一个会带来什么后果。',
         '从四个案例中各取一条证据，说明「变更的成本取决于它发生的位置」。')
   + det('参考答案与思路',
    p('<b>1.</b> 阅读准备、小组讨论、全班讨论。因为案例信息故意不完整、决策涉及多方价值权衡，评价标准是「证据强度与推理质量」，不是「是否猜中主角的选择」。')
    + p('<b>2.</b> 4 周做计划、设计与实现，2 周专门测试与修缺陷，使「每个迭代交付的特性都像可发布一样完整」。整体回退解决了「带缺陷的特性污染增量」的问题，保证质量门禁；代价是浪费已完成代码、把压力推到下一迭代，并可能反复回退。')
    + p('<b>3.</b> 产品成熟度决定「客户眼中的基础功能」与「团队认知的定制项」之间的落差；需求演化使客户在开发中持续修改且期望不延期。两者叠加 → 团队压缩评审与测试 → 实现偏离原设计 → 后续修改更贵、可维护性下降。')
    + p('<b>4.</b> 机制性：11 点才部署（直接压缩上午窗口）、测试数据难找（每个用例的准备时间不同）。结构性：手工测试无法复用（整体水平低）、测试机内存与网络延迟（环境能力）。区分重要，因为机制性原因可以立即改正并验证效果，结构性原因需要投资与商业论证。')
    + p('<b>5.</b> precision = 真阳性 ÷ 全部阳性（假阳性少则高）；recall = 真阳性 ÷（真阳性 + 假阴性）。医疗诊断优先 recall → 漏诊少但误诊多（本案即此，女性 19% 假阳性）；优先 precision → 误诊少但漏诊多，可能延误治疗。取舍应结合疾病的可逆性与误诊伤害。')
    + p('<b>6.</b> IBM：需求出现在最后迭代，所以 4000 万美元的改动极难；Sasken：接口规范由运营商持续升级，变更出现在离用户最远的离岸团队；EXCEED：投诉出现在系统测试阶段，返工成本高；Catalise：偏差在数据准备阶段被引入，越晚修复代价越大（重采样 + 再训练 + 再验证）。'))),
 exam=(cal('exam', '必考', '案例法三步与「信息故意不完整」；IBM 的 6 周迭代构成、整体回退、代码冻结、三个选项；Sasken 的五类压力与缺陷率数字、codec 与 player 的对比；EXCEED 的 V 过程、机制性 vs 结构性原因；Catalise 的 19%/2.1%、precision/recall、六步 AI 流程。')
  + cal('warn', '易错 1', '把案例题答成「知识点默写」。案例题评分看「是否引用案例具体事实」与「是否权衡了替代方案」。')
  + cal('warn', '易错 2', '把 EXCEED 的「低值几天」直接当成「过程失控」。要先判断是否超出正常波动。')
  + cal('warn', '易错 3', '把 precision 与 recall 的定义写反。记法：precision 看「报出来的有多少是真的」，recall 看「真的有多少被报出来」。')
  + cal('warn', '易错 4', '在 Catalise 题中只写「应该遵守伦理」。必须给出可执行方案（修数据、限定适用人群、临床复核、升级决策）与商业论证。')
  + cal('tip', '进阶', '能用「变更的成本取决于位置」把四个案例串起来，并指出「伦理要求应写进非功能需求」——这一步把案例课升格为对整门课的综合。')),
 checklist=(h2('案例分析的清单')
  + st('读首尾两节，写出核心情境、主角目标、必须做的决策',
       '扫读图表，标出关键数字（金额、日期、比率、人数）',
       '列出「要判断这个决策还缺什么信息」，并在案例中找对应证据',
       '把决策选项列全（至少三个，含「不做」与「部分做」）',
       '为每个选项写收益、代价、风险与可逆性',
       '用课程概念命名问题（范围蔓延、技术债、non-functional requirement、偏差）',
       '检查伦理维度：受影响方、ACM/IEEE 原则、可执行的替代方案',
       '给出立场，并写明「什么新证据会让我改变立场」')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('16_Week 10/2_Case Study/data/IBM.pdf', 'p1', '案例情境、4000 万美元需求、末期插入、四个待答问题'),
   ('16_Week 10/2_Case Study/data/IBM.pdf', 'p2–p5', 'IBM 业务与战略、RAD 与 WAS 的依赖、发布节奏、开发四阶段与代码冻结、回归缺陷'),
   ('16_Week 10/2_Case Study/data/IBM.pdf', 'p5–p7', '瀑布的辩护与批评、迭代方法、6 周迭代构成、回退规则、三个选项'),
   ('16_Week 10/2_Case Study/data/IBM.pdf', 'p8–p9', '业务板块财务数据（支撑「4000 万美元」量级判断）'),
   ('Sasken.pdf', 'p1–p4', '日本移动市场与价值网络、接口规范由运营商主导、Sasken 背景'),
   ('Sasken.pdf', 'p4–p7', 'codec 与 media player 两项目对比、产品成熟度、过程纪律、需求演化'),
   ('Sasken.pdf', 'p7–p10', '质量与缺陷率、测试层级与根因分析、离岸协作与 bug sheet、文化差异、产品 vs 服务'),
   ('Sasken.pdf', 'p10–p15', '上线与后续、财务与架构附录、术语表'),
   ('16_Week 10/2_Case Study/data/EXCEED.pdf', 'p2–p4', 'V 过程、时间与材料合同、投诉分类、测试执行统计、团队会上的多种原因'),
   ('16_Week 10/2_Case Study/data/EXCEED.pdf', 'p7–p8', '用例执行数据表、网络响应时间数据（用于相关/因果分析）'),
   ('17_Week 11/2_Case Study/data/Move Fast, but without Bias - A.pdf', 'p1–p3', 'Catalise 背景、Catalisten、19% vs 2.1%、六周修复成本、NLP 与诊断'),
   ('17_Week 11/2_Case Study/data/Move Fast, but without Bias - A.pdf', 'p3–p5', 'AI 产品六步流程、数据偏差的两个拐点、precision 与 recall、Eduardo 的决定、行动问题'),
   ('（合并）', '—', 'IBM 的 6 份重复副本、Move Fast 的 2 份副本已按内容去重，此处只列一次'),
   ('（拓展）', '—', '案例阅读八步法为通用分析方法，可迁移到其他管理案例'),
   ('（跳过）', '—', '各周 Case Study 的 Moodle 说明页（讨论题与阅读指南）内容已并入 12.1，不单列'))))
# ============================================================ 13
LEC.append(L(
 slug='l13-course-project-and-report-writing',
 tzh='第 13 讲 · 课程项目与状态报告写作',
 ten='The Course Project: Requirements Specification, Status Report and Project Plan',
 keywords=['requirements specification', 'project proposal', 'status report', 'final report', 'use case table', 'requirement priority', 'rejected requirement', 'risk table', 'project plan', 'reflection', 'Harvard referencing'],
 files=['ProjectIntroduction2025.pdf', 'FinalProjectTips.pdf', '07_Week 1/2_Exercise Sessions/data/Example_project1.pdf', '20_Course Project/3_Course Project Final Report/intro/files/Project Final Report Template.docx'],
 overview=(h2('本节定位')
  + p('这一讲把整门课收束到一件具体的事：交出一份「像真的一样」的需求规格说明书 + 项目计划 + 界面设计，并在两次演示中讲清楚。它不是写作技巧课，而是把第 4 讲（需求）、第 5 讲（用例）、第 9 讲（项目计划）、第 10 讲（质量与配置）落到一份可评分的文档上。')
  + p('为什么值得认真对待：项目占 25%，且必须通过（至少 50 分）并完成两次演示。更重要的是，它训练的是工作中最常见的交付物——一份能被客户、开发、测试三方同时读懂的规格。')
  + p('学完本节你应当能够：')
  + ck('说出项目三次提交的内容、格式要求与截止时间，并据此排自己的进度',
     '按模板结构写出一份合格的需求规格说明书（含 ≥50 条需求、4 个用例、界面设计与附录）',
     '把用户故事拆成带 ID、描述与优先级的需求条目，并写出被拒绝需求及理由',
     '写出状态报告中的「变更表」（日期、动机、描述、影响）与「反思」',
     '按七段结构写项目计划，并给出可信的任务、检查点、成本与风险表',
     '用评分标准自查：需求是否合理、计划是否现实、演示是否在时限内讲清重点')),
 detail=(h3('13.1 项目是什么')
  + p('项目目的：为一个<b>移动应用</b>产出需求规格说明书。课件明确：“You do not need to program anything. Consider the requirements from different perspectives, such as the customer or the developer, and document the requirements as if the application would actually be developed.”（不需要编程；要从客户、开发者等不同视角考虑需求，并像应用真的会被开发一样把需求文档化。）')
  + p('学习目标：了解软件项目中要做什么，以及项目计划里包含哪些内容。')
  + p('组织形式：5–6 人一组，由课程预先分组；项目是必修的，值 100 分（占成绩 25%）；通过需要至少 <b>50 分</b>，并完成<b>两次演示</b>（状态演示与终期演示）。')
  + p('背景故事（写文档时的设定，很重要）：')
  + p('「你在一家叫 X Software 的公司工作。这是家有 10 人的小公司，办公室在 Lahti Science Park，专做移动应用。现在公司想开发一款新应用，可能增加收入并让公司有能力多招人。应用要在 6 个月内准备好，会有 6 人团队参与。你的工作是创建这个项目并定义新的移动应用。」')
  + p('这个设定决定了三件事：① 团队规模 6 人、周期 6 个月——所有排期与成本估算都要与之一致；② 公司小、要增加收入——商业目标必须写清楚；③ 应用是「产品」而非「某客户的定制系统」——需求来自你们对市场的判断（对应第 1 讲的 generic product）。')
  + p('如果没有想法，课件给了三个方向：旅行应用（指路、餐厅、景点、酒店）、烹饪应用（按名称或食材找食谱、收藏、上传、评论）、健康应用（饮食日记、运动记录、每日健康提示）。')
  + p('要回答的六个问题：应用如何工作？用户能用它做什么？在什么场景/何时/为何使用？需求是什么？界面长什么样？应用怎么做、项目是什么样的？→ 最终交付：<b>需求规格 + 界面设计 + 项目计划</b>。')
  + h3('13.2 三次提交与评分')
  + tb(('提交', '内容', '截止/形式', '分值'),
       ('项目提案 Project proposal', '应用想法、客户需求、团队角色；用 Moodle 模板', '9 月 25 日', '5 分'),
       ('状态报告 Status report', '项目状态、项目目标、干系人、用户群、应用描述、团队反思；用模板', '10 月 30 日；另加 5 分钟演示（10 月 31 日/11 月 1 日，替代该周练习课）', '10 分 + 演示 8 分'),
       ('终期报告 Final report', '完整需求规格 + 界面设计 + 项目计划 + 附录', '12 月 11 日；另加 7 分钟演示（12 月 12/13 日）', '需求 25 + 界面 15 + 计划 25 + 演示 12'))
  + p('评分细则（课件原文口径）：')
  + tb(('评分项', '分值', '评分要点'),
       ('需求规格', '25', '需求合理、说得通；有功能需求也有非功能需求；识别出重要干系人群体；用例清晰'),
       ('界面设计', '15', '符合需求；清晰完整；展示最重要的视图；解释了不同界面'),
       ('项目计划', '25', '清晰、全面、现实；遵循课程所教原则；与用例和需求一致'),
       ('终期演示', '12', '易懂、简明地呈现应用、遵守时限'),
       ('状态演示', '8', '同上'),
       ('项目提案', '5', '遵循模板、清楚呈现项目想法、初始用户群与干系人合理'),
       ('状态报告', '10', '遵循模板、清楚呈现项目想法、初始用户群与干系人合理'))
  + h3('13.3 终期报告的骨架')
  + p('模板的章节顺序本身就是一个检查清单：')
  + ol('Introduction（概述 + 挑战与状态）；',
       'Project Goals（目标表）；',
       'Limitations（限制表）；',
       'Stakeholders（干系人表）；',
       'User Groups（用户群表）；',
       'Requirements（需求表，≥50 条）；',
       'Use Cases（列出 4 个用例，详细描述放附录 1）；',
       'Assumptions（假设）；',
       'Team（背景与角色/贡献）；',
       'Project Plan（七段结构）；',
       'References；',
       '附录 1 用例与用例图；附录 2 界面；附录 3 被拒绝的需求；附录 4 反思。')
  + p('注意模板里的编号：正文写「Appendix 1. Use cases」「Appendix 2. User interface」「Appendix 4. Rejected requirements」「Appendix 5. Reflection」，而目录与提示里又出现 Appendix 3 界面、Appendix 4 反思——这是模板自身的小不一致。提交前统一编号即可，评分看内容不看编号。')
  + h3('13.4 需求怎么写：ID、描述、优先级')
  + p('需求表四列：ID、日期、需求（短名）、需求描述、优先级。示例项目的做法值得模仿：ID 用 01–59 连续编号；每条需求一句「The app should …」；优先级用五档——Very important、Important、Quite important、Optional（示例中还出现 Interested，属笔误，不要学）。')
  + p('写需求的四条实务规则：')
  + ul('一条需求只表达一件事——「用户应能登录，并能用邮箱或手机号注册」应拆成两条；',
       '用「The app should …」句式，避免「可能」「尽量」「友好」这类不可验证的词；',
       '把非功能需求也编号（示例项目第 17–22 条就是性能、可靠性、安全、可用性、可扩展性、容量）；',
       '每条需求都能对应到某个用例或界面，否则它可能是「愿望」而不是需求。')
  + p('示例项目的非功能需求写法可以直接借鉴：「The application should have an average loading duration under 3 seconds for its functionality.」（性能）「The application should have an uptime of 99.5%.」（可靠性）「The application should be able to handle 1000 requests per second.」（容量）——它们都有度量。')
  + h3('13.5 被拒绝的需求：附录里最容易被忽略的加分项')
  + p('模板要求单列「被拒绝的需求」表：ID、拒绝日期、需求、理由。示例项目给了五个很好的例子：')
  + tb(('被拒需求', '理由', '可取之处'),
       ('地图应有明显指南针', '我们不需要这个需求', '直接说明范围外'),
       ('用户应能查看区域实时信息（交通、温度）', '需求含糊（ambiguous）', '点出「不可验证」这一根本问题'),
       ('平均加载时间低于 1 秒', '实现成本超出预算', '用可行性（realism）拒绝，符合五维检查'),
       ('用户应能在应用内订酒店', '功能过于复杂，用户可通过应用跳转酒店网站完成', '给出替代方案，而非简单说「不做」'),
       ('付费会员可享更多服务', '应用没有那么多额外服务', '说明与产品定位不符'))
  + p('为什么这张表重要：它证明你们做过<b>范围管理</b>（第 4 讲的 prioritisation and negotiation）与<b>可行性判断</b>（realism）。评审看这份文档时，最想知道的是「你们知不知道自己不做什么、为什么」。')
  + p('写理由的三个层次（从差到好）：「我们不想做」→「超出预算/工期」→「该需求与产品定位冲突，或不可验证，且已有替代路径（用户在浏览器完成）」。')
  + h3('13.6 用例与用例图')
  + p('要求：至少 <b>4 个用例</b>（“You should have at least 4 use cases. Do not describe trivial use cases.”），不要描述琐碎用例；要画一张包含所有用例的用例图。用例表的字段（第 4 讲已给）：ID、名称与版本、参与者、前置条件、描述、异常、结果、其他需求。')
  + p('示例项目的四个用例（可作为写法参照）：登录或注册（UC-1）、浏览地图（UC-6）、阅读反馈（UC-8）、切换语言与时区（UC-26）。它们的共同点是：都有明确的前置条件（如「用户已登录」「手机已开启定位并授予权限」）、都有异常分支（如「邮箱已被记录则提示创建失败」）、都有可判定的结果（如「新用户创建成功」）。')
  + p('常见失分点：用例写成功能列表（无参与者、无异常、无结果）；前置条件写成「用户打开应用」（这不是前置条件，是描述的一部分）；异常写成「系统出错」（不可判定）。')
  + p('用例图要点（第 5 讲）：参与者画在系统边界之外；用例用椭圆；参与者与用例之间用连线；不要把「先登录再下单」的顺序画进用例图——顺序用顺序图或文字描述。')
  + h3('13.7 界面设计')
  + p('要求：<b>5 个不同设计</b>（展示应用的不同视图，如主视图、个人资料、登录）；说明每个设计展示什么、各按钮与图标的作用；必须<b>符合需求</b>；可用 Miro 的 App wireframe 模板、Figma 或任何设计工具；终期报告里放截图并逐图解释。')
  + p('评分逻辑：界面不是「好看」加分，而是「与需求一致」加分。做法：给每个界面标注它实现了哪几条需求 ID；如果某条界面元素没有对应需求，要么补需求，要么删元素。')
  + h3('13.8 项目计划：七段结构')
  + p('模板要求先做一次选择：<b>瀑布还是敏捷</b>，然后按所选模型填写。七段内容：')
  + tb(('段落', '要写什么', '常见错误'),
       ('Background', '公司现状、为什么启动这个项目', '写成产品介绍，不写组织动因'),
       ('Project Goal', '终点目标与子目标（可量化）', '只写「做一个 App」，无成功判据'),
       ('Tasks', '要做哪些任务、与目标的关系', '任务与需求不对应'),
       ('Schedule & Checkpoints', '进度表 + 检查点 + 每个检查点评审什么', '检查点只有日期，没有「评审什么」'),
       ('Costs', '总成本与成本构成（人力、工具、分发）', '只写一个总数，无构成与依据'),
       ('Risk Analysis', '5–10 个风险：风险、概率、严重性、原因、预防', '只写风险名，无原因与预防'),
       ('Quality / Change Management / Organization', '质量如何保证与测试；变更如何管理（含版本控制）；项目组与项目板成员及角色', '质量写成「会认真测试」；变更写成「按需修改」'))
  + p('示例项目的计划可以作为「合格线」的参照：')
  + ul('<b>任务与检查点</b>：T00 准备开始（2023-01-02）→ T01 项目启动（工作站与工具就绪，检查点「所有工作站具备所需工具并符合公司标准」）→ T02 城市文字指南（依赖 T01）→ T03 数据库结构（后续地图功能的前置）→ T04 基础地图（检查点：地图框架完成后，其他地图特性可并行）→ T05 路线（依赖 T04）→ T06 搜索与过滤（依赖 T04）→ T07 用户资料（依赖 T03）→ T08 位置信息（依赖 T03）→ T09 实时流与通知（依赖 T08，检查点：用户收到适量且相关的通知）→ T10 本地化（前置：所有文本菜单完成）→ T11 终测（前置：所有任务完成；检查点：无重大缺陷）→ T12 上架（前置：终测完成）。',
       '<b>成本</b>：6 名全职（1 名资深工程师 + 5 名开发者）；工资按芬兰平均水平估算：资深 6 个月 €29 376，5 名开发者共 €104 558，合计 €133 934；工作站 6 × €1 000 = €6 000，开发工具 6 × €500 = €3 000，Apple 开发者计划 €94，Google Play 注册 €25；工具合计 €9 119；<b>总计 €143 053</b>。',
       '<b>风险表</b>（示例给了五个，每个都有概率、严重性、原因、预防）：人员变动（较可能/显著；预防：早期团队建设 + 有吸引力的福利）；不达截止日（可能/可控；预防：遵守冲刺计划 + 明确可选需求清单以便裁剪）；额外成本（不太可能/不严重；预防：不过度排期、任务均衡）；性能问题（中等/显著；预防：用测试确保新特性不显著降低性能）；商家兴趣低（中等/严重；预防：与商家干系人频繁沟通，确保其期望的功能被纳入）。',
       '<b>质量与变更</b>：质量由「每人负责特定需求类别」+ 自动化测试（回归 + 监控构建间性能变化）保证；变更管理依靠「高度模块化 + 可选需求可裁剪」，并设专人做市场调研以确保最有市场的特性被纳入。',
       '<b>组织</b>：6 人，其中 3 人组成项目板（资深工程师兼项目经理、项目秘书、市场与需求分析师），另有 UI 设计师、全栈开发者、后端开发者。')
  + p('这套写法的高明之处在于「一致性」：6 人团队、6 个月、€143 053、12 个任务、5 个风险，全部互相对得上；项目板 3 人正好对应「规划与优先级」的职责。评分标准里的「is clear, comprehensive and realistic」说的就是这个。')
  + h3('13.9 状态报告与反思')
  + p('状态报告的模板结构与终期报告类似，但多了两块：<b>Project Status</b>（第一次迭代的计划是什么、团队完成了什么、自提案以来的重大变更）与 <b>Appendix 1 Reflection</b>（什么顺利、什么不顺、未达目标的原因、如何克服、下一迭代要改什么）。')
  + p('变更表必须有四列：变更、日期、动机、变更描述、影响（implications）。示例（Ventura 组的做法）值得学：')
  + tb(('变更', '日期', '动机', '描述', '影响'),
       ('投资额筛选 Investment Ask Filter', '2026-10-22', '提供更个性化的用户体验', '让投资人按愿意投资的金额筛选机会，而不必看完整个 pitch', '下一迭代需为筛选器投入更多时间'),
       ('分享功能 Share Feature', '2026-11-01', '提供更有用的功能', '允许投资人把 pitch 分享给其他投资人', '需在第二迭代实现，因为该功能属于「Feed」标签页，而 Feed 大部分在第一迭代完成'))
  + p('反思怎么写才算好：具体、可归因、前后一致。课程反馈里点名批评过一份状态报告：「Appendix 1 的回答很泛，而且自相矛盾——第一问说『我们团队合作很好、彼此沟通』，第三问却把未达目标归因于『沟通不畅』。」这是最典型的失分方式。')
  + p('好的反思长什么样（结构）：① 顺利的事 + 具体做法（「每日 15 分钟站会 + 共享任务板，使阻塞当天暴露」）；② 不顺的事 + 具体机制（「需求在第二周才基线化，导致界面设计与数据模型返工」）；③ 未达目标的原因（用数据或事件，不用「沟通不畅」这类结论）；④ 下一迭代的两个具体改动（可验证）。')
  + h3('13.10 从反馈中学到的六条')
  + p('课程给出的状态报告反馈（原文摘录与转述）几乎覆盖了所有常见问题，值得逐条对照：')
  + ol('<b>与竞品比较不足</b>（0.5/1）：只描述自己的应用，没有说明「相比现有方案，为什么用户会换」。',
       '<b>干系人与用户群被混用</b>（0.5/1）：同一批人被同时写进两张表，且描述重复。干系人是「受影响的个人或组织」（含投资人、监管、平台方），用户群是「会使用应用的人群」（按需求与场景划分）。',
       '<b>反思泛化且自相矛盾</b>（0.75/1.5）：见 13.9。',
       '<b>目标表的日期应是未来的目标截止日</b>，而不是报告提交日（反馈明确指出「14.11.2026 是提交日，不是目标日」）。',
       '<b>引用不足</b>：终期报告要增加参考文献，并按哈佛格式（LUT 要求学术引用，in-text citation 作者 + 年份，文末 References 列表）。',
       '<b>校对与封面</b>：报告要通读校对、填好标题页；演示要提前练习并预约时段。')
  + p('正面反馈也值得注意：「应用描述及其定位非常出色，而且是一个真实的原型！」——这说明「把应用讲清楚、有可点的原型」比堆砌需求更能打动评审。')
  + h3('13.11 两次演示')
  + p('状态演示（5 分钟）：介绍团队、应用概览、干系人、用户群。终期演示（7 分钟）：简短说明应用是什么、用户能做什么；展示界面设计并简要解释应用如何工作；<b>没有时间讲每个细节，抓重点</b>；提前练习。')
  + p('演示的评分点是「易懂、简明、守时」，不是「信息密度」。7 分钟的结构建议：1 分钟问题与用户；2 分钟核心流程（用界面串起来）；1.5 分钟项目计划要点（团队、进度、风险）；1 分钟质量与测试；1 分钟收获与下一步；30 秒缓冲。')
  + h3('13.12 提交前的自查清单')
  + p('把评分标准翻译成可勾选的动作，比反复读模板有效得多。以下几项是「一定会被检查」的：需求 ≥ 50 条且功能与非功能都有；干系人 5–10 个、用户群 5–10 个且互不重复；4 个用例都有前置条件、异常与结果，并配用例图；5 个界面且每个都对应需求；项目计划七段齐全且数字自洽；被拒需求有理由；反思具体不矛盾；参考文献按哈佛格式；标题页与目录完整。')),
 kws=K(('requirements specification', '需求规格说明书', 'The official statement of what is required of the system developers; WHAT, not HOW.'),
       ('project proposal', '项目提案', 'Application idea, customer needs and team roles; first submission.'),
       ('status report', '状态报告', 'Project status, goals, stakeholders, user groups, application description and reflection.'),
       ('use case table', '用例表', 'ID, name and version, actors, preconditions, description, exceptions, result, other requirements.'),
       ('requirement priority', '需求优先级', 'Very important, important, quite important, optional.'),
       ('rejected requirement', '被拒绝的需求', 'A requirement deliberately excluded, with a stated reason.'),
       ('risk table', '风险表', 'Risk, probability, severity, reasons, prevention.'),
       ('project plan', '项目计划', 'Background, goal, tasks, schedule, checkpoints, costs, risks, quality, change, organisation.'),
       ('reflection', '反思', 'What went well, what did not, causes and next-iteration changes.'),
       ('Harvard referencing', '哈佛引用格式', 'In-text author–year citations plus a reference list.'),
       ('checkpoint', '检查点', 'A scheduled review that states what is reviewed, not just a date.'),
       ('assumption', '假设', 'Hardware or user-expertise assumptions behind requirements and use cases.')),
 examples=(qa('例 1　把用户故事拆成需求条目',
   p('情境：用户故事「作为一个经常出差的人，我想在到陌生城市前保存一份两天的行程，这样我下飞机就能直接按计划走」。请拆成 4 条需求（含 1 条非功能），并给优先级。')
   + p('<b>解：</b>')
  + tb(('ID', '需求', '描述', '优先级'),
       ('R01', '创建行程', '用户应能创建一份带名称与起止日期的行程。', 'Very important'),
       ('R02', '添加地点', '用户应能把地点（景点、餐厅、酒店）加入某一天的行程。', 'Very important'),
       ('R03', '离线查看', '用户应能在无网络时查看已保存行程的地点名称、地址与备注。', 'Important'),
       ('R04', '同步时延', '行程在联网后 30 秒内完成同步，冲突时以最后一次修改为准并提示用户。', 'Quite important'))
  + p('<b>分析：</b>原故事包含三个可分离的能力（创建、添加、离线查看）与一个隐含的非功能要求（同步）。拆分的判据是「能否独立验收」：R01 与 R02 可以分别演示；R03 需要断网测试；R04 需要构造冲突场景。')
  + p('<b>注意：</b>不要把「保存行程」写成一条巨型需求——它无法在一个冲刺内验收，也无法定位缺陷。'))
  + qa('例 2　写一张风险表（5 条）',
   p('情境：你的项目是「校园二手书交易 App」，6 人、6 个月、预算约 €140 000。请写出 5 条风险并给概率、严重性、原因、预防。')
   + p('<b>示例：</b>')
  + tb(('风险', '概率', '严重性', '原因', '预防'),
       ('用户增长不及预期，交易冷启动失败', '高', '严重', '双边市场，先有书还是先有人', '先在一个学院试点，用班级群导流；把「求购」做成可发布需求'),
       ('支付/物流对接延期', '中', '显著', '第三方审批周期不可控', '第 1 个月就发起申请；先做「线下自提」兜底'),
       ('核心成员期末周不可用', '高', '可控', '学期节奏与项目周期重叠', '排期避开考试周；关键模块双人熟悉'),
       ('书籍信息录入质量差', '中', '显著', '用户不愿填 ISBN', '支持扫码录入；缺 ISBN 时用「书名 + 封面照」'),
       ('隐私与合规（学生个人信息）', '低', '严重', '涉及个人信息收集', '最小化收集；上线前做一次合规自查并写入质量计划'))
  + p('<b>要点：</b>每条都要有「原因」，否则概率无法评估；「预防」要能落到具体动作与时间点，而不是「注意风险」。'))
  + qa('例 3　写一条状态报告的变更行',
   p('情境：项目第 6 周，团队决定把「书籍推荐」从第一版移除，改为「按课程代码筛选」。请写出变更表的四个字段，并说明它如何影响计划。')
   + p('<b>变更行：</b>变更 = 用「课程代码筛选」替换「书籍推荐」；日期 = 第 6 周（具体日期）；动机 = 推荐算法需要大量交易数据，而冷启动阶段数据不足，推荐质量无法保证；筛选功能直接对应「找同门教材」这一高频场景，且实现成本低。描述 = 在搜索结果页增加课程代码下拉筛选，移除推荐位。影响 = 需求表删除 2 条推荐相关需求、新增 1 条筛选需求；界面设计第 3 屏调整；第三迭代的任务从「推荐服务」改为「筛选索引」，工期减少约 4 人日，可用于补测试；风险表新增「课程代码数据来源不稳定」，预防为「提供手工录入兜底」。')
  + p('<b>为什么这样写：</b>变更行不只是「记录改了什么」，而是要让读者看出「为什么改、改到哪里、对计划的影响」。这正是模板要求 date / motivation / description / implications 四个字段的原因。'))
  + qa('例 4　用评分标准自查',
   p('情境：你的终期报告已完成。请按 100 分结构做一次自查，列出最可能丢分的三项与补救动作。')
   + p('<b>自查（按分值权重）：</b>')
  + tb(('评分项', '自查问题', '若答「否」的补救'),
       ('需求 25', '有 ≥50 条？功能与非功能都有？每条可验收？', '补非功能需求（性能、可靠性、安全、容量各一条）；把「友好」「快速」改成度量'),
       ('界面 15', '5 个界面？每个都标了对应需求 ID？解释了按钮/图标？', '补第 5 屏；给每个界面加「实现 Rxx」标注'),
       ('计划 25', '七段齐全？任务与需求对得上？成本有构成？风险有原因与预防？', '补成本明细；给每个检查点写「评审什么」'),
       ('演示 12+8', '7 分钟内讲完？练过 3 次？', '删细节，只留问题—流程—计划—质量'),
       ('提案/状态 15', '遵循模板？目标日期是未来？反思具体？', '把目标日期改成真实目标；重写反思'),
       ('其他', '哈佛引用？封面？目录页码？', '补参考文献与标题页'))
  + p('<b>结论：</b>最常丢分的是「需求不可验收」「界面与需求脱节」「计划数字不自洽」。这三项都能在提交前两小时内修好，收益远大于再写一个新功能。'))),
 practice=(ol('项目的三次提交分别是什么？各占多少分？通过项目的两个硬性条件是什么？',
         '「干系人」与「用户群」的区别是什么？各举三个例子（用你自己的项目）。',
         '版本控制中的「变更表」四列是什么？为什么「影响」这一列不能省？',
         '写出项目计划的七个段落，并为「检查点」写一句合格的定义。',
         '一条需求写成「应用应易于使用」，问题在哪？请改写为可验收的需求。',
         '状态报告的反思部分，怎样写才算「具体、可归因、前后一致」？给一个反例与一个正例。')
   + det('参考答案与思路',
    p('<b>1.</b> 提案（5 分，9/25）、状态报告 + 5 分钟演示（10 + 8 分，10/30 与 10/31–11/1）、终期报告 + 7 分钟演示（需求 25 + 界面 15 + 计划 25 + 演示 12，12/11 与 12/12–13）。硬性条件：总分 ≥ 50，且完成两次演示。')
    + p('<b>2.</b> 干系人是受系统影响、有正当利益的个人或组织：投资人、学校 IT 部门、支付平台、监管机构；用户群是会使用应用的人群：本校学生、教职工、校外买家。前者关注项目成败与合规，后者关注功能与体验。')
    + p('<b>3.</b> 变更、日期、动机、描述、影响。「影响」回答「这次变更牵动哪些需求、界面、任务、工期与风险」，没有它，变更记录就只是日志，读者无法据此调整计划。')
    + p('<b>4.</b> 背景、项目目标、任务、进度、检查点、成本、风险分析、质量管理、变更管理、项目组织（模板把后四项放在计划内）。检查点 = 「在某个日期，由谁评审哪些产物、依据什么标准判定通过」。')
    + p('<b>5.</b> 问题：不可验证（没有度量、没有条件、没有阈值）。改写：「新用户在无培训条件下，5 分钟内完成首次发布书籍，成功率 ≥ 90%（可用性测试 n ≥ 20）」。')
    + p('<b>6.</b> 反例：「我们团队合作很好，沟通顺畅……未达目标的主要原因是沟通不畅。」正例：「第一迭代我们做了每日 15 分钟站会与共享任务板，阻塞平均当天暴露，因此 R01–R06 按期完成；但需求在第 2 周才基线化，导致界面第 3 屏与数据模型返工约 3 人日，使 R12 延至第二迭代。下一迭代我们会在冲刺计划前完成需求评审并冻结范围。」'))),
 exam=(cal('exam', '必考', '三次提交的内容与分值、评分七项、需求表四列与优先级、用例表八字段、项目计划七段、风险表五列、被拒需求表、反思的写法。')
  + cal('warn', '易错 1', '把干系人与用户群写成同一批人。两张表必须有实质差异。')
  + cal('warn', '易错 2', '目标表的日期写成报告提交日。应是未来的目标截止日。')
  + cal('warn', '易错 3', '需求只写功能、不写非功能。评分明确要求两者都有。')
  + cal('warn', '易错 4', '检查点只写日期。必须写「评审什么、依据什么标准」。')
  + cal('tip', '进阶', '能用「需求 ID ↔ 界面 ↔ 用例 ↔ 任务 ↔ 测试」的追溯链把整份报告串起来，是本项目最高效的加分方式：评审一眼就能看出文档是「设计出来的」而不是「拼出来的」。')),
 checklist=(h2('提交前的自查清单')
  + st('需求 ≥ 50 条，功能与非功能都有，每条可验收',
       '干系人 5–10 个、用户群 5–10 个，两张表不重复',
       '4 个用例齐全（前置、异常、结果），并配一张用例图',
       '5 个界面，每个标注实现的需求 ID 与按钮/图标说明',
       '项目计划七段齐全；任务、进度、检查点、成本、风险互相自洽',
       '风险 5–10 条，每条有概率、严重性、原因、预防',
       '被拒需求有理由（不可验证/超预算/与定位冲突/有替代路径）',
       '变更表四列齐全，影响写到需求、界面、任务与风险',
       '反思具体、可归因、不矛盾；下一迭代改动 ≤ 2 项且可验证',
       '哈佛引用、封面、目录、页码、拼写检查',
       '演示计时练 3 次，7 分钟内讲完')),
 mapping=tb(('源文件', '页码', '覆盖知识点'),
   ('ProjectIntroduction2025.pdf', 'p2–p8', '项目目的、学习目标、分组与分值、三次检查点、背景故事、应用方向、要回答的六个问题'),
   ('ProjectIntroduction2025.pdf', 'p9–p15', '需求规格与 50 条要求、界面设计 5 屏、项目计划要点、两次演示的内容、评分细则 100 分'),
   ('FinalProjectTips.pdf', 'p3–p6', '终期报告三份文档的具体要求、用例与图、被拒需求、反思、界面工具（Miro/Figma）'),
   ('FinalProjectTips.pdf', 'p7–p11', '哈佛引用格式、in-text citation 与参考列表、终期演示要求、校对与预约'),
   ('07_Week 1/2_Exercise Sessions/data/Example_project1.pdf', 'p1–p7', '示例项目结构：应用描述、商业目标表、限制表、干系人表、用户群表、用例表、假设'),
   ('07_Week 1/2_Exercise Sessions/data/Example_project1.pdf', 'p8–p12', '项目计划：背景、目标、12 个任务与检查点、成本明细（€143 053）、风险表、质量与变更管理、组织与项目板'),
   ('07_Week 1/2_Exercise Sessions/data/Example_project1.pdf', 'p14–p19', '59 条需求（含非功能）、用例与用例图、界面、被拒需求表、贡献分工'),
   ('20_Course Project（模板三份与 Ventura 提案/状态报告）', '全篇', '模板章节顺序、需求/目标/干系人/用户群/风险表列结构、变更表四列、反思问题清单、反馈中的六类问题'),
   ('（合并）', '—', '三份模板的重复副本（提案模板 3 份、状态模板 2 份）已按内容去重'),
   ('（拓展）', '—', '模板附录编号在 1–5 与 1–4 之间存在不一致，提交前统一编号即可'),
   ('（跳过）', '—', 'Online text 与 Feedback comments 的提交页框架；反馈内容已提炼进 13.10'))))

emit('30361', 7, 'CT60A4050 软件工程基础', 'Software Engineering Fundamentals', 'CT60A4050 软件工程基础',
     '以 Sommerville 第 10 版为骨架的英文授课软件工程入门：从软件与工程的定义、SDLC 与敏捷（瀑布、螺旋、V、RAD、XP、Scrum）、过程活动与过程改进，到需求工程、UML 建模、体系结构设计、测试与质量管理、演化与遗留系统、项目管理与估算、质量与配置管理；并以 Telerik、Pearson、IBM、Sasken、EXCEED、Catalise 六个真实案例训练判断，最终落到课程项目（需求规格、界面设计、项目计划与两次演示）。',
     LEC)
