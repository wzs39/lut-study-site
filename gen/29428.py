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

LEC = []

ov = "".join(
    [
        h2("本讲定位"),
        p(
            "LUT Digital Orientation（数字导览）没有课件文本，它本身就是一组图：一张 eLUT 首页、一张“六个主题”的导航图、一张“四个最重要的系统”、一张辅导主题周、一张学生生活拼图、一张学习能力模型、一张聊天机器人界面，以及一份“Speaking up”指引。本讲把这些图里的服务名称、顺序与流程逐个拆开，变成你第一周就能照着做的动作。"
        ),
        p(
            "它与 CT10A9900、CT30A1000 的关系是“同一套系统的另一视角”：导览告诉你<b>有哪些东西、按什么顺序接触</b>；那两门课告诉你<b>每个系统具体怎么用、作业怎么交</b>。三讲合起来，才是一张完整的入学地图。"
        ),
        p("学完本讲你应当能够："),
        ck(
            "说出 Sisu、Moodle、Time-Edit、Tuudo 四个系统各自解决什么问题",
            "按辅导主题周的八个主题安排入学前两个月的关注点",
            "用学习能力模型的四块定位“我卡在哪一环”",
            "按 Neo 的四条使用规则提问，并对回答做核实",
            "遇到不当言行时，按 Speaking up 的步骤处理并留下记录",
        ),
    ]
)

