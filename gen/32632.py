# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import (L, emit, h2, h3, p, ul, ol, ck, st, tb, K, cal, badge, qa, det, pre, code, chips)


def Q(*a):
    if len(a) == 1:
        s = a[0]
        i = s.find('<p>')
        return qa(s[:i], s[i:])
    return qa(a[0], ''.join(a[1:]))


def D(*a):
    if len(a) == 1:
        s = a[0]
        i = s.find('<p>')
        return det(s[:i], s[i:])
    return det(a[0], ''.join(a[1:]))

LEC = []

# ============================================================ 1
LEC.append(L(
 slug='l1-launch-self-intro',
 tzh='第 1 讲 · 开课、自我介绍与学习资源',
 ten='Course Launch, Introducing Yourself, and Learning Resources',
 keywords=['baseline assignment', 'self-introduction', 'preferred name', 'yes/no question', 'tense choice', 'lingua franca', 'learner’s dictionary', 'collocation'],
 files=['3_Assignments_1_BASELINE ASSIGNMENT Introduction Video [DL Sep 10]_intro_intro.html',
        'Bingo (B2).docx',
        '7_Resources_2_Interesting facts about English.docx',
        '7_Resources_1_Online dictionaries.html',
        '4_UNIT 1 Building Know-how_1_Meeting 1 homework.html'],
 overview=(h2('本节定位')
  + p('KE00DA03 Professional English 是一门以<b>口头产出</b>为主线的专业英语课。第一讲做两件事：把课程的运作方式与考核规则讲清楚，然后立刻让你开口——用 1 至 2 分钟介绍自己，并用完整句向同学提问。这两件事决定了后面 12 次课的基础：老师要知道你的起点，你要知道这门课怎么算通过。')
  + p('本讲对应 Unit 1 Building Know-how 的开头，也是整门课「先建立表达习惯，再谈技巧」的逻辑起点。下一讲进入朗读与分块（chunking），那是把口语说清楚的技术底座。')
  + p('学完本讲你应当能够：')
  + ck('说清这门课的三个单元、四次作业与评分换算规则',
     '在不看稿的情况下用 1 至 2 分钟自然介绍自己的姓名、专业、来历与兴趣',
     '按信息槽写出地道英文自我介绍句，并正确选择一般现在时、现在完成时与一般过去时',
     '把 Bingo 卡片上的短语改写为正确的 Yes/No 问句，并用追问延续对话',
     '用英文复述「英语使用现状」中的比例与数量表达',
     '在 sanakirja.fi、Merriam-Webster、Cambridge、Longman 等词典之间按需要选择，并判断译文工具的输出能不能直接用')),
 detail=(h3('1.1 课程结构与四次作业')
  + p('课程按 13 次 meeting 推进，内容分三个单元：<b>Unit 1 Building Know-how</b>（自我介绍、朗读与分块、技术词汇、词序与介词），<b>Unit 2 Expressing Opinions</b>（电梯演讲、图表描述、会议对话、同意与不同意），<b>Unit 3 Communicating Professionally</b>（新闻幻灯片与小组陈述）。所有作业都在 Moodle 提交，不看邮箱。')
  + tb(('作业', '截止', '形式与要求', '计分'),
       ('BASELINE ASSIGNMENT: Introduction Video', 'Sep 10', '1 至 2 分钟自我介绍视频，正对镜头，不可剪辑、不可读稿', 'pass / fail'),
       ('ASSIGNMENT 1: Elevator Pitch', 'Nov 5（Meeting 11 现场录制）', '约 60 秒电梯演讲，先写稿、再练、课上录', '0–100 分'),
       ('ASSIGNMENT 2: Pronunciation Test', 'Nov 18（Moodle 10:00–22:00 开放）', '朗读本课程课上练过的材料与 Padlet 句子', '课程作业，按说明完成'),
       ('ASSIGNMENT 3: Presentation', 'Nov 27（最后一次网课）', '3 至 4 分钟工程主题演讲 + 视觉材料，breakout room 3 至 5 人', '0–100 分'))
  + p('两次计分作业的分值换算成 1 至 5 级：0 至 49.99 为 Fail (revise)，50 至 59.99 为 Passable (1)，60 至 69.99 为 Satisfactory (2)，70 至 79.99 为 Good (3)，80 至 89.99 为 Very Good (4)，90 至 100 为 Excellent (5)。注意 49.99 与 50.00 之间是一条硬线：差 0.01 分也是重修。')
  + cal('warn', '计分口径', 'Baseline 视频只判 pass/fail，语法和发音都不评分；但 ASSIGNMENT 1 与 ASSIGNMENT 3 明确把 grammar、pronunciation 列入评分项。所以「第一周说得粗糙没关系」这句话只在 baseline 阶段成立。')
  + h3('1.2 基线视频：它到底在测什么')
  + p('作业说明写得很清楚：<i>Your task is to create a short video where you introduce yourself. The point is to determine your base level of English (how you would speak naturally).</i>——目的是判断你的<b>基线水平</b>，也就是你自然说话时的样子，而不是你背诵时的样子。')
  + p('硬性要求有五条：时长 1 至 2 分钟；必须被看到正对镜头说话（<i>You must be seen talking in the video, directly to the camera</i>）；不能剪辑；<b>不能照着笔记读</b>；设备不限。评分只有一条：自然地说满 1 至 2 分钟。')
  + p('因此准备方式不是写稿，而是写<b>要点卡</b>：一张纸上写 6 个关键词（name、hometown、major、why、hobby、Finland），看一眼就行。写完整句子再背，反而会因为「背稿」被扣。')
  + p('这项作业还标注了 AI 使用禁令（AI use prohibited）。原文对 output 的定义是：<i>the final work or competence produced by a student that meets the objectives of the given learning task</i>——口语视频本身就是产出，所以不能由 AI 代写、代读、代合成。')
  + h3('1.3 自我介绍的六个信息槽')
  + p('把自我介绍拆成「信息槽」，每个槽配一句可复用的句型，比整段背诵稳得多。下面六个槽覆盖了作业里点名的全部内容（姓名与称呼、来自哪里、爱好与家庭、学什么与为什么、怎么来的芬兰）。')
  + tb(('信息槽', '可复用句型', '语言点'),
       ('姓名与称呼', 'My name is Zishuo Wang, but please call me Zishuo.', 'please call me + 名，说明 preferred name'),
       ('家乡', 'I’m from Zhengzhou, a city in central China.', 'be from + 地点；同位语补充说明'),
       ('专业与年级', 'I’m a second-year student at LUT, and I’m majoring in mechanical engineering.', '一般现在时表事实；major in'),
       ('选择理由', 'I chose this field because I’ve always been interested in how machines work.', '现在完成时 + interested in + 名词或 V-ing'),
       ('来芬经历', 'I came to Finland in 2023, after finishing high school.', '一般过去时 + 时间点；after + V-ing'),
       ('兴趣', 'In my free time I enjoy badminton, and I’ve recently taken up photography.', 'enjoy + V-ing；take up 表开始一项爱好'))
  + p('句型之外还有一条组织原则：<b>先给身份，再给理由，最后给一个可追问的钩子</b>。例如结尾说 <i>I’m also looking for a team to play badminton with, so let me know if you’re interested.</i>——这句会自然引发追问，让老师记住你。')
  + h3('1.4 时态：四个选择，不要混用')
  + p('中文母语者在这一段最容易出的错全部集中在时态。四条规则足以覆盖自我介绍：')
  + ul('<b>一般现在时</b>说稳定事实：<i>I study at LUT. I live in Lappeenranta.</i>',
       '<b>现在进行时</b>说现阶段临时状态：<i>I’m currently taking a course on thermodynamics.</i>',
       '<b>现在完成时</b>说持续到现在的经历或时长：<i>I’ve studied English for ten years. I’ve been to Sweden twice.</i>',
       '<b>一般过去时</b>说已结束的事件：<i>I came to Finland in 2023. I finished high school last June.</i>')
  + cal('warn', '高频错误', '说「我从 2023 年起在 LUT 读书」不能写成 <i>I am studying at LUT since 2023</i>。since 要求完成时：<i>I have been studying at LUT since 2023.</i> 同理 <i>I have 20 years</i> 是错的，年龄用 be：<i>I’m 20 years old.</i>')
  + h3('1.5 让口语听起来自然的三件小事')
  + p('第一，<b>语速</b>。英语自然语速约每分钟 130 至 150 词，1 至 2 分钟就是 130 至 300 词。说得过快是紧张的直接信号，说得过慢则显得在读。第二，<b>填充与自我修正</b>：<i>Well, … Actually, … I mean, … Let me think for a second.</i> 这些是母语者的正常停顿手段，比连续说「um」自然。第三，<b>句末降调</b>：陈述句句尾下沉，表示「我说完了」，这也是把发言权交回给对方的方式。')
  + p('练习方法：录音一次，回听时只做一件事——数一数有几个「um」，再录一次把它换成 <i>Well</i> 或一个 0.5 秒的静默。这个微调对基线视频的「自然」评价影响极大。')
  + h3('1.6 Bingo：用完整句提问')
  + p('Bingo (B2) 是本课程的开场活动：每个格子里是一条关于同学的描述（<i>Older than 22</i>、<i>Has had a pet</i>、<i>Able to touch their toes</i>……）。规则是<b>用完整句提问</b>（<i>Using full sentences, ask other students about the following topics</i>），对方答 yes 就把名字写进格子，连成五格喊 Bingo。')
  + p('把短语变成问句只需要判断三件事：句子里有没有 be 动词或情态动词（有就提前）、是不是 have 作实义动词（借 do/does）、其余动词一律借 do/does/did。')
  + tb(('卡片短语', '正确问句', '为什么'),
       ('Older than 22', 'Are you older than 22?', 'be 动词提前，不借 do'),
       ('Enjoys Finnish weather', 'Do you enjoy Finnish weather?', '实义动词，主语 you 用 do'),
       ('Has had a pet', 'Have you ever had a pet?', '完成时 have 提前；ever 表经历'),
       ('Able to play an instrument', 'Can you play an instrument?', '情态动词 can 提前'),
       ('Left-handed', 'Are you left-handed?', '形容词作表语，用 be'),
       ('Knows how to say ‘thank you’ in Finnish', 'Do you know how to say ‘thank you’ in Finnish?', '实义动词 know，借 do'))
  + cal('warn', '两个必错点', '① 第三人称 -s 不能搬到问句里：<i>Do you has a pet?</i> 错，应为 <i>Do you have a pet?</i> ② be 动词句不能借 do：<i>Do you are left-handed?</i> 错，应为 <i>Are you left-handed?</i>')
  + p('追问才是活动真正的语言训练。<i>Really? How long have you had it?</i>（现在完成时问持续时长）／<i>Where did you learn that?</i>（过去时问已结束事件）／<i>What kind of music do you play?</i>（do 问习惯）。每一轮追问都在练「时态跟着意义走」。')
  + h3('1.7 Interesting facts about English：数字与比例的表达')
  + p('课程资源里的这篇短文本身是一份语言材料，它的价值在于<b>比例、数量和被动语态</b>的写法。原文八条事实值得逐条拆：')
  + tb(('原文', '语言点', '中文'),
       ('about 650–700 million people with a native-like command of English', 'native-like command = 接近母语的掌握程度；million 前有具体数字时不加 s', '约 6.5 亿至 7 亿人英语接近母语水平'),
       ('Another 800 million people have a basic to average command of English.', 'basic to average 区间表达；another + 数量', '另有 8 亿人处于基础到中等水平'),
       ('Altogether, around 1400–1500 million people speak English.', 'Altogether 表合计；around 表约数', '合计约 14 至 15 亿人说英语'),
       ('This is almost a quarter of the world’s population.', '分数表达 a quarter；population 单数', '这几乎是世界人口的四分之一'),
       ('English is used as an official or semi-official language in over 60 countries.', 'be used as + 身份；over = more than', '英语在 60 多个国家作为官方或半官方语言使用'),
       ('Over two thirds of the world’s scientists write in English.', 'two thirds of + 复数名词 → 复数动词', '超过三分之二的世界科学家用英语写作'),
       ('Over 80% of all the information stored electronically around the world is in English.', '80% of + 不可数名词 → 单数动词', '全球电子存储的信息 80% 以上是英语'),
       ('More than two thirds of the world’s mail is written in English.', '一般现在时被动语态 is written', '世界邮件三分之二以上用英语书写'))
  + cal('warn', '主谓一致', '比例短语作主语时，动词跟 <b>of 后面的名词</b>走：<i>Two thirds of the scientists <b>write</b></i>（复数），<i>80% of the information <b>is</b></i>（不可数）。写成 <i>Two thirds of the scientists writes</i> 或 <i>80% of information are</i> 都是典型错误。')
  + p('这段材料还有一个可迁移的写作技巧：<b>用「据估计」开头，把数字的责任交给来源</b>。<i>According to an estimate, there are about 650–700 million people …</i> 这样写既专业又留了余地，做图表描述和演讲引用数据时同样适用。')
  + h3('1.8 词典与翻译工具：怎么用才不误事')
  + p('课程给出的词典清单分两类。芬英芬词典 <b>sanakirja.fi</b> 用 LUT/LAB 账号登录可获完整权限；英英词典有 <b>Merriam-Webster</b>（美式）、<b>Merriam-Webster’s Learner’s Dictionary</b>（学习者词典，释义用简单词）、<b>Cambridge Dictionary</b>（英式，带学习者版）、<b>Oxford Dictionaries</b>、<b>Collins</b>、<b>Longman</b>。翻译工具列了 sanakirja.fi translator、DeepL、Google Translate。')
  + p('课程对工具的态度是明确的警告：<i>Be critical in using online dictionaries or dictionary apps on your phone. Free wiki-based dictionaries are not necessarily the best option for in-depth language learning.</i> 以及 <i>Translation tools … don’t do as well in accuracy and Finnish-English translation … Always write your own texts yourself.</i>')
  + st('查词性与音标（重音位置决定你能不能读对）',
       '看搭配栏：动词看接什么介词，名词看可数不可数',
       '看语域标签：formal / informal / technical，决定能不能用在演讲里',
       '抄一个原句，再自己造一句；只抄不造等于没学')
  + p('同一个词在英式与美式里可能拼法、发音都不同：<i>organisation / organization</i>、<i>centre / center</i>、<i>programme / program</i>、<i>colour / color</i>；发音如 <i>process</i> 英 /ˈprəʊses/、美 /ˈprɑːses/，<i>schedule</i> 英 /ˈʃedjuːl/、美 /ˈskedʒuːl/。写作业时选定一种变体并保持一致，比混用更专业。')
  + h3('1.9 三次作业的 AI 红线各不相同')
  + p('同一个课程里，AI 规则是<b>逐作业</b>规定的，不能一概而论：')
  + tb(('作业', '可以用 AI 做什么', '不能用 AI 做什么'),
       ('Baseline 视频', '无（标注 AI use prohibited）', '任何代写、代读、代生成'),
       ('Elevator Pitch', '生成示例 pitch 作参考、语言指导、检查最终稿错误', '全部或部分代写 pitch 稿'),
       ('Presentation', '头脑风暴、协助检索（须复核来源）、总结信息、制作视觉材料', '写演讲稿、代做视觉材料以外的任何材料'))
  + p('这条规则的语言值得记住：<i>You must produce your own text.</i> 与 <i>AI can only be used as a guide.</i> 换句话说，AI 可以当教练，不能当作者。')
  + h3('1.10 与下一讲的衔接')
  + p('到这里你已经能开口介绍自己、能提问、能读懂数字表达。下一讲解决「说得清不清楚」：把句子切成意义块（chunking）、处理生词、把一段技术文本读给自己听。这是 Assignment 2 朗读测试与 Assignment 3 演讲的共同底座。')),
 kws=K(('baseline', '基线；基准测试', 'A first recording used to measure your starting level.'),
       ('native-like command', '接近母语的掌握', 'About 650–700 million people have a native-like command of English.'),
       ('average command', '中等掌握程度', 'Another 800 million have a basic to average command.'),
       ('lingua franca', '通用语', 'English works as a lingua franca in business and science.'),
       ('preferred name', '希望被称呼的名字', 'My name is Wang Zishuo, but please call me Zishuo.'),
       ('major in', '主修', 'I’m majoring in mechanical engineering.'),
       ('take up', '开始从事（爱好）', 'I’ve recently taken up photography.'),
       ('be interested in', '对……感兴趣', 'I’ve always been interested in how machines work.'),
       ('according to an estimate', '据估计', 'According to an estimate, 1.4 billion people speak English.'),
       ('two thirds of', '三分之二', 'Over two thirds of the world’s scientists write in English.'),
       ('a quarter of', '四分之一', 'This is almost a quarter of the world’s population.'),
       ('be used as', '被用作', 'English is used as an official language in over 60 countries.'),
       ('learner’s dictionary', '学习者词典', 'A learner’s dictionary explains words with simple definitions.'),
       ('collocation', '搭配', 'Heavy rain is a collocation; strong rain is not.'),
       ('register', '语域', 'The label informal tells you not to use the word in a report.'),
       ('pass / fail', '通过 / 不通过', 'The baseline video is graded pass or fail only.')),
 examples=(Q('例 1　把下面这段中式自我介绍改写成地道英文：',
   p('「我叫王梓硕，来自中国郑州。我在 LUT 学习机械工程，因为我对机器很感兴趣。我 2023 年来芬兰。我喜欢打羽毛球。」') +
   p('<b>解：</b>逐句定位问题，再改写。') +
   p('① 「我叫……」→ 英文姓名顺序与称呼习惯：<i>My name is Wang Zishuo, but please call me Zishuo.</i>（英文名在前，姓在后；主动给出 preferred name）。') +
   p('② 「我在 LUT 学习」→ 现在进行时误用为一般现在时：<i>I’m a second-year student at LUT, and I’m majoring in mechanical engineering.</i> 地点介词用 at，不用 in。') +
   p('③ 「因为我对机器很感兴趣」→ 中文「对……感兴趣」是 interested in，不是 of：<i>I chose this field because I’ve always been interested in how machines work.</i>') +
   p('④ 「我 2023 年来芬兰」→ 已结束事件用过去时：<i>I came to Finland in 2023.</i> 若说「自 2023 年起一直在芬兰」则用 <i>I’ve been in Finland since 2023.</i>') +
   p('⑤ 「我喜欢打羽毛球」→ enjoy 后接 V-ing：<i>In my free time I enjoy playing badminton.</i>') +
   p('<b>通用思路：</b>先按信息槽切句 → 每句判定时态（事实／经历／已结束）→ 修介词与动词形式 → 最后加一句钩子。'))
  + Q('例 2　把 Bingo 卡片上的 <i>Has broken a bone</i> 与 <i>Considers themselves to be a good cook</i> 改成问句，并为每个问句准备一个追问。' +
   p('<b>解：</b>第一步判结构。<i>Has broken a bone</i> 是现在完成时，助动词 have 提前，主语 you：<i>Have you ever broken a bone?</i> 加 ever 是因为问的是「至今为止的经历」。') +
   p('<i>Considers themselves to be a good cook</i> 的谓语是实义动词 consider，主语 you 借 do：<i>Do you consider yourself to be a good cook?</i> 注意反身代词随主语变：themselves → yourself。') +
   p('第二步准备追问：<i>Have you ever broken a bone?</i> → <i>Ouch. How long did it take to heal?</i>（过去时问已结束的过程）；<i>Do you consider yourself a good cook?</i> → <i>What’s your signature dish?</i>（一般现在时问习惯性事实）。') +
   p('<b>通用思路：</b>看谓语类型（be／情态／完成／实义）→ 决定提前谁 → 换对反身代词与人称 → 用不同时态追问，逼迫对话继续。'))
  + Q('例 3　用英文复述这条事实并说明动词为什么用单数：<i>Over 80% of all the information stored electronically around the world is in English.</i>' +
   p('<b>解：</b>先找主语中心词。主语是 <i>Over 80% of all the information</i>，中心名词是 <b>information</b>，不可数，所以谓语用单数 <b>is</b>。') +
   p('再看修饰：<i>stored electronically around the world</i> 是过去分词短语后置修饰 information，等于 <i>which is stored …</i> 的省略。这种「名词 + 过去分词短语」的压缩结构在技术英语里极常见。') +
   p('复述示范：<i>More than four fifths of the information that is stored electronically worldwide is in English.</i> 同义替换：Over → More than；80% → four fifths；around the world → worldwide。') +
   p('<b>通用思路：</b>比例主语先定中心名词的数 → 再定谓语单复数 → 最后做同义替换（数字换成另一种分数、副词换成同义词），确保意思不变。'))
  + Q('例 4　同学写了 <i>I am studying at LUT since 2023 and I have 20 years.</i> 请指出错误并说明规则。' +
   p('<b>解：</b>两处错误。① <i>am studying … since 2023</i>：since 引导的时间段必须与完成时搭配，改为 <i>I have been studying at LUT since 2023.</i>（现在完成进行时强调持续）。') +
   p('② <i>I have 20 years.</i>：年龄在英语里用 be 动词，<i>I’m 20 years old.</i> 若要说「我学英语学了 20 年」才是 <i>I’ve studied English for 20 years.</i>') +
   p('<b>通用思路：</b>看到 since／for 先查时态；看到年龄先查动词是 be 还是 have；这类错误在自我介绍的 30 秒内出现频率最高。'))),
 practice=(ol('用 6 个信息槽写一段 90 至 110 词的自我介绍，然后数词数并估算朗读时长（按 130 词／分钟）。',
         '把下列短语改成 Yes/No 问句：<i>Able to whistle</i>；<i>Has a younger sibling</i>；<i>Worried about English classes</i>；<i>Able to speak more than three languages</i>。',
         '改错：<i>Do you has a pet?</i> / <i>Do you are left-handed?</i> / <i>I am student of LUT.</i> / <i>My hobby is play basketball.</i>',
         '把 <i>Two thirds of the world’s mail is written in English.</i> 改成主动语态，并说明主语单复数为什么不变。',
         '你要查 <i>comply</i> 这个词准备用在会议对话里。写出查词典的四步，并说明为什么不能只看中文释义。')
  + D('答案与思路' +
   p('<b>1.</b> 参考答案（104 词）：<i>Hi, my name is Wang Zishuo, but please call me Zishuo. I’m from Zhengzhou, a city in central China. I’m a second-year student at LUT and I’m majoring in mechanical engineering. I chose this field because I’ve always been interested in how machines work, and I spent two years in a robotics club in high school. I came to Finland in 2023, right after I finished high school. In my free time I enjoy playing badminton and I’ve recently taken up photography.</i> 104 词 ÷ 130 词／分钟 ≈ 0.8 分钟，偏短，可再补一句钩子到 130 词左右。') +
   p('<b>2.</b> <i>Can you whistle?</i>（情态动词提前）／<i>Do you have a younger sibling?</i>（实义 have 借 do）／<i>Are you worried about English classes?</i>（形容词表语用 be）／<i>Can you speak more than three languages?</i>。') +
   p('<b>3.</b> <i>Do you has a pet?</i> → <i>Do you have a pet?</i>（助动词已承担人称，主要动词回归原形）；<i>Do you are left-handed?</i> → <i>Are you left-handed?</i>（be 动词句不借 do）；<i>I am student of LUT.</i> → <i>I’m a student at LUT.</i>（单数可数名词要冠词，地点用 at）；<i>My hobby is play basketball.</i> → <i>My hobby is playing basketball.</i>（表语位置用 V-ing）。') +
   p('<b>4.</b> <i>People write more than two thirds of the world’s mail in English.</i> 改为主动后主语变成 people，仍是复数，动词 write 用原形；原句的主语中心词 mail 不可数，所以被动句用 is。两种写法的主谓一致都由「谁作主语」决定。') +
   p('<b>5.</b> 四步：查词性与音标（comply /kəmˈplaɪ/，动词）→ 查搭配（comply <b>with</b> a standard／regulation）→ 查语域（正式、技术语境）→ 抄原句并造句（<i>The plug does not comply with the standard.</i>）。只背中文「遵守」会导致写成 comply to，因为中文不告诉你介词。'))),
 exam=(cal('exam', '必考', '课程结构与作业截止时间；Baseline 视频的五条硬性要求；自我介绍的六个信息槽与时态选择；Yes/No 问句的三类构成；比例主语的主谓一致。这些都会在课堂提问、作业说明和测验里反复出现。')
  + cal('warn', '易错 1', '时态与 since／for 的搭配：<i>I am studying here since 2023</i> 必错。凡 since 必接完成时。')
  + cal('warn', '易错 2', '问句里保留第三人称 -s（<i>Do you has</i>）与 be 动词句借 do（<i>Do you are</i>）。这两种错误在口语里最容易被听出来。')
  + cal('warn', '易错 3', '比例主语的主谓一致：<i>two thirds of the scientists write</i>（复数）／<i>80% of the information is</i>（单数）。')
  + cal('tip', '进阶', '把 <i>native-like command</i>、<i>lingua franca</i>、<i>semi-official language</i> 这类短语用进自己的演讲开头，比只用 <i>English is important</i> 更能体现词汇层次。')),
 checklist=(h2('本讲方法清单')
  + h3('自我介绍四步检查')
  + ck('信息槽齐不齐：姓名与称呼、家乡、专业、选择理由、来芬经历、兴趣',
     '每句时态对不对：事实用现在时、经历用完成时、已结束用过去时',
     '冠词与介词：a student at LUT、interested in、major in、arrive in',
     '自然度：有没有背稿腔、语速是否在 130 至 150 词／分钟、句末是否降调')
  + h3('查词典四步')
  + st('查词性与音标，确认重音位置',
       '查搭配与介词，抄下原句',
       '查语域与英美变体，决定用哪一种',
       '自己造一句并读出来，确认能说出口')
  + h3('问句生成三步')
  + ck('看谓语：be／情态／完成时助动词／实义动词',
     '决定提前谁：be 与情态直接提前，完成时提前 have，实义动词借 do/does/did',
     '主要动词回归原形，人称与反身代词跟着主语改')),
 mapping=tb(('源文件', '位置 / 页码', '覆盖内容'),
   ('3_Assignments/1_BASELINE ASSIGNMENT Introduction Video [DL Sep 10]/intro/intro.html', '全篇', '作业目的、五条硬性要求、pass/fail 标准、AI 禁令'),
   ('3_Assignments_1_BASELINE ASSIGNMENT Introduction Video [DL Sep 10]_Submissions_Zishuo Wang_Online text.html', '全篇', '学生提交的 YouTube 链接，仅作提交格式示例，不构成语言点'),
   ('Bingo (B2).docx', '全表', 'Bingo 规则、25 个话题短语、完整句提问要求'),
   ('7_Resources/2_Interesting facts about English.docx', '全篇', '英语使用现状八条事实、比例与数量表达、被动语态'),
   ('Interesting facts about English.docx', '全篇', '同上（重复副本，内容一致）'),
   ('7_Resources/1_Online dictionaries.html', '全篇', '词典与翻译工具清单、批判使用的警告'),
   ('4_UNIT 1/1_Meeting 1 homework.html', '全篇', '开课调查、baseline 截止日、芬兰利弊讨论、带笔记本上课'),
   ('（跳过）', '—', '重复副本 Interesting facts about English.docx 与 Submissions 中的链接页，不再单独设知识点'),
   ('（拓展）', '—', '自我介绍信息槽句型表、时态四选择、130 至 150 词／分钟语速换算为教学补充，原文只给作业要求'))))
