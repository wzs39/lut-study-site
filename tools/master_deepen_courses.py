# -*- coding: utf-8 -*-
"""全站核心学科讲义全章节深度增强、拓展标注与文不对题修复主程序

特性：
1. 从基准分支读取干净内容，保证幂等性与纯净注入
2. 所有进阶理论与推导小节均统一标注：
   - 标题级徽标：<h3><span class="badge purple">拓展深化</span> ...</h3>
   - 专属提示框：<div class="callout idea" data-ext="true"><b>【拓展深化】...</b><p>...</p></div>
   - 全局聚合联动：build.py 自动将全站所有的拓展提示框索引并汇总到 extend.html（知识拓展专页）
3. 彻底修复章节跳号、错序与文不对题
"""
import json, re, os, io, subprocess

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
# 1. 修复与深化 32632 (大学英语)
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

# 注入大学英语技术沟通认知修辞拓展
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
  <li><b>计算作为流水线与容器</b>：<code>Pipeline</code>（管道传输数据）、<code>Buffer / Queue</code>（队列排队）、<code>Thread / Process</code>（线程交织与进程生命）。动词使用时必须保持物理场的一致性，如数据“流经”（stream through）而非“走入”（walk into）。</li>
  <li><b>内存作为物理空间与生命周期</b>：<code>Memory Leak</code>（内存像液体容器破损般泄漏）、<code>Garbage Collection</code>（垃圾回收）、<code>Orphan Process</code>（孤儿进程）。</li>
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
# 2. 修复与深化 33295 (芬兰语 1)
# ==============================================================================
d33295 = get_base_json('33295.json')
for l in d33295['lectures']:
    if l['slug'] == 't10-genetiivi':
        l['title_zh'] = 'Tunti 10 · 属格与所有格'
        l['part'] = '第 4 章 属格、个人信息与复习'
        fin_extra = r"""
<h3><span class="badge purple">拓展深化</span> 10.5 乌拉尔语系黏着语音系学：辅音交替（Astevaihtelu）底层音步与开闭音节物理机制</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】芬兰语辅音强弱交替的开闭音节物理平衡定理</b>
<p>辅音交替（K/P/T 强弱交替）常被视为死记硬背的规则，但其背后是由音节闭合引起的声学能量自发平衡（Phonological Compensatory Shortening）。掌握开闭音节本质，即可推导全语系变格变位。</p>
</div>
<p><b>1. 音步与音节开闭的物理定律</b>：</p>
<ul>
  <li><b>开音节（Avotavu）</b>：以元音结尾的音节（如 <code>ta-kki</code> 中的第一音节因双写闭合，但词干 <code>ta-lo</code> 为开音节）。在开音节中，辅音处于<b>强级（Vahva aste）</b>。</li>
  <li><b>闭音节（Umpitavu）</b>：以辅音结尾的音节。当加上单辅音后缀（如属格后缀 <code>-n</code>、单数第一人称动词后缀 <code>-n</code>、宾格 <code>-t</code>）时，原词根末音节由“开”转“闭”（如 <code>ku-ppi</code> $\to$ <code>ku-pin</code>）。为了保持音步重音能量守恒，音节首的辅音被迫自发弱化为<b>弱级（Heikko aste）</b>。</li>
</ul>
<p><b>2. 辅音交替的完整代数矩阵</b>：</p>
<table>
  <tr><th>类型</th><th>强级（开音节）</th><th>弱级（闭音节）</th><th>名词变格例词（原形 ⟹ 属格）</th><th>动词变位例词（原型 ⟹ 1.sg）</th></tr>
  <tr><td>数量双写交替</td><td>kk / pp / tt</td><td>k / p / t</td><td>pankki ⟹ pankin / kuppi ⟹ kupin</td><td>nukkua ⟹ nukun / ottaa ⟹ otan</td></tr>
  <tr><td>清塞音弱化交替</td><td>p ⟹ v</td><td>v</td><td>halpa ⟹ halvan</td><td>leipoa ⟹ leivon</td></tr>
  <tr><td>同化与脱落交替</td><td>t ⟹ d / k ⟹ ∅</td><td>d / ∅</td><td>koti ⟹ kodin / jalka ⟹ jalan</td><td>tietää ⟹ tiedän / lukea ⟹ luen</td></tr>
  <tr><td>鼻音流音同化</td><td>mp ⟹ mm / lt ⟹ ll</td><td>mm / ll</td><td>kampa ⟹ kamman / ilta ⟹ illan</td><td>ampua ⟹ ammun / kieltää ⟹ kiellän</td></tr>
</table>
"""
        l['html'] = inject_to_section(l['html'], 'detail', fin_extra)
    elif l['slug'] == 't11-henkilotiedot':
        l['title_zh'] = 'Tunti 11 · 个人信息与咖啡厅场景'
        l['part'] = '第 4 章 属格、个人信息与复习'
    elif l['slug'] == 't12-kertaus':
        l['title_zh'] = 'Tunti 12 (Kertaus) · 复习、考试与文化'
        l['part'] = '第 4 章 属格、个人信息与复习'

save_json('33295.json', d33295)
print('[OK] 33295 芬兰语 课次规范与音系学拓展标注完成')

# ==============================================================================
# 3. 修复与深化 30352 (Python 程序设计)
# ==============================================================================
d30352 = get_base_json('30352.json')
for l in d30352['lectures']:
    if l['slug'] == 'ch11-errors':
        l['title_zh'] = '第 9 讲 · 错误、异常与调试体系'
    elif l['slug'] == 'ch12-dicts-sets-json':
        l['title_zh'] = '第 10 讲 · 字典、集合、JSON 与自有模块'
    elif l['slug'] == 'ch11-tuples-sets-packages-numpy':
        l['title_zh'] = '第 11 讲 · 元组、包管理与 NumPy 数组科学计算'

fn_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.0 函数调用的底层机理：调用栈（Call Stack）与 LEGB 作用域解析</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】函数栈帧生命周期与作用域空间隔离原理</b>
<p>在底层计算机体系中，函数并非纯粹的代码跳转，而是拥有独立运行上下文的栈帧对象（PyFrameObject）。理解调用栈与 LEGB 探测顺序，是杜绝未绑定局部变量异常（UnboundLocalError）与内存泄露的基石。</p>
</div>
<p><b>1. 调用栈与栈帧（Stack Frame）生命周期</b>：每当发生一次函数调用时，CPython 解释器都会在进程的调用栈上压入一个全新的栈帧对象 <code>PyFrameObject</code>。该栈帧独立持有：局部变量表（Fast Locals）、求值栈（Evaluation Stack）和指令指针（f_lasti）。当函数返回时，该栈帧被弹出并销毁，局部变量绑定的对象引用计数减 1。递归过深导致的 <code>RecursionError</code>，本质上是调用栈帧数量触碰了 Python 的安全防御阈值（默认 1000）。</p>
<p><b>2. 作用域查找的 LEGB 严格顺序</b>：当在函数中引用一个变量名时，解释器严格按照四层命名空间逐层向上探测：<b><code>L (Local 局部) ⟹ E (Enclosing 闭包外层) ⟹ G (Global 全局模块) ⟹ B (Built-in 内建函数)</code></b>。注意：在函数内部对变量进行赋值默认会将该变量直接标记为 Local。若要在内部修改全局变量或外层闭包变量，必须显式使用 <code>global</code> 或 <code>nonlocal</code> 声明，否则解释器会在编译阶段将其优化为局部变量，导致 <code>UnboundLocalError</code>。</p>
"""

cls_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.0 面向对象的高级机制：魔法方法（Dunder Methods）与 Python 数据模型</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Python 统一数据模型与双下划线协议契约</b>
<p>Python 一切皆对象的核心在于数据模型（Data Model）。通过实现 <code>__repr__</code>、<code>__eq__</code> 与 <code>__hash__</code>，自定义类型可以无缝融入 Python 语言生态并支持哈希集合与字典键检索。</p>
</div>
<p><b>1. <code>__str__</code> 与 <code>__repr__</code> 的设计哲学区分</b>：</p>
<ul>
  <li><code>__repr__</code>：面向开发者和调试器。其返回字符串应当尽可能精确无歧义，理想情况下满足 <code>eval(repr(obj)) == obj</code>。</li>
  <li><code>__str__</code>：面向终端用户。返回人类易读的展示信息。如果类中未定义 <code>__str__</code>，解释器会自动降级调用 <code>__repr__</code>。</li>
</ul>
<p><b>2. 对象可哈希性（Hashability）与字典键契约</b>：如果一个对象要作为字典的 Key 或存入 <code>set</code>，它必须是不可变对象且满足哈希公理：若自定义类重写了 <code>__eq__</code>，Python 会自动将 <code>__hash__</code> 设为 <code>None</code>（即该类对象默认变为不可哈希），防止放入哈希表后因属性修改导致哈希槽位失效。若需要作为只读键，必须显式重写 <code>__hash__</code>，且满足 <code>a == b ⟹ hash(a) == hash(b)</code>。</p>
"""

numpy_extra = r"""
<h3><span class="badge purple">拓展深化</span> 11.5 NumPy 连续内存步进（Strides）与广播机制（Broadcasting）的数学几何原理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】NumPy 连续 C 内存布局与多维张量广播代数</b>
<p>NumPy 高性能的核心是连续内存缓冲区与步长元组（Strides），广播机制允许在零内存复制开销下对齐不同维度的张量进行矢量化运算。</p>
</div>
<p><b>1. 内存存储模型：从扁平一维数组到高维张量</b>：NumPy 数组内部由两部分构成：一块连续的 C 语言原生内存缓冲区（Data Buffer）和元数据（Shape, Dtype, Strides）。<b>步长（Strides）</b> 是一个元组，指明在每个维度上前进一步需要在底层内存跳过多少个字节。例如一个 <code>float64</code>（8字节）的 $3 \times 4$ 行优先（C-order）矩阵，其 <code>shape=(3, 4)</code>，而 <code>strides=(32, 8)</code>。矩阵转置 <code>A.T</code> 仅仅是将 <code>strides</code> 反转为 <code>(8, 32)</code>，完全不发生任何内存拷贝（Zero-copy View）。</p>
<p><b>2. 广播机制（Broadcasting）的严格代数准则</b>：当两个形状不同的数组进行二元算术运算时，NumPy 从<b>最末尾维度（尾部对齐）</b>开始逐维向前比较：</p>
<ul>
  <li>若两维度尺寸相等，匹配成功；</li>
  <li>若其中一个维度尺寸为 1，则该维度被“广播”（虚拟复制延伸）以匹配另一个维度的尺寸；此时底层通过将该维度的步长设为 0（<code>stride = 0</code>），实现同一块内存反复读取而不占用额外物理内存；</li>
  <li>若维度完全缺失，则在前部补充尺寸为 1 的维度；</li>
  <li>若两维度尺寸不相等且均不为 1，抛出 <code>ValueError: operands could not be broadcast together</code>。</li>
</ul>
"""