de = "".join(
    [
        h2("一、导览的入口：eLUT 首页"),
        p(
            "eLUT 首页的结构在图中很清楚：左侧是 LUT University 标识；顶部四个菜单项依次是 <b>SEARCH</b>、<b>LANGUAGE MENU</b>、<b>QUICK LINKS</b>、<b>MAIN MENU</b>；页面中部是一张校园照片与一块黑色说明区，标题是 <b>“Welcome to eLUT!”</b>。"
        ),
        p(
            "说明区的文字给出三件事：eLUT 是 LUT 学生的信息页（info page for LUT students），在这里可以找到面向全体学生的最重要新闻与活动（the most important news and events for all students）；可以订阅学生支持与指导服务的通讯（subscribe to support and guidance service newsletter for students），图中还加了一句 “Don’t miss this info.”；站内有一个聊天机器人服务，但要查看对话，<b>Neo bot 需要你同意分析（Analytics consent）</b>。"
        ),
        p(
            "页面底部有一个搜索框（Search）与放大镜图标。结合顶部菜单，可以看出一套典型的三层入口：<b>搜索</b>用于已知关键词的精确查找，<b>快捷链接</b>用于每天都要点的常用服务，<b>主菜单</b>用于浏览全部服务与说明。"
        ),
        cal(
            "tip",
            "先订阅，再搜索",
            "导览把“订阅通讯”放在首页说明区，说明它承载的是“会变的信息”（截止日期、活动、服务时间）。先把通讯订阅上，再用搜索查具体规则，两条腿走路才不漏消息。",
        ),
        h2("二、六个主题：导览的目录结构"),
        p(
            "另一张图用六块并列的卡片给出导览的六个主题，顺序是：<b>Information channels</b>（信息渠道）、<b>Planning &amp; completing studies</b>（规划与完成学业）、<b>Study ability &amp; support</b>（学习能力与支持）、<b>Campuses</b>（校区）、<b>Student life</b>（学生生活）、<b>Equality &amp; Ethics</b>（平等与伦理）。"
        ),
        p(
            "这个顺序不是随意的：先解决“消息从哪来”，再解决“学业怎么排”，然后才是“人撑不撑得住”“在哪个校区”“生活怎么过”，最后是“遇到不当对待怎么办”。它其实是一条从“事务”到“人”的路径。"
        ),
        tb(
            ("顺序", "主题（图中原文）", "本讲对应内容"),
            ("1", "Information channels", "第一节 eLUT 与首页菜单、第七节 Neo 机器人"),
            (
                "2",
                "Planning &amp; completing studies",
                "第三节 Sisu 与 Time-Edit、第四节辅导主题周",
            ),
            ("3", "Study ability &amp; support", "第六节学习能力模型"),
            ("4", "Campuses", "第三节校区与通勤相关信息（导览中以主题出现）"),
            ("5", "Student life", "第五节学生生活"),
            ("6", "Equality &amp; Ethics", "第八节 Speaking up 指引"),
        ),
        cal(
            "warn",
            "不要跳过第 6 块",
            "很多新生只看“怎么选课、去哪上课”，把 Equality &amp; Ethics 留到最后。但这一块给的是“遇到问题时怎么做”的具体话术与流程，真遇到事时再找已经来不及。",
        ),
        h2("三、四个最重要的系统"),
        p(
            "导览用一张四象限图给出“学生最重要的系统与工具”，中心写着 <b>“Most important systems and tools for students”</b>，四个角分别是四个系统，每个系统下面一行说明它管什么。"
        ),
        tb(
            ("系统", "图中说明", "它解决的问题", "什么时候打开"),
            (
                "Sisu",
                "Student information system（学生信息系统）",
                "学习计划、选课与报名、学分与成绩记录",
                "做 PSP、选课、报名考试、查学分",
            ),
            (
                "Moodle",
                "Online learning platform（在线学习平台）",
                "课程材料、作业提交、测验与讨论",
                "每次上课前后、交作业、看反馈",
            ),
            (
                "Time-Edit",
                "Schedules（课表）",
                "课程时间、教室、考试安排",
                "每天出门前、课表变动时",
            ),
            (
                "Tuudo",
                "Makes your daily study life easier（让日常学习生活更轻松）",
                "日常学习生活的随身入口（图中只给这一句定位）",
                "日常查日程、找服务、跑校区",
            ),
        ),
        p(
            "四者的关系可以用一句话记住：<b>Sisu 管“我的学业状态”，Moodle 管“课程内容”，Time-Edit 管“什么时候在哪”，Tuudo 管“每天怎么过”。</b>它们不是互相替代的四个 App，而是一条链上的四段。"
        ),
        cal(
            "warn",
            "图里没有说的，不要替它说",
            "导览对 Tuudo 只给了“makes your daily study life easier”这一句定位，没有列出具体功能。本讲因此只把它放在“日常入口”的位置，不虚构它有哪些按钮或服务。需要具体功能时，以 Tuudo 应用内的说明为准。",
        ),
        h3("3.1 一条日常链：从起床到交作业"),
        st(
            "早上先看 Time-Edit：今天几点、哪间教室、有没有考试",
            "打开 Moodle：这门课本周要读什么、要交什么",
            "需要改计划或报名时进 Sisu：选课、考试报名、看学分",
            "日常琐事（日程、校区服务）用 Tuudo 处理",
            "晚上回到 Moodle 提交，并在 Sisu 确认报名状态",
        ),
        p(
            "这条链的关键是“不跳步”：先看时间地点，再看内容，最后才动学业记录。顺序颠倒的典型后果是“在 Moodle 里找到了作业，却不知道今天在哪上课”。"
        ),
        h2("四、辅导主题周：八周的接触顺序"),
        p(
            "导览用一张“路标”图给出辅导（tutoring）的主题周，左侧竖排写着 <b>TUTORING THEME / WEEKS</b>，右侧八个箭头从上到下依次是：<b>Orientation</b>、<b>Student’s wellbeing</b>、<b>Living in Finland</b>、<b>Activities and hobbies</b>、<b>Healthcare and safety</b>、<b>Career Services and employment in Finland</b>、<b>Exam rules, academic misconduct, and study tips</b>、<b>Fun things to do with the group</b>。图的右上角同时有 LUT University 与 LAB University of Applied Sciences 两个标识。"
        ),
        p(
            "这八个主题的顺序本身就是一份“入学适应时间表”：先 orientation（把系统与规则讲清），再 wellbeing（人先稳住），然后才是生活与娱乐、医疗与安全、就业、考试规则，最后以“和小组一起做点好玩的事”收尾。"
        ),
        tb(
            ("周次（按图中顺序）", "主题", "这一周要拿到的东西"),
            ("1", "Orientation", "系统账号、课表、课程页、辅导小组联系方式"),
            ("2", "Student’s wellbeing", "校内支持服务的位置与预约方式"),
            ("3", "Living in Finland", "住宿、交通、日常生活的基本规则"),
            ("4", "Activities and hobbies", "一个可长期参加的社团或活动"),
            ("5", "Healthcare and safety", "学生健康服务与紧急情况下的求助路径"),
            (
                "6",
                "Career Services and employment in Finland",
                "就业服务入口、实习与求职的基本信息",
            ),
            (
                "7",
                "Exam rules, academic misconduct, and study tips",
                "考试规则、学术不端界限、学习技巧",
            ),
            ("8", "Fun things to do with the group", "与辅导小组的一次共同活动"),
        ),
        p(
            "注意两点：第一，图里用的是“主题周”，不是“课程周”，所以它更像辅导活动的节奏，具体日期以辅导小组的通知为准；第二，LUT 与 LAB 两个标识同时出现，说明这套主题周是两校共同的辅导安排，遇到跨校活动不必惊讶。"
        ),
        h2("五、学生生活：三类画面"),
        p(
            "学生生活那张拼图配了三句文案：<b>“Student life is about events and fun time,”</b>、<b>“outdoor activities and hangouts,”</b>、<b>“and studying together with friends, of course!”</b> 三句对应三类画面。"
        ),
        ul(
            "活动与欢乐时光：户外集市式的聚会、水边活动、草地上的集体游戏、露天演出；",
            "户外活动与聚会：滑雪、林间骑行、湖边日落、草地上的人群；",
            "与朋友一起学习：室内小组讨论、共享桌上的笔记与电脑、休息区里各自看书。",
        ),
        p(
            "图片右下角标注了摄影者：<b>© Teemu Leinonen, Linnea Varamaki, Meermaria Ketokulta</b>。这句话本身也是一个提醒：校园活动的照片有版权，做社团宣传或课程展示时，转载要注明来源。"
        ),
        p(
            "把这张图与辅导主题周对照，会发现它们讲的是同一件事的两面：主题周给你“什么时候该去找什么”，学生生活图告诉你“找的东西长什么样”。两者都指向一个结论——<b>入学适应不是把课修完，而是把人和关系建立起来</b>。"
        ),
        h2("六、学习能力：四块互相作用"),
        p(
            "导览给出一张模型图，顶部一句总纲：<b>“The ability to study forms and evolves in a dynamic interaction between the student and the study environment.”</b> 中间是 <b>ABILITY TO STUDY</b>，四周是四个板块，板块之间用双向箭头连接，说明它们互相影响。"
        ),
        tb(
            ("板块", "图中列出的条目"),
            (
                "Personal resources（个人资源）",
                "Health and health-related behaviour；Socioemotional skills；Cognitive skills；Social relationships；Identity development；Life situation and conditions",
            ),
            (
                "Study skills（学习技能）",
                "Prior knowledge；Study motivation；Study-related emotions；Planning, time management and achievement；Study technique；Interaction skills",
            ),
            (
                "Study environment（学习环境）",
                "Physical study environment；Digital study environment；Psychosocial study environment；Cultural study environment；Pedagogic environment",
            ),
            (
                "Teaching and counselling（教学与辅导）",
                "Student-oriented approach；Constructively aligned teaching；Assessment and feedback；Achievability；Student-oriented guidance；Commitment and involvement",
            ),
        ),
        p(
            "图里还画了几个小场景，正好对应四块：左侧一个人牵着狗、抱着书，旁边有植物（个人资源）；右上两个人一起看书，旁边有钟表与“I was able to read on time.”“Remember the exam!”（学习技能）；下方一群人围在一起（学习环境）；右下一位教师在与学生交谈（教学与辅导）。"
        ),
        cal(
            "tip",
            "用它做诊断，不做评判",
            "当你说“我学不进去”，先问是哪一块：睡不好是个人资源；不会拆任务是学习技能；环境太吵是学习环境；不知道评分标准是教学与辅导。找到那一块，才知道该改什么。",
        ),
        h2("七、Neo：eLUT 的聊天机器人"),
        p(
            "最后一张图是聊天窗口：顶部写着 <b>eLUT bot</b>，窗口里是机器人 <b>Neo</b>，身份标注为 <b>eLUT assistant</b>。它的开场白是："
        ),
        p(
            "“Hi! I am the new chatbot for LUT. I am still learning and practicing, so please verify the accuracy of the information. Ask clearly and precisely to help me to understand you better (e.g. tell city of your study, your degree etc.). Use natural language and avoid abbreviations. Please do not tell me your personal information.”"
        ),
        p("这段话可以拆成四条使用规则与一条免责声明："),
        ol(
            "<b>核实准确性</b>：它自己在学习与练习中，你要验证信息；",
            "<b>问得清楚具体</b>：告诉它你在哪个城市学习、读什么学位等背景；",
            "<b>用自然语言、避免缩写</b>：缩写是它最容易误解的输入；",
            "<b>不要提供个人信息</b>：这是隐私边界，不是客气话。",
        ),
        p(
            "免责声明是“I am still learning and practicing”，也就是它可能答错。把它当“第一轮检索”，把 eLUT 页面与课程说明当“最终依据”。"
        ),
        tb(
            ("不好的问法", "为什么不好", "好的问法"),
            (
                "“DD 的 PSP 咋弄？”",
                "缩写 + 口语 + 没有城市/学位背景",
                "“I am a first-year double degree student in Lahti. How do I create my personal study plan in Sisu?”",
            ),
            (
                "“我的学号是（此处为示例号码），帮我查成绩”",
                "提供了个人信息，且它不该处理这类查询",
                "“Where can I see my completed credits in Sisu?”（自己去 Sisu 查）",
            ),
            (
                "“明天上课吗”",
                "缺少课程与日期，答案无法核实",
                "“I have CT30A1000 on Tuesday. Where can I check the room?”",
            ),
        ),
        h2("八、Speaking up：遇到不当行为的步骤"),
        p(
            "平等与伦理这一块的素材是一份 LTKY 的指引（Speaking up_instructions_LTKY）。它的前提写在最上方：<b>“If you have a problem with someone’s behavior, speak up!”</b> 未解决的问题与没说出口的事会不断累积（unsolved problems and unspoken issues tend to multiply），所以要尽早解决。"
        ),
        p(
            "指引同时给了一个关键定性：<b>把问题提出来不是评判或批评</b>（not judgment or criticism），而是以中立、尊重的方式进行，目标是共同找到解决办法；有时问题只是双方对情境的理解不同。理想的沟通是双向的，双方都感到被听见、被理解。"
        ),
        h3("8.1 六步操作"),
        tb(
            ("步骤", "图中做法", "可直接用的句子"),
            (
                "1 保持冷静",
                "深呼吸，整理思绪；感到不快是正常的，但保持镇定能让你更有效地表达",
                "（先停三秒，不在这时回击）",
            ),
            (
                "2 引起对方注意",
                "把对话从公开场合拉到私下",
                "“Can I talk to you in private for a minute?” / “How do you think you’re behaving right now?” / “That comment was not actually nice.”",
            ),
            (
                "3 使用非语言信号",
                "如果直接说让你不舒服，可以用摇头、抱臂、后退等信号",
                "（后退半步、摇头、停止微笑）",
            ),
            (
                "4 保持眼神接触",
                "显示自信与坚定，表明你在设定边界、不容忍骚扰",
                "（平视对方，不低头看手机）",
            ),
            (
                "5 明确指出具体行为",
                "说清“哪一句话、哪个动作”让你不适，而不是评价对方的人格",
                "“Your comments about my appearance are inappropriate and make me uncomfortable. I need you to stop making such remarks.”",
            ),
            (
                "6 用“我”而不是“你”",
                "表达自己的感受，而不是给对方定性",
                "“I feel uncomfortable when you make those comments,” 而不是 “You are making me uncomfortable.”",
            ),
        ),
        p(
            "如果行为持续，还有两步收尾：<b>说明后果</b>——“If this continues, I will have to report it to the HCP.”（HCP 是图中用到的机构缩写，指处理骚扰事务的联络人）；<b>记录事件</b>——记下日期、时间、地点与发生了什么，这些信息之后对 HCP 有用。"
        ),
        p(
            "指引最后一句很重要：如果事情在当下就被讨论清楚，可能就不需要联系 HCP。也就是说，这套步骤的目标是“解决问题”，不是“升级冲突”。"
        ),
        cal(
            "warn",
            "记录不是报复",
            "记录日期、时间、地点、原话，是为了在需要时能准确陈述事实。不要把它变成情绪日记或对他人的评价清单；事实越具体，越有用。",
        ),
        h2("九、把导览落到第一周"),
        p(
            "导览的价值不在“看完”，而在“按顺序做完”。把六块主题、四个系统与八个主题周压成一张两周行动表："
        ),
        st(
            "第 1 天：登录 eLUT，订阅支持与指导服务的通讯；把 Sisu、Moodle、Time-Edit、Tuudo 各打开一次",
            "第 2 天：在 Time-Edit 找到本周课表，在 Moodle 打开每门课，在 Sisu 确认选课状态",
            "第 3 天：找到辅导小组的联系方式，记下主题周的顺序与第一场活动",
            "第 1 周内：用 Neo 问一个具体问题，并回到 eLUT 页面核实答案",
            "第 2 周内：参加一次学生活动或社团，认识两个可以一起学习的人",
            "第 2 周内：读完 Speaking up 指引，把 HCP 的求助方式存进手机",
        ),
        p(
            "做完这六步，你就把“数字导览”变成了“可用的地图”：知道消息从哪来、课在哪上、作业在哪交、遇到事找谁。"
        ),
    ]
)

