# -*- coding: utf-8 -*-
"""向全站核心讲义注入程序化解题方法、题型步骤、采分模板与易错陷阱（纯净 Unicode + 视觉卡片版）"""
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
# 1. 80 (工程数学 II) - 高斯消元、特征值
# ==============================================================================

# 1.1 高斯消元程序化求解法典
chk_gauss = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】非齐次线性方程组 Ax = b 消元求解四步通法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】高斯-约尔当消元（Gauss-Jordan）标准作业程序（SOP）</b>
<p>严格按照四步有限状态机执行：写出增广矩阵 → 正向行阶梯化 → 逆向约化最简形 → 向量空间参数化表示，杜绝运算符号失误与自由变量遗漏。</p>
</div>
<ol class="steps">
  <li><b>步骤一（构造增广矩阵）</b>：将方程组 <code>Ax = b</code> 严格对齐未知数顺序，提取系数矩阵与常数项列构成增广矩阵 <code>[A | b]</code>。务必检查缺项补 0。</li>
  <li><b>步骤二（正向行化简为阶梯形 REF）</b>：从第一列开始，选取绝对值最大的非零元作为主元（减小舍入误差）。利用初等行变换 <code>rᵢ ← rᵢ − c · rⱼ</code> 将主元下方元素全化为 0。重复此过程直至右下角。</li>
  <li><b>步骤三（逆向约化为最简阶梯形 RREF）</b>：将各主元行同除以主元系数化为 1；从最右侧主元开始自下而上，利用初等行变换将主元上方元素全消为 0。</li>
  <li><b>步骤四（解结构判别与通解参数化）</b>：
    <ul>
      <li>若出现 <code>[0 0 … 0 | d]</code>（<code>d ≠ 0</code>），立刻终止并判定<b>无解</b>（<code>rank(A) < rank([A | b])</code>）；</li>
      <li>若非零行数 <code>r = n</code>（未知数个数），直接读出<b>唯一解</b>；</li>
      <li>若 <code>r < n</code>，区分<b>主元变量（Basic Variables）</b>与<b>自由变量（Free Variables）</b>。将自由变量设为任意实数参数 <code>t₁, t₂, … ∈ ℝ</code>，将解向量表示为标准形式：<code>x = x_p + t₁ v₁ + t₂ v₂ + …</code>。</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>步骤 1（+2分）</b>：正确写出增广矩阵，无符号或缺项抄写错误；</li>
  <li><b>步骤 2（+3分）</b>：每步初等行变换必须显式标注算子（如 <code>r₂ − 2r₁ → r₂</code>），得到正确的阶梯形；</li>
  <li><b>步骤 3（+3分）</b>：准确判定自由变量个数 <code>n − rank(A)</code>，正确列出特解 <code>x_p</code> 与齐次基础解系 <code>vᵢ</code>；</li>
  <li><b>步骤 4（+2分）</b>：显式声明参数 <code>tᵢ ∈ ℝ</code>，用向量参数形式完整作答。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（致命丢分）</b>：初等行变换做错减法符号（负负得正漏掉），导致后续满盘皆输。自查法：消元完立刻代入原方程第二行验算。</li>
  <li><b>陷阱二</b>：在通解中写出坐标形式却漏写“其中 <code>t ∈ ℝ</code> 为任意实数”，扣 1~2 分格式分。</li>
  <li><b>陷阱三</b>：把初等行变换与初等列变换混淆。解方程组<b>严禁使用列变换</b>，因为列变换直接打乱了未知数的对应关系！</li>