# ============================================================ 2
LEC.append(L(
 slug='l2-reading-chunking',
 tzh='第 2 讲 · 朗读、分块与技术文本阅读',
 ten='Reading Aloud, Chunking, and Technical Texts',
 keywords=['chunking', 'sense group', 'pausing', 'head noun', 'skim', 'scan', 'signpost word', 'glossary'],
 files=['4_UNIT 1 Building Know-how_2_Meeting 2 homework.html',
        '4_UNIT 1 Building Know-how_3_Meeting 3 homework.html',
        '5_UNIT 2 Expressing Opinions_1_Meeting 8 homework.html'],
 overview=(h2('本节定位')
  + p('第 2 讲把「说」从敢说推进到说清楚。课程在第 2、3 次 meeting 布置的作业是：找一篇短文朗读、列出新词与难读词；读完 Supercell 的阅读练习并<b>准备把短语用在对话里</b>；到 Meeting 8 再读 Data Centers，要求 <i>Collect words and chunks + prepare to discuss next time</i>。这条线的关键词是 <b>chunking</b>——把句子切成意义块。')
  + p('它是第 1 讲自我介绍的延长线（说得自然），也是后面电梯演讲与 3 至 4 分钟演讲的地基：所有「听起来像英语」的效果，都来自块与块之间的停顿和块内的连贯。')
  + p('学完本讲你应当能够：')
  + ck('用竖线给一段 40 词左右的技术文本标出意义块与三档停顿',
     '把 5 个词以上的长名词短语从后往前拆成可读的单位',
     '按「词性→音标→搭配→例句→入库」五步处理一个生词',
     '用 skim 与 scan 两种速度分别处理结构与数据',
     '识别 however、therefore、whereas 等信号词并判断作者态度',
     '在 simplified 与 advanced 两版文本之间选择阅读顺序',
     '用「立场—理由—例证」三段式准备一段 60 秒的阅读讨论发言')),
 detail=(h3('2.1 为什么课程把朗读放在第一位')
  + p('Meeting 2 的作业写得很朴素：<i>Find a short text, read it out loud, and list new / difficult-to-pronounce words.</i> 朗读之所以是最高效的诊断工具，是因为它同时暴露四个层面的问题：<b>音</b>（单个音素发不准）、<b>词</b>（重音位置错）、<b>块</b>（该停的地方不停）、<b>调</b>（该降的升上去）。默读时这四层全被掩盖。')
  + p('课程同时给了操作细节：把新词与难读词列成笔记带到课堂上讨论（<i>Bring your notes to class next time</i>）。这意味着朗读不是表演，而是<b>取样本</b>——你要带着证据来上课。')
  + h3('2.2 Chunking：把句子切成意义块')
  + p('<b>Chunking</b>（分块）指把连续语流切成若干 <b>sense group / thought group</b>（意义块），每块是一个完整的意思单元，通常 3 至 6 个词。块内不停顿，块间停顿。它是英语口语的「呼吸单位」，也是听力理解的「切分单位」。')
  + p('切分不是凭感觉，有四条可操作的规则：')
  + tb(('规则', '做法', '例'),
       ('主语与谓语之间', '主语较长时，主语后停一次', 'The cooling system we installed last year | has reduced costs.'),
       ('动词与宾语之间', '动词后稍停，把宾语作为一个整体', 'The report describes | a new type of connector.'),
       ('介词短语前', '介词短语是独立的信息单位', 'The head office is located | outside Lappeenranta.'),
       ('从句与列举处', '连词、关系词、逗号处停；列举每项后停', 'If the plugs are the wrong type, | they will have to be replaced.'),
       ('长名词短语内部', '在中心名词前断开，不把修饰语读散', 'the cross connection room | operator | maintenance log'))
  + cal('warn', '最常见的破句', '把介词与它的宾语拆开读：<i>… is located outside | Lappeenranta</i>。这会让听者以为句子结束。介词短语必须整块读：<i>… is located | outside Lappeenranta</i>。')
  + h3('2.3 三档停顿与标记法')
  + p('英语的停顿有长短之分，标记时可以统一约定：单竖线 <code>|</code> 表示 0.3 至 0.5 秒的短停（换气、分块），双竖线 <code>||</code> 表示 0.8 至 1 秒的中停（句末、段落转换），段落之间用 <code>|||</code>。这套记号与课程「Read and record the story — pausing, pitch and intonation」的作业要求完全对应：先把停顿标在纸上，再录。')
  + p('示范（对话原句）：<i>The plug is the wrong type. || It’s almost exactly like the correct one | but when you look at it carefully, | you can see that it’s slightly different.</i>')
  + p('注意第二句的三个块：<i>It’s almost exactly like the correct one</i>（主句）／<i>but when you look at it carefully</i>（条件从句）／<i>you can see that it’s slightly different</i>（结果）。块数与信息单元数一致，读起来就有层次。')
  + h3('2.4 长名词短语：从后往前拆')
  + p('技术英语的招牌结构是「修饰语堆在名词前」：<i>high-pressure steam turbine maintenance schedule</i>。中文习惯把中心词放后面说「……的……的……」，英文则反过来。处理办法是<b>先找中心名词，再从右往左一层层加</b>：')
  + st('找中心名词：schedule（计划表）',
       '往左一层：maintenance schedule（维护计划）',
       '再往左：steam turbine maintenance schedule（蒸汽轮机维护计划）',
       '最左：high-pressure …（高压蒸汽轮机维护计划）')
  + p('读的时候只在中心名词前停一次：<i>high-pressure steam turbine | maintenance schedule</i>，不要每个词都顿。写的时候则相反——修饰语超过三个就改成介词短语或从句：<i>the maintenance schedule for the high-pressure steam turbine</i>，可读性立刻提升。')
  + h3('2.5 生词处理五步：从「认识」到「能用」')
  + p('课程要求 <i>list new / difficult-to-pronounce words</i>，但列表本身不产生能力。把生词变成可用的词块（chunk），需要五步：')
  + st('标词性：名词、动词、形容词还是不可数名词，决定后面能不能加 -s、要不要冠词',
       '抄音标并标重音：<i>nuisance</i> /ˈnjuːsns/，重音在第一音节；<i>comply</i> /kəmˈplaɪ/，重音在第二音节',
       '抄搭配：<i>a nuisance</i> 常与 <i>cause / be / quite a</i> 连用；<i>comply with</i> 不接 to',
       '造一句与自己专业相关的句子：<i>The noise from the compressor is quite a nuisance.</i>',
       '入 glossary：按主题归档（meeting language、electrical parts、graphs），每次课新增 5 至 8 条')
  + p('这套流程对应课程里反复出现的两个要求：<i>Collect words and chunks</i>（收词要收块）与 <i>prepare to use the phrases in conversation</i>（收了要在对话里用掉）。只收藏不使用，词汇永远停留在被动词汇层。')
  + cal('tip', '词块优先', '记 <i>cause a nuisance</i>、<i>comply with the standard</i>、<i>a loose connection</i> 这样的三词块，比单记 nuisance / comply / connection 三个词更省力，也更容易在口语中调用。')
  + h3('2.6 两种阅读速度：skim 与 scan')
  + p('<b>Skim</b>（略读）求结构：读标题、小标题、首末段、每段第一句，30 秒内回答「这篇讲什么、分几块」。<b>Scan</b>（扫读）求数据：眼睛只找数字、单位、专有名词、日期，不读句子。技术文本的阅读顺序通常是 skim → scan → 精读需要的那一段。')
  + p('这一步之所以重要，是因为 Presentation 作业要求 <i>finding reliable information</i> 与 <i>Find sources on the topic (must be mentioned)</i>：你需要在多篇来源里快速判断哪一篇值得引用，而不是从第一行读到最后一行。')
  + tb(('信号词', '功能', '读到它要做什么'),
       ('however / nevertheless', '转折', '后面的内容才是作者真正的主张'),
       ('therefore / as a result / consequently', '因果', '找前面那句话的原因'),
       ('in addition / moreover / furthermore', '递进', '这是第二个并列论据，可跳过细节'),
       ('whereas / in contrast / on the other hand', '对比', '两边都要记，常出比较题'),
       ('for instance / such as', '举例', '例子可快速扫过，除非要引用数据'),
       ('in other words / that is', '重述', '前面那句没读懂，靠这句补救'))
  + h3('2.7 Supercell：两版文本怎么用')
  + p('Meeting 3 的作业提供同一篇材料的两个版本：<b>Supercell (advanced)</b> 与 <b>Supercell (simplified)</b>，任务是 <i>Finish the reading exercise</i> 并 <i>Prepare to use the phrases in conversation next time</i>。两版并存的设计意图很清楚：先用简化版建立框架，再用原版抓真实词块。')
  + st('先读 simplified：10 分钟内搞清楚「谁、做了什么、结果如何」三件事',
       '再读 advanced：把简化版里被替换掉的表达圈出来（如 <i>make → generate</i>、<i>a lot of → a substantial number of</i>）',
       '对比同一句在两版中的写法，抄下 5 组「升级表达」',
       '把这些表达套进自己的句子，准备在下次对话中使用')
  + p('这套方法可以直接迁移到 Data Centers 的阅读：作业同样给了简化版链接，也是要求「收词块 + 准备讨论」。')
  + h3('2.8 从读到说：讨论准备的三段式')
  + p('Meeting 8 的要求是 <i>Collect words and chunks + prepare to discuss next time</i>。讨论发言最稳的结构是三段：<b>立场句 → 理由 → 例证</b>。')
  + p('示范：<i>I think data centres will keep growing in Finland. || The main reason is that our electricity is relatively cheap and the climate helps with cooling. || For example, the new facility outside Lappeenranta uses outside air for most of the year.</i>')
  + p('三段之间正是双竖线的位置：每一段一个意义块群，段内用单竖线。这个结构与后面电梯演讲的「钩子—证据—价值」是同构的，只是长度不同。')
  + h3('2.9 录音三听法')
  + p('作业要求朗读并录音，但录音只有被分析才有价值。三听法：<b>第一听</b>只听停顿——块切对了吗，有没有在介词后断；<b>第二听</b>只听词尾——-s、-ed、-t 有没有吞掉；<b>第三听</b>只听重音——每块里最重的那个词是不是信息词。每次只关注一件事，比一次听全部有效得多。')
  + cal('warn', '朗读的三个通病', '① 逐词读，每个词都停（听起来像机器）；② 重音落在功能词上（<i>the</i>、<i>of</i>、<i>to</i> 读得比名词响）；③ 句末不降调，听者不知道你说完了。这三点在 Assignment 2 的朗读测试中都会被听出来。')
  + h3('2.10 从本讲到后面三讲')
  + p('分块解决「一段话怎么切」，下一讲解决「一个词怎么用、一句话怎么排」：技术词汇的分层（食物、厨具、电脑与手机部件、专业词表）与语法诊所（词序、问句、介词）。再往后，电梯演讲与演讲作业都要用到本讲的停顿与三段式。')),
 kws=K(('chunking', '分块', 'Breaking speech into meaning groups instead of word by word.'),
       ('sense group / thought group', '意义块', 'Each chunk carries one complete idea, usually 3–6 words.'),
       ('pausing', '停顿', 'Short pauses mark chunks; long pauses mark sentence ends.'),
       ('head noun', '中心名词', 'In a long noun phrase, the head noun is the last content word.'),
       ('skim', '略读', 'Read headings and first sentences to get the structure.'),
       ('scan', '扫读', 'Look only for numbers, names and dates.'),
       ('signpost word', '信号词', 'However, therefore and whereas tell you how ideas connect.'),
       ('glossary', '术语表', 'A topic-based word list you build yourself.'),
       ('read aloud', '朗读', 'Reading out loud reveals pronunciation problems that silent reading hides.'),
       ('difficult-to-pronounce word', '难读词', 'Words you list and bring to class for feedback.'),
       ('simplified version', '简化版', 'A rewritten text with easier vocabulary, used to build the frame first.'),
       ('loose connection', '松动的接头', 'There is a loose connection here.'),
       ('nuisance', '麻烦事', 'The error has been quite a nuisance.'),
       ('comply with', '符合（标准）', 'The plug does not comply with the standard.'),
       ('collect words and chunks', '收集词与词块', 'Collect words and chunks, then prepare to discuss.'),
       ('stance–reason–example', '立场—理由—例证', 'A three-step structure for a short discussion turn.')),
 examples=(Q('例 1　给下面这句话标出意义块与三档停顿：<i>The head office is located outside Lappeenranta and it employs over four hundred people.</i>' +
   p('<b>解：</b>先找谓语与连词。两个并列分句由 and 连接，and 前是中停。第一分句主语 The head office 较短，不必停；谓语 is located 与介词短语 between 之间停一次。第二分句主语 it 轻读不停。') +
   p('标注结果：<i>The head office is located | outside Lappeenranta, || and it employs | over four hundred people.</i>') +
   p('为什么 <i>outside Lappeenranta</i> 前面停：介词短语是独立的地点信息块。为什么 <i>over four hundred people</i> 前面停：动词 employs 后稍停，把宾语作为整体读出。') +
   p('<b>通用思路：</b>先划连词与标点（定中停）→ 再找介词短语与从句（定短停）→ 最后检查有没有把介词与宾语拆开。'))
  + Q('例 2　把 <i>the cross connection room operator maintenance log</i> 拆成可读单位，并改写为更清楚的介词短语形式。' +
   p('<b>解：</b>从右往左找中心名词：log（日志）→ maintenance log（维护日志）→ operator maintenance log（操作员维护日志）→ cross connection room operator …（交叉连接室操作员的……）。') +
   p('朗读切分：<i>the cross connection room | operator | maintenance log</i>。三块对应三个语义层：地点、人、物。') +
   p('改写：<i>the maintenance log kept by the operator of the cross connection room</i>。用 kept by 与 of 把三层关系显性化，读者不必猜。') +
   p('<b>通用思路：</b>先定中心词，再从右往左加修饰；朗读在中心词前停，写作在修饰超过三层时改用介词短语或从句。'))
  + Q('例 3　为 <i>nuisance</i> 做一张词卡，并用它写一句与设备故障有关的句子。' +
   p('<b>解：</b>词性：可数名词（a nuisance / nuisances）。音标：/ˈnjuːsns/，重音第一音节，第二个音节弱化为 /sns/。') +
   p('搭配：<i>be a nuisance</i>、<i>cause a nuisance</i>、<i>quite a nuisance</i>、<i>a real nuisance</i>。语域：口语与半正式书面均可用，技术报告里偏向 <i>problem</i> 或 <i>fault</i>。') +
   p('例句：<i>The error has been quite a nuisance: we have had three short interruptions this week.</i> 这句同时示范了现在完成时（持续到现在）与冒号后的具体化。') +
   p('<b>通用思路：</b>词卡必须包含词性、音标、搭配、语域、自造句五项；缺任何一项，这个词在口语里就调不出来。'))
  + Q('例 4　读下面两句，指出哪一句更适合作为讨论发言的立场句，并说明理由：',
   p('A. <i>Data centres use a lot of electricity and I read something about it.</i>')
   + p('B. <i>In my view, data centres can be a good fit for Finland, mainly because of cheap electricity and cool air.</i>') +
   p('<b>解：</b>B 更适合。它有三个特征：明确的立场标记 <i>In my view</i>；可被反驳的主张 <i>can be a good fit</i>（而不是模糊的「用了很多电」）；预告了理由 <i>mainly because of …</i>，为下一块留出接口。') +
   p('A 的问题：<i>I read something about it</i> 是来源不明的主观陈述，无法支撑讨论；<i>a lot of</i> 在书面讨论里偏口语，可换 <i>a substantial amount of</i>。') +
   p('改写 A 的一种方式：<i>Data centres consume a substantial amount of electricity, which is why location matters.</i> 把事实句改成带因果的主张句，就能接理由块。') +
   p('<b>通用思路：</b>立场句必须「可被反对」；判断标准是听者能不能回一句 <i>I don’t agree, because …</i>。不能，就还不是立场句。'))),
 practice=(ol('给这句话标三档停顿：<i>If the plugs are all the wrong type they will have to be substituted as soon as possible because sooner or later they will cause more trouble.</i>',
         '把 <i>the high-pressure steam turbine maintenance schedule</i> 改写为介词短语形式，并说明朗读时在哪里停。',
         '用 skim 与 scan 的分工，说明你拿到一篇 6 页的 Data Centers 报告后前 3 分钟会做什么。',
         '为 <i>comply</i> 与 <i>substitute</i> 各做一张词卡（词性、音标、搭配、例句）。',
         '用「立场—理由—例证」三段式写一段 60 秒发言，主题：芬兰是否适合建数据中心。')
  + D('答案与思路' +
   p('<b>1.</b> <i>If the plugs are all the wrong type | they will have to be substituted | as soon as possible, || because sooner or later | they will cause more trouble.</i> 条件从句后短停；<i>as soon as possible</i> 是时间状语块，独立成块；because 前中停。') +
   p('<b>2.</b> <i>the maintenance schedule for the high-pressure steam turbine</i>。朗读时在 <i>schedule</i> 后停一次即可，因为中心词提前了，修饰语变成后置介词短语，结构更线性。') +
   p('<b>3.</b> skim（1 分钟）：读标题、目录、摘要、每章第一句，写下三句结构笔记；scan（1 分钟）：只找装机容量、能耗、PUE、年份、地点等数字与专有名词；最后一分钟决定精读哪一节（通常是与自己演讲主题相关的那一节）。') +
   p('<b>4.</b> comply /kəmˈplaɪ/ 动词，搭配 <i>comply with</i> + 标准或规定，例 <i>All plugs must comply with the standard.</i>；substitute /ˈsʌbstɪtjuːt/ 动词或名词，搭配 <i>substitute A for B</i>（用 A 替换 B）与 <i>a substitute for B</i>，例 <i>We substituted the old plugs for the new type.</i> 注意 substitute 的介词是 for，不是 with。') +
   p('<b>5.</b> 参考：<i>I’d argue that Finland is a good location for data centres. || Electricity is relatively cheap here and the cold climate reduces cooling costs. || For instance, waste heat from one facility is already used to warm nearby buildings.</i> 三段分别 1 句、1 句、1 句，共约 45 词，加上停顿与眼神约 30 秒，可再扩一句数据。'))),
 exam=(cal('exam', '必考', 'chunking 的四条切分规则与三档停顿记号；长名词短语的中心词判断；生词处理五步；skim 与 scan 的分工；信号词的六种功能。朗读测试与演讲评分都会直接检验这几项。')
  + cal('warn', '易错 1', '在介词与宾语之间停顿（<i>located outside | Lappeenranta</i>），造成句意断裂。')
  + cal('warn', '易错 2', '把长名词短语逐词顿开，或反过来一口气读完不做任何切分——两种都让听者无法解析结构。')
  + cal('warn', '易错 3', '生词只记中文释义，不记搭配：结果写出 <i>comply to the standard</i>、<i>substitute with</i> 这类介词错误。')
  + cal('tip', '进阶', '把信号词当「阅读路标」用：读摘要时只圈 however、therefore、whereas，三分钟就能还原作者的论证骨架。')),
 checklist=(h2('本讲方法清单')
  + h3('一段文本的朗读准备（四步）')
  + st('先默读一遍，划出连词、标点、从句边界',
       '用单竖线标短停、双竖线标中停，每块控制在 3 至 6 词',
       '圈出每块里最重要的一个词（信息词），准备重读',
       '录一遍，按「只听停顿→只听词尾→只听重音」三听法自评')
  + h3('生词入库五步')
  + ck('标词性与可数性', '抄音标与重音', '抄两个搭配', '造一句本专业的句子', '按主题归入 glossary')
  + h3('技术文本三遍读法')
  + ck('第一遍 skim：标题、小标题、首末句，写下结构',
     '第二遍 scan：数字、单位、专有名词、日期',
     '第三遍精读：只读与任务相关的那一节，圈信号词与词块')),
 mapping=tb(('源文件', '位置 / 页码', '覆盖内容'),
   ('4_UNIT 1/2_Meeting 2 homework.html', '全篇', '朗读短文并列出新词与难读词；Padlet 词表朗读；YLE News 作素材'),
   ('4_UNIT 1/3_Meeting 3 homework.html', '全篇', 'chunking 作业、Supercell 两版文本、准备在对话中使用短语、无笔记谈学习'),
   ('5_UNIT 2/1_Meeting 8 homework.html', '全篇', 'Data Centers 阅读（含简化版）、收集词与词块、准备讨论'),
   ('（拓展）', '—', '三档停顿记号、长名词短语从后往前拆、skim/scan 分工、信号词表、三段式发言为教学补充，原文只给任务指令'),
   ('（跳过）', '—', '作业页中的 Padlet、SharePoint、YLE 外链不逐条复述，仅保留其语言任务'))))
