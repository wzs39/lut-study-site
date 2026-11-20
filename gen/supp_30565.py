# -*- coding: utf-8 -*-
"""30565 数学A · 补遗一讲：12 套习题与解答册（未被引用的源文件）"""

import os, sys, json, io

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import L, h2, h3, p, ul, ol, ck, st, tb, K, cal, qa, det, pre, code, chips

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "30565"
PATH = os.path.join(SITE, "content", CID + ".json")
kw = K  # 术语表：10–16 条，列数与 genlib.K 一致


def qa(title, *bodies):
    """本脚本内的 qa：允许一次传多个段落，内部拼成一个 body。"""
    from genlib import qa as _qa
    return _qa(title, chr(10).join(str(b) for b in bodies))


LEC = L(
    slug="supp-exercises",
    tzh="补遗 · 12 套习题课题目与解答册：六类题型与标准写法",
    ten="Exercise Sets 1-12 and the Solutions Booklet: Six Problem Types and Standard Wording",
    keywords=[
        "exercise set",
        "double inclusion",
        "contrapositive",
        "proof by contradiction",
        "counterexample",
        "binomial coefficient",
        "induction step",
        "base case",
        "divisibility",
        "Euclidean algorithm",
        "multiplicative inverse",
        "two-line notation",
    ],
    files=[
        "01-exercise-solutions.pdf",
        "02-exercise-solutions.pdf",
        "03-exercise-solutions.pdf",
        "04-exercise-solutions.pdf",
        "05-exercise-solutions.pdf",
        "06-exercise-solutions.pdf",
        "07-exercise-solutions.pdf",
        "08-exercise-solutions.pdf",
        "09-exercise-solutions.pdf",
        "10-exercise-solutions.pdf",
        "02-exercise.pdf",
        "02-lesson-WB.pdf",
        "03-lesson-WB.pdf",
        "04-lesson-WB.pdf",
        "05-lesson-WB.pdf",
        "07-lesson-WB.pdf",
        "routine-exercises-solutions.pdf",
        "01_Homework info.html",
    ],
    # ------------------------------------------------------------------ overview
    overview="\n".join(
        [
            h2("本节定位"),
            p(
                "前 13 讲把 lecture 1–8 的定义、定理与算法讲完了，但整套练习材料一直没有进正文："
                "<code>02-exercise</code> 到 <code>12-exercise</code> 是每周带到 exercise class 上的题面，"
                "<code>01-exercise-solutions</code> 到 <code>10-exercise-solutions</code> 是课后发下来的标准解答。"
                "正文只引用了 lesson PDF、Lecture 1–8 的讲义与历年考试卷，练习册恰好落在缝里。"
            ),
            p(
                "本讲把这些文件收进来，做三件正文没做的事：把六十道题归成六类、每类给出可迁移的解法步骤、"
                "把解答册里最值得照抄的英文句式挑出来。板书版（<code>-WB</code>）与例行练习库也一并交代清楚，"
                "以后复习时不必再猜它们是什么。"
            ),
            p("学完本讲你能够："),
            ck(
                "能够把任意一道练习判进「集合与逻辑 / 证明 / 计数 / 归纳 / 整除与模 / 函数与关系」六类之一，并说出该类的第一步动作；",
                "能够用双向包含模板写出集合等式证明，并用一句话说明为什么不能拿特例代替证明；",
                "能够区分「原命题、逆命题、逆否命题、反证」四种写法，判断一段证明是否 sound；",
                "能够在 <code>exercise-solutions</code> 里找到与当前题目同型的标准解答，照它的句式重写自己的答案；",
                "能够说明 <code>-WB</code> 文件为什么没有新知识，以及 <code>routine-exercises-solutions</code> 的正确用法。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ detail
    detail="\n".join(
        [
            h2("一、这批文件的实际结构"),
            p(
                "先把数量对齐。目录里 <code>02-exercise.pdf</code> 到 <code>12-exercise.pdf</code> 共 11 份题面，"
                "页眉写的集号依次是 2 到 11，另有一份 <code>13_Week 11_1_12-exercise.pdf</code> 与 "
                "<code>12-exercise.pdf</code> 内容完全相同（只有首行 <code>SOURCE:</code> 不同）。"
                "解答册只有 <code>01</code> 到 <code>10</code>，也就是 set 1–10 有解、set 11 与 set 12 没有解答。"
                "所以「12 套题」是集号 1–12，题面缺 set 1（只在第一次习题课当堂发），解答缺 set 11 与 set 12。"
            ),
            p(
                "还有两处原文自身的不一致，读的时候不要被绕进去："
                "<code>02-exercise.pdf</code> 的页眉是「Exercise set 2」，文件名却比集号小 1，全套都是这个偏移；"
                "<code>12-exercise.pdf</code> 的页眉仍写「Exercise set 11」，但文件名与题目要求的上交周（23.–27.11.）"
                "都指向第 12 套，最可能是排版时页眉没改。判断集号时以「页眉的集号 + 上交周次」两者一起看，"
                "只看文件名会错位一格。"
            ),
            p(
                "每套题固定 6 题。解答册 <code>08-exercise-solutions.pdf</code> 里会出现第 7 个 "
                "<code>Exercise</code> 标题，那是正文里「(n + 1) over 2」被拆行后误识别成标题，实际仍是 6 题。"
            ),
            h3("1.1 上交节奏"),
            ul(
                "<code>02</code>（set 2）7.–11.9.；<code>03</code>（set 3）14.–18.9.；"
                "<code>04</code>（set 4）21.–25.9.；<code>05</code>（set 5）28.9.–2.10.；"
                "<code>06</code>（set 6）5.–9.10.；<code>07</code>（set 7）12.–16.10.；"
                "<code>08</code>（set 8）26.–30.10.；<code>09</code>（set 9）2.–6.11.；"
                "<code>10</code>（set 10）9.–13.11.；<code>11</code>（set 11）16.–20.11.；"
                "<code>12</code>（set 12）23.–27.11.",
                "set 1 的说明是「To be done during the first week's exercise class」，属于当堂练习，"
                "并且明确要求「Do these exercises without a calculator!」，答案写精确值，例如写 2/3 而不是 0.6667。",
            ),
            h3("1.2 计分规则（set 2 原文给出的三条）"),
            p(
                "从 set 2 起，题面开头都写着同一段规则：参加小组 1 分、上台在白板前讲（一部分）题 1 分、"
                "每道标为 done 的题 1 分。关键是「标 done」的含义被原文解释得很松："
                "「It can be a partial solution, or it can be what you tried even if it didn't work.」"
                "也就是说白板上只要有东西可写就算，包括走错的尝试。"
            ),
            p(
                "这条规则直接决定了练习的用法：先自己动手写，写不下去也把卡住的地方写出来，"
                "再到课上对照别人的白板与助教的说法修正。解答册是周五发布、用来对照的，不是用来抄的"
                "（set 4 开头原文：「Remember to read the solutions to homework which are posted on Fridays at 5PM "
                "and compare with your own.」）。"
            ),
            h3("1.3 每套末尾的 hints"),
            p(
                "每套解答册最后一页都有「Hints and things to pay attention to」。它比题面更接近考点，"
                "因为那是出题人写下的「这题最容易被搞错的地方」。例如 set 2 的提示里有三条值得记住："
                "「if x ∈ A and B ∈ C, it doesn't necessarily mean that x ∈ C」、「difference between ∈ and ⊆」、"
                "「to show that A = B make sure to prove both A ⊆ B and B ⊆ A」。"
                "复习时先读 hint，再回看自己错在哪一类，比刷题本身有效。"
            ),
            h2("二、六类题型：判别信号与要调用的定义"),
            p(
                "六十道题看起来杂，其实按「第一步该做什么」可以分成六类。下表左列是类别，第二列是它出现在哪几套，"
                "第三列是看到题干里什么词就该归到这一类，第四列是必须立刻写出来的定义。"
            ),
            tb(
                ("类别", "出现套数", "判别信号", "第一步要写出的定义"),
                (
                    "集合与逻辑",
                    "set 2、3、4",
                    "「List the elements」「A ⊆ B?」「A ∩ B」「family of sets」「A × B」",
                    "∈ 与 ⊆ 的定义；∪、∩、\\、∁、△ 的定义",
                ),
                (
                    "证明",
                    "set 2、5、6、9",
                    "「Prove」「Show that」「Is this a sound proof」「is false」",
                    "命题的符号化；双向包含；逆否；反证；反例",
                ),
                (
                    "计数",
                    "set 8",
                    "「In how many ways」「selection」「Prove for natural numbers n」",
                    "C(n, k) = n!/(k!(n−k)!)，带重复 C(n+k−1, k)",
                ),
                (
                    "归纳",
                    "set 9",
                    "「for any integer n ≥ 2」「Prove by induction」「is it missing details」",
                    "base case；induction assumption；把 n = k 的结果代进 n = k+1",
                ),
                (
                    "整除与模",
                    "set 5、10、11、12",
                    "「a | b」「gcd」「ax + by = c」「mod」「remainder」",
                    "a | b ⇔ ∃k ∈ Z, b = ka；Euclid 算法；同余两边可加可乘",
                ),
                (
                    "函数与关系",
                    "set 3、4、6、7",
                    "「injection」「surjection」「permutation」「RS」「R⁻¹」「cardinality」",
                    "单射/满射；合成 RS 的顺序；two-line notation",
                ),
            ),
            p(
                "这张表不是分类学，而是行动表：题干里出现哪个信号，就先把对应那一行的定义抄在纸上，"
                "后面每一步都用得上。练习册里失分最多的情况不是不会算，而是没写出定义就开始变形，"
                "变到一半忘了自己允许做什么。"
            ),
            h2("三、逐类的通用解法"),
            h3("3.1 集合与逻辑：先数元素，再判关系"),
            p(
                "集合题的第一动作永远是「把元素列清楚」。三种花招要认出来："
                "第一，<code>{10, {20, {2}, {}, 2}, 3}</code> 这种嵌套，元素是逗号分隔的那几项，"
                "要靠配对括号找出内层集合从哪开始到哪结束（set 2 Ex1(b)：元素是 10、集合 {20, {2}, {}, 2}、3）；"
                "第二，<code>{{5}}</code> 只有一个元素，那个元素是集合 {5}，与 <code>{5}</code> 不同；"
                "第三，<code>∅</code> 没有元素，但 <code>{∅}</code> 有一个元素。"
            ),
            p("往下是三个不同的判定动作，混用就会全错："),
            ol(
                "X ⊆ Y：取 X 的<b>每个</b>元素，逐个检查是否属于 Y。反例只要一个元素就够。",
                "X ∈ Y：不看 X 的内部，只看 Y 的元素列表里有没有一项<b>等于</b> X。"
                "set 2 Ex4 的 (c) 与 (d) 就是同一件事的两种写法：<code>{1, 2, {1, 2}}</code> 里既有 1、2 又有集合 {1, 2}，所以 ⊆ 与 ∈ 同时成立。",
                "集合族：先确认每个元素本身是集合（set 3 Ex1(a) 的毛病就是混进了数字 5），再看 ∪A 与 ∩A。"
                "要构造「∪A 等于给定集合」的族，把它拆成若干块即可；要构造「∩B = {a, b, c}」的 9001 个集合，"
                "就让 a、b、c 出现在每一个集合里，其余元素各不相同。",
            ),
            p(
                "笛卡尔积的检验有一个非常快的判据：若 P = A × B，那么只要 (a, b₁) 与 (a′, b₂) 都在 P 里，"
                "就说明 a、a′ ∈ A 且 b₁、b₂ ∈ B，于是 (a, b₂) 也必须在 P 里。"
                "set 3 Ex3(a) 正是用这条否掉：由 (b, a) 得 b ∈ A，由 (f, b) 得 b ∈ B，于是 (b, b) 必须出现，"
                "而它不在集合里。写这类「不是笛卡尔积」的题，只需指出这一个缺失的元素。"
            ),
            p(
                "幂集的元素个数是 2^n，这是所有「P(C) 有几个元素」问题的唯一入口。"
                "set 3 Ex2(c) 要求至少 5 个、至多 10 个，逐个试：n = 2 得 4、n = 3 得 8、n = 4 得 16，"
                "只有 n = 3 落在区间里，答案就是「任意三元集合」。"
            ),
            p(
                "逻辑部分（set 4 Ex4–6）要会用真值表，也要会认出「骑士与无赖」这种语义题："
                "骑士说真话、无赖说假话，把每句话写成命题再检查真假一致性即可，"
                "set 4 给了两种解法——直接推理与真值表——两种都要能写。"
                "<code>P ⇒ Q</code> 与 <code>¬P ∨ Q</code> 等值这一条，是后面所有「证明是否 sound」判断的底座。"
            ),
            h3("3.2 证明：四个模板与一个判据"),
            p(
                "集合等式（set 2 Ex5、Ex6，set 3 Ex4）用<b>双向包含</b>模板，五个动作固定："
            ),
            st(
                "声明要证 X ⊆ Y 与 Y ⊆ X 两个方向；",
                "写「Let x ∈ X be arbitrary.」（任取，不许挑特例）；",
                "用定义把 x ∈ X 展开成若干个「且」或「或」；",
                "逐条推到 x ∈ Y；",
                "收尾写「Since x was arbitrary, X ⊆ Y.」，再对反方向重复一遍。",
            ),
            p(
                "如果两个集合都是同一批定义的改写（例如 <code>A × (B ∩ C)</code> 与 <code>(A × B) ∩ (A × C)</code>），"
                "set 3 Ex4 用的是更短的写法：一路「⇐⇒」下去，每一步旁边注明用的是哪个定义，"
                "最后得到「(a, b) 属于左边当且仅当属于右边」。这种写法在每个箭头都可逆时才成立，"
                "一旦中间出现平方、开方这类不可逆步骤就必须回到双向包含。"
            ),
            p(
                "<b>逆否</b>模板（set 5 Ex3(a)）：要证「ab 偶 ⇒ a 或 b 偶」，改证「a 与 b 都奇 ⇒ ab 奇」。"
                "写法是「Suppose a and b are odd, that is a = 2k + 1 and b = 2m + 1」，展开乘积写成 2(…) + 1。"
                "<b>反证</b>模板（set 5 Ex3(c)、set 6 Ex1）：假设结论的否定成立，推出矛盾，"
                "收尾写「A contradiction. Hence …」。set 6 Ex1 判 x² = 4y + 2 无解，"
                "关键一步是「x² 是偶数，所以 x 是偶数」，写成 x = 2k 后得到 2k² = 2y + 1，左边偶右边奇。"
            ),
            p(
                "<b>反例</b>模板（set 6 Ex2）：要证「对任意关系 R、S 都有 (RS)⁻¹ = R⁻¹S⁻¹」是假的，"
                "只需一组反例。原文取 R = {(0, 1)}、S = {(1, 2)}，算出 (RS)⁻¹ = {(2, 0)} 而 R⁻¹S⁻¹ = ∅。"
                "写反例题的标准句式是「It is enough to find some example …」，然后真的把两边都算出来，"
                "不能只说「显然不等」。"
            ),
            p(
                "判断一段证明是否 <b>sound</b>（set 5 Ex3）有一个机械的判据：把结论命题符号化成 "
                "<code>P ⇒ Q</code>，再看这段文字实际建立的是哪个蕴含式。"
                "(a) 假设 ¬Q 推出 ¬P，建的是 <code>¬Q ⇒ ¬P</code>，正是 P ⇒ Q 的逆否，等价，sound；"
                "(b) 假设 Q 推出 P，建的是 <code>Q ⇒ P</code>，这是逆命题（converse），与 P ⇒ Q 不等价，无效；"
                "(c) 假设 P ∧ ¬Q 推出矛盾 F，建的是 <code>(P ∧ ¬Q) ⇒ F</code>，等价于 P ⇒ Q，是反证，sound。"
                "这套判据也解释了 set 10 Ex2 的 Juha 之错：他从「a 被 6 整除」推到「a 被 3 整除」，"
                "证的是逆命题，原文的评语是「The deduction assumes the conclusion and proves the assumption.」"
            ),
            h3("3.3 计数：先把「顺序重不重要、能不能重复」问清"),
            p(
                "set 8 的每道题都卡在这两个问题上。四条公式的分工："
                "不放回且不计顺序用 C(n, k)；不放回且计顺序用 n!/(n−k)!；"
                "放回且不计顺序用 C(n+k−1, k)；放回且计顺序用 n^k。"
            ),
            p(
                "计算 C(n, k) 时不要真的去乘阶乘。原文示范的是「先约分再乘」："
                "C(70, 5) = (70·69·68·67·66)/(5·4·3·2·1)，把 70/5 得 14、69/3 得 23、68/4 得 17、66/2 得 33，"
                "于是 14·23·17·67·33 = 12 103 014。原文还有一句值得记住的话："
                "「in a division a·b/(c·d) we can do the division in any order」，所以挑好约的组合去约，"
                "不要老老实实按从左到右除。"
            ),
            p(
                "「带重复、不计顺序」的典型外壳是「买 10 块寿司、5 种可选」（set 8 Ex2）："
                "把 10 次选择看成 10 个球放进 5 个盒子，答案是 C(5+10−1, 10) = C(14, 10) = 1001。"
                "只要题干出现「只关心每种各取几个，不管顺序」，就用这一条。"
            ),
            p(
                "恒等式的证明（set 8 Ex3、Ex4 与 Pascal 规则）走代数路线：把 C(n, k) 展开成阶乘，"
                "通分后分子合并。set 8 Ex3 的收尾是「n(n−1)/2 + (n+1)n/2 = (n² − n + n² + n)/2 = n²」，"
                "两行就完。二项式展开（set 8 Ex6 的 (2 + x)⁸）则是把 C(8, k)·2^(8−k)·x^k 逐项写出，"
                "系数与次数都要写全，中间漏一项就是错。"
            ),
            p(
                "set 8 Ex5 用同一批数字问出三种答案，正好检验那两个问题有没有答完："
                "4 位 PIN 码允许重复、顺序重要，是 10⁴ = 10000；"
                "递增序列 x₁ ≤ x₂ ≤ x₃ ≤ x₄ 允许重复，但选好集合后顺序被大小关系定死，"
                "所以等价于「带重复、不计顺序」，是 C(13, 4) = 715；"
                "4 元子集不允许重复、顺序无关，是 C(10, 4) = 210。"
                "数字集合相同、取几个也相同，三个问法三个答案——公式必须靠那两个问题来选。"
            ),
            h3("3.4 归纳：三步与三处常见缺失"),
            p(
                "set 9 Ex2 把一段有毛病的归纳证明摊开让人找错，那段批注本身就是这三步的教科书："
            ),
            st(
                "Base case：把 n 的最小值代进去，左右两边各算一遍，明确写「so the base case is true」；",
                "Induction assumption：写「Assume that the claim is true when n = k」，这是<b>假设</b>，不是结论；",
                "Induction step：把 n = k+1 的左边拆成「前 k 项 + 第 k+1 项」，用假设替换前 k 项，"
                "再化到 n = k+1 的右边。",
            ),
            p(
                "原文点出的三处问题正好对应三个高频错误：缺 base case；把「The claim is true when n = k」写成结论"
                "（那是假设，必须写 Assume）；以及跳过代数步骤——从 1/3·k(k+1)(k+2) + (k+1)(k+2) 到 "
                "1/3·(k+1)((k+1)+1)((k+1)+2) 之间要写出「提取公因子 (k+1)(k+2)，括号里 1/3·k + 1 = (k+3)/3」。"
                "评分时这三处任何一处缺失都算不完整，因为归纳法的说服力就靠这三段闭合。"
            ),
            p(
                "set 9 还收了几个必须会证的经典式：1/(1·2) + 1/(2·3) + … + 1/((n−1)n) = (n−1)/n（n ≥ 2 起）；"
                "Nicomachus 定理（前 n 个奇数的和是 n² 的立方关系）；Fibonacci 数的归纳性质；"
                "以及带谓词的堆叠蕴含（set 9 Ex1 与 Ex6）。堆叠蕴含的写法是「逐层假设、逐层放宽」："
                "先假设 A × B ⊆ C × D，再任取 x ∈ A，取一个 y ∈ B 造出 (x, y)，才能用上第一个假设。"
                "注意「B 非空」这个条件是必要的，否则 (x, y) 根本造不出来——这也是原文特意声明 A、B、C、D 都非空的原因。"
            ),
            h3("3.5 整除与模：定义、Euclid、回代、判据"),
            p(
                "所有整除题的起点只有一句：<code>a | b</code> 当且仅当存在整数 k 使 <code>b = k·a</code>。"
                "set 10 Ex1 要求「by definition」证明 5 | 75、−3 | 51、55 | 0，答案就是三个等式："
                "75 = 15·5、51 = (−17)·(−3)、0 = 0·55。第三步最容易漏，因为 0 的写法不唯一，但 0 = 0·55 就是定义要的。"
            ),
            p(
                "「求所有 n 使 n | (3n + 2)」是这类题的模板：把条件写成 3n + 2 = k·n，移项得 2 = (k − 3)n，"
                "于是 n 必须是 2 的因数——2 的整数分解只有 1·2、2·1、(−1)(−2)、(−2)(−1) 四种，"
                "所以 n ∈ {2, 1, −2, −1}，再逐一代回验证。原文特意提醒「Remember negative solutions too!」。"
            ),
            p(
                "gcd 一律用 Euclid 算法，并且要写成带余除法的竖列，每一步都写全："
                "2023 = 1·1428 + 595；1428 = 2·595 + 238；595 = 2·238 + 119；238 = 2·119 + 0，"
                "所以 gcd = 119。最后余数为 0 时，上一行的余数就是答案，这是最容易写错位置的一步。"
            ),
            p(
                "要解 <code>ax + by = c</code>（set 10 Ex4、Ex5），先算 gcd(a, b)，再看它是否整除 c："
                "不整除就写「无整数解」，理由要写明「左边永远是 gcd 的倍数，右边不是」——"
                "set 10 Ex5(b) 的 21x − 35y = 24 就是这一类。整除则用<b>回代</b>："
                "从 Euclid 竖列的最下面一行往上，把每个余数写成上一行的组合，最后得到 "
                "<code>119 = 5·2023 − 7·1428</code>，于是 (x, y) = (5, 7)。"
                "原文还给出通解形式 x = 5 + 12k、y = 7 + 17k（1428/119 = 12、2023/119 = 17），"
                "但题目只要求「some integers x and y」时，给出一个解就够。"
            ),
            p(
                "同余部分（set 11、set 12）要背三条操作：两边可以同时加同一个数、乘同一个数；"
                "可以整体取幂；除以一个数与模不互素的因子时不行（那正是「乘法逆元是否存在」的问题）。"
                "set 12 Ex1 求 7^2026 的末位，就是取模 10 看周期：7¹ = 7、7² = 9、7³ = 3、7⁴ = 1，周期 4，"
                "2026 ÷ 4 余 2，末位是 9。set 11 Ex3「x ≡ 9 (mod 24) 时 7x + 4 的最小非负余数」，"
                "直接把 x = 9 代进去算 67 mod 24 = 19 即可，因为同余类里取哪个代表元结果都一样。"
            ),
            p(
                "素因子分解（set 11 Ex1）要「试到 √n 为止」：143 = 11·13、561 = 3·11·17、588 = 2²·3·7²。"
                "原文的 hint 写得很硬：「Make sure to try dividing the number n by <b>all</b> prime numbers "
                "in the range 2 ≤ p ≤ √n」，漏掉一个大于 √n 之前没试的素数，就可能把合数当素数。"
            ),
            h3("3.6 函数、关系与基数"),
            p(
                "合成关系的方向是最容易反的一处。原文的定义是「xRSz if and only if there is y ∈ Y such that "
                "xRy and ySz」，也就是 <code>RS</code> 表示<b>先 R 后 S</b>，与函数复合 f∘g 的「先 g 后 f」相反。"
                "set 4 Ex1 因此建议画箭头图：把 X→Y→Z 三段箭头并排，从 x 顺着箭头能走到的 z 就是合成里的对。"
                "逆关系 R⁻¹ 就是把所有箭头翻向，所以 RR⁻¹ 里会出现 (5, 6) 与 (6, 5) 这种「同一对的两个方向」——"
                "这正是原文算出 {(4,4), (5,5), (5,6), (6,5), (6,6)} 的原因。"
            ),
            p(
                "单射与满射的判定动作不同：单射要「假设 f(a) = f(b)，推出 a = b」，"
                "或者「假设 a ≠ b，推出 f(a) ≠ f(b)」；满射要「任取值域里的 c，解 f(x) = c，并说明解落在定义域里」。"
                "set 6 Ex5 的 f(x) = x/(2 − x) 就是从 f(x) = c 解出 x = 2c/(1 + c)，"
                "顺带看出 c = −1 时无解，于是它不是满射——这类题必须把「解不出来」的那个点指出来才算完整。"
            ),
            p(
                "置换的 two-line notation（set 7 Ex2）复合时，把 p 的第二行改写成「按 q 的像排列」再上下对齐，"
                "逐列读下来就是 p∘q：q 把 1 送到 3，p 把 3 送到 4，所以 p∘q 把 1 送到 4。"
                "求 q⁻¹ 就是把两行交换后按第一行排序。原文提醒这两个运算「well defined」是因为定义域与值域都是同一个 M 且都是双射。"
            ),
            p(
                "基数部分（set 7 Ex3–6）的三件工具：能构造双射就说明等势（[0,1] 与 (0,1) 的构造题）；"
                "Hilbert 旅馆说明可数集加上有限个甚至可数无穷个元素后仍可数（把老客人往后挪）；"
                "对角线法说明实数不可数（假设列表存在，逐位取反造出一个不在表里的序列）。"
                "这三件工具在正文第 6 讲讲过，练习册的价值在于要求你真的把双射写出来，而不是只说「显然」。"
            ),
            h2("四、解答册里值得背下来的句式"),
            p(
                "这些句子不是装饰，而是评分点：助教扫一眼就知道你有没有按定义做。原文原句照抄，后面是用途。"
            ),
            ul(
                "「Let x ∈ A be arbitrary.」＋「Since x was arbitrary, A ⊆ B.」——双向包含的两端，缺任一端逻辑链就断；",
                "「It is enough to find some example …」——反例题的开场，先声明策略再算；",
                "「Suppose, for contradiction, that …」——反证题的开场；",
                "「Taking (k + 1)(k + 2) as a common factor we see that …」——归纳题里跳过代数的那一步，写出来就不丢分；",
                "「The elements of a set are the objects separated by commas …, and the elements of an element are not elements of the original set.」——set 2 Ex1 的原话，一句话解释嵌套集合；",
                "「X ∈ Y means that some element of Y is equal to X. X ⊆ Y means that every element of X is an element of Y.」——set 2 Ex4 把两个符号并排定义，比任何解释都清楚；",
                "「We have a | b if and only if there is k ∈ Z such that b = k·a.」——所有整除题的第一行；",
                "「This is the contrapositive of … and hence equivalent to it.」——判断证明是否 sound 时的结论句。",
            ),
            h2("五、板书版（-WB）与重复副本"),
            p(
                "七份 <code>-WB</code> 文件（<code>02</code>、<code>03</code>、<code>04</code>、<code>05</code>、<code>07</code>、"
                "以及同名副本 <code>06</code>、<code>10</code>、<code>11</code>）在文本层里只有页码标记，正文长度 17–47 个字符，"
                "说明它们是把课上白板拍照后直接装订成的 PDF，没有文字层。所以："
                "一是它们<b>不提供新知识</b>，与对应 lesson 的内容重复，只是把课堂上现场推的式子留了影；"
                "二是<b>不能用文字检索</b>，要用只能看图像；"
                "三是它们在不同周目录里重复出现（<code>02</code> 与 <code>10</code> 的文本层一致、"
                "<code>03</code> 与 <code>06</code>、<code>11</code> 一致），同一张板书被复制到了多个周次下面。"
                "复习时直接把 <code>-WB</code> 跳过，看 lesson 正文即可。"
            ),
            h2("六、例行练习库与作业信息页"),
            p(
                "<code>routine-exercises-solutions.pdf</code> 是 62 页的自学题库，与上交作业无关（原文第一句："
                "「For your own self study and practice.」），2026-08-28 最后更新，开头有从 2022 年起的更新日志。"
                "它按 12 个主题分节，每节题目连续编号，正好可以按讲次对号入座："
            ),
            ul(
                "第 1 节 集合；第 2 节 序对、关系与图；第 3 节 命题逻辑；第 4 节 二进制与证明类型；"
                "第 5 节 函数；第 6 节 基数；第 7 节 组合；第 8 节 归纳；"
                "第 9 节 整除、mod 运算、Euclid 算法、gcd 与整数方程 ax + by = c；"
                "第 10 节 同余与 RSA 加密；第 11 节 矩阵运算；第 12 节 高斯消元与 Gauss–Jordan 法。"
            ),
            p(
                "用法建议：每讲复习完，只做对应那一节的单数题，错的那道再回正文找定义。"
                "它比练习册更适合考前突击，因为题量大、按主题归好、且带完整解答。"
            ),
            p(
                "<code>01_Info_1_Homework info.html</code> 是行政页，不含数学内容，但有三条与学习节奏有关的规则："
            ),
            ul(
                "作业每周一 8:00 提前一周发布，所以「第 2 周的作业」放在第 1 周的页签下；",
                "不许用 AI 写<b>最终解答</b>，但可以用 AI 练习或加深理解——原文引的是 Arene 的红灯模型；"
                "第一周的题在课上发，助教会当场带着做；",
                "习题课得分规则：参加 1 分、上台讲 1 分、每解出一题 1 分（上限 6 分），折算成考试加分；"
                "分数在 Grades 的 User report 里查，缺分要自己发邮件问本组助教；"
                "每组上限 20 人，固定参加自己那一组；线上答疑走 Zoom，链接发在每周页签里。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ keywords
    kws=kw(
        (
            "exercise set",
            "习题集",
            "Each set has six problems; sets 2-12 are on paper, set 1 is done in class.",
        ),
        (
            "exercise class",
            "习题课",
            "Present your solution on the whiteboard and get exercise points.",
        ),
        (
            "hint",
            "提示",
            'The last page of each solution booklet lists "Hints and things to pay attention to".',
        ),
        ("set equality", "集合相等", "To prove A = B, prove A ⊆ B and B ⊇ A."),
        (
            "double inclusion",
            "双向包含",
            "The standard template for set equalities, one direction at a time.",
        ),
        (
            "arbitrary element",
            "任意元素",
            "Let x ∈ A be arbitrary; never pick a specific x.",
        ),
        ("contrapositive", "逆否命题", "P ⇒ Q is equivalent to ¬Q ⇒ ¬P."),
        (
            "converse",
            "逆命题",
            "Q ⇒ P is not equivalent to P ⇒ Q; proving it proves nothing.",
        ),
        (
            "proof by contradiction",
            "反证法",
            "Assume P ∧ ¬Q and derive a contradiction F.",
        ),
        (
            "counterexample",
            "反例",
            'One example is enough to disprove a "for all" claim.',
        ),
        (
            "binomial coefficient",
            "二项式系数",
            "C(n, k) = n! / (k!(n − k)!); cancel before multiplying.",
        ),
        (
            "with repetition",
            "允许重复",
            "Choosing k from n types, order ignored: C(n + k − 1, k).",
        ),
        (
            "induction step",
            "归纳步",
            "Split off the (k + 1) term, substitute the assumption, simplify.",
        ),
        (
            "base case",
            "基础情形",
            "Check the smallest n; a missing base case makes the proof incomplete.",
        ),
        ("divisibility", "整除", "a | b iff there is k ∈ Z with b = k·a."),
        (
            "Euclidean algorithm",
            "欧几里得算法",
            "Repeated division; the last non-zero remainder is the gcd.",
        ),
    ),
    # ------------------------------------------------------------------ examples
    examples="\n".join(
        [
            qa(
                "例 1 · ∈ 与 ⊆ 同时判断（set 2 Ex4(e)）",
                p(
                    "设 X = {1, 2}，W = {2, 3}，Y = (X \\ W) ∪ {X ∪ W}。判断 X ⊆ Y 与 X ∈ Y 各自真假。"
                ),
                p("<b>解：</b>先算 Y，两步都要按定义。"),
                p(
                    "第一步，差集：X \\ W = {1, 2} \\ {2, 3}，把 W 的元素从 X 里去掉，得 {1}。"
                ),
                p(
                    "第二步，括号里的集合：{X ∪ W} 是一个<b>以集合为元素</b>的集合，X ∪ W = {1, 2, 3}，"
                    "所以 {X ∪ W} = {{1, 2, 3}}。注意这里不能漏掉外层花括号，它是「单元素集合」，"
                    "元素本身是 {1, 2, 3}。"
                ),
                p(
                    "于是 Y = {1} ∪ {{1, 2, 3}} = {1, {1, 2, 3}}，Y 有两个元素：数字 1 和一个集合。"
                ),
                p(
                    "判 ⊆：X 的元素是 1 与 2。1 ∈ Y，但 2 不在 Y 的两个元素里（Y 里没有数字 2，"
                    "只有一个集合 {1, 2, 3}，而 2 ≠ {1, 2, 3}），所以 X ⊄ Y。"
                ),
                p("判 ∈：Y 的元素是 1 与 {1, 2, 3}，没有一个是 {1, 2}，所以 X ∉ Y。"),
                p(
                    "<b>要点：</b>「2 ∈ {1, 2, 3}」为真，但「2 ∈ Y」为假，因为 Y 的元素不是 {1, 2, 3} 的成员，"
                    "而是 {1, 2, 3} 这个整体。集合嵌套题的失分九成出在这里。"
                ),
            ),
            qa(
                "例 2 · 用双向包含证明 De Morgan（set 2 Ex5）",
                p("设 A、B 是全集 U 的子集，证明 (A ∪ B)∁ = A∁ ∩ B∁。"),
                p("<b>解：</b>等式两边都是集合，按模板证两个方向。"),
                p(
                    "<b>方向一</b>（(A ∪ B)∁ ⊆ A∁ ∩ B∁）：任取 x ∈ (A ∪ B)∁。由补集定义，x ∈ U 且 x ∉ A ∪ B。"
                    "而 x ∉ A ∪ B 意味着「x 不在 A 里，且 x 不在 B 里」（若在任一个里就属于并集）。"
                    "于是 x ∈ A∁ 且 x ∈ B∁，即 x ∈ A∁ ∩ B∁。因为 x 是任取的，所以 (A ∪ B)∁ ⊆ A∁ ∩ B∁。"
                ),
                p(
                    "<b>方向二</b>（A∁ ∩ B∁ ⊆ (A ∪ B)∁）：任取 x ∈ A∁ ∩ B∁。则 x ∈ A∁ 且 x ∈ B∁，"
                    "即 x ∉ A 且 x ∉ B。既然两个都不在，x 就不可能在并集里，所以 x ∉ A ∪ B，"
                    "也就是 x ∈ (A ∪ B)∁。方向二成立。"
                ),
                p("两个方向都成立，故 (A ∪ B)∁ = A∁ ∩ B∁。∎"),
                p(
                    "<b>要点：</b>「x ∉ A ∪ B」要展开成「x ∉ A 且 x ∉ B」，这是并集定义的逆用，"
                    "原文的 hint 也专门点了这一步。若只在 Venn 图上涂色说明，原文的评语是"
                    "「This is acceptable as a proof in practice as long as there is clear explanation」，"
                    "但考试写文字证明更稳。"
                ),
            ),
            qa(
                "例 3 · 带重复不计顺序的计数（set 8 Ex2）",
                p(
                    "寿司店有 5 种寿司（Anago、Ebi、Kappa maki、Maguro、Sake），买 10 块。"
                    "只关心每种各买几块，不问顺序，有多少种选法？"
                ),
                p(
                    "<b>解：</b>先把题干翻成模型语言。选 10 次、每次从 5 种里选，同一种可以选多次，"
                    "「只关心每种几块」＝不计顺序，所以是「带重复、不计顺序」的情形，公式 C(n + k − 1, k)，"
                    "其中 n = 5（种类）、k = 10（块数）。"
                ),
                p("代入：C(5 + 10 − 1, 10) = C(14, 10) = 14!/(10!·4!)。"),
                p(
                    "约分：分子写 14·13·12·11（14! 与 10! 消掉后只剩这四个），分母 4·3·2·1 = 24。"
                    "12/4 = 3、3/3 = 1、14/2 = 7，于是 7·13·1·11 = 1001。"
                ),
                p("<b>答：</b>1001 种。"),
                p(
                    "<b>要点：</b>同一道题如果改成「按顺序摆在盘子里」，答案就变成 5¹⁰。"
                    "「顺序是否重要」这一问必须在套公式之前答完，答错方向整题归零。"
                ),
            ),
            qa(
                "例 4 · Euclid 算法与回代（set 10 Ex4）",
                p(
                    "求 gcd(2023, 1428)，并找整数 x、y 使 2023x − 1428y = gcd(2023, 1428)。"
                ),
                p("<b>解：</b>第一步，竖列做带余除法，直到余数为 0。"),
                pre(
                    "2023 = 1 * 1428 + 595\n1428 = 2 * 595 + 238\n595 = 2 * 238 + 119\n238 = 2 * 119 + 0"
                ),
                p("最后一个非零余数是 119，所以 gcd(2023, 1428) = 119。"),
                p("第二步，从最下面一行往上回代，把 119 写成 2023 与 1428 的组合。"),
                p(
                    "由 595 = 2·238 + 119 得 119 = 595 − 2·238；"
                    "把 238 = 1428 − 2·595 代进去：119 = 595 − 2(1428 − 2·595) = 5·595 − 2·1428；"
                    "再把 595 = 2023 − 1·1428 代进去：119 = 5(2023 − 1428) − 2·1428 = 5·2023 − 7·1428。"
                ),
                p(
                    "对照 2023x − 1428y = 119，得 (x, y) = (5, 7)。验证：5·2023 − 7·1428 = 10115 − 9996 = 119。"
                ),
                p(
                    "<b>要点：</b>回代必须<b>每层只替换一个数</b>，替换完立刻合并同类项，否则四个式子叠在一起就没法查错。"
                    "原文还给出通解 x = 5 + 12k、y = 7 + 17k（12 = 1428/119、17 = 2023/119），"
                    "题目只要一个解时不写通解也行，但要知道为什么步长是这两个数。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ practice
    practice="\n".join(
        [
            p(
                "<b>练习 1</b>（set 3 Ex2(c) 的变体）　设 P(C) 的元素个数不少于 5、不多于 10，求 |C|，并说明为什么只有这一个可能。"
            ),
            det(
                "参考答案与思路",
                p(
                    "|P(C)| = 2^|C|。逐试：|C| = 2 得 4（太少）、|C| = 3 得 8（落在 5–10）、"
                    "|C| = 4 得 16（太多）。指数函数严格递增，所以区间内只有 |C| = 3。"
                    "答案：C 是任意三元集合，例如 C = {1, 2, 3}，P(C) 有 8 个元素。"
                ),
            ),
            p("<b>练习 2</b>　证明 (A ∩ B)∁ = A∁ ∪ B∁，要求两个方向都写出来。"),
            det(
                "参考答案与思路",
                p(
                    "方向一：任取 x ∈ (A ∩ B)∁，则 x ∉ A ∩ B，即「不同时在 A 和 B 里」，"
                    "也就是「x ∉ A 或 x ∉ B」，故 x ∈ A∁ 或 x ∈ B∁，即 x ∈ A∁ ∪ B∁。"
                    "方向二：任取 x ∈ A∁ ∪ B∁，则 x ∉ A 或 x ∉ B，所以不可能同时在 A 与 B 中，"
                    "x ∉ A ∩ B，即 x ∈ (A ∩ B)∁。两方向成立，等式成立。"
                    "关键：∩ 的否定是「或」，∪ 的否定是「且」，这一步就是全部内容。"
                ),
            ),
            p("<b>练习 3</b>　求满足 n | (3n + 2) 的全部整数 n。"),
            det(
                "参考答案与思路",
                p(
                    "写成 3n + 2 = k·n（k ∈ Z），移项得 2 = (k − 3)n。"
                    "令 k′ = k − 3，则 2 = k′·n，即 n 是 2 的因数。"
                    "2 的整数分解为 1·2、2·1、(−1)(−2)、(−2)(−1)，故 n ∈ {1, 2, −1, −2}。"
                    "验证：2 | 8、1 | 5、−2 | −4、−1 | −1，全部成立。"
                    "易错：只写正因数 {1, 2}，漏掉负解。"
                ),
            ),
            p(
                "<b>练习 4</b>　用归纳法证明：对任意整数 n ≥ 2，1/(1·2) + 1/(2·3) + … + 1/((n−1)n) = (n−1)/n。"
            ),
            det(
                "参考答案与思路",
                p(
                    "Base case n = 2：左边 = 1/2，右边 = (2−1)/2 = 1/2，成立。"
                    "Induction：设 n = k 时成立。n = k+1 时左边 = (前 k 项) + 1/(k(k+1)) "
                    "= (k−1)/k + 1/(k(k+1))，通分到 k(k+1)：(k−1)(k+1)/(k(k+1)) + 1/(k(k+1)) "
                    "= (k² − 1 + 1)/(k(k+1)) = k²/(k(k+1)) = k/(k+1)，正是 (k+1−1)/(k+1)。"
                    "三步齐全：base、assume、化简到目标形状。"
                ),
            ),
            p(
                "<b>练习 5</b>　指出下面这段归纳证明缺了什么：「The claim is true when n = k. Then "
                "(sum to k+1) = (sum to k) + (k+1)(k+2) = … so the claim is true.」"
            ),
            det(
                "参考答案与思路",
                p(
                    "三处：①缺 base case（要从最小 n 验一遍）；"
                    "②「The claim is true when n = k」被写成了陈述，应是 Assume；"
                    "③从「加一项」到「等于 n = k+1 的右边」之间缺少代数过程（要写提取公因子、合并的过程）。"
                    "这正是 set 9 Ex2 原文点名的三个毛病。"
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
                    "① 集合等式的双向包含证明（De Morgan、分配律、笛卡尔积对 ∩/∪ 的分配）；"
                    "② 用定义做整除题，尤其是「求所有 n 使 n | (an + b)」这一型；"
                    "③ Euclid 算法求 gcd 加回代求 ax + by = c 的一个解；"
                    "④ 带重复不计顺序的计数（寿司题外壳）；"
                    "⑤ 归纳三段的完整写法，以及「找出这段归纳证明的毛病」的批改题。"
                ),
            ),
            cal(
                "warn",
                "易错",
                p(
                    "① 拿特例当证明（set 2 原文专门警告过：只能证你自己那几个集合）；"
                    "② 把逆命题当原命题（set 10 的 Juha 之错，set 5 Ex3(b) 同型）；"
                    "③ 漏 base case，或把归纳假设写成结论；"
                    "④ 混淆 ∈ 与 ⊆，尤其在嵌套集合与 {X ∪ W} 这种「集合当元素」的写法上；"
                    "⑤ 关系合成的顺序：RS 是先 R 后 S，写成先 S 后 R 就全错；"
                    "⑥ 算 C(n, k) 时硬乘阶乘，既慢又容易算错；"
                    "⑦ gcd 的最后一步取错余数（应取最后一个非零余数）。"
                ),
            ),
            cal(
                "tip",
                "进阶",
                p(
                    "① △（对称差）表的构造与「A △ B = ∅ ⇔ A = B」的观察（set 3 Ex6）；"
                    "② Iverson 括号写分段方程（set 6 Ex3(f)：[x ≤ 0](−2x − 1) + [x ≥ −1]x² = 2）；"
                    "③ 堆叠蕴含「逐层假设」的写法，以及「非空」条件为什么不能省（set 9 Ex1）；"
                    "④ 「p unless q」的符号化（set 5 Ex6 专门考了这个短语）；"
                    "⑤ 对角线法构造「不在列表里的序列」（set 7 Ex6）；"
                    "⑥ 用模 9 或模 11 的位数规则检查一长串乘法是否算错（set 11 Ex6）。"
                ),
            ),
        ]
    ),
    # ------------------------------------------------------------------ checklist
    checklist="\n".join(
        [
            p("做任何一道练习，按这个顺序走一遍；这也是 whiteboard 上该出现的顺序："),
            st(
                '读题干，先把出现的符号对应的定义写在纸上（∈、⊆、|、"even" 的代数形式等）；',
                "判类型：查上面的六类表，确定第一步是「列元素」「双向包含」「套计数公式」「写 base case」还是「做竖列除法」；",
                "写策略句：证明题先写「We prove both directions」或「It is enough to find one example」，让助教一眼看到路线；",
                "做代数：每一步只改一处，并在旁边注明用的是哪个定义（原文的 ⇐⇒ 链就是这么写的）；",
                "检查边界：是否漏了负解、是否漏了 n = 1、分母是否可能为 0、定义域是否被扩大；",
                "对答案：周五发布解答后逐题对照，错的题回到对应讲次找定义，不要只记结论；",
                "把这一题的 hint 抄到错题本上，下次遇到同型先看 hint。",
            ),
            cal(
                "",
                "自查一句话",
                "如果一道题你写不出「用的是哪个定义」，那这道题你还没做完，只是碰巧算对了。",
            ),
        ]
    ),
    # ------------------------------------------------------------------ mapping
    mapping="\n".join(
        [
            p(
                "下表把这 18 组文件（去重后）逐一对到页码与内容。同一份文件在周目录里的副本已合并成一行，"
                "并在备注里写明重复关系；批次总量为 34 个实体副本，去重后 18 组。"
            ),
            tb(
                ("文件", "页码 / 章节", "覆盖内容与备注"),
                (
                    "01-exercise-solutions.pdf",
                    "p1–p4 / Exercise set 1",
                    "数集与代数：相反数、绝对值、倒数、指数与根式、展开、二次方程、函数最小值；set 1 无题面文件",
                ),
                (
                    "02-exercise-solutions.pdf",
                    "p1–p7 / Exercise set 2",
                    "集合：列元素、∁/∩/\\、Venn 8 区、∈ 与 ⊆、De Morgan 与分配律的双向包含",
                ),
                (
                    "03-exercise-solutions.pdf",
                    "p1–p5 / Exercise set 3",
                    "集合族与 ∪/∩、幂集 2^n、笛卡尔积检验、R×R⁺ 上的关系、△ 关系表",
                ),
                (
                    "04-exercise-solutions.pdf",
                    "p1–p6 / Exercise set 4",
                    "关系合成 RS 与 RR⁻¹、箭头图、含根号方程、命题逻辑、骑士与无赖、P ⇒ Q ≡ ¬P ∨ Q",
                ),
                (
                    "05-exercise-solutions.pdf",
                    "p1–p6 / Exercise set 5",
                    "Lebombo 骨刻与象形数制、十六进制、二进制转换表、四段证明的 soundness 判定、整除传递、unless 的符号化",
                ),
                (
                    "06-exercise-solutions.pdf",
                    "p1–p6 / Exercise set 6",
                    "反证（x² = 4y + 2 无解）、反例（(RS)⁻¹ ≠ R⁻¹S⁻¹）、定义域限制下的指数/对数/绝对值/ Iverson 方程、关系的性质、单射判定",
                ),
                (
                    "07-exercise-solutions.pdf",
                    "p1–p6 / Exercise set 7",
                    "join 算子的单射/满射、置换 two-line notation 的复合与逆、等势、Hilbert 旅馆、[0,1]→(0,1) 双射、对角线法",
                ),
                (
                    "08-exercise-solutions.pdf",
                    "p1–p5 / Exercise set 8",
                    "C(70,5) 与 C(121,115) 的约分、带重复计数（寿司）、n² 恒等式、Pascal 规则、PIN 码 10⁴ 与递增序列 C(13,4) 与 4 元子集 C(10,4)、(2+x)⁸ 展开",
                ),
                (
                    "09-exercise-solutions.pdf",
                    "p1–p7 / Exercise set 9",
                    "堆叠蕴含与「非空」条件、归纳证明的三处毛病与修正、1/(k(k+1)) 求和、Nicomachus、Fibonacci、谓词归纳",
                ),
                (
                    "10-exercise-solutions.pdf",
                    "p1–p5 / Exercise set 10",
                    "整除定义与 n | (3n+2)、Juha 的逆命题之错、gcd(250,210) 与 A∩B、gcd(2023,1428) 回代、3x−5y=7 等的可解性判据",
                ),
                (
                    "02-exercise.pdf",
                    "p1–p2 / Exercise set 2",
                    "题面（6 题）。重复副本：03_Week 1_1_02-exercise.pdf，内容仅首行 SOURCE 不同",
                ),
                (
                    "02/03/04/05/07-lesson-WB.pdf",
                    "p1 起（各 1–7 页）",
                    "板书照片，无文字层（正文 17–47 字符，仅页码标记），与对应 lesson 内容重复，不含新知识",
                ),
                (
                    "06-lesson-WB.pdf、10-lesson-WB.pdf、11-lesson-WB.pdf",
                    "p1 等",
                    "重复副本：06 与 03、10 与 02、11 与 03 的文本层完全一致，是同一张板书被复制到不同周目录",
                ),
                (
                    "routine-exercises-solutions.pdf",
                    "p1–p62 / 12 个 section",
                    "自学题库：集合、关系与图、命题逻辑、二进制与证明、函数、基数、组合、归纳、整除与 gcd、同余与 RSA、矩阵、Gauss–Jordan；2026-08-28 版",
                ),
                (
                    "01_Homework info.html",
                    "整页（行政页）",
                    "作业发布节奏、AI 使用红线、习题课 1+1+每题 1 分（上限 6 分）、分组上限 20 人、Zoom 答疑、成绩查询路径",
                ),
                (
                    "—（本课源文件）",
                    "—",
                    "本课未出现任何「not in exam / 不考」字样：练习册与解答册都属于课程训练内容，只是没有进正文；唯一明确「不考」的说明出现在 30352 的 Extra reading，见那门课的补遗",
                ),
            ),
            cal(
                "tip",
                "怎么用这张表",
                "按讲次找人：第 1–3 讲看 set 1–3 的解答，第 4–7 讲看 set 4–7，第 8–10 讲看 set 8–10，"
                "第 9–11 讲看 set 10–11，第 11–12 讲看 set 11–12 的题面（无解答）。"
                "考前一晚只看两处：hints 与 routine-exercises 的对应节。",
            ),
        ]
    ),
)


with io.open(PATH, encoding="utf-8") as fh:
    data = json.load(fh)

before = len(data["lectures"])
old = [len(x["html"]) for x in data["lectures"]]
assert not any(x["slug"] == LEC["slug"] for x in data["lectures"]), "slug 重复"
data["lectures"].append(LEC)

with io.open(PATH, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

print(
    "[ok] %s lectures %d -> %d, new html %d chars"
    % (CID, before, len(data["lectures"]), len(LEC["html"]))
)