</ul>
</div>
"""
update_lecture_section('80', 'ch3-gaussian-elimination', 'checklist', chk_gauss)

# 1.2 特征值与对角化程序化求解法典
chk_eigen = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】矩阵特征值、特征向量与对角化五步标准流程</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】对角化 A = P D P⁻¹ 判定与构造算法</b>
<p>严格遵循：特征多项式因式分解 → 各特征值齐次方程求核 → 几何重数比对 → 相似变换阵拼装 → 逆矩阵验算闭环。</p>
</div>
<ol class="steps">
  <li><b>步骤一（列出特征方程并解多项式）</b>：计算行列式 <code>det(A − λI) = 0</code>。展开为关于 <code>λ</code> 的一元 <code>n</code> 次多项式，因式分解求出所有实特征值 <code>λ₁, λ₂, …</code> 并标明代数重数（Algebraic Multiplicity）。</li>
  <li><b>步骤二（求每个特征值的基础解系/特征向量）</b>：对每一个求出的 <code>λᵢ</code>，代入齐次线性方程组 <code>(A − λᵢ I)v = 0</code>。对矩阵 <code>(A − λᵢ I)</code> 进行初等行化简求出核空间 <code>ker(A − λᵢ I)</code> 的一组基，即为属于该特征值的线性无关特征向量。</li>
  <li><b>步骤三（对角化可行性判别）</b>：统计所有特征向量总数。矩阵可对角化的充要条件是：<b>所有特征值的几何重数之和等于矩阵阶数 n</b>（即每个特征值的线性无关特征向量个数等于其代数重数）。若不足 <code>n</code> 个，立刻得出结论：<b>该矩阵不可对角化</b>。</li>
  <li><b>步骤四（构造可逆矩阵 P 与对角阵 D）</b>：若可对角化，将 <code>n</code> 个特征向量作为列向量拼成矩阵 <code>P = [v₁ v₂ … vₙ]</code>，对应的对角矩阵为 <code>D = diag(λ₁, λ₂, …, λₙ)</code>。注意：<code>P</code> 中列向量顺序必须与 <code>D</code> 中特征值对角元顺序严格一致！</li>
  <li><b>步骤五（可逆性验证与闭环检验）</b>：计算 <code>det(P) ≠ 0</code> 确认线性无关；抽查检验 <code>A · v₁ = λ₁ · v₁</code> 是否恒等。</li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>行列式计算（+3分）</b>：正确写出 <code>det(A − λI)</code> 并得出正确的特征多项式根；</li>
  <li><b>解齐次方程组（+3分）</b>：完整写出 <code>(A − λI)</code> 的行阶梯化过程，准确写出特征向量；</li>
  <li><b>对角化结论判定（+2分）</b>：明确陈述几何重数等于代数重数（或特征向量总数等于 <code>n</code>）；</li>
  <li><b>写出 P 与 D（+2分）</b>：列出 <code>P</code> 与 <code>D</code>，且列与特征值严格位置对应。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（对应次序错位）</b>：<code>P</code> 的第一列放了属于 <code>λ₂</code> 的特征向量，但 <code>D</code> 的 <code>(1,1)</code> 位置却写了 <code>λ₁</code>。这是零容忍错误，导致 <code>P⁻¹AP ≠ D</code>。</li>
  <li><b>陷阱二（重根时少求向量）</b>：若二重特征值对应的方程组只解出一个自由变量，误以为其可对角化。此时几何重数 1 < 代数重数 2，必须断定不可对角化！</li>
</ul>
</div>
"""
update_lecture_section('80', 'ch3-eigenvalues-cramer', 'checklist', chk_eigen)

