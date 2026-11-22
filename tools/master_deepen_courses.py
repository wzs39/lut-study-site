# -*- coding: utf-8 -*-
"""全站核心学科讲义全章节深度增强与文不对题修复主程序"""
import json, re, os, io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(SITE, 'content')

def inject_to_section(lec_html, sec_type, extra_html, marker):
    pattern = r'(<section[^>]*data-type="' + sec_type + r'"[^>]*>)(.*?)(</section>)'
    m = re.search(pattern, lec_html, flags=re.S)
    if not m:
        return lec_html
    if marker in m.group(2):
        return lec_html
    new_sec = m.group(1) + m.group(2) + extra_html + m.group(3)
    return lec_html[:m.start()] + new_sec + lec_html[m.end():]

# ==============================================================================
# 1. 修复 32632 语序倒置与 None 章节属性
# ==============================================================================
p32632 = os.path.join(CONTENT, '32632.json')
with io.open(p32632, 'r', encoding='utf-8') as f:
    d32632 = json.load(f)

lecs_by_slug = {l['slug']: l for l in d32632['lectures']}
order_32632 = [
    'l1-launch-self-intro', 'l2-reading-chunking', 'l3-vocabulary-grammar-clinic',
    'l4-elevator-pitch', 'l5-presentation-data', 'l6-meetings-negotiation',
    'l7-word-order-questions', 'l8-assignments-listening', 'l9-pronunciation-clinic',
    'supp-homework-map'
]
new_lecs_32632 = []
for s in order_32632:
    if s in lecs_by_slug:
        l = lecs_by_slug[s]
        if s == 'l6-meetings-negotiation':
            l['title_zh'] = '第 6 讲 · 会议沟通、协商与专业简报'
            l['part'] = '第 3 章 会议沟通与协商'
        elif s == 'l7-word-order-questions':
            l['title_zh'] = '第 7 讲 · Unit 1 语法专题：语序、问句与附加疑问句'
            l['part'] = '第 3 章 语法与句型'
        elif s == 'l8-assignments-listening':
            l['title_zh'] = '第 8 讲 · 四项作业、口语测试与课堂听说材料'
            l['part'] = '第 4 章 作业与听说实战'
        elif s == 'l9-pronunciation-clinic':
            l['title_zh'] = '第 9 讲 · 语音诊所：重音、语调、最小对立与录音交付'
            l['part'] = '第 5 章 语音与口语测试'
        elif s == 'supp-homework-map':
            l['title_zh'] = '补遗 · 十三次课的作业地图、交付通道与考核节点'
            l['part'] = '第 5 章 语音与口语测试'
        new_lecs_32632.append(l)

d32632['lectures'] = new_lecs_32632
with io.open(p32632, 'w', encoding='utf-8') as f:
    json.dump(d32632, f, ensure_ascii=False, indent=2)
print('[OK] 32632 顺序与空属性修复完成')

# ==============================================================================
# 2. 修复 33295 课次跳号
# ==============================================================================
p33295 = os.path.join(CONTENT, '33295.json')
with io.open(p33295, 'r', encoding='utf-8') as f:
    d33295 = json.load(f)

for l in d33295['lectures']:
    if l['slug'] == 't10-genetiivi':
        l['title_zh'] = 'Tunti 10 · 属格与所有格'
        l['part'] = '第 4 章 属格、个人信息与复习'
    elif l['slug'] == 't11-henkilotiedot':
        l['title_zh'] = 'Tunti 11 · 个人信息与咖啡厅场景'
        l['part'] = '第 4 章 属格、个人信息与复习'
    elif l['slug'] == 't12-kertaus':
        l['title_zh'] = 'Tunti 12 (Kertaus) · 复习、考试与文化'
        l['part'] = '第 4 章 属格、个人信息与复习'

with io.open(p33295, 'w', encoding='utf-8') as f:
    json.dump(d33295, f, ensure_ascii=False, indent=2)
print('[OK] 33295 课次跳号规范完成')

# ==============================================================================
# 3. 修复与深化 30352 (Python)
# ==============================================================================
p30352 = os.path.join(CONTENT, '30352.json')
with io.open(p30352, 'r', encoding='utf-8') as f:
    d30352 = json.load(f)

for l in d30352['lectures']:
    if l['slug'] == 'ch11-errors':
        l['title_zh'] = '第 9 讲 · 错误、异常与调试体系'
    elif l['slug'] == 'ch12-dicts-sets-json':
        l['title_zh'] = '第 10 讲 · 字典、集合、JSON 与自有模块'
    elif l['slug'] == 'ch11-tuples-sets-packages-numpy':
        l['title_zh'] = '第 11 讲 · 元组、包管理与 NumPy 数组科学计算'

