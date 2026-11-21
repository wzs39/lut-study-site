# -*- coding: utf-8 -*-
"""32632 大学英语 · 并入 2026-11-21 从 Moodle SharePoint 收割的 16 份文档。

来源（moodle-updates/2026-11-21/linked/32632/，文本在同目录上级 text/32632/）：
  Chunking 任务 B1/C1、食物词汇卡×5、数据中心文章 B1/C1、Student A/B 同意不同意卡、
  CEE Unit 6 可行性、Meeting 9 幻灯片、pronunciation recap、Recording instructions。
做法：对既有讲义按 section 追加（不改动原有内容），并新增第 9 讲语音诊所。
"""
import io
import json
import os
import sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, chips, badge  # noqa: E402

CONTENT = os.path.join(SITE, 'content', '32632.json')
BACKUP = CONTENT + '.before-materials'

LINKED = 'moodle-updates/2026-11-21/linked/32632/'
TEXT = 'moodle-updates/2026-11-21/text/32632/'

with io.open(CONTENT, encoding='utf-8') as fh:
    data = json.load(fh)
if not os.path.exists(BACKUP):
    with io.open(BACKUP, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    print('[backup] 32632.json.before-materials')


def lecture(slug):
    for x in data['lectures']:
        if x['slug'] == slug:
            return x
    raise KeyError(slug)


def splice(html, section, extra):
    marker = 'data-type="%s">' % section
    i = html.find(marker)
    if i < 0:
        raise ValueError('missing section ' + section)
    j = html.find('</section>', i)
    return html[:j] + extra + html[j:]


def apply(slug, adds, files=(), keywords=()):
    lec = lecture(slug)
    html = lec['html']
    for section, extra in adds:
        html = splice(html, section, extra)
    lec['html'] = html
    for f in files:
        if f not in lec['source_files']:
            lec['source_files'].append(f)
    for kw in keywords:
        if kw not in lec['keywords']:
            lec['keywords'].insert(0, kw)


def rows(*triples):
    return tb(('English', '中文', '说明 / 例句'), *triples)


# =====================================================================
# 1) l2-reading-chunking · Supercell 分块任务（B1/C1 双版全文落地）
# =====================================================================
l2_detail = (
    h3('2.11 分块任务原文落地：Supercell 文章（B1/C1 双版）')
    + cal('tip', '材料', '两份 PDF 全文已归档：<code>' + LINKED + 'link-02-…(B1).pdf</code> 与 <code>link-01-…(C1).pdf</code>，提取文本见 <code>' + TEXT + '</code>。两版讲同一件事，难度不同。')
    + p(
        '<b>任务原文五步（两版一致）：</b>① 朗读 Supercell 文章；② 挑 5 个你想用的 chunk/短语（如 '
        '<i>popular mobile games</i>、<i>developing a game</i>、<i>the traditional approach</i>、'
        '<i>get out of their way</i>、<i>the management structure</i>）；③ 看粉色词，'
        '用它们造 10 个句子——<b>只说不写</b>；④ 想 Supercell 的管理结构与中国公司有何不同；'
        '⑤ 下节课带着你练的短语和文章观点来分享。'
    )
    + p('<b>为什么分块有效（原文类比）：</b>电话号码 045 678 4192 比 0 4 5 6 7 8 4 1 9 2 好记，'
        '因为大脑按「块」存储。语言里高频同现的词组（<i>occur together</i>）就是块：'
        '<i>Look at this</i> / <i>introduce a feature</i> / <i>Can you help me…</i> / '
        '<i>open-source project</i> / <i>need to</i> / <i>a user-friendly interface</i> / '
        '<i>In my opinion</i>。按块说话比逐词拼装快得多——这就是流利度的来源。')
    + p('<b>块 + 块 = 句（原文拼装示例）：</b>'
        '<code>Look at this.</code> + <code>Is it a user-friendly interface?</code>；'
        '<code>Can you help me?</code> + <code>I need to introduce a feature.</code>'
        '——工程场景里先攒块、再拼接，说话和写作同时提速。')
    + h3('2.12 Supercell 文章内容地图（C1 版，Kris Graft）')
    + rows(
        ('Helsinki, Finland-based', '总部赫尔辛基', 'Clash of Clans / Clash Royale / Boom Beach / Hay Day 四款爆款'),
        ('to the tune of $810m / $2bn', '利润 8.1 亿 / 营收 20 亿美元', '2017 财年数据，介绍成绩的高频句型'),
        ('upside-down organization', '倒置的组织', '全文题眼：creatives run the company'),
        ('cells of 10-17 developers', '10–17 人小队', '公司名 Supercell 的由来；每个 cell 做自己的游戏'),
        ('no greenlight process', '没有立项审批', '对比传统公司：管理层不放行项目'),
        ('no milestone meetings', '没有里程碑汇报会', '不用向财务证明项目值得存在'),
        ('teams can kill their games', '团队可以亲手砍掉游戏', '砍游戏是团队自己的决定'),
        ('get out of their way', '给创作者让路', '管理层唯一的职责：建好团队然后让开'),
        ('in spite of the structure', '尽管有这种结构仍成功', 'Paananen 论断：传统公司是「尽管有架构」而非「因为有架构」而成功'),
        ('snuff out a big success', '扼杀一个大成功', '管理层善意干预反而坏事'),
        ('I wasn\'t a big believer in…', '我起初不看好…', 'Clash Royale：CEO 自己都不看好，后来成最大爆款之一'),
        ('wanted to can it', '想砍掉它', 'Boom Beach：所有 team lead 投票反对，唯独负责人坚持'),
        ('lopsided vote / overrule', '一边倒的投票 / 多数否决', 'Paananen 的两难：业务正确 vs 文化代价'),
        ('culture of independence and responsibility', '独立与负责的文化', '宁可要文化也不 9:1 否决'),
        ('take the long view', '着眼长远', '5–10 年后看：游戏失败不可怕，团队学到东西、文化保住才重要'),
    )
    + p('<b>B1 版差异：</b>同一故事改写为 B1 难度（短句、常见词），开头 '
        '<i>Supercell is a game company in Helsinki, Finland. It is famous for making popular mobile games like…</i>'
        ' 两版对读，正好练「同一信息、两种语言难度」的表达切换。')
)
l2_practice = (
    qa('练 1 · 粉色词口头造句（按原文任务）',
       p('从文章任选 10 个粉色词/短语，<b>只说不写</b>，每个说一个与工程或游戏行业相关的完整句。'
         '例：<i>Supercell lets small teams develop games without a greenlight process.</i>')
       + det('思路', st('先给短语分类（名词短语 / 动词短语 / 句子框架）',
                        '每类配一个主语和时态（游戏行业常用一般现在时、一般过去时）',
                        '口头连读三遍，检查 chunk 之间是否停顿过多',
                        '录音 60 秒自评：块与块衔接是否自然'))))
l2_check = ck('分块学习五步（原文 Instructions 直译）',
              '① 通读文章（朗读，不是默读）',
              '② 挑 5 个最想内化的 chunk',
              '③ 粉色词口头造 10 句（只说不写）',
              '④ 对比 Supercell 管理结构与你熟悉的国内公司',
              '⑤ 下节课口头分享短语与观点')
apply('l2-reading-chunking',
      [('detail', l2_detail), ('practice', l2_practice), ('checklist', l2_check)],
      files=['Homework_Task_-_Chunking_(C1).pdf', 'Homework_Task_-_Chunking_(B1).pdf'],
      keywords=['chunking', 'Supercell', 'greenlight process'])

# =====================================================================
# 2) l3-vocabulary-grammar-clinic · 五套食物词汇卡（约 180 词）
# =====================================================================
# -- vegetables
veg = [
    ('potato', '土豆', 'baked / mashed potatoes'), ('carrot', '胡萝卜', 'grated carrot'),
    ('pumpkin', '南瓜', 'Halloween carving'), ('cabbage', '卷心菜', 'red / white cabbage'),
    ('lettuce', '生菜', 'a head of lettuce'), ('turnip', '芜菁', ''),
    ('tomato', '番茄', '复数 tomatoes（易错拼写）'), ('cucumber', '黄瓜', 'as cool as a cucumber'),
    ('chili / chilli', '辣椒', '英 chilli / 美 chili'), ('bell pepper / sweet pepper', '甜椒', ''),
    ('red/yellow/green pepper', '红/黄/绿椒', ''), ('cauliflower', '花椰菜', 'broccoli 的近亲'),
    ('celery', '芹菜', 'celery sticks'), ('beet / beetroot', '甜菜根', '美 beet / 英 beetroot'),
    ('zucchini / courgette', '西葫芦', '美 zucchini / 英 courgette'),
    ('asparagus', '芦笋', '不可数用法常见'), ('mushroom', '蘑菇', ''),
    ('champignon', '口蘑（双孢菇）', '法源词'), ('eggplant / aubergine', '茄子', '美 eggplant / 英 aubergine'),
    ('artichoke', '朝鲜蓟', 'artichoke hearts'), ('onion', '洋葱', 'spring onion 大葱/小葱'),
    ('garlic', '蒜', 'a clove of garlic 一瓣蒜'), ('rutabaga / swede', '芜菁甘蓝', '美 rutabaga / 英 swede'),
    ('ginger', '姜', 'ginger tea'), ('yam', '山药/薯蓣', ''), ('sweet potato', '红薯', ''),
    ('radish', '小萝卜', ''), ('avocado', '牛油果', 'guacamole'),
    ('broccoli', '西兰花', '不可数'), ('fennel', '茴香', 'fennel bulb'),
    ('parsnip', '欧防风', '根菜类'), ('spinach', '菠菜', '不可数'),
    ('celeriac', '根芹', 'celery root'), ('squash', '笋瓜类（总称）', 'butternut squash'),
    ('kale', '羽衣甘蓝', 'superfood 语境高频'),
]
grain = [
    ('wheat', '小麦', 'whole wheat 全麦'), ('oats', '燕麦（粒）', ''),
    ('barley', '大麦', 'pearl barley'), ('rye', '黑麦', 'rye bread 芬兰常见'),
    ('corn (maize)', '玉米', '美 corn / 英 maize'), ('rice', '大米', 'cooked rice 米饭'),
    ('kidney bean', '红腰豆', 'chili con carne'), ('green beans', '四季豆', '复数'),
    ('soybean', '大豆', 'soy sauce 酱油'), ('peas', '豌豆', 'split peas'),
    ('chickpeas', '鹰嘴豆', 'hummus 原料'), ('lentils', '小扁豆', '红/绿 lentil'),
    ('walnut', '核桃', ''), ('cashew nut', '腰果', ''), ('peanut', '花生', 'peanut butter'),
    ('pistachios', '开心果', ''), ('coconut', '椰子', 'coconut milk'),
    ('pecan', '山核桃', 'pecan pie'), ('hazel nut', '榛子', 'nutella 原料'),
    ('almond', '杏仁', 'almond milk'), ('wheat flour', '（小麦）面粉', ''),
    ('rolled oats / oatmeal', '燕麦片', 'porridge 原料'), ('rye bread', '黑麦面包', '芬兰食堂高频'),
    ('cooked rice', '米饭', 'raw rice 生米'), ('cereal', '谷物早餐', '亦泛指 grain 谷物'),
    ('oatmeal (porridge)', '燕麦粥', '美 oatmeal / 英 porridge'),
    ('spaghetti', '意大利细面', '不可数'), ('pasta', '意面（总称）', '不可数'),
    ('quinoa', '藜麦', '读 /ˈkiːnwɑː/'), ('millet', '小米', ''),
    ('buckwheat', '荞麦', '芬兰 kasha'), ('wholegrain-foods', '全谷物食品', '包装标签高频'),
]
fruit = [
    ('apple', '苹果', ''), ('banana', '香蕉', ''), ('orange', '橙子', ''),
    ('apricot', '杏', ''), ('grapefruit', '西柚', ''), ('cherry', '樱桃', ''),
    ('mango', '芒果', ''), ('lemon', '柠檬', ''), ('kiwi', '猕猴桃', ''),
    ('fig', '无花果', ''), ('date', '椰枣', 'date 亦是「约会/日期」'),
    ('pear', '梨', ''), ('plum', '李子', ''), ('pomegranate', '石榴', ''),
    ('watermelon', '西瓜', ''), ('honeydew (melon)', '蜜瓜', ''),
    ('cantaloupe', '哈密瓜（网纹瓜）', ''), ('lingonberry', '越橘', '芬兰 berry 高频'),
    ('blueberry', '蓝莓', '芬兰森林常见'), ('strawberry', '草莓', ''),
    ('raspberry', '覆盆子', ''), ('blackberry', '黑莓', ''),
    ('gooseberry', '醋栗', ''), ('currant', '红/黑加仑', ''),
    ('cloudberry', '云莓', '北欧限定，贵'), ('pineapple', '菠萝', ''),
    ('lime', '青柠', ''), ('cranberry', '蔓越莓', ''),
    ('rowanberry', '花楸果', '芬兰路树常见'), ('kumquat', '金桔', ''),
    ('mandarin', '橘子', ''), ('clementine', '小柑橘', ''),
    ('satsuma', '无籽蜜橘', ''), ('pomelo', '柚子', ''),
    ('grapes', '葡萄', 'a bunch of grapes'), ('nectarine', '油桃', ''),
    ('boysenberry', '博伊森莓', ''), ('dragon fruit (pitaya)', '火龙果', ''),
    ('passion fruit (granadilla)', '百香果', ''), ('star fruit (carambola)', '杨桃', ''),
    ('arctic raspberry/bramble', '北极悬钩子', ''), ('chokeberry (aronia)', '野樱莓', ''),
    ('buckthorn', '沙棘', '芬兰 sea buckthorn 高频'),
]
animal = [
    ('eggs', '鸡蛋', 'boiled / fried / scrambled'), ('honey', '蜂蜜', '不可数'),
    ('milk', '牛奶', 'whole / skimmed milk'), ('cheese', '奶酪', '芬兰bread table 常客'),
    ('vegan cheese / cheeze', '素食奶酪', '拼写 cheeze 标产品'), ('yogurt', '酸奶', '英 yoghurt 亦见'),
    ('vegan/plant butter', '植物黄油', ''), ('oil', '油', 'olive / rapeseed oil'),
    ('ice cream', '冰淇淋', ''), ('sour cream', '酸奶油', ''),
    ('vegan sour cream', '素食酸奶油', ''), ('buttermilk', '酪乳', '芬兰 piimä'),
    ('condensed milk', '炼乳', ''), ('condensed coconut milk', '椰浆炼乳', ''),
    ('plant-based cream', '植物奶油', '标签 dairy-free'), ('salmon', '三文鱼', '芬兰 loop 温泉鱼'),
    ('fish', '鱼（总称）', 'fish and chips'), ('tuna', '金枪鱼', '罐头高频'),
    ('game', '野味', 'moose 驼鹿肉属 game'), ('chicken', '鸡肉', ''),
    ('poultry', '禽肉（总称）', '分类词，非单只鸟'), ('turkey', '火鸡', '感恩节语境'),
    ('duck', '鸭肉', ''), ('reindeer', '驯鹿肉', '芬兰特色'),
    ('rabbit', '兔肉', ''), ('veggie burger/patty', '素食汉堡饼', ''),
    ('steak', '牛排', 'medium rare 三分熟'), ('ribs', '肋排', 'BBQ ribs'),
    ('minced meat', '肉末', '英 minced / 美 ground'), ('bacon', '培根', ''),
    ('tofu', '豆腐', ''), ('seitan', '面筋蛋白', '素食蛋白'),
    ('tempeh', '天贝（发酵豆饼）', '印尼源词'),
]
kitchen = [
    ('fork', '叉子', ''), ('knife', '刀', '复数 knives'), ('spoon', '勺子', ''),
    ('plate', '盘子', ''), ('glass', '玻璃杯', 'glasses 亦指眼镜'),
    ('silverware / cutlery', '餐具（总称）', '美 silverware / 英 cutlery'),
    ('wok (pan)', '炒锅', '中餐高频'), ('frying pan', '平底煎锅', ''),
    ('casserole dish', '烤盅/砂锅', ''), ('spatula', '锅铲', ''),
    ('ladle', '长柄勺', 'serve soup'), ('vegetable peeler', '削皮器', ''),
    ('grater', '擦丝器', 'grate cheese'), ('chopping board', '砧板', '英 board / 美 cutting board'),
    ('measuring cup', '量杯', '烘焙必备'), ('glass bowl / steel bowl', '玻璃/钢盆', ''),
    ('baking tray', '烤盘', '英 tray / 美 sheet'), ('cooking pot', '汤锅', ''),
    ('blender', '搅拌机（破壁）', ''), ('kettle', '水壶', '芬兰人烧水必备'),
    ('electric kettle', '电热水壶', ''), ('toaster', '烤面包机', ''),
    ('stove / cooker / range', '灶', '美 stove / 英 cooker'), ('oven', '烤箱', 'in the oven'),
    ('colander', '滤锅/沥水篮', 'drain pasta'), ('tea pot', '茶壶', ''),
    ('chopsticks', '筷子', '复数，a pair of'), ('measuring spoons', '量勺', ''),
    ('cleaver', '菜刀（中式）', ''), ('rolling pin', '擀面杖', ''),
    ('whisk / beater', '打蛋器', 'whisk 亦是动词'), ('electric mixer', '电动打蛋器', ''),
    ('wooden spoon', '木勺', ''), ('coffee maker', '咖啡机', '芬兰人均咖啡量世界第一'),
]
l3_detail = (
    h3('3.11 五套食物词汇卡全表（与 3.2/3.3 互补）')
    + cal('tip', '来源', '五张词卡 PDF 已归档（<code>' + LINKED + 'link-03…07</code>）。3.3 的 24 个烹饪动词即 <code>food_vocab_cooking.pdf</code>，此处不重复；下面补齐五套名词卡，共约 180 词。')
    + p('<b>英美同物异名（卡片成对出现，考试易错）：</b>'
        'aubergine（英）= eggplant（美）；courgette（英）= zucchini（美）；swede（英）= rutabaga（美）；'
        'maize（英）= corn（美）；beetroot（英）= beet（美）；chilli（英）= chili（美）；'
        'minced meat（英）= ground meat（美）；cooker（英）= stove（美）。')
    + h3('3.11a 蔬菜（greens 35 词）') + rows(*veg)
    + h3('3.11b 谷物豆类坚果（grain-bean-nut 32 词）') + rows(*grain)
    + h3('3.11c 水果浆果（fruits-berries 43 词）') + rows(*fruit)
    + h3('3.11d 动物制品与替代品（animal products 35 词）') + rows(*animal)
    + h3('3.11e 厨具（kitchenware 34 词）') + rows(*kitchen)
    + p('<b>芬兰特色词（课堂材料专门标注）：</b>rye bread 黑麦面包、lingonberry 越橘、'
        'cloudberry 云莓、reindeer 驯鹿肉、buttermilk (piimä)、sea buckthorn 沙棘——'
        '这些词在芬兰超市与课堂对话里出现率极高，属于「本地加分词汇」。')
)
l3_practice = (
    qa('练 1 · 可数性 × 量词搭配（用新词）',
       p('把下列词按可数/不可数分组，并配一个正确的量词短语：<i>broccoli, cherry, garlic, pasta, lettuce, salmon, chopsticks, oatmeal</i>。')
       + det('参考答案',
             p('可数：a cherry 樱桃一颗 / two heads of lettuce 两颗生菜 / a pair of chopsticks 一双筷子。'
               '不可数：some broccoli / a clove of garlic 一瓣蒜 / a bowl of pasta / a fillet of salmon 一块三文鱼排 / a bowl of oatmeal。'
               '易错：broccoli、pasta、oatmeal 都不可数，不加 a；garlic 论「瓣」用 clove。'))))
apply('l3-vocabulary-grammar-clinic',
      [('detail', l3_detail), ('practice', l3_practice)],
      files=['food_vocab_greens.pdf', 'food_vocab_grain-bean-nut.pdf', 'food_vocab_fruits-berries.pdf',
             'food_vocab_animal-products-and-substitutes.pdf', 'food_vocab_kitchenware.pdf'],
      keywords=['aubergine', 'courgette', 'lingonberry', 'kitchenware'])

# =====================================================================
# 3) l5-presentation-data · Meeting 9 图表词库 + 数据中心阅读
# =====================================================================
graphs = [
    ('pie chart (circle chart)', '饼图', 'circular graphic divided into slices → numerical proportion'),
    ('line graph (line chart)', '折线图', 'shows information that changes over time'),
    ('bar chart (column chart)', '柱状图', 'categories represented by rectangles'),
    ('area chart', '面积图', 'lines + filled areas'),
    ('scatter plot', '散点图', 'dots for two numeric variables'),
]
up = [('increase (steady)', '稳步上升'), ('rise', '上升'), ('grow', '增长'), ('go up', '上行'),
      ('soar (rapid)', '暴涨'), ('double', '翻倍'), ('multiply', '成倍增长'), ('climb', '爬升'),
      ('exceed', '超过')]
down = [('decrease', '下降'), ('drop (rapid)', '骤降'), ('fall', '下跌'), ('decline', '衰退'),
        ('plummet (rapid)', '断崖式下跌'), ('halve', '减半'), ('depreciate', '贬值'), ('plunge (rapid)', '猛跌')]
mid = [('fluctuate / undulate', '波动'), ('dip', '先降后升的小低谷'), ('reach a peak / peaked', '到达峰值'),
       ('bottom out', '触底'), ('sink to a trough', '跌入谷底'), ('level off', '趋平'),
       ('remain constant/steady', '保持稳定')]
deg = [('小幅', 'gently · gradually · slightly · steadily · a little'),
       ('大幅', 'suddenly · sharply · dramatically · steeply · abruptly · substantially')]
l5_detail = (
    h3('5.11 图表词库扩展（Meeting 9 原版词库）')
    + cal('tip', '来源', '数据中心文章（B1/C1 两版）与 Meeting 9 幻灯片已归档；本块把幻灯片里的图表词库全部落进讲义。')
    + h3('5.11a 五种图（Types of Graphs）') + rows(*graphs)
    + h3('5.11b 上升（NUMBER IS GOING UP）') + rows(*[(a, b, '') for a, b in up])
    + h3('5.11c 下降（NUMBER IS GOING DOWN）') + rows(*[(a, b, '') for a, b in down])
    + h3('5.11d 波动·峰值·平稳（UP AND DOWN / STAYING THE SAME）') + rows(*[(a, b, '') for a, b in mid])
    + h3('5.11e 幅度副词（LEVEL OF CHANGE）') + rows(*[(a, b, '') for a, b in deg])
    + p('<b>幻灯片原例句（背下来直接用）：</b>'
        '<i>Consumer demand will rise in the following months.</i>；'
        '<i>The number of complaints has been increasing since June.</i>（现在完成进行时）；'
        '<i>Our market share is expected to decline this year.</i>（is expected to 预测句式）；'
        '<i>The number of Windows users has plunged in the past two years.</i>；'
        '<i>Sales dipped in July but peaked again in December.</i>；'
        '<i>Customer satisfaction improved gradually for years until it decreased sharply in 2020.</i>（gradually + sharply 对比）')
    + h3('5.12 阅读落地：为什么数据中心落户芬兰（B1/C1 双版精读）')
    + p('<b>文章结构（businessfinland.com, 2025-01-20）：</b>标题 <i>Cool, calm and connected: Why companies are '
        'placing their data centers in Finland</i>——四个自然优势 + 一组量化数字 + 政策引语。')
    + rows(
        ('ICT industry is heavy on the environment', 'ICT 产业环境负担重', '总起句：servers consume massive amounts of electricity'),
        ('water is needed to cool the equipment', '冷却要耗水', '与耗电并列的第二个环境成本'),
        ('the explosion of generative AI', '生成式 AI 的爆发', '加重大负担的表达'),
        ('asking ChatGPT-4 to write a 100-word email', '让 GPT 写一封 100 词邮件', '≈ 14 只 LED 灯亮 1 小时的电量 + 超过半升水'),
        ('if 1 in 10 Americans asked once a week…', '每十个美国人每周一次', '电量 ≈ 华盛顿特区全部住户 20 天用电；水 > 4.35 亿升'),
        ('CO2 targets / accountability', '碳目标 / 问责压力', '企业选址的两大推力'),
        ('cool climate', '凉爽气候', '天然免费冷源'),
        ('affordable clean energy', '廉价清洁能源', '芬兰电网低碳'),
        ('abundant fresh water', '充足淡水', '冷却资源'),
        ('robust / excellent digital infrastructure', '扎实的数字基础设施', 'connectivity 连通性'),
        ('50 construction-ready sites', '50 个可开工建设场址', '小至小型、大到 1000 MW+'),
        ('renewable energy · top-notch security', '可再生能源 · 顶级安全', '投资推介标准三件套'),
    )
    + p('<b>B1 版用法：</b>同一事实用短句改写（如 <i>Servers use a lot of electricity. AI makes it worse.</i>），'
        '适合先读 B1 抓结构，再回 C1 采集高级表达（<i>stack it all together</i> 把数字加总、'
        '<i>staggering</i> 惊人的、<i>prime location</i> 优选地、<i>paywall</i> 付费墙）。')
)
l5_examples = (
    qa('例 · 用词库描述一张三阶段折线图',
       p('图：某 App 月活跃用户 2022-2025——2022 缓升，2023 中段暴涨，2024 后回落趋平。')
       + p('<b>解（三段式 + 词库替换）：</b>① 开头点题：<i>This line graph shows our monthly active users from 2022 to 2025.</i>'
           '② 分段描述：From 2022 to mid-2023, the number <b>climbed steadily</b>. '
           'Then it <b>soared</b> after the AI feature launch, nearly <b>doubling</b> within a year. '
           'Since 2024, however, it has <b>declined slightly</b> and <b>levelled off</b> around 4 million.'
           '③ 收尾：Overall, growth was <b>gradual</b> at first but turned <b>dramatic</b> in 2023.'
           '——每段动词都标注了「速度」（steady/rapid/unsteady），这正是 5.6 的三类词。')))
apply('l5-presentation-data',
      [('detail', l5_detail), ('examples', l5_examples)],
      files=['Meeting9_EHUT_3015.pdf', 'News_article_2_(Energy&Software)_-_Data_centers_(C1).pdf',
             'News_article_2_(Energy&Software)_-_Data_centers_(B1).pdf'],
      keywords=['pie chart', 'scatter plot', 'soar', 'plummet', 'level off', 'generative AI'])

# =====================================================================
# 4) l6-meetings-negotiation · A/B 角色卡 + CEE 可行性
# =====================================================================
l6_detail = (
    h3('7.13 角色卡落地：同意与不同意（Student A / Student B）')
    + cal('tip', '玩法（卡片首页原文）', '两人一组：A 用 A 卡，B 用 B 卡。对话里只有「指令句」（斜体提示），'
        '你要把指令变成真实台词；对方卡上印着参考答案，说完互相核对。共两段对话都要过。')
    + p('<b>对话 1 · Discussing a Project（改计划 + 延期）：</b>'
        'A 表态要改计划 → B 澄清（<i>Do you mean that we should change the timeline or the overall approach?</i>）→ '
        'A 说明想延期 → B 顾虑预算（<i>I see what you mean, but extending the deadline might affect our budget.</i>）→ '
        'A 不想赶工并征询意见 → B 赞成并加建议（<i>Yes, I quite agree. … How about we also add more team members?</i>）→ '
        'A 采纳并提议和团队商量。')
    + p('<b>对话 2 · Discussing Product Design（换材料）：</b>'
        'A 主张换复合材料（更轻更耐用 <i>less weight, more durable</i>）→ B 顾虑成本（<i>might increase the cost significantly</i>）→ '
        'A 坚持值得 → B 赞同主线并建议改进表面处理（<i>improve the surface finish to enhance the product\'s appearance</i>）→ '
        'A 这回要<b>表示不同意</b>（<i>I\'m afraid I don\'t see the benefits… We should concentrate on qualities that affect the functioning of the product.</i>）→ '
        'B 收尾接受另一观点、提议找设计团队。')
    + rows(
        ('Do you mean that…?', '澄清式提问', '把模糊建议钉成具体方案'),
        ('I see what you mean, but…', '半步让步反驳', '先接住再转折，比直接 but 礼貌'),
        ('Yes, I quite agree.', '明确赞成', 'quite 加强语气'),
        ('How about we also…?', '附赠建议', '顺着对方观点加自己的'),
        ('From my point of view…', '表明立场', '引导论证'),
        ('It might be a good idea to…', '缓和建议', 'hedging 软化'),
        ('I\'m afraid I don\'t see the benefits of…', '委婉否定', 'afraid 垫在前，否定不伤人'),
        ('The benefits outweigh the costs.', '收益大于成本', '权衡句式'),
        ('concentrate on functionality', '聚焦功能性', 'design 争论里的务实立场'),
        ('Let\'s discuss this with the design team.', '把分歧交给团队', '会议收尾标准句'),
    )
    + h3('7.14 可行性讨论：CEE Unit 6（预算、工期与容差）')
    + p('<b>单元定位（Cambridge English for Engineering pp.46-53）：</b>讨论技术要求、提出方案、'
        '<b>评估可行性（assessing feasibility）</b>、描述改进与重新设计。核心对话：德国龙门吊工程师 Viktor '
        '电话印度工地经理 Rajesh，商量混凝土墙上的孔怎么成形。')
    + rows(
        ('feasibility', '可行性', '受 budget（预算）与 schedule（工期）双重约束'),
        ('gantry crane', '龙门吊', '场景主设备'),
        ('core drilled holes', '钻孔成孔', '现浇后钻：precision 高、cost 高、慢'),
        ('preformed holes', '预制孔', '浇筑前留：便宜快，风险是位置公差'),
        ('play', '旷量/间隙', '本语境指孔与螺栓之间的余量，不是「玩」'),
        ('tolerance', '公差', 'e.g. a tolerance of ±2 mm；preformed 易达较粗公差'),
        ('budget → design', '预算决定方案档次', 'bigger budget → more sophisticated/innovative design'),
        ('schedule → quality', '工期影响质量', 'longer schedule → higher reliability/efficiency'),
        ('feasibility 三问', '成本 · 精度 · 工期', '9b 对比 core drilling vs preforming 的三个维度'),
        ('the risk of using preformed holes', '预制孔的风险', '位置偏差 → 螺栓装不进 → play 不足'),
        ('apart from technical questions', '除技术问题外', '引出预算与工期两大决定因素'),
    )
    + p('<b>9d 听力六问（自测）：</b>① preformed 孔在成本与工期上的优势？② core drilling 的主要缺点？'
        '③ preformed 能轻松达到什么公差？④ 本项目要求什么公差？⑤ 用 preformed 的风险？'
        '⑥ Rajesh 指出的关键可行性问题？（答案都在录音稿里，先自己口头答再核对）')
)
l6_practice = (
    qa('练 · A/B 卡补台词（Discussing a Project，A 视角）',
       p('A 卡第 3 条指令是 <i>Clarify that you need more time (extend deadline)</i>——请给出你的台词，'
         '并预判 B 可能的两种反应。')
       + det('参考答案',
             p('台词：<i>Well, for a start, we should change the timeline. It might be a good idea to extend the deadline by two weeks.</i>'
               '（A 卡参考稿原句）B 反应一（同意）：<i>Yes, I quite agree. Quality is important.</i> '
               'B 反应二（顾虑）：<i>I see what you mean, but extending the deadline might affect our budget.</i> '
               '——同一指令，B 站哪边都接得住，这就是半步让步句式的价值。'))))
apply('l6-meetings-negotiation',
      [('detail', l6_detail), ('practice', l6_practice)],
      files=['STUDENT-A_agreeing_disagreeing_AB.pdf', 'STUDENT-B_agreeing_disagreeing_AB.pdf',
             'Meeting8_CEE_UNIT6_Technical_development_pp.46-53.pdf'],
      keywords=['feasibility', 'tolerance', 'preformed hole', 'core drilling'])

# =====================================================================
# 5) l4-elevator-pitch · 三种语气交付（Meeting 9 布置）
# =====================================================================
l4_practice = (
    qa('练 · 电梯演讲 × 3 种语气（Meeting 9 课后任务）',
       p('周四前把你的 elevator pitch 用<b>至少三种不同语气</b>各讲一遍，从清单里选：'
         '<i>Exited · Confident · Calm · Unsure · Tired · Frustrated · Energetic · Angry</i>。'
         '注意语调、语速与停顿（intonation, pace, pacing）。')
       + det('怎么做才算完成',
             p('① 每种语气先定「参数」：Exited = 语速快+音高抬；Confident = 降调收尾+重音清晰；'
               'Unsure = 升调+迟疑停顿；Calm = 慢速+长停顿。'
               '② 内容不变，只变 prosody——这正是本课「同一文本、不同副语言」的核心练习。'
               '③ 录音回听对照：语气差是否一听就能分辨。'))))
apply('l4-elevator-pitch',
      [('practice', l4_practice)],
      files=['Meeting9_EHUT_3015.pdf'],
      keywords=['tone of voice'])

# =====================================================================
# 6) l8-assignments-listening · 录音工具链（Recording instructions）
# =====================================================================
l8_detail = (
    h3('8.6 录音交付工具链（Recording instructions，2026-11-20 版）')
    + rows(
        ('Windows Camera', '录视频（无录屏）', 'Win10/11 搜 "Camera/Kamera"，右侧选 video'),
        ('Teams', '录屏+摄像头', 'Calendar → Meet now → Start meeting → … → Start recording；结束后链接在 Chat，打开下载'),
        ('Zoom', '录屏+摄像头', '注册 zoom.us → New meeting → Share screen → Record；结束退出会议后转码存 Documents/Zoom（.mp4）'),
        ('Screenpal / Vimeo / VEED.IO', '备选工具', '任何你顺手的录屏软件都行'),
        ('Vocaroo', '网页录音（纯音频）', '可生成直链分享'),
        ('Windows Voice Recorder', '系统录音机', '纯音频备选'),
        ('交付方式', '云盘分享链接', '录完传 SharePoint/云盘，把<b>链接</b>发老师'),
    )
    + cal('warn', '两个坑', '① Zoom 录制只能在桌面端（手机不行），且必须先退出会议视频才落盘；'
          '② 分享的是<b>链接</b>不是文件本体——上传后用「共享」生成链接再发。')
)
apply('l8-assignments-listening',
      [('detail', l8_detail)],
      files=['Recording_instructions.pdf'],
      keywords=['Vocaroo', 'screen recording'])

# =====================================================================
# 7) 新增第 9 讲 · 语音诊所
# =====================================================================
minimal_pairs = [
    ('/æ/ – /e/', 'man – men /\'mæn/ – /\'men/', 'had – head；sad – said', 'I saw three men. One man had a hat on his head. He said he was sad.'),
    ('/ɪ/ – /iː/', 'ship – sheep /\'ʃɪp/ – /\'ʃiːp/', 'sit – seat；live – leave', 'They ship the sheep from Wales. Take a seat and sit down.'),
    ('/t/ – /θ/', 'tree – three /\'triː/ – /\'θriː/', 'tank – thank；mat – math', 'The tree has three apples.'),
    ('/v/ – /w/', 'vet – wet /\'vet/ – /\'wet/', 'vile – while；vary – wary', 'The vet didn\'t like the wet dog.'),
    ('/r/ – /w/', 'run – one /\'rʌn/ – /\'wʌn/', 'rate – wait；rich – witch', 'If you wait, I will rate your work.'),
    ('/r/ – /l/', 'feel – fear', 'full – four；fewer – fuel', 'He had fewer fuel canisters than us.'),
    ('/ŋk/ – /ŋ/', 'sink – sing /\'sɪŋk/ – /\'sɪŋ/', 'wink – wing；rink – ring', 'Just wink if you want another wing.'),
    ('/n/ – /ŋ/', 'win – wing /\'wɪn/ – /\'wɪŋ/', '', ''),
]
stress_rules = [
    ('双音节名词/形容词', '第一音节', 'engine /ˈen.dʒɪn/ · motor · coated · narrow'),
    ('词尾 -ic', '倒数第二音节', 'elastic · automatic /ˌɑː.t̬əˈmæt̬.ɪk/'),
    ('词尾 -sion / -tion', '倒数第二音节', 'extension /ɪkˈsten.ʃən/ · institution'),
    ('词尾 -graphy / -logy / -nomy', '倒数第三音节', 'geography · technology /tekˈnɑː.lə.dʒi/ · economy'),
    ('词尾 -cy / -ty / -al', '倒数第三音节', 'democracy · electricity · critical /ˈkrɪt̬.ɪ.kəl/'),
    ('双音节动词', '最后音节', 'require /rɪˈkwaɪr/ · decide /dɪˈsaɪd/'),
    ('带前缀的词', '主干词首音节', 'inaccurate /ɪnˈæk.jɚ.ət/ · recharge · unload'),
]
homographs = [
    ('present', '礼物 / 出席（名·形）', '/ˈprez.ənt/', 'present（动词）展示', '/prɪˈzent/'),
    ('record', '记录（名词）', '/ˈrek.ɚd/', 'record（动词）录制', '/rɪˈkɔːrd/'),
]
abbrev = [('LED', '/ˌel.iːˈdiː/ 逐字母'), ('CPU', '/ˌsiː.piːˈjuː/ 逐字母'),
          ('USB', '/ˌjuː.esˈbiː/ 逐字母'), ('CAD', '/kæd/ 当单词读')]
twisters = ['Shake rattle and roll', 'All aluminum alloy', 'Mouse mouth month', 'Buried berry barrier',
            'Bad Bed Bug', 'World work week', 'Thumb through thunderstruck', 'Simultaneously similar',
            'Black blood blade', 'Specific squirrel salary']
your_pairs = [('place – palace', '/\'pleɪs/ – /\'pælɪs/'), ('uncle – ankle', '/\'ʌŋkəl/ – /\'æŋkəl/'),
              ('wheel – while', '/\'wiːl/ – /\'waɪl/'), ('screen – scream', '/\'skriːn/ – /\'skriːm/'),
              ('word – ward – world', '/\'wɜːd/ – /\'wɔːd/ – /\'wɜːld/'),
              ('flower – flow – flour', '/\'flaʊər/ – /\'fləʊ/ – /\'flaʊər/'),
              ('one – own – won', '/\'wʌn/ – /\'əʊn/ – /\'wʌn/'), ('quiet – quite', '/\'kwaɪət/ – /\'kwaɪt/')]
homophones = [('buy – by – bye', '/\'baɪ/'), ('see – sea – C', '/\'siː/'), ('two – too – to', '/\'tuː/'),
              ('board – bored', '/\'bɔːd/'), ('there – their – they\'re', '/\'ðeər/'),
              ('break – brake', '/\'breɪk/'), ('dear – deer', '/\'dɪər/'), ('no – know', '/\'nəʊ/')]

lec9 = L(
    slug='l9-pronunciation-clinic',
    tzh='第 9 讲 · 语音诊所：重音、语调、最小对立与录音交付',
    ten='Pronunciation Clinic: Stress, Intonation, Minimal Pairs and Recording Workflow',
    keywords=['prosody', 'minimal pair', 'syllable stress', 'intonation', 'pitch',
              'homophone', 'tongue twister', 'recording'],
    files=['pronunciation_recap_3015.pdf', 'Recording_instructions.pdf', 'Meeting9_EHUT_3015.pdf',
           'ASSIGNMENT 2 Pronunciation Test - page.txt'],
    overview=(
        h2('本节定位')
        + p('本讲把 2026-11-21 归档的三份语音材料（<i>pronunciation_recap_3015.pdf</i>、'
            '<i>Recording_instructions.pdf</i>、Meeting 9 幻灯片的语音部分）整合成一节。'
            '它直接服务 11 月 18 日的 ASSIGNMENT 2 发音测试与 Assignment 3 的口语交付。')
        + p('学完本节你应当能够：')
        + ck('用重音规则读出生词的重音位置（-ic / -tion / -graphy / 双音节动词）',
             '听辨并自主纠正 8 组最小对立（minimal pairs）',
             '用重音移动与语调改变同一句话的意思',
             '按 prosody（内容词重读、功能词弱化）读出自然节奏',
             '用 Camera / Teams / Zoom / Vocaroo 录制并交付链接')
        + p('前置：第 2 讲的朗读停顿、第 8 讲的作业通道。后续：Assignment 3 演讲的口语呈现。')
    ),
    detail=(
        h2('一、Prosody：语言的「音乐」')
        + p('说话时并非每个词都一样清楚：<b>content words（内容词）</b>被强调——音高抬高、时长拉长；'
            '<b>function words（功能词）</b>被弱化——重音降低、语速加快，英语词之间还会连读（linked），'
            '个别词甚至听不见。中文母语者的通病是每个音节等长等重，听起来「平」。')
        + h3('1.1 Pace 与 Pausing')
        + ul('Pace = 语速：慢下来表示冷静、强调；加快表示激动、进攻或想让内容一带而过。',
             'Pausing = 停顿：为效果（"wait for it"）、给听众思考时间、犹豫。')
        + h3('1.2 Stress 与 Rhythm')
        + p('句层：内容词重读（更响/更长/变音高），功能词弱读。同一句两种读法意思不同：'
            '<i>We are going to have to act if we want to live in a different world.</i>——'
            '重读 <b>act</b> 是「必须行动」，重读 <b>different</b> 是「世界必须不同」。')
        + h3('1.3 重音规则表（读新词就靠它）') + rows(*stress_rules)
        + cal('tip', 'IPA 提示', 'IPA 里重音符号 <code>ˈ</code> 标在重读音节<b>前</b>，二级重音是 <code>ˌ</code>。')
        + h3('1.4 同形异读（Homographs）与缩略语')
        + rows(('present（n. 礼物 / v. 呈现）', '/ˈprez.ənt/ vs /prɪˈzent/', '重音位置决定词性：名词读前，动词读后'),
               ('record（n. 记录 / v. 录制）', '/ˈrek.ɚd/ vs /rɪˈkɔːrd/', '录音测试里 record 多作动词，读后重音'))
        + p('缩略语有的逐字母读、有的当单词读：') + rows(*[(a, b, '') for a, b in abbrev])
        + cal('warn', '易错', 'CAD 不读 C-A-D，读 /kæd/——芬兰课堂材料专门点了这个词。')
        + h3('1.5 Emphasis：重音移位改变句义')
        + p('同一句 <i>I don\'t like the new operating system.</i> 重读不同词，句义不同：'
            '重读 <b>I</b> = 「（别人喜欢）我不喜欢」；重读 <b>don\'t</b> = 强烈否认；'
            '重读 <b>like</b> = 「不喜欢但也不是讨厌」；重读 <b>new</b> = 「旧的还行，新的不行」；'
            '重读 <b>operating system</b> = 「不是硬件问题」。')
        + h3('1.6 Pitch 与 Intonation')
        + ul('降调 falling：陈述、确定。', '升调 rising：疑问、迟疑。',
             '升+降 rise-fall：强烈情感。', '平调 flat：未说完、保留意见。',
             '示例：You like broccoli 四种语调 = 陈述 / 疑问 / 惊讶 / 试探。')
        + h2('二、Minimal Pairs：一个音换掉，意思全变')
        + p('最小对立对是发音自测的最小单元——只改一个音，意思就变。') + rows(*minimal_pairs)
        + h3('2.1 课程累计「你的词」（Your Words）')
        + p('易混对（minimal-ish）：') + rows(*[(a, b, '') for a, b in your_pairs])
        + p('同音词（homophones）：') + rows(*[(a, b, '') for a, b in homophones])
        + p('其他易错：change /\'tʃeɪndʒ/ vs chance /\'tʃæns/；nature → natural 的重音位移；'
            'thorough /\'θʌrəʊ/；dairy /\'deəri/（勿读成 diary）。')
        + h3('2.2 绕口令十条（Tongue Twisters）')
        + ul(*twisters)
        + h2('三、录音交付工作流（Recording instructions，2026-11-20）')
        + p('视频作业三选一：<b>Windows Camera</b>（只录摄像头，不录屏）；<b>Teams</b>（Calendar → Meet now → '
            'Start recording，录完在 Chat 里拿链接下载）；<b>Zoom</b>（桌面端，Share screen + Record，'
            '退出会议后自动转码存 Documents/Zoom 为 .mp4）。纯音频用 <b>Vocaroo</b>（网页版可直链分享）'
            '或 Windows Voice Recorder。最终交付 = 上传云盘 → 分享<b>链接</b>给老师。')
        + cal('warn', '11-18 发音测试', 'ASSIGNMENT 2 在 11 月 18 日当天 10:00–22:00 开窗（见第 8 讲与补遗）。'
              '考前用本讲 2.1–2.2 的 pairs 与 rules 过一遍「你的词」清单。')
    ),
    kws=K(
        ('prosody', '韵律', 'The music of language: stress, pace, pitch, rhythm.'),
        ('content word', '内容词', 'Carries meaning; gets stressed. Nouns, verbs, adjectives.'),
        ('function word', '功能词', 'Grammar glue; gets reduced. of, the, to, a.'),
        ('syllable stress', '音节重音', 'Which syllable is loudest: tech-NO-lo-gy.'),
        ('minimal pair', '最小对立对', 'Two words differing in one sound: ship/sheep.'),
        ('homophone', '同音词', 'Same sound, different spelling: buy/by/bye.'),
        ('homograph', '同形异音词', 'Same spelling, different sound & meaning: record.'),
        ('intonation', '语调', 'The melody of a sentence: rising for questions.'),
        ('pitch', '音高', 'How high or low the voice is.'),
        ('tongue twister', '绕口令', 'She sells sea shells — articulation drill.'),
        ('IPA', '国际音标', 'ˈ marks the stressed syllable: /tekˈnɑː.lə.dʒi/.'),
        ('Vocaroo', '网页录音工具', 'Records audio and gives a shareable link.'),
    ),
    examples=(
        qa('例 1 · 判断新词重音（三步法）',
           p('读出 <i>technology</i> 的重音位置。')
           + p('<b>解：</b>① 认词尾：<code>-logy</code> → 规则「-graphy/-logy/-nomy 倒数第三」。'
               '② 数音节：tech-no-lo-gy 共 4 个 → 重读第 2 个。'
               '③ 验证 IPA：/tekˈnɑː.lə.dʒi/，ˈ 在 no 前。答：tech-NO-lo-gy。'))
        + qa('例 2 · 用 minimal pair 纠音',
           p('总是把 sheep 读成 ship，怎么自测？')
           + p('<b>解：</b>① 定位对立音：/ɪ/（短）vs /iː/（长）。② 口型：/ɪ/ 松、嘴角不拉；'
               '/iː/ 紧、嘴角向两侧拉长。③ 最小对立句练习：<i>They ship the sheep from Wales.</i>'
               '（一句含两词，交替读）。④ 录音回听：ship 的元音是否更短更松。'))
        + qa('例 3 · 语调改义',
           p('把 <i>You like broccoli</i> 分别读成陈述与疑问。')
           + p('<b>解：</b>陈述 = 全句降调（broccoli 上降到低点）；疑问 = broccoli 后升调。'
               '升级版：rise-fall（升后骤降）= 「居然喜欢？」的惊讶。'))
    ),
    practice=(
        qa('练 1 · 重音规则应用',
           p('标出重音：analysis, circumference, construction, diagonal, diameter, direction, '
             'efficient, equipment, accelerate, accurate, reinforce, terminology。')
           + det('参考答案',
                 p('-ic / -tion / -ity 系：construc-TION, direc-TION, effi-CIENT, accelE-rate（动词末音节）, '
                   'accu-RATE（形容词第一音节——与 accelerate 对照！）。-graphy/-logy：termi-NO-lo-gy, geo-LO-gy。'
                   'analysis /əˈnæl.ə.sɪs/ 重音在第二音节。equipment 重音在首音节。reinforce 重音在第二音节。'
                   '——前后缀只决定重音「落点区」，最终以 IPA 校验。')))
        + qa('练 2 · 对立句朗读',
           p('每组读三遍：I saw three men / The tree has three apples / Just wink if you want another wing。')
           + det('要点', p('三组分别是 /θ–t/、/θ–t/、/ŋ–ŋk/。读 wink/wing 时体会舌根是否抵住软腭（ŋk 有爆破收尾）。')))
        + qa('练 3 · Frost 诗朗读（Meeting 9 课堂材料）',
           p('Whose woods these are I think I know. / His house is in the village though; / '
             'He will not see me stopping here / To watch his woods fill up with snow.')
           + det('步骤', st('先默读定意：哪几个词承载你要的意思（know? snow? stopping?）',
                            '标记强调词与弱读词',
                            '按意群朗读，注意 pace 与 pausing',
                            '换一种理解再读一遍（如「犹豫」版：慢速+平调）')))
        + qa('练 4 · 绕口令分级',
           p('从 10 条里选 3 条，慢-中-快三档各读一遍，录音对比。')
           + det('目标', p('快档不塌音：每个 target sound（如 aluminum 的 /l/、berry 的 /e–æ/）仍然可辨。')))
        + qa('练 5 · 三语气电梯演讲',
           p('Meeting 9 布置：把 elevator pitch 按三种语气交付（见第 4 讲练 2），'
             '本讲补一个「Unsure」版本要点。')
           + det('要点', p('Unsure = 句尾升调频繁 + 语速偏慢 + 填充词（um, kind of）增多。'
                          '对比 Confident 版本（降调收尾、零填充）录在同一段音频里，听辨差异。')))
    ),
    exam=(
        p(badge('bad', '必考') + '重音规则三大家族（-ic/-tion、-graphy/-logy/-nomy、双音节动词）——发音测试的高频题源。')
        + p(badge('bad', '必考') + '最小对立 /ɪ–iː/ 与 /æ–e/：中文母语者最大的两个坑，测试必查。')
        + p(badge('warn', '易错') + 'homograph 动名异读（present / record）——读错意思就答错。')
        + p(badge('warn', '易错') + '/v–w/ 与 /r–l/：vet–wet、feel–fear，需要口型与舌位刻意区分。')
        + p(badge('warn', '易错') + '缩略语 CAD 当词读 /kæd/，LED/CPU/USB 逐字母——不能混。')
        + p(badge('mute', '进阶') + 'prosody 自然度：内容词重读 + 功能词弱化 + 连读，是把「正确」读到「地道」的一层。')
    ),
    checklist=(
        h2('录音交付五步（任何工具通用）')
        + st('选工具：视频 → Camera / Teams / Zoom；纯音频 → Vocaroo / Voice Recorder',
             '录制：Zoom 记得桌面端 + Share screen；Teams 用 More actions 里的 Start recording',
             '落盘：Zoom 退出会议后存 Documents/Zoom（.mp4）；Teams 从 Chat 链接下载',
             '上传：传到云盘（SharePoint 等）',
             '分享：把链接（不是文件）发给老师')
        + h2('发音自测四步（考前 10 分钟）')
        + ck('过一遍「你的词」三张清单（易混对 / 同音词 / 其他）',
             '每对用最小对立句读两遍',
             '抽查 5 个 -tion/-logy 词的重音',
             '录 30 秒回听：content words 是否真的重读了')
    ),
    mapping=(
        h2('源文件对应')
        + rows(
            ('pronunciation_recap_3015.pdf', LINKED + 'link-09-…（' + TEXT + '同名 .txt）',
             'Minimal pairs 全部 8 组、Your Words 三清单、绕口令十条'),
            ('Meeting9_EHUT_3015.pdf', LINKED + '（slides 33-37 即此文件）',
             'Prosody / pace / stress rules / homographs / 缩略语 / emphasis / pitch & intonation / Frost 诗 / 三语气 pitch'),
            ('Recording_instructions.pdf', LINKED + 'link-12-…',
             'Camera / Teams / Zoom / Vocaroo 录音流程与交付方式'),
            ('ASSIGNMENT 2 Pronunciation Test - page.txt', TEXT,
             '发音测试的提交窗口与要求（11-18）'),
            ('补充拓展', '—', '重音规则表为幻灯片原内容的整理；语调四种类型为 recap + Meeting 9 合并表述'),
        )
    ),
)
# 插入到 supp-homework-map 之前
idx = next(i for i, x in enumerate(data['lectures']) if x['slug'] == 'supp-homework-map')
data['lectures'].insert(idx, lec9)

# =====================================================================
# 8) supp-homework-map · 材料对照更新
# =====================================================================
apply('supp-homework-map',
      [('mapping',
        p('<b>2026-11-21 更新：</b>「六、素材页：有清单、没有正文的那几页」里指向 SharePoint 的 16 份文档已全部抓回归档'
          '（<code>' + LINKED + '</code>，清单见同目录 <code>linked-manifest.json</code>），'
          '正文已并入第 2、3、4、5、6、8、9 讲。') 
        + rows(
            ('Chunking 任务 + Supercell 文章', LINKED + 'link-01/02', '并入 2.11–2.12'),
            ('五套食物词汇卡', LINKED + 'link-03…07', '并入 3.11a–e'),
            ('数据中心文章 B1/C1', LINKED + 'link-10/11', '并入 5.12'),
            ('Student A/B 角色卡', LINKED + 'link-13/14', '并入 7.13'),
            ('Meeting 9 幻灯片 + CEE Unit 6', LINKED + '（PDF）', '并入 5.11 / 7.14 / 9.x'),
            ('发音 recap + 录音说明', LINKED + 'link-09/12', '并入第 9 讲'),
        ))])

with io.open(CONTENT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
total = sum(len(x['html']) for x in data['lectures'])
print('[ok] 32632 now %d lectures, %d html chars' % (len(data['lectures']), total))
