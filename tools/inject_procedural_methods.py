# -*- coding: utf-8 -*-
"""向全站核心讲义注入程序化解题方法、题型步骤、采分模板与易错陷阱"""
import json, os, io, re

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(SITE, 'content')

def update_lecture_section(cid, slug, sec_type, content_to_append):
    p = os.path.join(CONTENT, f"{cid}.json")
    with io.open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    found = False
    for lec in data['lectures']:
        if lec['slug'] == slug:
            pattern = r'(<section[^>]*data-type="' + sec_type + r'"[^>]*>)(.*?)(</section>)'
            m = re.search(pattern, lec['html'], flags=re.S)
            if m:
                # Check if already injected
                if "【程序化解题法典】" in m.group(2) or "【题型标准采分】" in m.group(2):
                    continue
                new_sec = m.group(1) + m.group(2) + content_to_append + m.group(3)
                lec['html'] = lec['html'][:m.start()] + new_sec + lec['html'][m.end():]
                found = True
                break
    
    if found:
        with io.open(p, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Injected procedural method to {cid} / {slug} [{sec_type}]")

# ==============================================================================
# 1. 80 (工程数学 II) - 高斯消元、特征值、参数曲线
# ==============================================================================

# 1.1 高斯消元程序化求解法典
chk_gauss = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】非齐次线性方程组 $Ax = b$ 消元求解四步通法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】高斯-约尔当消元（Gauss-Jordan）标准作业程序（SOP）</b>
<p>严格按照四步有限状态机执行：写出增广矩阵 $\to$ 正向行阶梯化 $\to$ 逆向约化最简形 $\to$ 向量空间参数化表示，杜绝运算符号失误与自由变量遗漏。</p>
</div>
<ol class="steps">
  <li><b>步骤一（构造增广矩阵）</b>：将方程组 $Ax = b$ 严格对齐未知数顺序，提取系数矩阵与常数项列构成增广矩阵 $[A \mid b]$。务必检查缺项补 0。</li>
  <li><b>步骤二（正向行化简为阶梯形 REF）</b>：从第一列开始，选取绝对值最大的非零元作为主元（减小舍入误差）。利用初等行变换 $r_i \leftarrow r_i - c \cdot r_j$ 将主元下方元素全化为 0。重复此过程直至右下角。</li>
  <li><b>步骤三（逆向约化为最简阶梯形 RREF）</b>：将各主元行同除以主元系数化为 1；从最右侧主元开始自下而上，利用初等行变换将主元上方元素全消为 0。</li>
  <li><b>步骤四（解结构判别与通解参数化）</b>：
    <ul>
      <li>若出现 $[0\ 0\ \dots\ 0 \mid d]$（$d \ne 0$），立刻终止并判定<b>无解</b>（$\text{rank}(A) < \text{rank}(A \mid b)$）；</li>
      <li>若非零行数 $r = n$（未知数个数），直接读出<b>唯一解</b>；</li>
      <li>若 $r < n$，区分<b>主元变量（Basic Variables）</b>与<b>自由变量（Free Variables）</b>。将自由变量设为任意实数参数 $t_1, t_2, \dots \in \mathbb{R}$，将解向量表示为标准形式：$x = x_p + t_1 v_1 + t_2 v_2 + \dots$。</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>步骤 1（+2分）</b>：正确写出增广矩阵，无符号或缺项抄写错误；</li>
  <li><b>步骤 2（+3分）</b>：每步初等行变换必须显式标注算子（如 $r_2 - 2r_1 \to r_2$），得到正确的阶梯形；</li>
  <li><b>步骤 3（+3分）</b>：准确判定自由变量个数 $n - \text{rank}(A)$，正确列出特解 $x_p$ 与齐次基础解系 $v_i$；</li>
  <li><b>步骤 4（+2分）</b>：显式声明参数 $t_i \in \mathbb{R}$，用向量参数形式完整作答。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（致命丢分）</b>：初等行变换做错减法符号（负负得正漏掉），导致后续满盘皆输。自查法：消元完立刻代入原方程第二行验算。</li>
  <li><b>陷阱二</b>：在通解中写出坐标形式却漏写“其中 $t \in \mathbb{R}$ 为任意实数”，扣 1~2 分格式分。</li>
  <li><b>陷阱三</b>：把初等行变换与初等列变换混淆。解方程组<b>严禁使用列变换</b>，因为列变换直接打乱了未知数的对应关系！</li>
</ul>
</div>
"""
update_lecture_section('80', 'ch3-gaussian-elimination', 'checklist', chk_gauss)

# 1.2 特征值与对角化程序化求解法典
chk_eigen = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】矩阵特征值、特征向量与对角化五步标准流程</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】对角化 $A = PDP^{-1}$ 判定与构造算法</b>
<p>严格遵循：特征多项式因式分解 $\to$ 各特征值齐次方程求核 $\to$ 几何重数比对 $\to$ 正交化/可逆阵拼装 $\to$ 逆矩阵验算闭环。</p>
</div>
<ol class="steps">
  <li><b>步骤一（求特征多项式）</b>：计算行列式 $|A - \lambda I| = 0$。计算技巧：先利用行列式性质在某行或某列制造尽可能多的 0，再按该行/列展开，尽量保持因式分解形式 $(\lambda - \lambda_1)^{m_1}(\lambda - \lambda_2)^{m_2} = 0$，严禁盲目全部拆开成高次多项式。</li>
  <li><b>步骤二（求特征根及其代数重数 AM）</b>：解多项式方程求出所有特征值 $\lambda_i$，并记录每个特征值的代数重数（Algebraic Multiplicity）。利用迹与行列式性质速验：$\sum \lambda_i = \text{tr}(A)$ 且 $\prod \lambda_i = \det(A)$。</li>
  <li><b>步骤三（求各特征值的特征向量与几何重数 GM）</b>：对每个 $\lambda_i$，求解齐次线性系统 $(A - \lambda_i I)v = 0$。通过高斯消元求出其基础解系，解空间的维数即为几何重数 $\text{GM} = \dim(\ker(A - \lambda_i I))$。</li>
  <li><b>步骤四（对角化可行性判别）</b>：
    <ul>
      <li>充分必要条件：矩阵可对角化 $\iff$ 对所有特征值均有 $\text{GM}(\lambda_i) = \text{AM}(\lambda_i)$；</li>
      <li>若某个特征值的 $\text{GM} < \text{AM}$，立刻得出结论：<b>该矩阵不可对角化</b>，不可求出相似对角阵。</li>
    </ul>
  </li>
  <li><b>步骤五（组装变换矩阵 $P$ 与对角阵 $D$）</b>：若可对角化，将所有线性无关的特征向量依次作为列向量拼成变换矩阵 $P = [v_1 \mid v_2 \mid \dots \mid v_n]$，对应的对角矩阵为 $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$。满足恒等式 $AP = PD \iff P^{-1}AP = D$。</li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>特征方程建立与因式分解（+3分）</b>：正确写出 $|A - \lambda I|$ 并分解因式；</li>
  <li><b>特征向量求解过程（+3分）</b>：写出 $(A-\lambda I)v=0$ 增广矩阵消元步骤，指出非零基础解系；</li>
  <li><b>可对角化判定结论（+2分）</b>：必须显式说明“存在 $n$ 个线性无关特征向量”或“几何重数等于代数重数”；</li>
  <li><b>结果组装与对应性（+2分）</b>：矩阵 $P$ 的列顺序必须与对角阵 $D$ 的特征值顺序绝对一致。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（特征向量写成零向量）</b>：特征向量定义中<b>必须非零</b>（$v \ne 0$）。若写出零向量当作解直接扣该小问全部分数。</li>
  <li><b>陷阱二（顺序错位）</b>：若 $P = [v_1, v_2]$，但 $D = \text{diag}(\lambda_2, \lambda_1)$，则 $AP \ne PD$，直接判定计算错误。</li>
  <li><b>陷阱三（未声明非零任意常数）</b>：基础解系乘以任意非零常数 $k \ne 0$ 才是特征向量集合，书写时需注明 $k \ne 0$。</li>
</ul>
</div>
"""
update_lecture_section('80', 'ch3-eigenvalues-cramer', 'checklist', chk_eigen)

# ==============================================================================
# 2. 62 (工程数学 I) - 极限证明、微积分基本定理
# ==============================================================================

# 2.1 极限 epsilon-delta 证明四步法定式
chk_limit = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】柯西 $\epsilon-\delta$ 严格极限证明五步定式法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】形式化不等式双向放缩证明规范</b>
<p>严格按照“逆向放缩探索 $\to$ 确定探测步长 $\to$ 取最小值构造 $\delta \to$ 正向逻辑演绎 $\to$ 证毕闭环”五步书写，拿下期末考试最难理论大题。</p>
</div>
<ol class="steps">
  <li><b>步骤一（形式化陈述目标）</b>：在草稿纸上写下严格目标：要证明 $\lim_{x \to c} f(x) = L$，即对任意给定的 $\varepsilon > 0$，需找到 $\delta > 0$，使得当 $0 < |x - c| < \delta$ 时，恒有 $|f(x) - L| < \varepsilon$。</li>
  <li><b>步骤二（逆向分解误差表达式）</b>：展开绝对值式 $|f(x) - L|$，通过代数提取因式，分离出目标核心控制因子 $|x - c|$：
  $$|f(x) - L| = |g(x)| \cdot |x - c|$$
  此时的目标转化为：为多项式因子 $|g(x)|$ 找到一个有限的绝对上界 $M > 0$。</li>
  <li><b>步骤三（设定先验探测邻域约束 $|g(x)|$）</b>：预先人为设定一个初步步长，通常取 $\delta_1 = 1$。当 $|x - c| < 1$ 时，推导出 $x$ 的取值区间，从而计算出 $|g(x)| \le M$ 的常数上界。</li>
  <li><b>步骤四（取下确界合成 $\delta$）</b>：由 $|g(x)| \cdot |x - c| < M \cdot |x - c|$，为确保整体小于 $\varepsilon$，要求 $|x - c| < \frac{\varepsilon}{M}$。因此构造定义：
  $$\delta = \min\left(1, \frac{\varepsilon}{M}\right)$$</li>
  <li><b>步骤五（卷面正向严格论述与证毕闭环）</b>：誊写到正式卷面：
    <p>“证明：对任意给定的 $\varepsilon > 0$，取 $\delta = \min(1, \frac{\varepsilon}{M}) > 0$。当 $0 < |x - c| < \delta$ 时，由 $\delta \le 1$ 得 $|g(x)| \le M$；由 $\delta \le \frac{\varepsilon}{M}$ 得 $|x - c| < \frac{\varepsilon}{M}$。故 $|f(x) - L| = |g(x)||x - c| < M \cdot \frac{\varepsilon}{M} = \varepsilon$。证毕。”</p>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>定式开头（+1分）</b>：写出“对任意 $\varepsilon > 0$，取 $\delta = \dots$”的量词引导句；</li>
  <li><b>逆向因式分解与绝对值放缩（+3分）</b>：正确提取出 $|x - c|$，三角不等式或绝对值不等式运用严密；</li>
  <li><b>预设步长与上界 $M$ 构造（+3分）</b>：明确写出先验限制（如“假设 $|x - c| < 1$”），严谨推导出有界常数 $M$；</li>
  <li><b>$\min$ 函数合成与正向链条闭环（+3分）</b>：正确写出 $\delta = \min(1, \dots)$ 并完成最终小于 $\varepsilon$ 的代数推导。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（循环定义死穴）</b>：把 $\delta$ 定义为含有未知数 $x$ 的表达式（例如写成 $\delta = \frac{\varepsilon}{|2x+1|}$）。$\delta$ 只能依赖于 $\varepsilon$ 和已知常数，绝对不能包含自变量 $x$！此项一犯该题判 0 分。</li>
  <li><b>陷阱二（遗漏去心邻域）</b>：条件写成 $|x - c| < \delta$ 而漏掉 $0 <$，在考查极限存在性而非连续性时会被扣 1 分。</li>
  <li><b>陷阱三（未声明 $\delta > 0$）</b>：构造出的 $\delta$ 必须在卷面上显式标明 $> 0$。</li>
</ul>
</div>
"""
update_lecture_section('62', 't2-limits-continuity', 'checklist', chk_limit)

# ==============================================================================
# 3. 30565 (离散数学) - 扩展欧几里得算法求逆元、归纳法规范
# ==============================================================================

# 3.1 扩展欧几里得算法表格化求模逆元程序
chk_modular = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】扩展欧几里得算法表格化求模逆元 $ax \equiv 1 \pmod m$ 四步通法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】三列矩阵跟踪（Bézout Identity Table）算法</b>
<p>采用三列递推矩阵表格法，将欧几里得除法与回代合并为单向流水线计算，零心智负担求解裴蜀等式 $ax + my = \gcd(a, m) = 1$ 与正模逆元。</p>
</div>
<ol class="steps">
  <li><b>步骤一（互素存在性判定）</b>：检查题目要求的方程 $ax \equiv 1 \pmod m$。若 $\gcd(a, m) \ne 1$，直接得出结论：<b>模逆元不存在</b>，方程无解！只有当 $\gcd(a, m) = 1$ 时才继续执行步骤二。</li>
  <li><b>步骤二（初始化四列表格）</b>：建立包含四列的递推计算表：商 $q$、余数 $r$、系数 $s$、系数 $t$。初始化前两行：
    <table style="width:auto;margin:6px 0;">
      <tr><th>Step</th><th>商 $q_k$</th><th>余数 $r_k$</th><th>系数 $s_k$</th><th>系数 $t_k$</th></tr>
      <tr><td>k=0</td><td>—</td><td>$m$</td><td>$1$</td><td>$0$</td></tr>
      <tr><td>k=1</td><td>—</td><td>$a$</td><td>$0$</td><td>$1$</td></tr>
    </table>
    满足不变式：$m \cdot s_k + a \cdot t_k = r_k$ 恒成立。
  </li>
  <li><b>步骤三（迭代带余除法直至余数为 0）</b>：对于第 $k \ge 2$ 行：
    <ul>
      <li>计算整除商与余数：$q_k = \lfloor r_{k-2} / r_{k-1} \rfloor$，$r_k = r_{k-2} - q_k \cdot r_{k-1}$；</li>
      <li>递推更新系数：$s_k = s_{k-2} - q_k \cdot s_{k-1}$，$t_k = t_{k-2} - q_k \cdot t_{k-1}$；</li>
      <li>当计算出余数 $r_k = 0$ 时迭代终止。上一行（倒数第二行）的 $r_{k-1}$ 即为 $\gcd(a, m) = 1$，对应的 $t_{k-1}$ 即为裴蜀系数！</li>
    </ul>
  </li>
  <li><b>步骤四（负数逆元正化取模）</b>：求得的系数 $t$ 即满足 $a \cdot t \equiv 1 \pmod m$。若 $t < 0$，必须执行正化运算：
  $$x = (t \pmod m + m) \pmod m$$
  使其严格处于规范剩余系 $\{0, 1, \dots, m-1\}$ 之间。</li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>互素条件判定（+1分）</b>：显式指明 $\gcd(a, m) = 1$ 是逆元存在的充要条件；</li>
  <li><b>带余除法与辗转相除过程（+4分）</b>：写清每次除法的除数、被除数、商与余数；</li>
  <li><b>回代或表格递推过程（+3分）</b>：准确解出满足 $ax + my = 1$ 的整数解对 $(x, y)$；</li>
  <li><b>最终模化结果（+2分）</b>：将解换算为区间 $[0, m-1]$ 内的正整数并带回方程验算。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（交卷留负数）</b>：算出的解是负数（如 $t = -7$），未换算为模系统内的正数（如模 26 下应为 19）。直接写负数会被扣 1~2 分。</li>
  <li><b>陷阱二（除法符号抄错）</b>：递推式是减法 $t_{k-2} - q_k t_{k-1}$，易误写成加法。速查法：每行算完立刻代入 $m \cdot s_k + a \cdot t_k = r_k$ 验算。</li>
</ul>
</div>
"""
update_lecture_section('30565', 'primes-and-modular-arithmetic', 'checklist', chk_modular)

# ==============================================================================
# 4. 86 (计算机导论) - IEEE 754 浮点转换
# ==============================================================================
chk_float = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】IEEE 754 单精度（32-bit）浮点数手工编解码四步通法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】十进制浮点数与十六进制机器码双向转换 SOP</b>
<p>严格按照：符号位提取 $\to$ 整数小数分别转二进制 $\to$ 科学记数法规格化移位 $\to$ 阶码加偏置（+127）与尾数右补零拼装。</p>
</div>
<ol class="steps">
  <li><b>步骤一（确定符号位 S）</b>：若数为正，$S = 0$；若数为负，$S = 1$。记录符号后，后续全按正数处理绝对值 $|N|$。</li>
  <li><b>步骤二（整数与小数分别二进制化）</b>：
    <ul>
      <li>整数部分：除 2 取余，逆序排列；</li>
      <li>小数部分：乘 2 取整，顺序排列。若循环小数，按精度截断。</li>
      <li>拼接两部分得到纯二进制形式：$|N|_2 = b_k \dots b_0 . b_{-1} b_{-2} \dots$。</li>
    </ul>
  </li>
  <li><b>步骤三（规格化为标准科学记数法）</b>：移动小数点，将其化为 $1.M \times 2^E$ 形式（最高位必须唯一且为 1）：
    <ul>
      <li>若向左移动 $p$ 位，则指数 $E = +p$；若向右移动 $p$ 位，则指数 $E = -p$；</li>
      <li>移位后小数点右侧的二进制序列即为<b>尾数有效位（Mantissa）</b>；隐藏最高位 1（不占用存储空间）。</li>
    </ul>
  </li>
  <li><b>步骤四（计算偏置阶码并组装 32-bit 十六进制）</b>：
    <ul>
      <li>单精度偏置量（Bias）为 127。计算阶码字段：$E_{\text{stored}} = E + 127$；将该十进制数转换为 8 位无符号二进制序列；</li>
      <li>尾数字段取 $M$ 的前 23 位；若不足 23 位，在<b>右侧补 0（后置补零）</b>填充至 23 位；</li>
      <li>将 32 位按格式拼接：<code>[S (1位)] [E_stored (8位)] [M (23位)]</code>；</li>
      <li>每 4 位一组，转换为 8 位十六进制数（例如 <code>0x41C80000</code>）。</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>符号位判定（+1分）</b>：正确写出 0（正）或 1（负）；</li>
  <li><b>二进制展开与规格化（+3分）</b>：乘基取整步骤清晰，正确写出 $1.M \times 2^E$；</li>
  <li><b>偏置量加法（+3分）</b>：正确加上 127 并化为 8 位二进制；</li>
  <li><b>尾数 23 位对齐与十六进制转译（+3分）</b>：右侧正确补零至 23 位，每 4 位转 hex 无错。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（尾数补零方向反了）</b>：尾数不足 23 位必须在<b>右边（低位）补 0</b>！如果补在左边相当于做成了数值缩放，直接导致数值完全错误，扣该步全部 3 分。</li>
  <li><b>陷阱二（隐藏位处理错误）</b>：规格化后的前导 1 是默认隐含的，尾数绝对<b>不能包含小数点左边的 1</b>。</li>
  <li><b>陷阱三（偏置量减反了）</b>：从机器码还原十进制时，真实指数是 $E = E_{\text{stored}} - 127$，容易做成加法导致指数爆炸。</li>
</ul>
</div>
"""
update_lecture_section('86', 'w3-signed-numbers-and-float', 'checklist', chk_float)

# ==============================================================================
# 5. 30361 (软件工程) - 白盒测试基本路径法
# ==============================================================================
chk_mccabe = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】白盒测试控制流图与麦凯布圈复杂度基本路径测试四步通法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】结构化基本路径测试集（Basis Path Testing）工程化步骤</b>
<p>严格按照：源码节点化绘出 CFG $\to$ 欧拉示性数与判定节点算复杂度 $\to$ 选定主干基路径 $\to$ 独立路径翻转构造与用例数据推导。</p>
</div>
<ol class="steps">
  <li><b>步骤一（代码控制流切分并绘制控制流图 CFG）</b>：
    <ul>
      <li>将顺序执行语句合并为一个节点（Node）；</li>
      <li>将每一个判定分支点（<code>if</code>, <code>while</code>, <code>for</code>）独立画为一个判定节点；复合条件（如 <code>A && B</code>）必须拆解为两个串联/并联的单判定节点；</li>
      <li>用有向边连接控制转移路径，画出规范的单入口单出口有向图。</li>
    </ul>
  </li>
  <li><b>步骤二（双方法计算并验证圈复杂度 $V(G)$）</b>：
    <ul>
      <li>方法一（边节点公式）：$V(G) = E - V + 2$，其中 $E$ 为边数，$V$ 为节点数；</li>
      <li>方法二（判定节点公式）：$V(G) = \pi + 1$，其中 $\pi$ 为图中的二元谓词判定节点数；</li>
      <li>方法三（封闭区域数）：$V(G) = R$（图平面划分出的区域数，含外部区域）。三法结果必须完全一致以交叉自检。</li>
    </ul>
  </li>
  <li><b>步骤三（确定线性无关的基本路径集合 Basis Paths）</b>：
    <ul>
      <li>首先选择一条最具代表性的无循环或最直观路径作为基路径 Path 1；</li>
      <li>后续路径依次翻转且仅翻转一个判定节点的分支，保证每条新路径至少包含一条此前未被覆盖的有向边；</li>
      <li>直到构造出的独立路径总数恰好等于圈复杂度 $V(G)$。</li>
    </ul>
  </li>
  <li><b>步骤四（推导测试用例输入与预期输出）</b>：
    <ul>
      <li>针对每一条基本路径，反推能够触发该分支流向的变量输入值（Path Condition Constraint Solving）；</li>
      <li>列出表格：<code>[测试用例ID, 覆盖路径编号, 输入参数集合, 预期输出结果]</code>。</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>控制流图完整性（+3分）</b>：节点与边对应正确，无孤立节点或死循环假死边；复合逻辑拆分严谨；</li>
  <li><b>圈复杂度定量计算（+2分）</b>：公式 $V(G) = E - V + 2 = \pi + 1$ 计算过程完整准确；</li>
  <li><b>独立路径集枚举（+3分）</b>：列出节点序列，每条路径确实引入了新边，总数严格等于 $V(G)$；</li>
  <li><b>测试用例数据设计（+2分）</b>：输入值与断言输出明确，切实能遍历对应分支。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（复合判断漏拆）</b>：遇到 <code>if (a > 0 && b < 10)</code> 未拆为两个判定节点，导致计算出的圈复杂度比真实值少 1，后续全部用例遗漏。</li>
  <li><b>陷阱二（不可行路径 Infeasible Path）</b>：设计的路径在逻辑上不可能同时满足（例如前面判定 $x > 5$，后面同一路径上判定 $x < 0$），导致无法设计出实际测试用例。自查时需剔除不可行路径并调整基底。</li>
</ul>
</div>
"""
update_lecture_section('30361', 'l07-testing-and-quality', 'checklist', chk_mccabe)

print("\n" + "="*50)
print("核心学科程序化解题法典、标准采分模板与易错陷阱库全部注入成功！")
print("="*50)