# 注入 Python 底层原理
fn_extra = """
<h3>6.0 函数调用的底层机理：调用栈（Call Stack）与 LEGB 作用域解析</h3>
<p>在高级语言中，函数不仅是代码复用单元，更是独立的<b>运行时执行上下文（Execution Context）</b>。</p>
<p><b>1. 调用栈与栈帧（Stack Frame）生命周期</b>：每当发生一次函数调用时，CPython 解释器都会在进程的调用栈上压入一个全新的栈帧对象 <code>PyFrameObject</code>。该栈帧独立持有：局部变量表（Fast Locals）、求值栈（Evaluation Stack）和指令指针（f_lasti）。当函数返回时，该栈帧被弹出并销毁，局部变量绑定的对象引用计数减 1。递归过深导致的 <code>RecursionError</code>，本质上是调用栈帧数量触碰了 Python 的安全防御阈值（默认 1000）。</p>
<p><b>2. 作用域查找的 LEGB 严格顺序</b>：当在函数中引用一个变量名时，解释器严格按照四层命名空间逐层向上探测：<b><code>L (Local 局部) ⟹ E (Enclosing 闭包外层) ⟹ G (Global 全局模块) ⟹ B (Built-in 内建函数)</code></b>。注意：在函数内部对变量进行赋值默认会将该变量直接标记为 Local。若要在内部修改全局变量或外层闭包变量，必须显式使用 <code>global</code> 或 <code>nonlocal</code> 声明，否则解释器会在编译阶段将其优化为局部变量，导致 <code>UnboundLocalError</code>。</p>
"""
oop_extra = """
<h3>7.0 面向对象的高级机制：魔法方法（Dunder Methods）与 Python 数据模型</h3>
<p>在 Python 中，面向对象绝非简单的 class 封装，而是通过一套统一的<b>数据模型协议（Data Model Protocols）</b>驱动：</p>
<ol>
<li><b>字符串表达的双重契约</b>：<code>__repr__(self)</code> 面向开发者与调试器，输出应当具有明确性，理想情况下应满足 <code>eval(repr(obj)) == obj</code>；而 <code>__str__(self)</code> 面向终端用户，输出易读的人性化文本。</li>
<li><b>可哈希性与对象恒等性</b>：如果自定义类重写了 <code>__eq__</code>，解释器会自动将其 <code>__hash__</code> 置为 None，使之不能作为字典的键或加入集合中！若需要对象作为 Hash Key，必须同时重写 <code>__eq__</code> 与 <code>__hash__</code>，且保证在对象的生命周期内哈希值恒定不变（不可变对象）。</li>
<li><b>属性访问拦截与描述符（Descriptors）</b>：<code>@property</code> 装饰器本质上是实现了 <code>__get__</code> 和 <code>__set__</code> 协议的描述符对象，它让属性的“取值”与“校验”在保持字段访问语法简洁性的同时具备了严格的防御性封装。</li>
</ol>
"""
numpy_extra = """
<h3>11.5 NumPy 连续内存步进（Strides）与广播机制（Broadcasting）的数学几何原理</h3>
<p>为什么原生 Python 列表处理 100 万个浮点数耗时数百毫秒，而 NumPy 只需不到 1 毫秒？核心在于其底层的 <b>C 连续内存模型与步进计算</b>。</p>
<p><b>1. 连续存储与缓存预取</b>：NumPy 的 <code>ndarray</code> 将数据以二进制同质格式连续平铺在堆内存中。当 CPU 加载一个数组元素时，硬件高速缓存行（L1/L2 Cache Line，通常 64 字节）会瞬时预取后续 8 个双精度浮点数，消除了指针解引用的内存墙延迟。</p>
<p><b>2. 步进（Strides）与零拷贝视图（Zero-Copy Views）</b>：NumPy 定位多维数组元素的公式为：<code>Byte_Offset(i, j) = i · strides[0] + j · strides[1]</code>。当执行矩阵转置 <code>A.T</code> 或切片 <code>A[::2, ::2]</code> 时，<b>NumPy 根本不复制任何底层数据</b>！它仅仅生成一个新的轻量元数据头，将步进元组调换或翻倍。这种零内存开销是科学计算与深度学习处理海量张量数据时维持高吞吐的关键。</p>
<p><b>3. 广播机制（Broadcasting Rules）的形式化判定准则</b>：当对两个不同形状的数组做运算时，从末尾维度向前逐维比对：对每一个维度，两数组在该维度的大小完全相等，或者其中一个数组在该维度的大小恰好为 1（该维度将沿着步进为 0 虚拟复制拉伸，不消耗额外内存）。</p>
"""