for l in d30352['lectures']:
    if l['slug'] == 'ch06-functions':
        l['html'] = inject_to_section(l['html'], 'detail', fn_extra)
    elif l['slug'] == 'ch07-classes':
        l['html'] = inject_to_section(l['html'], 'detail', cls_extra)
    elif l['slug'] == 'ch11-tuples-sets-packages-numpy':
        l['html'] = inject_to_section(l['html'], 'detail', numpy_extra)

save_json('30352.json', d30352)
print('[OK] 30352 Python 编程核心原理与拓展标注完成')

# ==============================================================================
# 4. 修复与深化 80 (工程数学 II / 线性代数与几何)
# ==============================================================================
d80 = get_base_json('80.json')

param_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.9 参数曲线的斜率、光滑性与二阶导数深度推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】参数方程二阶导数链式法则展开</b>
<p>参数方程 $x=x(t), y=y(t)$ 的二阶导数 $\frac{d^2y}{dx^2}$ 必须由 $\frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{y'(t)}{x'(t)}\right)}{x'(t)}$ 计算，分母出现三次项 $(x'(t))^3$。</p>
</div>
<p><b>【推导过程】</b>：设参数方程为 $x=x(t), y=y(t)$ 且 $x'(t) \ne 0$。一阶导数为 $\frac{dy}{dx} = \frac{y'(t)}{x'(t)}$。根据链式法则求二阶导数：</p>
<p>$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{y'(t)}{x'(t)}\right)}{\frac{dx}{dt}} = \frac{\frac{y''(t)x'(t) - y'(t)x''(t)}{[x'(t)]^2}}{x'(t)} = \frac{x'(t)y''(t) - x''(t)y'(t)}{[x'(t)]^3}$$</p>
<p>注意：分母是三次项 $[x'(t)]^3$ 而非平方，且二阶导数绝不能写成 $y''(t)/x''(t)$！当 $\frac{d^2y}{dx^2} > 0$ 时曲线在对应区间严格凹向上（Concave up），反之凹向下。</p>

<h3><span class="badge purple">拓展深化</span> 1.9.1 几何进阶：参数曲线的曲率（Curvature）与密切圆</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】曲率公式 $\kappa(t)$ 的内积展开与密切圆几何意义</b>
<p>曲率度量切向量转角对弧长的变化率 $\kappa = |\frac{d\phi}{ds}|$，通过单位切向量微分与外积展开推导出二维参数形式 $\kappa(t) = \frac{|x'y'' - y'x''|}{(x'^2 + y'^2)^{3/2}}$。</p>
</div>
<p>曲率 $\kappa$ 描述曲线上某点弯曲剧烈程度，定义为切线切向角 $\phi$ 对弧长 $s$ 的变化率：$\kappa = |\frac{d\phi}{ds}|$。由于 $ds = \sqrt{x'^2 + y'^2}dt$，而 $\tan\phi = \frac{y'}{x'}$，对其关于 $t$ 微分得 $\sec^2\phi \frac{d\phi}{dt} = \frac{y''x' - y'x''}{x'^2}$，代入 $\sec^2\phi = 1 + (y'/x')^2 = \frac{x'^2+y'^2}{x'^2}$，最终得到曲率公式：</p>
<p>$$\kappa(t) = \frac{|x'(t)y''(t) - x''(t)y'(t)|}{\left([x'(t)]^2 + [y'(t)]^2\right)^{3/2}}$$</p>
<p>曲率半径定义为 $\rho = 1/\kappa$。在曲线该点处沿内法线方向距离为 $\rho$ 的圆称为<b>密切圆（Osculating Circle）</b>，它是二阶微积分意义上与原曲线吻合度最高的二次切圆。</p>
"""

polar_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.2.1 弧长公式的第一性原理：折线逼近与微元法</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】微元切线逼近与高阶无穷小严格推导</b>
<p>从折线段长度 $\Delta s_k = \sqrt{(\Delta x_k)^2 + (\Delta y_k)^2}$ 出发，结合拉格朗日中值定理与黎曼积分严格证明弧长微分 $ds = \sqrt{1 + [f'(x)]^2}dx$。</p>
</div>
<p>在区间 $[a, b]$ 上插入分割点 $a = x_0 < x_1 < \dots < x_n = b$。相连弦长为 $\Delta L_k = \sqrt{(\Delta x_k)^2 + (\Delta y_k)^2}$。由拉格朗日中值定理，$\Delta y_k = f(x_k) - f(x_{k-1}) = f'(\xi_k)\Delta x_k$（其中 $\xi_k \in (x_{k-1}, x_k)$）。因此：</p>
<p>$$\Delta L_k = \sqrt{1 + [f'(\xi_k)]^2} \Delta x_k \implies L = \lim_{\\|\Delta x\\| \to 0} \sum_{k=1}^n \sqrt{1 + [f'(\xi_k)]^2} \Delta x_k = \int_a^b \sqrt{1 + [f'(x)]^2} dx$$</p>

<h3><span class="badge purple">拓展深化</span> 2.16.1 极坐标下的斜率陷阱：切勿混淆 dr/dθ 与 dy/dx</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】极坐标曲线切线斜率与径向变化率的严格区分</b>
<p>极坐标方程 $r=f(\theta)$ 中 $\frac{dr}{d\theta}$ 仅代表矢径长度对极角的变化率，而切线斜率必须通过参数转换 $x=r\cos\theta, y=r\sin\theta$ 求得 $\frac{dy}{dx}$。</p>
</div>
<p>在极坐标 $r = f(\theta)$ 下，许多同学误将 $dr/d\theta$ 当作切线斜率。实际上切线斜率是平面直角坐标系下的 $dy/dx$。利用参数方程 $x = r\cos\theta = f(\theta)\cos\theta,\quad y = r\sin\theta = f(\theta)\sin\theta$：</p>
<p>$$\frac{dy}{dx} = \frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}} = \frac{f'(\theta)\sin\theta + f(\theta)\cos\theta}{f'(\theta)\cos\theta - f(\theta)\sin\theta} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta}$$</p>
<p>只有当曲线穿过极点（即 $r = 0$）且 $r'(\theta) \ne 0$ 时，公式化简为 $\frac{dy}{dx} = \frac{r'\sin\theta}{r'\cos\theta} = \tan\theta$，此时切线方向刚好与极角射线 $\theta$ 重合。</p>
"""

cyl_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.7.1 坐标变换的局部体积变形率：雅可比行列式（Jacobian）推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】雅可比行列式作为正交曲线坐标基向量标量三重积</b>
<p>柱坐标体积元 $dV = r\,dr\,d\theta\,dz$ 与球坐标体积元 $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ 的本质是切向量张成微元平行六面体的标量三重积（行列式）。</p>
</div>
<p>在多元微积分变量替换中，微元体积变换满足 $dV = |J| du\\,dv\\,dw$。雅可比行列式 $J$ 几何意义是局部切空间基向量张成的平行六面体有向体积：</p>
<p><b>1. 柱坐标雅可比推导</b>：变换为 $x = r\cos\theta, y = r\sin\theta, z = z$。计算偏导数行列式：</p>
<p>$$J_{cyl} = \det \begin{pmatrix} \cos\theta & -r\sin\theta & 0 \\\\ \sin\theta & r\cos\theta & 0 \\\\ 0 & 0 & 1 \end{pmatrix} = 1 \cdot (r\cos^2\theta - (-r\sin^2\theta)) = r \implies dV = r\\,dr\\,d\theta\\,dz$$</p>
<p><b>2. 球坐标雅可比推导</b>：变换为 $x = \rho\sin\phi\cos\theta, y = \rho\sin\phi\sin\theta, z = \rho\cos\phi$。经行列式展开化简可严格得出：$J_{sph} = \rho^2 \sin\phi$，故 $dV = \rho^2\sin\phi\\,d\rho\\,d\phi\\,d\theta$。</p>
"""

mat_extra = r"""
<h3><span class="badge purple">拓展深化</span> 4.6.1 为什么矩阵乘法是“行乘列”：线性映射复合的本质推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】矩阵乘法行乘列法则的同态复合起源</b>
<p>矩阵本质上是有限维向量空间之间线性映射在选定基底下的坐标表示，两矩阵相乘对应两个线性映射的复合变换 $T_B \circ T_A$。</p>
</div>
<p>设线性变换 $T_A: \mathbb{R}^p \to \mathbb{R}^n$ 由矩阵 $A_{n\times p}$ 诱导，即 $y = Ax$；变换 $T_B: \mathbb{R}^m \to \mathbb{R}^p$ 由矩阵 $B_{p\times m}$ 诱导，即 $x = Bz$。考虑复合变换 $T = T_A \circ T_B: \mathbb{R}^m \to \mathbb{R}^n$：</p>
<p>$$y_i = \sum_{k=1}^p a_{ik} x_k = \sum_{k=1}^p a_{ik} \left(\sum_{j=1}^m b_{kj} z_j\right) = \sum_{j=1}^m \left( \sum_{k=1}^p a_{ik} b_{kj} \right) z_j$$</p>
<p>为使复合变换仍满足 $y = Cz$，矩阵 $C$ 的第 $i$ 行第 $j$ 列元素必须定义为 $c_{ij} = \sum_{k=1}^p a_{ik}b_{kj}$。这在几何上正是 $A$ 的第 $i$ 个行向量与 $B$ 的第 $j$ 个列向量的标准内积！因此，“行乘列”并非人为规定，而是线性函数复合的唯一必然代数表达。</p>

<h3><span class="badge purple">拓展深化</span> 4.10.1 经典几何变换矩阵的严密推导：平面正交旋转矩阵</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】正交旋转矩阵的标准推导与保范性</b>
<p>通过追踪标准基向量 $e_1, e_2$ 在逆时针旋转 $\theta$ 后的映射像，以及和角公式严格构造正交旋转矩阵 $R_\theta$。</p>
</div>
<p>设向量绕原点逆时针旋转 $\theta$。标准基向量 $e_1 = (1, 0)^T$ 旋转后变为 $(\cos\theta, \sin\theta)^T$；$e_2 = (0, 1)^T$ 旋转后变为 $(-\sin\theta, \cos\theta)^T$。由线性变换性质，以像向量为列构成变换矩阵：</p>
<p>$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\\\ \sin\theta & \cos\theta \end{pmatrix}$$</p>
<p>验证其行列式 $\det(R_\theta) = \cos^2\theta + \sin^2\theta = 1$。且 $R_\theta^T R_\theta = I$，证明平面旋转属于保内积、保长度的正交变换群 $SO(2)$。</p>
"""

det_extra = r"""
<h3><span class="badge purple">拓展深化</span> 5.3.1 伴随矩阵与逆矩阵核心恒等式的严格证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Laplace 代数余子式展开与伴随矩阵恒等式 $A \cdot \text{adj}(A) = |A|I$ 证明</b>
<p>证明 $i=j$ 时代数余子式展开等于行列式自身，而 $i \ne j$ 时异行代数余子式相乘等于带有相同两行的奇异矩阵行列式（必为 0）。</p>
</div>
<p>定义伴随矩阵 $\text{adj}(A) = [C_{ij}]^T$，其中 $C_{ij} = (-1)^{i+j}M_{ij}$ 为代数余子式。考虑乘积 $P = A \cdot \text{adj}(A)$ 的第 $i$ 行第 $k$ 列元素：</p>
<p>$$P_{ik} = \sum_{j=1}^n a_{ij} (\text{adj}(A))_{jk} = \sum_{j=1}^n a_{ij} C_{kj}$$</p>
<ul>
  <li>当 $i = k$ 时：$\sum_{j=1}^n a_{ij} C_{ij} = \det(A)$（按第 $i$ 行的 Laplace 行列式展开定理）；</li>
  <li>当 $i \ne k$ 时：$\sum_{j=1}^n a_{ij} C_{kj}$ 等价于将矩阵 $A$ 的第 $k$ 行替换为第 $i$ 行后求行列式。因为该新矩阵包含两个完全相同的行（第 $i$ 行与第 $k$ 行），根据行列式反对称性质，其行列式必恒等于 0！</li>
</ul>
<p>因此 $A \cdot \text{adj}(A) = \det(A) I$。当 $\det(A) \ne 0$ 时两边同除以 $\det(A)$，即严格证明 $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$。</p>
"""

gauss_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.3.1 高斯消元背后的矩阵代数：初等行变换等于左乘初等矩阵</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】初等矩阵的可逆性与行化简代数算子化</b>
<p>高斯消元中的倍加、对换、倍乘操作在代数上完全等价于左乘三种初等矩阵 $E_{ij}(c), P_{ij}, D_i(c)$，均严格非奇异且逆矩阵同型。</p>
</div>
<p>对矩阵进行初等行变换等价于对单位矩阵 $I$ 施行相同变换得到的<b>初等矩阵（Elementary Matrix）</b>实施左乘：</p>
<ul>
  <li><b>倍加行变换 $r_i \leftarrow r_i + c r_j$</b>：对应初等矩阵 $E_{ij}(c)$，其逆矩阵为同型的 $E_{ij}(-c)$；</li>
  <li><b>交换行变换 $r_i \leftrightarrow r_j$</b>：对应置换矩阵 $P_{ij}$，其逆矩阵为自身 $P_{ij}^{-1} = P_{ij}$；</li>
  <li><b>倍乘非零标量 $r_i \leftarrow k r_i (k \ne 0)$</b>：对应对角初等矩阵 $D_i(k)$，逆矩阵为 $D_i(1/k)$。</li>
</ul>
<p>由于所有初等矩阵均为满秩可逆矩阵，消元过程 $E_k \dots E_2 E_1 A = R$ 保持了线性映射的核（Kernel）和解空间绝对不变。</p>

<h3><span class="badge purple">拓展深化</span> 6.3.2 线性方程组解结构的完备定理：Rouché–Capelli 判定法则</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Rouché-Capelli 定理与线性方程组解空间维数</b>
<p>系数矩阵秩 $\text{rank}(A)$ 与增广矩阵秩 $\text{rank}(A|b)$ 的比较是判断方程组相容性的充要条件，自由未知量数目等于解空间的维数 $n - \text{rank}(A)$。</p>
</div>
<p>对于线性系统 $Ax = b$（$n$ 个未知数）：</p>
<ul>
  <li><b>无解（Inconsistent）</b>：$\text{rank}(A) < \text{rank}(A|b)$。此时阶梯形出现形如 $[0\\ 0\\ \dots\\ 0 \mid d]$（$d \ne 0$）的矛盾行；</li>
  <li><b>唯一解</b>：$\text{rank}(A) = \text{rank}(A|b) = n$。主元列数等于未知数个数，零空间平凡 $\ker(A) = \\{0\\}$；</li>
  <li><b>无穷多解</b>：$\text{rank}(A) = \text{rank}(A|b) = r < n$。解集结构为特解加齐次通解：$x = x_p + \sum_{i=1}^{n-r} c_i v_i$，其中自由变量数目恰好为解空间的自由度度量 $n - r$。</li>
</ul>
"""

eigen_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.1.1 特征值与不变子空间理论深度推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】特征方程 $|A - \lambda I| = 0$ 的非平凡解核空间本质</b>
<p>特征向量所在的一维子空间在变换 $A$ 下保持方向不变，几何重数 $\dim(\ker(A-\lambda I))$ 不超过代数重数是矩阵可对角化的核心准则。</p>
</div>
<p>若存在非零向量 $v$ 使得 $Av = \lambda v$，说明线性变换 $A$ 将一维子空间 $\text{span}\\{v\\}$ 映射到其自身，该一维子空间称为算子的<b>不变子空间（Invariant Subspace）</b>。改写为齐次方程 $(A - \lambda I)v = 0$。由克拉默法则与秩定理，齐次系统存在非零解的充要条件是系数矩阵奇异，即行列式特征方程 $\det(A - \lambda I) = 0$。特征值对应特征子空间 $E_\lambda = \ker(A - \lambda I)$ 的维数称为<b>几何重数（Geometric Multiplicity）</b>，它必小于等于特征多项式根的<b>代数重数（Algebraic Multiplicity）</b>。</p>
"""

cauchy_extra = r"""
<h3><span class="badge purple">拓展深化</span> 8.6 柯西-施瓦茨不等式（Cauchy-Schwarz Inequality）的经典代数证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】构造实系数非负二次三项式判定柯西-施瓦茨不等式</b>
<p>构造函数 $P(t) = \sum (u_i t + v_i)^2 \ge 0$，利用判别式 $\Delta = B^2 - 4AC \le 0$ 极为优雅地完成恒等论证与等号成立条件判定。</p>
</div>
<p><b>【严密定理证明】</b>：对于任意两组实向量 $u = (u_1, \dots, u_n)$ 与 $v = (v_1, \dots, v_n)$，有：</p>
<p>$$\left( \sum_{i=1}^n u_i v_i \right)^2 \le \left( \sum_{i=1}^n u_i^2 \right) \left( \sum_{i=1}^n v_i^2 \right)$$</p>
<p><b>证明</b>：构造关于实变量 $t$ 的实二次函数 $P(t) = \sum_{i=1}^n (u_i t + v_i)^2$。显然对所有实数 $t$，由于各项均为实数平方和，必有 $P(t) \ge 0$。将 $P(t)$ 展开按 $t$ 的幂次整理：</p>
<p>$$P(t) = \left( \sum_{i=1}^n u_i^2 \right) t^2 + 2 \left( \sum_{i=1}^n u_i v_i \right) t + \left( \sum_{i=1}^n v_i^2 \right) = A t^2 + B t + C$$</p>
<p>其中 $A = \\|u\\|^2, B = 2(u \cdot v), C = \\|v\\|^2$。若 $A = 0$，则 $u = 0$，不等式显然成立 ($0 \le 0$)。若 $A > 0$，由于开口向上的二次多项式 $P(t) \ge 0$ 对所有实数 $t$ 恒成立，该方程至多有一个实根，因此其判别式必须满足 $\Delta = B^2 - 4AC \le 0$：</p>
<p>$$\Delta = [2(u \cdot v)]^2 - 4 \\|u\\|^2 \\|v\\|^2 = 4 (u \cdot v)^2 - 4 \\|u\\|^2 \\|v\\|^2 \le 0 \implies (u \cdot v)^2 \le \\|u\\|^2 \\|v\\|^2$$</p>
<p>两边开方即得 $|u \cdot v| \le \\|u\\| \\|v\\|$。等号成立当且仅当存在 $t_0$ 使得 $P(t_0) = 0$，即对所有 $i$ 有 $u_i t_0 + v_i = 0$，这表示向量 $u$ 与 $v$ 线性相关！</p>

<h3><span class="badge purple">拓展深化</span> 8.7 三角不等式（Triangle Inequality）的推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】向量模长三角不等式的范数公理证明</b>
<p>利用柯西-施瓦茨不等式展开 $\|u + v\|^2 = \|u\|^2 + 2(u \cdot v) + \|v\|^2 \le (\|u\| + \|v\|)^2$，完成赋范向量空间核心公理推导。</p>
</div>
<p>在柯西-施瓦茨不等式基础上证明 $\|u + v\| \le \\|u\\| + \\|v\\|$：</p>
<p>$$\\|u + v\\|^2 = (u + v) \cdot (u + v) = \\|u\\|^2 + 2(u \cdot v) + \\|v\\|^2$$</p>
<p>因为 $u \cdot v \le |u \cdot v| \le \\|u\\| \\|v\\|$（柯西-施瓦茨不等式），故：</p>
<p>$$\\|u + v\\|^2 \le \\|u\\|^2 + 2\\|u\\| \\|v\\| + \\|v\\|^2 = (\\|u\\| + \\|v\\|)^2$$</p>
<p>两端均非负，开平方即得 $\\|u + v\\| \le \\|u\\| + \\|v\\|$。几何直观即“三角形两边之和大于等于第三边”。</p>
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
print('[OK] 80 工程数学 II 全章节深度增强与拓展标注完成')

# ==============================================================================
# 5. 修复与深化 62 (工程数学 I / 单变量微积分)
# ==============================================================================
d62 = get_base_json('62.json')

lim_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.0 极限的本质形式化：柯西 ε-δ 语言与严谨证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】柯西 $\epsilon-\delta$ 极限形式化分析方法</b>
<p>从动态直觉过渡到静态严格集合刻画：对任意给定的任意小容差 $\epsilon>0$，如何通过逆向解不等式构造出自变量受控邻域 $\delta = \min(1, \frac{\epsilon}{M})$。</p>
</div>
<p><b>【定义】</b>：我们称 $\lim_{x \to c} f(x) = L$，如果对于<b>任意</b>给定的正数 $\varepsilon > 0$，<b>都存在</b>一个正数 $\delta > 0$，使得当自变量 $x$ 满足：</p>
<p>$$0 < |x - c| < \delta \implies |f(x) - L| < \varepsilon$$</p>
<p><b>【严谨 ε-δ 证明典范】</b>：证明 $\lim_{x \to 3} (2x^2 - 5x) = 3$。</p>
<p><b>证明构思与分析</b>：需控制 $|(2x^2 - 5x) - 3| = |2x + 1| |x - 3| < \varepsilon$。我们需要先限制 $|x - 3|$ 使得因子 $|2x + 1|$ 具备一个有限的上界。先设定一个初始探测步长 $\delta_1 = 1$。当 $|x - 3| < 1$ 时，$-1 < x - 3 < 1 \implies 2 < x < 4$。因此 $5 < 2x + 1 < 9 \implies |2x + 1| < 9$。此时有：</p>
<p>$$|2x + 1| |x - 3| < 9 |x - 3|$$</p>
<p>为了使乘积小于 $\varepsilon$，只需额外要求 $|x - 3| < \frac{\varepsilon}{9}$。因此我们取 $\delta = \min\left(1, \frac{\varepsilon}{9}\right)$。</p>
<p><b>正式证明论述</b>：对任意给定的 $\varepsilon > 0$，取 $\delta = \min\left(1, \frac{\varepsilon}{9}\right) > 0$。当 $0 < |x - 3| < \delta$ 时，由于 $\delta \le 1$，必有 $|2x + 1| < 9$；同时由于 $\delta \le \frac{\varepsilon}{9}$，必有 $|x - 3| < \frac{\varepsilon}{9}$。两式相乘得：</p>
<p>$$|(2x^2 - 5x) - 3| = |2x + 1| |x - 3| < 9 \cdot \frac{\varepsilon}{9} = \varepsilon$$</p>
<p>证毕。这就是柯西形式化分析方法的核心：通过不等式放缩将任意给定的 $\varepsilon$ 逆向映射构造出 $\delta$。</p>

<h3><span class="badge purple">拓展深化</span> 2.5.1 夹逼定理（Squeeze Theorem）与第一重要极限</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】单位圆扇形面积不等式与 $\lim_{x \to 0} \frac{\sin x}{x} = 1$ 几何构造论证</b>
<p>在单位圆中由三角形面积小于扇形面积小于外切三角形面积建立 $\cos\theta < \frac{\sin\theta}{\theta} < 1$，由夹逼定理完成首要超越极限证明。</p>
</div>
<p>在第一象限单位圆内，当 $0 < \theta < \frac{\pi}{2}$ 时，显然有面积包合关系：</p>
<p>$$\text{Area}(\triangle OAP) < \text{Area}(\text{Sector } OAP) < \text{Area}(\triangle OAT)$$</p>
<p>代入公式：$\frac{1}{2} \cdot 1 \cdot \sin\theta < \frac{1}{2} \cdot 1^2 \cdot \theta < \frac{1}{2} \cdot 1 \cdot \tan\theta \implies \sin\theta < \theta < \frac{\sin\theta}{\cos\theta}$。各边同除以 $\sin\theta > 0$ 并取倒数，不等号变向：</p>
<p>$$\cos\theta < \frac{\sin\theta}{\theta} < 1$$</p>
<p>由于 $\lim_{\theta \to 0^+} \cos\theta = 1$ 且 $\lim_{\theta \to 0^+} 1 = 1$，由夹逼定理，右极限为 1。由于 $\frac{\sin(-\theta)}{-\theta} = \frac{\sin\theta}{\theta}$ 为偶函数，左极限亦为 1。故严谨得证：$\lim_{x \to 0} \frac{\sin x}{x} = 1$。</p>
"""

prod_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.1.1 乘积法则（Product Rule）的严密代数推导</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】差商展开中“加一项减一项”对称技巧推导 $(fg)' = f'g + fg'$</b>
<p>深入差商结构 $\frac{f(x+h)g(x+h) - f(x)g(x)}{h}$，引入中间项拆分为两个极限项，严谨展现可微性与连续性的内在联系。</p>
</div>
<p>设 $u(x) = f(x)g(x)$，且 $f, g$ 在 $x$ 处均可微（由可微性可知 $f$ 必在 $x$ 处连续，即 $\lim_{h \to 0} f(x+h) = f(x)$）。根据导数微商定义：</p>
<p>$$u'(x) = \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x)g(x)}{h}$$</p>
<p>技巧：在分子中<b>减去并加上</b>辅助项 $f(x+h)g(x)$：</p>
<p>$$u'(x) = \lim_{h \to 0} \frac{[f(x+h)g(x+h) - f(x+h)g(x)] + [f(x+h)g(x) - f(x)g(x)]}{h}$$</p>
<p>$$= \lim_{h \to 0} \left[ f(x+h) \cdot \frac{g(x+h) - g(x)}{h} + g(x) \cdot \frac{f(x+h) - f(x)}{h} \right]$$</p>
<p>利用极限的线性运算法则及连续性 $\lim_{h \to 0} f(x+h) = f(x)$：</p>
<p>$$u'(x) = \left(\lim_{h \to 0} f(x+h)\right) \cdot \left(\lim_{h \to 0} \frac{g(x+h) - g(x)}{h}\right) + g(x) \cdot \left(\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}\right) = f(x)g'(x) + g(x)f'(x)$$</p>
<p>证毕。此推导清晰展现了微积分代数构造中引入对称平衡项的核心技巧。</p>
"""

mvt_extra = r"""
<h3><span class="badge purple">拓展深化</span> 4.2.1 微分中值定理体系链：罗尔 ⟹ 拉格朗日 ⟹ 柯西中值定理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】从极值费马引理到微分中值定理三大核心推导链</b>
<p>由闭区间连续函数必有最值结合费马引理证明罗尔定理；构造割线偏差辅助函数证明拉格朗日定理；再推广至参数曲线比率辅助函数证明柯西定理。</p>
</div>
<p>整个微分学的核心理论基石由三大中值定理递进构成：</p>
<p><b>1. 费马引理（Fermat's Lemma）</b>：若 $f$ 在可导点 $c$ 取极值，则必有 $f'(c) = 0$。证明考察左导数 $\ge 0$ 与右导数 $\le 0$，迫使其导数必为 0。</p>
<p><b>2. 罗尔定理（Rolle's Theorem）</b>：若 $f \in C[a, b]$，在 $(a, b)$ 可导，且 $f(a) = f(b)$。由极值定理，$f$ 在闭区间必达最大值 $M$ 与最小值 $m$。若 $M = m$ 则为常数函数，导数恒为 0；若 $M > m$，则必至少有一个最值在开区间内部某点 $\xi$ 取得，由费马引理即得 $f'(\xi) = 0$。</p>
<p><b>3. 拉格朗日中值定理（Lagrange MVT）</b>：构造割线偏差辅助函数 $g(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a)$。易验 $g(a) = g(b) = 0$。由罗尔定理，存在 $\xi \in (a, b)$ 使得 $g'(\xi) = 0$，即：</p>
<p>$$f'(\xi) = \frac{f(b) - f(a)}{b - a} \iff f(b) - f(a) = f'(\xi)(b - a)$$</p>
<p><b>4. 柯西中值定理（Cauchy MVT）</b>：若有两个函数 $f, g$，构造辅助函数 $h(x) = [g(b) - g(a)]f(x) - [f(b) - f(a)]g(x)$，对 $h(x)$ 应用罗尔定理即得 $\frac{f'(\xi)}{g'(\xi)} = \frac{f(b) - f(a)}{g(b) - g(a)}$。这是洛必达法则的直接理论根基！</p>
"""

ftc_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.1.1 微积分基本定理（FTC）第一与第二部分的严密证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】积分上限函数导数与牛顿-莱布尼茨公式双向证明</b>
<p>第一部分利用积分中值定理严格证明变上限积分的导数等于被积函数；第二部分通过对区间划分施加拉格朗日中值定理与黎曼和收敛证明 $\int_a^b f(x)dx = F(b)-F(a)$。</p>
</div>
<p><b>FTC 第一部分（变上限函数导数）</b>：设 $g(x) = \int_a^x f(t) dt$。计算导数微商：</p>
<p>$$\frac{g(x+h) - g(x)}{h} = \frac{1}{h} \left( \int_a^{x+h} f(t)dt - \int_a^x f(t)dt \right) = \frac{1}{h} \int_x^{x+h} f(t)dt$$</p>
<p>由定积分中值定理，存在 $\mu$ 介于 $x$ 与 $x+h$ 之间使得 $\frac{1}{h} \int_x^{x+h} f(t)dt = f(\mu)$。当 $h \to 0$ 时，$\mu \to x$。由 $f$ 的连续性，$\lim_{h \to 0} f(\mu) = f(x)$。因此：$g'(x) = \frac{d}{dx}\int_a^x f(t)dt = f(x)$。</p>
<p><b>FTC 第二部分（牛顿-莱布尼茨公式）</b>：设 $F$ 为 $f$ 的任一原函数，即 $F'(x) = f(x)$。对区间 $[a, b]$ 插入划分 $a = x_0 < x_1 < \dots < x_n = b$：</p>
<p>$$F(b) - F(a) = \sum_{i=1}^n [F(x_i) - F(x_{i-1})]$$</p>
<p>由拉格朗日中值定理，对每个子区间存在 $\xi_i \in (x_{i-1}, x_i)$ 使得 $F(x_i) - F(x_{i-1}) = F'(\xi_i)\Delta x_i = f(\xi_i)\Delta x_i$。代入得：</p>
<p>$$F(b) - F(a) = \sum_{i=1}^n f(\xi_i) \Delta x_i$$</p>
<p>当网格细度 $\lambda = \max\Delta x_i \to 0$ 时，右边恰好是定积分的黎曼和定义。故取极限即证：$\int_a^b f(x)dx = F(b) - F(a)$。</p>
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
print('[OK] 62 工程数学 I 全章节深度增强与拓展标注完成')

# ==============================================================================
# 6. 修复与深化 86 (计算机导论 / 计算思维)
# ==============================================================================
d86 = get_base_json('86.json')

num_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.0 进位记数法的数学抽象与进制转换的代数原理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】位置记数法幂级数与带余除法进制转换代数证明</b>
<p>通过多项式 $N = \sum d_i b^i$ 与数学归纳法严格证明为什么整数“除基取余”与小数“乘基取整”具有数学完备性与唯一确定性。</p>
</div>
<p><b>【数学抽象】</b>：任意实数 $N$ 在基底 $b \in \mathbb{Z}_{>1}$ 下的位置记数多项式唯一展开为：</p>
<p>$$N = \sum_{i=-m}^{n-1} d_i \cdot b^i = d_{n-1}b^{n-1} + \dots + d_1 b^1 + d_0 b^0 + d_{-1}b^{-1} + \dots + d_{-m}b^{-m}\quad (d_i \in \\{0, 1, \dots, b-1\\})$$</p>
<p><b>【带余除法算法证明】</b>：为什么“除以 $b$ 取余数”能提取从低到高的数位？考察整数部分 $N = d_0 + b(d_1 + b(d_2 + \dots))$：</p>
<ul>
  <li>第一次除以 $b$：$N = b \cdot Q_1 + R_0$，其中商 $Q_1 = d_1 + d_2 b + \dots$，余数 $R_0 = d_0$。余数严格满足 $0 \le R_0 < b$，故直接确定最低位 $d_0$；</li>
  <li>第二次对商递归操作：$Q_1 = b \cdot Q_2 + R_1$，余数 $R_1 = d_1$；</li>
  <li>由于商序列严格递减 $N > Q_1 > Q_2 > \dots \ge 0$，算法必然在有限步后终止于 $Q_k = 0$。证毕。</li>
</ul>
"""

float_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.3 浮点数灾难性抵消（Catastrophic Cancellation）与数值算法防御</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】IEEE 754 近似数相减有效位数丢失与数值稳定化算法</b>
<p>推导浮点数相对误差在同量级数相减时的放大效应，给出经典求根公式有理化变型 $x_1 = \frac{-b - \text{sgn}(b)\sqrt{b^2-4ac}}{2a}$ 与 $x_2 = \frac{c}{a x_1}$ 的防抵消实现。</p>
</div>
<p><b>1. 误差放大理论推导</b>：设两近似数 $x, y$ 拥有微小相对误差 $\epsilon_x, \epsilon_y$。考虑差值 $z = x - y$ 的相对误差：</p>
<p>$$\epsilon_z = \frac{(x(1+\epsilon_x) - y(1+\epsilon_y)) - (x-y)}{x-y} = \frac{x\epsilon_x - y\epsilon_y}{x - y}$$</p>
<p>当 $x \approx y$ 时，分母 $|x - y| \to 0$ 极为微小，导致相对误差 $\epsilon_z$ 发生数个数量级的剧烈膨胀！原本具有 53 位精度的有效数字会被完全抵消抹平，高位仅剩舍入噪声。</p>
<p><b>2. 数值算法工程防御</b>：以二次方程 $ax^2 + bx + c = 0$ 求根为例，当 $b > 0$ 且 $b^2 \gg 4ac$ 时，$\sqrt{b^2-4ac} \approx b$，计算 $-b + \sqrt{b^2-4ac}$ 会产生致命的灾难性抵消。经典稳定求根法通过分子有理化改造算法：</p>
<p>$$x_1 = \frac{-b - \text{sgn}(b)\sqrt{b^2-4ac}}{2a},\qquad x_2 = \frac{c}{a x_1}$$</p>
<p>两步运算均完全避开相近浮点数相减，在科学计算库中是极其关键的数值防御范例。</p>
"""

utf_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.3.1 UTF-8 编码的前缀自同步特性（Self-Synchronization）</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】UTF-8 状态机无歧义重同步与前缀码设计</b>
<p>分析 10xxxxxx 作为续字节与 110/1110 引导字节的互斥性，证明当网络传输出现单字节丢失时算法只需跳过至多 3 字节即可自动恢复正常解析。</p>
</div>
<p>UTF-8 能够统一全球网络字符编码的核心数学原因，在于其无前缀自由冲突与<b>自同步（Self-synchronizing）</b>属性：</p>
<ul>
  <li><b>单字节（ASCII 兼容）</b>：<code>0xxxxxxx</code>（最高位恒为 0）；</li>
  <li><b>多字节引导头（Leading byte）</b>：<code>110xxxxx</code>（双字节）、<code>1110xxxx</code>（三字节）、<code>11110xxx</code>（四字节）；</li>
  <li><b>多字节续字节（Continuation byte）</b>：<code>10xxxxxx</code>（最高两位恒为 10）。</li>
</ul>
<p><b>容错定理证明</b>：由于续字节的模式 <code>10xxxxxx</code> 与引导头及 ASCII 字节的模式互不相交（集合交集为空），如果数据流在传输时发生损坏导致解析指针偏离，解码器只需依次扫描字节：遇到任何 <code>10xxxxxx</code> 字节一律略过，直到碰见首个非 <code>10xxxxxx</code> 的字节，即可 100% 确定该处为一个新字符的精确边界，重新同步耗时至多不超过 3 个字节！</p>
"""

shannon_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.3.1 香农第一信源编码定理（Shannon's Source Coding Theorem）与熵界</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】信息熵作为无损压缩理论下界与哈夫曼最优前缀码证明</b>
<p>深入香农熵 $H(X) = -\sum p_i \log_2 p_i$ 的物理与概率论背景，结合 Kraft 不等式证明任何无损前缀编码的平均码长无法低于信源熵。</p>
</div>
<p>克劳德·香农在 1948 年奠定了现代信息论基石：信源所含的平均不可消除信息量由<b>信息熵（Information Entropy）</b>严格度量：</p>
<p>$$H(X) = - \sum_{i=1}^n p_i \log_2 p_i \quad (\text{bits/symbol})$$</p>
<p><b>香农第一编码定理（无失真信源编码定理）</b>指明：对于离散无记忆信源 $X$，使用二进制前缀码对其进行无损编码时，每个符号所需的期望平均码长 $L = \sum p_i l_i$ 必然满足硬下界：</p>
<p>$$L \ge H(X)$$</p>
<p>且存在最优前缀码（如 Huffman 编码），使得平均码长任意逼近熵：$H(X) \le L < H(X) + 1$。任何商业压缩软件（ZIP, GZIP, 7z）无论算法如何进化，都不可能突破香农熵设定的理论物理极限。</p>
"""

ir_extra = r"""
<h3><span class="badge purple">拓展深化</span> 1.3.1 倒排索引求交优化：跳表指针（Skip Pointers）</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】倒排记录表跳表指针步长 $\sqrt{L}$ 的复杂度理论证明</b>
<p>对倒排索引求交算法建立代价模型，证明当跳步长度取 $\sqrt{L}$ 时能将比较次数由 $O(L_1 + L_2)$ 最优降低至 $O(\min(L_1, L_2) \cdot \sqrt{L_1})$。</p>
</div>
<p>在搜索引擎布尔检索中，两个词项的倒排记录表（Posting List）求交（AND 查询）是高频瓶颈。若线性遍历，时间复杂度为 $O(L_1 + L_2)$。通过为长度为 $L$ 的有序链表每隔一定步长 $S$ 设立<b>跳表指针（Skip Pointer）</b>：</p>
<p><b>【最佳步长 $\sqrt{L}$ 的数学极值证明】</b>：设跳表步长为 $S$，则整个链表包含 $L/S$ 个跳步节点。在最坏情况下，如果目标元素位于跳步区间末端，查找代价为：跳步比较次数（至多 $L/S$）加上区间内回退线性扫描次数（至多 $S$）。总比较代价为 $f(S) = \frac{L}{S} + S$。利用基本不等式或求导：</p>
<p>$$f'(S) = -\frac{L}{S^2} + 1 = 0 \implies S = \sqrt{L}$$</p>
<p>因此，选择等距步长 $S = \lceil \sqrt{L} \rceil$ 具有严格的数学最优解，能够将稠密查询与稀疏查询的合并代价大幅压降至 $O(\sqrt{L})$ 级别。</p>
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
print('[OK] 86 计算机导论 全章节深度增强与拓展标注完成')

# ==============================================================================
# 7. 修复与深化 30565 (离散数学 / Discrete Mathematics)
# ==============================================================================
d30565 = get_base_json('30565.json')

lec6_html = r"""<section class="card" data-type="overview"><h2>本节定位</h2><p>本讲探讨集合论最令人震撼的数学前沿：<b>基数（Cardinality）与无穷的度量</b>。针对大学生的知识体系，我们将彻底抛弃简单的感性比喻，从严格的第一性原理建立双射映射尺度，系统性论证可数集（Countable Sets）、康托尔对角线法、希尔伯特无限旅馆构造，以及现代数理逻辑的核心基石——康托尔幂集定理。</p></section>
<section class="card" data-type="detail">
<h3><span class="badge purple">拓展深化</span> 6.0 从伽利略悖论到无限基数：双射作为度量无限的唯一尺度</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】集合基数概念的公理化延伸与等势关系等价类</b>
<p>深入分析为什么在无限集合中“部分可以等于整体”，双射关系如何将所有集合划分为基数等价类并定义超限序数与基数层次。</p>
</div>
<p><b>1. 伽利略悖论（Galileo's Paradox）</b>：在有限集合中，“部分严格小于整体”是直觉公理。但在偶数集 $2\mathbb{N}$ 与正整数集 $\mathbb{N}$ 之间，通过对应规则 $n \leftrightarrow 2n$，每个正整数都能与唯一偶数无遗漏配对！如果坚持“部分小于整体”，就会得出偶数比正整数少；如果坚持“能一一配对则数量相等”，就会得出偶数与正整数一样多。康托尔（Georg Cantor）打破僵局，将<b>双射（Bijection，即一一对应）</b>定义为度量无限集合元素数量（基数）的唯一最高准则。</p>
<p><b>2. 等势与可数性严格公理</b>：</p>
<ul>
  <li>两个集合 $A, B$ 称为<b>等势（Equipotent, 记为 $|A| = |B|$）</b>，当且仅当存在一个双射 $f: A \to B$；</li>
  <li>若一个集合 $A$ 与自然数子集等势，则称 $A$ 为<b>有限集</b>；若 $|A| = |\mathbb{N}|$，则称 $A$ 为<b>可数无限集（Countably Infinite）</b>，其基数记为阿列夫零（$\aleph_0$）；</li>
  <li>有限集与可数无限集统称为<b>可数集（Countable Set）</b>；基数严格大于 $\aleph_0$ 的集合称为<b>不可数集（Uncountable Set）</b>。</li>
</ul>

<h3><span class="badge purple">拓展深化</span> 6.1 康托尔配对函数与有理数集 ℚ 的可数性严密证明</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Cantor Pairing Function $\pi(k_1, k_2) = \frac{(k_1+k_2)(k_1+k_2+1)}{2} + k_2$ 单射证明</b>
<p>严谨证明 $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ 的双射构造与二阶多项式单调性，推导出任何可数个可数集的并集依然可数。</p>
</div>
<p>许多初学者直觉上认为有理数 $\mathbb{Q}$ 稠密分布于数轴上，一定比自然数多得多。康托尔给出了颠覆性的严格代数证明：$|\mathbb{Q}| = |\mathbb{N}|$。</p>
<p><b>第一步：证明 $\mathbb{N} \times \mathbb{N}$ 是可数的</b>。构造<b>康托尔配对函数（Cantor Pairing Function）</b> $\pi: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$：</p>
<p>$$\pi(k_1, k_2) = \frac{(k_1 + k_2)(k_1 + k_2 + 1)}{2} + k_2$$</p>
<p>该公式在几何上对应按对角线折线遍历第一象限整点网格 $(0,0), (1,0), (0,1), (2,0), \dots$。由三角形数单调性可严密证明 $\pi$ 为严格双射。</p>
<p><b>第二步：有理数嵌入</b>。每个正有理数可唯一表示为不可约正分数 $p/q$。定义单射 $f(p/q) = \pi(p, q) \in \mathbb{N}$。由 Cantor-Bernstein-Schröder 定理，$|\mathbb{Q}^+| = |\mathbb{N}|$。同理负有理数与 0 亦可数，可数集的有限并依然可数，故 $|\mathbb{Q}| = \aleph_0$！</p>

<h3><span class="badge purple">拓展深化</span> 6.2 希尔伯特无限旅馆的数学分段函数构造</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】素数幂分解实现无限量无限客人的无冲突房间分配函数</b>
<p>利用算术基本定理的唯一分解性，将第 $i$ 辆无限大巴的第 $j$ 位客人映射到房间 $p_{i+1}^j$，彻底形式化希尔伯特旅馆思维实验。</p>
</div>
<p>希尔伯特旅馆拥有编号为 $1, 2, 3, \dots$ 的无限个房间，且已经全部客满：</p>
<ul>
  <li><b>场景一：新来 1 位客人</b>：将原有住客按函数 $f(n) = n + 1$ 顺移到下一个房间，1 号房间腾空，新客人入住；</li>
  <li><b>场景二：新来一辆载有无限多客人的巴士（客人编号 $1, 2, 3, \dots$）</b>：将原有住客顺移到偶数号房间 $f(n) = 2n$（所有奇数号房间 $2k-1$ 腾出）；新大巴的第 $k$ 位客人直接入住第 $2k-1$ 号房间，两者均一一配对；</li>
  <li><b>场景三：新来可数无限辆巴士，每辆载有无限多客人</b>：利用<b>素数幂分解的唯一性</b>构造无冲突映射函数！原住客搬入 $2^n$ 号房（以 2 为底）；第 $i$ 辆大巴（$i \ge 1$）的第 $j$ 位客人入住房间号 $P(i, j) = p_{i+1}^j$（其中 $p_k$ 是第 $k$ 个素数：$p_2 = 3, p_3 = 5, p_4 = 7, \dots$）。由于不同素数的幂次绝不可能相同，所有客人立刻获得独立房间，且留出海量空房间供未来使用！</li>
</ul>

<h3><span class="badge purple">拓展深化</span> 6.3 康托尔定理的本质证明：|S| < |P(S)| 对角线子集反证法</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】构造对角子集 $D = \{x \in S \mid x \notin f(x)\}$ 证明幂集势严格大于原集</b>
<p>该证明是现代数理逻辑的核心瑰宝：罗素悖论、图灵停机问题不可判定性、哥德尔不完备定理均源于对角子集构造这一共同数学结构。</p>
</div>
<p><b>【Cantor's Theorem】</b>：对于<b>任意</b>集合 $S$（无论有限还是无限），其幂集 $\mathcal{P}(S)$ 的基数严格大于 $S$ 自身的基数，即 $|S| < |\mathcal{P}(S)|$。</p>
<p><b>严格反证法证明</b>：</p>
<ol>
  <li>显见单射存在：映射 $g(x) = \\{x\\}$ 将 $S$ 映入 $\mathcal{P}(S)$，故 $|S| \le |\mathcal{P}(S)|$；</li>
  <li>需证明不存在从 $S$ 到 $\mathcal{P}(S)$ 的满射。假设存在满射 $f: S \to \mathcal{P}(S)$，即对于 $\mathcal{P}(S)$ 中的任何子集 $A$，都能在 $S$ 中找到原像 $x$ 使得 $f(x) = A$；</li>
  <li>构造著名的<b>对角反转子集 $D$</b>：
  $$D = \\{ x \in S \mid x \notin f(x) \\}$$
  显然 $D \subseteq S$，故由幂集定义，$D \in \mathcal{P}(S)$；</li>
  <li>因为 $f$ 是满射，必定存在某个元素 $d \in S$ 使得 $f(d) = D$；</li>
  <li>现在考察 $d$ 是否属于 $D$：
    <ul>
      <li>若 $d \in D$：根据 $D$ 的构造定义，必有 $d \notin f(d)$。而 $f(d) = D$，故推出 $d \notin D$，产生矛盾！</li>
      <li>若 $d \notin D$：说明 $d$ 不满足属于 $D$ 的排除条件，即 $d \in f(d)$。而 $f(d) = D$，故推出 $d \in D$，再次产生矛盾！</li>
    </ul>
  </li>
  <li>无论何种情况均产生逻辑崩溃矛盾，假设不成立！故不存在任何满射 $f$。</li>
</ol>
<p>由上述定理，令 $S = \mathbb{N}$，则 $|\mathcal{P}(\mathbb{N})| = 2^{\aleph_0} > \aleph_0$。这证明了<b>不可数无穷的存在</b>，且无穷拥有无穷无尽的层次：$\aleph_0 < 2^{\aleph_0} < 2^{2^{\aleph_0}} < \dots$，粉碎了亚里士多德以来关于单一无穷的朴素观念。</p>
</section>
<section class="card" data-type="keywords"><table><tr><th>English</th><th>中文</th><th>说明</th></tr><tr><td>Cardinality</td><td>基数 / 势</td><td>度量集合元素数量的尺度</td></tr><tr><td>Bijection</td><td>双射 / 一一对应</td><td>既是单射又是满射</td></tr><tr><td>Countable</td><td>可数的</td><td>能与自然数子集建立双射</td></tr><tr><td>Uncountable</td><td>不可数的</td><td>基数严格大于可数无限</td></tr><tr><td>Cantor Pairing</td><td>康托尔配对函数</td><td>证明两个可数集的笛卡尔积仍可数</td></tr><tr><td>Diagonal Argument</td><td>对角线论证法</td><td>证明实数不可数与停机问题不可判定</td></tr><tr><td>Power Set</td><td>幂集</td><td>由原集合所有子集构成的集合</td></tr></table></section>
<section class="card" data-type="examples"><h2>例题 1：证明奇数集可数</h2><div class="qa"><div class="q">构造正奇数集合 $O = \\{1, 3, 5, \dots\\}$ 到正整数集 $\mathbb{Z}^+$ 的双射。</div><p><b>解</b>：令 $f(n) = 2n - 1$。单射证明：若 $2n_1 - 1 = 2n_2 - 1 \implies 2n_1 = 2n_2 \implies n_1 = n_2$。满射证明：任意正奇数 $k$，必存在整数 $n = (k+1)/2 \ge 1$ 使得 $f(n) = k$。故 $f$ 为双射，奇数集与正整数集基数相等。</p></div>
<h2>例题 2：对角线实数不可数判定</h2><div class="qa"><div class="q">说明如何构造 $(0, 1)$ 区间内不同于所有可数列出的新实数。</div><p><b>解</b>：设列出的小数为 $r_n = 0.d_{n1}d_{n2}d_{n3}\dots$。定义新实数 $x = 0.x_1 x_2 x_3\dots$，其中若 $d_{nn} = 5$ 则取 $x_n = 6$，否则取 $x_n = 5$。由于 $x$ 的第 $n$ 位小数与 $r_n$ 的第 $n$ 位小数严格不相等，故 $x \ne r_n$ 对所有自然数 $n$ 恒成立，矛盾！</p></div></section>
<section class="card" data-type="practice"><h2>自我检测</h2><p>1. 两个无限集合能够建立一一对应，是否说明它们基数相等？</p><details><summary>答案解析</summary><div class="ans"><p>正确。根据康托尔集合论定义，存在双射正是两集合等势（基数相等）的充要条件。</p></div></details>
<p>2. 实数集与复数集基数谁更大？</p><details><summary>答案解析</summary><div class="ans"><p>两者基数相等，均为连续统势 $\mathfrak{c} = 2^{\aleph_0}$。可通过对实部虚部交错织成单实数建立双射。</p></div></details></section>
<section class="card" data-type="exam"><h2>核心考点</h2><div class="callout exam"><b>期末必考</b><ul><li>可数集与不可数集的定义判定</li><li>证明给定集合可数的双射构造法</li><li>康托尔对角线法在实数证明中的经典步骤</li><li>幂集基数公式 $|\mathcal{P}(S)| = 2^{|S|}$ 与康托尔定理</li></ul></div></section>
<section class="card" data-type="checklist"><h2>复习核对表</h2><ol class="steps"><li>熟记双射是证明等势的唯一标准</li><li>掌握偶数、奇数、整数、有理数可数的构造映射</li><li>理解希尔伯特旅馆三次客流模型的数学函数</li><li>能独立写出对角子集 $D = \\{x \mid x \notin f(x)\\}$ 的反证全过程</li></ol></section>
<section class="card" data-type="mapping"><h2>教学大纲对应</h2><table><tr><th>知识模块</th><th>大纲位置</th><th>进阶说明</th></tr><tr><td>集合与基数</td><td>Chapter 2.1</td><td>补充了 Cantor Pairing Function 与对角子集形式化公理证明</td></tr><tr><td>可数与不可数</td><td>Chapter 2.2</td><td>补充了希尔伯特旅馆素数幂分配数学解</td></tr></table></section>"""

for l in d30565['lectures']:
    if l['slug'] == 'cardinality-countable-sets':
        l['html'] = lec6_html

save_json('30565.json', d30565)
print('[OK] 30565 离散数学 基数理论深度重构与拓展标注完成')

# ==============================================================================
# 8. 修复与深化 30361 (软件工程 / Software Engineering)
# ==============================================================================
d30361 = get_base_json('30361.json')

sdlc_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.0 软件工程经济学定律：Boehm 缺陷修复成本指数曲线</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Boehm 缺陷放大模型与生命周期质量经济学</b>
<p>需求阶段缺陷蔓延至运维阶段修复成本上升 100~200 倍的经验定律与数学解释，揭示敏捷迭代与 CI/CD 快速验证闭环的本质商业动因。</p>
</div>
<p>Barry Boehm 在《Software Engineering Economics》中提出的经典经验法则揭示了缺陷潜伏的非线性成本放大效应：</p>
<table>
  <tr><th>发现并修复缺陷的阶段</th><th>相对修复成本倍数</th><th>工程机理与代价来源</th></tr>
  <tr><td>需求工程阶段（Requirements）</td><td><b>1×</b></td><td>仅需修改文字描述或线框图，耗时数分钟</td></tr>
  <tr><td>架构与详细设计（Design）</td><td><b>3× – 6×</b></td><td>需调整 UML 类图、状态机或接口签名协议</td></tr>
  <tr><td>编码阶段（Coding）</td><td><b>10×</b></td><td>需局部重构函数、调整局部数据结构与单元测试</td></tr>
  <tr><td>系统集成测试（Integration Test）</td><td><b>15× – 40×</b></td><td>需回溯排查跨模块调用链路，触发大范围回归测试</td></tr>
  <tr><td>生产环境运维（Post-Release Operations）</td><td><b>60× – 200×</b></td><td>灾难性代价：数据库脏数据清洗、客户信任丧失、紧急热修复发布</td></tr>
</table>
<p>这解释了为何现代软件工程转向敏捷迭代（Scrum）与持续集成/持续交付（CI/CD）：敏捷的核心经济学目标不是“写代码更快”，而是<b>缩短从代码产生到验证反馈的周期</b>，把缺陷发现时间点强制收敛在成本最低的编码与单元测试阶段。</p>
"""

cap_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.0 分布式系统设计的基石定理：CAP 定理的严格反证</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Gilbert & Lynch (2002) CAP 定理形式化论证</b>
<p>在异步不可靠网络下构造网络分区（Partition）实验，严格反证任何算法不可能同时满足强一致性（Linearizability）与全局可用性（Availability）。</p>
</div>
<p>2000 年 Eric Brewer 提出猜想，2002 年 Seth Gilbert 与 Nancy Lynch 给出形式化数学证明。在存在网络分区的分布式读写存储模型中：</p>
<ul>
  <li><b>强一致性（Consistency / Linearizability）</b>：任何一次读操作，必须返回最近一次写入成功的值或返回错误，所有节点状态全局一致；</li>
  <li><b>可用性（Availability）</b>：每个非故障节点接收到请求后，必须在有限时间内返回非错误的响应（不能无限等待或超时拒绝）；</li>
  <li><b>分区容错性（Partition Tolerance）</b>：网络任意丢失消息或发生分裂通信故障时，系统仍能维持运行。</li>
</ul>
<p><b>严密反证构造</b>：设分布式系统由两个独立节点 $G_1, G_2$ 组成。当物理光缆中断时，系统陷入分区状态 $P$（$G_1$ 与 $G_2$ 无法通信）：</p>
<ol>
  <li>客户端向 $G_1$ 发起写请求 <code>Write(v=1)</code>；</li>
  <li>若系统满足可用性（A），$G_1$ 必须在不能与 $G_2$ 通信的情况下单方面向客户端确认写入成功；</li>
  <li>紧接着另一个客户端向 $G_2$ 发起读请求 <code>Read()</code>；</li>
  <li>若系统满足可用性（A），$G_2$ 必须在有限时间内响应；</li>
  <li>由于网络分区断开，$G_2$ 根本不知道 $v=1$ 的发生，只能返回旧值 $v=0$。此时强一致性（C）被彻底打破！</li>
  <li>若要保住强一致性（C），$G_2$ 必须拒绝响应或阻塞超时，这又打破了可用性（A）。</li>
</ol>
<p>结论：在物理网络不可靠的客观现实下，分区容错性（P）是必然客观属性，架构师只能在 <b>CP 架构</b>（如 ZooKeeper, Raft）与 <b>AP 架构</b>（如 Cassandra, DynamoDB 最终一致性）之间做工程取舍。</p>
"""

mccabe_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.0 白盒测试复杂度度量：麦凯布圈复杂度（McCabe Cyclomatic Complexity）</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】图论欧拉示性数推导圈复杂度公式 $V(G) = E - V + 2 = \pi + 1$</b>
<p>将控制流图视为一维单纯复形，证明独立线性执行路径数量严格等于圈基维数，为判定单元测试覆盖率分支边界提供严格定量指标。</p>
</div>
<p>托马斯·麦凯布（Thomas McCabe）在 1976 年将图论拓扑学引入软件度量：程序控制流图（Control Flow Graph, CFG）的结构复杂度可以通过圈数定量衡量。</p>
<p><b>【数学公式推导】</b>：设程序的控制流图为强连通有向图 $G = (V, E)$，其中 $V$ 为指令块节点数，$E$ 为控制流转移边数。根据代数拓扑学欧拉示性数，图的独立回路数（圈复杂度）为：</p>
<p>$$V(G) = E - V + 2P$$</p>
<p>对于单入口单出口的独立函数模块（连通分支数 $P = 1$），公式简化为：</p>
<p>$$V(G) = E - V + 2$$</p>
<p><b>等价判定法则</b>：若流图中包含 $\pi$ 个二元判定节点（例如 <code>if</code>, <code>while</code>, <code>for</code>, <code>and</code>, <code>or</code> 条件），则其圈复杂度严格等于：</p>
<p>$$V(G) = \pi + 1$$</p>
<p><b>工程指导意义</b>：圈复杂度 $V(G)$ 精确对应<b>线性无关基路径集合（Basis Path Set）的大小</b>。它为白盒测试覆盖提供了数学铁律：若要实现 100% 的基本路径测试覆盖，编写的独立测试用例数量的理论下界必须严格等于 $V(G)$！若 $V(G) > 10$，函数缺陷率呈指数级上升，必须强制重构。</p>
"""

for l in d30361['lectures']:
    if l['slug'] == 'l02-sdlc-models-and-agile':
        l['html'] = inject_to_section(l['html'], 'detail', sdlc_extra)
    elif l['slug'] == 'l06-architectural-design':
        l['html'] = inject_to_section(l['html'], 'detail', cap_extra)
    elif l['slug'] == 'l07-testing-and-quality':
        l['html'] = inject_to_section(l['html'], 'detail', mccabe_extra)

save_json('30361.json', d30361)
print('[OK] 30361 软件工程 全章节深度增强与拓展标注完成')

# ==============================================================================
# 9. 扩展 30332 (工具与 AI)
# ==============================================================================
d30332 = get_base_json('30332.json')
ai_extra = r"""
<h3><span class="badge purple">拓展深化</span> 6.5 大语言模型 Transformer 架构自注意力机制（Self-Attention）与幻觉机理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】自注意力矩阵计算 $\text{softmax}(QK^T / \sqrt{d_k})V$ 与自回归生成确定性困境</b>
<p>从数学推导解释 Transformer 为何本质上是条件概率密度的自回归采样器，为什么它不具备符号逻辑演绎的保真保证，从而从数学底层理解 AI 幻觉的不可避免性及 RAG 检索增强生成的必要性。</p>
</div>
<p><b>1. 缩放点积注意力核心公式</b>：设输入词嵌入序列经线性投影生成查询矩阵 $Q$、键矩阵 $K$ 和值矩阵 $V$（维度均为 $d_k$）：</p>
<p>$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$$</p>
<p>其中除以缩放因子 $\sqrt{d_k}$ 是为了防止在维度较大时向量点积数值过大，导致 $\text{softmax}$ 函数进入导数极小的梯度饱和区。通过注意力权重矩阵，模型能够在 $O(1)$ 步内建立长距离依赖语义关联。</p>
<p><b>2. 幻觉（Hallucination）的统计学本质</b>：大语言模型在生成文本时遵循严格的自回归条件概率链式法则：$P(w_1, \dots, w_T) = \prod_{t=1}^T P(w_t \mid w_1, \dots, w_{t-1})$。模型的目标是逼近训练语料的统计分布概率，而非物理客观真理。当上下文先验缺乏严格约束时，模型倾向于采样符合语法和流畅度的高概率词串，从而造成“一本正经地胡说八道”。因此在工程落地中，必须引入 <b>RAG（检索增强生成）</b> 与 <b>CoT（思维链逻辑外挂）</b> 来约束解空间。</p>
"""
for l in d30332['lectures']:
    if l['slug'] == 'ai-in-studies':
        l['html'] = inject_to_section(l['html'], 'detail', ai_extra)
save_json('30332.json', d30332)
print('[OK] 30332 工具与 AI 拓展标注完成')

# ==============================================================================
# 10. 扩展 29911 (循环经济) 与 29913 (气候变化)
# ==============================================================================
d29911 = get_base_json('29911.json')
ce_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.5 工业生态学热力学定律：从热力学第二定律（熵增）看循环经济的物理边界</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】物质循环的热力学极限与不可逆熵增约束</b>
<p>利用热力学第二定律证明：任何材料回收与再加工过程必然伴随着能量耗散与杂质扩散（熵增）。不存在 100% 的永久闭环循环，循环经济方案必须进行完整的全生命周期评估（LCA）与㶲分析（Exergy Analysis）。</p>
</div>
<p><b>1. 物质与能量的不可逆退化</b>：根据热力学第二定律，孤立系统熵增不减 $\Delta S \ge 0$。自然界中高品质材料（低熵状态，如纯铜、结构合金）在使用过程中不可避免地发生耗散与混合（高熵状态，如合金微量元素互溶、微塑料扩散）。要将高度分散的杂质分离并提纯回初始纯度，必须输入巨大的外部有用功（㶲，Exergy），这往往导致回收过程消耗的高品位化石能源或电力反超原生开采。</p>
<p><b>2. 9R 框架的物理优先级推导</b>：为什么欧盟 9R 体系将 <b>Refuse（拒绝）与 Reuse（复用）</b> 排在 <b>Recycle（回收）</b> 之前？因为复用仅维护宏观产品形态，耗散熵最小；而物理/化学回收则彻底打碎微观结构重新冶炼，伴随着剧烈的熵增与能量二次损失。因此“循环经济不是单纯的垃圾回收”，必须从源头系统设计（Design for Disassembly）进行热力学优化。</p>
"""
for l in d29911['lectures']:
    if l['slug'] == 'c3-circular-concepts':
        l['html'] = inject_to_section(l['html'], 'detail', ce_extra)
save_json('29911.json', d29911)
print('[OK] 29911 循环经济 热力学拓展标注完成')

d29913 = get_base_json('29913.json')
climate_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.5 全球气候敏感度与辐射强迫（Radiative Forcing）对数响应模型</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】斯特藩-玻尔兹曼定律与大气温室效应非线性饱和模型</b>
<p>基于黑体辐射定律与简化的两层大气能平衡模型，推导温室气体浓度翻倍时的辐射强迫经验公式 $\Delta F = 5.35 \ln(C/C_0) \text{ W/m}^2$，揭示气候系统响应非线性与反馈机制的物理本质。</p>
</div>
<p><b>1. 地球能量平衡零维模型</b>：在热平衡态下，地球吸收的太阳短波辐射必须等于向太空辐射的长波红外辐射：</p>
<p>$$\frac{S_0}{4} (1 - \alpha) = \epsilon \sigma T_e^4$$</p>
<p>其中太阳常数 $S_0 \approx 1361 \text{ W/m}^2$，反照率 $\alpha \approx 0.3$，$\sigma$ 为斯特藩-玻尔兹曼常数。无温室气体时有效辐射温度仅为 $T_e \approx 255 \text{ K} (-18^\circ\text{C})$。正是温室效应拦截了部分出射红外线，使地表平均温度提升至舒适的 $288 \text{ K} (+15^\circ\text{C})$。</p>
<p><b>2. 对数饱和效应与气候敏感度</b>：由于二氧化碳在 $15\\,\mu\text{m}$ 的核心红外吸收带早已趋于光学饱和，新增的 $\text{CO}_2$ 主要在吸收带边缘吸收红外线。根据 IPCC 标准辐射传输模型，辐射强迫 $\Delta F$ 并不随浓度线性增长，而是遵循对数响应曲线：</p>
<p>$$\Delta F = 5.35 \ln\left( \frac{C}{C_0} \right) \quad (\text{W/m}^2)$$</p>
<p>当 $\text{CO}_2$ 浓度翻倍时（$\ln 2 \approx 0.693$），直接辐射强迫为 $\Delta F_{2\times} \approx 3.71 \text{ W/m}^2$。结合水汽正反馈与冰雪反照率正反馈，最终推导出平衡态气候敏感度（ECS）在 $2.5^\circ\text{C} \sim 4.0^\circ\text{C}$ 之间，为全球双碳目标提供了坚实的物理地球系统科学依据。</p>
"""
for l in d29913['lectures']:
    if l['slug'] == 'c2-supplemental-references':
        l['html'] = inject_to_section(l['html'], 'detail', climate_extra)
save_json('29913.json', d29913)
print('[OK] 29913 气候变化 物理模型拓展标注完成')

# ==============================================================================
# 11. 扩展 34583 (芬兰语 2)
# ==============================================================================
d34583 = get_base_json('34583.json')
fin2_extra = r"""
<h3><span class="badge purple">拓展深化</span> 7.5 芬兰语动词六大变位族（Verbit 1–6）底层词干提取算法与辅音交替逆向定理</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】动词变位词干推导与反向强弱交替的生成语言学矩阵</b>
<p>动词变位常被视为庞杂的特例记忆，但在生成语言学框架下，动词 1 型为正向交替（原形强 $\to$ 人称弱），而动词 3/4/6 型则遵循逆向交替（原形弱 $\to$ 人称强）。掌握底层词干提取算法即可统一推演所有不规则动词。</p>
</div>
<p><b>1. 动词六大族的词尾判定与词干（Vartalo）提取算法</b>：</p>
<table>
  <tr><th>动词族</th><th>原型标志词尾</th><th>人称词干提取规则</th><th>辅音交替方向</th><th>典型范式演化</th></tr>
  <tr><td><b>Verbityyppi 1</b></td><td>-V + -a/-ä（双元音结尾）</td><td>去掉末尾 -a/-ä：<code>puhu-a</code> ⟹ <code>puhu-n</code></td><td><b>正向交替</b>：原型为强级，1/2 人称音节闭合变为弱级</td><td>ottaa ⟹ otan / tietää ⟹ tiedän</td></tr>
  <tr><td><b>Verbityyppi 2</b></td><td>-da / -dä</td><td>去掉 -da/-dä：<code>syö-dä</code> ⟹ <code>syö-n</code></td><td><b>无交替</b>：词干辅音恒定保持不变</td><td>juoda ⟹ juon / tehdä ⟹ teen</td></tr>
  <tr><td><b>Verbityyppi 3</b></td><td>-la/-lä, -ra/-rä, -na/-nä, -sta/-stä</td><td>去掉尾缀补元音 <code>-e-</code>：<code>tul-la</code> ⟹ <code>tule-n</code></td><td><b>逆向交替</b>：原型同化为弱级，人称开音节还原为强级</td><td>ajatella ⟹ ajattelen / purra ⟹ puren</td></tr>
  <tr><td><b>Verbityyppi 4</b></td><td>-Vt + -a/-ä（元音+t+a）</td><td>去掉 -t- 补元音 <code>-a-/-ä-</code>：<code>hava-ta</code> ⟹ <code>havaitse-n</code></td><td><b>逆向交替</b>：原型弱级，人称强级</td><td>tavata ⟹ tapaan / luvata ⟹ lupaan</td></tr>
  <tr><td><b>Verbityyppi 5</b></td><td>-ita / -itä</td><td>去掉 -ta 补 <code>-tse-</code>：<code>tarv-ita</code> ⟹ <code>tarvitse-n</code></td><td><b>无交替</b>：词干固定添加 tse 后缀</td><td>valita ⟹ valitsen / häiritä ⟹ häiritsen</td></tr>
  <tr><td><b>Verbityyppi 6</b></td><td>-eta / -etä</td><td>去掉 -ta 补 <code>-ne-</code>：<code>lämm-etä</code> ⟹ <code>lämpene-n</code></td><td><b>逆向交替</b>：原型弱级，人称强级</td><td>kylmetä ⟹ kylmenen / paeta ⟹ pakenen</td></tr>
</table>
"""
for l in d34583['lectures']:
    if l['slug'] == 't7-verb-types-1-6':
        l['html'] = inject_to_section(l['html'], 'detail', fin2_extra)
save_json('34583.json', d34583)
print('[OK] 34583 芬兰语 2 动词音系学变位拓展标注完成')

# ==============================================================================
# 12. 扩展 30331 (软件工程专业导论 / DD Studies)
# ==============================================================================
d30331 = get_base_json('30331.json')
psp_extra = r"""
<h3><span class="badge purple">拓展深化</span> 3.5 个人软件工程过程（PSP）量化建模：PROBE 估算与代码质量缺陷密度</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】Watts Humphrey 个人软件过程（PSP）的工程量化方法论</b>
<p>大学计算机系学生从“编程爱好者”迈向“专业软件工程师”的分水岭，在于从拍脑袋估算转向基于经验数据的 PROBE 线性回归估算与缺陷注入/消除漏斗模型。</p>
</div>
<p><b>1. PROBE（Proxy Based Estimation）规模与工期估算法</b>：利用历史开发模块的规模代理（如功能点、代码行 LOC 或类方法数）建立经验回归方程 $Y = \beta_0 + \beta_1 X$。结合标准差计算 95% 置信区间预测项目工期，摆脱盲目乐观导致的死线延期崩溃。</p>
<p><b>2. 质量漏斗与缺陷密度（Defect Density）度量</b>：</p>
<ul>
  <li><b>阶段缺陷注入率</b>：统计在需求、设计、编码阶段每千行代码（KLOC）注入的缺陷数；</li>
  <li><b>评审去除效率（Review Yield）</b>：公式 $\text{Yield} = \frac{\text{评审发现的缺陷数}}{\text{评审前总潜伏缺陷数}} \times 100\%$。严格的同行桌面走查（Desk Check）能在代码编译前以极低成本消除 60%~70% 的逻辑与内存缺陷。</li>
</ul>
"""
for l in d30331['lectures']:
    if l['slug'] == 'degree-structure-psp':
        l['html'] = inject_to_section(l['html'], 'detail', psp_extra)
save_json('30331.json', d30331)
print('[OK] 30331 学习导论 PSP 工程量化拓展标注完成')

# ==============================================================================
# 13. 扩展 29428 (数字导览与学术演讲 Speaking Up)
# ==============================================================================
d29428 = get_base_json('29428.json')
toulmin_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.5 国际学术答辩与批判性沟通：图尔敏论证模型（Toulmin Model）应用</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】学术主张（Claim）与辩驳防御（Rebuttal）的数理逻辑结构</b>
<p>在欧洲大学的讨论课（Seminar）与 Thesis 答辩中，有说服力的陈述绝非主观观点的宣泄，而是遵循哲学逻辑学家 Stephen Toulmin 的六元论证结构。</p>
</div>
<p><b>图尔敏论证六要素在工程与学术答辩中的映射</b>：</p>
<ol>
  <li><b>主张（Claim）</b>：你希望听众接受的结论或设计选型（如：“系统应当选用微服务架构而非单体”）；</li>
  <li><b>数据/事实（Data / Grounds）</b>：支撑主张的客观测量指标（如：“压测数据显示并发请求量超过 50,000 QPS”）；</li>
  <li><b>保证（Warrant）</b>：连接数据与主张的底层工程原理或行业规律（如：“当单体系统的通信吞吐超过单机带宽瓶颈时，横向拆分能降低单个故障域的影响”）；</li>
  <li><b>支持（Backing）</b>：支撑保证成立的更深层权威文献或理论依据（如：“根据 Amdahl 定律与分布式系统理论基准...”）；</li>
  <li><b>限定词（Qualifier）</b>：主张成立的严密适用边界（如：“在网络延迟低于 5ms 的内网局域网集群环境下，该结论在 95% 置信度下成立”）；</li>
  <li><b>辩驳反例（Rebuttal）</b>：主动指出该主张不适用的例外边界（如：“除非系统处于极度匮乏运维算力的小微团队初创阶段”）。</li>
</ol>
"""
for l in d29428['lectures']:
    if l['slug'] == 'speaking-up':
        l['html'] = inject_to_section(l['html'], 'detail', toulmin_extra)
save_json('29428.json', d29428)
print('[OK] 29428 学术演讲 图尔敏论证模型拓展标注完成')

# ==============================================================================
# 14. 扩展 32667 (英语语音)
# ==============================================================================
d32667 = get_base_json('32667.json')
ipa_extra = r"""
<h3><span class="badge purple">拓展深化</span> 2.5 实验语音学与声学共振峰理论：F1/F2 舌位四边形与频谱感知</h3>
<div class="callout idea" data-ext="true">
<b>【拓展深化】声道滤波声学原理（Source-Filter Model）与元音共振峰解析</b>
<p>为什么母语为汉语的学生容易混淆 /i:/ 与 /ɪ/、/e/ 与 /æ/？声学语音学揭示：元音的音色本质是声带基音在咽腔和口腔构成的双共振腔中激发的共振峰频率（Formant Frequencies）。</p>
</div>
<p><b>1. 声源-滤波器模型（Source-Filter Model）</b>：声带振动提供具有丰富泛音的声源波，声道（Vocal Tract）形状充当可调谐的声学滤波器。前两个共振峰频率唯一决定元音音色：</p>
<ul>
  <li><b>第一共振峰（F1）</b>：与<b>舌位高低（Tongue Height）</b>及下颌开合度成反比。舌位越高（如 /i:/, /u:/），咽腔容积越大，F1 频率越低（约 250~300 Hz）；舌位越低（如 /ɑ:/, /æ/），开口度大，F1 频率显著升高（达 700~800 Hz）；</li>
  <li><b>第二共振峰（F2）</b>：与<b>舌位前后（Tongue Advancement）</b>成正比。前元音（如 /i:/）口腔共振腔短，F2 高达 2200~2500 Hz；后元音（如 /u:/）嘴唇圆唇向前延伸且舌后缩，F2 跌落至 800~900 Hz。</li>
</ul>
<p><b>2. 最小对立体（Minimal Pairs）的声学边界纠偏</b>：<code>sheep /ʃi:p/</code> 与 <code>ship /ʃɪp/</code> 的核心差异不仅在于发音时长（Duration），更在于 /ɪ/ 是松元音，舌位更偏央且略低，其 F1 略高而 F2 显著低于紧元音 /i:/。了解共振峰物理机制可避免单纯依赖“拉长声音”的错误发音习惯。</p>
"""
for l in d32667['lectures']:
    if l['slug'] == 'p2-vowels-consonants':
        l['html'] = inject_to_section(l['html'], 'detail', ipa_extra)
save_json('32667.json', d32667)
print('[OK] 32667 英语语音 声学共振峰拓展标注完成')

print("\n" + "="*50)
print("全站全部学科讲义深度增强、系统化拓展标注与修复大功告成！")
print("="*50)