kw = K(
    (
        "eLUT",
        "学生信息门户",
        "The info page for LUT students; news, events and quick links.",
    ),
    ("Neo", "eLUT 聊天机器人", "The eLUT assistant chatbot; answers must be verified."),
    ("Analytics consent", "分析同意", "Needed before the chat window can be shown."),
    (
        "Sisu",
        "学生信息系统",
        "Student information system: study plan, enrolments, credits.",
    ),
    (
        "Moodle",
        "在线学习平台",
        "Online learning platform: materials, submissions, quizzes.",
    ),
    ("Time-Edit", "课表系统", "Schedules: course times, rooms and exam dates."),
    (
        "Tuudo",
        "日常学习生活应用",
        "Makes your daily study life easier (as described in the orientation figure).",
    ),
    (
        "tutoring",
        "辅导",
        "Peer and staff guidance for new students, organised in theme weeks.",
    ),
    (
        "theme weeks",
        "主题周",
        "Eight tutoring themes from orientation to fun with the group.",
    ),
    (
        "study ability",
        "学习能力",
        "Formed in the interaction between the student and the study environment.",
    ),
    (
        "personal resources",
        "个人资源",
        "Health, socioemotional and cognitive skills, relationships, identity, life situation.",
    ),
    (
        "study environment",
        "学习环境",
        "Physical, digital, psychosocial, cultural and pedagogic environments.",
    ),
    (
        "constructively aligned teaching",
        "建构一致的教学",
        "Teaching, assessment and outcomes designed to support each other.",
    ),
    (
        "speaking up",
        "发声",
        "Raising a problem with someone’s behaviour neutrally and respectfully.",
    ),
    (
        "HCP",
        "骚扰联络人",
        "The contact person to whom persistent harassment is reported.",
    ),
    (
        "document the incident",
        "记录事件",
        "Note dates, times, locations and details for later use.",
    ),
)