for l in d30352['lectures']:
    if l['slug'] == 'ch06-functions':
        l['html'] = inject_to_section(l['html'], 'detail', fn_extra, '6.0 函数调用的底层机理')
    elif l['slug'] == 'ch07-classes':
        l['html'] = inject_to_section(l['html'], 'detail', oop_extra, '7.0 面向对象的高级机制')
    elif l['slug'] == 'ch11-tuples-sets-packages-numpy':
        l['html'] = inject_to_section(l['html'], 'detail', numpy_extra, '11.5 NumPy 连续内存')

with io.open(p30352, 'w', encoding='utf-8') as f:
    json.dump(d30352, f, ensure_ascii=False, indent=2)
print('[OK] 30352 编程基础核心原理注入完成')

# ==============================================================================
# 4. 深度升级 80 (工程数学 II)
# ==============================================================================
p80 = os.path.join(CONTENT, '80.json')
with io.open(p80, 'r', encoding='utf-8') as f:
    d80 = json.load(f)

p1_extra_80 = """
<h3>1.9 参数曲线的斜率、光滑性与二阶导数深度推导</h3>
<p>在工程与物理学中，质点的轨迹由参数方程给出。一阶导数给出了轨迹切线的斜率，而<b>二阶导数则决定了曲线的凹凸性（Concavity）与轨迹的曲率</b>。</p>
<p><b>一阶导数公式的微分形式推导</b>：设 <code>x = f(t), y = g(t)</code>。由一阶微分形式不变性：<code>dx = f'(t)dt</code>，<code>dy = g'(t)dt</code>。在 <code>f'(t) ≠ 0</code> 时，两者相除即得：<b><code>dy/dx = (g'(t)dt) / (f'(t)dt) = g'(t) / f'(t) = (dy/dt) / (dx/dt)</code></b>。</p>
<p><b>二阶导数的严格推导（链式法则核心）</b>：二阶导数定义为「对 x 求一阶导数的导数」：<code>d²y/dx² = d/dx [ dy/dx ]</code>。由于 <code>dy/dx</code> 是参数 t 的函数，记作 <code>y'(t)</code>，它对自变量 x 无法直接求导，必须再次借用链式法则对参数 t 求导，然后除以 <code>dx/dt</code>：</p>
<p><b><code>d²y/dx² = (d/dt [ dy/dx ]) / (dx/dt) = (d/dt [ g'(t)/f'(t) ]) / f'(t)</code></b></p>
<div class="callout exam"><b>高频致命错误警示</b>绝对不能写成 <code>d²y/dt² / d²x/dt² = g''(t) / f''(t)</code>！展开商法则可知：<code>d²y/dx² = [ g''(t)f'(t) - g'(t)f''(t) ] / [ f'(t) ]³</code>。分母是 <code>[f'(t)]³</code>（三次方），分子是二阶行列式，与两个二阶导数之商有着根本的数学结构差异。</div>
<h3>1.9.1 几何进阶：参数曲线的曲率（Curvature）与密切圆</h3>
<p>在机器人轨迹规划与高速铁路设计中，曲线不能突变转向。曲率 <code>κ</code> 衡量切向量随弧长 s 的转动速率：<code>κ = |dφ/ds|</code>。由平面速度向量 <code>v(t) = (x'(t), y'(t))</code>，其单位切向量为 <code>T(t) = v(t) / ||v(t)||</code>。经过严格微商链式法则推导，参数曲线的曲率公式为：<b><code>κ(t) = | x'(t)y''(t) - y'(t)x''(t) | / [ (x'(t))² + (y'(t))² ]^(3/2)</code></b>。曲率半径 <code>R = 1/κ</code> 对应于该点处最佳相切的密切圆（Osculating Circle）半径，法向向心加速度即为 <code>a_n = v² / R = κ v²</code>。</p>
"""

p2_extra_80 = """
<h3>2.2.1 弧长公式的第一性原理：折线逼近与微元法</h3>
<p>如何严格定义并计算一条连续参数曲线 <code>C: (x(t), y(t)), a ≤ t ≤ b</code> 的长度？分割区间为 n 个小区间，相连折线总长为 <code>L_n = ∑ ||P_i - P_{i-1}|| = ∑ √[ (Δx_i)² + (Δy_i)² ]</code>。应用拉格朗日中值定理，分别存在 <code>c_i, d_i</code> 使得 <code>Δx_i = x'(c_i)Δt_i, Δy_i = y'(d_i)Δt_i</code>。取分割直径趋于 0 的黎曼极限，收敛至定积分：<b><code>L = ∫_a^b √[ (x'(t))² + (y'(t))² ] dt</code></b>。微元形式为 <code>ds = √[ (dx)² + (dy)² ] = √[ (x')² + (y')² ] dt</code>。</p>
<h3>2.16.1 极坐标下的斜率陷阱：切勿混淆 dr/dθ 与 dy/dx</h3>
<p>初学者常误以为极坐标切线斜率是 <code>dr/dθ</code>。实际上 <code>dr/dθ</code> 仅代表径向膨胀率。严格推导必须化为参数方程：<code>x = r(θ) cos θ, y = r(θ) sin θ</code>。相除可得：<b><code>dy/dx = ( (dr/dθ) sin θ + r cos θ ) / ( (dr/dθ) cos θ - r sin θ )</code></b>。在极点处（r = 0），若 <code>dr/dθ ≠ 0</code>，退化为 <code>dy/dx = tan θ</code>，切线正是穿过极点的射线！</p>
"""