# ============================================================ 3
LEC.append(L(
 slug='l3-vocabulary-grammar-clinic',
 tzh='第 3 讲 · 词汇与语法诊所',
 ten='Vocabulary and Grammar Clinic',
 keywords=['collocation', 'uncountable noun', 'word family', 'word order', 'frequency adverb', 'indirect question', 'question tag', 'preposition'],
 files=['4_UNIT 1 Building Know-how_8_Food material.html',
        '4_UNIT 1 Building Know-how_6_EXERCISE Computers  Phones.html',
        '4_UNIT 1 Building Know-how_7_Meeting 5 homework.html',
        '4_UNIT 1 Building Know-how_9_Meeting 7 homework.html',
        '5_UNIT 2 Expressing Opinions_5_GRAMMAR Online Exercises.html',
        '5_UNIT 2 Expressing Opinions_6_Meeting 11 homework.html'],
 overview=(h2('本节定位')
  + p('第 3 讲把课程里分散在三处的语言训练合并成一套系统：<b>主题词汇</b>（食物与厨具、电脑与手机部件、专业词表）、<b>构词与词族</b>、<b>语法诊所</b>（词序、否定、频率副词、四类问句、介词 at/in/on）。课程把它们放在 Meeting 5 至 Meeting 11 的作业里循环出现，说明它们是「必须形成习惯」而不是「知道就行」的内容。')
  + p('为什么合并成一讲：词汇和语法在产出时是同一条流水线——选词错了是搭配问题，句子排错了是词序问题，介词用错了往往两者都是。把三件事一起练，才能在口语里一次到位。')
  + p('学完本讲你应当能够：')
  + ck('按「认识—搭配—产出」三层管理主题词汇，并自建 glossary',
     '正确使用食物与厨具词汇，区分可数与不可数、选择量词',
     '用 24 个烹饪动词描述流程，搭配不错',
     '说出电脑与手机主要部件的英文名，并用 8 个常用搭配描述故障',
     '用词族表扩展专业词汇，判断前缀的含义',
     '按 S–V–O–M–P–T 排出正确词序，放对频率副词与否定词',
     '构造 Yes/No、wh-、间接问句与反意疑问句四类问句',
     '按时间、地点、抽象搭配三条线选对 at/in/on')),
 detail=(h3('3.1 词汇的三层与 glossary 模板')
  + p('一个词真正属于你，要经过三层：<b>recognition</b>（看到能懂）、<b>collocation</b>（知道它和谁连用）、<b>production</b>（自己能用对）。课程里反复出现的 <i>Collect words and chunks</i> 与 <i>Complete the document with vocabulary from field-specific exercise</i> 就是在逼你从第一层走到第三层。')
  + p('glossary 建议用五列，一次课新增 5 至 8 条，考前直接复习这张表：')
  + tb(('English', '音标 / 词性', '中文', '搭配', '自造句'),
       ('plug', '/plʌɡ/ n.', '插头', 'a loose plug, the wrong type of plug', 'The plug is the wrong type.'),
       ('wiring', '/ˈwaɪərɪŋ/ n. 不可数', '布线', 'check the wiring, faulty wiring', 'Mona checked the wiring manually.'),
       ('standstill', '/ˈstændstɪl/ n.', '停机', 'come to a standstill, a production standstill', 'When is a standstill possible?'),
       ('subcontractor', '/ˌsʌbkənˈtræktə/ n.', '分包商', 'call a subcontractor, a local subcontractor', 'I’ll call our subcontractor immediately.'))
  + h3('3.2 食物与厨具：可数性决定量词')
  + p('课程的食物材料分六组图片：蔬菜（33 张）、谷物豆类与坚果（33 张）、水果与浆果（45 张）、动物制品与替代品（33 张）、厨具（33 张）、烹饪动词（24 张），另有一组「菜肴」词表与四个 Cambridge／Moodle 小测。背单词表之前先解决一个语法前提：<b>可数还是不可数</b>。')
  + tb(('类别', '不可数（不加 -s）', '可数（可加 -s）', '量词示范'),
       ('主食', 'bread, rice, pasta, flour', 'a loaf, a roll, a slice', 'two slices of bread, a bowl of rice'),
       ('乳制品', 'milk, cheese, butter, yoghurt', 'a cheese（一种奶酪）', 'a glass of milk, a piece of cheese'),
       ('肉与鱼', 'beef, pork, chicken（肉）, fish（肉）', 'a chicken（一只鸡）, two fish（两条鱼）', 'a kilo of beef, a fillet of fish'),
       ('蔬果', '—（多数可数）', 'an onion, two carrots, a cucumber', 'a head of lettuce, a clove of garlic'),
       ('调味', 'salt, pepper, sugar, oil', '—', 'a pinch of salt, a tablespoon of oil'))
  + cal('warn', '中式高频错误', '<i>a bread</i>、<i>some breads</i>、<i>many rices</i> 都错。bread 与 rice 不可数，要说 <i>a slice of bread</i>、<i>a bowl of rice</i>。反过来 <i>a vegetable</i> 是对的，蔬菜可数。')
  + h3('3.3 24 个烹饪动词：动作要分得清')
  + p('烹饪动词是最容易被「一个 cook 走天下」毁掉的词群。按动作类型分组记，比按字母背有效：')
  + tb(('动作类型', '动词', '典型搭配', '易混点'),
       ('切', 'chop, slice, dice, mince, grate', 'chop an onion, slice the bread, dice the carrots, mince the garlic, grate the cheese', 'chop 粗切、dice 切丁、mince 切末'),
       ('去皮与分份', 'peel, core, deseed', 'peel the potatoes, core the apple', 'peel 只用于皮'),
       ('混合', 'stir, whisk, blend, knead', 'stir the sauce, whisk the eggs, blend the soup, knead the dough', 'whisk 打蛋／奶油，knead 揉面'),
       ('加热', 'boil, simmer, steam, fry, deep-fry, sauté, roast, bake, grill', 'boil the pasta, simmer the sauce, steam the fish, fry an egg, roast the vegetables, bake a cake, grill the chicken', 'bake 只用于烤箱（面包、蛋糕），roast 用于肉与蔬菜'),
       ('调味与处理', 'season, marinate, drain, mash, pour', 'season with salt, marinate the meat, drain the pasta, mash the potatoes', 'season 用调料，marinate 需时间'))
  + p('流程描述示范：<i>First, peel the potatoes and dice them. Then boil them for about fifteen minutes, drain them, and mash them with butter and a pinch of salt.</i> 注意每个动作都用<b>一般现在时祈使句或顺序副词</b>（first、then、after that、finally），这是食谱与工艺说明的通用语体。')
  + cal('warn', '搭配错误', '<i>cook the bread</i> 应为 <i>bake the bread</i>；<i>boil the egg in oil</i> 逻辑不通（水煮用 water，煎用 fry）；<i>make a cake</i> 口语可以，但书面流程用 <i>bake a cake</i> 更准确。')
  + h3('3.4 电脑与手机：部件与故障表达')
  + p('Meeting 5 的选做练习给两条线：电脑（Quizlet 部件图 + GeeksforGeeks 组件文章）或手机（维修参考图 + 移动网络原理）。两条线共享同一批高频搭配，掌握 16 个就够描述日常故障。')
  + tb(('部件', '英文', '常见搭配 / 故障句'),
       ('主板', 'motherboard', 'The motherboard is faulty.'),
       ('处理器', 'processor / CPU', 'The CPU overheats under load.'),
       ('内存', 'memory / RAM', 'The laptop needs more RAM.'),
       ('硬盘 / 固态盘', 'hard drive / SSD', 'The hard drive crashed and I lost the files.'),
       ('电源', 'power supply / charger', 'The power supply failed. / Plug in the charger.'),
       ('显卡', 'graphics card', 'The graphics card is not detected.'),
       ('散热风扇', 'cooling fan', 'The cooling fan is noisy.'),
       ('接口', 'port / USB port', 'The USB port is loose.'),
       ('屏幕', 'screen / display', 'The screen is cracked.'),
       ('电池', 'battery', 'The battery runs out quickly. / I need to recharge.'),
       ('SIM 卡槽', 'SIM tray', 'Insert the SIM tray with the pin.'),
       ('话筒与扬声器', 'microphone / speaker', 'The microphone is muted.'))
  + p('八个万能动词搭配：<i>install / update / uninstall software</i>、<i>plug in</i>、<i>charge</i>、<i>reboot</i>、<i>freeze</i>、<i>crash</i>、<i>run out of battery</i>、<i>back up files</i>。句法上注意：<i>crash</i> 与 <i>freeze</i> 是不及物动词（<i>The app crashed.</i>），不要写成 <i>I crashed the app</i>（那是「我把它弄崩了」）。')
  + p('复合名词的重音落在<b>第一个成分</b>：<i>ˈmotherboard</i>、<i>ˈhard drive</i>、<i>ˈpower supply</i>、<i>ˈUSB port</i>、<i>ˈcooling fan</i>。重音放错会让听者以为是两个词（<i>hard</i> + <i>drive</i>）。')
  + h3('3.5 词族与构词：一个词变四个')
  + p('专业词汇量不是靠背单词表堆出来的，而是靠词族（word family）扩展。看到一个新词，同时记它的名词、动词、形容词、副词形式：')
  + tb(('动词', '名词（动作）', '名词（人或物）', '形容词'),
       ('produce', 'production', 'product / producer', 'productive'),
       ('install', 'installation', 'installer', 'installed'),
       ('connect', 'connection', 'connector', 'connected'),
       ('consume', 'consumption', 'consumer', 'consumable'),
       ('maintain', 'maintenance', 'maintainer', 'maintainable'),
       ('apply', 'application', 'applicant / appliance', 'applicable'))
  + p('前缀决定方向：<i>re-</i>（再次：rebuild、reconnect）、<i>un-</i>（否定：unplug、unsafe）、<i>over-</i>（过度：overheat、overload）、<i>under-</i>（不足：undersized、underestimate）、<i>sub-</i>（下级：subcontractor、subsystem）。这些前缀在课程语料里都出现过，属高频。')
  + cal('tip', '一词四用', '把 <i>maintain</i> 写成一句话：<i>Regular maintenance keeps the system maintainable and reduces production downtime.</i> 一句话里用三个词族成员，比背四个释义牢固。')
  + h3('3.6 专业词表：从对话里取词')
  + p('Meeting 5 的作业要求 <i>Complete the document with vocabulary from field-specific exercise</i>：从你另一门专业课（物理、数学等）的习题里挑一道，把其中的术语、动词与句式抄进共享词表。Meeting 7 又要求把这些词用进一个自制小测（Chinese food quiz，2 至 4 题，选项式，链接贴到 Padlet）。')
  + p('这意味着词表不是「词典摘抄」，而是<b>从真实任务里长出来的</b>。示范一条来自课程对话的词条：')
  + tb(('术语', '中文', '搭配', '例句'),
       ('cross connection', '交叉连接', 'the cross connection room', 'They found the cross connection room on the second floor.'),
       ('spare part', '备件', 'carry spare parts, order a spare part', 'I have the necessary spare parts with me.'),
       ('technician', '技术员', 'send a technician, a service technician', 'I’ll ask them to send a technician.'),
       ('comply with', '符合', 'comply with the standard / the regulation', 'The plug does not comply with the standard.'))
  + h3('3.7 词序：S–V–O–M–P–T')
  + p('英语陈述句的基本顺序是「主语—谓语—宾语」，状语按 <b>方式（Manner）—地点（Place）—时间（Time）</b> 排列，简称 M–P–T。中文习惯「时间—地点—动作」，正好相反，这是词序错误的最大来源。')
  + tb(('错误', '正确', '规则'),
       ('I went yesterday by bus to Helsinki.', 'I went to Helsinki by bus yesterday.', '地点先于时间；方式先于地点'),
       ('He works in the lab carefully.', 'He works carefully in the lab.', '方式先于地点'),
       ('We discussed in the meeting the problem.', 'We discussed the problem in the meeting.', '宾语紧跟动词，不被状语切开'),
       ('Every day I usually check the log.', 'I usually check the log every day.', '频率副词在主谓之间，时间状语可句末'))
  + p('频率副词（always, usually, often, sometimes, seldom, never）的位置有两条硬规则：<b>实义动词前</b>（<i>I usually check …</i>）、<b>be 动词后</b>（<i>He is always late.</i>）。有助动词时夹在助动词与主要动词之间：<i>I have never seen this error before.</i>')
  + p('否定句的构成也遵循同一逻辑：有助动词就在助动词后加 not（<i>It does not comply with the standard.</i>），没有就借 do/does/did（<i>We did not find any loose connections.</i>）。一般过去时的否定用 did + 原形，不要写成 <i>did not found</i>。')
  + cal('warn', '否定 + 频率副词', '<i>I don’t usually work on Saturdays.</i> 正确语序是「助动词 + not + 频率副词 + 动词」。写成 <i>I usually don’t work …</i> 语法可接受但语意不同（强调「通常不」而非「不常」）；写成 <i>I don’t work usually …</i> 则不合习惯。')
  + h3('3.8 四类问句，一套判断流程')
  + p('课程在 Meeting 5 与 Meeting 7 连续布置了九组词序练习，覆盖陈述句、否定句、Wh- 问句、Yes/No 问句、间接问句与反意疑问句。它们的构造可以用一张流程走完：')
  + tb(('类型', '结构', '例', '要点'),
       ('Yes/No 问句', '助动词／be／情态 + 主语 + 主动词', 'Does the plug comply with the standard?', '主动词回原形'),
       ('Wh- 问句', '疑问词 + 助动词 + 主语 + 主动词', 'When is a standstill possible?', '疑问词本身作主语时不再借 do'),
       ('主语提问', 'Who / What + 谓语（第三人称单数）', 'Who called the supplier?', '不说 Who did call …'),
       ('间接问句', '引导句 + 陈述语序', 'Could you tell me where the port is?', '不倒装，句末不用问号（若主句是陈述）'),
       ('反意疑问句', '陈述 + 简短反问（前肯后否）', 'It doesn’t comply, does it?', '助动词与主语要与前半句一致'))
  + p('间接问句是最容易错的一类，因为学习者会把直接问句的倒装照搬进去：<i>Could you tell me where is the port?</i> 错，应为 <i>where the port is</i>。同理 <i>Do you know when does the meeting start?</i> 应为 <i>when the meeting starts</i>。')
  + p('反意疑问句的四条特殊规则：<i>I am …</i> 的反问是 <i>aren’t I</i>；<i>Let’s …</i> 用 <i>shall we</i>；祈使句用 <i>will you</i>；含 never、hardly、nothing 等否定词的前半句视为否定，反问用肯定（<i>He never comes late, does he?</i>）。')
  + p('语调也参与意义：反问句用<b>降调</b>表示「我确信，你同意吧」；用<b>升调</b>表示「我真的在问」。这一点与本课程朗读测试的语调要求直接相连。')
  + h3('3.9 介词 at / in / on：三条线各管一段')
  + p('课程给了五组介词练习（at/in/on 的句子填空、时间表达、混合练习、Moodle 练习）。归纳成三条线就够用：')
  + tb(('线', 'at（点）', 'in（范围／容器）', 'on（面／接触）'),
       ('时间', 'at 8 o’clock, at noon, at night, at Christmas', 'in July, in 2023, in the morning, in two hours', 'on Monday, on 5 May, on Monday morning'),
       ('地点', 'at the station, at the office, at the top', 'in Finland, in the room, in the cabinet', 'on the table, on the wall, on the second floor'),
       ('抽象与固定搭配', 'at risk, at least, good at, arrive at（小地点）', 'in charge of, interested in, arrive in（城市／国家）, involved in', 'on purpose, depend on, based on, focused on'))
  + p('还有一批高频动词搭配必须整块记，因为它们不服从上面任何一条线：<i>comply with</i>、<i>substitute A for B</i>、<i>replace A with B</i>、<i>responsible for</i>、<i>depend on</i>、<i>consist of</i>、<i>result in</i>、<i>prevent from</i>。')
  + cal('warn', '七个必错介词', '① <i>in Monday</i> → on Monday；② <i>at 2023</i> → in 2023；③ <i>on the morning</i> → in the morning；④ <i>arrive to Helsinki</i> → arrive in Helsinki（小地点用 at）；⑤ <i>discuss about the problem</i> → discuss the problem；⑥ <i>comply to the standard</i> → comply with；⑦ <i>interested of</i> → interested in。')
  + h3('3.10 产出前的两张检查卡')
  + p('写任何句子（作业稿、幻灯片、邮件）之前，用两张卡快速过一遍：<b>词序卡</b>（主语在不在最前、状语是否 M–P–T、宾语有没有被状语切开、频率副词位置）与<b>介词卡</b>（时间用 at/in/on 哪条线、动词固定搭配是什么、可数性是否需要量词）。这两张卡覆盖了本课程语法作业里的绝大部分考点。')),
 kws=K(('collocation', '搭配', 'Words that naturally go together: heavy rain, not strong rain.'),
       ('uncountable noun', '不可数名词', 'Bread and rice take no plural and no a/an.'),
       ('quantifier', '量词', 'a slice of bread, a pinch of salt, a clove of garlic.'),
       ('word family', '词族', 'produce, production, product, productive.'),
       ('prefix', '前缀', 're-, un-, over-, under-, sub- change the meaning of a word.'),
       ('word order', '词序', 'English follows subject–verb–object, then manner–place–time.'),
       ('frequency adverb', '频率副词', 'Always, usually and never go before the main verb, after be.'),
       ('indirect question', '间接问句', 'Could you tell me where the port is? — no inversion.'),
       ('question tag', '反意疑问句', 'It doesn’t comply, does it?'),
       ('preposition of time', '时间介词', 'at 8, in July, on Monday.'),
       ('comply with', '符合', 'All plugs must comply with the standard.'),
       ('substitute A for B', '用 A 替换 B', 'We substituted the old plugs for the new type.'),
       ('plug in', '插上电源', 'Plug in the charger before you start.'),
       ('run out of battery', '电量耗尽', 'My phone ran out of battery during the meeting.'),
       ('standstill', '停机', 'When is a standstill possible?'),
       ('season with', '用……调味', 'Season the soup with salt and pepper.')),
 examples=(Q('例 1　改正下列句子的词序，并说明依据：',
   p('A. <i>I checked yesterday the wiring in the cabinet carefully.</i>')
   + p('B. <i>He always is late for the morning meeting.</i>')
   + p('C. <i>We didn’t found any loose connection.</i>') +
   p('<b>解：</b>A 有三处问题。宾语 <i>the wiring</i> 被时间状语切开，应紧跟动词；状语顺序应为方式—地点—时间。改为 <i>I checked the wiring in the cabinet carefully yesterday.</i>') +
   p('B 是 be 动词与频率副词位置错：频率副词在 be 之后，改为 <i>He is always late for the morning meeting.</i>') +
   p('C 是过去时否定的形式错：did 已承担时态，主动词回原形，改为 <i>We didn’t find any loose connection.</i> 另外 any 用于否定句与疑问句，正确。') +
   p('<b>通用思路：</b>先定位谓语 → 把宾语贴回谓语后 → 状语按 M–P–T 排 → 最后查频率副词与助动词后的动词形式。'))
  + Q('例 2　把下列直接问句改为间接问句（用 <i>Could you tell me …</i> 开头）：',
   p('A. <i>Where is the cross connection room?</i>　B. <i>When does the meeting start?</i>　C. <i>Does the plug comply with the standard?</i>') +
   p('<b>解：</b>三步：保留疑问词 → 去掉倒装、改回陈述语序 → 调整时态与人称（主句为现在时则不用改时态）。') +
   p('A → <i>Could you tell me where the cross connection room is?</i>（is 移到主语后）。') +
   p('B → <i>Could you tell me when the meeting starts?</i>（does 消失，动词恢复第三人称单数 -s）。') +
   p('C 没有疑问词，用 if／whether：<i>Could you tell me if the plug complies with the standard?</i>（同样恢复 -s）。') +
   p('<b>通用思路：</b>疑问词照抄 → 助动词删掉、主动词还原 → 主语提前到动词前 → 主句过去时则整体后移一个时态。'))
  + Q('例 3　补全反意疑问句并说明该用升调还是降调：',
   p('A. <i>The plugs are the wrong type, ______?</i>　B. <i>You haven’t called the supplier yet, ______?</i>　C. <i>Let’s check the wiring again, ______?</i>') +
   p('<b>解：</b>A 前半句肯定（are），反问用否定，助动词与主语一致：<i>aren’t they?</i> 说话人已看到实物、只是寻求确认，用<b>降调</b>。') +
   p('B 前半句有否定词 haven’t，反问用肯定：<i>have you?</i> 若真的在询问对方是否已联系，用<b>升调</b>；若只是寒暄式确认，用降调。') +
   p('C Let’s 的特殊反问是 <i>shall we?</i>，固定搭配，用降调。') +
   p('<b>通用思路：</b>看前半句肯定／否定（含 never、hardly、nothing 视为否定）→ 取同一助动词与代词 → 前肯后否、前否后肯 → 最后按「真问用升、求确认用降」定调。'))
  + Q('例 4　填入 at / in / on，并说明理由：',
   p('① The meeting starts ______ 8:15 ______ Friday morning.　② The spare parts are ______ the cabinet.　③ We arrived ______ Helsinki ______ 2023.　④ The technician is good ______ troubleshooting.　⑤ The report is based ______ last year’s data.') +
   p('<b>解：</b>① <i>at 8:15</i>（钟点是 at）＋ <i>on Friday morning</i>（具体某天的上午用 on，不用 in）。') +
   p('② <i>in the cabinet</i>：柜子是一个三维容器，用 in。③ <i>arrived in Helsinki</i>（城市用 in）＋ <i>in 2023</i>（年份用 in）。') +
   p('④ <i>good at</i>：能力形容词的固定搭配。⑤ <i>based on</i>：抽象依据用 on。') +
   p('<b>通用思路：</b>先判「点／范围／面」→ 再看是不是固定搭配（good at、based on、responsible for）→ 固定搭配优先于三条线规则。'))),
 practice=(ol('把下列不可数名词组成正确的量词短语：bread（两片）、rice（一碗）、salt（一撮）、garlic（一瓣）、oil（一勺）。',
         '用 first／then／after that／finally 写一段 5 句的煮意面流程，至少用 5 个烹饪动词。',
         '改正词序：<i>She explained in the meeting the procedure clearly.</i> / <i>I have never seen this error before yesterday.</i> / <i>Why you didn’t call the technician?</i>',
         '把 <i>Do you know what is the standstill time?</i> 改为正确间接问句，并说明改动理由。',
         '填介词并说明：<i>responsible ___ / interested ___ / comply ___ / substitute the old plug ___ a new one / arrive ___ Lappeenranta</i>。',
         '给你的专业词表新增 3 条（术语、搭配、例句），并各造一句与自己项目有关的句子。')
  + D('答案与思路' +
   p('<b>1.</b> two slices of bread / a bowl of rice / a pinch of salt / a clove of garlic / a tablespoon of oil。规则：不可数名词靠「容器 + of」计量，量词本身可数（two slices、two cloves）。') +
   p('<b>2.</b> 参考：<i>First, boil a large pot of water. Then add the pasta and simmer for about ten minutes. After that, drain it and pour the sauce over it. Finally, season with salt and grate some cheese on top.</i> 五个动词：boil、simmer、drain、pour、grate；另加 season。') +
   p('<b>3.</b> <i>She explained the procedure clearly in the meeting.</i>（宾语紧跟动词，方式在地点前）；<i>I had never seen this error before yesterday.</i>（before yesterday 指过去某一时点之前，用过去完成时）；<i>Why didn’t you call the technician?</i>（Wh- 问句：疑问词 + 助动词 + 主语）。') +
   p('<b>4.</b> <i>Do you know what the standstill time is?</i> 间接问句用陈述语序，is 移到主语后；主句为一般现在时，从句时态不变。') +
   p('<b>5.</b> responsible <b>for</b>；interested <b>in</b>；comply <b>with</b>；substitute the old plug <b>for</b> a new one（substitute A for B）；arrive <b>in</b> Lappeenranta（城市）。') +
   p('<b>6.</b> 参考三条：<i>voltage</i> /ˈvəʊltɪdʒ/ 电压，搭配 measure the voltage，例 <i>Measure the voltage across the resistor.</i>；<i>torque</i> /tɔːk/ 扭矩，搭配 apply torque，例 <i>Apply a torque of 20 Nm to the bolt.</i>；<i>tolerance</i> /ˈtɒlərəns/ 公差，搭配 within tolerance，例 <i>The diameter must be within tolerance.</i>'))),
 exam=(cal('exam', '必考', '词序 M–P–T 与频率副词位置；四类问句的构造（含间接问句不倒装）；反意疑问句的四条特殊规则；at/in/on 三条线；comply with 与 substitute A for B 两个高频搭配。')
  + cal('warn', '易错 1', '间接问句照搬倒装：<i>Could you tell me where is the port?</i> 必须改为 <i>where the port is</i>。')
  + cal('warn', '易错 2', '过去时否定写 <i>didn’t found</i>；频率副词放在 be 前 <i>He always is late</i>。')
  + cal('warn', '易错 3', '可数性判断错导致 a bread／many rices；介词搭配错导致 comply to、substitute with、discuss about。')
  + cal('tip', '进阶', '把介词与词族一起记成「一句话模板」：<i>All components must comply with the standard, and any faulty part should be substituted for a certified one.</i> 一句里同时练两个搭配与被动语态。')),
 checklist=(h2('本讲方法清单')
  + h3('句子产出四步检查（词序 + 介词 + 可数 + 时态）')
  + ck('主语与谓语是否相邻，宾语有没有被状语切开',
     '状语是否按方式—地点—时间排列，频率副词是否在主谓之间（be 之后）',
     '名词可数性是否影响冠词与量词，动词搭配的介词是否背对',
     '否定与问句里助动词是否已承担时态，主动词是否回原形')
  + h3('问句生成流程')
  + st('判断是 Yes/No 还是 Wh-，需不需要疑问词',
       '找助动词／be／情态；没有就按人称借 do／does／did',
       '主动词还原，主语回到动词前（间接问句用陈述语序）',
       '反意疑问句取同一助动词，前肯后否，最后定升调或降调')
  + h3('词汇入库')
  + ck('五列词卡（英文、音标词性、中文、搭配、自造句）一次写全', '每课新增 5 至 8 条并复习旧条目', '每条词卡至少朗读三遍，确认重音位置')),
 mapping=tb(('源文件', '位置 / 页码', '覆盖内容'),
   ('4_UNIT 1/8_Food material.html', '全篇', '蔬菜、谷物豆类坚果、水果浆果、动物制品、厨具、烹饪动词六组图词表；菜肴词表；四个小测'),
   ('4_UNIT 1/6_EXERCISE Computers  Phones.html', '全篇', '电脑部件、手机部件与移动网络的选做阅读'),
   ('4_UNIT 1/7_Meeting 5 homework.html', '全篇', 'CEE 练习、专业词表文档、九组词序语法练习'),
   ('4_UNIT 1/9_Meeting 7 homework.html', '全篇', '同一组九项语法练习 + 自制中国食物小测（2 至 4 题、贴 Padlet）'),
   ('5_UNIT 2/5_GRAMMAR Online Exercises.html', '全篇', 'at/in/on 句子填空与时间表达两组练习'),
   ('5_UNIT 2/6_Meeting 11 homework.html', '全篇', '介词混合、时间介词与 Moodle 介词练习'),
   ('（拓展）', '—', '可数性分组表、烹饪动词动作分类、复合名词重音、词族与前缀表、间接问句与反意疑问句特殊规则为教学补充'),
   ('（跳过）', '—', 'Padlet、Quizlet、Cambridge、GeeksforGeeks 等外链只保留其词汇任务，不逐条复述'))))