# ==============================================================================
# 2. 62 (工程数学 I) - 柯西 ε-δ 极限证明
# ==============================================================================
chk_limit = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】柯西 ε-δ 严格极限证明五步定式法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】形式化不等式双向放缩证明规范</b>
<p>严格按照“逆向放缩探索 → 确定探测步长 → 取最小值构造 δ → 正向逻辑演绎 → 证毕闭环”五步书写，拿下期末考试最难理论大题。</p>
</div>
<ol class="steps">
  <li><b>步骤一（写出目标不等式）</b>：明确目标：对任意给定的 <code>ε > 0</code>，需寻找 <code>δ > 0</code>，使得当 <code>0 < |x − c| < δ</code> 时，满足 <code>|f(x) − L| < ε</code>。草稿纸写下待控绝对值表达式 <code>|f(x) − L|</code>。</li>
  <li><b>步骤二（因式分解提取因式 |x − c|）</b>：将待控项化为两部分之积：<code>|f(x) − L| = |g(x)| · |x − c|</code>，其中 <code>g(x)</code> 是剩余的扰动项。</li>
  <li><b>步骤三（先验限制邻域半径控制扰动项界限）</b>：强制限定 <code>|x − c| < δ₁</code>（通常取 <code>δ₁ = 1</code> 或 <code>δ₁ = |c|/2</code>）。在此闭区间内推导出 <code>|g(x)|</code> 的严格上界 <code>M</code>，使得：<code>|g(x)| < M</code>。</li>
  <li><b>步骤四（构造逆向映射综合半径 δ）</b>：为使 <code>|g(x)| · |x − c| < M · |x − c| < ε</code>，只需额外令 <code>|x − c| < ε / M</code>。取两者的最小值：<code>δ = min(δ₁, ε / M)</code>。</li>
  <li><b>步骤五（答题纸正式规范陈述正向推导）</b>：
    <ul>
      <li>“任给 <code>ε > 0</code>，取 <code>δ = min(δ₁, ε / M) > 0</code>。”</li>
      <li>“当 <code>0 < |x − c| < δ</code> 时，因为 <code>|x − c| < δ₁</code>，故 <code>|g(x)| < M</code>；同时因为 <code>|x − c| < ε / M</code>，所以：”</li>
      <li>“<code>|f(x) − L| = |g(x)| · |x − c| < M · (ε / M) = ε</code>。”</li>
      <li>“由柯西极限定义，证得 <code>lim_{x→c} f(x) = L</code>。”</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>因式分离与提取 |x − c|（+3分）</b>：正确因式分解，无代数变形错误；</li>
  <li><b>对剩余项给出合理常数界 M（+3分）</b>：显式声明 <code>δ₁ = 1</code> 并给出放缩推导；</li>
  <li><b>正确取 min 表达式构造 δ（+2分）</b>：必须写出 <code>δ = min(..., ...) > 0</code>；</li>
  <li><b>完整的正向演绎结论（+2分）</b>：逻辑闭环，有头有尾。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（δ 表达式中包含 x）</b>：写出 <code>δ = ε / |2x + 1|</code>。绝对大忌！<code>δ</code> 只能依赖于预给常数 <code>ε</code> 和常数点 <code>c</code>，绝对不能包含自变量 <code>x</code>！一旦出现 <code>x</code> 该题判定为 0 分。</li>
  <li><b>陷阱二（漏写 min）</b>：直接写 <code>δ = ε / 9</code>，却未在证明中先交代 <code>|x − c| < 1</code>，导致放缩不等式缺乏前提。</li>