p3_extra_80 = """
<h3>3.7.1 坐标变换的局部体积变形率：雅可比行列式（Jacobian）推导</h3>
<p>在多变量重积分变换中，必须乘以变换的雅可比行列式作为局域体积缩放比：</p>
<p><b>1. 柱坐标</b>：变换 <code>x = r cos θ, y = r sin θ, z = z</code>。计算偏导行列式 <code>J_{cyl} = r(cos²θ + sin²θ) = r</code>。空间微元体积为 <b><code>dV = r dr dθ dz</code></b>。</p>
<p><b>2. 球坐标</b>：变换 <code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code>。计算三阶行列式可得 <code>J_{sph} = ρ² sin φ</code>。空间球微元体积为 <b><code>dV = ρ² sin φ dρ dφ dθ</code></b>。这从根本上证明了重积分中不可遗漏的几何因子。</p>
"""

p4_extra_80 = """
<h3>4.6.1 为什么矩阵乘法是“行乘列”：线性映射复合的本质推导</h3>
<p>矩阵的本质是向量空间之间的线性映射。设有映射 <code>y = B u</code>（将 u 从 p 维变至 n 维）与 <code>x = A y</code>（将 y 从 n 维变至 m 维）。复合映射为 <code>x = A(B u) = C u</code>。展开分量：<code>x_i = ∑_{j=1}^n A_{ij} ( ∑_{k=1}^p B_{jk} u_k ) = ∑_{k=1}^p ( ∑_{j=1}^n A_{ij} B_{jk} ) u_k</code>。由 u 的任意性，必定恒等满足 <b><code>C_{ik} = ∑_{j=1}^n A_{ij} B_{jk}</code></b>。这证明了行乘列求和是线性映射保持复合自洽的唯一必然结果！</p>
<h3>4.10.1 经典几何变换矩阵的严密推导：平面正交旋转矩阵</h3>
<p>标准正交基 <code>e₁=(1, 0)ᵀ</code> 旋转 θ 后落在 <code>(cos θ, sin θ)ᵀ</code>；<code>e₂=(0, 1)ᵀ</code> 旋转后落在 <code>(-sin θ, cos θ)ᵀ</code>。拼装成列即得二维旋转矩阵：<b><code>R(θ) = [ cos θ, -sin θ ; sin θ, cos θ ]</code></b>。它满足 <code>det(R)=1</code> 且 <code>Rᵀ R = I</code>（保长保角保面积）。</p>
"""

p5_extra_80 = """
<h3>5.3.1 伴随矩阵与逆矩阵核心恒等式的严格证明</h3>
<p>教科书给出逆矩阵公式 <code>A⁻¹ = (1/det A) adj(A)</code>。证明基于核心引理 <b><code>A · adj(A) = det(A) · I</code></b>：乘积矩阵的第 (i, k) 个元素为 <code>P_{ik} = ∑_{j=1}^n A_{ij} C_{kj}</code>。当 i = k 时，这正是 A 沿第 i 行的余子式展开，结果为 <code>det(A)</code>；当 i ≠ k 时，等价于将 A 的第 k 行替换为第 i 行后求行列式，由于两行相同行列式必为 0！故非对角元全为 0。两边同除 <code>det(A)</code> 严格得出逆矩阵公式。 $\blacksquare$</p>
"""

p6_extra_80 = """
<h3>6.3.1 高斯消元背后的矩阵代数：初等行变换等于左乘初等矩阵</h3>
<p>每一种初等行变换都严格等价于左乘一个可逆初等矩阵：换行对应置换阵 <code>E_{i↔j} (det=-1)</code>，数乘对应伸缩阵 <code>E_{i(k)} (det=k≠0)</code>，倍加对应剪切三角阵 <code>E_{j+c*i} (det=1)</code>。消元过程就是构造一系列可逆阵使得 <code>E_k ... E₁ A = R</code>。</p>
<h3>6.3.2 线性方程组解结构的完备定理：Rouché–Capelli 判定法则</h3>
<p>对于方程 <code>A x = b</code>：若 <code>rank(A) < rank([A|b])</code> 则无解；若 <code>rank(A) = rank([A|b]) = n</code> 则有唯一解；若 <code>rank(A) = rank([A|b]) = r < n</code> 则有无穷多解，解集维度为 <code>n - r</code>（即零空间维度 Nullity）。</p>
"""