# ============================================================ 4
LEC.append(L(
 slug='l4-elevator-pitch',
 tzh='第 4 讲 · 电梯演讲：60 秒说清你是谁',
 ten='The 60-Second Elevator Pitch',
 keywords=['elevator pitch', 'unique value', 'audience alignment', 'hook', 'call to action', 'speech rate', 'pronunciation clarity', 'body language'],
 files=['3_Assignments_2_ASSIGNMENT 1 Elevator Pitch [DL Nov 5]_intro_intro.html',
        '5_UNIT 2 Expressing Opinions_1_Meeting 8 homework.html',
        '5_UNIT 2 Expressing Opinions_3_Meeting 9 homework.html',
        '5_UNIT 2 Expressing Opinions_6_Meeting 11 homework.html'],
 overview=(h2('本节定位')
  + p('第 4 讲是 Unit 2 Expressing Opinions 的第一个产出任务：<b>60 秒电梯演讲</b>（elevator pitch），先写稿、再练、在 Meeting 11 现场录制。它把前三讲的能力第一次压缩成一个成品：自我介绍的语篇（第 1 讲）、说清楚的停顿与重音（第 2 讲）、准确的词序与搭配（第 3 讲）。')
  + p('课程对它的定义值得抄下来：<i>An elevator pitch is a professional summary or introduction to who you are and the value you can potentially bring to a company.</i> 并特别指出，芬兰的面试常以 <i>Tell us about yourself</i> 开场，电梯演讲就是这道题的标准答案。')
  + p('学完本讲你应当能够：')
  + ck('用七个规划问题把经历整理成「技能—热情—独特价值」三条线索',
     '按「钩子—身份—证据—价值—差异—行动邀请」六段结构写出 130 至 150 词稿',
     '把空洞的形容词句改写为带证据的具体句',
     '按 130 至 150 词／分钟估算时长并留出停顿余量',
     '用录音自评三项：清晰度、语速、难发音词',
     '面对镜头完成 60 秒演讲，保持眼神接触与面部表情',
     '判断哪些 AI 用法被允许、哪些属于「代写稿件」的禁区')),
 detail=(h3('4.1 任务与评分：三个维度、一条硬线')
  + p('作业说明的第一句就把场景钉死了：<i>This assignment requires you to create and present a 60-second elevator pitch. You prepare your pitch in advance and you deliver it live during Meeting 11.</i> 也就是说稿子可以提前写好、练熟，但交付是<b>现场录制</b>，不能剪辑补救。')
  + p('三个评分维度：<b>language</b>（语法的正确性与表达的自然度）、<b>content</b>（是否使用了电梯演讲的结构）、<b>audience</b>（眼神、面部表情等肢体语言，以及与目标听众的匹配度）。三者权重相当，这意味着「稿子写得好」只能拿到三分之一。')
  + cal('exam', '计分换算', '0 至 49.99 Fail (revise)；50 至 59.99 Passable (1)；60 至 69.99 Satisfactory (2)；70 至 79.99 Good (3)；80 至 89.99 Very Good (4)；90 至 100 Excellent (5)。三个维度任一出现明显缺陷（如全程低头读稿），就很难进入 4 级以上。')
  + h3('4.2 三个阶段：Planning / Preparing / Presenting')
  + p('作业把流程明确分成三段，每段都有可检查的产出物。照着做，准备过程本身就是一个可复用的方法：')
  + tb(('阶段', '作业要求', '你要产出的东西'),
       ('1. Planning', '用思维导图或笔记回答七个问题；决定听众是谁；读老师给的电梯演讲材料（Meeting 8 slides 15–21）；写稿', '一张思维导图 + 一份 130 至 150 词稿'),
       ('2. Preparing', '大声读稿练习；录音并回听；分析自己是否清晰、过快、不自然，哪些词难说', '一份自评笔记（3 条问题 + 对应改法）'),
       ('3. Presenting', '课上录视频，约 60 秒，提交到 Moodle', '一个不剪辑的视频文件或链接'))
  + p('七个规划问题原文如下，它们不是写作提示，而是<b>内容清单</b>：<i>Who are you? What do you study? What professional experiences do you have? Why is what you do important for them? Why are you passionate about this? What makes you stand out? Why should someone employ you?</i>')
  + p('注意第四、第七个问题都指向<b>对方</b>（them、someone）。这是电梯演讲与自我介绍的分水岭：自我介绍以「我」为中心，电梯演讲必须回答「这对你有什么用」。')
  + h3('4.3 六段结构：60 秒的分配方案')
  + p('把七个问题压进 60 秒，需要一个明确的结构。下面这套六段式在 130 至 150 词内可以稳定跑完，每段都有时间预算：')
  + tb(('段落', '时长', '功能', '句式模板'),
       ('① 钩子', '5 秒', '一句让人抬头的话', 'Most people don’t realise that … / I build systems that …'),
       ('② 身份', '8 秒', '姓名、专业、学校', 'I’m … , a third-year … student at LUT.'),
       ('③ 证据', '15 秒', '一段具体经历 + 一个数字', 'Last summer I interned at … , where I … , which cut … by 20%.'),
       ('④ 价值', '15 秒', '你能为对方解决什么', 'What I can offer your team is … / I help companies … by …'),
       ('⑤ 差异', '10 秒', '你和别人的不同', 'What sets me apart is …'),
       ('⑥ 行动邀请', '7 秒', '给对方一个下一步', 'I’d be glad to show you … / I’d love to hear how your team …'))
  + p('合起来 60 秒。注意③④两段占一半时间——这是刻意的：<b>证据与价值才是听众真正在听的部分</b>，钩子只负责让人愿意听下去。')
  + cal('warn', '结构失衡', '初学者常把 40 秒花在②身份上（学校、城市、课程名），最后 10 秒才慌忙说「我很努力」。评分表里 content 一项考的是 <i>use of elevator pitch structure</i>，身份信息超过三句就是结构分丢失。')
  + h3('4.4 语速与字数：60 秒到底多少词')
  + p('自然英语演讲语速约 130 至 150 词／分钟，折算每秒 2.2 至 2.5 词。60 秒的理想稿长是 <b>130 至 150 词</b>；若含 3 次明显停顿与 2 次强调，实际能装进去的内容约 120 至 140 词。')
  + p('算法：词数 ÷ 语速 = 分钟数。例如 140 词 ÷ 145 词／分钟 ≈ 0.97 分钟，接近 58 秒，正好留 2 秒开场呼吸。若你的稿子是 200 词，除以 145 得 1.38 分钟——超时 23 秒，必须删掉整整一段。')
  + p('删减优先级：先删身份细节（课程名、城市），再删形容词（hard-working、passionate 单独出现时没有信息量），最后才动证据句。证据句是唯一不能删的部分。')
  + h3('4.5 把形容词换成证据：六组改写')
  + p('电梯演讲最常见的失分点是「形容词堆砌」。形容词不可验证，证据可验证。下面六组对照可以直接套用：')
  + tb(('空洞表达', '改写为证据句', '改写理由'),
       ('I’m hard-working.', 'I worked 20 hours a week in a lab while taking five courses, and still finished the project on schedule.', '用具体工时与结果替代评价'),
       ('I’m good at teamwork.', 'In our capstone project I coordinated a team of four and set up the weekly task board.', '用角色与动作说明「团队」'),
       ('I’m passionate about engineering.', 'I’ve been rebuilding small engines since I was fifteen, and I now volunteer at a repair café.', '用时间跨度与持续行动证明热情'),
       ('I have good communication skills.', 'I presented our prototype to twelve industry visitors and wrote the two-page summary afterwards.', '用场景与听众规模说话'),
       ('I’m a fast learner.', 'I taught myself Python in one semester to automate our measurement reports.', '用自学路径与用途说明'),
       ('I want to work for you.', 'I’d like to bring my test-automation experience to your production line team.', '把「想要」换成「能带来什么」'))
  + cal('tip', '一个数字胜过三个形容词', '60 秒里最多放两个数字（如 20%、4 人、2 个月），多了听众记不住。数字要能一句话说清来源：<i>which cut our setup time by about a third</i>。')
  + h3('4.6 语言：时态、动词与礼貌强度')
  + p('电梯演讲只用三种时态，混用会立刻显得不专业：<b>一般现在时</b>说身份与能力（<i>I’m a third-year student. I work with embedded systems.</i>）；<b>一般过去时</b>说具体经历（<i>Last summer I interned at …</i>）；<b>现在完成时</b>说持续至今的积累（<i>I’ve worked with CAD for three years.</i>）。')
  + p('动词要选有力度的实义动词，避免 <i>do、make、get、have</i> 万能化：用 <i>designed、built、tested、cut、reduced、coordinated、automated</i> 替代。同一句话对比：<i>I did a project about automation</i>（弱）→ <i>I automated the test sequence for a small production line</i>（强）。')
  + p('礼貌强度也要拿捏。请求式表达用 <i>I’d be glad to … / I’d love to hear …</i>；不要用 <i>I want you to give me a chance</i>（听起来像要求）。自我评价用 <i>I’d describe myself as …</i> 比 <i>I am …</i> 更稳。')
  + cal('warn', '固定搭配错误', '<i>apply for a job</i>（不是 apply a job）；<i>be interested in working</i>（不是 interested to work）；<i>two years of experience</i>（不是 two years experience）；<i>responsible for</i>（不是 responsible of）；<i>good at + V-ing</i>（不是 good in）。这五个错在 pitch 里一出现，language 一项就掉档。')
  + h3('4.7 准备阶段：录音自评的三个问题')
  + p('作业在 Preparing 阶段给了三个自评问题，照抄如下：<i>are you speaking clearly, too fast, too unnaturally? Are some words difficult to say? Which words?</i> 这三个问题对应三种不同的修正手段：')
  + ul('<b>清晰度</b>不足 → 问题多在词尾与辅音群（<i>texts</i> /teksts/、<i>asked</i> /ɑːskt/），做法是把难词单独抄出来，慢速读十遍再放回句子。',
       '<b>语速</b>过快 → 用第 2 讲的停顿记号在稿子上标竖线，每 8 至 10 词一个短停，强迫自己减速。',
       '<b>不自然</b> → 多半是背稿腔：句子太长、书面语太重。把 <i>Furthermore, I would like to emphasise that …</i> 改成 <i>What I really enjoy is …</i>。')
  + p('难发音词是个人化的清单，但中国学习者的高频难词有共性：<i>three</i> /θriː/、<i>technology</i> /tekˈnɒlədʒi/、<i>southern</i> /ˈsʌðən/、<i>engineering</i> /ˌendʒɪˈnɪərɪŋ/、<i>analysis</i> /əˈnæləsɪs/、<i>entrepreneur</i> /ˌɒntrəprəˈnɜː/。把重音位置标在稿子上（大写重读音节），比反复整句念更有效。')
  + h3('4.8 Presenting：镜头前的三个技术点')
  + p('第一，<b>看镜头不看屏幕</b>。摄像头就是听众的眼睛，眼神飘向自己的画面会让 audience 一项直接失分。第二，<b>站姿与手</b>：手在胸前小幅度动作即可，不要抱臂或插兜。第三，<b>开头与结尾各留半秒静默</b>，让听者有时间进入与收尾——这半秒是「从容」与「慌张」的分界。')
  + p('现场录制还有一个现实约束：<i>Please bring your phone to class to record yourself.</i> 手机录制意味着没有提词器，所以稿子必须练到「只靠六个关键词就能说」的程度。练习方法：把稿子压缩成六张关键词卡，遮住稿子只说关键词，说不下去再看一眼。')
  + h3('4.9 AI 边界：可以当教练，不能当作者')
  + p('这项作业的 AI 规则是三份作业里最宽松也最清楚的一份：允许 <i>creating an example pitch to use as inspiration</i>、<i>language guidance</i>、<i>checking your final product for errors</i>；禁止 <i>writing a script for the pitch completely or partially</i>。')
  + p('分界线画在「文本的作者是谁」。让 AI 给三个开头句作参考、让它挑出你稿子里的介词错误，这是教练；让它写一段你直接照读，这是作者。作业原文还补了一句：<i>you are supposed to be the author of the text that you upload</i>。')),
 kws=K(('elevator pitch', '电梯演讲', 'A 60-second professional summary of who you are and the value you bring.'),
       ('unique value', '独特价值', 'What you can offer that others cannot.'),
       ('audience alignment', '听众匹配', 'Adapting your pitch to the company or team in front of you.'),
       ('hook', '钩子', 'The first sentence that makes people want to listen.'),
       ('call to action', '行动邀请', 'The last sentence that suggests the next step.'),
       ('speech rate', '语速', 'About 130–150 words per minute in natural speech.'),
       ('proof point', '证据点', 'A concrete experience or number that supports a claim.'),
       ('stand out', '脱颖而出', 'What makes you stand out from other candidates?'),
       ('passionate about', '对……充满热情', 'I’m passionate about building things that work reliably.'),
       ('internship', '实习', 'Last summer I interned at a manufacturing company.'),
       ('apply for', '申请', 'I decided to apply for this programme.'),
       ('two years of experience', '两年经验', 'I have two years of experience in test automation.'),
       ('responsible for', '负责', 'I was responsible for the weekly test report.'),
       ('eye contact', '眼神接触', 'Keep eye contact with the camera lens, not the screen.'),
       ('body language', '肢体语言', 'Body language is one third of the assessment.'),
       ('author of the text', '文本作者', 'You are supposed to be the author of the text you upload.')),
 examples=(Q('例 1　你写了一份 186 词的稿子，按 145 词／分钟计算时长，并给出删减到 60 秒的方案。' +
   p('<b>解：</b>第一步算时长：186 ÷ 145 ≈ 1.28 分钟 ≈ 77 秒，超时 17 秒。') +
   p('第二步定删减量：要回到 58 秒（留 2 秒呼吸），目标词数 = 145 × 0.97 ≈ 140 词，需删 46 词。') +
   p('第三步按优先级删：身份段里的 <i>which is a city in central China</i>（7 词）、课程名与年级细节（约 12 词）、两个形容词句 <i>I am hard-working and passionate</i>（9 词）、钩子里的一句铺垫（约 18 词），合计 46 词。') +
   p('第四步复核：保留钩子、证据、价值、差异、行动邀请五段完整，只压缩身份段。') +
   p('<b>通用思路：</b>先算总时长 → 定目标词数 → 按「形容词→身份细节→铺垫→证据」的顺序删 → 保证证据与价值两段完整。'))
  + Q('例 2　把 <i>I am a hard-working student and I have good teamwork skills. I want to work in your company.</i> 改写为有证据的版本。' +
   p('<b>解：</b>原句三处问题：形容词不可验证（hard-working、good）；teamwork 没有场景；<i>want to work in your company</i> 以自我为中心。') +
   p('改写：<i>In our capstone project I coordinated a team of four and set up a weekly task board, which kept us on schedule. I’d like to bring that way of working to your production team.</i>') +
   p('改动清单：形容词 → 角色与动作（coordinated a team of four）；skills → 具体工具（a weekly task board）；结果（kept us on schedule）；结尾从「我想要」变成「我能带来」。') +
   p('<b>通用思路：</b>每个形容词问一句「凭什么」→ 找到那件事 → 补角色、动作、结果 → 结尾指向对方。'))
  + Q('例 3　诊断下面这段 pitch 缺了哪两段，并各补一句：',
   p('<i>Hi, I’m Pauli Salo. I’m a third-year electrical engineering student at LUT. I study power systems and I have taken courses in automation and control. I’m also interested in data centres. I hope to find a summer job.</i>') +
   p('<b>解：</b>六段里只有①钩子（其实也没有钩子，只是问候）与②身份，缺<b>③证据</b>、<b>④价值</b>、<b>⑤差异</b>，⑥行动邀请也太弱（<i>I hope to find a summer job</i> 是在陈述愿望，不是给对方下一步）。') +
   p('补③证据：<i>Last spring I built a small monitoring setup for a lab test bench, which cut manual logging time by half.</i>') +
   p('补④价值：<i>What I can offer your team is hands-on experience with measurement and reporting tools.</i>') +
   p('补⑤差异：<i>What sets me apart is that I’ve worked both on the hardware side and on the data side of the same project.</i>') +
   p('<b>通用思路：</b>用六段表逐段打勾，空白处就是缺内容；每补一段只写一句，先保证结构齐，再打磨语言。'))
  + Q('例 4　改错并说明规则：<i>I am graduated from LUT last year. I have two years experience in a lab, and I am good in teamwork. I am interested to work in your company.</i>' +
   p('<b>解：</b>四处错误。① <i>am graduated</i> → <i>graduated</i>：graduate 是不及物动词，完成时用 have graduated，过去时直接用 graduated；若尚未毕业则 <i>I’m a final-year student</i>。') +
   p('② <i>two years experience</i> → <i>two years of experience</i>：数量短语修饰不可数名词要加 of。') +
   p('③ <i>good in teamwork</i> → <i>good at working in a team</i>：能力形容词用 at + V-ing；teamwork 本身可作名词，但 <i>good at teamwork</i> 略显生硬。') +
   p('④ <i>interested to work</i> → <i>interested in working</i>：interested 固定接 in + V-ing。') +
   p('<b>通用思路：</b>这四个错分别是「动词及物性、数量短语、形容词介词、固定搭配」，属于必须先背下来的高频条目，考场上没有推理空间。'))),
 practice=(ol('把下面五个规划问题的答案各写成一句英文（每句不超过 20 词）：你是谁、你学什么、你有什么专业经历、你能为对方做什么、你为什么对这个领域有热情。',
         '用六段结构写一份 140 词的 pitch 稿，并给每段标上预估秒数，合计不超过 60 秒。',
         '改写为证据句：<i>I’m a fast learner.</i> / <i>I have strong problem-solving skills.</i>',
         '给下列句子标出重读音节与两处停顿：<i>What I can offer your team is hands-on experience with test automation.</i>',
         '判断下列 AI 用法是否被本作业允许，并说明理由：① 让 AI 生成一份示例 pitch 作参考；② 让 AI 把你的中文草稿译成英文当稿子；③ 让 AI 找出你稿子里的介词错误。')
  + D('答案与思路' +
   p('<b>1.</b> 参考：<i>I’m Pauli Salo, an electrical engineering student from Finland.</i> / <i>I’m in my third year, focusing on power systems and automation.</i> / <i>Last summer I interned at a substation maintenance team.</i> / <i>I can help your team turn measurement data into clear reports.</i> / <i>I enjoy this field because every fault has a traceable cause.</i>') +
   p('<b>2.</b> 参考稿（138 词，标注秒数）：钩子 5 秒 <i>Most power cuts start with one loose connection.</i>｜身份 8 秒 <i>I’m Pauli Salo, a third-year electrical engineering student at LUT.</i>｜证据 15 秒 <i>Last summer I interned at a substation team, where I logged and analysed 60 fault reports.</i>｜价值 15 秒 <i>What I can offer is a habit of tracing faults to their source instead of replacing parts.</i>｜差异 10 秒 <i>What sets me apart is that I have worked both in the field and with the data afterwards.</i>｜邀请 7 秒 <i>I’d be glad to show you how I structured those reports.</i>') +
   p('<b>3.</b> <i>I’m a fast learner</i> → <i>I taught myself Python in one semester to automate our weekly measurement reports.</i>；<i>I have strong problem-solving skills</i> → <i>When our test bench kept overheating, I traced it to a blocked filter and redesigned the airflow.</i>') +
   p('<b>4.</b> 重读：<b>OFF</b>er、<b>TEAM</b>、<b>HANDS</b>-on、<b>EX</b>perience、<b>TEST</b>、<b>AU</b>tomation。停顿：<i>What I can offer your team | is hands-on experience | with test automation.</i> 三块，每块 3 至 5 词。') +
   p('<b>5.</b> ① 允许：作业明确列出 <i>creating an example pitch to use as inspiration</i>。② 不允许：译文当稿子等于让 AI 写稿，属于 <i>writing a script completely or partially</i>。③ 允许：属于 <i>checking your final product for errors</i>，但改完必须自己判断是否接受。'))),
 exam=(cal('exam', '必考', '六段结构与 60 秒时间分配；130 至 150 词／分钟的换算；三个评分维度（language / content / audience）；七个规划问题；AI 允许与禁止的边界。')
  + cal('warn', '易错 1', '身份段过长，挤掉证据与价值；结尾用 <i>I hope to …</i> 代替行动邀请。')
  + cal('warn', '易错 2', '形容词堆砌（hard-working、passionate）而无证据；时态混用（<i>I am graduated</i>、<i>I am studying here since</i>）。')
  + cal('warn', '易错 3', '固定搭配：apply for、interested in + V-ing、two years of experience、good at、responsible for。')
  + cal('tip', '进阶', '把差异段写成「两种经验的交叉」而不是「我更努力」：<i>I’ve worked both in the field and with the data afterwards</i> 比任何形容词都更能让人记住。')),
 checklist=(h2('本讲方法清单')
  + h3('60 秒 pitch 五步准备法')
  + st('回答七个规划问题，每个答案压成一句，写成思维导图',
       '按六段结构排句，标出每段秒数，总时长不超过 60 秒',
       '算词数：目标 130 至 150 词，超了就按「形容词→身份细节→铺垫」删',
       '大声读三遍并录音，按「清晰度／语速／不自然」三项自评，标出难词',
       '缩成六张关键词卡，遮稿练习到只靠关键词能说完，再录正式版')
  + h3('镜头前交付检查')
  + ck('眼睛看镜头而不是屏幕，开头结尾各留半秒静默',
     '手在胸前小幅度动作，不抱臂、不插兜',
     '每段第一个词重读，段间停顿 0.5 秒',
     '难词已标重音并单独练过十遍',
     '稿子是自己写的：AI 只用于示例、语言指导与查错')),
 mapping=tb(('源文件', '位置 / 页码', '覆盖内容'),
   ('3_Assignments/2_ASSIGNMENT 1 Elevator Pitch [DL Nov 5]/intro/intro.html', '全篇', '定义与使用场景、三个 AIM、三阶段流程、七个规划问题、时长与提交要求、0–100 评分表与三个评分维度、AI 规则'),
   ('3_Assignments_2_ASSIGNMENT 1 Elevator Pitch [DL Nov 5]_Submissions_Zishuo Wang_Online text.html', '全篇', '学生提交的 YouTube 链接，仅作提交格式示例'),
   ('5_UNIT 2/1_Meeting 8 homework.html', '全篇', '开始构思稿子：你想在职业层面说什么；并指向 Meeting 8 slides 15–21 的 pitch 材料'),
   ('5_UNIT 2/3_Meeting 9 homework.html', '全篇', '完成稿子、按 slides 33–37 练习、下次课内完成作业'),
   ('5_UNIT 2/6_Meeting 11 homework.html', '全篇', '课上录制后上传 Moodle 返交框、分享链接的技术说明'),
   ('（拓展）', '—', '六段结构与秒数分配、130 至 150 词／分钟换算、六组形容词改写、镜头前三个技术点为教学补充'),
   ('（跳过）', '—', 'slides 15–21 与 33–37 的原始幻灯片不在源文本中，仅按作业描述转述其用途'))))