ex = "".join(
    [
        qa(
            "例 1　第一周用四个系统跑通一条链",
            "".join(
                [
                    p(
                        "<b>第 1 步（Time-Edit）：</b>打开本周课表，记下今天的时间、教室与课程代码。导览把 Time-Edit 标为 “Schedules”，它解决的就是“什么时候、在哪”。"
                    ),
                    p(
                        "<b>第 2 步（Moodle）：</b>按课程代码打开课程页，看本周材料与作业，确认提交入口。"
                    ),
                    p(
                        "<b>第 3 步（Sisu）：</b>确认这门课已注册、学分显示正常；若要报名考试，在 Sisu 完成。"
                    ),
                    p(
                        "<b>第 4 步（Tuudo）：</b>把今天的日程与校区服务信息放到随手可查的位置。"
                    ),
                    p(
                        "<b>判断标准：</b>四步之间没有互相矛盾——课表上的课在 Moodle 有页面，在 Sisu 有注册记录；任何一处缺失，当天就去补。"
                    ),
                ]
            ),
        ),
        qa(
            "例 2　按八个主题周安排入学前两个月",
            "".join(
                [
                    p(
                        "把主题周当成“关注点清单”，每周只做一件与之对应的动作：第 1 周 orientation——把四个系统各打开一次并收藏；第 2 周 wellbeing——找到校内支持服务的预约方式；第 3 周 living in Finland——把住宿与交通的规则问清；第 4 周 activities——加入一个社团。"
                    ),
                    p(
                        "第 5 周 healthcare and safety——记下学生健康服务与紧急求助路径；第 6 周 career services——看一次就业服务的入口与实习信息；第 7 周 exam rules——读完考试规则与学术不端的界限；第 8 周 fun with the group——参加一次小组活动。"
                    ),
                    p(
                        "<b>为什么按这个顺序：</b>导览的箭头就是从 orientation 到 fun 的单向顺序，前面的主题是后面的前提（不知道规则就谈不上安全与就业）。"
                    ),
                    p(
                        "<b>注意：</b>具体日期以辅导小组通知为准，图给的是主题顺序，不是日历。"
                    ),
                ]
            ),
        ),
        qa(
            "例 3　向 Neo 提一个能被核实的问题",
            "".join(
                [
                    p(
                        "<b>不好的写法：</b>“PSP 怎么弄？”——没有城市、学位、系统名，还用了缩写。"
                    ),
                    p(
                        "<b>好的写法：</b>“I am a first-year double degree student in Lahti. Where can I find the instructions for creating my personal study plan in Sisu?”——给了身份、城市、系统与动作。"
                    ),
                    p(
                        "<b>拿到回答后：</b>按 Neo 自己的提示“please verify the accuracy of the information”，回到 eLUT 的页面或课程说明核对；对不上就以页面为准。"
                    ),
                    p(
                        "<b>边界：</b>不要输入学号、电话、住址等个人信息，Neo 的开场白明确要求不要提供 personal information。"
                    ),
                ]
            ),
        ),
        qa(
            "例 4　遇到不当评论，按六步处理并记录",
            "".join(
                [
                    p(
                        "<b>场景：</b>小组讨论中，一位同学反复评论你的外貌，你已明确表示不适，对方仍继续。"
                    ),
                    p(
                        "<b>当场（步骤 1–3）：</b>先深呼吸三秒，不在这时争吵；说“Can I talk to you in private for a minute?”，把对话移到私下；如果不想直接说，用摇头、后退、停止回应等非语言信号。"
                    ),
                    p(
                        "<b>明确（步骤 4–6）：</b>保持眼神接触；指出具体行为——“Your comments about my appearance are inappropriate and make me uncomfortable. I need you to stop making such remarks.”；用“我”表达感受，而不是“你这人有问题”。"
                    ),
                    p(
                        "<b>收尾：</b>若继续，说明后果——“If this continues, I will have to report it to the HCP.”；同时记录日期、时间、地点、原话与在场的人。"
                    ),
                    p(
                        "<b>判断标准：</b>你说了“具体行为 + 我的感受 + 要求停止”三件事；若对方停止，事情可能就到此为止；若继续，记录足以支撑后续向 HCP 说明。"
                    ),
                ]
            ),
        ),
    ]
)