</ul>
</div>
"""
update_lecture_section('62', 't2-limits-continuity', 'checklist', chk_limit)

# ==============================================================================
# 3. 30565 (离散数学) - 扩展欧几里得求模逆元
# ==============================================================================
chk_modular = r"""
<h3><span class="badge purple">拓展深化</span> 【程序化解题法典】扩展欧几里得算法表格化求模逆元 ax ≡ 1 (mod m) 四步通法</h3>
<div class="callout idea" data-ext="true">
<b>【程序化算法】三列矩阵跟踪（Bézout Identity Table）算法</b>
<p>采用三列递推矩阵表格法，将欧几里得除法与回代合并为单向流水线计算，零心智负担求解裴蜀等式 <code>ax + my = gcd(a, m) = 1</code> 与正模逆元。</p>
</div>
<ol class="steps">
  <li><b>步骤一（前置可逆性充要判定）</b>：检查 <code>gcd(a, m) = 1</code>（互质）。若不互质，立刻判定<b>逆元不存在</b>，无需盲目计算。</li>
  <li><b>步骤二（初始化三列扩展表格）</b>：建立表格列：<code>[商 q, 余数 r, 系数 s, 系数 t]</code>，其中满足不变式 <code>r = s · a + t · m</code>：
    <ul>
      <li>Row 0: <code>r₀ = m, s₀ = 0, t₀ = 1</code></li>
      <li>Row 1: <code>r₁ = a, s₁ = 1, t₁ = 0</code></li>
    </ul>
  </li>
  <li><b>步骤三（单向递推除法直到余数为 1）</b>：
    <ul>
      <li>计算整数商 <code>q = ⌊r_{k-1} / rₖ⌋</code>，新余数 <code>r_{k+1} = r_{k-1} − q · rₖ</code>；</li>
      <li>同步更新系数：<code>s_{k+1} = s_{k-1} − q · sₖ</code>，<code>t_{k+1} = t_{k-1} − q · tₖ</code>；</li>
      <li>重复上述步骤，直到余数 <code>r_{k+1} = 1</code>。最后一行的 <code>s</code> 即为对应未知数系数。</li>
    </ul>
  </li>
  <li><b>步骤四（模归一化输出正余数逆元）</b>：
    <ul>
      <li>解出的 <code>s</code> 可能为负数。若 <code>s < 0</code>，必须通过模加运算转换到标准剩余系区间 <code>[0, m − 1]</code>：<code>x = (s mod m + m) mod m</code>；</li>
      <li>验算：将 <code>(a · x) mod m</code> 算一遍，必须严格等于 1。</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>欧几里得除法流程（+3分）</b>：各步商与余数计算准确；</li>
  <li><b>乘法逆元或裴蜀系数回代（+4分）</b>：正确写出等式 <code>a · s + m · t = 1</code>；</li>
  <li><b>负数逆元规范转正（+2分）</b>：若 <code>s</code> 为负，正确转换至 <code>[0, m − 1]</code> 区间；</li>
  <li><b>同余验算闭环（+1分）</b>：写出 <code>(a · x) mod m = 1</code> 验算行。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（直接写负数答案）</b>：在离散数学中，模逆元默认要求在 <code>ℤ_m</code> 中，若算出 <code>s = −15</code> 直接当作最终答案，会被扣 1~2 分。必须写 <code>−15 + 26 = 11 (mod 26)</code>。</li>
  <li><b>陷阱二（除法符号取整错误）</b>：在递推系数 <code>s_{k-1} − q · sₖ</code> 时减法带负号算错符号，导致全表报废。每走两行应立刻使用 <code>r = s · a + t · m</code> 验算行不变式。</li>
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
<p>严格按照：符号位提取 → 整数小数分别转二进制 → 科学记数法规格化移位 → 阶码加偏置（+127）与尾数右补零拼装。</p>
</div>
<ol class="steps">
  <li><b>步骤一（符号位确定）</b>：正数 <code>S = 0</code>，负数 <code>S = 1</code>。后续仅处理绝对值。</li>
  <li><b>步骤二（数值绝对值转换为二进制原码）</b>：
    <ul>
      <li>整数部分：除 2 取余，逆序排列；</li>
      <li>小数部分：乘 2 取整，顺序排列；</li>
      <li>拼接为完整的纯二进制形式：如 <code>1101.011₂</code>。</li>
    </ul>
  </li>
  <li><b>步骤三（规格化移位并提取尾数与真实指数）</b>：
    <ul>
      <li>将小数点移动到最高有效位（第一个 1）的右侧，写成 <code>1.M × 2ᴱ</code> 形式；</li>
      <li>向左移 <code>E</code> 位则指数为正 <code>+E</code>，向右移 <code>E</code> 位则指数为负 <code>−E</code>；</li>
      <li>丢弃前导 <code>1.</code>，将小数点右边的有效串作为尾数字段 <code>M</code>。</li>
    </ul>
  </li>
  <li><b>步骤四（计算偏置阶码并拼装 32 位机器字）</b>：
    <ul>
      <li><b>阶码（8位）</b>：<code>E_{stored} = E + 127</code>。将十进制 <code>E_{stored}</code> 转为 8 位无符号二进制码；</li>
      <li><b>尾数（23位）</b>：取步骤三的 <code>M</code>，在<b>右侧（末尾）补 0</b> 直至填满 23 位；</li>
      <li><b>最终拼装</b>：<code>[S(1位)] [E_{stored}(8位)] [M(23位)]</code>，共 32 位。通常每 4 位一组转为 8 位十六进制表示。</li>
    </ul>
  </li>