# ============================================================ 5
LEC.append(L(
 slug='l5-presentation-data',
 tzh='第 5 讲 · 工程演讲与图表描述',
 ten='Technical Presentations and Describing Graphs',
 keywords=['credible source', 'signposting', 'breakout room', 'trend verb', 'percentage point', 'visual design', 'fluency', 'pronunciation test'],
 files=['3_Assignments_4_ASSIGNMENT 3 Presentation [DL Nov 27]_intro_intro.html',
        '5_UNIT 2 Expressing Opinions_3_Meeting 9 homework.html',
        '5_UNIT 2 Expressing Opinions_8_Meeting 12 homework.html',
        '4_UNIT 1 Building Know-how_5_Meeting 5 homework.html',
        '4_UNIT 1 Building Know-how_2_Meeting 2 homework.html'],
 overview=(h2('本节定位')
  + p('第 5 讲对应 Assignment 3：3 至 4 分钟的工程主题演讲，在最后一次网课的 breakout room 里向 3 至 5 人小组交付，并为老师录制。它同时并入了两条支线：Meeting 9 的<b>图表描述</b>（British Council B1 材料 + 小游戏）与 Meeting 12 的<b>朗读测试</b>准备（11 月 18 日，Moodle 10:00–22:00）。')
  + p('与前几讲的关系：第 4 讲练「60 秒说服」，本讲练「4 分钟讲清一件事」；第 2 讲的分块与停顿、第 3 讲的词序与搭配在这里被同时调用，评分表也第一次把 fluency、vocabulary、pronunciation、grammar 四项并列。')
  + p('学完本讲你应当能够：')
  + ck('判断一个来源是否属于课程认可的可信来源，并说明理由',
     '在 3 至 4 分钟里安排 400 至 520 词的内容，分配开场、主体、结尾的时间',
     '用 first、second、finally、moving on 等路标语组织演讲',
     '用趋势动词、副词与四类句式准确描述一张折线图或柱状图',
     '区分 increase by 与 increase to、percent 与 percentage point',
     '为一页幻灯片做减法：一个信息点、清晰的层级、标注来源',
     '用绕口令与最小对立对练发音，完成朗读测试的考前准备',
     '在 breakout room 里交付并录制，用 Zoom 桌面端而不是手机或浏览器')),
 detail=(h3('5.1 任务与评分：五项并列')
  + p('作业要求可以拆成五步：选一个与未来专业相关的工程主题（公司、技术、产品、流程、发明、创新均可）→ 找来源且必须在演讲中提及 → 做 3 至 4 分钟的演讲 → 加视觉材料（PowerPoint 可以，但不必须是；Canva 等自由选择）→ 在最后一次网课（11 月 27 日）的 breakout room 里向 3 至 5 人小组演讲，同时为老师录制。')
  + p('评分维度有五项，原文列出：<i>overall impression (content, sources, visuals)</i>、<i>fluency</i>、<i>vocabulary</i>、<i>pronunciation</i>、<i>grammar</i>。注意第一项是<b>整体印象</b>，它把内容、来源、视觉三者打包评价——这意味着「资料找得对、幻灯片做得清楚」本身就能拿分。')
  + cal('exam', '计分换算', '与电梯演讲同一套：0 至 49.99 Fail (revise)，50 至 59.99 Passable (1)，60 至 69.99 Satisfactory (2)，70 至 79.99 Good (3)，80 至 89.99 Very Good (4)，90 至 100 Excellent (5)。')
  + h3('5.2 选源：什么样的来源算可信')
  + p('作业对来源的限制非常具体，这是本讲最容易被忽略却最容易丢分的部分：<i>Credible sources include research articles, reports, and government/organization websites. Do not use commercial websites, blogs, news articles, or wikis.</i>')
  + tb(('来源', '可用？', '理由'),
       ('研究论文（期刊、会议论文）', '可用', '有同行评审，方法与数据可追溯'),
       ('机构或政府报告（能源署、统计局、标准组织）', '可用', '署名机构、有统计口径与年份'),
       ('大学或实验室官网的技术说明', '可用', '属 organization website，作者与日期明确'),
       ('企业产品页 / 营销页面', '不可用', '商业网站，数据为营销目的服务'),
       ('个人博客、Medium 专栏', '不可用', '无审稿，作者资质不明'),
       ('新闻文章（含英文新闻网站）', '不可用', '二次转述，常缺方法与口径'),
       ('维基百科等 wiki', '不可用', '多人协作、随时改动，不能作为引用来源'))
  + p('判断一个来源能不能用，问三个问题：<b>谁写的</b>（署名机构还是匿名）、<b>数据从哪来</b>（原始统计还是转述）、<b>有没有日期与口径</b>（年份、样本、单位）。三问有一问答不上来，就换一个来源。')
  + cal('warn', '常见误区', '新闻网站上的「某研究称……」不能当来源——你要引的是那项研究本身。反过来，研究论文里引用的政府统计数据，可以直接去政府网站找原始表格。')
  + h3('5.3 3 至 4 分钟装多少内容')
  + p('按 130 至 150 词／分钟计算，3 分钟约 390 至 450 词，4 分钟约 520 至 600 词。留出幻灯片切换与两次停顿，安全区间是 <b>400 至 520 词</b>。超过 550 词几乎必然超时，因为切换幻灯片时语流会中断。')
  + tb(('段落', '3 分钟版', '4 分钟版', '内容'),
       ('开场', '25 秒', '35 秒', '钩子 + 主题 + 路线图（今天讲三点）'),
       ('主体一', '50 秒', '65 秒', '背景与问题：为什么这件事值得讲'),
       ('主体二', '55 秒', '75 秒', '技术核心：原理、流程或数据'),
       ('主体三', '40 秒', '55 秒', '影响与限制：成本、风险、前景'),
       ('结尾', '20 秒', '30 秒', '总结一句 + 行动邀请 + 提问'))
  + p('这个分配有一个纪律：<b>主体三点、每点一句主张</b>。三点讲不透，不如两点讲透。作业评分看的是整体印象与流利度，不是信息量。')
  + h3('5.4 路标语：让听众知道你在哪')
  + p('演讲的流利不等于语速快，而是<b>结构可预测</b>。路标语（signposting）就是给听众的路牌，每一句都在告诉他「现在到哪了、接下来去哪」：')
  + tb(('功能', '句型', '使用时机'),
       ('开场与路线图', 'Today I’ll cover three points: first … , then … , and finally … .', '第一页幻灯片'),
       ('开始第一点', 'Let’s start with the background.', '进入主体'),
       ('切换', 'That brings me to my second point.', '换页时，代替「接下来」'),
       ('举例', 'A good example of this is … .', '需要具体化时'),
       ('强调', 'What matters here is … .', '核心数据前后'),
       ('收束', 'So, to sum up, … .', '最后一张幻灯片'),
       ('邀请提问', 'I’m happy to take any questions.', '结尾'))
  + p('这些句子还有一个副作用：它们给你<b>换气的时机</b>。每切换一次就有一个自然停顿，语速会自动稳定下来。')
  + h3('5.5 一页幻灯片只讲一件事')
  + p('作业只要求 <i>Add some visuals</i>，没有规定版式，但评分维度里的 visuals 决定了你需要遵守几条基本纪律：')
  + ck('一页一个信息点：标题就是这一页的结论，不是「结果」这样的空标题',
     '文字不超过六行，每行不超过八个词；讲稿放在你嘴里，不放在屏幕上',
     '图表大于文字：能用一张图说清的，不要用三行 bullet',
     '层级清楚：标题最大，数据次之，来源最小但必须有',
     '来源标注格式统一：机构名 + 年份，写在页面底部')
  + p('来源标注不是形式主义。作业要求 <i>Find sources on the topic (must be mentioned)</i>——「提及」既包括口头说 <i>according to a 2023 report by …</i>，也包括幻灯片上的一行小字。两者都做最稳。')
  + h3('5.6 图表描述：三类词、四类句式')
  + p('Meeting 9 的作业给了两条训练：一个 learningapps 上的图表词小游戏，以及 British Council B1 的 <i>describing charts</i> 阅读加三个任务。核心是把「趋势」拆成<b>方向、幅度、时间</b>三个变量。')
  + tb(('方向', '动词', '名词形式'),
       ('上升', 'rise, increase, grow, climb, go up', 'an increase, a rise, growth'),
       ('下降', 'fall, decline, decrease, drop, go down', 'a fall, a decline, a decrease'),
       ('平稳', 'remain stable, stay steady, level off, plateau', 'stability, a plateau'),
       ('波动', 'fluctuate, vary', 'fluctuation'),
       ('峰值与低谷', 'peak, reach a peak, hit a low, bottom out', 'a peak, a low'))
  + tb(('幅度副词', '含义', '例'),
       ('sharply / dramatically / steeply', '急剧', 'Sales rose sharply from 20 to 45 units.'),
       ('significantly', '显著（可用于统计语境）', 'Energy use increased significantly after 2020.'),
       ('steadily / gradually', '稳定、渐进', 'The share grew steadily over five years.'),
       ('slightly / marginally', '轻微', 'Costs fell slightly in the second quarter.'))
  + p('四类句式覆盖绝大多数图表句：')
  + ul('<b>动词句</b>：<i>Sales rose from 20 to 45 units between January and March.</i>（from A to B 表区间）',
       '<b>名词句</b>：<i>There was a sharp increase in sales in the first quarter.</i>（there was + a + 形容词 + 名词 + in）',
       '<b>状态句</b>：<i>The figure stood at 12% at the end of the year.</i>（stood at 表某时点的值）',
       '<b>占比句</b>：<i>Wind power accounted for 30% of the total.</i>（account for 表占比）')
  + cal('warn', '四个数字陷阱', '① <i>increased by 20%</i> 是「增长了 20%」，<i>increased to 20%</i> 是「增长到 20%」；② <i>percent</i> 与 <i>percentage point</i> 不能混用：两个百分比之差用 <b>percentage points</b>（从 10% 到 13% 是上升 3 个百分点，不是 3%）；③ <i>the number of + 复数名词</i> 用单数谓语（<i>the number of units was</i>），<i>a number of + 复数名词</i> 用复数谓语；④ <i>amount</i> 配不可数（amount of energy），<i>number</i> 配可数（number of units）。')
  + h3('5.7 图表描述的三段式')
  + p('一段好的图表描述不是流水账，而是「引入—描述—解读」三步。以作业要求「找一个有意思的图，准备介绍并讨论」为例：')
  + p('<b>引入</b>：<i>This chart shows the share of renewable electricity in Finland from 2010 to 2023.</i>（说明图讲什么、时间范围、单位）。')
  + p('<b>描述</b>：<i>It rose steadily from about 25% to just over 40%, with a sharp increase after 2019.</i>（方向 + 幅度 + 转折点）。')
  + p('<b>解读</b>：<i>What stands out is that most of the growth came after 2019, which suggests that policy changes had an effect.</i>（一句结论 + 一句谨慎的原因，避免把相关当因果）。')
  + cal('tip', '解读要留余地', '用 <i>which suggests that …</i>、<i>this may be because …</i>，不要用 <i>this proves …</i>。图表只能显示相关，不能证明因果。')
  + h3('5.8 交付：breakout room 与 Zoom 录制')
  + p('交付方式有两个技术约束，每年都有人在这里丢分：演讲在 <b>breakout room（3 至 5 人）</b>进行，并且必须<b>为老师录制</b>；录制要求用 <b>Zoom 电脑应用程序</b>加入会议，因为 <i>recording does not work on phone/tablet or in browser version</i>。')
  + st('提前用电脑端 Zoom 加入测试会议，确认本地录制可用',
       '把幻灯片存成 PDF 备份，避免字体或动画在共享时出错',
       '在 breakout room 里先报主题与时长，再开始讲',
       '讲完把录制文件上传云端并生成公开链接，课后提交到返交框')
  + h3('5.9 发音与流利度：朗读测试的考前准备')
  + p('Assignment 2 的朗读测试在 11 月 18 日，Moodle 当天 10:00 至 22:00 开放，范围是<b>课上练过的材料</b>，官方建议用 recap material 加 Padlet 上的句子复习。评分表里的 pronunciation 与 fluency 两项，也在此处被直接检验。')
  + p('Meeting 5 的作业要求在家练绕口令（tongue twisters），这是最省时的发音热身：')
  + ul('<i>She sells seashells by the seashore.</i>　练 /ʃ/ 与 /s/ 的切换，注意 <i>seashells</i> 中间不停。',
       '<i>Peter Piper picked a peck of pickled peppers.</i>　练 /p/ 的送气与连续爆破。',
       '<i>Red lorry, yellow lorry.</i>　练 /r/ 与 /l/，以及 /e/ 与 /əʊ/ 的区别。',
       '<i>Three thin thieves thought a thousand thoughts.</i>　练 /θ/ 与 /ð/ 的舌尖位置。')
  + p('练习方法不是「念快」，而是<b>三档速度</b>：慢速（每词清楚）→ 中速（连成块）→ 常速（只保证每块清楚，块内可含糊）。三档都过，才算练成。录音对比时只听一个音，不要一次听全部。')
  + h3('5.10 AI 规则与作者身份')
  + p('本作业允许 AI 做四件事：<i>brainstorming</i>、<i>help in the information search (double check AI sources!)</i>、<i>summarizing information</i>、<i>creating visuals</i>；禁止两件事：<i>writing a script for the presentation</i> 与 <i>producing any material (other than visuals)</i>。')
  + p('注意 <i>double check AI sources</i> 这个括号：AI 给的来源链接经常不存在或与内容不符，而本作业明确要求来源可信。凡是 AI 提供的文献，必须自己打开原文核对作者、年份与数据。')),
 kws=K(('credible source', '可信来源', 'Research articles, reports and government websites are acceptable.'),
       ('commercial website', '商业网站', 'Product pages cannot be used as sources in this assignment.'),
       ('signposting', '路标语', 'Today I’ll cover three points … helps listeners follow you.'),
       ('breakout room', '分组讨论室', 'You will present in breakout rooms of three to five people.'),
       ('trend verb', '趋势动词', 'rise, fall, level off, peak, fluctuate.'),
       ('percentage point', '百分点', 'A change from 10% to 13% is three percentage points.'),
       ('account for', '占（比例）', 'Wind power accounted for 30% of the total.'),
       ('stand at', '处于（某数值）', 'The figure stood at 12% at the end of the year.'),
       ('fluency', '流利度', 'One of the five criteria in the presentation assessment.'),
       ('overall impression', '整体印象', 'Content, sources and visuals are judged together.'),
       ('visual', '视觉材料', 'A visual can be a slide, a chart or a short clip.'),
       ('tongue twister', '绕口令', 'She sells seashells by the seashore.'),
       ('minimal pair', '最小对立对', 'ship / sheep differ in one vowel sound only.'),
       ('recap material', '复习材料', 'Use the recap material and the Padlet sentences before the test.'),
       ('local recording', '本地录制', 'Zoom recording only works in the desktop application.'),
       ('double check', '复核', 'Double check AI sources before you cite them.')),
 examples=(Q('例 1　改错并说明规则：<i>Sales increased with 20% from 20 to 45 units. The number of customers were higher in March.</i>' +
   p('<b>解：</b>第一处 <i>increased with 20%</i> 介词错：幅度用 by，<i>increased by 20%</i>。若要表达区间用 from … to …：<i>Sales increased from 20 to 45 units.</i>') +
   p('第二处 <i>The number of customers were</i> 主谓不一致：<i>the number of</i> 的中心词是 number，单数，改为 <i>was</i>。若写 <i>A number of customers were</i>（许多顾客）才用复数。') +
   p('第三处隐含问题：<i>increased by 20%</i> 与 <i>from 20 to 45</i> 同时出现会自相矛盾（从 20 到 45 是增长 125%）。二者只能选一个口径。') +
   p('<b>通用思路：</b>先定口径（幅度／区间／终值）→ 选对应介词（by／from…to／to）→ 再查 the number of 的主谓一致。'))
  + Q('例 2　用三句话描述这张图（2010 至 2023 年芬兰可再生能源电力占比：25% → 40%，2019 年后急升），并按「引入—描述—解读」标注。' +
   p('<b>解：</b>引入：<i>This chart shows the share of renewable electricity in Finland between 2010 and 2023.</i>') +
   p('描述：<i>The share rose steadily from about 25% to just over 40%, with a sharp increase after 2019.</i>（from … to … 表区间，steadily 表幅度，after 2019 标转折点）。') +
   p('解读：<i>What stands out is that most of the growth came after 2019, which suggests that policy changes played a role.</i>（what stands out 引出结论，which suggests 留余地）。') +
   p('<b>通用思路：</b>一句说明图是什么 → 一句说方向、幅度、转折 → 一句给谨慎的解读；三句之内不要出现两个以上数字口径。'))
  + Q('例 3　你要做 3 分 30 秒的演讲，写稿时该定多少词？给出分段字数与页数建议。' +
   p('<b>解：</b>3.5 分钟 × 140 词／分钟 ≈ 490 词，取整 480 词（留切换与停顿余量）。') +
   p('分段：开场 30 秒 70 词；主体一 55 秒 128 词；主体二 60 秒 140 词；主体三 50 秒 116 词；结尾 25 秒 58 词。合计 3 分 40 秒、512 词，略超，可把主体二压到 130 词。') +
   p('页数：开场 1 页、主体 3 页（每点一页）、结尾 1 页，共 5 页；每页平均停留 40 秒，正好够讲清楚一个信息点。') +
   p('<b>通用思路：</b>先定总时长 → 乘 140 得词数 → 按段落比例分配 → 页数等于段落数（一点一页），最后按实际朗读复测一次。'))
  + Q('例 4　判断下列来源可否用于本作业，并说明理由：① 某风电企业官网的技术页面；② 国际能源署（IEA）2024 年报告；③ 维基百科「Wind power」条目；④ 期刊论文《Nordic wind power integration》。' +
   p('<b>解：</b>① 不可用：商业网站（commercial website），数据服务于营销。② 可用：机构报告（organization report），有署名、年份与统计口径。③ 不可用：wiki，多人协作且随时改动，只能用来找线索，不能作引用来源。④ 可用：研究论文（research article），有同行评审与方法说明。') +
   p('补充做法：从③找到它引用的①与④，再回到原始来源核对数据——这正是 <i>double check</i> 的实际操作。') +
   p('<b>通用思路：</b>三问定生死——谁写的、数据从哪来、有没有年份与口径；三问全过才引用。'))),
 practice=(ol('把下列句子改成语义准确的图表句：<i>The price increased to 15%.</i> / <i>Production was raised with 200 units.</i> / <i>The amount of factories grew.</i>',
         '用「引入—描述—解读」三句描述一张你熟悉的图（可用课程作业里的能耗或产量数据），并标注每句的功能。',
         '写一份 3 分钟演讲的开场 30 秒（约 70 词），必须包含钩子、主题与三点路线图。',
         '把下面这段路标语补齐：<i>Today I’ll cover three points. ______ , the background. ______ , the technology itself. And ______ , what it means for Finland.</i>',
         '判断四个来源能否引用并写一句理由：政府统计年鉴、企业产品手册、大学实验室技术报告、个人技术博客。',
         '给 <i>She sells seashells by the seashore</i> 设计三档速度的练习方案，并说明每档要检查什么。')
  + D('答案与思路' +
   p('<b>1.</b> <i>The price rose by 15%.</i>（若原意是「涨到 15% 这个水平」则用 <i>rose to 15%</i>，但价格通常用幅度）；<i>Production was raised by 200 units.</i>；<i>The number of factories grew.</i>（factory 可数，用 number 不用 amount）。') +
   p('<b>2.</b> 参考：引入 <i>This chart shows electricity consumption per capita in Finland from 2015 to 2023.</i>／描述 <i>It stayed almost flat until 2020 and then fell slightly, from about 15 MWh to 14 MWh.</i>／解读 <i>What stands out is how stable consumption has been, which may reflect efficiency gains offsetting new demand.</i>') +
   p('<b>3.</b> 参考（72 词）：<i>Every winter, Finland burns more energy than it can store. I’m going to talk about one technology that changes that: large-scale heat storage. Today I’ll cover three points — first, why storage matters; then, how the technology works; and finally, what it could mean for Finnish industry.</i> 含钩子、主题、三点路线图。') +
   p('<b>4.</b> <i>First</i>／<i>Second</i>／<i>finally</i>（或 <i>To begin with</i>／<i>Next</i>／<i>And finally</i>）。注意 first 与 second 后接逗号，finally 前用 and 更自然。') +
   p('<b>5.</b> 政府统计年鉴：可用（政府网站 + 原始统计）；企业产品手册：不可用（商业网站）；大学实验室技术报告：可用（organization 的技术文档，署名与日期清楚）；个人技术博客：不可用（blog，无审稿）。') +
   p('<b>6.</b> 慢速：每词清楚，重点查 /s/ 与 /ʃ/ 是否分清（seashells 里两个音相邻）；中速：块内连读，<i>sells seashells</i> 不停；常速：只保证 <i>she / sells / seashells / seashore</i> 四个重读词清楚，块内可含糊。每档录 10 秒对比。'))),
 exam=(cal('exam', '必考', '可信来源的四类与四类禁用；3 至 4 分钟对应 400 至 520 词；路标语七种功能；图表四类句式与四个数字陷阱；五项评分维度；Zoom 桌面端录制限制；朗读测试的时间与范围。')
  + cal('warn', '易错 1', 'increase by 与 increase to 混用；percent 与 percentage point 混用；the number of 后接复数谓语。')
  + cal('warn', '易错 2', '把新闻文章或维基当来源；幻灯片堆满文字、无来源标注。')
  + cal('warn', '易错 3', '用手机或浏览器版 Zoom 录制，结果没有文件——这是纯技术性丢分，完全可避免。')
  + cal('tip', '进阶', '图表解读句加一层限定：<i>which suggests that …</i>、<i>although other factors may also be involved</i>，比直接下因果结论更专业，也更难被质疑。')),
 checklist=(h2('本讲方法清单')
  + h3('演讲准备五步')
  + st('选主题并写一句主张（这次演讲要让人记住哪一件事）',
       '找 3 个可信来源，每个来源记下机构、年份、关键数字',
       '按五段分配秒数与词数，总词数控制在 400 至 520',
       '每段配一页幻灯片，页面只放结论与数据，讲稿留在嘴里',
       '按 130 至 150 词／分钟朗读复测，超时按「例子→背景→细节」顺序删')
  + h3('图表句四查')
  + ck('口径对不对：幅度用 by，区间用 from … to，终值用 to',
     '主谓一致：the number of 单数，a number of 复数',
     '单位与百分比：percent 与 percentage point 不混用',
     '解读留余地：suggests／may，而不是 proves')
  + h3('发音考前热身')
  + ck('四个绕口令各三档速度，每档录 10 秒',
     'Padlet 上的句子逐句朗读，标出难词并单独练',
     '只查一个音（如 /θ/ 或 /ʃ/），不要一次改全部',
     '测试当天提前 10 分钟测试麦克风，10:00 至 22:00 窗口内提交')),
 mapping=tb(('源文件', '位置 / 页码', '覆盖内容'),
   ('3_Assignments/4_ASSIGNMENT 3 Presentation [DL Nov 27]/intro/intro.html', '全篇', '五个 AIM、五步任务、来源限制、视觉要求、breakout room 与 Zoom 录制、0–100 评分与五项维度、AI 规则'),
   ('5_UNIT 2/3_Meeting 9 homework.html', '全篇', '图表描述：learningapps 小游戏、British Council B1 describing charts 阅读与三个任务、找一张有意思的图准备介绍'),
   ('5_UNIT 2/8_Meeting 12 homework.html', '全篇', '朗读测试：11 月 18 日、Moodle 10:00–22:00、范围为课上材料、recap material 与 Padlet 句子'),
   ('4_UNIT 1/5_Meeting 5 homework.html', '全篇', '在家练绕口令'),
   ('4_UNIT 1/2_Meeting 2 homework.html', '全篇', 'Padlet 词表朗读与难读词清单，构成朗读测试的复习范围'),
   ('（拓展）', '—', '五段时间分配表、路标语七种功能、图表四类句式与四个数字陷阱、三档速度练习法为教学补充'),
   ('3_Assignments_3_ASSIGNMENT 2 Pronunciation Test [DL Nov 18]_Submissions_Zishuo Wang_Online text.html', '全篇', '学生提交的朗读测试视频链接，仅作提交格式示例'),
   ('（跳过）', '—', 'H5P 演示材料、learningapps 游戏与 British Council 页面本身不在源文本内，仅按作业描述转述其任务'))))