p7_extra_80 = """
<h3>7.1.1 特征值与不变子空间理论深度推导</h3>
<p>线性变换中满足 <code>A v = λ v (v ≠ 0)</code> 的向量构成变换的一维不变子空间。改写为齐次方程 <code>(A - λ I) v = 0</code>。该齐次组有非零解当且仅当系数矩阵不可逆，即特征方程 <b><code>det(A - λ I) = 0</code></b>。特征值的和等于矩阵的迹（<code>∑ λ_i = tr(A)</code>），特征值的乘积等于行列式（<code>∏ λ_i = det(A)</code>）。若存在某个特征值的几何重数（特征子空间维度）小于代数重数（根的重数），则矩阵亏损（Defective），无法对角化。</p>
"""

p8_extra_80 = """
<h3>8.6 柯西-施瓦茨不等式（Cauchy-Schwarz Inequality）的经典代数证明</h3>
<p>在任意内积空间中，柯西-施瓦茨不等式 <b><code>|u · v| ≤ ||u|| ||v||</code></b> 是定义多维夹角的先决保障。证明：构造向量 <code>w(t) = u + t v</code>。其模平方恒非负：<code>||u + t v||² = ||u||² + 2t (u · v) + t² ||v||² ≥ 0, ∀ t ∈ ℝ</code>。这是一个关于 t 的开口向上一元二次函数。其判别式必须小于等于零：<code>Δ = 4(u · v)² - 4 ||u||² ||v||² ≤ 0 ⟹ (u · v)² ≤ ||u||² ||v||²</code>。开方即得不等式。等号成立当且仅当 u 与 v 线性相关（共线）。 $\blacksquare$</p>
<h3>8.7 三角不等式（Triangle Inequality）的推导</h3>
<p>展开 <code>||u + v||² = ||u||² + 2(u · v) + ||v||² ≤ ||u||² + 2|u · v| + ||v||² ≤ ||u||² + 2||u||||v|| + ||v||² = (||u|| + ||v||)²</code>。开方即得 <b><code>||u + v|| ≤ ||u|| + ||v||</code></b>。</p>
"""

for l in d80['lectures']:
    s = l['slug']
    if s == 'ch1-parametric-curves':
        l['html'] = inject_to_section(l['html'], 'detail', p1_extra_80, '1.9 参数曲线的斜率')
    elif s == 'ch1-arc-polar':
        l['html'] = inject_to_section(l['html'], 'detail', p2_extra_80, '2.2.1 弧长公式')
    elif s == 'ch2-cyl-spherical':
        l['html'] = inject_to_section(l['html'], 'detail', p3_extra_80, '3.7.1 坐标变换')
    elif s == 'ch2-matrices':
        l['html'] = inject_to_section(l['html'], 'detail', p4_extra_80, '4.6.1 为什么矩阵乘法')
    elif s == 'ch3-determinant-inverse':
        l['html'] = inject_to_section(l['html'], 'detail', p5_extra_80, '5.3.1 伴随矩阵')
    elif s == 'ch3-gaussian-elimination':
        l['html'] = inject_to_section(l['html'], 'detail', p6_extra_80, '6.3.1 高斯消元背后的矩阵代数')
    elif s == 'ch3-eigenvalues-cramer':
        l['html'] = inject_to_section(l['html'], 'detail', p7_extra_80, '7.1.1 特征值与不变子空间')
    elif s == 'ch4-vectors-dot-product':
        l['html'] = inject_to_section(l['html'], 'detail', p8_extra_80, '8.6 柯西-施瓦茨不等式')

with io.open(p80, 'w', encoding='utf-8') as f:
    json.dump(d80, f, ensure_ascii=False, indent=2)
print('[OK] 80 工程数学 II 全章节深度增强完成')

# ==============================================================================
# 5. 深度升级 62 (工程数学 I)
# ==============================================================================
p62 = os.path.join(CONTENT, '62.json')
with io.open(p62, 'r', encoding='utf-8') as f:
    d62 = json.load(f)