pr = "".join(
    [
        ol(
            "说出 Sisu、Moodle、Time-Edit、Tuudo 各自解决的问题，并举一个“该打开它”的场景。",
            "按顺序写出辅导主题周的八个主题，并说明为什么 orientation 排在第一。",
            "用学习能力模型的四块，分析“我总是赶在截止前才交作业”的可能原因（至少两块）。",
            "写出 Neo 的四条使用规则，并把“DD 的 PSP 咋弄？”改写成一条合格提问。",
            "按 Speaking up 的步骤，为“同学在群里反复开你玩笑”设计一段当面沟通（写出你会说的三句话）。",
        ),
        det(
            "参考答案与思路",
            "".join(
                [
                    p(
                        "<b>1.</b> Sisu 管学业状态（选课、报名、学分）；Moodle 管课程内容（材料、提交、测验）；Time-Edit 管时间地点（课表、教室、考试）；Tuudo 是日常学习生活的随身入口。场景示例：出门前看 Time-Edit；交作业用 Moodle；改学习计划用 Sisu；查校区日常服务用 Tuudo。"
                    ),
                    p(
                        "<b>2.</b> Orientation、Student’s wellbeing、Living in Finland、Activities and hobbies、Healthcare and safety、Career Services and employment in Finland、Exam rules and academic misconduct and study tips、Fun things to do with the group。orientation 排第一，因为后面的主题都预设你已知系统、规则与自己的小组。"
                    ),
                    p(
                        "<b>3.</b> 学习技能：不会把任务拆成可验收的小块、时间估计过于乐观；个人资源：睡眠不足或生活事件占用精力；学习环境：宿舍干扰多、通知常驻。干预要选最便宜的一块先做（例如先拆任务 + 开勿扰）。"
                    ),
                    p(
                        "<b>4.</b> 规则：核实准确性；问得清楚具体（给城市、学位等背景）；用自然语言、避免缩写；不要提供个人信息。改写示例：“I am a first-year double degree student in Lahti. How do I create my personal study plan in Sisu?”"
                    ),
                    p(
                        "<b>5.</b> 示例三句：“Can I talk to you in private for a minute?”；“I feel uncomfortable when you make those jokes about me — please stop.”；“If this continues, I will report it to the HCP.” 说完记录时间、地点与原话。"
                    ),
                ]
            ),
        ),
    ]
)