</ol>
<div class="callout exam">
<b>【期末评分标准与采分点】</b>
<ul>
  <li><b>符号位与基础转换（+2分）</b>：二进制绝对值转换无误；</li>
  <li><b>规格化与指数提取（+2分）</b>：前导 1 识别无误，指数 <code>E</code> 符号正确；</li>
  <li><b>阶码偏置计算（+3分）</b>：<code>E + 127</code> 计算正确并转为 8 位二进制；</li>
  <li><b>尾数 23 位对齐与十六进制转译（+3分）</b>：右侧正确补零至 23 位，每 4 位转 hex 无错。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（尾数补零方向反了）</b>：尾数不足 23 位必须在<b>右边（低位）补 0</b>！如果补在左边相当于做成了数值缩放，直接导致数值完全错误，扣该步全部 3 分。</li>
  <li><b>陷阱二（隐藏位处理错误）</b>：规格化后的前导 1 是默认隐含的，尾数绝对<b>不能包含小数点左边的 1</b>。</li>
  <li><b>陷阱三（偏置量减反了）</b>：从机器码还原十进制时，真实指数是 <code>E = E_{stored} − 127</code>，容易做成加法导致指数爆炸。</li>
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
<p>严格按照：源码节点化绘出 CFG → 欧拉示性数与判定节点算复杂度 → 选定主干基路径 → 独立路径翻转构造与用例数据推导。</p>
</div>
<ol class="steps">
  <li><b>步骤一（代码控制流切分并绘制控制流图 CFG）</b>：
    <ul>
      <li>将顺序执行语句合并为一个节点（Node）；</li>
      <li>将每一个判定分支点（<code>if</code>, <code>while</code>, <code>for</code>）独立画为一个判定节点；复合条件（如 <code>A && B</code>）必须拆解为两个串联/并联的单判定节点；</li>
      <li>用有向边连接控制转移路径，画出规范的单入口单出口有向图。</li>
    </ul>
  </li>
  <li><b>步骤二（双方法计算并验证圈复杂度 V(G)）</b>：
    <ul>
      <li>方法一（边节点公式）：<code>V(G) = E − V + 2</code>，其中 <code>E</code> 为边数，<code>V</code> 为节点数；</li>
      <li>方法二（判定节点公式）：<code>V(G) = π + 1</code>，其中 <code>π</code> 为图中的二元谓词判定节点数；</li>
      <li>方法三（封闭区域数）：<code>V(G) = R</code>（图平面划分出的区域数，含外部区域）。三法结果必须完全一致以交叉自检。</li>
    </ul>
  </li>
  <li><b>步骤三（确定线性无关的基本路径集合 Basis Paths）</b>：
    <ul>
      <li>首先选择一条最具代表性的无循环或最直观路径作为基路径 Path 1；</li>
      <li>后续路径依次翻转且仅翻转一个判定节点的分支，保证每条新路径至少包含一条此前未被覆盖的有向边；</li>
      <li>直到构造出的独立路径总数恰好等于圈复杂度 <code>V(G)</code>。</li>
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
  <li><b>圈复杂度定量计算（+2分）</b>：公式 <code>V(G) = E − V + 2 = π + 1</code> 计算过程完整准确；</li>
  <li><b>独立路径集枚举（+3分）</b>：列出节点序列，每条路径确实引入了新边，总数严格等于 <code>V(G)</code>；</li>
  <li><b>测试用例数据设计（+2分）</b>：输入值与断言输出明确，切实能遍历对应分支。</li>
</ul>
</div>
<div class="callout warn">
<b>【高频扣分陷阱与易错清单】</b>
<ul>
  <li><b>陷阱一（复合判断漏拆）</b>：遇到 <code>if (a > 0 && b < 10)</code> 未拆为两个判定节点，导致计算出的圈复杂度比真实值少 1，后续全部用例遗漏。</li>
  <li><b>陷阱二（不可行路径 Infeasible Path）</b>：设计的路径在逻辑上不可能同时满足（例如前面判定 <code>x > 5</code>，后面同一路径上判定 <code>x < 0</code>），导致无法设计出实际测试用例。自查时需剔除不可行路径并调整基底。</li>
</ul>
</div>
"""
update_lecture_section('30361', 'l07-testing-and-quality', 'checklist', chk_mccabe)

print("\n" + "="*50)
print("核心学科程序化解题法典、标准采分模板与易错陷阱库全部注入成功！")
print("="*50)