t2_extra_62 = """
<h3>2.0 极限的本质形式化：柯西 ε-δ 语言与严谨证明</h3>
<p>形式化定义：设函数 f 在包含 c 的开区间上有定义。我们称 <code>lim_{x→c} f(x) = L</code>，如果对任意给定的 <code>ε > 0</code>，都存在一个 <code>δ > 0</code>，使得只要 <code>0 < |x - c| < δ</code>，恒有 <b><code>|f(x) - L| < ε</code></b>。</p>
<p><b>【典范证明】用 ε-δ 证明 <code>lim_{x→3} (2x + 1) = 7</code></b>：欲使 <code>|(2x + 1) - 7| < ε ⟺ 2|x - 3| < ε ⟺ |x - 3| < ε/2</code>。对任意给定的 <code>ε > 0</code>，取 <code>δ = ε/2 > 0</code>。当 <code>0 < |x - 3| < δ</code> 时，恒有 <code>|(2x + 1) - 7| = 2|x - 3| < 2δ = ε</code>。由极限定义命题获证。 $\blacksquare$</p>
<h3>2.5.1 夹逼定理（Squeeze Theorem）与第一重要极限</h3>
<p>若在 c 的去心邻域内 <code>g(x) ≤ f(x) ≤ h(x)</code> 且 <code>lim g = lim h = L</code>，则 <code>lim f = L</code>。典范应用：证明 <code>lim_{x→0} x² sin(1/x) = 0</code>。由 <code>-1 ≤ sin(1/x) ≤ 1</code>，两端乘 x² 夹逼，当 x→0 时两端趋于 0，中间逼迫收敛于 0。</p>
"""

t3_extra_62 = """
<h3>3.1.1 乘积法则（Product Rule）的严密代数推导</h3>
<p>导数定义式：<code>d/dx [f(x)g(x)] = lim_{h→0} [ f(x+h)g(x+h) - f(x)g(x) ] / h</code>。在分子中同时减去并加上 <code>f(x+h)g(x)</code>：拆分为 <code>lim f(x+h) [(g(x+h)-g(x))/h] + lim g(x) [(f(x+h)-f(x))/h]</code>。由 f 的可导必连续性 <code>lim f(x+h) = f(x)</code>，两项极限分别收敛，严格得出 <b><code>(f g)' = f g' + f' g</code></b>。 $\blacksquare$</p>
"""

t4_extra_62 = """
<h3>4.2.1 微分中值定理体系链：罗尔 ⟹ 拉格朗日 ⟹ 柯西中值定理</h3>
<p>1. <b>罗尔定理</b>：f 在 [a, b] 连续在 (a, b) 可导且 f(a)=f(b)，必有 <code>f'(c) = 0</code>。</p>
<p>2. <b>拉格朗日中值定理</b>：构造辅助函数 <code>F(x) = f(x) - [ f(a) + (f(b)-f(a))/(b-a) · (x-a) ]</code>。由于 <code>F(a)=F(b)=0</code>，应用罗尔定理得存在 c 满足 <b><code>f(b) - f(a) = f'(c)(b - a)</code></b>（有限增量公式）。</p>
<p>3. <b>柯西中值定理</b>：构造 <code>G(x) = [f(b)-f(a)]g(x) - [g(b)-g(a)]f(x)</code>，同理推导 <b><code>f'(c) / g'(c) = [f(b)-f(a)] / [g(b)-g(a)]</code></b>，奠定了洛必达法则的严格证明基石。</p>
"""

t7_extra_62 = """
<h3>7.1.1 微积分基本定理（FTC）第一与第二部分的严密证明</h3>
<p><b>【FTC 第一部分证明：变上限积分导数等于被积函数】</b>：设 <code>F(x) = ∫_a^x f(t) dt</code>。导数差商为 <code>1/h ∫_x^{x+h} f(t) dt</code>。由积分中值定理，存在 <code>c_h</code> 介于 x 与 x+h 之间使得积分等于 <code>f(c_h) · h</code>。当 h→0 时中值点 <code>c_h → x</code>，由 f 连续性极限收敛至 <code>f(x)</code>，证得 <b><code>d/dx [ ∫_a^x f(t) dt ] = f(x)</code></b>。</p>
<p><b>【FTC 第二部分（牛顿-莱布尼茨公式）证明】</b>：设 G(x) 为任意原函数，则 <code>G(x) = ∫_a^x f(t) dt + C</code>。代入 x=a 得 <code>C = G(a)</code>；代入 x=b 移项得 <b><code>∫_a^b f(t) dt = G(b) - G(a)</code></b>。定理完全获证。 $\blacksquare$</p>
"""

for l in d62['lectures']:
    s = l['slug']
    if s == 't2-limits-continuity':
        l['html'] = inject_to_section(l['html'], 'detail', t2_extra_62, '2.0 极限的本质')
    elif s == 't3-derivatives-rules':
        l['html'] = inject_to_section(l['html'], 'detail', t3_extra_62, '3.1.1 乘积法则')
    elif s == 't4-higher-order-extrema-implicit':
        l['html'] = inject_to_section(l['html'], 'detail', t4_extra_62, '4.2.1 微分中值')
    elif s == 't7-integration-techniques':
        l['html'] = inject_to_section(l['html'], 'detail', t7_extra_62, '7.1.1 微积分基本定理')

