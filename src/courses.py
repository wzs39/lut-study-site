# -*- coding: utf-8 -*-
"""15 门课的元数据：id -> 排序、中英文名、源目录、一句话摘要。"""

C = {}


def add(cid, order, zh, en, src, summary):
    C[cid] = {'order': order, 'name_zh': zh, 'name_en': en,
              'source_dir': src, 'summary': summary}


add('29428', 1, 'LUT 数字导览', 'LUT Digital Orientation 2026-2027',
    'LUT digital orientation 数字导览',
    '新生入学数字导览：学习系统与工具、平等与伦理准则、学术诚信。以无关闭日的自测题为主。')
add('29911', 2, 'BH60A7201 循环经济', 'Kiertotalous.nyt / Circular Economy Now',
    'BH60A7201 Kiertotalous.nyt 循环经济',
    '循环经济 MOOC：从线性经济到循环经济的范式转变，交付物为 MOOC 证书与书面汇总。')
add('29913', 3, 'BH60A7400 Climate.Now 气候', 'Climate.Now',
    'BH60A7400 Climate.Now 气候',
    '气候通识 MOOC 加五选四论文：碳足迹、可再生能源、适应策略、社区行动、可持续预算；重引用规范与 AI 使用披露。')
add('30331', 4, 'CT10A9900 学习导论', 'Introduction to DD Studies in Software and Systems Engineering',
    'CT10A9900 学习导论 DD Studies',
    '软件与系统工程专业入门：学位结构、Sisu 个人学习计划、团队协作、学术 CV。')
add('30332', 5, 'CT30A1000 学习工具与 AI', 'Software Tools and AI for Studies',
    'CT30A1000 学习工具与AI',
    '六讲工具课：学习服务与 IT 指南、Office 与 AI、演示工具、绘图与设计、AI 生成内容、在学习中使用 AI 的边界。')
add('30352', 6, 'CT60A0250 编程基础', 'Fundamentals of Programming for International Programs',
    'CT60A0250 编程基础',
    'Python 从零到项目实战：变量与类型、控制流、函数、类与容器、文件与 CSV/JSON、模块与标准库，终点是租车管理系统。')
add('30361', 7, 'CT60A4050 软件工程基础', 'Fundamentals of Software Engineering',
    'CT60A4050 软件工程基础',
    '软件工程全流程：需求、敏捷与 Scrum、质量度量、测试与 CI、工作量估算、伦理与 AI 偏见；含团队项目三份报告。')
add('30565', 8, 'BM20A9200 数学 A', 'Mathematics A',
    'BM20A9200 数学A',
    '离散数学主线：集合与关系、命题逻辑与证明、函数与基数、组合与归纳、数论与 RSA、矩阵。考试可带 A4 手写小抄。')
add('32632', 9, 'KE00DA03 大学英语', 'English for the Hebei University of Technology',
    'KE00DA03 大学英语',
    '学术英语口语与展示：电梯演讲、发音测试、期末演示；三个 UNIT 覆盖构建专业知识、表达观点、职业沟通。')
add('32667', 10, 'KE00BX35 英语语音', 'English Pronunciation',
    'KE00BX35 英语语音',
    '音素、重音与语调三模块加个人演讲；以录音作业为主，重可懂度而非口音。')
add('33295', 11, 'K200DJ96 芬兰语 1', 'Finnish 1',
    'K200DJ96 芬兰语1',
    '芬兰语 A1：字母与发音、问候与自我介绍、数字、国名与语言、动词类型、元音和谐、属格基础。')
add('34583', 12, 'K200DJ99 芬兰语 2', 'Finnish 2',
    'K200DJ99 芬兰语2',
    '芬兰语 A1 到 A2：时间与日期、天气、爱好、食物与餐厅、属格与部分格、动词类型与格变化。')
add('62', 20, 'HDD4010 工程数学 I', 'Engineering Mathematics I (Calculus)',
    'hebut/学习资料/HDD4010 工程数学 I',
    '单变量微积分：实数与坐标几何、极限与连续、导数与微分法则、中值定理与单调性、指数对数、洛必达法则、积分与应用。')
add('80', 21, 'HDD4020 工程数学 II', 'Engineering Mathematics II',
    'hebut/学习资料/HDD4020 工程数学 II',
    '参数曲线与极坐标、柱面与球面坐标、矩阵运算、行列式与逆、高斯消元与 Cramer 法则、向量与点积。')
add('86', 22, 'HDD5020 信息处理基础', 'Foundations of Information Processing',
    'hebut/学习资料/HDD5020 信息处理基础',
    '信息表示全景：数制、数字编码、字符编码、图像、音频与视频、数据压缩、存储与文件、检索、加密、逻辑。')
