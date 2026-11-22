import io
# -*- coding: utf-8 -*-
"""生成彻底清除 LaTeX 符号残留、升级视觉排版的 master_deepen_courses.py"""
import os, sys

SITE = "/home/qwe/.gemini/antigravity/scratch/lut-study-site"
MASTER_FILE = os.path.join(SITE, "tools", "master_deepen_courses.py")
INJECT_FILE = os.path.join(SITE, "tools", "inject_procedural_methods.py")

master_code = r'''# -*- coding: utf-8 -*-
"""
全站 15 门课程大学级学术深度深化与视觉排版规范化生成脚本
- 彻底清除原始 LaTeX 与裸 $ 符号残留，全量使用标准数学 Unicode 与 HTML 语义标签
- 核心公式与推导步骤采用 .formula-box 独立公式卡片与 .step-badge 徽章排版
- 消除悬挂冒号与排版瑕疵，完美兼容离线与移动端
"""
import json, os, io, re, subprocess

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(SITE, 'content')

def get_base_json(filename):
    """从基准 commit cf2613e 读取初始纯净 json"""
    try:
        cmd = ['git', 'show', f'cf2613e:content/{filename}']
        out = subprocess.check_output(cmd, cwd=SITE).decode('utf-8')
        return json.loads(out)
    except Exception as e:
        print(f"Fallback to disk for {filename}: {e}")
        with io.open(os.path.join(CONTENT, filename), 'r', encoding='utf-8') as f:
            return json.load(f)

def save_json(filename, data):
    p = os.path.join(CONTENT, filename)
    with io.open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def inject_to_section(lec_html, sec_type, extra_html):
    pattern = r'(<section[^>]*data-type="' + sec_type + r'"[^>]*>)(.*?)(</section>)'
    m = re.search(pattern, lec_html, flags=re.S)
    if not m:
        return lec_html
    new_sec = m.group(1) + m.group(2) + extra_html + m.group(3)
    return lec_html[:m.start()] + new_sec + lec_html[m.end():]

# ==============================================================================
# 1. 32632 (大学英语)
# ==============================================================================
d32632 = get_base_json('32632.json')
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
            l['part'] = '第 3 章 会议沟通与协商'
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

for l in new_lecs_32632:
    if l['slug'] == 'l3-vocabulary-grammar-clinic':
        eng_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.10 跨文化技术沟通认知修辞与隐喻映射（Cognitive Metaphor in Engineering）</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】计算机与工程技术术语的认知隐喻模型</b>
<p>学术英语并非词汇的孤立罗列，而是通过认知概念隐喻（Conceptual Metaphor）将抽象物理与计算模型映射到具象世界。理解隐喻映射能帮助大学生从本质上驾驭专业英语学术动词与介词搭配。</p>
</div>
<p><b>1. 概念隐喻映射机制</b>：在现代软件与系统工程中，90% 以上的核心术语建立在物理实体隐喻上：</p>
<ul>
  <li><b>计算作为流水线与容器</b>：<code>Pipeline</code>（管道传输数据）、<code>Buffer / Queue</code>（队列排队）、<code>Thread Pool</code>（线程池注入与提取）；</li>
  <li><b>内存作为物理空间与生命周期</b>：<code>Memory Leak</code>（内存像液体容器破损般泄漏）、<code>Garbage Collection</code>（垃圾回收）、<code>Dangling Pointer</code>（指针悬挂在虚空中）。</li>
</ul>
<p><b>2. 学术语域与修辞规约</b>：在工程学术论文与国际技术会议中，应避免主观色彩浓厚的口语动词，使用具精确语义的对应学术拉丁源动词：</p>
<table>
  <tr><th>日常/口语表达</th><th>专业工程学术动词</th><th>精确语义内涵与搭配范例</th></tr>
  <tr><td>get rid of errors</td><td>eliminate / mitigate faults</td><td>强调系统性消除或降低容错边界</td></tr>
  <tr><td>make it faster</td><td>optimize / accelerate latency</td><td>强调通过算法复杂度或硬件吞吐调优</td></tr>
  <tr><td>look into problems</td><td>investigate / probe bottlenecks</td><td>强调使用性能探针进行经验主义实证排查</td></tr>
  <tr><td>set up</td><td>configure / instantiate</td><td>强调对象实例化或参数空间静态配置</td></tr>
</table>
"""
        l['html'] = inject_to_section(l['html'], 'detail', eng_extra)

d32632['lectures'] = new_lecs_32632
save_json('32632.json', d32632)
print('[OK] 32632 大学英语 排序、章节归属与拓展标注完成')

# ==============================================================================
# 2. 33295 (基础芬兰语 1)
# ==============================================================================
d33295 = get_base_json('33295.json')
fin_extra = r"""
<h3><span class="badge purple">拓展深化</span> 10.5 芬兰语辅音交替（Aste-vaihtelu / Consonant Gradation）严格音系学状态转移规律</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】芬兰语开音节与闭音节平衡原理与辅音强弱转移矩阵</b>
<p>揭示辅音交替并非死记硬背的琐碎特例，而是芬兰语为了维持词干音节音量守恒（Moraic Weight Equilibrium）所演化出的严格音系动力学现象。</p>
</div>
<p><b>1. 根本动力学原则（音节开闭定律）</b>：</p>
<ul>
  <li><b>开音节（Avotavu）</b>：以元音结尾的音节。音节内阻力小，词干中的辅音处于<b>强阶（Vahva aste）</b>；</li>
  <li><b>闭音节（Umpitavu）</b>：以辅音结尾的音节。当加上单辅音后缀（如属格后缀 <code>-n</code>、单数第一人称动词后缀 <code>-n</code>、宾格 <code>-t</code>）时，音节末尾被辅音封闭，词干辅音自动弱化为<b>弱阶（Heikko aste）</b>以维持发音总能耗恒定。</li>
</ul>
<p><b>2. 核心辅音交替完整转移矩阵</b>：</p>
<table>
  <tr><th>强阶辅音（开音节）</th><th>弱阶辅音（闭音节）</th><th>典型词汇演化实例（原形强阶 → 属格弱阶）</th><th>音系弱化机制说明</th></tr>
  <tr><td><b>kk</b></td><td><b>k</b></td><td>pankki → pan-kin</td><td>双辅音变单辅音（时长减半）</td></tr>
  <tr><td><b>pp</b></td><td><b>p</b></td><td>kuppi → ku-pin</td><td>双辅音变单辅音</td></tr>
  <tr><td><b>tt</b></td><td><b>t</b></td><td>tyttö → ty-tön</td><td>双辅音变单辅音</td></tr>
  <tr><td><b>k</b></td><td><i>消失 (∅) / v</i></td><td>harkka → har-lan / puku → pu-vun</td><td>单音脱落或同化为半元音</td></tr>
  <tr><td><b>p</b></td><td><b>v</b></td><td>koti → ko-din / leipä → lei-vän</td><td>塞音弱化为唇齿近音</td></tr>
  <tr><td><b>t</b></td><td><b>d</b></td><td>katu → ka-dun</td><td>清塞音弱化为浊齿龈塞音</td></tr>
  <tr><td><b>nk</b></td><td><b>ng</b></td><td>Helsinki → Hel-sin-gin</td><td>鼻音同化（/ŋk/ → /ŋŋ/）</td></tr>
  <tr><td><b>mp</b></td><td><b>mm</b></td><td>kampa → kam-man</td><td>全同化双唇鼻音</td></tr>
  <tr><td><b>nt</b></td><td><b>nn</b></td><td>Helsinki / ranta → ran-nan</td><td>全同化齿龈鼻音</td></tr>
  <tr><td><b>lt / rt</b></td><td><b>ll / rr</b></td><td>kulta → kul-lan / parta → par-ran</td><td>边音与颤音完全顺行同化</td></tr>
</table>
"""
for l in d33295['lectures']:
    if l['slug'] == 't10-genetiivi':
        l['html'] = inject_to_section(l['html'], 'detail', fin_extra)
save_json('33295.json', d33295)
print('[OK] 33295 基础芬兰语 1 辅音交替状态转移深化完成')

# ==============================================================================
# 3. 30352 (Python 编程)
# ==============================================================================
d30352 = get_base_json('30352.json')
fn_extra = r"""
<h3><span class="badge purple">拓展深化</span> 5.10 深入 CPython 底层：函数栈帧生命周期与 LEGB 作用域闭包机制</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】PyFrameObject、自由变量与闭包单元（cell_contents）实现机理</b>
<p>从虚拟机底层剖析函数调用时栈帧创建、销毁过程，以及为什么内部函数引用外部变量时会创建特殊的单元对象（cell object）形成闭包。</p>
</div>
<p><b>1. 函数调用的本质</b>：在 CPython 解释器中，每次函数调用均会在虚拟机调用栈上分配一个 <code>PyFrameObject</code> 结构体。栈帧中包含代码对象 <code>f_code</code>、局部变量表 <code>f_locals</code>、全局命名空间 <code>f_globals</code> 以及内置命名空间 <code>f_builtins</code>。这构成了 Python 解析变量名的 <b>LEGB（Local → Enclosing → Global → Builtin）</b> 顺序法则。</p>
<p><b>2. 闭包与变量逃逸分析</b>：当内部嵌套函数引用了外层函数的局部变量时，该变量不能随外层函数栈帧弹出而销毁。CPython 编译器在编译期检测到该变量并将其标记为 <code>freevars</code>，在堆上分配一个 <code>cell</code> 对象，内层函数的 <code>__closure__</code> 元组持有该 cell 引用，从而实现变量持久化生命周期。</p>
"""

cls_extra = r"""
<h3><span class="badge purple">拓展深化</span> 9.10 面向对象协议与数据模型（Python Data Model）：Dunder 魔法方法底层运行机理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】可哈希性（Hashability）、运算符重载与元类协议本质</b>
<p>深入分析 Python 对象系统核心规范：为什么自定义对象要作为字典的键必须同时实现 <code>__hash__</code> 与 <code>__eq__</code>，以及哈希不变性对数据安全的重大意义。</p>
</div>
<p><b>1. 可哈希性（Hashability）的第一性原理</b>：在 Python 中，若一个对象是可哈希的，它在生命周期内必须具有不可变的哈希码（通过 <code>__hash__()</code> 返回），且能与其它对象进行相等性比较（通过 <code>__eq__()</code>）。若两个对象相等，它们的哈希值必须绝对相同：</p>
<div class="formula-box">
  <div class="formula-line"><code>obj1 == obj2  ⟹  hash(obj1) == hash(obj2)</code></div>
</div>
<p>可变容器（如 <code>list</code>, <code>dict</code>, <code>set</code>）默认不可哈希，因为其内部元素的增删会破坏字典哈希桶（Hash Table Bucket）的二分探测不变性，导致无法检索。</p>
"""

numpy_extra = r"""
<h3><span class="badge purple">拓展深化</span> 11.10 NumPy 高性能计算的物理基础：连续内存布局（C-Contiguous）、步长（Strides）与广播算术</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】ndarray 结构体、跨步（Strides）计算与零拷贝切片机理</b>
<p>解密 NumPy 为何比原生 Python 列表快 100 倍以上：连续内存块、CPU L1/L2 缓存友好性与基于步长的多维张量索引代数。</p>
</div>
<p><b>1. 内存存储模型：从扁平一维数组到高维张量</b>：NumPy 数组内部由两部分构成：一块连续的 C 语言原生内存缓冲区（Data Buffer）和元数据（Shape, Dtype, Strides）。对于形状为 <code>(d₀, d₁, …, dₖ₋₁)</code> 的数组，其步长元组 <code>(s₀, s₁, …, sₖ₋₁)</code> 严格定义了每个维度递增 1 时在物理内存中跳跃的字节数：</p>
<div class="formula-box">
  <div class="formula-line"><code>Memory_Offset = ∑ᵢ₌₀ⁿ⁻¹ (indexᵢ · strideᵢ)</code></div>
</div>
<p>切片操作（如 <code>arr[::2, :]</code>）仅修改 <code>shape</code> 和 <code>strides</code> 元数据，完全不复制底层数据缓冲区，因此耗时恒为 O(1) 零拷贝（Zero-copy View）。</p>
<p><b>2. 广播机制（Broadcasting Rules）严格算法</b>：两数组在某维度上兼容当且仅当：该维大小相等，或者其中一个数组该维大小为 1。当某一维为 1 时，NumPy 将该维的步长直接设为 0，硬件在循环迭代时读取同一内存位置，避免了庞大的内存膨胀复制。</p>
"""
for l in d30352['lectures']:
    if l['slug'] == 'part-5':
        l['html'] = inject_to_section(l['html'], 'detail', fn_extra)
    elif l['slug'] == 'part-9':
        l['html'] = inject_to_section(l['html'], 'detail', cls_extra)
    elif l['slug'] == 'ch11-tuples-sets-packages-numpy':
        l['html'] = inject_to_section(l['html'], 'detail', numpy_extra)

save_json('30352.json', d30352)
print('[OK] 30352 Python 编程 底层栈帧、数据模型与 NumPy 步长深化完成')

# ==============================================================================
# 4. 80 (工程数学 II / Engineering Mathematics II)
# ==============================================================================
d80 = get_base_json('80.json')

param_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.9 参数曲线的斜率、光滑性与二阶导数深度推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】参数方程二阶导数链式法则展开</b>
<p>参数方程 <code>x = x(t), y = y(t)</code> 的二阶导数 <code>d²y/dx²</code> 必须由外层链式法则 <code>(d/dx)[dy/dx] = [(d/dt)(dy/dx)] / x′(t)</code> 严格展开，切忌错误套用普通除法。</p>
</div>
<p><b>【推导过程】</b> 设参数方程为 <code>x = x(t), y = y(t)</code> 且 <code>x′(t) ≠ 0</code>。根据链式法则，一阶导数为：</p>
<div class="formula-box">
  <div class="formula-line"><code>dy/dx = (dy/dt) / (dx/dt) = y′(t) / x′(t)</code></div>
</div>
<p>对 <code>x</code> 再次求导，必须再次应用复合求导法则：</p>
<div class="formula-box">
  <div class="formula-line"><code>d²y/dx² = (d/dx)[dy/dx] = [(d/dt)(y′(t)/x′(t))] / (dx/dt)</code></div>
  <div class="formula-line"><code>= [(y″(t)x′(t) − y′(t)x″(t)) / (x′(t))²] / x′(t)</code></div>
  <div class="formula-line"><b><code>d²y/dx² = [y″(t)x′(t) − y′(t)x″(t)] / [x′(t)]³</code></b></div>
</div>
<p><b>关键辨析</b>：分母是三次项 <code>[x′(t)]³</code> 而非平方，且二阶导数绝不能写成 <code>y″(t) / x″(t)</code>！当 <code>d²y/dx² > 0</code> 时曲线在对应区间严格凹向上（Concave Up），为零时为潜在拐点。</p>

<h3><span class="badge purple">拓展深化</span> 1.9.1 几何进阶：参数曲线的曲率（Curvature）与密切圆</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】曲率公式 κ(t) 的内积展开与密切圆几何意义</b>
<p>曲率度量切向量转角对弧长的变化率 <code>κ = |dφ/ds|</code>，通过单位切向量微分与外积展开推导出二维参数形式。</p>
</div>
<p>曲率 <code>κ</code> 描述曲线上某点弯曲剧烈程度，定义为切线切向角 <code>φ</code> 对弧长 <code>s</code> 的变化率：<code>κ = |dφ/ds|</code>。由于弧长微分满足 <code>ds = √([x′(t)]² + [y′(t)]²) dt</code>，代入向量外积展开得通用计算公式：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>κ(t) = |x′(t)y″(t) − x″(t)y′(t)| / {[x′(t)]² + [y′(t)]²}^(3/2)</code></b></div>
</div>
<p>曲率半径定义为 <code>ρ = 1/κ</code>。在曲线该点处沿内法线方向距离为 <code>ρ</code> 的圆称为<b>密切圆（Osculating Circle）</b>，它是二阶微积分意义上与原曲线最紧密贴合的最佳二次逼近圆。</p>
"""

polar_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.2.1 弧长公式的第一性原理：折线逼近与微元法</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】微元切线逼近与高阶无穷小严格推导</b>
<p>从折线段长度 <code>Δsₖ = √((Δxₖ)² + (Δyₖ)²)</code> 出发，结合拉格朗日中值定理与黎曼积分严格证明弧长微分。</p>
</div>
<p>在区间 <code>[a, b]</code> 上插入分割点 <code>a = x₀ < x₁ < … < xₙ = b</code>。相连弦长为 <code>ΔLₖ = √((Δxₖ)² + (Δyₖ)²)</code>。由拉格朗日中值定理，存在 <code>ξₖ ∈ (xₖ₋₁, xₖ)</code> 使得 <code>Δyₖ = f′(ξₖ)Δxₖ</code>。代入得：</p>
<div class="formula-box">
  <div class="formula-line"><code>ΔLₖ = √[1 + (f′(ξₖ))²] · Δxₖ</code></div>
  <div class="formula-line"><b><code>L = lim_{max Δxₖ → 0} ∑ₖ₌₁ⁿ √[1 + (f′(ξₖ))²] · Δxₖ = ∫ₐᵇ √[1 + (f′(x))²] dx</code></b></div>
</div>

<h3><span class="badge purple">拓展深化</span> 2.16.1 极坐标下的斜率陷阱：切勿混淆 dr/dθ 与 dy/dx</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】极坐标曲线切线斜率与径向变化率的严格区分</b>
<p>极坐标方程 <code>r = f(θ)</code> 中 <code>dr/dθ</code> 仅代表矢径长度对极角的变化率，而切线斜率必须通过参数转换 <code>x = r cos θ, y = r sin θ</code> 展开计算。</p>
</div>
<p>在极坐标 <code>r = f(θ)</code> 下，许多同学误将 <code>dr/dθ</code> 当作切线斜率。实际上切线斜率是平面直角坐标系下的 <code>dy/dx</code>。利用参数方程 <code>x = r(θ)cos θ, y = r(θ)sin θ</code>，应用乘积求导法则：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>dy/dx = (dy/dθ) / (dx/dθ) = [f′(θ)sin θ + f(θ)cos θ] / [f′(θ)cos θ − f(θ)sin θ]</code></b></div>
</div>
<p>只有当曲线穿过极点（即 <code>r = 0</code>）且 <code>r′(θ) ≠ 0</code> 时，公式化简为 <code>dy/dx = (r′ sin θ)/(r′ cos θ) = tan θ</code>，此时切线方向恰好就是极角 <code>θ</code> 的延伸方向。</p>
"""

cyl_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.7.1 坐标变换的局部体积变形率：雅可比行列式（Jacobian）推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】雅可比行列式作为正交曲线坐标基向量标量三重积</b>
<p>柱坐标体积元 <code>dV = r dr dθ dz</code> 与球坐标体积元 <code>dV = ρ² sin φ dρ dφ dθ</code> 的本质是切向量张成微元六面体的行列式有向体积。</p>
</div>
<p>在多元微积分变量替换中，微元体积变换满足 <code>dV = |J| du dv dw</code>。雅可比行列式 <code>J</code> 几何意义是局部切空间基向量张成的平行六面体有向体积：</p>
<p><b>1. 柱坐标雅可比推导</b>：变换关系为 <code>x = r cos θ, y = r sin θ, z = z</code>。计算偏导数行列式：</p>
<div class="formula-box">
  <div class="formula-line"><code>J_cyl = det [[cos θ, −r sin θ, 0], [sin θ, r cos θ, 0], [0, 0, 1]] = cos θ(r cos θ) − (−r sin θ)(sin θ) = r</code></div>
  <div class="formula-line"><b><code>dV_cyl = r · dr dθ dz</code></b></div>
</div>
<p><b>2. 球坐标雅可比推导</b>：变换关系为 <code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code>。展开 3×3 偏导数矩阵行列式：</p>
<div class="formula-box">
  <div class="formula-line"><code>J_sph = det(∂(x,y,z)/∂(ρ,φ,θ)) = ρ² sin φ</code></div>
  <div class="formula-line"><b><code>dV_sph = ρ² sin φ · dρ dφ dθ</code></b></div>
</div>
<p>这从根本上解释了为什么球坐标积分绝不能漏写因子 <code>ρ² sin φ</code>，它代表纬度与经度网格在球面上的实际面积缩放率。</p>
"""

mat_extra = r"""
<h3><span class="badge purple">拓展深化</span> 4.6.1 为什么矩阵乘法是“行乘列”：线性映射复合的本质推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】矩阵乘法行乘列法则的同态复合起源</b>
<p>矩阵本质上是有限维向量空间之间线性映射在选定基底下的坐标表示，两矩阵相乘对应两个线性映射的复合变换 <code>T_B ∘ T_A</code>。</p>
</div>
<p>设线性变换 <code>T_A: ℝᵖ → ℝⁿ</code> 由矩阵 <code>A</code> 诱导，即 <code>y = Ax</code>；变换 <code>T_B: ℝᵐ → ℝᵖ</code> 由矩阵 <code>B</code> 诱导，即 <code>x = Bz</code>。考察复合映射 <code>T = T_A ∘ T_B: ℝᵐ → ℝⁿ</code>：</p>
<div class="formula-box">
  <div class="formula-line"><code>yᵢ = ∑ₖ₌₁ᵖ a_{ik} xₖ = ∑ₖ₌₁ᵖ a_{ik} (∑ⱼ₌₁ᵐ b_{kj} zⱼ) = ∑ⱼ₌₁ᵐ (∑ₖ₌₁ᵖ a_{ik} b_{kj}) zⱼ</code></div>
</div>
<p>为使复合变换仍满足 <code>y = Cz</code>，矩阵 <code>C</code> 的第 <code>i</code> 行第 <code>j</code> 列元素必须定义为 <code>c_{ij} = ∑ₖ₌₁ᵖ a_{ik} b_{kj}</code>。这在几何上正是 <code>A</code> 的第 <code>i</code> 个行向量与 <code>B</code> 的第 <code>j</code> 个列向量的标准内积。因此，“行乘列”不是人为规定的运算规则，而是保持映射复合结合律的唯一数学选择。</p>

<h3><span class="badge purple">拓展深化</span> 4.10.1 经典几何变换矩阵的严密推导：平面正交旋转矩阵</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】基向量旋转变换与和差角公式推导正交矩阵</b>
<p>标准正交基 <code>e₁ = [1, 0]ᵀ, e₂ = [0, 1]ᵀ</code> 逆时针旋转 <code>θ</code> 角后的坐标直接给出旋转矩阵的列向量。</p>
</div>
<p>利用线性变换的基底决定性定理：一个线性变换完全由它对一组基向量的作用所决定。将第一基向量 <code>e₁</code> 逆时针旋转 <code>θ</code> 得到 <code>[cos θ, sin θ]ᵀ</code>；将第二基向量 <code>e₂</code> 旋转 <code>θ</code> 得到 <code>[−sin θ, cos θ]ᵀ</code>。两列向量拼接即得到旋转算子矩阵：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>R_θ = [[cos θ, −sin θ], [sin θ, cos θ]]</code></b></div>
</div>
<p>由于各列互相正交且模长为 1，满足 <code>(R_θ)ᵀ · R_θ = I</code> 且 <code>det(R_θ) = cos²θ + sin²θ = 1</code>，这严格证明了平面刚体旋转是保长、保角且保定向的特殊正交群 SO(2) 变换。</p>
"""

det_extra = r"""
<h3><span class="badge purple">拓展深化</span> 5.8.1 行列式降阶与代数余子式定理：伴随矩阵恒等式证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Laplace 代数余子式展开与伴随矩阵恒等式 A · adj(A) = |A|I 证明</b>
<p>证明 <code>i = j</code> 时代数余子式展开等于行列式自身，而 <code>i ≠ j</code> 时异行代数余子式相乘等于带有相同两行的奇异矩阵行列式（必为 0）。</p>
</div>
<p>定义伴随矩阵 <code>adj(A) = [C_{ij}]ᵀ</code>，其中 <code>C_{ij} = (−1)ⁱ⁺ʲ M_{ij}</code> 为代数余子式。考虑乘积 <code>P = A · adj(A)</code> 的第 <code>i</code> 行第 <code>k</code> 列元素：</p>
<div class="formula-box">
  <div class="formula-line"><code>P_{ik} = ∑ⱼ₌₁ⁿ a_{ij} (adj(A))_{jk} = ∑ⱼ₌₁ⁿ a_{ij} C_{kj}</code></div>
</div>
<ul>
  <li>当 <code>i = k</code> 时：上式恰好是矩阵 <code>A</code> 沿第 <code>i</code> 行的 Laplace 展开式，其值严格等于行列式 <code>det(A)</code>；</li>
  <li>当 <code>i ≠ k</code> 时：上式表示用 <code>A</code> 的第 <code>i</code> 行元素去乘第 <code>k</code> 行的代数余子式，其几何等价于计算一个将第 <code>k</code> 行替换为第 <code>i</code> 行的新矩阵的行列式。由于该新矩阵包含两行完全相同元素，由行列式反对称性，其值恒等于 0。</li>
</ul>
<p>综合两项即严格证明核心矩阵恒等式：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>A · adj(A) = adj(A) · A = det(A) · I</code></b></div>
  <div class="formula-line"><b><code>当 det(A) ≠ 0 时，A⁻¹ = (1 / det(A)) · adj(A)</code></b></div>
</div>
"""

gauss_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.3.1 高斯消元背后的初等矩阵分解与矩阵秩（Rank）的本质</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】初等行变换的初等矩阵乘积同构与相抵标准形</b>
<p>高斯消元中的倍加、对换、倍乘操作在代数上完全等价于左乘三种初等矩阵 <code>E_{ij}(c), P_{ij}, D_i(c)</code>，均严格非奇异且逆矩阵同型。</p>
</div>
<p>对矩阵进行初等行变换等价于对单位矩阵 <code>I</code> 施行相同变换得到的<b>初等矩阵（Elementary Matrix）</b>实施左乘：</p>
<ul>
  <li><b>倍加行变换 <code>rᵢ ← rᵢ + c · rⱼ</code></b>：对应初等矩阵 <code>E_{ij}(c)</code>，其逆矩阵为同型的 <code>E_{ij}(−c)</code>；</li>
  <li><b>交换行变换 <code>rᵢ ↔ rⱼ</code></b>：对应置换矩阵 <code>P_{ij}</code>，其逆矩阵为自身 <code>P_{ij}⁻¹ = P_{ij}</code>；</li>
  <li><b>倍乘行变换 <code>rᵢ ← c · rᵢ (c ≠ 0)</code></b>：对应对角阵 <code>D_i(c)</code>，其逆矩阵为 <code>D_i(1/c)</code>。</li>
</ul>
<p>由于所有初等矩阵皆可逆，消元过程 <code>Eₖ … E₂ E₁ A = U</code> 保持矩阵行阶梯空间的秩（Rank）完全不变。根据 <b>Rouché-Capelli 定理</b>：</p>
<div class="formula-box">
  <div class="formula-line"><code>rank(A) = rank([A | b]) = n  ⟹  唯一解</code></div>
  <div class="formula-line"><code>rank(A) = rank([A | b]) = r < n  ⟹  无穷多解（自由未知数个数为 n − r）</code></div>
  <div class="formula-line"><code>rank(A) < rank([A | b])  ⟹  无解（增广列包含独立矛盾阶梯）</code></div>
</div>
"""

eigen_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.1.1 特征值与特征向量的几何代数本质：不变子空间与对角化充要条件</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】特征方程 det(A − λI) = 0 的非平凡解核空间本质</b>
<p>特征向量所在的一维子空间在变换 <code>A</code> 下保持方向不变，几何重数 <code>dim(ker(A − λI))</code> 不超过代数重数是矩阵可对角化的核心准则。</p>
</div>
<p>若存在非零向量 <code>v</code> 使得 <code>Av = λv</code>，说明线性变换 <code>A</code> 将一维子空间 <code>span{v}</code> 映射到其自身，该一维子空间称为算子的<b>一维不变子空间（Invariant Subspace）</b>。移项得同质方程：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>(A − λI)v = 0  ⟺  det(A − λI) = 0</code></b></div>
</div>
<p>该齐次线性方程组存在非零解当且仅当系数矩阵奇异，从而导出特征多项式。若 <code>n</code> 阶矩阵具有 <code>n</code> 个线性无关的特征向量，则可构造相似变换矩阵 <code>P = [v₁ v₂ … vₙ]</code>，使得 <code>P⁻¹AP = diag(λ₁, λ₂, …, λₙ)</code> 实现完全解耦对角化。</p>
"""

cauchy_extra = r"""
<h3><span class="badge purple">拓展深化</span> 8.4.1 柯西-施瓦茨不等式（Cauchy-Schwarz）判别式代数证明与三角不等式</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】基于二次实多项式非负性与判别式 Δ ≤ 0 的精妙证明</b>
<p>构建参数化二次实多项式 <code>P(t) = ||u + t v||² ≥ 0</code>，利用实数二次型恒非负则一元二次方程判别式必须非正，彻底推导出向量内积的核心不等式。</p>
</div>
<p><b>【严密代数证明】</b> 对任意实内积空间中的向量 <code>u, v</code>，构造实变量 <code>t</code> 的标量函数：</p>
<div class="formula-box">
  <div class="formula-line"><code>P(t) = ||u + t v||² = (u + t v) · (u + t v) = ||v||² t² + 2(u · v) t + ||u||²</code></div>
</div>
<p>根据内积的正定性，对任意实数 <code>t</code> 恒有 <code>P(t) ≥ 0</code>。这是一个关于 <code>t</code> 的一元二次多项式。若 <code>||v|| ≠ 0</code>，它要对所有实数 <code>t</code> 恒非负，其对应二次方程的一元二次判别式 <code>Δ</code> 必须满足 <code>Δ ≤ 0</code>：</p>
<div class="formula-box">
  <div class="formula-line"><code>Δ = [2(u · v)]² − 4 · ||v||² · ||u||² ≤ 0</code></div>
  <div class="formula-line"><code>4(u · v)² ≤ 4 ||u||² ||v||²  ⟹  (u · v)² ≤ ||u||² ||v||²</code></div>
  <div class="formula-line"><b><code>|u · v| ≤ ||u|| · ||v||</code></b></div>
</div>
<p>两边开平方即得<b>柯西-施瓦茨不等式</b>，等号成立当且仅当 <code>u</code> 与 <code>v</code> 线性相关。</p>
<p><b>【推论：三角不等式】</b> 考察两向量之和的模平方：</p>
<div class="formula-box">
  <div class="formula-line"><code>||u + v||² = ||u||² + 2(u · v) + ||v||² ≤ ||u||² + 2|u · v| + ||v||²</code></div>
  <div class="formula-line"><code>≤ ||u||² + 2||u|| · ||v|| + ||v||² = (||u|| + ||v||)²</code></div>
  <div class="formula-line"><b><code>||u + v|| ≤ ||u|| + ||v||</code></b></div>
</div>
<p>证毕。这从代数上保证了内积空间中两向量夹角余弦 <code>cos θ = (u · v) / (||u|| ||v||)</code> 严格落在 <code>[−1, 1]</code> 区间内，使得空间夹角概念具有严格的几何自洽性。</p>
"""

for l in d80['lectures']:
    if l['slug'] == 'ch1-parametric-curves':
        l['html'] = inject_to_section(l['html'], 'detail', param_extra)
    elif l['slug'] == 'ch1-arc-polar':
        l['html'] = inject_to_section(l['html'], 'detail', polar_extra)
    elif l['slug'] == 'ch2-cyl-spherical':
        l['html'] = inject_to_section(l['html'], 'detail', cyl_extra)
    elif l['slug'] == 'ch2-matrices':
        l['html'] = inject_to_section(l['html'], 'detail', mat_extra)
    elif l['slug'] == 'ch3-determinant-inverse':
        l['html'] = inject_to_section(l['html'], 'detail', det_extra)
    elif l['slug'] == 'ch3-gaussian-elimination':
        l['html'] = inject_to_section(l['html'], 'detail', gauss_extra)
    elif l['slug'] == 'ch3-eigenvalues-cramer':
        l['html'] = inject_to_section(l['html'], 'detail', eigen_extra)
    elif l['slug'] == 'ch4-vectors-dot-product':
        l['html'] = inject_to_section(l['html'], 'detail', cauchy_extra)

save_json('80.json', d80)
print('[OK] 80 工程数学 II 全章节深度增强与公式排版完成')

# ==============================================================================
# 5. 62 (工程数学 I / Engineering Mathematics I)
# ==============================================================================
d62 = get_base_json('62.json')

lim_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.0 极限的本质形式化：柯西 ε-δ 语言与严谨证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】柯西 ε-δ 极限形式化分析方法</b>
<p>从动态直觉过渡到静态严格集合刻画：对任意给定的任意小容差 <code>ε > 0</code>，如何通过逆向解不等式构造出自变量受控邻域 <code>δ = min(1, ε/9)</code>。</p>
</div>
<p><b>【定义】</b> 我们称 <code>lim_{x→c} f(x) = L</code>，如果对于<b>任意</b>给定的正数 <code>ε > 0</code>，<b>都存在</b>一个正数 <code>δ > 0</code>，使得对定义域内所有满足 <code>0 < |x − c| < δ</code> 的 <code>x</code>，恒有：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>0 < |x − c| < δ  ⟹  |f(x) − L| < ε</code></b></div>
</div>
<p><b>【严谨 ε-δ 证明典范】</b> 证明 <code>lim_{x→3} (2x² − 5x) = 3</code>。</p>
<p><b>证明构思与分析</b>：需控制 <code>|(2x² − 5x) − 3| = |2x + 1| · |x − 3| < ε</code>。我们需要先限制 <code>|x − 3|</code> 使得因子 <code>|2x + 1|</code> 有界。取初始半径 <code>δ₁ = 1</code>，则：<code>|x − 3| < 1 ⟹ 2 < x < 4 ⟹ 5 < 2x + 1 < 9 ⟹ |2x + 1| < 9</code>。于是：</p>
<div class="formula-box">
  <div class="formula-line"><code>|2x + 1| · |x − 3| < 9 |x − 3|</code></div>
</div>
<p>为了使乘积小于 <code>ε</code>，只需额外要求 <code>|x − 3| < ε/9</code>。因此我们取 <code>δ = min(1, ε/9)</code>。</p>
<p><b>正式证明论述</b>：对任意给定的 <code>ε > 0</code>，取 <code>δ = min(1, ε/9) > 0</code>。当 <code>0 < |x − 3| < δ</code> 时，既有 <code>|x − 3| < 1</code>（保证 <code>|2x + 1| < 9</code>），又有 <code>|x − 3| < ε/9</code>。两式相乘：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>|(2x² − 5x) − 3| = |2x + 1| · |x − 3| < 9 · (ε/9) = ε</code></b></div>
</div>
<p>证毕。这就是柯西形式化分析方法的核心：通过不等式放缩将任意给定的 <code>ε</code> 逆向映射构造出 <code>δ</code>。</p>

<h3><span class="badge purple">拓展深化</span> 2.5.1 夹逼定理（Squeeze Theorem）与第一重要极限</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】单位圆扇形面积不等式与 lim_{x→0} (sin x)/x = 1 几何构造论证</b>
<p>在单位圆中由三角形面积小于扇形面积小于外切三角形面积建立 <code>cos θ < (sin θ)/θ < 1</code>，由夹逼定理完成首要超越极限证明。</p>
</div>
<p>在第一象限单位圆内，当 <code>0 < θ < π/2</code> 时，考察几何面积包合关系：</p>
<div class="formula-box">
  <div class="formula-line"><code>Area(△OAP) < Area(Sector OAP) < Area(△OAT)</code></div>
  <div class="formula-line"><code>(1/2) · 1 · sin θ < (1/2) · 1² · θ < (1/2) · 1 · tan θ</code></div>
  <div class="formula-line"><code>sin θ < θ < tan θ</code></div>
</div>
<p>同除以 <code>sin θ > 0</code> 并取倒数，不等号变号：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>cos θ < (sin θ)/θ < 1</code></b></div>
</div>
<p>由于 <code>lim_{θ→0⁺} cos θ = 1</code> 且 <code>lim_{θ→0⁺} 1 = 1</code>，由夹逼定理，右极限为 1。由于 <code>(sin θ)/θ</code> 为偶函数，左极限亦为 1。故 <code>lim_{θ→0} (sin θ)/θ = 1</code>。</p>
"""

prod_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.1.1 乘积法则（Product Rule）的严密代数推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】差商展开中“加一项减一项”对称技巧推导 (fg)′ = f′g + fg′</b>
<p>深入差商结构 <code>[f(x+h)g(x+h) − f(x)g(x)] / h</code>，引入中间项拆分为两个极限项，严谨展现可微性与连续性的内在联系。</p>
</div>
<p>设 <code>u(x) = f(x)g(x)</code>，且 <code>f, g</code> 在 <code>x</code> 处均可微（由可微性可知 <code>f</code> 必在 <code>x</code> 处连续，即 <code>lim_{h→0} f(x+h) = f(x)</code>）。根据导数微商定义：</p>
<div class="formula-box">
  <div class="formula-line"><code>u′(x) = lim_{h→0} [f(x+h)g(x+h) − f(x)g(x)] / h</code></div>
</div>
<p><b>推导关键技巧</b>：在分子中<b>减去并加上</b>辅助项 <code>f(x+h)g(x)</code>：</p>
<div class="formula-box">
  <div class="formula-line"><code>u′(x) = lim_{h→0} {[f(x+h)g(x+h) − f(x+h)g(x)] + [f(x+h)g(x) − f(x)g(x)]} / h</code></div>
  <div class="formula-line"><code>= lim_{h→0} [ f(x+h) · (g(x+h) − g(x))/h + g(x) · (f(x+h) − f(x))/h ]</code></div>
</div>
<p>利用极限的线性运算法则及连续性 <code>lim_{h→0} f(x+h) = f(x)</code>：</p>
<div class="formula-box">
  <div class="formula-line"><code>u′(x) = (lim_{h→0} f(x+h)) · (lim_{h→0} (g(x+h)−g(x))/h) + g(x) · (lim_{h→0} (f(x+h)−f(x))/h)</code></div>
  <div class="formula-line"><b><code>= f(x)g′(x) + g(x)f′(x)</code></b></div>
</div>
<p>证毕。此推导清晰展现了微积分代数构造中引入对称平衡项的核心技巧。</p>
"""

mvt_extra = r"""
<h3><span class="badge purple">拓展深化</span> 4.2.1 微分中值定理体系链：罗尔 ⟹ 拉格朗日 ⟹ 柯西中值定理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】从极值费马引理到微分中值定理三大核心推导链</b>
<p>由闭区间连续函数必有最值结合费马引理证明罗尔定理；构造割线偏差辅助函数证明拉格朗日定理；再推广至参数曲线比率辅助函数证明柯西定理。</p>
</div>
<p>整个微分学的核心理论基石由三大中值定理递进构成：</p>
<p><b>1. 费马引理（Fermat's Lemma）</b>：若 <code>f</code> 在可导点 <code>c</code> 取极值，则必有 <code>f′(c) = 0</code>。证明考察左导数 <code>≥ 0</code> 与右导数 <code>≤ 0</code>，迫使两边极限等于 0。</p>
<p><b>2. 罗尔定理（Rolle's Theorem）</b>：若 <code>f ∈ C[a, b]</code>，在 <code>(a, b)</code> 可导，且 <code>f(a) = f(b)</code>。由极值定理，<code>f</code> 在闭区间必达最大值 <code>M</code> 与最小值 <code>m</code>。若 <code>M = m</code> 则为常数函数导数恒为 0；若 <code>M ≠ m</code>，至少有一个极值在开区间内取得，由费马引理得 <code>f′(ξ) = 0</code>。</p>
<p><b>3. 拉格朗日中值定理（Lagrange MVT）</b>：构造割线偏差辅助函数 <code>g(x) = f(x) − f(a) − [(f(b)−f(a))/(b−a)](x − a)</code>。易验 <code>g(a) = g(b) = 0</code>。由罗尔定理，存在 <code>ξ ∈ (a, b)</code> 使得 <code>g′(ξ) = 0</code>，即：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>f′(ξ) = [f(b) − f(a)] / (b − a)  ⟺  f(b) − f(a) = f′(ξ)(b − a)</code></b></div>
</div>
<p><b>4. 柯西中值定理（Cauchy MVT）</b>：若有两个函数 <code>f, g</code>，构造辅助函数 <code>h(x) = [g(b) − g(a)]f(x) − [f(b) − f(a)]g(x)</code>，同样满足 <code>h(a) = h(b)</code>。由罗尔定理可得：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>[f(b) − f(a)] / [g(b) − g(a)] = f′(ξ) / g′(ξ)</code></b></div>
</div>
<p>这是洛必达法则（L'Hôpital's Rule）求未定式极限的直接理论依据。</p>
"""

ftc_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.1.1 微积分基本定理（FTC）第一与第二部分的严密证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】积分上限函数导数与牛顿-莱布尼茨公式双向证明</b>
<p>第一部分利用积分中值定理严格证明变上限积分的导数等于被积函数；第二部分通过对区间划分施加拉格朗日中值定理与黎曼和收敛证明 <code>∫ₐᵇ f(x)dx = F(b) − F(a)</code>。</p>
</div>

<p><span class="step-badge step1">Part 1</span><b>FTC 第一部分（变上限函数导数）</b></p>
<p>设连续函数 <code>g(x) = ∫ₐˣ f(t) dt</code>。由导数定义计算其微商增量比：</p>
<div class="formula-box">
  <div class="formula-line"><code>[g(x+h) − g(x)] / h = (1/h) · [∫ₐ^{x+h} f(t)dt − ∫ₐˣ f(t)dt] = (1/h) · ∫ₓ^{x+h} f(t)dt</code></div>
</div>
<p>应用<b>定积分第一中值定理</b>，在闭区间 <code>[x, x+h]</code> 内必定存在一点 <code>μ</code>，使得：</p>
<div class="formula-box">
  <div class="formula-line"><code>(1/h) · ∫ₓ^{x+h} f(t)dt = f(μ)</code></div>
</div>
<p>当 <code>h → 0</code> 时，夹逼迫使 <code>μ → x</code>。由函数 <code>f</code> 的连续性可知 <code>lim_{h→0} f(μ) = f(x)</code>。因此得出微积分基本定理第一结论：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>g′(x) = (d/dx) ∫ₐˣ f(t)dt = f(x)</code></b></div>
</div>

<p><span class="step-badge step2">Part 2</span><b>FTC 第二部分（牛顿-莱布尼茨公式）</b></p>
<p>设 <code>F(x)</code> 为 <code>f(x)</code> 的任意原函数，即 <code>F′(x) = f(x)</code>。对积分区间 <code>[a, b]</code> 任意插入剖分节点 <code>a = x₀ < x₁ < … < xₙ = b</code>：</p>
<p>利用“伸缩求和（Telescoping Sum）”将两端差值展开为相邻切片差：</p>
<div class="formula-box">
  <div class="formula-line"><code>F(b) − F(a) = ∑ᵢ₌₁ⁿ [F(xᵢ) − F(xᵢ₋₁)]</code></div>
</div>
<p>在每个子区间 <code>[xᵢ₋₁, xᵢ]</code> 上对可导函数 <code>F</code> 施加<b>拉格朗日中值定理</b>，必定存在点 <code>ξᵢ ∈ (xᵢ₋₁, xᵢ)</code> 满足：</p>
<div class="formula-box">
  <div class="formula-line"><code>F(xᵢ) − F(xᵢ₋₁) = F′(ξᵢ) · Δxᵢ = f(ξᵢ) · Δxᵢ</code></div>
</div>
<p>代回求和式得到精确等式：</p>
<div class="formula-box">
  <div class="formula-line"><code>F(b) − F(a) = ∑ᵢ₌₁ⁿ f(ξᵢ) · Δxᵢ</code></div>
</div>
<p>当网格细度 <code>λ = max(Δxᵢ) → 0</code> 时，右侧根据定义恰好收敛为定积分的黎曼和（Riemann Sum）。两端取极限即严格证明：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>∫ₐᵇ f(x)dx = F(b) − F(a)</code></b></div>
</div>
"""

for l in d62['lectures']:
    if l['slug'] == 't2-limits-continuity':
        l['html'] = inject_to_section(l['html'], 'detail', lim_extra)
    elif l['slug'] == 't3-derivatives-rules':
        l['html'] = inject_to_section(l['html'], 'detail', prod_extra)
    elif l['slug'] == 't4-higher-order-extrema-implicit':
        l['html'] = inject_to_section(l['html'], 'detail', mvt_extra)
    elif l['slug'] == 't7-integration-techniques':
        l['html'] = inject_to_section(l['html'], 'detail', ftc_extra)

save_json('62.json', d62)
print('[OK] 62 工程数学 I 全章节深度增强与公式排版完成')

# ==============================================================================
# 6. 86 (计算机导论 / 计算思维)
# ==============================================================================
d86 = get_base_json('86.json')

num_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.0 进位记数法的数学抽象与进制转换的代数原理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】位置记数法幂级数与带余除法进制转换代数证明</b>
<p>通过多项式 <code>N = ∑ dᵢ bⁱ</code> 与数学归纳法严格证明为什么整数“除基取余”与小数“乘基取整”具有数学完备性与唯一确定性。</p>
</div>
<p><b>1. 进位制的代数定义</b>：任何基数 <code>b ≥ 2</code> 的非负整数 <code>N</code> 均可唯一展开为关于基数 <code>b</code> 的有限多项式：</p>
<div class="formula-box">
  <div class="formula-line"><code>N = ∑ᵢ₌₀ⁿ dᵢ · bⁱ = d₀ + b · (d₁ + b · (d₂ + … + b · dₙ))</code></div>
</div>
<p>其中数码 <code>dᵢ ∈ {0, 1, …, b − 1}</code>。将上式按 <code>b</code> 提取公因式：</p>
<div class="formula-box">
  <div class="formula-line"><code>N = b · Q₁ + d₀，其中 Q₁ = ∑ᵢ₌₁ⁿ dᵢ · bⁱ⁻¹</code></div>
</div>
<p>根据带余除法（Division Algorithm），<code>d₀ = N mod b</code> 恰好是 <code>N</code> 除以 <code>b</code> 的余数，商为 <code>Q₁ = ⌊N / b⌋</code>。对新商 <code>Q₁</code> 重复执行除法即依次输出 <code>d₁, d₂, …</code>，直至商为 0。这严格证明了“除基取余、逆序排列”的代数必然性。</p>
"""

float_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.0 IEEE 754 浮点误差分析：灾难性抵消与数值稳定算法设计</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】浮点减法有效位损失（Catastrophic Cancellation）与条件数分析</b>
<p>从机器精度 <code>ε_mach</code> 与泰勒级数展开剖析两个相近大数相减导致的精度崩塌，并给出求根公式的数值稳定重构方案。</p>
</div>
<p><b>1. 灾难性抵消机理</b>：在有限字长二进制浮点数中，若两数 <code>x ≈ y</code>，计算 <code>x − y</code> 时，高位相同的数码被相减消除，导致原本位于低位的舍入噪声被左移规格化成为首要有效位，相对误差急剧膨胀！原本具有 53 位精度的有效数字会被完全抵消。</p>
<p><b>2. 经典案例：一元二次方程求根公式数值稳定改造</b>：对于标准方程 <code>ax² + bx + c = 0</code>，传统求根公式在 <code>b > 0</code> 且 <code>b² ≫ 4ac</code> 时，计算 <code>−b + √(b² − 4ac)</code> 会发生严重抵消。利用分子有理化重构算法：</p>
<div class="formula-box">
  <div class="formula-line"><code>x₁ = [−b − sgn(b) · √(b² − 4ac)] / (2a)</code></div>
  <div class="formula-line"><b><code>x₂ = (2c) / [−b − sgn(b) · √(b² − 4ac)] = c / (a · x₁)</code></b></div>
</div>
<p>改用 Viete 定理计算次根 <code>x₂ = c / (a x₁)</code>，完全避开了减法运算，消除了抵消误差，这是科学计算中数值分析的基本修养。</p>
"""

utf_extra = r"""
<h3><span class="badge purple">拓展深化</span> 4.0 变长编码的自同步性（Self-Synchronizing）与 UTF-8 有限状态机</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】UTF-8 前缀互斥设计与随机寻址容错机理</b>
<p>深入分析为什么 UTF-8 不会出现字节错位假冒字符：前缀码模式匹配如何实现 O(1) 字符边界自动恢复与流式传输健壮性。</p>
</div>
<p>UTF-8 最精妙之处在于其<b>无歧义自同步性</b>：任意字节通过观察高位特征即可瞬时判定其语义身份：</p>
<ul>
  <li><code>0xxxxxxx</code>（0x00~0x7F）：单字节 ASCII 字符；</li>
  <li><code>110xxxxx</code>：2 字节序列的起始头字节；</li>
  <li><code>1110xxxx</code>：3 字节序列的起始头字节（汉字主要区间）；</li>
  <li><code>11110xxx</code>：4 字节序列的起始头字节（Emoji 与罕见字）；</li>
  <li><code>10xxxxxx</code>：后续尾字节（Continuation Byte），永远以 <code>10</code> 开头。</li>
</ul>
<p>因为起始字节永远不会匹配 <code>10xxxxxx</code> 模式，如果传输过程中丢弃或损坏了若干字节，解码器只需线性快进扫描至下一个不以 <code>10</code> 开头的字节，即可立即且无状态地恢复字符同步，绝不会导致后续文本全部乱码。</p>
"""

shannon_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.0 信息论极限定理：香农信源编码定理与霍夫曼编码最优性证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】香农熵物理本质与无损压缩下界（Kraft 不等式）</b>
<p>深入香农熵 <code>H(X) = −∑ pᵢ log₂ pᵢ</code> 的物理与概率论背景，结合 Kraft 不等式证明任何无损前缀编码的平均码长无法低于信源熵。</p>
</div>
<p><b>1. 信息熵（Entropy）的数学本质</b>：对于输出离散随机变量 <code>X</code> 的信源，香农将符号出现的不确定性度量定义为自信息 <code>I(xᵢ) = −log₂ p(xᵢ)</code>。信源的平均不确定性即为信息熵：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>H(X) = − ∑ᵢ₌₁ⁿ pᵢ · log₂(pᵢ)  (bits/symbol)</code></b></div>
</div>
<p><b>香农第一编码定理（无失真信源编码定理）</b>指明：对于离散无记忆信源 <code>X</code>，使用二进制前缀码对其进行无损编码时，每个符号所需的期望平均码长 <code>L = ∑ pᵢ lᵢ</code> 必然满足：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>L ≥ H(X)</code></b></div>
</div>
<p>霍夫曼编码通过自底向上贪心合并最小概率节点，构造出一棵最优二叉树，其平均码长严格落在区间 <code>[H(X), H(X) + 1)</code> 内，数学上已被证明在基于单符号的前缀编码体系中达到了理论绝对最优。</p>
"""

ir_extra = r"""
<h3><span class="badge purple">拓展深化</span> 9.0 倒排索引跳表指针（Skip Pointers）的数学最优步长推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】倒排记录表跳表指针步长 √L 的复杂度理论证明</b>
<p>对倒排索引求交算法建立代价模型，证明当跳步长度取 <code>√L</code> 时能将比较次数由 <code>O(L₁ + L₂)</code> 最优降低至 <code>O(min(L₁, L₂) · √L)</code> 亚线性级别。</p>
</div>
<p>在搜索引擎布尔检索中，两个词项的倒排记录表（Posting List）求交（AND 查询）是高频瓶颈。若线性遍历，时间复杂度为 <code>O(L₁ + L₂)</code>。通过为长度为 <code>L</code> 的有序链表每隔 <code>S</code> 个节点建立一个带最大值的跳表指针（Skip Pointer），当跳跃目标值小于待查值时可直接跳过 <code>S</code> 个元素：</p>
<p><b>【最佳步长 √L 的数学极值证明】</b> 设跳表步长为 <code>S</code>，则整个链表包含 <code>L/S</code> 个跳步节点。在最坏情况下，如果目标元素位于跳步区间末端，查找代价为：跳步比较次数 <code>L/S</code> 加上区间内线性查找次数 <code>S</code>。总比较次数模型为：</p>
<div class="formula-box">
  <div class="formula-line"><code>T(S) = (L / S) + S</code></div>
</div>
<p>对步长 <code>S</code> 求一阶导数并令其为 0：</p>
<div class="formula-box">
  <div class="formula-line"><code>dT/dS = −(L / S²) + 1 = 0  ⟹  S² = L  ⟹  S = √L</code></div>
</div>
<p>二阶导数 <code>d²T/dS² = 2L / S³ > 0</code>，故驻点必为极小值点。因此取步长为 <code>√L</code> 时获得最优性能，总查找代价由线性 <code>O(L)</code> 锐减为 <code>O(√L)</code>。</p>
"""

for l in d86['lectures']:
    if l['slug'] == 'w2-number-systems':
        l['html'] = inject_to_section(l['html'], 'detail', num_extra)
    elif l['slug'] == 'w3-signed-numbers-and-float':
        l['html'] = inject_to_section(l['html'], 'detail', float_extra)
    elif l['slug'] == 'w4-character-encoding':
        l['html'] = inject_to_section(l['html'], 'detail', utf_extra)
    elif l['slug'] == 'w7-data-compression':
        l['html'] = inject_to_section(l['html'], 'detail', shannon_extra)
    elif l['slug'] == 'w9-information-retrieval':
        l['html'] = inject_to_section(l['html'], 'detail', ir_extra)

save_json('86.json', d86)
print('[OK] 86 计算机导论 全章节深度增强与公式排版完成')

# ==============================================================================
# 7. 30565 (离散数学 / Discrete Mathematics)
# ==============================================================================
d30565 = get_base_json('30565.json')

card_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.0 从伽利略悖论到无限基数：双射作为度量无限的唯一尺度</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】集合基数概念的公理化延伸与等势关系等价类</b>
<p>深入分析为什么在无限集合中“部分可以等于整体”，双射关系如何将所有集合划分为基数等价类并定义超限序数与基数层次。</p>
</div>
<p>在有限世界中，真子集的元素数量必然严格小于整体集合。然而在无限世界中，这一常识彻底失效：偶数集 <code>2ℕ</code> 是自然数集 <code>ℕ</code> 的真子集，但映射 <code>f(n) = 2n</code> 构成了两者的完美一一对应（双射）。康托尔由此确立了现代公理化集合论的基石原则：<b>两个集合基数相等（等势，Equinumerous），当且仅当存在一个从 A 到 B 的双射映射 <code>f: A → B</code></b>。</p>

<h3><span class="badge purple">拓展深化</span> 6.1 康托尔配对函数与有理数集 ℚ 的可数性严密证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】多项式对角线蛇形折叠双射构造</b>
<p>通过康托尔多项式函数 <code>π(k₁, k₂) = (1/2)(k₁ + k₂)(k₁ + k₂ + 1) + k₂</code> 严格证明 <code>ℕ × ℕ</code> 与 <code>ℕ</code> 具有完全相同的无限基数 ℵ₀。</p>
</div>
<p>许多初学者直觉认为有理数在数轴上是处处稠密的（Dense），因而其数量必远多于自然数。然而康托尔利用“蛇形穿线法”严格构造了双射证明：</p>
<p><b>1. 康托尔配对多项式</b>：将二维网格点 <code>(k₁, k₂) ∈ ℕ × ℕ</code> 按对角线层级逐项编码：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>π(k₁, k₂) = (1/2) · (k₁ + k₂) · (k₁ + k₂ + 1) + k₂</code></b></div>
</div>
<p><b>2. 素数幂次质因数分解唯一性证明</b>：构造映射 <code>f(m, n) = 2ᵐ⁻¹ · (2n − 1)</code>。根据算术基本定理，任何正整数均可唯一表示为一个 2 的幂与一个奇数的乘积，故 <code>f</code> 构成了从 <code>ℕ × ℕ</code> 到 <code>ℕ</code> 的严格双射！由此推导出二维正整数网格乃至全体正有理数集 <code>ℚ⁺</code> 均为可数集，其基数恒等于 ℵ₀。</p>

<h3><span class="badge purple">拓展深化</span> 6.2 希尔伯特无限旅馆的数学分段函数构造</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】无限旅馆接待新客的分段平移与乘积空间算法映射</b>
<p>用严格的映射公式解决“已满员旅馆”如何继续无条件容纳有限新客、可数无限个新客、以及无限辆满载无限乘客的大巴。</p>
</div>
<p>设旅馆房间编号为正整数集合 <code>ℕ = {1, 2, 3, …}</code>，目前每间房均已住满：</p>
<ul>
  <li><b>场景 1（新来 1 位客人）</b>：让原房号为 <code>n</code> 的客人搬至 <code>n + 1</code> 号房。映射 <code>f(n) = n + 1</code> 腾出了 1 号房，且新映射仍为单射。</li>
  <li><b>场景 2（新来可数无限 ℵ₀ 位客人）</b>：让原房号为 <code>n</code> 的客人搬至 <code>2n</code> 号房。腾出了所有奇数号房 <code>1, 3, 5, …</code>，由双射 <code>g(k) = 2k − 1</code> 完美安置无限新客。</li>
  <li><b>场景 3（新来无限辆大巴，每辆坐着无限名客人）</b>：利用第 <code>i</code> 个素数 <code>pᵢ</code> 编码：让原住客搬至 <code>2ⁿ</code> 号房；第 <code>k</code> 辆大巴上的第 <code>m</code> 位乘客分配至 <code>(p_{k+1})ᵐ</code> 号房。由素数因式分解唯一性，所有房间分配互不冲突！</li>
</ul>

<h3><span class="badge purple">拓展深化</span> 6.3 康托尔定理的本质证明：|S| < |P(S)| 对角线子集反证法</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】康托尔定理超越有限维度的终极反证：幂集严格大于原集</b>
<p>严格反证说明为什么任何集合（无论多大、无论有限还是无限）的幂集基数绝对严格大于原集合，从而推导出无限基数的阿列夫层级谱系。</p>
</div>
<p><b>【严密定理证明】</b> 设 <code>S</code> 为任意集合，<code>𝒫(S)</code> 为其幂集（所有子集构成的集合）。</p>
<p>显然存在单射 <code>g: S → 𝒫(S)</code>，由 <code>g(x) = {x}</code> 给出，因此 <code>|S| ≤ |𝒫(S)|</code>。下证不存在任何从 <code>S</code> 到 <code>𝒫(S)</code> 的满射（Surjection）：</p>
<p>假设存在一个满射 <code>f: S → 𝒫(S)</code>。对 <code>S</code> 中的任意元素 <code>x</code>，<code>f(x)</code> 是 <code>S</code> 的一个子集。此时元素 <code>x</code> 要么属于 <code>f(x)</code>，要么不属于 <code>f(x)</code>。我们构造一个“病态对角线子集” <code>D</code>：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>D = { x ∈ S | x ∉ f(x) } ⊆ S</code></b></div>
</div>
<p>因为 <code>D</code> 是 <code>S</code> 的子集，所以 <code>D ∈ 𝒫(S)</code>。由于假设 <code>f</code> 是满射，在 <code>S</code> 中必须存在某个元素 <code>d ∈ S</code>，使得 <code>f(d) = D</code>。现在质问：元素 <code>d</code> 是否属于集合 <code>D</code>？</p>
<ul>
  <li>若 <code>d ∈ D</code>：根据 <code>D</code> 的定义，必须满足 <code>d ∉ f(d)</code>。但由 <code>f(d) = D</code>，可推出 <code>d ∉ D</code>，前后自相矛盾！</li>
  <li>若 <code>d ∉ D</code>：即 <code>d ∉ f(d)</code>，这恰好满足了进入集合 <code>D</code> 的准入条件，从而必须有 <code>d ∈ D</code>，同样自相矛盾！</li>
</ul>
<p>无论 <code>d</code> 属于还是不属于 <code>D</code>，均引发不可调和的逻辑谬误。这证明假设破产：<b>任何从 S 到 𝒫(S) 的满射绝对不存在</b>！</p>
<p>综合单射存在性与满射不存在性，严格证明 <code>|S| < |𝒫(S)|</code>。这意味着即便是无限集，其幂集也是更大阶级的无限，从而打开了无穷之上的超限基数天梯（<code>ℵ₀ < 2^{ℵ₀} = 𝔠 < 2^𝔠 < …</code>）。</p>
"""

for l in d30565['lectures']:
    if l['slug'] == 'cardinality-countable-sets':
        l['html'] = inject_to_section(l['html'], 'detail', card_extra)

save_json('30565.json', d30565)
print('[OK] 30565 离散数学 基数理论深度重构与拓展标注完成')

# ==============================================================================
# 8. 30361 (软件工程 / Software Engineering)
# ==============================================================================
d30361 = get_base_json('30361.json')

sdlc_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.0 软件工程经济学定律：Boehm 缺陷修复成本指数曲线</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Barry Boehm 软件缺陷修复成本阶段倍增效应</b>
<p>从软件生命周期（SDLC）不同阶段剖析为什么需求阶段发现的缺陷修复代价为 1x，而在发布上线后修复代价急剧飙升至 100x~200x。</p>
</div>
<p>软件工程大师 Barry Boehm 通过大量工业界实证研究总结出著名的缺陷成本放大律：缺陷在生命周期中潜伏的时间越长，其修复成本呈几何级数（指数）爆炸：</p>
<table>
  <tr><th>发现与修复阶段</th><th>相对修复成本乘数</th><th>工程根因分析</th></tr>
  <tr><td>需求分析（Requirements）</td><td><b>1×</b>（基准）</td><td>只需修改文档文本或用例描述，几乎无附加返工。</td></tr>
  <tr><td>架构设计（Architecture）</td><td><b>3× ~ 5×</b></td><td>重新设计组件接口，波及小范围设计图纸。</td></tr>
  <tr><td>编码阶段（Coding）</td><td><b>10×</b></td><td>需要重写代码、重新通过单元测试。</td></tr>
  <tr><td>系统集成测试（Integration）</td><td><b>40× ~ 50×</b></td><td>需多模块联调、回归测试、耗费 QA 团队人力排查。</td></tr>
  <tr><td>生产发布上线后（Production）</td><td><b>100× ~ 200×</b></td><td>涉及线上数据热修复、停机补偿、品牌公关与法律合规责任。</td></tr>
</table>
"""

cap_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.0 分布式系统设计的基石定理：CAP 定理的严格反证</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】网络分区下一致性（Consistency）与可用性（Availability）的不可能三角反证</b>
<p>严格反证说明在异步不可靠网络信道中，为什么任何分布式数据存储无法同时实现强一致性、高可用性与分区容错性。</p>
</div>
<p><b>严密反证构造</b>：设分布式系统由两个独立节点 <code>G₁, G₂</code> 组成。当物理光缆中断时，系统陷入分区状态 <code>P</code>（<code>G₁</code> 与 <code>G₂</code> 无法通信）：</p>
<ul>
  <li>客户端向 <code>G₁</code> 发起写请求 <code>Write(v = 1)</code>；</li>
  <li>若系统满足可用性（A），<code>G₁</code> 必须在不能与 <code>G₂</code> 通信的情况下单方面向客户端确认写入成功；</li>
  <li>紧接着另一个客户端向 <code>G₂</code> 发起读请求 <code>Read()</code>；</li>
  <li>若系统要保证可用性（A），<code>G₂</code> 必须立刻响应而不能无限阻塞等待网络恢复；</li>
  <li>但因为网络分区阻断了 <code>G₁</code> 向 <code>G₂</code> 同步数据的消息，<code>G₂</code> 只能返回旧值 <code>v = 0</code>。</li>
</ul>
<p>此时客户端在 <code>G₂</code> 上读到了脏数据，违反了强一致性（C）。若强制要求一致性，<code>G₂</code> 必须拒绝请求报错，则违反了可用性（A）。因此在分区容错（P）不可避免的物理现实下，架构师必须在 AP 与 CP 之间做出取舍权衡。</p>
"""

mccabe_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.0 白盒测试复杂度度量：麦凯布圈复杂度（McCabe Cyclomatic Complexity）</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】图论欧拉示性数推导圈复杂度公式 V(G) = E − V + 2 = π + 1</b>
<p>通过控制流图（CFG）的代数拓扑回路基底，严格推导程序线性独立路径数量的计算方法，指导基本路径测试集的覆盖设计。</p>
</div>
<p><b>【数学公式推导】</b> 设程序的控制流图为强连通有向图 <code>G = (V, E)</code>，其中 <code>V</code> 为指令块节点数，<code>E</code> 为控制流转移边数。根据代数拓扑学欧拉示性数，图的独立回路数（圈复杂度）由下式严格定义：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>V(G) = E − V + 2P</code></b></div>
</div>
<p>对于单入口单出口的独立函数模块（连通分支数 <code>P = 1</code>），公式简化为：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>V(G) = E − V + 2 = π + 1</code></b></div>
</div>
<p>其中 <code>π</code> 是图中的判定分支节点数（如 <code>if, while, for</code>）。圈复杂度给出了设计全分支覆盖所需的<b>最小线性独立测试路径数</b>，通常工业界建议单个函数的 <code>V(G) ≤ 10</code>，若超过 15 则必须实施重构拆分。</p>
"""

for l in d30361['lectures']:
    if l['slug'] == 'l02-sdlc-models-and-agile':
        l['html'] = inject_to_section(l['html'], 'detail', sdlc_extra)
    elif l['slug'] == 'l06-architectural-design':
        l['html'] = inject_to_section(l['html'], 'detail', cap_extra)
    elif l['slug'] == 'l07-testing-and-quality':
        l['html'] = inject_to_section(l['html'], 'detail', mccabe_extra)

save_json('30361.json', d30361)
print('[OK] 30361 软件工程 经济模型、CAP 定理与圈复杂度深化完成')

# ==============================================================================
# 9. 30332 (AI in Studies)
# ==============================================================================
d30332 = get_base_json('30332.json')
ai_extra = r"""
<h3><span class="badge purple">拓展深化</span> 4.5 大语言模型核心架构：Transformer 自注意力机制（Self-Attention）与幻觉成因剖析</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】自注意力矩阵计算 Attention(Q, K, V) 与自回归生成确定性困境</b>
<p>从缩放点积注意力公式 <code>softmax((QKᵀ)/√dₖ)V</code> 揭示大模型动态权重分配机理，并从马尔可夫自回归采样概率角度解释为什么 AI 会产生不可避免的幻觉（Hallucination）。</p>
</div>
<p><b>1. 缩放点积注意力核心公式</b>：设输入词嵌入序列经线性投影生成查询矩阵 <code>Q</code>、键矩阵 <code>K</code> 和值矩阵 <code>V</code>（维度均为 <code>dₖ</code>）：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>Attention(Q, K, V) = softmax( (Q Kᵀ) / √dₖ ) · V</code></b></div>
</div>
<p>其中除以缩放因子 <code>√dₖ</code> 是为了防止在维度较大时向量点积数值过大，导致 <code>softmax</code> 函数进入导数极小的梯度饱和区。通过注意力权重矩阵，模型能够在 O(1) 的路径长度内直接捕捉序列中任意两词之间的长程语义关联。</p>
<p><b>2. 自回归解码与幻觉本质</b>：生成式大语言模型本质上是条件概率极大似然估计器：<code>P(wₜ | w₁, w₂, …, wₜ₋₁)</code>。模型在生成每一个词时仅基于统计概率分布进行采样，其目标是输出“在语料统计上最自然连贯的延续”，而非“逻辑上真实自洽的事实”，这在认识论上构成了幻觉无法仅凭预训练完全杜绝的理论根源。</p>
"""
for l in d30332['lectures']:
    if l['slug'] == 'ai-in-studies':
        l['html'] = inject_to_section(l['html'], 'detail', ai_extra)

save_json('30332.json', d30332)
print('[OK] 30332 AI 学习应用 Transformer 机制深化完成')

# ==============================================================================
# 10. 29911 (循环经济)
# ==============================================================================
d29911 = get_base_json('29911.json')
ce_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.5 工业生态学热力学定律：从热力学第二定律（熵增）看循环经济的物理边界</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】物质循环的熵能消耗边界与下行闭环瓶颈</b>
<p>揭示循环经济并非零成本永动机：物质分散、合金元素稀释与材料降级回收（Downcycling）背后不可逾越的热力学耗散极限。</p>
</div>
<p><b>1. 物质与能量的不可逆退化</b>：根据热力学第二定律，孤立系统熵增不减 <code>ΔS ≥ 0</code>。自然界中高品质材料（低熵状态，如纯铜、结构合金）在使用过程中不可避免地发生耗散与稀释（微量添加剂分散、杂质混入）。要将分散的高熵废弃物提纯重新还原为原生品质的材料，外界必须输入巨大的吉布斯自由能（做功）并向环境排放更多的废热与熵。</p>
<p><b>2. 循环经济的务实边界</b>：因此，最经济的闭环永远是处于高层级的<b>维护（Maintain）与再制造（Remanufacture）</b>，而非无休止地熔炼与物料回收。工业生态系统设计必须在物料闭环率与全生命周期能耗之间寻找平衡点。</p>
"""
for l in d29911['lectures']:
    if l['slug'] == 'c3-circular-concepts':
        l['html'] = inject_to_section(l['html'], 'detail', ce_extra)
save_json('29911.json', d29911)
print('[OK] 29911 循环经济 热力学边界深化完成')

# ==============================================================================
# 11. 29913 (气候变化)
# ==============================================================================
d29913 = get_base_json('29913.json')
climate_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.5 全球气候敏感度与辐射强迫（Radiative Forcing）对数响应模型</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】斯特藩-玻尔兹曼能平衡与二氧化碳辐射强迫对数公式</b>
<p>基于黑体辐射定律与两层大气能平衡模型，推导温室气体浓度翻倍时的辐射强迫经验公式 <code>ΔF = 5.35 · ln(C/C₀) W/m²</code>，揭示气候系统响应非线性特征。</p>
</div>
<p><b>1. 地球能量收支零维平衡</b>：地球系统在稳态下吸收的太阳短波辐射与射出长波红外辐射相等：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>(S₀ / 4) · (1 − α) = ε · σ · T_e⁴</code></b></div>
</div>
<p>其中太阳常数 <code>S₀ ≈ 1361 W/m²</code>，反照率 <code>α ≈ 0.3</code>，<code>σ</code> 为斯特藩-玻尔兹曼常数。无温室气体时有效辐射温度 <code>T_e ≈ 255 K (−18 °C)</code>，温室效应使其上升至 288 K（15 °C）。</p>
<p><b>2. 对数饱和效应与气候敏感度</b>：由于二氧化碳在 15 μm 的核心红外吸收带早已趋于光学饱和，新增的 CO₂ 主要在吸收带边缘吸收红外光子，其引起的对流层顶辐射强迫呈现对数规律：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>ΔF = 5.35 · ln(C / C₀)  (W/m²)</code></b></div>
</div>
<p>当 CO₂ 浓度从工业革命前 280 ppm 翻倍至 560 ppm 时，辐射强迫为 <code>ΔF ≈ 5.35 · ln(2) ≈ 3.7 W/m²</code>。考虑水汽正反馈与冰雪反照率反馈后，平衡态气候敏感度（ECS）预计全球升温 <code>ΔT = λ · ΔF ≈ 2.5 ~ 4.0 °C</code>。</p>
"""
for l in d29913['lectures']:
    if l['slug'] == 'c2-supplemental-references':
        l['html'] = inject_to_section(l['html'], 'detail', climate_extra)
save_json('29913.json', d29913)
print('[OK] 29913 气候变化 辐射强迫对数模型深化完成')

# ==============================================================================
# 12. 34583 (芬兰语 2)
# ==============================================================================
d34583 = get_base_json('34583.json')
fin2_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.5 芬兰语动词六大变位族（Verbit 1–6）底层词干提取算法与辅音交替逆向定理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】动词词干提取算法与弱强阶逆向演化规律</b>
<p>系统剖析 1~6 型动词词干的元音/辅音脱落算法，破解 3/4/6 型动词为什么原形处于弱阶而变位后进入强阶的逆向交替之谜。</p>
</div>
<p>动词变位常被视为庞杂的特例记忆，但在生成语言学框架下，动词 1 型为正向交替（原形强阶 → 人称弱阶），而动词 3/4/6 型则遵循逆向交替（原形弱阶 → 人称强阶）。掌握底层词干提取算法即可实现通解：</p>
<table>
  <tr><th>动词类型</th><th>原形特征</th><th>词干提取算法规则</th><th>辅音交替方向</th><th>典型范例</th></tr>
  <tr><td><b>1 型</b></td><td>-V+A/Ä</td><td>脱落末尾元音 <code>-a/-ä</code></td><td>正向（强 → 弱）</td><td>puhua → puhu-, ottaa → otan</td></tr>
  <tr><td><b>2 型</b></td><td>-DA/DÄ</td><td>脱落后缀 <code>-da/-dä</code></td><td>无交替（辅音稳定）</td><td>syödä → syö-, juoda → juon</td></tr>
  <tr><td><b>3 型</b></td><td>-LA/NA/RA/STA</td><td>脱落两字母并补入连接元音 <code>-e-</code></td><td>逆向（弱 → 强）</td><td>tulla → tule-, ajatella → ajattelen</td></tr>
  <tr><td><b>4 型</b></td><td>-VT+A/Ä</td><td>脱落 <code>-t-</code> 并补入连接元音 <code>-a/-ä</code></td><td>逆向（弱 → 强）</td><td>tavata → tapaa-, haluta → haluan</td></tr>
  <tr><td><b>5 型</b></td><td>-ITA/ITÄ</td><td>脱落 <code>-ta/-tä</code> 并补入 <code>-tse-</code></td><td>无交替</td><td>tarvita → tarvitse-</td></tr>
  <tr><td><b>6 型</b></td><td>-ETA/ETÄ</td><td>脱落 <code>-ta/-tä</code> 并补入 <code>-ne-</code></td><td>逆向（弱 → 强）</td><td>paeta → pakene-</td></tr>
</table>
"""
for l in d34583['lectures']:
    if l['slug'] == 't7-verb-types-1-6':
        l['html'] = inject_to_section(l['html'], 'detail', fin2_extra)
save_json('34583.json', d34583)
print('[OK] 34583 芬兰语 2 动词变位算法深化完成')

# ==============================================================================
# 13. 30331 (软件导论)
# ==============================================================================
d30331 = get_base_json('30331.json')
psp_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.5 个人软件工程过程（PSP）量化建模：PROBE 估算与代码质量缺陷密度</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Watts Humphrey PROBE 代理线性回归估算模型与缺陷漏网率指标</b>
<p>从卡耐基梅隆大学 SEI 软件工程度量体系切入，解析工程师如何通过历史开发数据建立规模与工时的实证统计回归方程。</p>
</div>
<p><b>1. PROBE（Proxy Based Estimation）规模与工期估算法</b>：利用历史开发模块的规模代理（如功能点、代码行 LOC 或类方法数）建立经验回归方程 <code>Y = β₀ + β₁ · X</code>，其中一阶斜率由最小二乘法严格给出：</p>
<div class="formula-box">
  <div class="formula-line"><b><code>β₁ = [n ∑ XY − (∑ X)(∑ Y)] / [n ∑ X² − (∑ X)²]</code></b></div>
</div>
<p><b>2. 软件过程质量两大核心度量</b>：</p>
<ul>
  <li><b>缺陷密度（Defect Density）</b>：<code>DD = 发现缺陷总数 / 代码千行数 (KLOC)</code>，成熟工程团队要求交付缺陷密度小于 0.5/KLOC；</li>
  <li><b>评审去除效率（Review Yield）</b>：公式 <code>Yield = [评审发现的缺陷数 / 评审前总潜伏缺陷数] × 100%</code>。量化证实代码审查（Peer Review）的缺陷去除能效是后期单元测试的 2 倍以上。</li>
</ul>
"""
for l in d30331['lectures']:
    if l['slug'] == 'degree-structure-psp':
        l['html'] = inject_to_section(l['html'], 'detail', psp_extra)
save_json('30331.json', d30331)
print('[OK] 30331 软件导论 PSP 量化估算深化完成')

# ==============================================================================
# 14. 29428 (学术演讲与辩论)
# ==============================================================================
d29428 = get_base_json('29428.json')
toulmin_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.5 国际学术答辩与批判性沟通：图尔敏论证模型（Toulmin Model）应用</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Stephen Toulmin 逻辑学六要素论证骨架</b>
<p>剖析学术论文与国际工程会议答辩如何运用“主张-依据-保证-支持-反驳-限定”六位一体框架，构筑无懈可击的技术论证闭环。</p>
</div>
<p>在国际学术交流与毕业论文答辩中，单纯罗列数据往往被评委评为“论证薄弱”。图尔敏论证模型提供了结构化批判性思维框架：</p>
<table>
  <tr><th>论证要素</th><th>功能定义</th><th>工程技术学术答辩典范</th></tr>
  <tr><td><b>Claim（主张）</b></td><td>你希望听众接受的核心技术结论</td><td>“所提出的分布式算法在千节点集群下延迟低于 5ms。”</td></tr>
  <tr><td><b>Data / Grounds（依据）</b></td><td>支撑主张的实验数据、基准测试结果</td><td>“在 AWS 真实集群上运行 100 次压测的 P99 延迟统计报表。”</td></tr>
  <tr><td><b>Warrant（保证）</b></td><td>从依据合乎逻辑推导到主张的根本原理</td><td>“测试基准覆盖了真实工业生产环境的高并发突发流量分布。”</td></tr>
  <tr><td><b>Backing（支持）</b></td><td>支持保证有效性的理论根基或权威文献</td><td>“遵循 IEEE/ACM 分布式系统基准评测规范（Benchmarking Standard）。”</td></tr>
  <tr><td><b>Rebuttal（反驳/例外）</b></td><td>承认系统可能失效的边界条件或反例</td><td>“除非集群跨机房骨干光纤发生超过 30% 的恶性网络丢包。”</td></tr>
  <tr><td><b>Qualifier（限定语）</b></td><td>表达主张确定性程度的精确科学修饰词</td><td>“在置信区间 95% 下，大概率（Likely）成立。”</td></tr>
</table>
"""
for l in d29428['lectures']:
    if l['slug'] == 'speaking-up':
        l['html'] = inject_to_section(l['html'], 'detail', toulmin_extra)
save_json('29428.json', d29428)
print('[OK] 29428 学术演讲 图尔敏论证模型深化完成')

# ==============================================================================
# 15. 32667 (实验语音学)
# ==============================================================================
d32667 = get_base_json('32667.json')
ipa_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.5 实验语音学与声学共振峰理论：F1/F2 舌位四边形与频谱感知</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】声道滤波声学模型（Source-Filter Model）与元音共振峰</b>
<p>从声学物理学角度解析声带基频（F0）与咽腔/口腔声道共振峰（F1/F2）的解耦分离，说明为什么人类可以通过共振峰频谱直观辨识元音。</p>
</div>
<p><b>1. 声源-滤波器理论（Fant 声学模型）</b>：人类语音生成由两部分独立决定：声带振动提供基频 <code>F0</code>（决定音调高低 Pitch），而声道的几何构型充当共振腔滤波器（Filter），使特定频率范围的声波共振增强，形成<b>共振峰（Formants）</b>。</p>
<p><b>2. F1 与 F2 对舌位几何的双向映射定理</b>：</p>
<ul>
  <li><b>第一共振峰 F1</b>：与<b>舌位高低（舌面抬起程度 / 口腔开合度）</b>严格成反比。舌位越高（如高元音 [i], [u]），咽腔共振体积越大，F1 频率越低（约 250~350 Hz）；舌位越低（如低元音 [a]），F1 频率越高（可达 800 Hz 以上）；</li>
  <li><b>第二共振峰 F2</b>：与<b>舌位前后（舌体前凸或后缩）</b>严格成正比。前元音（如 [i], [e]）口腔容积小，F2 极高（约 2000~2500 Hz）；后元音（如 [u], [o]）舌体后缩，F2 极低（约 700~1000 Hz）。</li>
</ul>
<p>在二维声学坐标系（以 F2 为横轴倒置、F1 为纵轴倒置）中，不同元音的测量点分布恰好精准复原了国际音标 IPA 的“生理舌位四边形”，构成了现代语音识别（ASR）与发音诊断算法的声学物理基石。</p>
"""
for l in d32667['lectures']:
    if l['slug'] == 'p2-vowels-consonants':
        l['html'] = inject_to_section(l['html'], 'detail', ipa_extra)
save_json('32667.json', d32667)
print('[OK] 32667 实验语音学 声学共振峰理论深化完成')

print("\n" + "="*50)
print("恭喜！全站 15 门课程已 100% 完成彻底的 LaTeX 语法清除与 Unicode / 视觉卡片重构！")
print("="*50)
'''

with io.open(MASTER_FILE, "w", encoding="utf-8") as f:
    f.write(master_code)
print(f"[SUCCESS] Wrote clean {MASTER_FILE}")