with io.open(p62, 'w', encoding='utf-8') as f:
    json.dump(d62, f, ensure_ascii=False, indent=2)
print('[OK] 62 工程数学 I 全章节深度增强完成')

# ==============================================================================
# 6. 深度升级 86 (计算机导论)
# ==============================================================================
p86 = os.path.join(CONTENT, '86.json')
with io.open(p86, 'r', encoding='utf-8') as f:
    d86 = json.load(f)

w2_extra_86 = """
<h3>1.0 进位记数法的数学抽象与进制转换的代数原理</h3>
<p>任意实数 N 在基数 b 下的幂级数展开：<code>N = ∑ a_i b^i</code>。整数除基取余法的数学原理：对 N 带余除法 <code>N = Q₀ b + r₀</code>。对比多项式展开，首次求余所得的 <code>r₀</code> 必为最低有效位（LSB）<code>a₀</code>，递推除法直到商为 0，余数逆序排列即为高位到低位的进制表示。</p>
"""
w3_extra_86 = """
<h3>1.3 浮点数灾难性抵消（Catastrophic Cancellation）与数值算法防御</h3>
<p>当两相近浮点数相减时，高位相消导致有效位数骤降，舍入噪声被放大。例如二次方程求根公式 <code>x = (-b + √(b²-4ac))/(2a)</code> 当 <code>b² ≫ 4ac</code> 时分子产生相消。工业防御算法改用韦达定理：先算大根 <code>x₁ = [ -b - sgn(b)√(b²-4ac) ] / (2a)</code>，再算小根 <code>x₂ = c / (a x₁)</code>，完全消除灾难性抵消误差。</p>
"""
w4_extra_86 = """
<h3>1.3.1 UTF-8 编码的前缀自同步特性（Self-Synchronization）</h3>
<p>UTF-8 字符起始字节以 <code>0</code>（单字节）或 <code>11...0</code>（多字节）开头，后续字节恒以 <code>10</code> 开头。网络丢包错位时，解码器只需跳过后续 <code>10</code> 字节，遇到首字节即刻重获同步，绝无全局乱码蔓延风险；且以单个 8 位字节处理，完全消除字节序（Endian）BOM 困扰。</p>
"""
w7_extra_86 = """
<h3>1.3.1 香农第一信源编码定理（Shannon's Source Coding Theorem）与熵界</h3>
<p>离散无记忆信源的信息熵为 <code>H(X) = - ∑ p_i log₂ p_i</code> 比特/符号。核心定理指出：任意无损前缀编码的平均码长下界必为 <code>L ≥ H(X)</code>。霍夫曼编码（Huffman Coding）以贪心二叉树构建，逼近该熵界极限：<code>H(X) ≤ L_{Huffman} < H(X) + 1</code>。</p>
"""
w9_extra_86 = """
<h3>1.3.1 倒排索引求交优化：跳表指针（Skip Pointers）</h3>
<p>处理“词 A AND 词 B”布尔查询时，常规双指针归并需 <code>O(m + n)</code> 时间。跳表技术在链表上每隔 <code>√L</code> 个节点建立快速跳转指针，比较时直接跨块跃迁，复杂度降至 <code>O(√L)</code>，配合 AVX-512 SIMD 并行指令实现毫秒级大规模文档检索。</p>
"""

for l in d86['lectures']:
    s = l['slug']
    if s == 'w2-number-systems':
        l['html'] = inject_to_section(l['html'], 'detail', w2_extra_86, '1.0 进位记数法')
    elif s == 'w3-signed-numbers-and-float':
        l['html'] = inject_to_section(l['html'], 'detail', w3_extra_86, '1.3 浮点数灾难性抵消')
    elif s == 'w4-character-encoding':
        l['html'] = inject_to_section(l['html'], 'detail', w4_extra_86, '1.3.1 UTF-8')
    elif s == 'w7-data-compression':
        l['html'] = inject_to_section(l['html'], 'detail', w7_extra_86, '1.3.1 香农第一信源')
    elif s == 'w9-information-retrieval':
        l['html'] = inject_to_section(l['html'], 'detail', w9_extra_86, '1.3.1 倒排索引求交优化')

with io.open(p86, 'w', encoding='utf-8') as f:
    json.dump(d86, f, ensure_ascii=False, indent=2)
print('[OK] 86 计算机导论全章节深度增强完成')

# ==============================================================================
# 7. 深度升级 30565 (数学 A / 离散数学)
# ==============================================================================
p30565 = os.path.join(CONTENT, '30565.json')
with io.open(p30565, 'r', encoding='utf-8') as f:
    d30565 = json.load(f)