em = "".join(
    [
        cal(
            "exam",
            "必考",
            "四个系统的对应关系；六个主题板块；八个主题周的顺序；学习能力四块；Neo 的四条规则；Speaking up 的六个步骤与两句关键话术。",
        ),
        cal(
            "warn",
            "易错 1",
            "<b>把 Tuudo 当学习平台。</b>导览对它的定位只有“让日常学习生活更轻松”，材料、提交与测验在 Moodle。",
        ),
        cal(
            "warn",
            "易错 2",
            "<b>把主题周当课程周。</b>它是辅导活动的主题顺序，不是教学日历；具体日期看辅导小组通知。",
        ),
        cal(
            "warn",
            "易错 3",
            "<b>用缩写问 Neo，或把个人信息发给它。</b>开场白明确要求自然语言、避免缩写、不要提供个人信息。",
        ),
        cal(
            "warn",
            "易错 4",
            "<b>用“你”指责对方。</b>指引要求用“我”表达感受，并指出具体行为，而不是评价人格。",
        ),
        cal(
            "tip",
            "进阶",
            "能解释“为什么导览先讲信息渠道、最后讲平等与伦理”：前者决定你能否找到规则，后者决定你在规则失效时怎么办。",
        ),
    ]
)

cl = "".join(
    [
        h2("第一周（照着做）"),
        ck(
            "登录 eLUT，订阅支持与指导服务的通讯",
            "在 Sisu 确认本学期选课与学分状态",
            "在 Moodle 打开每门课，收藏课程页",
            "在 Time-Edit 找到本周课表与教室",
            "在 Tuudo 里放好日常日程入口",
            "找到辅导小组的联系方式与第一次活动时间",
        ),
        h2("前两个月（按主题周）"),
        ck(
            "orientation：四个系统各用过一次",
            "wellbeing：知道校内支持服务怎么预约",
            "living in Finland：住宿、交通、日常规则已问清",
            "activities：加入一个社团或固定活动",
            "healthcare and safety：存好学生健康服务与紧急求助方式",
            "career services：看过一次就业与实习信息",
            "exam rules：读完考试规则与学术不端界限",
            "fun with the group：参加过一次小组活动",
        ),
        h2("用 Neo 与维权时"),
        ck(
            "提问含城市、学位、系统名，不用缩写",
            "不向 Neo 提供学号、电话、住址等个人信息",
            "对 Neo 的回答回到 eLUT 页面核实",
            "遇到不当行为，先说具体行为与感受，再说要求",
            "必要时说明后果并记录日期、时间、地点、原话",
            "知道 HCP 是谁、怎么联系",
        ),
    ]
)