# ============================================================ 6
LEC.append(L(
 slug='l6-meetings-negotiation',
 tzh='第 6 讲 · 会议沟通、协商与专业简报',
 ten='Meetings, Negotiation and Professional Briefings',
 keywords=['modal verb', 'hedging', 'suggest + clause', 'had better', 'agreeing and disagreeing', 'action point', 'news briefing', 'meeting etiquette'],
 files=['5_UNIT 2 Expressing Opinions_2_DIALOGUE Engineers Meet.html',
        '5_UNIT 2 Expressing Opinions_7_DIALOGUE Looking for the Problem.html',
        '5_UNIT 2 Expressing Opinions_4_EXERCISE Pair work (agreeing and disagreeing).html',
        '6_UNIT 3 Communicating Professionally_1_Meeting 13 homework.html',
        '4_UNIT 1 Building Know-how_4_Meeting 4 homework.html'],
 overview=(h2('本节定位')
  + p('第 6 讲收束整门课：把前五讲的句子能力放进真实工作场景。课程给了两段工程师现场对话（Promentor Protocall 第 4 章与第 7 章）、一个「同意与不同意」的双人练习，以及 Unit 3 的专业简报任务（读一篇 YLE 新闻、做一页幻灯片、用一分钟向小组讲并讨论视觉材料）。')
  + p('这一讲的语言重点不是新语法，而是<b>语用</b>：同一件事用 must、have to、should、had better 说出来，强度和责任归属完全不同；同一句反对，用三步法说出来是协商，直接说出来是冲撞。')
  + p('学完本讲你应当能够：')
  + ck('在会议里介绍第三方、寒暄并自然转入正题',
     '用现在完成进行时与一般过去时分别描述「一直存在的问题」与「刚发生的事件」',
     '用四种句式提出建议，并按 must–have to–should–had better 的强度阶梯选择情态动词',
     '用 hedging 把判断说得可协商：slightly、fairly、probably、I’m afraid',
     '用「承认—缓和—反提」三步法表达不同意',
     '为会议收出明确的行动项（谁、做什么、什么时候）',
     '从一篇新闻做出一页合规幻灯片，并用一分钟讲清它',
     '会前完成麦克风与摄像头检查，避免技术性失分')),
 detail=(h3('6.1 场景与人物：一段真实的现场会议')
  + p('两篇对话的标题分别是 <i>Chapter 4: Looking for the …</i> 与 <i>Chapter 7 – Looking for the Problem</i>，内容完全相同（后者是重复副本）。场景是：三位工程师驱车前往电站，进入交叉连接室（cross connection room），Roy 把来访者介绍给控制室操作员 Mike McGregory。')
  + p('人物与身份的表达值得注意：<i>Mona, Pauli – this is Mike McGregory. He is one of our operators.</i>（介绍第三方用 this is + 全名，再补一句职务）；<i>Mike, this is Mona Valli and Pauli Salo from Online Automation.</i>（用 from + 公司说明来处）；<i>They both come from Finland and Pauli is stationed in Sheffield at the moment.</i>（be stationed in 表派驻）。')
  + p('这套介绍方式有一条隐含的礼貌规则：<b>先介绍客人给主人，再补身份与来处</b>。中文里常先说「这是某某公司的某某」，英文更常见「这位是 X（全名）」+「他来自 Y 公司」。')
  + h3('6.2 寒暄与转场：三句话完成开场')
  + p('对话的开场只有四句，却覆盖了完整的寒暄—转场链条：')
  + tb(('话轮', '原句', '功能'),
       ('主人介绍', 'Mike, this is Mona Valli and Pauli Salo from Online Automation.', '介绍第三方'),
       ('客人回应', 'Nice to meet you both. / Likewise.', '寒暄；Likewise 是「我也一样」的正式说法'),
       ('寒暄', 'Hello, Mike. How are you? / I’m good, thanks.', '礼节性问候，答案要短'),
       ('转场', 'Well, has this error you’ve reported been bothering you lately?', '用 well 缓冲，直接进入问题'))
  + cal('tip', '转场词', '会议里最实用的三个转场词：<i>Well, …</i>（缓冲后进正题）、<i>OK, let me see now.</i>（开始查看／动手）、<i>Right, …</i>（确认信息后推进）。它们不承载信息，但决定了会议听起来是否从容。')
  + h3('6.3 描述问题：两种时态，两种含义')
  + p('Pauli 的第一问是 <i>has this error you’ve reported been bothering you lately?</i> 这是<b>现在完成进行时</b>（have/has been + V-ing），含义是「从过去到现在一直在持续，并且可能还在持续」。用它的理由很充分：故障是反复出现的，不是一次性事件。')
  + p('Mike 的回答一半用完成时、一半用过去时，切换得非常准确：<i>Yes, it has been quite a nuisance. Just 20 minutes ago we had a short interruption.</i> 前一句说「一直是麻烦」（持续状态），后一句说「20 分钟前发生了一次中断」（已结束的具体事件，用一般过去时 + ago）。')
  + tb(('时间表达', '搭配时态', '例'),
       ('lately / recently', '现在完成（进行）时', 'It has been quite a nuisance lately.'),
       ('… ago', '一般过去时', 'We had a short interruption twenty minutes ago.'),
       ('at the moment', '一般现在／进行时', 'Pauli is stationed in Sheffield at the moment.'),
       ('right away', '一般将来或祈使', 'I can’t tell you right away.'),
       ('within the next two weeks', '将来时', 'It should be done within the next two weeks.'),
       ('sooner or later', '将来时（警告）', 'Sooner or later they will cause more trouble.'))
  + cal('warn', '时态错配', '<i>It has been a nuisance twenty minutes ago</i> 是典型错误：有具体过去时间点（ago）就必须用一般过去时。反过来 <i>It was a nuisance lately</i> 也不对，lately 要求完成时。')
  + h3('6.4 提建议的四种句式')
  + p('这段对话是「提建议」的语料库，四种句式各有语用位置：')
  + tb(('句式', '原句', '语法要点'),
       ('suggest + (that) 从句', 'I suggest we have a look at the structure once more.', '从句用原形动词 have；不能写 suggest us to have 或 suggest to have'),
       ('Why don’t we …?', 'Why don’t we drive back to my office right away?', '反问形式表建议，语气最轻，留出对方否决的空间'),
       ('had better + 原形', 'I’d better replace this one at once.', 'had better 隐含「不这么做会有麻烦」，语气比 should 强'),
       ('will have to / must', 'We’ll have to check all the other plugs as well. / the plugs must be changed.', '客观义务与强制要求，用于不可协商的步骤'))
  + p('suggest 的语法是全军覆没区，三条规则记牢：<b>suggest + V-ing</b>（<i>I suggest checking the wiring.</i>）、<b>suggest + (that) + 主语 + 原形</b>（<i>I suggest we check the wiring.</i>）、<b>不能说 suggest sb to do</b>。同族词 recommend 也是如此。')
  + cal('warn', '三个高频错句', '<i>I suggest to check the wiring.</i>（错，改 I suggest checking）／<i>I suggest us to check the wiring.</i>（错，改 I suggest we check）／<i>He suggested me to call the supplier.</i>（错，改 He suggested that I call the supplier）。')
  + h3('6.5 义务与推测：一条强度阶梯')
  + p('会议里最容易失礼的地方，是把「建议」说成「命令」，或把「必须」说成「也许」。下面这条阶梯从强到弱，选错一档就会改变责任归属：')
  + tb(('强度', '表达', '含义与场合'),
       ('最强', 'must / will have to', '规定、安全要求、不可协商：The plugs must be changed.'),
       ('强', 'have to / will need to', '外部条件造成的义务：We’ll have to check all the others.'),
       ('中', 'had better', '隐含后果的劝告：You’d better call the supplier first.'),
       ('中弱', 'should', '预期或建议：It should be fairly easy to detect the address.'),
       ('弱', 'could / might want to', '可选方案：We could ask the subcontractor to send a technician.'))
  + p('推测的表达同样是分层的：<b>should</b> 表「按道理应该」（<i>It should be fairly easy</i>）；<b>can’t</b> 表「逻辑上不可能」（<i>This can’t be right!</i>）；<b>suppose</b> 表「我推测」（<i>I suppose it can’t wait too long?</i>）；<b>no doubt about that</b> 表「毫无疑问」，是强断言，要慎用。')
  + p('注意 <i>I suppose it can’t wait too long?</i> 这句用<b>升调</b>结尾，把陈述变成求确认——这是会议里最实用的软化技巧：把判断包装成问题，对方就能顺势修正而不失面子。')
  + h3('6.6 Hedging：把话说得可协商')
  + p('技术沟通里，把话说满往往不是优点。对话里布满模糊限制语（hedges），每一个都在为「可能判断错」留退路：')
  + ul('<i>slightly different</i>（略有不同）——比 completely different 更准确，也更留余地。',
       '<i>almost exactly like the correct one</i>（几乎一模一样）——先承认相似，再指出差异，逻辑更稳。',
       '<i>fairly easy</i>（相当容易）——降低对方预期，也给自己留时间。',
       '<i>It should be …</i>（按道理应该）——不承诺，只预测。',
       '<i>I’m afraid not.</i>（恐怕不行）——礼貌否定，比直接 No 柔和。',
       '<i>I can’t tell you right away.</i>（我没法马上答复）——拒绝的同时说明限制，而不是拒绝人。')
  + p('hedging 不是含糊，而是<b>精确地表达不确定度</b>。写报告、做汇报时同样适用：<i>The data suggest a link</i> 比 <i>The data prove a link</i> 更专业。')
  + h3('6.7 技术词汇与搭配：把对话读成词表')
  + p('这段对话本身就是一张电气与维护词表。逐条记搭配，比记单词有用：')
  + tb(('词', '中文', '搭配与例句'),
       ('cross connection room', '交叉连接室', 'They found the cross connection room on the ground floor.'),
       ('cabinet', '机柜', 'Mona examined the back of the cabinet.'),
       ('wiring', '布线', 'She checked the wiring manually.'),
       ('loose connection', '松动的连接', 'There is a loose connection here.'),
       ('plug', '插头', 'The plug is the wrong type.'),
       ('spare part', '备件', 'I have the necessary spare parts with me.'),
       ('subcontractor', '分包商', 'I’ll call our subcontractor immediately.'),
       ('technician', '技术员', 'I’ll ask them to send a technician.'),
       ('standstill', '停机', 'When is a standstill possible?'),
       ('foreman', '工长', 'I’ll have to talk to the foremen as well.'),
       ('interruption', '中断', 'We had a short interruption twenty minutes ago.'),
       ('comply with', '符合（标准）', 'It doesn’t comply with the standard either.'),
       ('substitute', '替换', 'They’ll have to be substituted as soon as possible.'),
       ('nuisance', '麻烦事', 'It has been quite a nuisance.'))
  + p('两个动词要分清：<b>replace A with B</b>（用 B 换掉 A）与 <b>substitute A for B</b>（用 A 替换 B）。方向相反，考试常考：<i>We replaced the old plugs with the new type.</i> = <i>We substituted the new type for the old plugs.</i>')
  + h3('6.8 会议推进与行动项')
  + p('对话的后半段是标准的「收行动项」流程，值得整段模仿：')
  + st('<b>排序</b>：First of all, the plugs must be changed.（先做最关键的）',
       '<b>分工</b>：I’ll call our subcontractor immediately. I’ll ask them to send a technician.（will 表当场决定）',
       '<b>确认窗口</b>：Mike, when is a standstill possible?（向能决定的人要时间）',
       '<b>给期限</b>：It should be done within the next two weeks.（给区间而不是精确日期）',
       '<b>收束</b>：Why don’t we drive back to my office right away and make the necessary calls.（把讨论转成行动）')
  + p('语法细节：<i>I’ll call …</i> 用 will 是因为这是<b>当场做出的决定</b>；若早已计划好则用 <i>I’m going to call …</i>。这个区别在会议记录里非常关键——will 表示承诺，going to 表示已定计划。')
  + p('行动项要写清三件事：<b>谁（who）、做什么（what）、什么时候（when）</b>。<i>I’ll call our subcontractor immediately</i> 具备前两项，第三项由 immediately 与后面的 within two weeks 补齐。缺任何一项，会后就会悬空。')
  + h3('6.9 同意与不同意：三步法')
  + p('课程的双人练习（Student A / Student B 材料分开）专门练「同意与不同意」。这类练习的目标不是赢辩论，而是<b>在不破坏关系的前提下推进决策</b>。')
  + tb(('功能', '表达', '强度'),
       ('强同意', 'I couldn’t agree more. / Exactly. / That’s exactly my point.', '强'),
       ('中性同意', 'That’s a good point. / I think so too. / I’d go along with that.', '中'),
       ('部分同意', 'I agree with the first part, but … / That’s true up to a point, although …', '中弱'),
       ('缓和反对', 'I’m not sure I agree. / I see it a bit differently.', '弱'),
       ('明确反对', 'I’m afraid I have to disagree. / I don’t think that would work, because …', '强'))
  + p('不同意最稳的结构是三步：<b>承认（acknowledge）→ 缓和（soften）→ 反提（counter）</b>。示范：')
  + p('<i>I see your point — replacing all the plugs at once would remove the risk. （承认）That said, we can’t afford a full standstill this month. （缓和）What if we start with the three cabinets that failed inspection? （反提）</i>')
  + p('三步法之所以有效：第一步让对方知道你听懂了，第二步把冲突归因于客观条件而不是对方的判断，第三步给出可执行的替代方案。直接把 <i>No, that’s wrong</i> 说出口，讨论就变成了立场之争。')
  + cal('tip', '语调也参与礼貌', '缓和反对时句末略升（<i>I’m not sure I agree?</i>），表示留有余地；强断言句末降调。同一句话，语调不同，听感从「商量」变成「顶撞」。')
  + h3('6.10 专业简报：一分钟讲一页幻灯片')
  + p('Unit 3 的作业是一条完整的简报流水线：从 YLE News 选一篇英文新闻读完 → 做<b>一页</b>幻灯片（PowerPoint 或 Canva）→ 幻灯片必须包含<b>标题、作者、日期</b> → 注意版面视觉 → 提交到返交框 → 下次课在小组里用<b>一分钟</b>讲，之后讨论视觉材料。')
  + p('一分钟的结构与 60 秒电梯演讲同构，只是内容换成「新闻」：<i>This article, published by … on 12 March, reports that … . The key figure is … . What makes it relevant for us is … .</i> 三句：来源与主张、关键数据、与本专业的相关性。')
  + p('版面纪律与第 5 讲一致：一页一个信息点、标题写结论、来源（标题／作者／日期）放在页脚、图表大于文字。作业特别写了 <i>Pay attention to the visual layout of this slide</i>——版式本身是评分对象。')
  + p('「讨论视觉材料」这一步常被忽略，其实有固定句型：<i>The chart on the left shows …</i>、<i>What stands out here is …</i>、<i>The colours make the comparison easy to read, but the axis labels are missing.</i> 最后一句既夸设计又提问题，是讨论可视化时最得体的说法。')
  + h3('6.11 会前准备：技术性失分最不该发生')
  + p('Meeting 4 的作业只有一条：<i>Online meeting (Zoom) on Friday, Sep 25 (8:15AM) — Check your microphone and camera.</i> 这条看似琐碎，却是整门课最实用的提醒：线上会议里，麦克风没声音、摄像头没画面，会让你的所有语言准备归零。')
  + ck('提前 10 分钟进入测试会议，确认麦克风电平有反应',
     '摄像头高度与眼睛齐平，背景干净、光线从前方来',
     '准备耳机，避免回声；关闭手机通知',
     '把幻灯片与讲稿放在同一台设备，另存一份 PDF 备份',
     '录制备份：若课堂录制失败，自己本地也留一份')
  + h3('6.12 六讲回顾')
  + p('把六讲连起来看：第 1 讲解决「敢说、说对自己」，第 2 讲解决「说得清」（分块与朗读），第 3 讲解决「说得准」（词汇、词序、介词），第 4 讲解决「60 秒说服」，第 5 讲解决「4 分钟讲透 + 图表」，第 6 讲解决「和别人一起把事推进」。这五件事合起来，就是这门课名称里的 Professional English。')),
 kws=K(('modal verb', '情态动词', 'must, have to, should and had better express different strengths of obligation.'),
       ('hedging', '模糊限制', 'Slightly, fairly and probably make a claim easier to negotiate.'),
       ('suggest + clause', 'suggest 接从句', 'I suggest we have a look — base verb, no to.'),
       ('had better', '最好（含警告）', 'I’d better replace this one at once.'),
       ('be stationed in', '派驻在', 'Pauli is stationed in Sheffield at the moment.'),
       ('likewise', '同样；我也一样', 'Nice to meet you. — Likewise.'),
       ('loose connection', '松动的连接', 'There is a loose connection here.'),
       ('comply with', '符合', 'The plug does not comply with the standard.'),
       ('substitute A for B', '用 A 替换 B', 'The new type was substituted for the old plugs.'),
       ('standstill', '停机', 'When is a standstill possible?'),
       ('action point', '行动项', 'Every action point needs a who, a what and a when.'),
       ('acknowledge–soften–counter', '承认—缓和—反提', 'A three-step way to disagree without conflict.'),
       ('I’m afraid not', '恐怕不行', 'A polite way to refuse.'),
       ('within the next two weeks', '未来两周内', 'It should be done within the next two weeks.'),
       ('news briefing', '新闻简报', 'One slide, one minute, one clear takeaway.'),
       ('pay attention to the layout', '注意版面', 'Pay attention to the visual layout of this slide.')),
 examples=(Q('例 1　把下列命令改写成合适的建议或义务表达，并说明强度：',
   p('A. <i>Check all the other plugs.</i>　B. <i>Call the subcontractor now.</i>　C. <i>Replace this plug.</i>') +
   p('<b>解：</b>A 若这是不可协商的安全步骤，用 must 的被动式：<i>All the other plugs must be checked.</i>（最强，责任不在说话人个人）。若只是建议，用 <i>I suggest we check all the other plugs as well.</i>（中弱，留出讨论空间）。') +
   p('B 若说话人当场决定自己做：<i>I’ll call our subcontractor immediately.</i>（will 表即时承诺）。若要指派对方，用 <i>Could you call the subcontractor right away?</i>（请求，礼貌）。') +
   p('C 若强调后果：<i>I’d better replace this one at once.</i>（had better，隐含「不换会出事」）。若客观条件要求：<i>This one will have to be replaced.</i>（外部义务）。') +
   p('<b>通用思路：</b>先定责任归属（我／你／规定）→ 再定强度（must／have to／should／had better）→ 最后决定用主动还是被动，被动能把责任推给流程，是会议里的常用技巧。'))
  + Q('例 2　判断下列情态动词的语用差别，并选出最合适的一句：',
   p('场景：你发现插头型号不对，需要说服对方接受「全部更换」。'
   + p('A. <i>All the plugs must be changed.</i>　B. <i>We’ll have to check all the other plugs as well.</i>　C. <i>Maybe someone could have a look at the other plugs.</i>') +
   p('<b>解：</b>A 最强，把结论说成规定，适合安全规范场合，但对同事说会显得越权。B 用 have to 把义务归于客观条件（「不得不」），并加 as well 表示这是补充而非推翻，最适合本场景。C 最弱，maybe + could 已经接近「随便看看」，在需要推动决策时反而不负责。') +
   p('选择依据：<b>你要的是对方行动，还是对方同意</b>。要行动且时间紧，用 B；要写进规程，用 A；只是试探，用 C。') +
   p('<b>通用思路：</b>列出三档强度 → 判断场景的紧迫度与权力关系 → 选一句并准备一句退让版本（<i>If that’s too much, we could start with the three cabinets that failed.</i>）。'))
  + Q('例 3　把 <i>No, you are wrong. We cannot stop production.</i> 改写为三步法的不同意。' +
   p('<b>解：</b>第一步承认：<i>I see your point — a full replacement would remove the risk completely.</i>') +
   p('第二步缓和：<i>That said, a complete standstill this month would affect deliveries we’ve already promised.</i>（把冲突归因于客观条件，不评价对方）。') +
   p('第三步反提：<i>What if we replace the plugs in the three cabinets that failed inspection first, and schedule the rest for the maintenance window in May?</i>') +
   p('改写后三句共 55 词，比原句长，但把「你错了」变成了「我们一起找方案」。') +
   p('<b>通用思路：</b>承认对方目标 → 指出客观限制 → 给出可执行替代；三步缺任何一步都会退回对立。'))
  + Q('例 4　分析 <i>It has been quite a nuisance. Just twenty minutes ago we had a short interruption.</i> 的时态选择，并说明如果改成 <i>It was a nuisance twenty minutes ago</i> 会丢失什么信息。' +
   p('<b>解：</b>第一句用现在完成时，表示麻烦从过去持续到现在，且暗示还会继续——这是让听者重视的关键。第二句用一般过去时 + ago，因为「二十分钟前的一次中断」是已结束的具体事件。') +
   p('若改成 <i>It was a nuisance twenty minutes ago</i>，只能表达「二十分钟前它是麻烦」，既丢了「一直如此」的持续性，也丢了「现在仍可能发生」的警告意味。') +
   p('补充：<i>It has been quite a nuisance</i> 用完成时还暗含抱怨的语气（nuisance 本身偏口语），若写正式报告应改为 <i>The fault has caused repeated interruptions.</i>') +
   p('<b>通用思路：</b>先看时间词（lately → 完成时；ago → 过去时）→ 再看事件是持续还是点状 → 最后看语域（nuisance 偏口语，report 用 fault／interruption）。')))),
 practice=(ol('把 <i>I suggest to check the wiring</i> / <i>He suggested me to call the supplier</i> / <i>We must to change the plugs</i> 改为正确形式。',
         '按强度从弱到强排列并各造一句：<i>could, should, had better, have to, must</i>。',
         '为下列场景各写一句会议用语：① 介绍同事给客户；② 请对方给一个停机时间；③ 礼貌拒绝本周完成。',
         '用「承认—缓和—反提」三步写一段 50 至 70 词的不同意，主题：是否立即更换全部插头。',
         '为一篇 YLE 新闻写一页幻灯片的三行文字（标题、关键数据、与本专业的相关性），并注明标题／作者／日期应放哪里。',
         '列出你会前 10 分钟的五项检查，并说明每一项失败会导致什么后果。')
  + D('答案与思路' +
   p('<b>1.</b> <i>I suggest checking the wiring.</i>（suggest + V-ing）或 <i>I suggest we check the wiring.</i>（从句用原形）；<i>He suggested that I call the supplier.</i>；<i>We must change the plugs.</i>（must 后直接接原形，不加 to）。') +
   p('<b>2.</b> 弱→强：<i>We could ask the subcontractor for a quote.</i>（可选）／<i>You should check the label before you install it.</i>（建议）／<i>You’d better wear gloves for this.</i>（含后果的劝告）／<i>We have to finish before the maintenance window closes.</i>（客观义务）／<i>All live parts must be isolated before work starts.</i>（强制规定）。') +
   p('<b>3.</b> ① <i>Mike, this is Anna Korhonen from our maintenance team.</i>；② <i>When is a standstill possible for you?</i> 或 <i>Could you tell me when we could schedule a standstill?</i>；③ <i>I’m afraid we can’t finish it this week, but we could have it done within the next two weeks.</i>（拒绝 + 替代时间）。') +
   p('<b>4.</b> 参考：<i>I see your point — replacing every plug now would remove the risk completely. That said, a full standstill this month would delay three deliveries we’ve already promised. What if we start with the cabinets that failed inspection and schedule the rest for May?</i>（62 词）。') +
   p('<b>5.</b> 参考三行：标题 <i>Finland’s grid operator reports record wind output</i>；关键数据 <i>Wind covered 24% of demand on 3 March, up from 15% in 2020</i>；相关性 <i>Relevant for us because grid balancing is exactly what our storage project targets</i>。标题、作者、日期放页脚，字号最小但必须可读。') +
   p('<b>6.</b> 麦克风（无声音则整场发言作废）／摄像头（无法被看到则失去 audience 分）／耳机与回声（回声会让所有人听不清）／幻灯片备份 PDF（字体丢失会让图表错位）／本地录制（课堂录制失败时仍有备份）。'))),
 exam=(cal('exam', '必考', 'suggest 的三条语法规则；must／have to／should／had better 的强度阶梯；现在完成进行时与一般过去时＋ago 的分工；replace A with B 与 substitute A for B 的方向；三步法不同意；行动项的三要素；一分钟简报的三句结构。')
  + cal('warn', '易错 1', '<i>suggest to do</i> 与 <i>suggest sb to do</i> 都是错的；<i>must to change</i> 也是错的。')
  + cal('warn', '易错 2', '有 ago 却用完成时（<i>has been a nuisance twenty minutes ago</i>）；lately 却用过去时。')
  + cal('warn', '易错 3', '把 substitute 与 replace 的介词方向弄反；对同事直接说 <i>You are wrong</i> 而不是三步法。')
  + cal('tip', '进阶', '会议里最有效的一句软化是把判断变成问题：<i>I suppose it can’t wait too long?</i> 用升调说出，既表达了判断，又给对方修正的机会。')),
 checklist=(h2('本讲方法清单')
  + h3('会议发言四步')
  + st('开场：介绍 + 一句寒暄 + well 转场到正题',
       '描述问题：持续状态用完成（进行）时，具体事件用过去时 + ago',
       '提出方案：suggest + 从句（原形）或 Why don’t we …，并说明理由',
       '收行动项：谁、做什么、什么时候，用 will 表当场承诺')
  + h3('不同意三步法')
  + ck('承认对方的目标或顾虑（I see your point — …）',
     '把冲突归因于客观限制（That said, … would affect …）',
     '给出可执行替代（What if we … first?）',
     '句末略升调，留出协商空间')
  + h3('一分钟新闻简报')
  + ck('第一句：来源、日期、主张（This article, published by … on … , reports that …）',
     '第二句：一个关键数字（The key figure is …）',
     '第三句：与本专业或听众的相关性（What makes it relevant is …）',
     '幻灯片页脚写清标题、作者、日期')),
 mapping=tb(('源文件', '位置 / 页码', '覆盖内容'),
   ('5_UNIT 2/2_DIALOGUE Engineers Meet.html', '全篇', 'Ch.4 现场对话：介绍第三方、寒暄、描述故障、suggest／had better／have to、行动项'),
   ('5_UNIT 2/7_DIALOGUE Looking for the Problem.html', '全篇', 'Ch.7 对话，内容与 Ch.4 完全相同（重复副本），语言点同上'),
   ('5_UNIT 2/4_EXERCISE Pair work (agreeing and disagreeing).html', '全篇', 'Student A / B 分开材料的双人练习，训练同意与不同意'),
   ('6_UNIT 3/1_Meeting 13 homework.html', '全篇', 'YLE 新闻选读、一页幻灯片（标题／作者／日期／版面）、一分钟小组陈述、之后讨论视觉'),
   ('4_UNIT 1/4_Meeting 4 homework.html', '全篇', '线上会议前检查麦克风与摄像头；带一道专业课习题到课堂看语言'),
   ('（跳过）', '—', '第二篇对话为重复副本，不重复设知识点；Student A/B 材料原件不在源文本中，仅按练习说明转述任务'),
   ('（拓展）', '—', '情态动词强度阶梯表、hedging 清单、三步法不同意、一分钟简报三句结构、会前五项检查为教学补充'))))
emit('32632', 11, 'KE00DA03 大学英语', 'Professional English', 'KE00DA03 大学英语',
     '面向国际学士项目的专业英语课，以口头产出为主线：从自我介绍与朗读分块，到技术词汇与词序、介词语法，再到 60 秒电梯演讲、3 至 4 分钟工程演讲与图表描述，最后落在会议协商与专业简报。考核为一次基线视频加三次作业，两次计分作业按 0–100 分换算 1–5 级。',
     LEC)