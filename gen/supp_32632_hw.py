# -*- coding: utf-8 -*-
"""32632 English for HEBUT · 补遗一讲：十三次课的作业地图与考核节点"""

import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, pre, code, chips

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "32632"
PATH = os.path.join(SITE, "content", CID + ".json")


def qa2(title, *bodies):
    """允许多段 body 的 qa。"""
    return (
        '<div class="qa"><div class="q">'
        + title
        + "</div>"
        + "".join(str(b) for b in bodies)
        + "</div>"
    )


LEC = L(
    slug="supp-homework-map",
    tzh="补遗 · 十三次课的作业地图、交付通道与考核节点",
    ten="Homework Map, Submission Channels and Assessment Points Across 13 Meetings",
    keywords=[
        "homework",
        "return box",
        "Padlet",
        "Office Forms",
        "quiz",
        "Sanakirja",
        "DeepL",
        "pronunciation test",
        "recap material",
        "elevator pitch",
        "Yle News",
        "visual layout",
        "chunk",
        "word order",
    ],
    files=[
        "UNIT 1 Building Know-how/Meeting 1 homework.html",
        "UNIT 1 Building Know-how/Meeting 2 homework.html",
        "UNIT 1 Building Know-how/Meeting 3 homework.html",
        "UNIT 1 Building Know-how/Meeting 4 homework.html",
        "UNIT 1 Building Know-how/Meeting 5 homework.html",
        "UNIT 1 Building Know-how/Meeting 7 homework.html",
        "UNIT 2 Expressing Opinions/Meeting 8 homework.html",
        "UNIT 2 Expressing Opinions/Meeting 9 homework.html",
        "UNIT 2 Expressing Opinions/Meeting 11 homework.html",
        "UNIT 2 Expressing Opinions/Meeting 12 homework.html",
        "UNIT 3 Communicating Professionally/Meeting 13 homework.html",
        "Resources/Online dictionaries.html",
        "UNIT 1 Building Know-how/Food material.html",
        "UNIT 2 Expressing Opinions/GRAMMAR Online Exercises.html",
        "UNIT 2 Expressing Opinions/EXERCISE Pair work (agreeing and disagreeing).html",
        "UNIT 1 Building Know-how/EXERCISE Computers  Phones.html",
    ],
    overview="".join(
        [
            h2("本节定位"),
            p(
                "这门课的内容在正文里是按能力组织的：朗读与分块、词汇与语法、电梯演讲、图表描述、会议沟通。"
                "但课程实际是按「Meeting 1 到 Meeting 13」一节一节推进的，每一节的作业页分散在三个 UNIT 目录下，"
                "每页只有三五句，却各自带着不同的交付通道（Moodle return box、Padlet、Office Forms、Moodle 录音）"
                "和不同的截止方式（DL Sep 10、下次课前、下周四、11 月 18 日当天开放）。"
            ),
            p(
                "本讲把这些散页收成一张表：第几次课交什么、交到哪里、什么时候交、拿什么评判。"
                "它不重复正文已经讲透的语言点（语块、介词、词序、电梯演讲结构都在 1–6 讲里），只补三件正文没有的事："
                "<b>时间轴</b>、<b>交付通道的机械细节</b>、<b>两个有固定时间窗的考核节点</b>（发音测试与新闻幻灯片）。"
            ),
            p(
                "另外两类材料一并收录：一是 "
                + code("Resources/Online dictionaries")
                + " 给的词典与翻译工具清单及其使用纪律——它决定了你查词时该信哪个来源；"
                "二是 "
                + code("Food material")
                + " 与 "
                + code("EXERCISE Computers / Phones")
                + " 这类「素材页」，页面本身只有清单与外部链接，没有正文可抽，需要标注清楚以免误以为漏读。"
            ),
            h3("学完本讲你能够"),
            ul(
                "按会议编号复述整门课的作业链：哪一次课要交什么、交到哪个通道、截止口径是日期还是「下次课前」；",
                "在 Office Forms 里从零做出一个 2–4 题、任何人可作答、链接能贴进 Padlet 的测验，并说清四个最常见的配置错误；",
                "按「查词 / 查搭配 / 查语域 / 翻整句」四类需求选对词典与翻译工具，并解释为什么 wiki 词典与整句机翻在语言课上不能当答案；",
                "说清 11 月 18 日发音测试的时间窗（当天 10:00–22:00 在 Moodle 开放）、考试范围（课上材料）与两份复习材料（recap + Padlet 句子）；",
                "把一篇 Yle News 英文报道压成一页幻灯片：标题、作者、日期三要素齐备，版式经得起投影，配一分钟口头稿；",
                "识别三个口头产出（脱稿自我介绍、电梯演讲、新闻幻灯片）各自的时间长度与评分关注点，提前排练习次序。",
            ),
            cal(
                "tip",
                "和正文的分工",
                "正文六讲回答「这个语言点怎么用」；本讲回答「哪天交、交到哪、按什么标准算过」。"
                "复习语言点回 1–6 讲，赶截止日期看本讲第 1 节与第 2 节。",
            ),
        ]
    ),
    detail="".join(
        [
            h2("一、时间轴：十三次课各自留了什么"),
            p(
                "课程页面按会议编号建，实际存在作业页的是 1、2、3、4、5、7、8、9、11、12、13 共十一次；"
                "第 6 与第 10 次没有独立作业页（内容并入相邻会议的练习与展示），所以看到编号跳号不是漏页。"
                "下表按会议顺序排，最后一列是原文给的时间口径——原页大多写「下次课前」而不给日期，"
                "只有少数写了具体日（DL Sep 10、Fri Sep 25、November 18），这个差别在排计划时很关键。"
            ),
            tb(
                ("会议", "课堂主线", "留的作业", "时间口径"),
                (
                    "1",
                    "开课、自我介绍、学习资源",
                    "完成 Moodle 上的 Start of the Course Survey；完成 Baseline assignment；"
                    "想好芬兰的 pros and cons（喜欢什么 / 不喜欢什么）；下次带笔记本或平板，<b>不许用手机</b>",
                    "两项都标 DL Sep 10",
                ),
                (
                    "2",
                    "朗读与发音诊断",
                    "在 Padlet 上练单词朗读（下次一起复述）；自己找一篇短文本朗读，列出新词与难发音词，"
                    "例子里给的来源是 YLE news in English；把笔记带到课堂",
                    "下次课前",
                ),
                (
                    "3",
                    "分块阅读与技术文本",
                    "完成 reading exercise：Supercell（advanced）或 Supercell（simplified）二选一；"
                    "准备把这些短语用进对话；复习与 studies 相关的说法，下次<b>脱稿</b>谈自己的学习",
                    "下次课前；下次上半节是 ICC 课，三个河北组同堂，可用手机翻译",
                ),
                (
                    "4",
                    "线上课与专业领域练习",
                    "周五 Sep 25 8:15 的 Zoom 课，先测麦克风与摄像头；从自己其他课（物理、数学等）"
                    "选一道练习带到周四的课，课上一起看这道题的语言与措辞",
                    "Zoom 定在 Fri Sep 25 8:15AM",
                ),
                (
                    "5",
                    "CEE 练习与专业词表",
                    "完成 Moodle 上的 CEE exercises；把专业练习里出现的词汇填进指定在线文档（打开即编辑）；"
                    "语法：完成全部 online exercises，共九项——地点时间状语词序、肯定句词序、词序总览、"
                    "一般过去时否定句词序、一般现在时频率副词否定句词序、Wh- 问句、Yes/No 问句、间接问句、反意疑问句",
                    "下次课前",
                ),
                (
                    "7",
                    "词序语法与中华美食测验",
                    "语法仍是最上面那九项 online exercises；用 Office Forms 做一个关于中国传统与家乡食物的测验"
                    "（2–4 题、带选项、标出正确答案），把链接贴到 Padlet，下次课一起玩",
                    "下次课前",
                ),
                (
                    "8",
                    "技术文本、发音作业与电梯演讲起步",
                    "完成 CEE 材料里的 12E 与 12F；Moodle 上的发音作业——练习并<b>录音</b>，下次课前完成；"
                    "开始想电梯演讲脚本：职业意义上的自己有什么可讲；读 Data Centers 文本（另给简化版），"
                    "收集词与语块，准备下次讨论",
                    "下次课前",
                ),
                (
                    "9",
                    "图表描述与脚本定稿",
                    "玩页面上那个 graph 小游戏；到 British Council 网站读文本并完成 task 1–3；"
                    "找一张自己觉得有意思的图表，准备介绍并讨论；电梯演讲脚本定稿，按 slides 33–37 练，"
                    "下周四课上完成这项作业",
                    "FOR NEXT THURSDAY",
                ),
                (
                    "11",
                    "电梯演讲提交与介词",
                    "把电梯演讲上传并把链接分享到 Moodle 的 return box（技术说明在页面内链）；"
                    "介词练习 Ex.3–Ex.5：混合介词、时间表达里的介词、Moodle 上的介词练习",
                    "下次课前",
                ),
                (
                    "12",
                    "发音测试准备",
                    "准备 11 月 18 日的发音测试：当天在 Moodle 上 10:00–22:00 开放；范围是课上讲过的材料；"
                    "复习用 recap 材料加上 Padlet 里的句子",
                    "November 18",
                ),
                (
                    "13",
                    "新闻幻灯片与小组展示",
                    "从 Yle News 选一篇报道读完；做<b>一页</b> PowerPoint 或 Canva，写清标题、作者、日期，"
                    "注意这页的视觉版式；交到 return box；下次小组内展示，每人一分钟，之后讨论视觉呈现",
                    "下次课前；展示时长 1 分钟",
                ),
            ),
            cal(
                "warn",
                "「下次课前」不是「不用管」",
                "十一次作业里只有三项给了硬日期（Sep 10、Sep 25、Nov 18），其余全靠课堂节奏。"
                "这类课最容易出现的失误不是写错，而是<b>上课才发现要带东西</b>：Meeting 1 要带设备、"
                "Meeting 3 要能脱稿谈学习、Meeting 4 要带一道专业课练习、Meeting 9 要带一张图表。"
                "把这三条写进日历提醒（课前两小时），比事后补交省事。",
            ),
            h2("二、交付通道：五个口子，五种规矩"),
            p(
                "作业看着零散，交付通道其实只有五种。认错通道的代价是「做了但没交」，而这门课的口头与写作产出都靠这些通道留痕。"
            ),
            tb(
                ("通道", "本课用在哪", "机械要求"),
                (
                    "Moodle return box",
                    "电梯演讲（Meeting 11）、新闻幻灯片（Meeting 13）",
                    "上传文件并按要求分享链接；提交后可在同一处看到状态，别把文件留在本地",
                ),
                (
                    "Padlet",
                    "单词朗读（Meeting 2）、Office Forms 测验链接（Meeting 7）、发音测试复习句子（Meeting 12）",
                    "班级共享墙；贴链接时确认是可点的 URL，不是一段带空格的文字",
                ),
                (
                    "Office Forms",
                    "中华美食测验（Meeting 7）",
                    "必须是「Anyone can respond」；题量 2–4；每题 Points 保持默认 1",
                ),
                (
                    "Moodle 录音 / 测验",
                    "发音作业（Meeting 8）、发音测试（Meeting 12）",
                    "录音在 Moodle 内完成；测试有固定时间窗，当天 10:00–22:00",
                ),
                (
                    "Zoom",
                    "Meeting 4 的线上课",
                    "课前测麦克风与摄像头；这是唯一一次明确要求线上出席的课",
                ),
            ),
            p(
                "两个容易忽略的点。第一，return box 与 Padlet 不是二选一：电梯演讲要求上传到 return box，"
                "而测验要求把链接贴到 Padlet，两处都在用。第二，Padlet 上的内容会被当成课堂材料复用——"
                "发音测试的复习句子就来自 Padlet，所以你在 Padlet 上写下的朗读词，等于给自己出了复习题。"
            ),
            h2("三、Office Forms 做测验：八步与四个坑"),
            p(
                "Meeting 7 的作业页把技术步骤写全了，照抄即可。顺序不能颠倒，尤其是最后两步——"
                "很多人卡在「链接贴进 Padlet 但别人打不开」，原因几乎都在第 6、7 步。"
            ),
            st(
                "打开 Office Forms，选 Create a new quiz（新建测验），先给它起名，名字会成为分享标题；",
                "Add new question，题型选 <b>Choice</b>（选择题）；",
                "写题干，再写 2–4 个选项，并勾选其中正确的那一个；",
                "Points 保持默认 1（每题 1 分，四题满分 4 分）；",
                "确认总题量落在 2–4 题之间——这是作业要求，不是建议；",
                "点 Collect responses（收集回答）；",
                "在权限里选 <b>Anyone can respond</b>（任何人可作答）；",
                "点 Copy link 复制链接，粘到课程的 Padlet 上，并在贴子里说明这是哪一次课的什么测验。",
            ),
            tb(
                ("症状", "原因", "处理"),
                (
                    "同学点链接提示无权访问",
                    "第 7 步仍停在「仅组织内」或「仅我」，没改成 Anyone can respond",
                    "回 Collect responses 改权限，重新 Copy link 后再贴一次（旧链接不变但权限已生效，贴新链接更稳）",
                ),
                (
                    "分数显示成 0 或没有正确答案",
                    "第 3 步没勾正确选项，或第 4 步把 Points 改成了 0",
                    "回题目里补勾正确答案，Points 恢复 1",
                ),
                (
                    "贴到 Padlet 上是一长串不可点的文字",
                    "复制成了题干或备注，而不是 Copy link 的结果",
                    "重新 Copy link，直接粘贴，不要手打",
                ),
                (
                    "题量被扣分",
                    "只做 1 题，或做成 6 题的问卷",
                    "压到 2–4 题；多选题也按题数算，不按选项数算",
                ),
            ),
            cal(
                "tip",
                "内容怎么出题",
                "题目要求是「中国传统食物 + 你家乡的食物」。最省事又最像样的出法是三层：一层认名字（英文名对中文名）、"
                "一层认做法（steamed / stir-fried / deep-fried）、一层认场合（节日、日常、待客）。"
                "每层一题，正好三题，答案选项里放一个同族干扰项（比如 dumpling 与 wonton），课堂玩起来才有讨论。",
            ),
            h2("四、词典与翻译工具：选对来源，用对方向"),
            p(
                code("Resources/Online dictionaries")
                + " 这一页把工具分成三组，并给了使用纪律。分组本身比清单更有用：它其实在说「不同问题问不同来源」。"
            ),
            tb(
                ("组别", "具体来源", "适用"),
                (
                    "芬兰语—英语—芬兰语",
                    "Sanakirja.fi（用 LUT / LAB 账号登录可用全部功能）",
                    "芬兰语词条、芬兰语用法；这是本课唯一指定的芬英双向词典",
                ),
                (
                    "英英词典",
                    "Merriam-Webster（美式）、Merriam-Webster's Learner's Dictionary、Cambridge（英式）、"
                    "Oxford（英式）、Collins（英式）、Longman",
                    "查英文释义、搭配、语域、发音；Learner's 版释义最浅、例句最多，写作用它起步",
                ),
                (
                    "翻译工具",
                    "Sanakirja.fi translator、DeepL、Google Translate",
                    "只用来「看懂大意」；原文明确说它们准确度不够，芬英方向尤其弱",
                ),
            ),
            p(
                "页面上还有两句态度很强的话，必须照做，否则作业会被打回。第一句：对手机上的词典 app 与免费 wiki 类词典要保持批判，"
                "它们不一定是深入学习的好选择——wiki 词典能给译名，给不了搭配与语域。"
                "第二句：翻译工具可以用来打底，但不能替你写；<b>Always write your own texts yourself</b>。"
            ),
            tb(
                ("你要解决的问题", "先查哪个", "再看哪个", "不要用"),
                (
                    "这个词中文是什么意思",
                    "Learner's Dictionary（浅释义 + 例句）",
                    "Cambridge（看英式发音与常见搭配）",
                    "整句机翻后反推词义",
                ),
                (
                    "这个词在工程语境里怎么用",
                    "Cambridge / Collins 的例句与搭配栏",
                    "自己课文里的原句（CEE、Data Centers、Supercell）",
                    "只看中文对应词",
                ),
                (
                    "这句英文写得对不对",
                    "自己按课文句式重写一遍",
                    "用词典确认介词与搭配，不看整句翻译",
                    "把中文丢进 DeepL 直接交",
                ),
                (
                    "芬兰语材料看不懂",
                    "Sanakirja.fi（登录后全功能）",
                    "先抓主干再看细节，别逐词翻",
                    "用英文词典猜芬兰语词形",
                ),
            ),
            h2("五、两个有固定时间窗的节点"),
            h3("5.1 发音测试：11 月 18 日，当天 10:00–22:00"),
            p(
                "Meeting 12 的作业页把这件事说清了：测试在 <b>November 18</b>，当天在 Moodle 上从 <b>10:00 开到 22:00</b>，"
                "范围是课上讲过的材料，复习用 recap 材料加上 Padlet 里的句子。这三点合起来意味着："
                "它考的不是「你会不会读生词」，而是「课上练过的那些词与句子，你的读法有没有到位」。"
            ),
            ul(
                "时间窗是 12 小时，不是全天：错过 22:00 就没有补做入口，别把这件事排到晚上十点以后；",
                "复习材料只有两份且都在课内：recap（课上回顾材料）+ Padlet 上贴过的朗读词与句子，没有额外题库；",
                "范围是「课堂上覆盖过的材料」，所以 Meeting 2 的 Padlet 朗读、Meeting 8 的录音作业、"
                "课上纠正过的词，就是你的题库——翻自己那几次的笔记比找新词有用；",
                "录音类作业的共同陷阱是环境噪声与麦克风距离：先在 Moodle 里试录一段，确认能听清再正式录。",
            ),
            h3("5.2 Yle News 幻灯片：一页、三要素、一分钟"),
            p(
                "Meeting 13 要求从 Yle News 选一篇报道：Yle 是芬兰的公共广播公司（public service media company），"
                "它把主要新闻做成英文版，所以这是本课唯一「真实新闻语料」的来源。作业形态是一页幻灯片，"
                "写清标题、作者、日期，<b>注意版面</b>，交到 return box，下次小组内每人讲一分钟，之后讨论视觉呈现。"
            ),
            tb(
                ("要素", "要求", "为什么被单列出来"),
                (
                    "标题",
                    "报道原标题，不改写",
                    "课堂讨论会对照原文，改写等于换了论点",
                ),
                (
                    "作者",
                    "署名作者；只有通讯社署名就写通讯社",
                    "新闻的可信度判断从这里开始，也是引用规范的一部分",
                ),
                (
                    "日期",
                    "报道发布日",
                    "同一事件不同日期的报道结论会变，缺日期无法核对时效",
                ),
                (
                    "版面",
                    "一页之内，字号能投影看清，图文不互相压",
                    "评分明确提到 visual layout，最后一栏讨论的就是「视觉呈现」",
                ),
            ),
            cal(
                "exam",
                "三个口头产出别混为一谈",
                "课程里共有三次开口：Meeting 3 的脱稿谈学习（无准备稿，考的是能不能连续说）、"
                "Meeting 11 的电梯演讲（有定稿脚本，考的是结构与 60 秒控制）、"
                "Meeting 13 的新闻幻灯片（一页视觉 + 一分钟讲解，考的是信息压缩）。"
                "三者的准备方式完全不同：第一个靠背语块，第二个靠改稿，第三个靠删字。",
            ),
            h2("六、素材页：有清单、没有正文的那几页"),
            p(
                "有几页打开只有清单与外链，没有可读正文，容易被误判成「内容缺失」。实际它们的用途是「指路」，"
                "正文里已经把对应的语言点讲过了。"
            ),
            tb(
                ("页面", "页面里有什么", "怎么用"),
                (
                    "Food material",
                    "六份食物词汇表（蔬菜 33、谷物豆类坚果 33、水果浆果 45、动物制品与替代品 33、厨房用具 33、"
                    "烹饪动词 24）加「菜品」一节；四个外部测验（烹饪与厨具 level 2、食物与饮料 level 3、"
                    "果蔬香草香料 level 2、烹饪动词）",
                    "词汇本体是图片册，页面只给入口；本讲与第 3 讲按主题收过词，练习去外部测验做",
                ),
                (
                    "EXERCISE Computers / Phones",
                    "二选一：Option A 电脑（部件、组件），Option B 手机（部件、移动连接）",
                    "选一个方向把部件名认全即可，两页都只有外链，没有题面",
                ),
                (
                    "EXERCISE Pair work (agreeing and disagreeing)",
                    "A/B 两人的材料入口，先分角色再各开各的",
                    "课堂内完成；正文第 6 讲已给同意与反对的句式梯度",
                ),
                (
                    "GRAMMAR Online Exercises",
                    "两组介词练习：at/in/on 在句子中的用法、at/in/on 在时间表达中的用法",
                    "与 Meeting 11 的 Ex.3–Ex.5 是同一主题的延伸，正文第 3 讲已给判断规则",
                ),
            ),
            cal(
                "warn",
                "外部链接不在本站范围内",
                "Food material 的六份词汇册是图片/PDF 形态，四个测验在 Cambridge 等外部站点，"
                "这两个来源都不随本站离线打包。也就是说：清单与主题已收录，图片与题面要在有网时打开原页。"
                "这不影响复习——课上真正考的是你能不能用这些词说出一段话，而不是刷完几套外部测验。",
            ),
        ]
    ),
    kws="".join(
        [
            h2("关键词"),
            K(
                ("homework", "作业", "Homework for lesson 2 — the page title pattern of every meeting."),
                ("return box", "提交箱", "Upload your elevator pitch and share the link in the Moodle return box."),
                ("Padlet", "共享墙", "Paste the link to your quiz on our Padlet."),
                ("quiz", "测验", "Create a quiz about traditional Chinese and your local foods."),
                ("Collect responses", "收集回答", "Click Collect responses, then select Anyone can respond."),
                ("Points", "分值", "Keep Points at 1 (the default) for each question."),
                ("baseline assignment", "基线作业", "The baseline assignment is due on Sep 10."),
                ("chunk", "语块", "Collect words and chunks before you discuss the text."),
                ("elevator pitch", "电梯演讲", "A 60-second professional self-introduction."),
                ("word order", "词序", "Word order in statements with expressions of place and time."),
                ("preposition", "介词", "at, in, on — prepositions of time and place."),
                ("recap material", "回顾材料", "Use the recap material plus the sentences from Padlet."),
                ("public service media", "公共广播", "Yle is the Finnish public service media company."),
                ("visual layout", "版面 / 视觉版式", "Pay attention to the visual layout of this slide."),
                ("gist", "大意", "Translation tools are good for the gist, not for accuracy."),
                ("field-specific", "专业领域的", "Choose one exercise from your other courses (physics, math)."),
            ),
        ]
    ),
    examples="".join(
        [
            h2("例 1 · 从空白 Forms 到可玩链接，走一遍并对照错误"),
            p(
                "把第 3 节的八步压成一条时间线，附带每一步「做错的症状」，方便自查。假设题目是三道关于中国食物的选择题。"
            ),
            pre(
                "新建测验 -> 命名 Chinese food quiz\n"
                "Add new question -> Choice\n"
                "  题干: Which of these is usually steamed?\n"
                "  选项: dumpling / steamed bun / fried rice / roast duck   (正确: steamed bun)\n"
                "  Points: 1\n"
                "重复两次，总题数控制在 3（要求 2-4）\n"
                "Collect responses -> Anyone can respond -> Copy link\n"
                "Padlet 贴子: Meeting 7 quiz - 3 questions - please try before Thursday"
            ),
            tb(
                ("步骤", "做对了的表现", "做错了会看到"),
                ("命名", "Padlet 上显示的标题就是测验名", "贴出来是 Untitled quiz，同学不知道点哪个"),
                ("选题型", "选项前有单选圆点", "变成填空或评分题，无法自动判分"),
                ("标正确答案", "题目旁出现对勾", "答题后所有人都显示 0 分"),
                ("Points = 1", "满分等于题数", "满分 0 分或 40 分"),
                ("题量 2–4", "符合作业要求", "超出范围按未达标处理"),
                ("Collect responses", "出现分享面板", "找不到 Copy link 按钮"),
                ("Anyone can respond", "陌生账号也能打开", "提示需要登录或无权访问"),
                ("Copy link + 粘贴", "Padlet 上是蓝色可点链接", "一长串黑色文字，点不开"),
            ),
            cal(
                "tip",
                "验收方式",
                "贴出去之前，用浏览器无痕窗口打开那个链接自测一次：能答题、能提交、能看到对错，三条都成立才算完成。"
                "无痕窗口没有你的登录态，正好模拟同学的环境。",
            ),
            h2("例 2 · 查一个工程词：bearing 的四步流程"),
            p(
                "课文里出现 bearing，中文直觉是「轴承」，但它还能表示「举止」与「方位」。按第 4 节的选源规则走一遍，"
                "四步之内能把词定死，而且每一步都不依赖整句机翻。"
            ),
            st(
                "先查 Learner's Dictionary：拿到最浅释义（a part of a machine that supports a moving part）与一个例句，"
                "确认机械义是主义；",
                "再查 Cambridge：看英式发音（近似 BEH-ring，词尾是 ng 的鼻音）与常见搭配（ball bearing、roller bearing），"
                "确认它在复合名词里怎么出现；",
                "回课文原句，把搭配抄下来：<code>the bearing was replaced</code> 说明它是可数名词、可被替换的零件；",
                "最后用 Sanakirja.fi 反查芬兰语对应词，确认在芬兰语材料里它落在同一个义项上（避免把「方位」义带进来）。",
            ),
            tb(
                ("来源", "给你的东西", "这一步的判据"),
                ("Learner's", "浅释义 + 一个生活化例句", "主义是不是机械义"),
                ("Cambridge", "英式音标 + 搭配", "作定语时的固定搭配形式"),
                ("课文原句", "真实语境的句法位置", "可数性、可替换性、与动词的搭配"),
                ("Sanakirja.fi", "芬兰语对应词", "跨语言义项是否收敛到同一处"),
            ),
            p(
                "反例也值得记：如果第一步就去 DeepL 翻「轴承坏了」，会得到一句语法通顺但搭配奇怪的英文，"
                "而你说不出它为什么怪——因为机翻替你做完了选择，你失去了判据。查词的目的是拿到判据，不是拿到句子。"
            ),
            h2("例 3 · 一页 Yle 幻灯片加一分钟讲稿"),
            p(
                "Meeting 13 的成品是一页幻灯片加一分钟口头。一页能放的东西很少，所以取舍规则要提前定：标题三要素、"
                "三条要点、一条「为什么和我们有关」。下面这版可以直接当模板改。"
            ),
            pre(
                "标题栏: <article title>  (as published, not rewritten)\n"
                "副行:   By <author> - <date>  |  Yle News\n"
                "要点 1: 发生了什么（一句，含数字或地点）\n"
                "要点 2: 为什么发生 / 谁受影响（一句）\n"
                "要点 3: 一个可讨论的问题（一句，留给听众）\n"
                "页脚:   Source: Yle News, <date>   (小字号)\n"
                "视觉:   左文右图或上文下图，留白不少于四分之一页；正文不小于 20 pt"
            ),
            tb(
                ("时间段", "说什么", "时长控制"),
                ("0:00–0:10", "报道标题 + 作者 + 日期，一句交代来源", "10 秒，不要念全文"),
                ("0:10–0:40", "三条要点按顺序讲，每条一句", "每条 10 秒"),
                ("0:40–0:55", "为什么这条新闻和工程 / 我们专业相关", "这段是加分项"),
                ("0:55–1:00", "把要点 3 的问题抛给听众", "停住，别再补充"),
            ),
            cal(
                "idea",
                "为什么强调版面",
                "同一页内容，字号 14 pt 投影后基本看不清，正文一多听众就开始读屏而不是听你讲。"
                "把字删到 20 pt 还能放下，是「信息已被压缩」的可靠信号；这也是评分里单列 visual layout 的原因。",
            ),
        ]
    ),
    practice="".join(
        [
            h2("练习"),
            ol(
                "不看表，按会议编号写出十一次作业各自交到哪个通道（Moodle return box / Padlet / Forms / Moodle 录音 / Zoom），"
                "写完再对第 1 节与第 2 节。",
                "把 Meeting 5 与 Meeting 7 的九项语法练习按「词序」与「问句」两类重排，说明为什么反意疑问句被放在问句一组。",
                "用 Office Forms 做出三题食物测验，按第 3 节八步配置，用无痕窗口自测并截图留证。",
                "取一个你专业课的术语（如 torque、viscosity、impeller），按例 2 的四步流程查一遍，写下四个来源各给了什么判据。",
                "把一段中文作业描述（三句）先用 DeepL 翻，再自己按课文的句式重写，逐句标出机翻在搭配或语域上错在哪。",
                "选一篇 Yle News 英文报道，按例 3 的模板做一页幻灯片，掐表讲一次，记录实际时长与超时的那一句。",
                "为 11 月 18 日的发音测试列一份 20 词清单：从 Meeting 2 的 Padlet 词、Meeting 8 的录音作业、课上被纠正过的词里各取若干。",
                "写一份「课前两小时」提醒清单，覆盖 Meeting 1 的设备、Meeting 3 的脱稿、Meeting 4 的专业课练习、Meeting 9 的图表。",
            ),
            qa2(
                "Meeting 6 与 Meeting 10 为什么没有作业页？",
                p(
                    "页面只建在 1、2、3、4、5、7、8、9、11、12、13 上，第 6 与第 10 次的内容并入了相邻会议的练习与展示"
                    "（例如 Meeting 3 明确说下次上半节是 ICC 课）。这不是漏读，也不需要去找替代页——"
                    "把相邻两次的作业按时间顺序接上即可。"
                ),
            ),
            qa2(
                "said「下次课前」到底指哪一天？",
                p(
                    "原文只写 before the next lesson，没有日期。可靠读法是：把当次课的下课时间当作起点，"
                    "下一次同周次的课当作终点，中间不含周末。若遇到线上课或展示周（Meeting 4、9、13），"
                    "以页面上写明的那个日子为准（Sep 25 / next Thursday / 小组展示当天）。"
                ),
            ),
            qa2(
                "发音测试能补考吗？",
                p(
                    "页面只写了当天 10:00–22:00 开放、范围是课上材料，没有提供补做入口，也没有给替代日期。"
                    "按「只有一次窗口」来安排：把复习放在测试前两天，别押在最后两小时——录音类任务在截止前集中提交最容易出设备问题。"
                ),
            ),
        ]
    ),
    exam="".join(
        [
            h2("考核怎么看"),
            p(
                "这门课没有纸面期末，成绩来自过程产出。把页面里出现过的评分口径归拢，实际被看的是四类东西："
                "课堂参与与准备（能不能脱稿谈、有没有带该带的东西）、发音（作业录音与 11 月 18 日测试）、"
                "口头产出（电梯演讲、新闻幻灯片各一分钟）、以及按时交付（通道对不对、链接能不能打开）。"
            ),
            tb(
                ("产出", "形式", "看什么", "常见失分"),
                (
                    "发音作业 / 发音测试",
                    "Moodle 录音；测试当天 10:00–22:00",
                    "课上材料的读法是否到位，词重音与句重音",
                    "错过时间窗；环境噪声盖住尾音；只练生词不练句子",
                ),
                (
                    "电梯演讲",
                    "定稿脚本 + 上传 return box + 分享链接",
                    "60 秒内说清「我是谁、我能做什么」；结构清楚",
                    "超时；堆履历不讲能力；链接未分享",
                ),
                (
                    "新闻幻灯片",
                    "一页 PPT/Canva + 一分钟讲解",
                    "标题/作者/日期齐备；版面可投影；一分钟内讲完",
                    "改写标题；缺日期；字号过小；念稿",
                ),
                (
                    "日常作业",
                    "Padlet、Forms、九项语法练习、CEE 12E/12F",
                    "是否按时、是否按格式（题量、权限、链接）",
                    "通道错、权限没开、题量越界",
                ),
            ),
            cal(
                "exam",
                "优先级排序",
                "如果时间只够做三件事：先把 11 月 18 日的发音复习材料（recap + Padlet 句子）过两遍，"
                "再把电梯演讲脚本改到 60 秒整，最后把新闻幻灯片压到一页。"
                "这三项都是「有时间窗或一次性交付」的产出，补不回来；语法练习与词汇表可以随时补。",
            ),
        ]
    ),
    checklist="".join(
        [
            h2("自查清单"),
            ck(
                "能按会议编号说出十一次作业各自的内容与通道，不看表；",
                "知道只有 Sep 10、Sep 25、Nov 18 三个硬日期，其余是「下次课前」；",
                "Meeting 1 的「带笔记本或平板，不许用手机」记在日历里；",
                "能用 Office Forms 在十分钟内做出 2–4 题、Anyone can respond、链接可点的测验；",
                "知道 Forms 四个常见坑：权限、正确选项、Points、题量；",
                "查词时先 Learner's 拿浅释义、再 Cambridge 拿搭配，不用整句机翻反推词义；",
                "能说出 wiki 词典与翻译工具在这门课里为什么不能当答案（缺搭配与语域判断）；",
                "11 月 18 日的窗口是 10:00–22:00，复习材料只有 recap 与 Padlet；",
                "Yle 幻灯片三要素（标题、作者、日期）与版式要求都写进了模板；",
                "三个口头产出（脱稿谈学习 / 电梯演讲 / 新闻幻灯片）各自的时长与准备方式分得清；",
                "知道 Food material 与 Computers/Phones 是清单页，图片与外部测验不在离线包内；",
                "所有交付都自测过一次：链接在无痕窗口能打开、录音能听清、文件在 return box 里有状态。",
            ),
        ]
    ),
    mapping="".join(
        [
            h2("材料对照"),
            p(
                "本讲只做归拢与补白，不重复正文的语言点。下表说明每份材料被用在哪里、抽出了什么、以及有没有缺口。"
            ),
            tb(
                ("材料", "抽取内容", "去处 / 覆盖说明"),
                (
                    "Meeting 1 / 2 / 3 / 4 / 5 homework",
                    "五页作业原文（Survey、Baseline、Padlet 朗读、Supercell、Zoom、CEE、九项语法）",
                    "第 1 节时间轴逐条收录；语言点已在第 2、3 讲讲过",
                ),
                (
                    "Meeting 7 / 8 / 9 / 11 / 12 / 13 homework",
                    "六页作业原文（Forms 测验、12E/12F、录音、电梯演讲、图表、介词、发音测试、Yle）",
                    "第 1 节时间轴 + 第 3 节 Forms 八步 + 第 5 节两个节点；电梯演讲结构与图表描述在正文第 4、5 讲",
                ),
                (
                    "Resources/Online dictionaries",
                    "三组工具清单（Sanakirja、六部英英词典、三个翻译工具）与两句使用纪律",
                    "第 4 节整节；选源表为新增，正文未覆盖",
                ),
                (
                    "Food material",
                    "六份词汇表标题与词量、菜品一节、四个外部测验名称",
                    "第 6 节素材页表；词汇本体是图片册，正文第 3 讲按主题收过词",
                ),
                (
                    "EXERCISE Computers / Phones",
                    "Option A 电脑 / Option B 手机 两条路径与外链",
                    "第 6 节素材页表；无题面可抽",
                ),
                (
                    "EXERCISE Pair work (agreeing and disagreeing)",
                    "A/B 双材料、先分角色的流程",
                    "第 6 节素材页表；句式梯度见正文第 6 讲",
                ),
                (
                    "GRAMMAR Online Exercises",
                    "两组 at/in/on 介词练习",
                    "第 6 节素材页表；判断规则见正文第 3 讲",
                ),
                (
                    "UNIT 2 的两份 DIALOGUE 与 Meeting 课件正文",
                    "对话全文与课件段落",
                    "已由正文第 2、5、6 讲覆盖，本讲不重复",
                ),
                (
                    "—（缺口说明）",
                    "Food material 的六份词汇册为图片/PDF，四个测验在 Cambridge 等外部站点",
                    "离线站内不收图片与外部题面；清单与主题已收录，需要时按原页入口打开",
                ),
            ),
            cal(
                "tip",
                "两处口径差异，别被绕住",
                "第一，作业页写「下次课前」的地方，正文与总览页可能按周次表述，两者不冲突——以本讲第 1 节的时间口径为准。"
                "第二，发音测试只出现在 Meeting 12 的作业页与课程总页，正文第 1 讲提到过考核构成但没有时间窗，"
                "时间窗以 11 月 18 日 10:00–22:00 为准。",
            ),
        ]
    ),
)


with io.open(PATH, encoding="utf-8") as fh:
    data = json.load(fh)

before = len(data["lectures"])
old = [i for i, x in enumerate(data["lectures"]) if x["slug"] == LEC["slug"]]
if old:
    # 可重复运行：已存在就替换（避免重复追加），并保留原位置
    data["lectures"][old[0]] = LEC
else:
    data["lectures"].append(LEC)

with io.open(PATH, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

print(
    "[ok] %s lectures %d -> %d, new html %d chars"
    % (CID, before, len(data["lectures"]), len(LEC["html"]))
)