mp = tb(
    ("来源", "素材", "提取到的信息"),
    (
        "来源：图片",
        "eLUT frontpage.png",
        "顶部 SEARCH / LANGUAGE MENU / QUICK LINKS / MAIN MENU；欢迎语；新闻与活动；订阅通讯；Neo 需要 Analytics consent；搜索框",
    ),
    (
        "来源：图片",
        "koostedigiperh.png",
        "六个主题：Information channels、Planning & completing studies、Study ability & support、Campuses、Student life、Equality & Ethics",
    ),
    (
        "来源：图片",
        "Opiskelijan tärkeimmät järjestelmät ja työkalut (2).png",
        "Sisu（学生信息系统）、Moodle（在线学习平台）、Time-Edit（课表）、Tuudo（日常学习生活）；中心语 Most important systems and tools for students",
    ),
    (
        "来源：图片",
        "Tuutoroinnin teemaviikot en1 (2).png",
        "TUTORING THEME WEEKS 八个箭头主题及顺序；LUT 与 LAB 双标识",
    ),
    (
        "来源：图片",
        "Student life_digiorient_ENG.png",
        "三句文案（events and fun time / outdoor activities and hangouts / studying together with friends）；摄影者署名",
    ),
    (
        "来源：图片",
        "ENG-Opiskelukyky-lauseella-1536x864.png",
        "学习能力总纲句；四个板块及全部条目；四个小场景",
    ),
    (
        "来源：图片",
        "image.png",
        "eLUT bot / Neo / eLUT assistant；开场白的四条规则与“仍在学习”声明",
    ),
    (
        "来源：图片",
        "Speaking up_instructions_LTKY.pdf",
        "发声的前提与定性；六步做法与原句；后果说明与事件记录；HCP",
    ),
    (
        "（跳过）",
        "—",
        "无文本课件；导览目录中的 LUT-LOGO-WHITE.png 仅为标识，未提供额外信息",
    ),
    (
        "（补充）",
        "—",
        "第一节“三层入口”、第三节“日常链”、第九节两周行动表，属于把图中信息组织成操作顺序的整理，非图中原文",
    ),
    (
        "（缺口）",
        "—",
        "导览图未给出 Tuudo 的具体功能清单、主题周的具体日期、校区通勤细节；本讲未作推测",
    ),
)