card_extra_30565 = """
<h3>6.0 从伽利略悖论到无限基数：双射作为度量无限的唯一尺度</h3>
<p>康托尔确立了无限基数的公理化标准：两集合等势（<code>|A| = |B|</code>）当且仅当存在双射 <code>f: A → B</code>。与自然数等势的集合称为可数无限集（基数记为 <code>ℵ₀</code>）。</p>
<h3>6.1 康托尔配对函数与有理数集 ℚ 的可数性严密证明</h3>
<p>有理数在数轴处处稠密，但基数依然是可数的！构造配对函数 <code>π(k₁, k₂) = [ (k₁ + k₂ - 1)(k₁ + k₂ - 2) ] / 2 + k₂</code> 沿斜对角线遍历 <code>ℕ⁺ × ℕ⁺</code>，建立了显式双射，证明了 <code>|ℚ| = |ℕ| = ℵ₀</code>。</p>
<h3>6.2 希尔伯特无限旅馆的数学分段函数构造</h3>
<p>再来一辆无限大巴时：原房客 <code>f(n) = 2n</code>，新客人 <code>g(k) = 2k - 1</code>。再来可数无限辆大巴时：利用质数幂分解定理，原房客住 <code>2ⁿ</code> 房，第 i 辆大巴第 j 位客人住 <code>p_{i+1}^j</code> 房，因质数互质绝无重房冲突！</p>
<h3>6.3 康托尔定理的本质证明：|S| < |P(S)| 对角线子集反证法</h3>
<p>证明任意集合的幂集势严格大于原集：构造对角子集 <code>D = { x ∈ S | x ∉ f(x) }</code>。若存在满射 f 使得 <code>f(d) = D</code>，无论 <code>d ∈ D</code> 还是 <code>d ∉ D</code> 均导致不可消除的逻辑悖论！故不存在满射，证得 <code>|S| < |P(S)|</code>。 $\blacksquare$</p>
"""

for l in d30565['lectures']:
    if l['slug'] == 'cardinality-countable-sets':
        l['html'] = inject_to_section(l['html'], 'detail', card_extra_30565, '6.0 从伽利略悖论')

with io.open(p30565, 'w', encoding='utf-8') as f:
    json.dump(d30565, f, ensure_ascii=False, indent=2)
print('[OK] 30565 离散数学核心讲义深度重构完成')

# ==============================================================================
# 8. 深度升级 30361 (软件工程基础)
# ==============================================================================
p30361 = os.path.join(CONTENT, '30361.json')
with io.open(p30361, 'r', encoding='utf-8') as f:
    d30361 = json.load(f)

sdlc_extra_30361 = """
<h3>2.0 软件工程经济学定律：Boehm 缺陷修复成本指数曲线</h3>
<p>巴里·勃姆（Barry Boehm）实证统计表明：缺陷修复成本随阶段呈指数级剧增。需求阶段修复为 1×，编码阶段为 5~10×，系统测试阶段为 20~50×，而生产上线阶段飙升至 100~200× 以上！这确立了现代敏捷开发与自动化测试左移（Shift-Left Testing）的根本经济学驱动力。</p>
"""
arch_extra_30361 = """
<h3>6.0 分布式系统设计的基石定理：CAP 定理的严格反证</h3>
<p>在不可避免网络分区的真实物理世界中，分布式系统无法同时兼顾强一致性（C）与高可用性（A）：写入节点因网络无法同步到远程节点时，若等待同步则系统阻塞失去可用性（成为 CP 系统），若立即响应则远程节点读出旧数据失去一致性（成为 AP 系统）。架构师的核心工作是在 CP 与 AP 之间做出符合业务场景的明智权衡。</p>
"""
test_extra_30361 = """
<h3>7.0 白盒测试复杂度度量：麦凯布圈复杂度（McCabe Cyclomatic Complexity）</h3>
<p>控制流图圈复杂度公式为 <code>V(G) = E - V + 2 = π + 1</code>（其中 π 为判断节点数）。它给出了实现基本路径全覆盖测试（Basis Path Testing）所需设计的最小线性无关测试用例数量下界。</p>
"""

for l in d30361['lectures']:
    s = l['slug']
    if s == 'l02-sdlc-models-and-agile':
        l['html'] = inject_to_section(l['html'], 'detail', sdlc_extra_30361, '2.0 软件工程经济学')
    elif s == 'l06-architectural-design':
        l['html'] = inject_to_section(l['html'], 'detail', arch_extra_30361, '6.0 分布式系统设计')
    elif s == 'l07-testing-and-quality':
        l['html'] = inject_to_section(l['html'], 'detail', test_extra_30361, '7.0 白盒测试复杂度')

with io.open(p30361, 'w', encoding='utf-8') as f:
    json.dump(d30361, f, ensure_ascii=False, indent=2)
print('[OK] 30361 软件工程基础全章节深度增强完成')

print('\n========================================')
print('全站主要学科讲义增强与文不对题修复全部成功！')
print('========================================')