LEC.append(
    L(
        slug="digital-orientation",
        tzh="第 1 讲 · 数字导览：LUT 学习环境与支持服务",
        ten="LUT Digital Orientation: Study Environment and Support Services",
        keywords=[
            "eLUT",
            "Neo",
            "Sisu",
            "Moodle",
            "Time-Edit",
            "Tuudo",
            "tutoring",
            "theme weeks",
            "study ability",
            "personal resources",
            "study environment",
            "speaking up",
            "HCP",
        ],
        files=[
            "eLUT frontpage.png",
            "koostedigiperh.png",
            "Opiskelijan tärkeimmät järjestelmät ja työkalut (2).png",
            "Tuutoroinnin teemaviikot en1 (2).png",
            "Student life_digiorient_ENG.png",
            "ENG-Opiskelukyky-lauseella-1536x864.png",
            "image.png",
            "Speaking up_instructions_LTKY.pdf",
        ],
        overview=ov,
        detail=de,
        kws=kw,
        examples=ex,
        practice=pr,
        exam=em,
        checklist=cl,
        mapping=mp,
    )
)

emit(
    "29428",
    12,
    "LUT digital orientation 数字导览",
    "LUT Digital Orientation",
    "LUT digital orientation 数字导览",
    "以图片为唯一素材的入学数字导览：eLUT 首页与六个主题、四个最重要的系统（Sisu/Moodle/Time-Edit/Tuudo）、八个辅导主题周、学生生活、学习能力四要素模型、Neo 聊天机器人的使用规则，以及 LTKY 的 Speaking up 处置步骤。",
    LEC,
)
