# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from genlib import (L, emit, h2, h3, p, ul, ol, ck, st, tb, K, cal, badge, qa, det, pre, code, chips)

LEC = []

# ============================================================ 1
LEC.append(L(
 slug='t1-parametric-curves',
 tzh='Topic 1 · 平面曲线与参数方程',
 ten='Plane Curves, Parametric Equations',
 keywords=['parametric equation', 'parameter', 'slope of a parametric curve', 'arc length', 'surface area of revolution', 'polar coordinates'],
 files=['Topic 1/EMII_Week1_Lecture1.pdf', 'Topic 1/EMII_Week1_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('HDD4020 从这里开始把「一元微积分」推向「多变量与线性代数」。第一步是换一种方式描述曲线：不再写 <code>y = f(x)</code>，而是让 x 与 y 各自成为一个参数的函数。这样圆、摆线、螺线这些「一个 x 对应两个 y」或「绕圈回来」的曲线才写得出来。')
  + p('学完本节你应当能够：')
  + ck('把常见的隐式或显式曲线写成参数方程，反之亦然',
     '对参数曲线求一阶导数 dy/dx 与二阶导数 d²y/dx²',
     '用积分公式求参数曲线的弧长',
     '用积分公式求旋转曲面的面积',
     '在直角坐标与极坐标之间互相转换')),
 detail=(h3('1.1 什么是参数方程')
  + p('若曲线上每一点 (x, y) 都可由一个变量 t 单独决定：<code>x = x(t)</code>、<code>y = y(t)</code>，则称这组式子是曲线的<b>参数方程</b>（parametric equations），t 称为<b>参数</b>（parameter）。t 通常被理解为时间，曲线就是质点运动的轨迹。')
  + p('与显式 <code>y = f(x)</code> 相比，参数方程的优势是<b>没有垂直方向上的限制</b>：一个 x 可以对应两个 y（如圆），曲线可以自交，也可以绕回。代价是每个量都多了一层 t，求导与积分都要用链式法则。')
  + h3('1.2 常见曲线的参数化')
  + tb(('曲线', '参数方程', '参数范围'),
       ('圆 x²+y²=r²', '<code>x = r cos t, y = r sin t</code>', '0 ≤ t ≤ 2π'),
       ('椭圆 x²/a²+y²/b²=1', '<code>x = a cos t, y = b sin t</code>', '0 ≤ t ≤ 2π'),
       ('抛物线 y = x²', '<code>x = t, y = t²</code>', 't ∈ ℝ'),
       ('摆线 cycloid', '<code>x = a(t − sin t), y = a(1 − cos t)</code>', 't ∈ ℝ'),
       ('螺线 spiral', '<code>x = t cos t, y = t sin t</code>', 't ≥ 0'))
  + cal('tip', '检验技巧', '把参数方程里的 t 消去，若能得到原来的直角坐标方程，说明参数化正确。圆的例子：<code>cos²t + sin²t = 1</code> → <code>(x/r)² + (y/r)² = 1</code>。')
  + h3('1.3 参数曲线的斜率')
  + p('由链式法则 <code>dy/dt = (dy/dx)(dx/dt)</code>，所以')
  + p('<b><code>dy/dx = (dy/dt) / (dx/dt)</code></b>，要求 <code>dx/dt ≠ 0</code>。')
  + p('这一步是整节的核心。它把「对 x 求导」换成两个「对 t 求导」的商。若 <code>dx/dt = 0</code> 而 <code>dy/dt ≠ 0</code>，切线竖直，斜率不存在；若两者同时为 0，则是奇点（singular point），需要单独讨论。')
  + p('二阶导数不能直接对一阶导数再除一次，必须写成：')
  + p('<b><code>d²y/dx² = (d/dt)[dy/dx] / (dx/dt)</code></b>')
  + cal('warn', '高频错误', '写成 <code>(d²y/dt²)/(d²x/dt²)</code> 是错的。正确做法是先把 dy/dx 当成 t 的函数求导，再除以 dx/dt。')
  + h3('1.4 弧长')
  + p('把曲线切成无数小段，每段长 <code>√((dx)² + (dy)²) = √(x′(t)² + y′(t)²) dt</code>，累加得：')
  + p('<b><code>L = ∫[α,β] √(x′(t)² + y′(t)²) dt</code></b>')
  + p('要求曲线光滑（x′、y′ 连续且不同时为零），并且每个点只被走一次，否则会把重叠段重复计入。')
  + h3('1.5 旋转曲面面积')
  + p('把曲线绕 x 轴旋转，微元是一段圆台，侧面积 <code>2π|y| ds</code>，其中 <code>ds = √(x′² + y′²) dt</code>。于是')
  + p('<b><code>S = 2π ∫[α,β] |y(t)| √(x′(t)² + y′(t)²) dt</code></b>')
  + p('绕 y 轴旋转则把 <code>|y|</code> 换成 <code>|x|</code>。绝对值不能省，因为半径必须非负。')
  + h3('1.6 极坐标入门')
  + p('用「到原点的距离 r」与「与极轴的夹角 θ」定位：<code>x = r cos θ</code>、<code>y = r sin θ</code>；反向 <code>r² = x² + y²</code>、<code>tan θ = y/x</code>（注意象限）。')
  + p('极坐标下的弧长微元是 <code>ds = √(r² + (dr/dθ)²) dθ</code>，扇区面积微元是 <code>dA = ½ r² dθ</code>，所以')
  + p('<b><code>A = ½ ∫[α,β] r(θ)² dθ</code></b>'),
 kws=K(('parametric equation', '参数方程', 'A pair of equations x = x(t), y = y(t) describing a curve.'),
       ('parameter', '参数', 'The variable t that drives both x and y.'),
       ('eliminate the parameter', '消参', 'Eliminate t to obtain a Cartesian equation.'),
       ('slope of a parametric curve', '参数曲线斜率', 'dy/dx = (dy/dt)/(dx/dt).'),
       ('arc length', '弧长', 'L = ∫ √(x′² + y′²) dt.'),
       ('surface of revolution', '旋转曲面', 'Rotating a curve about an axis sweeps out a surface.'),
       ('polar coordinates', '极坐标', 'x = r cos θ, y = r sin θ.'),
       ('smooth curve', '光滑曲线', 'x′ and y′ are continuous and never simultaneously zero.')),
 examples=(qa('例 1　求圆 x = 2cos t, y = 2sin t 在 t = π/4 处的切线斜率。',
   p('x′ = −2sin t，y′ = 2cos t。dy/dx = (2cos t)/(−2sin t) = −cot t。t = π/4 时得 −1。')
   + p('检验：该点为 (√2, √2)，圆在该点的切线斜率确实是 −x/y = −1。'))
  + qa('例 2　求摆线 x = t − sin t, y = 1 − cos t 在 0 ≤ t ≤ 2π 上的弧长（a = 1）。',
   p('x′ = 1 − cos t，y′ = sin t。<code>x′² + y′² = (1−cos t)² + sin²t = 2 − 2cos t = 4 sin²(t/2)</code>。')
   + p('故 <code>√(x′²+y′²) = 2 sin(t/2)</code>（t ∈ [0,2π] 时 sin(t/2) ≥ 0，无需绝对值）。')
   + p('<code>L = ∫[0,2π] 2 sin(t/2) dt = [−4 cos(t/2)]₀^{2π} = −4(−1) + 4(1) = 8</code>。')
   + p('这是一个经典结论：标准摆线一拱的弧长恰为 8a。'))
  + qa('例 3　把 r = 2cos θ 化成直角坐标方程。',
   p('两边乘 r：<code>r² = 2r cos θ</code>。代 <code>r² = x²+y²</code>、<code>r cos θ = x</code> 得 <code>x² + y² = 2x</code>，即 <code>(x−1)² + y² = 1</code>。')
   + p('所以它是一个圆心 (1,0)、半径 1 的圆。这类「r = 常数 × cos θ」必是过原点的圆。'))),
 practice=(ol('把 <code>x = 3cos t, y = 3sin t</code> 在 t = π/3 处的切线方程写出来。',
        '求 <code>x = t², y = t³</code> 的 d²y/dx²。',
        '求 <code>x = e^t cos t, y = e^t sin t</code> 从 t = 0 到 t = π 的弧长。',
        '求 <code>r = 1 + cos θ</code>（心形线）围成的面积。')
  + det('答案与思路',
   p('<b>1.</b> x′ = −3sin t，y′ = 3cos t，dy/dx = −cot t。t = π/3 时斜率 = −1/√3。点为 (3/2, 3√3/2)。切线：<code>y − 3√3/2 = −(1/√3)(x − 3/2)</code>。')
   + p('<b>2.</b> dy/dx = (3t²)/(2t) = 3t/2。再对 t 求导得 3/2，除以 dx/dt = 2t，得 <code>d²y/dx² = 3/(4t)</code>。')
   + p('<b>3.</b> x′ = e^t(cos t − sin t)，y′ = e^t(sin t + cos t)，平方和 = 2e^{2t}。故 <code>L = ∫₀^π √2 e^t dt = √2(e^π − 1)</code>。')
   + p('<b>4.</b> <code>A = ½∫₀^{2π}(1+cos θ)² dθ = ½∫(1 + 2cos θ + cos²θ)dθ</code>。cos θ 一项积分为 0，cos²θ 平均值为 ½，故 <code>A = ½(2π + π) = 3π/2</code>。')),
 exam=(p(badge('bad', '必考') + '参数曲线的 dy/dx、弧长积分、极坐标面积；把直角坐标方程参数化。')
  + p(badge('warn', '易错 1') + '<b>二阶导数公式写错</b>。必须是 <code>(d/dt)(dy/dx) ÷ (dx/dt)</code>，不是两个二阶导相除。')
  + p(badge('warn', '易错 2') + '<b>弧长公式里漏绝对值或漏平方</b>。<code>√(x′² + y′²)</code> 不是 <code>x′ + y′</code>；旋转面积要 <code>|y|</code>。')
  + p(badge('mute', '进阶') + '摆线、心形线、双纽线这类经典曲线的弧长与面积结论建议记住，考试常直接引用以节省时间。')),
 checklist=(h2('解题方法清单')
  + h3('求参数曲线的一切量')
  + st('写出 x(t)、y(t)，求 x′、y′',
       '斜率：dy/dx = y′/x′；若 x′ = 0 则判竖直',
       '二阶导：先把 dy/dx 化简成 t 的函数，再对 t 求导并除以 x′',
       '弧长：算 x′² + y′²，尽量化简成完全平方再开方',
       '旋转面积：在弧长被积函数前乘 2π|y|（绕 y 轴则乘 2π|x|）',
       '定积分上下限对应曲线起止点的 t 值，不要写成 x 的范围')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 1/EMII_Week1_Lecture1.pdf', '全篇', '平面曲线、参数方程定义、常见曲线参数化'),
   ('Topic 1/EMII_Week1_Lecture2.pdf', '全篇', '参数曲线斜率、弧长、旋转曲面面积、极坐标引入'),
   ('（补充）', '—', '二阶导数公式的推导与奇点讨论属于衔接性补充，原课件只给结论'))))

# ============================================================ 2
LEC.append(L(
 slug='t2-coordinate-systems',
 tzh='Topic 2 · 柱坐标与球坐标',
 ten='Cylindrical and Spherical Coordinates',
 keywords=['cylindrical coordinates', 'spherical coordinates', 'coordinate surface', 'Jacobian', 'volume element'],
 files=['Topic 2/EMII_Week2_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('平面上用极坐标，空间中就用柱坐标与球坐标。它们的共同思路是：<b>把「距离」与「角度」分开算</b>，让具有旋转对称性的曲面（圆柱、球、圆锥）写成极简单的方程。')
  + p('学完本节你应当能够：')
  + ck('在直角、柱、球三种坐标之间自由互换',
     '把常见曲面（柱面、球面、锥面）写成最简坐标方程',
     '写出三种坐标下的体积微元',
     '判断一道三重积分题该用哪种坐标')),
 detail=(h3('2.1 柱坐标 cylindrical coordinates')
  + p('在极坐标 (r, θ) 上直接加一个高度 z：')
  + p('<b><code>x = r cos θ, y = r sin θ, z = z</code></b>')
  + p('反变换：<code>r = √(x²+y²)</code>，<code>θ = arctan2(y, x)</code>，<code>z = z</code>。范围一般取 <code>r ≥ 0</code>、<code>0 ≤ θ &lt; 2π</code>、<code>z ∈ ℝ</code>（z 就是高度，可负）。')
  + p('柱坐标的坐标面（coordinate surfaces）：<code>r = 常数</code> 是圆柱面，<code>θ = 常数</code> 是过 z 轴的半平面，<code>z = 常数</code> 是水平平面。')
  + p('体积微元：<code>dV = r dr dθ dz</code>。那个多出的 r 是雅可比行列式（Jacobian）的绝对值，来源是极坐标面积微元 <code>r dr dθ</code>。')
  + h3('2.2 球坐标 spherical coordinates')
  + p('用「到原点的距离 ρ」与两个角度定位：')
  + p('<b><code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code></b>')
  + p('其中 <code>ρ ≥ 0</code> 是径向距离，<code>φ ∈ [0, π]</code> 是<b>与正 z 轴的夹角</b>（极角 / polar angle），<code>θ ∈ [0, 2π)</code> 是方位角（azimuthal angle）。')
  + cal('warn', '最容易错的一点', 'φ 是从 <b>z 轴</b> 量起的，不是从 xy 平面。所以 <code>z = ρ cos φ</code>，而 <code>r = ρ sin φ</code>。把 φ 与「与 xy 平面的夹角」弄反，整个公式全错。')
  + p('反变换：<code>ρ = √(x²+y²+z²)</code>，<code>cos φ = z/ρ</code>，<code>tan θ = y/x</code>。')
  + p('体积微元：<code>dV = ρ² sin φ dρ dφ dθ</code>。两个因子 ρ² 与 sin φ 缺一不可。')
  + h3('2.3 三种坐标下的典型曲面')
  + tb(('曲面', '直角坐标', '柱坐标', '球坐标'),
       ('圆柱面', 'x²+y² = a²', 'r = a', 'ρ sin φ = a'),
       ('球面', 'x²+y²+z² = a²', 'r²+z² = a²', 'ρ = a'),
       ('锥面（顶角 2α）', 'z² = k²(x²+y²)', 'z = kr', 'φ = α'),
       ('水平平面', 'z = c', 'z = c', 'ρ cos φ = c'),
       ('过 z 轴的半平面', 'y = x tan θ₀', 'θ = θ₀', 'θ = θ₀'))
  + cal('tip', '选题口诀', '球面或锥面 → 球坐标；圆柱面或绕 z 轴的对称 → 柱坐标；平面直角边界（长方体）→ 直角坐标。选对坐标能把三重积分降成一次单重积分。'),
 kws=K(('cylindrical coordinates', '柱坐标', 'x = r cos θ, y = r sin θ, z = z.'),
       ('spherical coordinates', '球坐标', 'x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ.'),
       ('polar angle', '极角 φ', 'The angle measured from the positive z-axis.'),
       ('azimuthal angle', '方位角 θ', 'The angle measured in the xy-plane from the positive x-axis.'),
       ('coordinate surface', '坐标面', 'r = const, θ = const, z = const.'),
       ('Jacobian', '雅可比', 'The factor r (or ρ² sin φ) in the volume element.'),
       ('volume element', '体积微元', 'dV = r dr dθ dz or dV = ρ² sin φ dρ dφ dθ.')),
 examples=(qa('例 1　把点 P(1, √3, 2) 从直角坐标换成柱坐标与球坐标。',
   p('柱坐标：<code>r = √(1+3) = 2</code>，<code>θ = arctan(√3/1) = π/3</code>（第一象限），<code>z = 2</code>。所以 (2, π/3, 2)。')
   + p('球坐标：<code>ρ = √(1+3+4) = 2√2</code>，<code>cos φ = z/ρ = 2/(2√2) = 1/√2</code> 得 <code>φ = π/4</code>，<code>θ = π/3</code>。')
   + p('检验：<code>ρ sin φ = 2√2 · 1/√2 = 2 = r</code> ✓。'))
  + qa('例 2　把 x² + y² + z² = 4z 化为球坐标方程，并说出它是什么曲面。',
   p('代入 <code>x²+y²+z² = ρ²</code>、<code>z = ρ cos φ</code>，得 <code>ρ² = 4ρ cos φ</code>。')
   + p('<code>ρ = 0</code> 是原点，其余点约去 ρ：<code>ρ = 4cos φ</code>。')
   + p('它是球心 (0,0,2)、半径 2 的球面（把原式配方：<code>x²+y²+(z−2)² = 4</code>）。'))),
 practice=(ol('把 <code>z = x² + y²</code> 化为柱坐标方程。',
        '求球坐标下 <code>φ = π/3</code> 对应的直角坐标曲面。',
        '把 <code>r = 2cos θ</code>（柱坐标）写成直角坐标方程。',
        '半径为 2 的球体内，用球坐标写出体积积分式（不需求值）。')
  + det('答案与思路',
   p('<b>1.</b> <code>z = r²</code>。这是一个开口向上的旋转抛物面。')
   + p('<b>2.</b> <code>cos φ = 1/2</code>，由 <code>z = ρ cos φ</code>、<code>r = ρ sin φ</code> 得 <code>z = r/√3</code>，平方得 <code>z² = (x²+y²)/3</code>，即顶角 60° 的锥面。')
   + p('<b>3.</b> 两边乘 r 得 <code>r² = 2r cos θ</code>，即 <code>x²+y² = 2x</code>，即 <code>(x−1)²+y² = 1</code>，一个圆柱面。')
   + p('<b>4.</b> <code>∫₀^{2π}∫₀^{π}∫₀^{2} ρ² sin φ dρ dφ dθ</code>。')),
 exam=(p(badge('bad', '必考') + '三种坐标的互换、把曲面写成最简坐标方程、写对体积微元。')
  + p(badge('warn', '易错 1') + '<b>球坐标 φ 的起算轴弄反</b>。φ 从 z 轴量起，<code>z = ρcos φ</code>。')
  + p(badge('warn', '易错 2') + '<b>漏写雅可比因子</b>。柱坐标漏 r、球坐标漏 ρ²sin φ，积分值会差一个量级。')
  + p(badge('warn', '易错 3') + '<b>θ 象限判断错</b>。用 <code>arctan(y/x)</code> 只给主值，x &lt; 0 时要加 π。')
  + p(badge('mute', '进阶') + '球坐标下「锥面 φ = α + 球面 ρ = a」围成的区域，俗称冰淇淋筒形区域，是三重积分最常见的考题。')),
 checklist=(h2('坐标转换清单')
  + st('先算 ρ（或 r），再算角，最后算 z（或 φ）',
       '判断 θ 所在象限：看 x、y 的符号',
       '球坐标用 <code>cos φ = z/ρ</code> 比用 sin 更稳（不会有符号歧义）',
       '写体积微元前先确认用什么坐标，把雅可比因子一并写上',
       '化简曲面方程时注意 ρ = 0 的点，必要时单独讨论')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture1.pdf', '全篇', '柱坐标、球坐标定义与互换、坐标面、体积微元'),
   ('（补充）', '—', '三种坐标选择口诀与冰淇淋筒形区域说法为衔接性补充'))))

# ============================================================ 3
LEC.append(L(
 slug='t2-matrices',
 tzh='Topic 2 · 矩阵、运算与线性变换',
 ten='Matrices, Operations on Matrices, Special Matrices, and Transformations',
 keywords=['matrix', 'entry', 'matrix multiplication', 'transpose', 'identity matrix', 'inverse', 'linear transformation'],
 files=['Topic 2/EMII_Week2_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('矩阵是把「一组线性关系」写成一张表。它既是方程组的紧凑写法，也是线性变换（旋转、缩放、投影）的坐标表示。本节先把矩阵当数据结构定清楚，再学四种基本运算，最后把它当「函数」用。')
  + p('学完本节你应当能够：')
  + ck('说出矩阵的阶、元素、行、列、主对角线',
     '做加法、数乘、乘法、转置，并判断哪些运算合法',
     '识别单位阵、零阵、对角阵、三角阵、对称阵',
     '把平面/空间的线性变换写成矩阵并作用于向量')),
 detail=(h3('3.1 矩阵的定义与记号')
  + p('一个 <b>m × n</b> 矩阵是 m 行 n 列的数表，元素记 <code>a_ij</code>（第 i 行第 j 列）。行数与列数相等时称<b>方阵</b>（square matrix），方阵从左上到右下的一排元素称<b>主对角线</b>（main diagonal）。')
  + p('两个矩阵相等当且仅当阶相同且每个对应元素相等——这一条是解矩阵方程的基本工具。')
  + h3('3.2 加法与数乘')
  + p('加法：同阶矩阵对应元素相加。数乘：每个元素乘以该数。两者合起来说明矩阵构成一个向量空间。')
  + p('两条必记性质：<code>A + B = B + A</code>（交换），<code>A(BC) = (AB)C</code>（乘法结合，前提是阶数能乘）。')
  + h3('3.3 矩阵乘法')
  + p('若 A 是 <b>m × p</b>、B 是 <b>p × n</b>，则 AB 是 <b>m × n</b>，且')
  + p('<b><code>(AB)_ij = Σ_{k=1..p} a_ik · b_kj</code></b>')
  + p('口诀：<b>「行乘列，加起来」</b>。左矩阵取一行，右矩阵取一列，对应元素相乘再求和。')
  + cal('warn', '三条打破直觉的性质', '(1) <code>AB ≠ BA</code>，乘法不交换；(2) <code>AB = 0</code> 不能推出 A = 0 或 B = 0；(3) <code>AB = AC</code> 且 A ≠ 0 也不能约去 A。这三条是选择题的高频陷阱。')
  + p('运算律中成立的部分：<code>A(BC) = (AB)C</code>、<code>A(B+C) = AB+AC</code>、<code>(A+B)C = AC+BC</code>、<code>(AB)ᵀ = BᵀAᵀ</code>（注意顺序颠倒）。')
  + h3('3.4 特殊矩阵')
  + tb(('名称', '特征', '作用'),
       ('零阵 O', '所有元素为 0', '加法单位元'),
       ('单位阵 I', '主对角为 1，其余 0', '<code>AI = IA = A</code>'),
       ('对角阵 diag(d₁…dₙ)', '非主对角均为 0', '相当于各方向分别缩放'),
       ('上/下三角阵', '对角线一侧全为 0', '行列式等于对角线乘积'),
       ('对称阵', '<code>Aᵀ = A</code>', '可正交对角化'),
       ('反对称阵', '<code>Aᵀ = −A</code>', '主对角必为 0'))
  + h3('3.5 线性变换')
  + p('矩阵作用于向量：<code>A x</code> 得到新向量。几何上：')
  + ul('<b>缩放</b>：<code>diag(s₁, s₂)</code> 把 (x,y) 变为 (s₁x, s₂y)',
      '<b>旋转 θ</b>：<code>[[cos θ, −sin θ],[sin θ, cos θ]]</code>',
      '<b>关于 x 轴反射</b>：<code>[[1,0],[0,−1]]</code>',
      '<b>关于 y = x 反射</b>：<code>[[0,1],[1,0]]</code>',
      '<b>投影到 x 轴</b>：<code>[[1,0],[0,0]]</code>')
  + p('判别技巧：看基向量 e₁ = (1,0)、e₂ = (0,1) 被送到哪里，那两列就是矩阵的两列。'),
 kws=K(('matrix', '矩阵', 'A rectangular array of numbers.'),
       ('order / dimension', '阶', 'An m × n matrix has m rows and n columns.'),
       ('entry / element', '元素', 'a_ij denotes the entry in row i, column j.'),
       ('transpose', '转置', '(Aᵀ)_ij = a_ji.'),
       ('identity matrix', '单位阵', 'The matrix I with ones on the diagonal.'),
       ('singular / non-singular', '奇异 / 非奇异', 'A singular matrix has no inverse.'),
       ('linear transformation', '线性变换', 'A map x ↦ Ax.'),
       ('rotation matrix', '旋转矩阵', '[[cos θ, −sin θ],[sin θ, cos θ]].')),
 examples=(qa('例 1　A = [[1,2],[3,4]]，B = [[0,1],[1,0]]，求 AB 与 BA。',
   p('AB = [[1·0+2·1, 1·1+2·0],[3·0+4·1, 3·1+4·0]] = [[2,1],[4,3]]。')
   + p('BA = [[0·1+1·3, 0·2+1·4],[1·1+0·3, 1·2+0·4]] = [[3,4],[1,2]]。')
   + p('结论：AB ≠ BA，乘法的不可交换性具体可见。注意 B 只是一个「交换 x 与 y」的变换。'))
  + qa('例 2　证明 AB = 0 但 A、B 均非零。',
   p('取 A = [[1,0],[0,0]]，B = [[0,0],[1,0]]。AB = [[0,0],[0,0]]。')
   + p('几何解释：A 把一切投影到 x 轴，B 把 y 轴方向映射到 x 轴之外…… 具体地说 B 的输出只有 y 分量，而 A 把 y 分量全部丢弃，故复合为零。'))
  + qa('例 3　求把平面绕原点逆时针旋转 90° 的矩阵，并作用于 (2, 3)。',
   p('θ = π/2：<code>cos = 0, sin = 1</code>，矩阵 <code>R = [[0,−1],[1,0]]</code>。')
   + p('<code>R(2,3)ᵀ = (0·2 + (−1)·3, 1·2 + 0·3)ᵀ = (−3, 2)ᵀ</code>。检验：长度仍为 √13 ✓。'))),
 practice=(ol('A 是 2×3，B 是 3×4，AB 是什么阶？BA 能乘吗？',
        '求 <code>[[1,2],[3,4]]</code> 的转置，并验证它是否对称。',
        '设 A = [[2,1],[1,2]]，求 <code>A² − 4A + 3I</code>。',
        '写出「关于 y 轴反射」的矩阵。')
  + det('答案与思路',
   p('<b>1.</b> AB 是 2×4。BA 需要 B 的列数 4 等于 A 的行数 2，不成立，不能乘。')
   + p('<b>2.</b> 转置为 <code>[[1,3],[2,4]]</code>，与原矩阵不等，不对称。注意 <code>[[1,2],[2,1]]</code> 才是对称的。')
   + p('<b>3.</b> <code>A² = [[5,4],[4,5]]</code>；<code>4A = [[8,4],[4,8]]</code>；<code>3I = [[3,0],[0,3]]</code>。相加减得 <code>[[0,0],[0,0]]</code>。这正说明 A 满足自己的特征方程 <code>λ² − 4λ + 3 = 0</code>。')
   + p('<b>4.</b> e₁ = (1,0) → (−1,0)，e₂ → (0,1)，所以矩阵 <code>[[−1,0],[0,1]]</code>。')),
 exam=(p(badge('bad', '必考') + '矩阵乘法（尤其阶数检查与顺序）、转置性质、线性变换矩阵的构造。')
  + p(badge('warn', '易错 1') + '把 <code>(AB)ᵀ</code> 写成 <code>AᵀBᵀ</code>。正确是 <code>BᵀAᵀ</code>。')
  + p(badge('warn', '易错 2') + '乘法时行列对错位。建议先写出结果矩阵的阶，再逐个格子算。')
  + p(badge('warn', '易错 3') + '以为 <code>AB = 0</code> 能推出 A 或 B 为零。')
  + p(badge('mute', '进阶') + '旋转矩阵的行列式为 1，反射矩阵为 −1，这是判断「保向还是反向」的快捷方法。')),
 checklist=(h2('矩阵运算检查清单')
  + st('先写阶：确认 m×p 与 p×n 能乘，结果 m×n',
       '算每个元素前，把左矩阵第 i 行与右矩阵第 j 列并排写在草稿上',
       '逐项乘加，不要跳项；p 较大时分两遍验算',
       '涉及转置时，先把括号顺序倒过来再展开',
       '用单位阵 I 做自检：<code>AI</code> 应该还等于 A')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture2.pdf', '全篇', '矩阵定义、加法与数乘、乘法、特殊矩阵、线性变换'),
   ('（补充）', '—', '旋转/反射/投影矩阵的具体形式与「看基向量」技巧为补充'))))

# ============================================================ 2
LEC.append(L(
 slug='t2-coordinate-systems',
 tzh='Topic 2 · 柱坐标与球坐标',
 ten='Cylindrical and Spherical Coordinates',
 keywords=['cylindrical coordinates', 'spherical coordinates', 'coordinate surface', 'Jacobian', 'volume element'],
 files=['Topic 2/EMII_Week2_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('平面上用极坐标，空间中就用柱坐标与球坐标。它们的共同思路是：<b>把「距离」与「角度」分开算</b>，让具有旋转对称性的曲面（圆柱、球、圆锥）写成极简单的方程。')
  + p('学完本节你应当能够：')
  + ck('在直角、柱、球三种坐标之间自由互换',
     '把常见曲面（柱面、球面、锥面）写成最简坐标方程',
     '写出三种坐标下的体积微元',
     '判断一道三重积分题该用哪种坐标')),
 detail=(h3('2.1 柱坐标 cylindrical coordinates')
  + p('在极坐标 (r, θ) 上直接加一个高度 z：')
  + p('<b><code>x = r cos θ, y = r sin θ, z = z</code></b>')
  + p('反变换：<code>r = √(x²+y²)</code>，<code>θ = arctan2(y, x)</code>，<code>z = z</code>。范围一般取 <code>r ≥ 0</code>、<code>0 ≤ θ &lt; 2π</code>、<code>z ∈ ℝ</code>（z 就是高度，可负）。')
  + p('柱坐标的坐标面（coordinate surfaces）：<code>r = 常数</code> 是圆柱面，<code>θ = 常数</code> 是过 z 轴的半平面，<code>z = 常数</code> 是水平平面。')
  + p('体积微元：<code>dV = r dr dθ dz</code>。那个多出的 r 是雅可比行列式（Jacobian）的绝对值，来源是极坐标面积微元 <code>r dr dθ</code>。')
  + h3('2.2 球坐标 spherical coordinates')
  + p('用「到原点的距离 ρ」与两个角度定位：')
  + p('<b><code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code></b>')
  + p('其中 <code>ρ ≥ 0</code> 是径向距离，<code>φ ∈ [0, π]</code> 是<b>与正 z 轴的夹角</b>（极角 / polar angle），<code>θ ∈ [0, 2π)</code> 是方位角（azimuthal angle）。')
  + cal('warn', '最容易错的一点', 'φ 是从 <b>z 轴</b> 量起的，不是从 xy 平面。所以 <code>z = ρ cos φ</code>，而 <code>r = ρ sin φ</code>。把 φ 与「与 xy 平面的夹角」弄反，整个公式全错。')
  + p('反变换：<code>ρ = √(x²+y²+z²)</code>，<code>cos φ = z/ρ</code>，<code>tan θ = y/x</code>。')
  + p('体积微元：<code>dV = ρ² sin φ dρ dφ dθ</code>。两个因子 ρ² 与 sin φ 缺一不可。')
  + h3('2.3 三种坐标下的典型曲面')
  + tb(('曲面', '直角坐标', '柱坐标', '球坐标'),
       ('圆柱面', 'x²+y² = a²', 'r = a', 'ρ sin φ = a'),
       ('球面', 'x²+y²+z² = a²', 'r²+z² = a²', 'ρ = a'),
       ('锥面（顶角 2α）', 'z² = k²(x²+y²)', 'z = kr', 'φ = α'),
       ('水平平面', 'z = c', 'z = c', 'ρ cos φ = c'),
       ('过 z 轴的半平面', 'y = x tan θ₀', 'θ = θ₀', 'θ = θ₀'))
  + cal('tip', '选题口诀', '球面或锥面 → 球坐标；圆柱面或绕 z 轴的对称 → 柱坐标；平面直角边界（长方体）→ 直角坐标。选对坐标能把三重积分降成一次单重积分。'),
 kws=K(('cylindrical coordinates', '柱坐标', 'x = r cos θ, y = r sin θ, z = z.'),
       ('spherical coordinates', '球坐标', 'x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ.'),
       ('polar angle', '极角 φ', 'The angle measured from the positive z-axis.'),
       ('azimuthal angle', '方位角 θ', 'The angle measured in the xy-plane from the positive x-axis.'),
       ('coordinate surface', '坐标面', 'r = const, θ = const, z = const.'),
       ('Jacobian', '雅可比', 'The factor r (or ρ² sin φ) in the volume element.'),
       ('volume element', '体积微元', 'dV = r dr dθ dz or dV = ρ² sin φ dρ dφ dθ.')),
 examples=(qa('例 1　把点 P(1, √3, 2) 从直角坐标换成柱坐标与球坐标。',
   p('柱坐标：<code>r = √(1+3) = 2</code>，<code>θ = arctan(√3/1) = π/3</code>（第一象限），<code>z = 2</code>。所以 (2, π/3, 2)。')
   + p('球坐标：<code>ρ = √(1+3+4) = 2√2</code>，<code>cos φ = z/ρ = 2/(2√2) = 1/√2</code> 得 <code>φ = π/4</code>，<code>θ = π/3</code>。')
   + p('检验：<code>ρ sin φ = 2√2 · 1/√2 = 2 = r</code> ✓。'))
  + qa('例 2　把 x² + y² + z² = 4z 化为球坐标方程，并说出它是什么曲面。',
   p('代入 <code>x²+y²+z² = ρ²</code>、<code>z = ρ cos φ</code>，得 <code>ρ² = 4ρ cos φ</code>。')
   + p('<code>ρ = 0</code> 是原点，其余点约去 ρ：<code>ρ = 4cos φ</code>。')
   + p('它是球心 (0,0,2)、半径 2 的球面（把原式配方：<code>x²+y²+(z−2)² = 4</code>）。'))),
 practice=(ol('把 <code>z = x² + y²</code> 化为柱坐标方程。',
        '求球坐标下 <code>φ = π/3</code> 对应的直角坐标曲面。',
        '把 <code>r = 2cos θ</code>（柱坐标）写成直角坐标方程。',
        '半径为 2 的球体内，用球坐标写出体积积分式（不需求值）。')
  + det('答案与思路',
   p('<b>1.</b> <code>z = r²</code>。这是一个开口向上的旋转抛物面。')
   + p('<b>2.</b> <code>cos φ = 1/2</code>，由 <code>z = ρ cos φ</code>、<code>r = ρ sin φ</code> 得 <code>z = r/√3</code>，平方得 <code>z² = (x²+y²)/3</code>，即顶角 60° 的锥面。')
   + p('<b>3.</b> 两边乘 r 得 <code>r² = 2r cos θ</code>，即 <code>x²+y² = 2x</code>，即 <code>(x−1)²+y² = 1</code>，一个圆柱面。')
   + p('<b>4.</b> <code>∫₀^{2π}∫₀^{π}∫₀^{2} ρ² sin φ dρ dφ dθ</code>。')),
 exam=(p(badge('bad', '必考') + '三种坐标的互换、把曲面写成最简坐标方程、写对体积微元。')
  + p(badge('warn', '易错 1') + '<b>球坐标 φ 的起算轴弄反</b>。φ 从 z 轴量起，<code>z = ρcos φ</code>。')
  + p(badge('warn', '易错 2') + '<b>漏写雅可比因子</b>。柱坐标漏 r、球坐标漏 ρ²sin φ，积分值会差一个量级。')
  + p(badge('warn', '易错 3') + '<b>θ 象限判断错</b>。用 <code>arctan(y/x)</code> 只给主值，x &lt; 0 时要加 π。')
  + p(badge('mute', '进阶') + '球坐标下「锥面 φ = α + 球面 ρ = a」围成的区域，俗称冰淇淋筒形区域，是三重积分最常见的考题。')),
 checklist=(h2('坐标转换清单')
  + st('先算 ρ（或 r），再算角，最后算 z（或 φ）',
       '判断 θ 所在象限：看 x、y 的符号',
       '球坐标用 <code>cos φ = z/ρ</code> 比用 sin 更稳（不会有符号歧义）',
       '写体积微元前先确认用什么坐标，把雅可比因子一并写上',
       '化简曲面方程时注意 ρ = 0 的点，必要时单独讨论')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture1.pdf', '全篇', '柱坐标、球坐标定义与互换、坐标面、体积微元'),
   ('（补充）', '—', '三种坐标选择口诀与冰淇淋筒形区域说法为衔接性补充'))))

# ============================================================ 3
LEC.append(L(
 slug='t2-matrices',
 tzh='Topic 2 · 矩阵、运算与线性变换',
 ten='Matrices, Operations on Matrices, Special Matrices, and Transformations',
 keywords=['matrix', 'entry', 'matrix multiplication', 'transpose', 'identity matrix', 'inverse', 'linear transformation'],
 files=['Topic 2/EMII_Week2_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('矩阵是把「一组线性关系」写成一张表。它既是方程组的紧凑写法，也是线性变换（旋转、缩放、投影）的坐标表示。本节先把矩阵当数据结构定清楚，再学四种基本运算，最后把它当「函数」用。')
  + p('学完本节你应当能够：')
  + ck('说出矩阵的阶、元素、行、列、主对角线',
     '做加法、数乘、乘法、转置，并判断哪些运算合法',
     '识别单位阵、零阵、对角阵、三角阵、对称阵',
     '把平面/空间的线性变换写成矩阵并作用于向量')),
 detail=(h3('3.1 矩阵的定义与记号')
  + p('一个 <b>m × n</b> 矩阵是 m 行 n 列的数表，元素记 <code>a_ij</code>（第 i 行第 j 列）。行数与列数相等时称<b>方阵</b>（square matrix），方阵从左上到右下的一排元素称<b>主对角线</b>（main diagonal）。')
  + p('两个矩阵相等当且仅当阶相同且每个对应元素相等——这一条是解矩阵方程的基本工具。')
  + h3('3.2 加法与数乘')
  + p('加法：同阶矩阵对应元素相加。数乘：每个元素乘以该数。两者合起来说明矩阵构成一个向量空间。')
  + p('两条必记性质：<code>A + B = B + A</code>（交换），<code>A(BC) = (AB)C</code>（乘法结合，前提是阶数能乘）。')
  + h3('3.3 矩阵乘法')
  + p('若 A 是 <b>m × p</b>、B 是 <b>p × n</b>，则 AB 是 <b>m × n</b>，且')
  + p('<b><code>(AB)_ij = Σ_{k=1..p} a_ik · b_kj</code></b>')
  + p('口诀：<b>「行乘列，加起来」</b>。左矩阵取一行，右矩阵取一列，对应元素相乘再求和。')
  + cal('warn', '三条打破直觉的性质', '(1) <code>AB ≠ BA</code>，乘法不交换；(2) <code>AB = 0</code> 不能推出 A = 0 或 B = 0；(3) <code>AB = AC</code> 且 A ≠ 0 也不能约去 A。这三条是选择题的高频陷阱。')
  + p('运算律中成立的部分：<code>A(BC) = (AB)C</code>、<code>A(B+C) = AB+AC</code>、<code>(A+B)C = AC+BC</code>、<code>(AB)ᵀ = BᵀAᵀ</code>（注意顺序颠倒）。')
  + h3('3.4 特殊矩阵')
  + tb(('名称', '特征', '作用'),
       ('零阵 O', '所有元素为 0', '加法单位元'),
       ('单位阵 I', '主对角为 1，其余 0', '<code>AI = IA = A</code>'),
       ('对角阵 diag(d₁…dₙ)', '非主对角均为 0', '相当于各方向分别缩放'),
       ('上/下三角阵', '对角线一侧全为 0', '行列式等于对角线乘积'),
       ('对称阵', '<code>Aᵀ = A</code>', '可正交对角化'),
       ('反对称阵', '<code>Aᵀ = −A</code>', '主对角必为 0'))
  + h3('3.5 线性变换')
  + p('矩阵作用于向量：<code>A x</code> 得到新向量。几何上：')
  + ul('<b>缩放</b>：<code>diag(s₁, s₂)</code> 把 (x,y) 变为 (s₁x, s₂y)',
      '<b>旋转 θ</b>：<code>[[cos θ, −sin θ],[sin θ, cos θ]]</code>',
      '<b>关于 x 轴反射</b>：<code>[[1,0],[0,−1]]</code>',
      '<b>关于 y = x 反射</b>：<code>[[0,1],[1,0]]</code>',
      '<b>投影到 x 轴</b>：<code>[[1,0],[0,0]]</code>')
  + p('判别技巧：看基向量 e₁ = (1,0)、e₂ = (0,1) 被送到哪里，那两列就是矩阵的两列。'),
 kws=K(('matrix', '矩阵', 'A rectangular array of numbers.'),
       ('order / dimension', '阶', 'An m × n matrix has m rows and n columns.'),
       ('entry / element', '元素', 'a_ij denotes the entry in row i, column j.'),
       ('transpose', '转置', '(Aᵀ)_ij = a_ji.'),
       ('identity matrix', '单位阵', 'The matrix I with ones on the diagonal.'),
       ('singular / non-singular', '奇异 / 非奇异', 'A singular matrix has no inverse.'),
       ('linear transformation', '线性变换', 'A map x ↦ Ax.'),
       ('rotation matrix', '旋转矩阵', '[[cos θ, −sin θ],[sin θ, cos θ]].')),
 examples=(qa('例 1　A = [[1,2],[3,4]]，B = [[0,1],[1,0]]，求 AB 与 BA。',
   p('AB = [[1·0+2·1, 1·1+2·0],[3·0+4·1, 3·1+4·0]] = [[2,1],[4,3]]。')
   + p('BA = [[0·1+1·3, 0·2+1·4],[1·1+0·3, 1·2+0·4]] = [[3,4],[1,2]]。')
   + p('结论：AB ≠ BA，乘法的不可交换性具体可见。注意 B 只是一个「交换 x 与 y」的变换。'))
  + qa('例 2　证明 AB = 0 但 A、B 均非零。',
   p('取 A = [[1,0],[0,0]]，B = [[0,0],[1,0]]。AB = [[0,0],[0,0]]。')
   + p('几何解释：A 把一切投影到 x 轴，B 把 y 轴方向映射到 x 轴之外…… 具体地说 B 的输出只有 y 分量，而 A 把 y 分量全部丢弃，故复合为零。'))
  + qa('例 3　求把平面绕原点逆时针旋转 90° 的矩阵，并作用于 (2, 3)。',
   p('θ = π/2：<code>cos = 0, sin = 1</code>，矩阵 <code>R = [[0,−1],[1,0]]</code>。')
   + p('<code>R(2,3)ᵀ = (0·2 + (−1)·3, 1·2 + 0·3)ᵀ = (−3, 2)ᵀ</code>。检验：长度仍为 √13 ✓。'))),
 practice=(ol('A 是 2×3，B 是 3×4，AB 是什么阶？BA 能乘吗？',
        '求 <code>[[1,2],[3,4]]</code> 的转置，并验证它是否对称。',
        '设 A = [[2,1],[1,2]]，求 <code>A² − 4A + 3I</code>。',
        '写出「关于 y 轴反射」的矩阵。')
  + det('答案与思路',
   p('<b>1.</b> AB 是 2×4。BA 需要 B 的列数 4 等于 A 的行数 2，不成立，不能乘。')
   + p('<b>2.</b> 转置为 <code>[[1,3],[2,4]]</code>，与原矩阵不等，不对称。注意 <code>[[1,2],[2,1]]</code> 才是对称的。')
   + p('<b>3.</b> <code>A² = [[5,4],[4,5]]</code>；<code>4A = [[8,4],[4,8]]</code>；<code>3I = [[3,0],[0,3]]</code>。相加减得 <code>[[0,0],[0,0]]</code>。这正说明 A 满足自己的特征方程 <code>λ² − 4λ + 3 = 0</code>。')
   + p('<b>4.</b> e₁ = (1,0) → (−1,0)，e₂ → (0,1)，所以矩阵 <code>[[−1,0],[0,1]]</code>。')),
 exam=(p(badge('bad', '必考') + '矩阵乘法（尤其阶数检查与顺序）、转置性质、线性变换矩阵的构造。')
  + p(badge('warn', '易错 1') + '把 <code>(AB)ᵀ</code> 写成 <code>AᵀBᵀ</code>。正确是 <code>BᵀAᵀ</code>。')
  + p(badge('warn', '易错 2') + '乘法时行列对错位。建议先写出结果矩阵的阶，再逐个格子算。')
  + p(badge('warn', '易错 3') + '以为 <code>AB = 0</code> 能推出 A 或 B 为零。')
  + p(badge('mute', '进阶') + '旋转矩阵的行列式为 1，反射矩阵为 −1，这是判断「保向还是反向」的快捷方法。')),
 checklist=(h2('矩阵运算检查清单')
  + st('先写阶：确认 m×p 与 p×n 能乘，结果 m×n',
       '算每个元素前，把左矩阵第 i 行与右矩阵第 j 列并排写在草稿上',
       '逐项乘加，不要跳项；p 较大时分两遍验算',
       '涉及转置时，先把括号顺序倒过来再展开',
       '用单位阵 I 做自检：<code>AI</code> 应该还等于 A')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture2.pdf', '全篇', '矩阵定义、加法与数乘、乘法、特殊矩阵、线性变换'),
   ('（补充）', '—', '旋转/反射/投影矩阵的具体形式与「看基向量」技巧为补充'))))

# ============================================================ 2
LEC.append(L(
 slug='t2-coordinate-systems',
 tzh='Topic 2 · 柱坐标与球坐标',
 ten='Cylindrical and Spherical Coordinates',
 keywords=['cylindrical coordinates', 'spherical coordinates', 'coordinate surface', 'Jacobian', 'volume element'],
 files=['Topic 2/EMII_Week2_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('平面上用极坐标，空间中就用柱坐标与球坐标。它们的共同思路是：<b>把「距离」与「角度」分开算</b>，让具有旋转对称性的曲面（圆柱、球、圆锥）写成极简单的方程。')
  + p('学完本节你应当能够：')
  + ck('在直角、柱、球三种坐标之间自由互换',
     '把常见曲面（柱面、球面、锥面）写成最简坐标方程',
     '写出三种坐标下的体积微元',
     '判断一道三重积分题该用哪种坐标')),
 detail=(h3('2.1 柱坐标 cylindrical coordinates')
  + p('在极坐标 (r, θ) 上直接加一个高度 z：')
  + p('<b><code>x = r cos θ, y = r sin θ, z = z</code></b>')
  + p('反变换：<code>r = √(x²+y²)</code>，<code>θ = arctan2(y, x)</code>，<code>z = z</code>。范围一般取 <code>r ≥ 0</code>、<code>0 ≤ θ &lt; 2π</code>、<code>z ∈ ℝ</code>（z 就是高度，可负）。')
  + p('柱坐标的坐标面（coordinate surfaces）：<code>r = 常数</code> 是圆柱面，<code>θ = 常数</code> 是过 z 轴的半平面，<code>z = 常数</code> 是水平平面。')
  + p('体积微元：<code>dV = r dr dθ dz</code>。那个多出的 r 是雅可比行列式（Jacobian）的绝对值，来源是极坐标面积微元 <code>r dr dθ</code>。')
  + h3('2.2 球坐标 spherical coordinates')
  + p('用「到原点的距离 ρ」与两个角度定位：')
  + p('<b><code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code></b>')
  + p('其中 <code>ρ ≥ 0</code> 是径向距离，<code>φ ∈ [0, π]</code> 是<b>与正 z 轴的夹角</b>（极角 / polar angle），<code>θ ∈ [0, 2π)</code> 是方位角（azimuthal angle）。')
  + cal('warn', '最容易错的一点', 'φ 是从 <b>z 轴</b> 量起的，不是从 xy 平面。所以 <code>z = ρ cos φ</code>，而 <code>r = ρ sin φ</code>。把 φ 与「与 xy 平面的夹角」弄反，整个公式全错。')
  + p('反变换：<code>ρ = √(x²+y²+z²)</code>，<code>cos φ = z/ρ</code>，<code>tan θ = y/x</code>。')
  + p('体积微元：<code>dV = ρ² sin φ dρ dφ dθ</code>。两个因子 ρ² 与 sin φ 缺一不可。')
  + h3('2.3 三种坐标下的典型曲面')
  + tb(('曲面', '直角坐标', '柱坐标', '球坐标'),
       ('圆柱面', 'x²+y² = a²', 'r = a', 'ρ sin φ = a'),
       ('球面', 'x²+y²+z² = a²', 'r²+z² = a²', 'ρ = a'),
       ('锥面（顶角 2α）', 'z² = k²(x²+y²)', 'z = kr', 'φ = α'),
       ('水平平面', 'z = c', 'z = c', 'ρ cos φ = c'),
       ('过 z 轴的半平面', 'y = x tan θ₀', 'θ = θ₀', 'θ = θ₀'))
  + cal('tip', '选题口诀', '球面或锥面 → 球坐标；圆柱面或绕 z 轴的对称 → 柱坐标；平面直角边界（长方体）→ 直角坐标。选对坐标能把三重积分降成一次单重积分。'),
 kws=K(('cylindrical coordinates', '柱坐标', 'x = r cos θ, y = r sin θ, z = z.'),
       ('spherical coordinates', '球坐标', 'x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ.'),
       ('polar angle', '极角 φ', 'The angle measured from the positive z-axis.'),
       ('azimuthal angle', '方位角 θ', 'The angle measured in the xy-plane from the positive x-axis.'),
       ('coordinate surface', '坐标面', 'r = const, θ = const, z = const.'),
       ('Jacobian', '雅可比', 'The factor r (or ρ² sin φ) in the volume element.'),
       ('volume element', '体积微元', 'dV = r dr dθ dz or dV = ρ² sin φ dρ dφ dθ.')),
 examples=(qa('例 1　把点 P(1, √3, 2) 从直角坐标换成柱坐标与球坐标。',
   p('柱坐标：<code>r = √(1+3) = 2</code>，<code>θ = arctan(√3/1) = π/3</code>（第一象限），<code>z = 2</code>。所以 (2, π/3, 2)。')
   + p('球坐标：<code>ρ = √(1+3+4) = 2√2</code>，<code>cos φ = z/ρ = 2/(2√2) = 1/√2</code> 得 <code>φ = π/4</code>，<code>θ = π/3</code>。')
   + p('检验：<code>ρ sin φ = 2√2 · 1/√2 = 2 = r</code> ✓。'))
  + qa('例 2　把 x² + y² + z² = 4z 化为球坐标方程，并说出它是什么曲面。',
   p('代入 <code>x²+y²+z² = ρ²</code>、<code>z = ρ cos φ</code>，得 <code>ρ² = 4ρ cos φ</code>。')
   + p('<code>ρ = 0</code> 是原点，其余点约去 ρ：<code>ρ = 4cos φ</code>。')
   + p('它是球心 (0,0,2)、半径 2 的球面（把原式配方：<code>x²+y²+(z−2)² = 4</code>）。'))),
 practice=(ol('把 <code>z = x² + y²</code> 化为柱坐标方程。',
        '求球坐标下 <code>φ = π/3</code> 对应的直角坐标曲面。',
        '把 <code>r = 2cos θ</code>（柱坐标）写成直角坐标方程。',
        '半径为 2 的球体内，用球坐标写出体积积分式（不需求值）。')
  + det('答案与思路',
   p('<b>1.</b> <code>z = r²</code>。这是一个开口向上的旋转抛物面。')
   + p('<b>2.</b> <code>cos φ = 1/2</code>，由 <code>z = ρ cos φ</code>、<code>r = ρ sin φ</code> 得 <code>z = r/√3</code>，平方得 <code>z² = (x²+y²)/3</code>，即顶角 60° 的锥面。')
   + p('<b>3.</b> 两边乘 r 得 <code>r² = 2r cos θ</code>，即 <code>x²+y² = 2x</code>，即 <code>(x−1)²+y² = 1</code>，一个圆柱面。')
   + p('<b>4.</b> <code>∫₀^{2π}∫₀^{π}∫₀^{2} ρ² sin φ dρ dφ dθ</code>。')),
 exam=(p(badge('bad', '必考') + '三种坐标的互换、把曲面写成最简坐标方程、写对体积微元。')
  + p(badge('warn', '易错 1') + '<b>球坐标 φ 的起算轴弄反</b>。φ 从 z 轴量起，<code>z = ρcos φ</code>。')
  + p(badge('warn', '易错 2') + '<b>漏写雅可比因子</b>。柱坐标漏 r、球坐标漏 ρ²sin φ，积分值会差一个量级。')
  + p(badge('warn', '易错 3') + '<b>θ 象限判断错</b>。用 <code>arctan(y/x)</code> 只给主值，x &lt; 0 时要加 π。')
  + p(badge('mute', '进阶') + '球坐标下「锥面 φ = α + 球面 ρ = a」围成的区域，俗称冰淇淋筒形区域，是三重积分最常见的考题。')),
 checklist=(h2('坐标转换清单')
  + st('先算 ρ（或 r），再算角，最后算 z（或 φ）',
       '判断 θ 所在象限：看 x、y 的符号',
       '球坐标用 <code>cos φ = z/ρ</code> 比用 sin 更稳（不会有符号歧义）',
       '写体积微元前先确认用什么坐标，把雅可比因子一并写上',
       '化简曲面方程时注意 ρ = 0 的点，必要时单独讨论')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture1.pdf', '全篇', '柱坐标、球坐标定义与互换、坐标面、体积微元'),
   ('（补充）', '—', '三种坐标选择口诀与冰淇淋筒形区域说法为衔接性补充'))))

# ============================================================ 3
LEC.append(L(
 slug='t2-matrices',
 tzh='Topic 2 · 矩阵、运算与线性变换',
 ten='Matrices, Operations on Matrices, Special Matrices, and Transformations',
 keywords=['matrix', 'entry', 'matrix multiplication', 'transpose', 'identity matrix', 'inverse', 'linear transformation'],
 files=['Topic 2/EMII_Week2_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('矩阵是把「一组线性关系」写成一张表。它既是方程组的紧凑写法，也是线性变换（旋转、缩放、投影）的坐标表示。本节先把矩阵当数据结构定清楚，再学四种基本运算，最后把它当「函数」用。')
  + p('学完本节你应当能够：')
  + ck('说出矩阵的阶、元素、行、列、主对角线',
     '做加法、数乘、乘法、转置，并判断哪些运算合法',
     '识别单位阵、零阵、对角阵、三角阵、对称阵',
     '把平面/空间的线性变换写成矩阵并作用于向量')),
 detail=(h3('3.1 矩阵的定义与记号')
  + p('一个 <b>m × n</b> 矩阵是 m 行 n 列的数表，元素记 <code>a_ij</code>（第 i 行第 j 列）。行数与列数相等时称<b>方阵</b>（square matrix），方阵从左上到右下的一排元素称<b>主对角线</b>（main diagonal）。')
  + p('两个矩阵相等当且仅当阶相同且每个对应元素相等——这一条是解矩阵方程的基本工具。')
  + h3('3.2 加法与数乘')
  + p('加法：同阶矩阵对应元素相加。数乘：每个元素乘以该数。两者合起来说明矩阵构成一个向量空间。')
  + p('两条必记性质：<code>A + B = B + A</code>（交换），<code>A(BC) = (AB)C</code>（乘法结合，前提是阶数能乘）。')
  + h3('3.3 矩阵乘法')
  + p('若 A 是 <b>m × p</b>、B 是 <b>p × n</b>，则 AB 是 <b>m × n</b>，且')
  + p('<b><code>(AB)_ij = Σ_{k=1..p} a_ik · b_kj</code></b>')
  + p('口诀：<b>「行乘列，加起来」</b>。左矩阵取一行，右矩阵取一列，对应元素相乘再求和。')
  + cal('warn', '三条打破直觉的性质', '(1) <code>AB ≠ BA</code>，乘法不交换；(2) <code>AB = 0</code> 不能推出 A = 0 或 B = 0；(3) <code>AB = AC</code> 且 A ≠ 0 也不能约去 A。这三条是选择题的高频陷阱。')
  + p('运算律中成立的部分：<code>A(BC) = (AB)C</code>、<code>A(B+C) = AB+AC</code>、<code>(A+B)C = AC+BC</code>、<code>(AB)ᵀ = BᵀAᵀ</code>（注意顺序颠倒）。')
  + h3('3.4 特殊矩阵')
  + tb(('名称', '特征', '作用'),
       ('零阵 O', '所有元素为 0', '加法单位元'),
       ('单位阵 I', '主对角为 1，其余 0', '<code>AI = IA = A</code>'),
       ('对角阵 diag(d₁…dₙ)', '非主对角均为 0', '相当于各方向分别缩放'),
       ('上/下三角阵', '对角线一侧全为 0', '行列式等于对角线乘积'),
       ('对称阵', '<code>Aᵀ = A</code>', '可正交对角化'),
       ('反对称阵', '<code>Aᵀ = −A</code>', '主对角必为 0'))
  + h3('3.5 线性变换')
  + p('矩阵作用于向量：<code>A x</code> 得到新向量。几何上：')
  + ul('<b>缩放</b>：<code>diag(s₁, s₂)</code> 把 (x,y) 变为 (s₁x, s₂y)',
      '<b>旋转 θ</b>：<code>[[cos θ, −sin θ],[sin θ, cos θ]]</code>',
      '<b>关于 x 轴反射</b>：<code>[[1,0],[0,−1]]</code>',
      '<b>关于 y = x 反射</b>：<code>[[0,1],[1,0]]</code>',
      '<b>投影到 x 轴</b>：<code>[[1,0],[0,0]]</code>')
  + p('判别技巧：看基向量 e₁ = (1,0)、e₂ = (0,1) 被送到哪里，那两列就是矩阵的两列。'),
 kws=K(('matrix', '矩阵', 'A rectangular array of numbers.'),
       ('order / dimension', '阶', 'An m × n matrix has m rows and n columns.'),
       ('entry / element', '元素', 'a_ij denotes the entry in row i, column j.'),
       ('transpose', '转置', '(Aᵀ)_ij = a_ji.'),
       ('identity matrix', '单位阵', 'The matrix I with ones on the diagonal.'),
       ('singular / non-singular', '奇异 / 非奇异', 'A singular matrix has no inverse.'),
       ('linear transformation', '线性变换', 'A map x ↦ Ax.'),
       ('rotation matrix', '旋转矩阵', '[[cos θ, −sin θ],[sin θ, cos θ]].')),
 examples=(qa('例 1　A = [[1,2],[3,4]]，B = [[0,1],[1,0]]，求 AB 与 BA。',
   p('AB = [[1·0+2·1, 1·1+2·0],[3·0+4·1, 3·1+4·0]] = [[2,1],[4,3]]。')
   + p('BA = [[0·1+1·3, 0·2+1·4],[1·1+0·3, 1·2+0·4]] = [[3,4],[1,2]]。')
   + p('结论：AB ≠ BA，乘法的不可交换性具体可见。注意 B 只是一个「交换 x 与 y」的变换。'))
  + qa('例 2　证明 AB = 0 但 A、B 均非零。',
   p('取 A = [[1,0],[0,0]]，B = [[0,0],[1,0]]。AB = [[0,0],[0,0]]。')
   + p('几何解释：A 把一切投影到 x 轴，B 把 y 轴方向映射到 x 轴之外…… 具体地说 B 的输出只有 y 分量，而 A 把 y 分量全部丢弃，故复合为零。'))
  + qa('例 3　求把平面绕原点逆时针旋转 90° 的矩阵，并作用于 (2, 3)。',
   p('θ = π/2：<code>cos = 0, sin = 1</code>，矩阵 <code>R = [[0,−1],[1,0]]</code>。')
   + p('<code>R(2,3)ᵀ = (0·2 + (−1)·3, 1·2 + 0·3)ᵀ = (−3, 2)ᵀ</code>。检验：长度仍为 √13 ✓。'))),
 practice=(ol('A 是 2×3，B 是 3×4，AB 是什么阶？BA 能乘吗？',
        '求 <code>[[1,2],[3,4]]</code> 的转置，并验证它是否对称。',
        '设 A = [[2,1],[1,2]]，求 <code>A² − 4A + 3I</code>。',
        '写出「关于 y 轴反射」的矩阵。')
  + det('答案与思路',
   p('<b>1.</b> AB 是 2×4。BA 需要 B 的列数 4 等于 A 的行数 2，不成立，不能乘。')
   + p('<b>2.</b> 转置为 <code>[[1,3],[2,4]]</code>，与原矩阵不等，不对称。注意 <code>[[1,2],[2,1]]</code> 才是对称的。')
   + p('<b>3.</b> <code>A² = [[5,4],[4,5]]</code>；<code>4A = [[8,4],[4,8]]</code>；<code>3I = [[3,0],[0,3]]</code>。相加减得 <code>[[0,0],[0,0]]</code>。这正说明 A 满足自己的特征方程 <code>λ² − 4λ + 3 = 0</code>。')
   + p('<b>4.</b> e₁ = (1,0) → (−1,0)，e₂ → (0,1)，所以矩阵 <code>[[−1,0],[0,1]]</code>。')),
 exam=(p(badge('bad', '必考') + '矩阵乘法（尤其阶数检查与顺序）、转置性质、线性变换矩阵的构造。')
  + p(badge('warn', '易错 1') + '把 <code>(AB)ᵀ</code> 写成 <code>AᵀBᵀ</code>。正确是 <code>BᵀAᵀ</code>。')
  + p(badge('warn', '易错 2') + '乘法时行列对错位。建议先写出结果矩阵的阶，再逐个格子算。')
  + p(badge('warn', '易错 3') + '以为 <code>AB = 0</code> 能推出 A 或 B 为零。')
  + p(badge('mute', '进阶') + '旋转矩阵的行列式为 1，反射矩阵为 −1，这是判断「保向还是反向」的快捷方法。')),
 checklist=(h2('矩阵运算检查清单')
  + st('先写阶：确认 m×p 与 p×n 能乘，结果 m×n',
       '算每个元素前，把左矩阵第 i 行与右矩阵第 j 列并排写在草稿上',
       '逐项乘加，不要跳项；p 较大时分两遍验算',
       '涉及转置时，先把括号顺序倒过来再展开',
       '用单位阵 I 做自检：<code>AI</code> 应该还等于 A')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture2.pdf', '全篇', '矩阵定义、加法与数乘、乘法、特殊矩阵、线性变换'),
   ('（补充）', '—', '旋转/反射/投影矩阵的具体形式与「看基向量」技巧为补充'))))

# ============================================================ 2
LEC.append(L(
 slug='t2-coordinate-systems',
 tzh='Topic 2 · 柱坐标与球坐标',
 ten='Cylindrical and Spherical Coordinates',
 keywords=['cylindrical coordinates', 'spherical coordinates', 'coordinate surface', 'Jacobian', 'volume element'],
 files=['Topic 2/EMII_Week2_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('平面上用极坐标，空间中就用柱坐标与球坐标。它们的共同思路是：<b>把「距离」与「角度」分开算</b>，让具有旋转对称性的曲面（圆柱、球、圆锥）写成极简单的方程。')
  + p('学完本节你应当能够：')
  + ck('在直角、柱、球三种坐标之间自由互换',
     '把常见曲面（柱面、球面、锥面）写成最简坐标方程',
     '写出三种坐标下的体积微元',
     '判断一道三重积分题该用哪种坐标')),
 detail=(h3('2.1 柱坐标 cylindrical coordinates')
  + p('在极坐标 (r, θ) 上直接加一个高度 z：')
  + p('<b><code>x = r cos θ, y = r sin θ, z = z</code></b>')
  + p('反变换：<code>r = √(x²+y²)</code>，<code>θ = arctan2(y, x)</code>，<code>z = z</code>。范围一般取 <code>r ≥ 0</code>、<code>0 ≤ θ &lt; 2π</code>、<code>z ∈ ℝ</code>（z 就是高度，可负）。')
  + p('柱坐标的坐标面（coordinate surfaces）：<code>r = 常数</code> 是圆柱面，<code>θ = 常数</code> 是过 z 轴的半平面，<code>z = 常数</code> 是水平平面。')
  + p('体积微元：<code>dV = r dr dθ dz</code>。那个多出的 r 是雅可比行列式（Jacobian）的绝对值，来源是极坐标面积微元 <code>r dr dθ</code>。')
  + h3('2.2 球坐标 spherical coordinates')
  + p('用「到原点的距离 ρ」与两个角度定位：')
  + p('<b><code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code></b>')
  + p('其中 <code>ρ ≥ 0</code> 是径向距离，<code>φ ∈ [0, π]</code> 是<b>与正 z 轴的夹角</b>（极角 / polar angle），<code>θ ∈ [0, 2π)</code> 是方位角（azimuthal angle）。')
  + cal('warn', '最容易错的一点', 'φ 是从 <b>z 轴</b> 量起的，不是从 xy 平面。所以 <code>z = ρ cos φ</code>，而 <code>r = ρ sin φ</code>。把 φ 与「与 xy 平面的夹角」弄反，整个公式全错。')
  + p('反变换：<code>ρ = √(x²+y²+z²)</code>，<code>cos φ = z/ρ</code>，<code>tan θ = y/x</code>。')
  + p('体积微元：<code>dV = ρ² sin φ dρ dφ dθ</code>。两个因子 ρ² 与 sin φ 缺一不可。')
  + h3('2.3 三种坐标下的典型曲面')
  + tb(('曲面', '直角坐标', '柱坐标', '球坐标'),
       ('圆柱面', 'x²+y² = a²', 'r = a', 'ρ sin φ = a'),
       ('球面', 'x²+y²+z² = a²', 'r²+z² = a²', 'ρ = a'),
       ('锥面（顶角 2α）', 'z² = k²(x²+y²)', 'z = kr', 'φ = α'),
       ('水平平面', 'z = c', 'z = c', 'ρ cos φ = c'),
       ('过 z 轴的半平面', 'y = x tan θ₀', 'θ = θ₀', 'θ = θ₀'))
  + cal('tip', '选题口诀', '球面或锥面 → 球坐标；圆柱面或绕 z 轴的对称 → 柱坐标；平面直角边界（长方体）→ 直角坐标。选对坐标能把三重积分降成一次单重积分。'),
 kws=K(('cylindrical coordinates', '柱坐标', 'x = r cos θ, y = r sin θ, z = z.'),
       ('spherical coordinates', '球坐标', 'x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ.'),
       ('polar angle', '极角 φ', 'The angle measured from the positive z-axis.'),
       ('azimuthal angle', '方位角 θ', 'The angle measured in the xy-plane from the positive x-axis.'),
       ('coordinate surface', '坐标面', 'r = const, θ = const, z = const.'),
       ('Jacobian', '雅可比', 'The factor r (or ρ² sin φ) in the volume element.'),
       ('volume element', '体积微元', 'dV = r dr dθ dz or dV = ρ² sin φ dρ dφ dθ.')),
 examples=(qa('例 1　把点 P(1, √3, 2) 从直角坐标换成柱坐标与球坐标。',
   p('柱坐标：<code>r = √(1+3) = 2</code>，<code>θ = arctan(√3/1) = π/3</code>（第一象限），<code>z = 2</code>。所以 (2, π/3, 2)。')
   + p('球坐标：<code>ρ = √(1+3+4) = 2√2</code>，<code>cos φ = z/ρ = 2/(2√2) = 1/√2</code> 得 <code>φ = π/4</code>，<code>θ = π/3</code>。')
   + p('检验：<code>ρ sin φ = 2√2 · 1/√2 = 2 = r</code> ✓。'))
  + qa('例 2　把 x² + y² + z² = 4z 化为球坐标方程，并说出它是什么曲面。',
   p('代入 <code>x²+y²+z² = ρ²</code>、<code>z = ρ cos φ</code>，得 <code>ρ² = 4ρ cos φ</code>。')
   + p('<code>ρ = 0</code> 是原点，其余点约去 ρ：<code>ρ = 4cos φ</code>。')
   + p('它是球心 (0,0,2)、半径 2 的球面（把原式配方：<code>x²+y²+(z−2)² = 4</code>）。'))),
 practice=(ol('把 <code>z = x² + y²</code> 化为柱坐标方程。',
        '求球坐标下 <code>φ = π/3</code> 对应的直角坐标曲面。',
        '把 <code>r = 2cos θ</code>（柱坐标）写成直角坐标方程。',
        '半径为 2 的球体内，用球坐标写出体积积分式（不需求值）。')
  + det('答案与思路',
   p('<b>1.</b> <code>z = r²</code>。这是一个开口向上的旋转抛物面。')
   + p('<b>2.</b> <code>cos φ = 1/2</code>，由 <code>z = ρ cos φ</code>、<code>r = ρ sin φ</code> 得 <code>z = r/√3</code>，平方得 <code>z² = (x²+y²)/3</code>，即顶角 60° 的锥面。')
   + p('<b>3.</b> 两边乘 r 得 <code>r² = 2r cos θ</code>，即 <code>x²+y² = 2x</code>，即 <code>(x−1)²+y² = 1</code>，一个圆柱面。')
   + p('<b>4.</b> <code>∫₀^{2π}∫₀^{π}∫₀^{2} ρ² sin φ dρ dφ dθ</code>。')),
 exam=(p(badge('bad', '必考') + '三种坐标的互换、把曲面写成最简坐标方程、写对体积微元。')
  + p(badge('warn', '易错 1') + '<b>球坐标 φ 的起算轴弄反</b>。φ 从 z 轴量起，<code>z = ρcos φ</code>。')
  + p(badge('warn', '易错 2') + '<b>漏写雅可比因子</b>。柱坐标漏 r、球坐标漏 ρ²sin φ，积分值会差一个量级。')
  + p(badge('warn', '易错 3') + '<b>θ 象限判断错</b>。用 <code>arctan(y/x)</code> 只给主值，x &lt; 0 时要加 π。')
  + p(badge('mute', '进阶') + '球坐标下「锥面 φ = α + 球面 ρ = a」围成的区域，俗称冰淇淋筒形区域，是三重积分最常见的考题。')),
 checklist=(h2('坐标转换清单')
  + st('先算 ρ（或 r），再算角，最后算 z（或 φ）',
       '判断 θ 所在象限：看 x、y 的符号',
       '球坐标用 <code>cos φ = z/ρ</code> 比用 sin 更稳（不会有符号歧义）',
       '写体积微元前先确认用什么坐标，把雅可比因子一并写上',
       '化简曲面方程时注意 ρ = 0 的点，必要时单独讨论')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture1.pdf', '全篇', '柱坐标、球坐标定义与互换、坐标面、体积微元'),
   ('（补充）', '—', '三种坐标选择口诀与冰淇淋筒形区域说法为衔接性补充'))))

# ============================================================ 3
LEC.append(L(
 slug='t2-matrices',
 tzh='Topic 2 · 矩阵、运算与线性变换',
 ten='Matrices, Operations on Matrices, Special Matrices, and Transformations',
 keywords=['matrix', 'entry', 'matrix multiplication', 'transpose', 'identity matrix', 'inverse', 'linear transformation'],
 files=['Topic 2/EMII_Week2_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('矩阵是把「一组线性关系」写成一张表。它既是方程组的紧凑写法，也是线性变换（旋转、缩放、投影）的坐标表示。本节先把矩阵当数据结构定清楚，再学四种基本运算，最后把它当「函数」用。')
  + p('学完本节你应当能够：')
  + ck('说出矩阵的阶、元素、行、列、主对角线',
     '做加法、数乘、乘法、转置，并判断哪些运算合法',
     '识别单位阵、零阵、对角阵、三角阵、对称阵',
     '把平面/空间的线性变换写成矩阵并作用于向量')),
 detail=(h3('3.1 矩阵的定义与记号')
  + p('一个 <b>m × n</b> 矩阵是 m 行 n 列的数表，元素记 <code>a_ij</code>（第 i 行第 j 列）。行数与列数相等时称<b>方阵</b>（square matrix），方阵从左上到右下的一排元素称<b>主对角线</b>（main diagonal）。')
  + p('两个矩阵相等当且仅当阶相同且每个对应元素相等——这一条是解矩阵方程的基本工具。')
  + h3('3.2 加法与数乘')
  + p('加法：同阶矩阵对应元素相加。数乘：每个元素乘以该数。两者合起来说明矩阵构成一个向量空间。')
  + p('两条必记性质：<code>A + B = B + A</code>（交换），<code>A(BC) = (AB)C</code>（乘法结合，前提是阶数能乘）。')
  + h3('3.3 矩阵乘法')
  + p('若 A 是 <b>m × p</b>、B 是 <b>p × n</b>，则 AB 是 <b>m × n</b>，且')
  + p('<b><code>(AB)_ij = Σ_{k=1..p} a_ik · b_kj</code></b>')
  + p('口诀：<b>「行乘列，加起来」</b>。左矩阵取一行，右矩阵取一列，对应元素相乘再求和。')
  + cal('warn', '三条打破直觉的性质', '(1) <code>AB ≠ BA</code>，乘法不交换；(2) <code>AB = 0</code> 不能推出 A = 0 或 B = 0；(3) <code>AB = AC</code> 且 A ≠ 0 也不能约去 A。这三条是选择题的高频陷阱。')
  + p('运算律中成立的部分：<code>A(BC) = (AB)C</code>、<code>A(B+C) = AB+AC</code>、<code>(A+B)C = AC+BC</code>、<code>(AB)ᵀ = BᵀAᵀ</code>（注意顺序颠倒）。')
  + h3('3.4 特殊矩阵')
  + tb(('名称', '特征', '作用'),
       ('零阵 O', '所有元素为 0', '加法单位元'),
       ('单位阵 I', '主对角为 1，其余 0', '<code>AI = IA = A</code>'),
       ('对角阵 diag(d₁…dₙ)', '非主对角均为 0', '相当于各方向分别缩放'),
       ('上/下三角阵', '对角线一侧全为 0', '行列式等于对角线乘积'),
       ('对称阵', '<code>Aᵀ = A</code>', '可正交对角化'),
       ('反对称阵', '<code>Aᵀ = −A</code>', '主对角必为 0'))
  + h3('3.5 线性变换')
  + p('矩阵作用于向量：<code>A x</code> 得到新向量。几何上：')
  + ul('<b>缩放</b>：<code>diag(s₁, s₂)</code> 把 (x,y) 变为 (s₁x, s₂y)',
      '<b>旋转 θ</b>：<code>[[cos θ, −sin θ],[sin θ, cos θ]]</code>',
      '<b>关于 x 轴反射</b>：<code>[[1,0],[0,−1]]</code>',
      '<b>关于 y = x 反射</b>：<code>[[0,1],[1,0]]</code>',
      '<b>投影到 x 轴</b>：<code>[[1,0],[0,0]]</code>')
  + p('判别技巧：看基向量 e₁ = (1,0)、e₂ = (0,1) 被送到哪里，那两列就是矩阵的两列。'),
 kws=K(('matrix', '矩阵', 'A rectangular array of numbers.'),
       ('order / dimension', '阶', 'An m × n matrix has m rows and n columns.'),
       ('entry / element', '元素', 'a_ij denotes the entry in row i, column j.'),
       ('transpose', '转置', '(Aᵀ)_ij = a_ji.'),
       ('identity matrix', '单位阵', 'The matrix I with ones on the diagonal.'),
       ('singular / non-singular', '奇异 / 非奇异', 'A singular matrix has no inverse.'),
       ('linear transformation', '线性变换', 'A map x ↦ Ax.'),
       ('rotation matrix', '旋转矩阵', '[[cos θ, −sin θ],[sin θ, cos θ]].')),
 examples=(qa('例 1　A = [[1,2],[3,4]]，B = [[0,1],[1,0]]，求 AB 与 BA。',
   p('AB = [[1·0+2·1, 1·1+2·0],[3·0+4·1, 3·1+4·0]] = [[2,1],[4,3]]。')
   + p('BA = [[0·1+1·3, 0·2+1·4],[1·1+0·3, 1·2+0·4]] = [[3,4],[1,2]]。')
   + p('结论：AB ≠ BA，乘法的不可交换性具体可见。注意 B 只是一个「交换 x 与 y」的变换。'))
  + qa('例 2　证明 AB = 0 但 A、B 均非零。',
   p('取 A = [[1,0],[0,0]]，B = [[0,0],[1,0]]。AB = [[0,0],[0,0]]。')
   + p('几何解释：A 把一切投影到 x 轴，B 把 y 轴方向映射到 x 轴之外…… 具体地说 B 的输出只有 y 分量，而 A 把 y 分量全部丢弃，故复合为零。'))
  + qa('例 3　求把平面绕原点逆时针旋转 90° 的矩阵，并作用于 (2, 3)。',
   p('θ = π/2：<code>cos = 0, sin = 1</code>，矩阵 <code>R = [[0,−1],[1,0]]</code>。')
   + p('<code>R(2,3)ᵀ = (0·2 + (−1)·3, 1·2 + 0·3)ᵀ = (−3, 2)ᵀ</code>。检验：长度仍为 √13 ✓。'))),
 practice=(ol('A 是 2×3，B 是 3×4，AB 是什么阶？BA 能乘吗？',
        '求 <code>[[1,2],[3,4]]</code> 的转置，并验证它是否对称。',
        '设 A = [[2,1],[1,2]]，求 <code>A² − 4A + 3I</code>。',
        '写出「关于 y 轴反射」的矩阵。')
  + det('答案与思路',
   p('<b>1.</b> AB 是 2×4。BA 需要 B 的列数 4 等于 A 的行数 2，不成立，不能乘。')
   + p('<b>2.</b> 转置为 <code>[[1,3],[2,4]]</code>，与原矩阵不等，不对称。注意 <code>[[1,2],[2,1]]</code> 才是对称的。')
   + p('<b>3.</b> <code>A² = [[5,4],[4,5]]</code>；<code>4A = [[8,4],[4,8]]</code>；<code>3I = [[3,0],[0,3]]</code>。相加减得 <code>[[0,0],[0,0]]</code>。这正说明 A 满足自己的特征方程 <code>λ² − 4λ + 3 = 0</code>。')
   + p('<b>4.</b> e₁ = (1,0) → (−1,0)，e₂ → (0,1)，所以矩阵 <code>[[−1,0],[0,1]]</code>。')),
 exam=(p(badge('bad', '必考') + '矩阵乘法（尤其阶数检查与顺序）、转置性质、线性变换矩阵的构造。')
  + p(badge('warn', '易错 1') + '把 <code>(AB)ᵀ</code> 写成 <code>AᵀBᵀ</code>。正确是 <code>BᵀAᵀ</code>。')
  + p(badge('warn', '易错 2') + '乘法时行列对错位。建议先写出结果矩阵的阶，再逐个格子算。')
  + p(badge('warn', '易错 3') + '以为 <code>AB = 0</code> 能推出 A 或 B 为零。')
  + p(badge('mute', '进阶') + '旋转矩阵的行列式为 1，反射矩阵为 −1，这是判断「保向还是反向」的快捷方法。')),
 checklist=(h2('矩阵运算检查清单')
  + st('先写阶：确认 m×p 与 p×n 能乘，结果 m×n',
       '算每个元素前，把左矩阵第 i 行与右矩阵第 j 列并排写在草稿上',
       '逐项乘加，不要跳项；p 较大时分两遍验算',
       '涉及转置时，先把括号顺序倒过来再展开',
       '用单位阵 I 做自检：<code>AI</code> 应该还等于 A')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture2.pdf', '全篇', '矩阵定义、加法与数乘、乘法、特殊矩阵、线性变换'),
   ('（补充）', '—', '旋转/反射/投影矩阵的具体形式与「看基向量」技巧为补充'))))

# ============================================================ 2
LEC.append(L(
 slug='t2-coordinate-systems',
 tzh='Topic 2 · 柱坐标与球坐标',
 ten='Cylindrical and Spherical Coordinates',
 keywords=['cylindrical coordinates', 'spherical coordinates', 'coordinate surface', 'Jacobian', 'volume element'],
 files=['Topic 2/EMII_Week2_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('平面上用极坐标，空间中就用柱坐标与球坐标。它们的共同思路是：<b>把「距离」与「角度」分开算</b>，让具有旋转对称性的曲面（圆柱、球、圆锥）写成极简单的方程。')
  + p('学完本节你应当能够：')
  + ck('在直角、柱、球三种坐标之间自由互换',
     '把常见曲面（柱面、球面、锥面）写成最简坐标方程',
     '写出三种坐标下的体积微元',
     '判断一道三重积分题该用哪种坐标')),
 detail=(h3('2.1 柱坐标 cylindrical coordinates')
  + p('在极坐标 (r, θ) 上直接加一个高度 z：')
  + p('<b><code>x = r cos θ, y = r sin θ, z = z</code></b>')
  + p('反变换：<code>r = √(x²+y²)</code>，<code>θ = arctan2(y, x)</code>，<code>z = z</code>。范围一般取 <code>r ≥ 0</code>、<code>0 ≤ θ &lt; 2π</code>、<code>z ∈ ℝ</code>（z 就是高度，可负）。')
  + p('柱坐标的坐标面（coordinate surfaces）：<code>r = 常数</code> 是圆柱面，<code>θ = 常数</code> 是过 z 轴的半平面，<code>z = 常数</code> 是水平平面。')
  + p('体积微元：<code>dV = r dr dθ dz</code>。那个多出的 r 是雅可比行列式（Jacobian）的绝对值，来源是极坐标面积微元 <code>r dr dθ</code>。')
  + h3('2.2 球坐标 spherical coordinates')
  + p('用「到原点的距离 ρ」与两个角度定位：')
  + p('<b><code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code></b>')
  + p('其中 <code>ρ ≥ 0</code> 是径向距离，<code>φ ∈ [0, π]</code> 是<b>与正 z 轴的夹角</b>（极角 / polar angle），<code>θ ∈ [0, 2π)</code> 是方位角（azimuthal angle）。')
  + cal('warn', '最容易错的一点', 'φ 是从 <b>z 轴</b> 量起的，不是从 xy 平面。所以 <code>z = ρ cos φ</code>，而 <code>r = ρ sin φ</code>。把 φ 与「与 xy 平面的夹角」弄反，整个公式全错。')
  + p('反变换：<code>ρ = √(x²+y²+z²)</code>，<code>cos φ = z/ρ</code>，<code>tan θ = y/x</code>。')
  + p('体积微元：<code>dV = ρ² sin φ dρ dφ dθ</code>。两个因子 ρ² 与 sin φ 缺一不可。')
  + h3('2.3 三种坐标下的典型曲面')
  + tb(('曲面', '直角坐标', '柱坐标', '球坐标'),
       ('圆柱面', 'x²+y² = a²', 'r = a', 'ρ sin φ = a'),
       ('球面', 'x²+y²+z² = a²', 'r²+z² = a²', 'ρ = a'),
       ('锥面（顶角 2α）', 'z² = k²(x²+y²)', 'z = kr', 'φ = α'),
       ('水平平面', 'z = c', 'z = c', 'ρ cos φ = c'),
       ('过 z 轴的半平面', 'y = x tan θ₀', 'θ = θ₀', 'θ = θ₀'))
  + cal('tip', '选题口诀', '球面或锥面 → 球坐标；圆柱面或绕 z 轴的对称 → 柱坐标；平面直角边界（长方体）→ 直角坐标。选对坐标能把三重积分降成一次单重积分。'),
 kws=K(('cylindrical coordinates', '柱坐标', 'x = r cos θ, y = r sin θ, z = z.'),
       ('spherical coordinates', '球坐标', 'x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ.'),
       ('polar angle', '极角 φ', 'The angle measured from the positive z-axis.'),
       ('azimuthal angle', '方位角 θ', 'The angle measured in the xy-plane from the positive x-axis.'),
       ('coordinate surface', '坐标面', 'r = const, θ = const, z = const.'),
       ('Jacobian', '雅可比', 'The factor r (or ρ² sin φ) in the volume element.'),
       ('volume element', '体积微元', 'dV = r dr dθ dz or dV = ρ² sin φ dρ dφ dθ.')),
 examples=(qa('例 1　把点 P(1, √3, 2) 从直角坐标换成柱坐标与球坐标。',
   p('柱坐标：<code>r = √(1+3) = 2</code>，<code>θ = arctan(√3/1) = π/3</code>（第一象限），<code>z = 2</code>。所以 (2, π/3, 2)。')
   + p('球坐标：<code>ρ = √(1+3+4) = 2√2</code>，<code>cos φ = z/ρ = 2/(2√2) = 1/√2</code> 得 <code>φ = π/4</code>，<code>θ = π/3</code>。')
   + p('检验：<code>ρ sin φ = 2√2 · 1/√2 = 2 = r</code> ✓。'))
  + qa('例 2　把 x² + y² + z² = 4z 化为球坐标方程，并说出它是什么曲面。',
   p('代入 <code>x²+y²+z² = ρ²</code>、<code>z = ρ cos φ</code>，得 <code>ρ² = 4ρ cos φ</code>。')
   + p('<code>ρ = 0</code> 是原点，其余点约去 ρ：<code>ρ = 4cos φ</code>。')
   + p('它是球心 (0,0,2)、半径 2 的球面（把原式配方：<code>x²+y²+(z−2)² = 4</code>）。'))),
 practice=(ol('把 <code>z = x² + y²</code> 化为柱坐标方程。',
        '求球坐标下 <code>φ = π/3</code> 对应的直角坐标曲面。',
        '把 <code>r = 2cos θ</code>（柱坐标）写成直角坐标方程。',
        '半径为 2 的球体内，用球坐标写出体积积分式（不需求值）。')
  + det('答案与思路',
   p('<b>1.</b> <code>z = r²</code>。这是一个开口向上的旋转抛物面。')
   + p('<b>2.</b> <code>cos φ = 1/2</code>，由 <code>z = ρ cos φ</code>、<code>r = ρ sin φ</code> 得 <code>z = r/√3</code>，平方得 <code>z² = (x²+y²)/3</code>，即顶角 60° 的锥面。')
   + p('<b>3.</b> 两边乘 r 得 <code>r² = 2r cos θ</code>，即 <code>x²+y² = 2x</code>，即 <code>(x−1)²+y² = 1</code>，一个圆柱面。')
   + p('<b>4.</b> <code>∫₀^{2π}∫₀^{π}∫₀^{2} ρ² sin φ dρ dφ dθ</code>。')),
 exam=(p(badge('bad', '必考') + '三种坐标的互换、把曲面写成最简坐标方程、写对体积微元。')
  + p(badge('warn', '易错 1') + '<b>球坐标 φ 的起算轴弄反</b>。φ 从 z 轴量起，<code>z = ρcos φ</code>。')
  + p(badge('warn', '易错 2') + '<b>漏写雅可比因子</b>。柱坐标漏 r、球坐标漏 ρ²sin φ，积分值会差一个量级。')
  + p(badge('warn', '易错 3') + '<b>θ 象限判断错</b>。用 <code>arctan(y/x)</code> 只给主值，x &lt; 0 时要加 π。')
  + p(badge('mute', '进阶') + '球坐标下「锥面 φ = α + 球面 ρ = a」围成的区域，俗称冰淇淋筒形区域，是三重积分最常见的考题。')),
 checklist=(h2('坐标转换清单')
  + st('先算 ρ（或 r），再算角，最后算 z（或 φ）',
       '判断 θ 所在象限：看 x、y 的符号',
       '球坐标用 <code>cos φ = z/ρ</code> 比用 sin 更稳（不会有符号歧义）',
       '写体积微元前先确认用什么坐标，把雅可比因子一并写上',
       '化简曲面方程时注意 ρ = 0 的点，必要时单独讨论')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture1.pdf', '全篇', '柱坐标、球坐标定义与互换、坐标面、体积微元'),
   ('（补充）', '—', '三种坐标选择口诀与冰淇淋筒形区域说法为衔接性补充'))))

# ============================================================ 3
LEC.append(L(
 slug='t2-matrices',
 tzh='Topic 2 · 矩阵、运算与线性变换',
 ten='Matrices, Operations on Matrices, Special Matrices, and Transformations',
 keywords=['matrix', 'entry', 'matrix multiplication', 'transpose', 'identity matrix', 'inverse', 'linear transformation'],
 files=['Topic 2/EMII_Week2_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('矩阵是把「一组线性关系」写成一张表。它既是方程组的紧凑写法，也是线性变换（旋转、缩放、投影）的坐标表示。本节先把矩阵当数据结构定清楚，再学四种基本运算，最后把它当「函数」用。')
  + p('学完本节你应当能够：')
  + ck('说出矩阵的阶、元素、行、列、主对角线',
     '做加法、数乘、乘法、转置，并判断哪些运算合法',
     '识别单位阵、零阵、对角阵、三角阵、对称阵',
     '把平面/空间的线性变换写成矩阵并作用于向量')),
 detail=(h3('3.1 矩阵的定义与记号')
  + p('一个 <b>m × n</b> 矩阵是 m 行 n 列的数表，元素记 <code>a_ij</code>（第 i 行第 j 列）。行数与列数相等时称<b>方阵</b>（square matrix），方阵从左上到右下的一排元素称<b>主对角线</b>（main diagonal）。')
  + p('两个矩阵相等当且仅当阶相同且每个对应元素相等——这一条是解矩阵方程的基本工具。')
  + h3('3.2 加法与数乘')
  + p('加法：同阶矩阵对应元素相加。数乘：每个元素乘以该数。两者合起来说明矩阵构成一个向量空间。')
  + p('两条必记性质：<code>A + B = B + A</code>（交换），<code>A(BC) = (AB)C</code>（乘法结合，前提是阶数能乘）。')
  + h3('3.3 矩阵乘法')
  + p('若 A 是 <b>m × p</b>、B 是 <b>p × n</b>，则 AB 是 <b>m × n</b>，且')
  + p('<b><code>(AB)_ij = Σ_{k=1..p} a_ik · b_kj</code></b>')
  + p('口诀：<b>「行乘列，加起来」</b>。左矩阵取一行，右矩阵取一列，对应元素相乘再求和。')
  + cal('warn', '三条打破直觉的性质', '(1) <code>AB ≠ BA</code>，乘法不交换；(2) <code>AB = 0</code> 不能推出 A = 0 或 B = 0；(3) <code>AB = AC</code> 且 A ≠ 0 也不能约去 A。这三条是选择题的高频陷阱。')
  + p('运算律中成立的部分：<code>A(BC) = (AB)C</code>、<code>A(B+C) = AB+AC</code>、<code>(A+B)C = AC+BC</code>、<code>(AB)ᵀ = BᵀAᵀ</code>（注意顺序颠倒）。')
  + h3('3.4 特殊矩阵')
  + tb(('名称', '特征', '作用'),
       ('零阵 O', '所有元素为 0', '加法单位元'),
       ('单位阵 I', '主对角为 1，其余 0', '<code>AI = IA = A</code>'),
       ('对角阵 diag(d₁…dₙ)', '非主对角均为 0', '相当于各方向分别缩放'),
       ('上/下三角阵', '对角线一侧全为 0', '行列式等于对角线乘积'),
       ('对称阵', '<code>Aᵀ = A</code>', '可正交对角化'),
       ('反对称阵', '<code>Aᵀ = −A</code>', '主对角必为 0'))
  + h3('3.5 线性变换')
  + p('矩阵作用于向量：<code>A x</code> 得到新向量。几何上：')
  + ul('<b>缩放</b>：<code>diag(s₁, s₂)</code> 把 (x,y) 变为 (s₁x, s₂y)',
      '<b>旋转 θ</b>：<code>[[cos θ, −sin θ],[sin θ, cos θ]]</code>',
      '<b>关于 x 轴反射</b>：<code>[[1,0],[0,−1]]</code>',
      '<b>关于 y = x 反射</b>：<code>[[0,1],[1,0]]</code>',
      '<b>投影到 x 轴</b>：<code>[[1,0],[0,0]]</code>')
  + p('判别技巧：看基向量 e₁ = (1,0)、e₂ = (0,1) 被送到哪里，那两列就是矩阵的两列。'),
 kws=K(('matrix', '矩阵', 'A rectangular array of numbers.'),
       ('order / dimension', '阶', 'An m × n matrix has m rows and n columns.'),
       ('entry / element', '元素', 'a_ij denotes the entry in row i, column j.'),
       ('transpose', '转置', '(Aᵀ)_ij = a_ji.'),
       ('identity matrix', '单位阵', 'The matrix I with ones on the diagonal.'),
       ('singular / non-singular', '奇异 / 非奇异', 'A singular matrix has no inverse.'),
       ('linear transformation', '线性变换', 'A map x ↦ Ax.'),
       ('rotation matrix', '旋转矩阵', '[[cos θ, −sin θ],[sin θ, cos θ]].')),
 examples=(qa('例 1　A = [[1,2],[3,4]]，B = [[0,1],[1,0]]，求 AB 与 BA。',
   p('AB = [[1·0+2·1, 1·1+2·0],[3·0+4·1, 3·1+4·0]] = [[2,1],[4,3]]。')
   + p('BA = [[0·1+1·3, 0·2+1·4],[1·1+0·3, 1·2+0·4]] = [[3,4],[1,2]]。')
   + p('结论：AB ≠ BA，乘法的不可交换性具体可见。注意 B 只是一个「交换 x 与 y」的变换。'))
  + qa('例 2　证明 AB = 0 但 A、B 均非零。',
   p('取 A = [[1,0],[0,0]]，B = [[0,0],[1,0]]。AB = [[0,0],[0,0]]。')
   + p('几何解释：A 把一切投影到 x 轴，B 把 y 轴方向映射到 x 轴之外…… 具体地说 B 的输出只有 y 分量，而 A 把 y 分量全部丢弃，故复合为零。'))
  + qa('例 3　求把平面绕原点逆时针旋转 90° 的矩阵，并作用于 (2, 3)。',
   p('θ = π/2：<code>cos = 0, sin = 1</code>，矩阵 <code>R = [[0,−1],[1,0]]</code>。')
   + p('<code>R(2,3)ᵀ = (0·2 + (−1)·3, 1·2 + 0·3)ᵀ = (−3, 2)ᵀ</code>。检验：长度仍为 √13 ✓。'))),
 practice=(ol('A 是 2×3，B 是 3×4，AB 是什么阶？BA 能乘吗？',
        '求 <code>[[1,2],[3,4]]</code> 的转置，并验证它是否对称。',
        '设 A = [[2,1],[1,2]]，求 <code>A² − 4A + 3I</code>。',
        '写出「关于 y 轴反射」的矩阵。')
  + det('答案与思路',
   p('<b>1.</b> AB 是 2×4。BA 需要 B 的列数 4 等于 A 的行数 2，不成立，不能乘。')
   + p('<b>2.</b> 转置为 <code>[[1,3],[2,4]]</code>，与原矩阵不等，不对称。注意 <code>[[1,2],[2,1]]</code> 才是对称的。')
   + p('<b>3.</b> <code>A² = [[5,4],[4,5]]</code>；<code>4A = [[8,4],[4,8]]</code>；<code>3I = [[3,0],[0,3]]</code>。相加减得 <code>[[0,0],[0,0]]</code>。这正说明 A 满足自己的特征方程 <code>λ² − 4λ + 3 = 0</code>。')
   + p('<b>4.</b> e₁ = (1,0) → (−1,0)，e₂ → (0,1)，所以矩阵 <code>[[−1,0],[0,1]]</code>。')),
 exam=(p(badge('bad', '必考') + '矩阵乘法（尤其阶数检查与顺序）、转置性质、线性变换矩阵的构造。')
  + p(badge('warn', '易错 1') + '把 <code>(AB)ᵀ</code> 写成 <code>AᵀBᵀ</code>。正确是 <code>BᵀAᵀ</code>。')
  + p(badge('warn', '易错 2') + '乘法时行列对错位。建议先写出结果矩阵的阶，再逐个格子算。')
  + p(badge('warn', '易错 3') + '以为 <code>AB = 0</code> 能推出 A 或 B 为零。')
  + p(badge('mute', '进阶') + '旋转矩阵的行列式为 1，反射矩阵为 −1，这是判断「保向还是反向」的快捷方法。')),
 checklist=(h2('矩阵运算检查清单')
  + st('先写阶：确认 m×p 与 p×n 能乘，结果 m×n',
       '算每个元素前，把左矩阵第 i 行与右矩阵第 j 列并排写在草稿上',
       '逐项乘加，不要跳项；p 较大时分两遍验算',
       '涉及转置时，先把括号顺序倒过来再展开',
       '用单位阵 I 做自检：<code>AI</code> 应该还等于 A')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture2.pdf', '全篇', '矩阵定义、加法与数乘、乘法、特殊矩阵、线性变换'),
   ('（补充）', '—', '旋转/反射/投影矩阵的具体形式与「看基向量」技巧为补充'))))

# ============================================================ 2
LEC.append(L(
 slug='t2-coordinate-systems',
 tzh='Topic 2 · 柱坐标与球坐标',
 ten='Cylindrical and Spherical Coordinates',
 keywords=['cylindrical coordinates', 'spherical coordinates', 'coordinate surface', 'Jacobian', 'volume element'],
 files=['Topic 2/EMII_Week2_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('平面上用极坐标，空间中就用柱坐标与球坐标。它们的共同思路是：<b>把「距离」与「角度」分开算</b>，让具有旋转对称性的曲面（圆柱、球、圆锥）写成极简单的方程。')
  + p('学完本节你应当能够：')
  + ck('在直角、柱、球三种坐标之间自由互换',
     '把常见曲面（柱面、球面、锥面）写成最简坐标方程',
     '写出三种坐标下的体积微元',
     '判断一道三重积分题该用哪种坐标')),
 detail=(h3('2.1 柱坐标 cylindrical coordinates')
  + p('在极坐标 (r, θ) 上直接加一个高度 z：')
  + p('<b><code>x = r cos θ, y = r sin θ, z = z</code></b>')
  + p('反变换：<code>r = √(x²+y²)</code>，<code>θ = arctan2(y, x)</code>，<code>z = z</code>。范围一般取 <code>r ≥ 0</code>、<code>0 ≤ θ &lt; 2π</code>、<code>z ∈ ℝ</code>（z 就是高度，可负）。')
  + p('柱坐标的坐标面（coordinate surfaces）：<code>r = 常数</code> 是圆柱面，<code>θ = 常数</code> 是过 z 轴的半平面，<code>z = 常数</code> 是水平平面。')
  + p('体积微元：<code>dV = r dr dθ dz</code>。那个多出的 r 是雅可比行列式（Jacobian）的绝对值，来源是极坐标面积微元 <code>r dr dθ</code>。')
  + h3('2.2 球坐标 spherical coordinates')
  + p('用「到原点的距离 ρ」与两个角度定位：')
  + p('<b><code>x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ</code></b>')
  + p('其中 <code>ρ ≥ 0</code> 是径向距离，<code>φ ∈ [0, π]</code> 是<b>与正 z 轴的夹角</b>（极角 / polar angle），<code>θ ∈ [0, 2π)</code> 是方位角（azimuthal angle）。')
  + cal('warn', '最容易错的一点', 'φ 是从 <b>z 轴</b> 量起的，不是从 xy 平面。所以 <code>z = ρ cos φ</code>，而 <code>r = ρ sin φ</code>。把 φ 与「与 xy 平面的夹角」弄反，整个公式全错。')
  + p('反变换：<code>ρ = √(x²+y²+z²)</code>，<code>cos φ = z/ρ</code>，<code>tan θ = y/x</code>。')
  + p('体积微元：<code>dV = ρ² sin φ dρ dφ dθ</code>。两个因子 ρ² 与 sin φ 缺一不可。')
  + h3('2.3 三种坐标下的典型曲面')
  + tb(('曲面', '直角坐标', '柱坐标', '球坐标'),
       ('圆柱面', 'x²+y² = a²', 'r = a', 'ρ sin φ = a'),
       ('球面', 'x²+y²+z² = a²', 'r²+z² = a²', 'ρ = a'),
       ('锥面（顶角 2α）', 'z² = k²(x²+y²)', 'z = kr', 'φ = α'),
       ('水平平面', 'z = c', 'z = c', 'ρ cos φ = c'),
       ('过 z 轴的半平面', 'y = x tan θ₀', 'θ = θ₀', 'θ = θ₀'))
  + cal('tip', '选题口诀', '球面或锥面 → 球坐标；圆柱面或绕 z 轴的对称 → 柱坐标；平面直角边界（长方体）→ 直角坐标。选对坐标能把三重积分降成一次单重积分。'),
 kws=K(('cylindrical coordinates', '柱坐标', 'x = r cos θ, y = r sin θ, z = z.'),
       ('spherical coordinates', '球坐标', 'x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ.'),
       ('polar angle', '极角 φ', 'The angle measured from the positive z-axis.'),
       ('azimuthal angle', '方位角 θ', 'The angle measured in the xy-plane from the positive x-axis.'),
       ('coordinate surface', '坐标面', 'r = const, θ = const, z = const.'),
       ('Jacobian', '雅可比', 'The factor r (or ρ² sin φ) in the volume element.'),
       ('volume element', '体积微元', 'dV = r dr dθ dz or dV = ρ² sin φ dρ dφ dθ.')),
 examples=(qa('例 1　把点 P(1, √3, 2) 从直角坐标换成柱坐标与球坐标。',
   p('柱坐标：<code>r = √(1+3) = 2</code>，<code>θ = arctan(√3/1) = π/3</code>（第一象限），<code>z = 2</code>。所以 (2, π/3, 2)。')
   + p('球坐标：<code>ρ = √(1+3+4) = 2√2</code>，<code>cos φ = z/ρ = 2/(2√2) = 1/√2</code> 得 <code>φ = π/4</code>，<code>θ = π/3</code>。')
   + p('检验：<code>ρ sin φ = 2√2 · 1/√2 = 2 = r</code> ✓。'))
  + qa('例 2　把 x² + y² + z² = 4z 化为球坐标方程，并说出它是什么曲面。',
   p('代入 <code>x²+y²+z² = ρ²</code>、<code>z = ρ cos φ</code>，得 <code>ρ² = 4ρ cos φ</code>。')
   + p('<code>ρ = 0</code> 是原点，其余点约去 ρ：<code>ρ = 4cos φ</code>。')
   + p('它是球心 (0,0,2)、半径 2 的球面（把原式配方：<code>x²+y²+(z−2)² = 4</code>）。'))),
 practice=(ol('把 <code>z = x² + y²</code> 化为柱坐标方程。',
        '求球坐标下 <code>φ = π/3</code> 对应的直角坐标曲面。',
        '把 <code>r = 2cos θ</code>（柱坐标）写成直角坐标方程。',
        '半径为 2 的球体内，用球坐标写出体积积分式（不需求值）。')
  + det('答案与思路',
   p('<b>1.</b> <code>z = r²</code>。这是一个开口向上的旋转抛物面。')
   + p('<b>2.</b> <code>cos φ = 1/2</code>，由 <code>z = ρ cos φ</code>、<code>r = ρ sin φ</code> 得 <code>z = r/√3</code>，平方得 <code>z² = (x²+y²)/3</code>，即顶角 60° 的锥面。')
   + p('<b>3.</b> 两边乘 r 得 <code>r² = 2r cos θ</code>，即 <code>x²+y² = 2x</code>，即 <code>(x−1)²+y² = 1</code>，一个圆柱面。')
   + p('<b>4.</b> <code>∫₀^{2π}∫₀^{π}∫₀^{2} ρ² sin φ dρ dφ dθ</code>。')),
 exam=(p(badge('bad', '必考') + '三种坐标的互换、把曲面写成最简坐标方程、写对体积微元。')
  + p(badge('warn', '易错 1') + '<b>球坐标 φ 的起算轴弄反</b>。φ 从 z 轴量起，<code>z = ρcos φ</code>。')
  + p(badge('warn', '易错 2') + '<b>漏写雅可比因子</b>。柱坐标漏 r、球坐标漏 ρ²sin φ，积分值会差一个量级。')
  + p(badge('warn', '易错 3') + '<b>θ 象限判断错</b>。用 <code>arctan(y/x)</code> 只给主值，x &lt; 0 时要加 π。')
  + p(badge('mute', '进阶') + '球坐标下「锥面 φ = α + 球面 ρ = a」围成的区域，俗称冰淇淋筒形区域，是三重积分最常见的考题。')),
 checklist=(h2('坐标转换清单')
  + st('先算 ρ（或 r），再算角，最后算 z（或 φ）',
       '判断 θ 所在象限：看 x、y 的符号',
       '球坐标用 <code>cos φ = z/ρ</code> 比用 sin 更稳（不会有符号歧义）',
       '写体积微元前先确认用什么坐标，把雅可比因子一并写上',
       '化简曲面方程时注意 ρ = 0 的点，必要时单独讨论')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture1.pdf', '全篇', '柱坐标、球坐标定义与互换、坐标面、体积微元'),
   ('（补充）', '—', '三种坐标选择口诀与冰淇淋筒形区域说法为衔接性补充'))))

# ============================================================ 3
LEC.append(L(
 slug='t2-matrices',
 tzh='Topic 2 · 矩阵、运算与线性变换',
 ten='Matrices, Operations on Matrices, Special Matrices, and Transformations',
 keywords=['matrix', 'entry', 'matrix multiplication', 'transpose', 'identity matrix', 'inverse', 'linear transformation'],
 files=['Topic 2/EMII_Week2_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('矩阵是把「一组线性关系」写成一张表。它既是方程组的紧凑写法，也是线性变换（旋转、缩放、投影）的坐标表示。本节先把矩阵当数据结构定清楚，再学四种基本运算，最后把它当「函数」用。')
  + p('学完本节你应当能够：')
  + ck('说出矩阵的阶、元素、行、列、主对角线',
     '做加法、数乘、乘法、转置，并判断哪些运算合法',
     '识别单位阵、零阵、对角阵、三角阵、对称阵',
     '把平面/空间的线性变换写成矩阵并作用于向量')),
 detail=(h3('3.1 矩阵的定义与记号')
  + p('一个 <b>m × n</b> 矩阵是 m 行 n 列的数表，元素记 <code>a_ij</code>（第 i 行第 j 列）。行数与列数相等时称<b>方阵</b>（square matrix），方阵从左上到右下的一排元素称<b>主对角线</b>（main diagonal）。')
  + p('两个矩阵相等当且仅当阶相同且每个对应元素相等——这一条是解矩阵方程的基本工具。')
  + h3('3.2 加法与数乘')
  + p('加法：同阶矩阵对应元素相加。数乘：每个元素乘以该数。两者合起来说明矩阵构成一个向量空间。')
  + p('两条必记性质：<code>A + B = B + A</code>（交换），<code>A(BC) = (AB)C</code>（乘法结合，前提是阶数能乘）。')
  + h3('3.3 矩阵乘法')
  + p('若 A 是 <b>m × p</b>、B 是 <b>p × n</b>，则 AB 是 <b>m × n</b>，且')
  + p('<b><code>(AB)_ij = Σ_{k=1..p} a_ik · b_kj</code></b>')
  + p('口诀：<b>「行乘列，加起来」</b>。左矩阵取一行，右矩阵取一列，对应元素相乘再求和。')
  + cal('warn', '三条打破直觉的性质', '(1) <code>AB ≠ BA</code>，乘法不交换；(2) <code>AB = 0</code> 不能推出 A = 0 或 B = 0；(3) <code>AB = AC</code> 且 A ≠ 0 也不能约去 A。这三条是选择题的高频陷阱。')
  + p('运算律中成立的部分：<code>A(BC) = (AB)C</code>、<code>A(B+C) = AB+AC</code>、<code>(A+B)C = AC+BC</code>、<code>(AB)ᵀ = BᵀAᵀ</code>（注意顺序颠倒）。')
  + h3('3.4 特殊矩阵')
  + tb(('名称', '特征', '作用'),
       ('零阵 O', '所有元素为 0', '加法单位元'),
       ('单位阵 I', '主对角为 1，其余 0', '<code>AI = IA = A</code>'),
       ('对角阵 diag(d₁…dₙ)', '非主对角均为 0', '相当于各方向分别缩放'),
       ('上/下三角阵', '对角线一侧全为 0', '行列式等于对角线乘积'),
       ('对称阵', '<code>Aᵀ = A</code>', '可正交对角化'),
       ('反对称阵', '<code>Aᵀ = −A</code>', '主对角必为 0'))
  + h3('3.5 线性变换')
  + p('矩阵作用于向量：<code>A x</code> 得到新向量。几何上：')
  + ul('<b>缩放</b>：<code>diag(s₁, s₂)</code> 把 (x,y) 变为 (s₁x, s₂y)',
      '<b>旋转 θ</b>：<code>[[cos θ, −sin θ],[sin θ, cos θ]]</code>',
      '<b>关于 x 轴反射</b>：<code>[[1,0],[0,−1]]</code>',
      '<b>关于 y = x 反射</b>：<code>[[0,1],[1,0]]</code>',
      '<b>投影到 x 轴</b>：<code>[[1,0],[0,0]]</code>')
  + p('判别技巧：看基向量 e₁ = (1,0)、e₂ = (0,1) 被送到哪里，那两列就是矩阵的两列。'),
 kws=K(('matrix', '矩阵', 'A rectangular array of numbers.'),
       ('order / dimension', '阶', 'An m × n matrix has m rows and n columns.'),
       ('entry / element', '元素', 'a_ij denotes the entry in row i, column j.'),
       ('transpose', '转置', '(Aᵀ)_ij = a_ji.'),
       ('identity matrix', '单位阵', 'The matrix I with ones on the diagonal.'),
       ('singular / non-singular', '奇异 / 非奇异', 'A singular matrix has no inverse.'),
       ('linear transformation', '线性变换', 'A map x ↦ Ax.'),
       ('rotation matrix', '旋转矩阵', '[[cos θ, −sin θ],[sin θ, cos θ]].')),
 examples=(qa('例 1　A = [[1,2],[3,4]]，B = [[0,1],[1,0]]，求 AB 与 BA。',
   p('AB = [[1·0+2·1, 1·1+2·0],[3·0+4·1, 3·1+4·0]] = [[2,1],[4,3]]。')
   + p('BA = [[0·1+1·3, 0·2+1·4],[1·1+0·3, 1·2+0·4]] = [[3,4],[1,2]]。')
   + p('结论：AB ≠ BA，乘法的不可交换性具体可见。注意 B 只是一个「交换 x 与 y」的变换。'))
  + qa('例 2　证明 AB = 0 但 A、B 均非零。',
   p('取 A = [[1,0],[0,0]]，B = [[0,0],[1,0]]。AB = [[0,0],[0,0]]。')
   + p('几何解释：A 把一切投影到 x 轴，B 把 y 轴方向映射到 x 轴之外…… 具体地说 B 的输出只有 y 分量，而 A 把 y 分量全部丢弃，故复合为零。'))
  + qa('例 3　求把平面绕原点逆时针旋转 90° 的矩阵，并作用于 (2, 3)。',
   p('θ = π/2：<code>cos = 0, sin = 1</code>，矩阵 <code>R = [[0,−1],[1,0]]</code>。')
   + p('<code>R(2,3)ᵀ = (0·2 + (−1)·3, 1·2 + 0·3)ᵀ = (−3, 2)ᵀ</code>。检验：长度仍为 √13 ✓。'))),
 practice=(ol('A 是 2×3，B 是 3×4，AB 是什么阶？BA 能乘吗？',
        '求 <code>[[1,2],[3,4]]</code> 的转置，并验证它是否对称。',
        '设 A = [[2,1],[1,2]]，求 <code>A² − 4A + 3I</code>。',
        '写出「关于 y 轴反射」的矩阵。')
  + det('答案与思路',
   p('<b>1.</b> AB 是 2×4。BA 需要 B 的列数 4 等于 A 的行数 2，不成立，不能乘。')
   + p('<b>2.</b> 转置为 <code>[[1,3],[2,4]]</code>，与原矩阵不等，不对称。注意 <code>[[1,2],[2,1]]</code> 才是对称的。')
   + p('<b>3.</b> <code>A² = [[5,4],[4,5]]</code>；<code>4A = [[8,4],[4,8]]</code>；<code>3I = [[3,0],[0,3]]</code>。相加减得 <code>[[0,0],[0,0]]</code>。这正说明 A 满足自己的特征方程 <code>λ² − 4λ + 3 = 0</code>。')
   + p('<b>4.</b> e₁ = (1,0) → (−1,0)，e₂ → (0,1)，所以矩阵 <code>[[−1,0],[0,1]]</code>。')),
 exam=(p(badge('bad', '必考') + '矩阵乘法（尤其阶数检查与顺序）、转置性质、线性变换矩阵的构造。')
  + p(badge('warn', '易错 1') + '把 <code>(AB)ᵀ</code> 写成 <code>AᵀBᵀ</code>。正确是 <code>BᵀAᵀ</code>。')
  + p(badge('warn', '易错 2') + '乘法时行列对错位。建议先写出结果矩阵的阶，再逐个格子算。')
  + p(badge('warn', '易错 3') + '以为 <code>AB = 0</code> 能推出 A 或 B 为零。')
  + p(badge('mute', '进阶') + '旋转矩阵的行列式为 1，反射矩阵为 −1，这是判断「保向还是反向」的快捷方法。')),
 checklist=(h2('矩阵运算检查清单')
  + st('先写阶：确认 m×p 与 p×n 能乘，结果 m×n',
       '算每个元素前，把左矩阵第 i 行与右矩阵第 j 列并排写在草稿上',
       '逐项乘加，不要跳项；p 较大时分两遍验算',
       '涉及转置时，先把括号顺序倒过来再展开',
       '用单位阵 I 做自检：<code>AI</code> 应该还等于 A')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 2/EMII_Week2_Lecture2.pdf', '全篇', '矩阵定义、加法与数乘、乘法、特殊矩阵、线性变换'),
   ('（补充）', '—', '旋转/反射/投影矩阵的具体形式与「看基向量」技巧为补充'))))

# ============================================================ 4
LEC.append(L(
 slug='t3-determinant-inverse',
 tzh='Topic 3 · 行列式、伴随矩阵与逆矩阵',
 ten='Determinant, Adjugate and Inverse of Square Matrix, System of Linear Equations',
 keywords=['determinant', 'cofactor', 'adjugate', 'inverse matrix', 'singular matrix', 'system of linear equations'],
 files=['Topic 3/EMII_Week3_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('上一节说矩阵「能乘」，这一节回答「能不能除」。方阵可逆的充要条件是行列式非零，而逆矩阵又可以直接写出线性方程组的解。三件事——行列式、伴随、逆——是一条链。')
  + p('学完本节你应当能够：')
  + ck('用展开法算 2×2、3×3 及更高阶行列式',
     '求余子式、代数余子式与伴随矩阵',
     '用 <code>A⁻¹ = adj(A)/det(A)</code> 求二阶三阶逆阵',
     '用逆矩阵解 <code>Ax = b</code> 型方程组')),
 detail=(h3('4.1 行列式的定义与性质')
  + p('行列式 det(A) 或 |A| 是方阵到实数的一个函数，几何意义是「该线性变换对面积/体积的伸缩倍数」，符号表示是否保向。')
  + p('二阶：<b><code>|a b; c d| = ad − bc</code></b>。这是后面所有公式的基石。')
  + p('三阶可用对角线法则（Sarrus）：主对角三积之和，减去副对角三积之和。')
  + p('高阶用<b>余子式展开</b>（cofactor expansion），沿任意一行或一列展开结果相同：')
  + p('<b><code>det(A) = Σ_j a_ij · C_ij</code></b>，其中 <code>C_ij = (−1)^{i+j} M_ij</code>，M_ij 是删去第 i 行第 j 列后的子行列式。')
  + p('必记性质：')
  + ul('两行互换 → 行列式变号',
      '某行乘 k → 行列式乘 k',
      '两行成比例（含某行为零） → 行列式为 0',
      '某行加上另一行的倍数 → 行列式不变',
      '<code>det(AB) = det(A)det(B)</code>',
      '<code>det(Aᵀ) = det(A)</code>',
      '三角阵（上或下）的行列式 = 主对角线元素之积')
  + cal('tip', '计算策略', '永远先用行变换把矩阵化成三角阵，再把对角线相乘。直接展开 4×4 要算 24 项，用行变换只需几次加减。')
  + h3('4.2 伴随矩阵与逆矩阵')
  + p('逆矩阵 A⁻¹ 满足 <code>AA⁻¹ = A⁻¹A = I</code>。存在条件：<b>det(A) ≠ 0</b>（此时称 A 非奇异 non-singular）。')
  + p('伴随矩阵 adj(A) 是「代数余子式矩阵的转置」：<code>adj(A)_ij = C_ji</code>。注意转置这一步最容易被漏。')
  + p('<b><code>A⁻¹ = adj(A) / det(A)</code></b>')
  + p('二阶有速算式：若 <code>A = [[a,b],[c,d]]</code>，则 <code>A⁻¹ = (1/(ad−bc))·[[d,−b],[−c,a]]</code>——主对角互换、副对角变号、除以行列式。')
  + p('性质：<code>(A⁻¹)⁻¹ = A</code>、<code>(AB)⁻¹ = B⁻¹A⁻¹</code>、<code>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</code>、<code>det(A⁻¹) = 1/det(A)</code>。')
  + h3('4.3 用逆矩阵解方程组')
  + p('把 <code>a₁₁x + a₁₂y = b₁</code>、<code>a₂₁x + a₂₂y = b₂</code> 写成 <code>Ax = b</code>。若 det(A) ≠ 0，两边左乘 A⁻¹：')
  + p('<b><code>x = A⁻¹ b</code></b>')
  + p('注意左乘而非右乘——矩阵乘法不交换。这也解释了为何 A 必须可逆：det(A) = 0 时变换把平面压成一条线，信息丢失，无法反推。'),
 kws=K(('determinant', '行列式', 'det(A) measures the scaling factor of the transformation.'),
       ('minor', '余子式', 'M_ij is the determinant after deleting row i and column j.'),
       ('cofactor', '代数余子式', 'C_ij = (−1)^{i+j} M_ij.'),
       ('adjugate matrix', '伴随矩阵', 'The transpose of the cofactor matrix.'),
       ('inverse matrix', '逆矩阵', 'A⁻¹ exists iff det(A) ≠ 0.'),
       ('singular', '奇异的', 'A square matrix with det(A) = 0.'),
       ('non-singular', '非奇异的', 'A square matrix with det(A) ≠ 0.'),
       ('cofactor expansion', '余子式展开', 'Expand along any row or column.')),
 examples=(qa('例 1　求 A = [[1,2,3],[0,1,4],[5,6,0]] 的行列式。',
   p('沿第一列展开：<code>det = 1·|1 4; 6 0| − 0·|2 3; 6 0| + 5·|2 3; 1 4|</code>。')
   + p('<code>= 1·(0−24) − 0 + 5·(8−3) = −24 + 25 = 1</code>。')
   + p('行列式非零，故 A 可逆。'))
  + qa('例 2　求 A = [[2,1],[1,3]] 的逆矩阵，并用它解 2x+y=5、x+3y=10。',
   p('<code>det = 2·3 − 1·1 = 5</code>。二阶速算：主对角互换、副对角变号 → <code>[[3,−1],[−1,2]]</code>，除 5 得 <code>A⁻¹ = (1/5)[[3,−1],[−1,2]]</code>。')
   + p('<code>x = A⁻¹b = (1/5)(3·5 − 1·10, −1·5 + 2·10) = (1/5)(5, 15) = (1, 3)</code>。')
   + p('验算：2·1 + 3 = 5 ✓；1 + 3·3 = 10 ✓。'))
  + qa('例 3　求点 (2,1) 关于直线 y = x 的对称点。',
   p('反射矩阵 <code>R = [[0,1],[1,0]]</code>，<code>R(2,1)ᵀ = (1,2)ᵀ</code>。')
   + p('也可用「det = −1 表示反向」自检：反射把面积取向翻转。'))),
 practice=(ol('求 <code>|3 1; 2 4|</code> 与 <code>|1 0 2; 0 3 0; 4 0 1|</code>。',
        '求 <code>[[1,2],[3,4]]</code> 的伴随矩阵与逆矩阵。',
        'k 取何值时 <code>[[k,2],[3,6]]</code> 不可逆？',
        '验证 <code>det(AB) = det(A)det(B)</code>，其中 A = [[1,2],[3,4]]、B = [[0,1],[1,1]]。')
  + det('答案与思路',
   p('<b>1.</b> <code>3·4 − 1·2 = 10</code>；第二个沿第二行展开：<code>3·|1 2; 4 1| = 3·(1−8) = −21</code>（注意符号 (−1)^{2+2} = +1）。')
   + p('<b>2.</b> det = 4−6 = −2。代数余子式矩阵 <code>[[4,−3],[−2,1]]</code>，转置得 adj = <code>[[4,−2],[−3,1]]</code>，除 −2 得 <code>[[−2,1],[1.5,−0.5]]</code>。')
   + p('<b>3.</b> det = 6k − 6 = 0 → k = 1。此时两行成比例。')
   + p('<b>4.</b> det(A) = −2，det(B) = −1，AB = [[2,3],[4,7]]，det(AB) = 14−12 = 2 = (−2)(−1) ✓。')),
 exam=(p(badge('bad', '必考') + '3×3 行列式计算、二阶逆矩阵公式、判断可逆性、用逆阵解二元方程组。')
  + p(badge('warn', '易错 1') + '<b>伴随矩阵忘了转置</b>。adj(A) 是代数余子式矩阵的<b>转置</b>。')
  + p(badge('warn', '易错 2') + '<b>行变换后忘了记录符号变化</b>。换行变号、乘行变倍数，要用笔记下来。')
  + p(badge('warn', '易错 3') + '<b>解方程时右乘 A⁻¹</b>。必须左乘。')
  + p(badge('mute', '进阶') + '克莱姆法则（下节）本质就是 <code>x_i = det(A_i)/det(A)</code>，与逆矩阵公式同源。')),
 checklist=(h2('行列式与逆矩阵清单')
  + st('先看阶数：2×2 直接 ad−bc；3×3 优先行变换化三角',
       '行变换三种操作分别对应「变号 / 乘倍数 / 不变」',
       '化成三角后对角线连乘得 det',
       'det = 0 → 停止，直接答「不可逆」',
       '求逆：算代数余子式 → 排成矩阵 → 转置 → 除以 det',
       '最后用 <code>AA⁻¹ = I</code> 验算一两个元素')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture1.pdf', '全篇', '行列式定义与性质、余子式与代数余子式、伴随矩阵、逆矩阵、线性方程组'),
   ('（补充）', '—', '二阶速算公式与「左乘」提醒为实操性补充'))))

# ============================================================ 5
LEC.append(L(
 slug='t3-gauss-eigen',
 tzh='Topic 3 · 高斯消元、特征值与克莱姆法则',
 ten="Gaussian Elimination, Trivial and Non-trivial Solutions, Eigenvalues, Cramer's Rule",
 keywords=['augmented matrix', 'row echelon form', 'Gaussian elimination', 'trivial solution', 'eigenvalue', 'eigenvector', "Cramer's rule"],
 files=['Topic 3/EMII_Week3_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('上一节用逆矩阵解方程，但求逆代价高且只适用于方阵。本节给出更通用的工具：高斯消元能解任意规模的方程组，并从消元结果直接读出「有唯一解 / 无穷多解 / 无解」。随后引入特征值——让 <code>Ax</code> 与 <code>x</code> 平行的那些特殊方向。')
  + p('学完本节你应当能够：')
  + ck('写出增广矩阵并用初等行变换化成行阶梓形',
     '由秩判定方程组解的情况',
     '区分平凡解与非平凡解',
     '求 2×2、3×3 矩阵的特征值与特征向量',
     '用克莱姆法则写出解的公式')),
 detail=(h3('5.1 增广矩阵与初等行变换')
  + p('把 <code>Ax = b</code> 的系数与常数项并排写成<b>增广矩阵</b>（augmented matrix）<code>[A | b]</code>。允许的三种初等行变换：')
  + ol('交换两行', '某行乘以非零常数', '某行加上另一行的倍数')
  + p('这三种变换不改变方程组的解集，而能把矩阵化为<b>行阶梓形</b>（row echelon form，REF）：每行首个非零元（主元 pivot）逐行右移，主元下方全为 0。')
  + h3('5.2 高斯消元与解的情况')
  + p('步骤：自上而下消元 → 得到上三角 → 自下而上回代（back substitution）。')
  + p('解的情况由<b>秩</b>（rank，非零行数）决定：')
  + tb(('关系', '结论', '几何'),
       ('rank(A) = rank([A|b]) = n', '唯一解', '直线/平面交于一点'),
       ('rank(A) = rank([A|b]) &lt; n', '无穷多解（含 n − rank 个自由变量）', '交于一条线或一个面'),
       ('rank(A) &lt; rank([A|b])', '无解', '平行不相交'))
  + cal('warn', '关键判别', '看最后一列能不能出现主元。若消元后出现形如 <code>[0 0 … 0 | c]</code> 且 <code>c ≠ 0</code> 的行，即为 <code>0 = c</code> 矛盾，立刻无解。')
  + h3('5.3 齐次方程组与平凡解')
  + p('形如 <code>Ax = 0</code> 的方程组称<b>齐次</b>（homogeneous）。它永远有<b>平凡解</b>（trivial solution）<code>x = 0</code>。')
  + p('<b>存在非平凡解</b>（non-trivial solution）的充要条件是 <code>det(A) = 0</code>（对方阵），等价于 <code>rank(A) &lt; n</code>。这一条与下一小节的特征值方程同构，非常重要。')
  + h3('5.4 特征值与特征向量')
  + p('若存在非零向量 x 与标量 λ 使 <b><code>Ax = λx</code></b>，则 λ 为<b>特征值</b>（eigenvalue），x 为对应的<b>特征向量</b>（eigenvector）。')
  + p('把式子移项：<code>(A − λI)x = 0</code>。要求有非零解，由上节结论得 <b><code>det(A − λI) = 0</code></b>——这就是<b>特征方程</b>（characteristic equation）。')
  + p('求解顺序：解特征方程得 λ → 每个 λ 代回 <code>(A − λI)x = 0</code> → 解齐次方程组得特征向量（只到比例常数，归一化即可）。')
  + cal('tip', '快速验算', '所有特征值之和 = 主对角线之和（迹 trace）；所有特征值之积 = 行列式。这两条能在考试中立刻发现算错。')
  + h3("5.5 克莱姆法则 Cramer's rule")
  + p('若 A 为 n×n 且 det(A) ≠ 0，则 <code>Ax = b</code> 的解为')
  + p('<b><code>x_i = det(A_i) / det(A)</code></b>，其中 A_i 是把 A 的第 i 列换成 b 得到的矩阵。')
  + p('优点：直接给出公式，不用消元。缺点：需要算 n+1 个行列式，n ≥ 3 时比消元慢；且只适用于「方程数 = 未知数且 det ≠ 0」的情形。'),
 kws=K(('augmented matrix', '增广矩阵', 'The matrix [A | b].'),
       ('elementary row operation', '初等行变换', 'Swap, scale, or add a multiple of a row.'),
       ('row echelon form', '行阶梓形', 'Pivots move right as you go down.'),
       ('pivot', '主元', 'The first non-zero entry of a row.'),
       ('rank', '秩', 'The number of non-zero rows after elimination.'),
       ('trivial solution', '平凡解', 'x = 0 always solves Ax = 0.'),
       ('eigenvalue', '特征值', 'λ with det(A − λI) = 0.'),
       ('characteristic equation', '特征方程', 'det(A − λI) = 0.'),
       ("Cramer's rule", '克莱姆法则', 'x_i = det(A_i)/det(A).')),
 examples=(qa('例 1　解 x + 2y + z = 4、2x + 5y + 3z = 11、x + y = 3。',
   p('增广矩阵：<code>[1 2 1 | 4; 2 5 3 | 11; 1 1 0 | 3]</code>。')
   + p('R2 − 2R1：<code>[0 1 1 | 3]</code>；R3 − R1：<code>[0 −1 −1 | −1]</code>。')
   + p('R3 + R2：<code>[0 0 0 | 2]</code>，出现 <code>0 = 2</code>，矛盾 → <b>无解</b>。')
   + p('几何解释：三个平面没有公共交点。'))
  + qa('例 2　求 A = [[3,1],[0,2]] 的特征值与特征向量。',
   p('特征方程 <code>|3−λ, 1; 0, 2−λ| = (3−λ)(2−λ) = 0</code>，得 λ = 3 或 2。')
   + p('λ = 3：<code>(A−3I)x = [[0,1],[0,−1]]x = 0</code> 得 <code>y = 0</code>，取 x = (1,0)。')
   + p('λ = 2：<code>[[1,1],[0,0]]x = 0</code> 得 <code>x + y = 0</code>，取 (1,−1)。')
   + p('验算：迹 = 5 = 3+2 ✓；行列式 = 6 = 3·2 ✓。'))
  + qa('例 3　用克莱姆法则解 2x + y = 5、x + 3y = 10。',
   p('<code>det(A) = 5</code>。<code>det(A₁) = |5 1; 10 3| = 15−10 = 5</code>，故 <code>x = 1</code>。')
   + p('<code>det(A₂) = |2 5; 1 10| = 20−5 = 15</code>，故 <code>y = 3</code>。'))),
 practice=(ol('判断 <code>x+y=2</code>、<code>2x+2y=4</code> 的解的情况。',
        '求 <code>[[2,0],[0,3]]</code> 的特征值。',
        '求 <code>[[1,2],[2,1]]</code> 的特征值与特征向量。',
        '用消元法解 <code>x + y + z = 6</code>、<code>2x − y = 0</code>、<code>y + 2z = 8</code>。')
  + det('答案与思路',
   p('<b>1.</b> 第二式是第一式两倍，rank = 1 &lt; 2，<b>无穷多解</b>：<code>y = 2 − x</code>，x 自由。')
   + p('<b>2.</b> 对角阵的特征值就是对角元：2 与 3，特征向量 e₁、e₂。')
   + p('<b>3.</b> <code>(1−λ)² − 4 = 0</code> 得 <code>λ² − 2λ − 3 = 0</code>，λ = 3 或 −1。λ=3 得 (−1,1)… 具体：<code>(A−3I) = [[−2,2],[2,−2]]</code>，得 <code>x = y</code>，取 (1,1)；λ=−1 得 <code>x = −y</code>，取 (1,−1)。')
   + p('<b>4.</b> 由第二式 <code>x = y/2</code>。代入第一式：<code>3y/2 + z = 6</code>。与第三式联立：<code>y + 2z = 8</code>。解得 <code>y = 2, z = 3, x = 1</code>。验算全部成立。')),
 exam=(p(badge('bad', '必考') + '消元判解的情况、特征值特征向量的完整流程、克莱姆法则公式。')
  + p(badge('warn', '易错 1') + '<b>把「无穷多解」写成「无解」</b>。看到全零行且常数也为 0，是无穷多解，不是无解。')
  + p(badge('warn', '易错 2') + '<b>特征向量忘了求全部</b>。求出 λ 后必须回代解齐次方程，只写 λ 不完整。')
  + p(badge('warn', '易错 3') + '<b>克莱姆法则用在 det = 0 的矩阵上</b>。此时法则失效，须改用消元。')
  + p(badge('mute', '进阶') + '特征值在工程上对应「主方向与主伸缩」：振动模态、主成分分析、稳定性判定都靠它。')),
 checklist=(h2('解方程组与特征值清单')
  + st('写成增广矩阵，标出目标：上三角 or 行阶梓形',
       '选主元：优先选绝对值大且便于消元的行',
       '逐列向下消元，记录每步行变换',
       '消完看最后几行：全零行为自由变量行；<code>[0…0|c]</code> 为无解',
       '回代求各变量',
       '特征值题：先写 det(A−λI)=0 展开，再用迹与行列式验算')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture2.pdf', '全篇', '高斯消元、行阶梓形、平凡/非平凡解、特征值与特征向量、克莱姆法则'),
   ('（补充）', '—', '秩与解的情况对应表、迹与行列式验算法为补充'))))

# ============================================================ 4
LEC.append(L(
 slug='t3-determinant-inverse',
 tzh='Topic 3 · 行列式、伴随矩阵与逆矩阵',
 ten='Determinant, Adjugate and Inverse of Square Matrix, System of Linear Equations',
 keywords=['determinant', 'cofactor', 'adjugate', 'inverse matrix', 'singular matrix', 'system of linear equations'],
 files=['Topic 3/EMII_Week3_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('上一节说矩阵「能乘」，这一节回答「能不能除」。方阵可逆的充要条件是行列式非零，而逆矩阵又可以直接写出线性方程组的解。三件事——行列式、伴随、逆——是一条链。')
  + p('学完本节你应当能够：')
  + ck('用展开法算 2×2、3×3 及更高阶行列式',
     '求余子式、代数余子式与伴随矩阵',
     '用 <code>A⁻¹ = adj(A)/det(A)</code> 求二阶三阶逆阵',
     '用逆矩阵解 <code>Ax = b</code> 型方程组')),
 detail=(h3('4.1 行列式的定义与性质')
  + p('行列式 det(A) 或 |A| 是方阵到实数的一个函数，几何意义是「该线性变换对面积/体积的伸缩倍数」，符号表示是否保向。')
  + p('二阶：<b><code>|a b; c d| = ad − bc</code></b>。这是后面所有公式的基石。')
  + p('三阶可用对角线法则（Sarrus）：主对角三积之和，减去副对角三积之和。')
  + p('高阶用<b>余子式展开</b>（cofactor expansion），沿任意一行或一列展开结果相同：')
  + p('<b><code>det(A) = Σ_j a_ij · C_ij</code></b>，其中 <code>C_ij = (−1)^{i+j} M_ij</code>，M_ij 是删去第 i 行第 j 列后的子行列式。')
  + p('必记性质：')
  + ul('两行互换 → 行列式变号',
      '某行乘 k → 行列式乘 k',
      '两行成比例（含某行为零） → 行列式为 0',
      '某行加上另一行的倍数 → 行列式不变',
      '<code>det(AB) = det(A)det(B)</code>',
      '<code>det(Aᵀ) = det(A)</code>',
      '三角阵（上或下）的行列式 = 主对角线元素之积')
  + cal('tip', '计算策略', '永远先用行变换把矩阵化成三角阵，再把对角线相乘。直接展开 4×4 要算 24 项，用行变换只需几次加减。')
  + h3('4.2 伴随矩阵与逆矩阵')
  + p('逆矩阵 A⁻¹ 满足 <code>AA⁻¹ = A⁻¹A = I</code>。存在条件：<b>det(A) ≠ 0</b>（此时称 A 非奇异 non-singular）。')
  + p('伴随矩阵 adj(A) 是「代数余子式矩阵的转置」：<code>adj(A)_ij = C_ji</code>。注意转置这一步最容易被漏。')
  + p('<b><code>A⁻¹ = adj(A) / det(A)</code></b>')
  + p('二阶有速算式：若 <code>A = [[a,b],[c,d]]</code>，则 <code>A⁻¹ = (1/(ad−bc))·[[d,−b],[−c,a]]</code>——主对角互换、副对角变号、除以行列式。')
  + p('性质：<code>(A⁻¹)⁻¹ = A</code>、<code>(AB)⁻¹ = B⁻¹A⁻¹</code>、<code>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</code>、<code>det(A⁻¹) = 1/det(A)</code>。')
  + h3('4.3 用逆矩阵解方程组')
  + p('把 <code>a₁₁x + a₁₂y = b₁</code>、<code>a₂₁x + a₂₂y = b₂</code> 写成 <code>Ax = b</code>。若 det(A) ≠ 0，两边左乘 A⁻¹：')
  + p('<b><code>x = A⁻¹ b</code></b>')
  + p('注意左乘而非右乘——矩阵乘法不交换。这也解释了为何 A 必须可逆：det(A) = 0 时变换把平面压成一条线，信息丢失，无法反推。'),
 kws=K(('determinant', '行列式', 'det(A) measures the scaling factor of the transformation.'),
       ('minor', '余子式', 'M_ij is the determinant after deleting row i and column j.'),
       ('cofactor', '代数余子式', 'C_ij = (−1)^{i+j} M_ij.'),
       ('adjugate matrix', '伴随矩阵', 'The transpose of the cofactor matrix.'),
       ('inverse matrix', '逆矩阵', 'A⁻¹ exists iff det(A) ≠ 0.'),
       ('singular', '奇异的', 'A square matrix with det(A) = 0.'),
       ('non-singular', '非奇异的', 'A square matrix with det(A) ≠ 0.'),
       ('cofactor expansion', '余子式展开', 'Expand along any row or column.')),
 examples=(qa('例 1　求 A = [[1,2,3],[0,1,4],[5,6,0]] 的行列式。',
   p('沿第一列展开：<code>det = 1·|1 4; 6 0| − 0·|2 3; 6 0| + 5·|2 3; 1 4|</code>。')
   + p('<code>= 1·(0−24) − 0 + 5·(8−3) = −24 + 25 = 1</code>。')
   + p('行列式非零，故 A 可逆。'))
  + qa('例 2　求 A = [[2,1],[1,3]] 的逆矩阵，并用它解 2x+y=5、x+3y=10。',
   p('<code>det = 2·3 − 1·1 = 5</code>。二阶速算：主对角互换、副对角变号 → <code>[[3,−1],[−1,2]]</code>，除 5 得 <code>A⁻¹ = (1/5)[[3,−1],[−1,2]]</code>。')
   + p('<code>x = A⁻¹b = (1/5)(3·5 − 1·10, −1·5 + 2·10) = (1/5)(5, 15) = (1, 3)</code>。')
   + p('验算：2·1 + 3 = 5 ✓；1 + 3·3 = 10 ✓。'))
  + qa('例 3　求点 (2,1) 关于直线 y = x 的对称点。',
   p('反射矩阵 <code>R = [[0,1],[1,0]]</code>，<code>R(2,1)ᵀ = (1,2)ᵀ</code>。')
   + p('也可用「det = −1 表示反向」自检：反射把面积取向翻转。'))),
 practice=(ol('求 <code>|3 1; 2 4|</code> 与 <code>|1 0 2; 0 3 0; 4 0 1|</code>。',
        '求 <code>[[1,2],[3,4]]</code> 的伴随矩阵与逆矩阵。',
        'k 取何值时 <code>[[k,2],[3,6]]</code> 不可逆？',
        '验证 <code>det(AB) = det(A)det(B)</code>，其中 A = [[1,2],[3,4]]、B = [[0,1],[1,1]]。')
  + det('答案与思路',
   p('<b>1.</b> <code>3·4 − 1·2 = 10</code>；第二个沿第二行展开：<code>3·|1 2; 4 1| = 3·(1−8) = −21</code>（注意符号 (−1)^{2+2} = +1）。')
   + p('<b>2.</b> det = 4−6 = −2。代数余子式矩阵 <code>[[4,−3],[−2,1]]</code>，转置得 adj = <code>[[4,−2],[−3,1]]</code>，除 −2 得 <code>[[−2,1],[1.5,−0.5]]</code>。')
   + p('<b>3.</b> det = 6k − 6 = 0 → k = 1。此时两行成比例。')
   + p('<b>4.</b> det(A) = −2，det(B) = −1，AB = [[2,3],[4,7]]，det(AB) = 14−12 = 2 = (−2)(−1) ✓。')),
 exam=(p(badge('bad', '必考') + '3×3 行列式计算、二阶逆矩阵公式、判断可逆性、用逆阵解二元方程组。')
  + p(badge('warn', '易错 1') + '<b>伴随矩阵忘了转置</b>。adj(A) 是代数余子式矩阵的<b>转置</b>。')
  + p(badge('warn', '易错 2') + '<b>行变换后忘了记录符号变化</b>。换行变号、乘行变倍数，要用笔记下来。')
  + p(badge('warn', '易错 3') + '<b>解方程时右乘 A⁻¹</b>。必须左乘。')
  + p(badge('mute', '进阶') + '克莱姆法则（下节）本质就是 <code>x_i = det(A_i)/det(A)</code>，与逆矩阵公式同源。')),
 checklist=(h2('行列式与逆矩阵清单')
  + st('先看阶数：2×2 直接 ad−bc；3×3 优先行变换化三角',
       '行变换三种操作分别对应「变号 / 乘倍数 / 不变」',
       '化成三角后对角线连乘得 det',
       'det = 0 → 停止，直接答「不可逆」',
       '求逆：算代数余子式 → 排成矩阵 → 转置 → 除以 det',
       '最后用 <code>AA⁻¹ = I</code> 验算一两个元素')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture1.pdf', '全篇', '行列式定义与性质、余子式与代数余子式、伴随矩阵、逆矩阵、线性方程组'),
   ('（补充）', '—', '二阶速算公式与「左乘」提醒为实操性补充'))))

# ============================================================ 5
LEC.append(L(
 slug='t3-gauss-eigen',
 tzh='Topic 3 · 高斯消元、特征值与克莱姆法则',
 ten="Gaussian Elimination, Trivial and Non-trivial Solutions, Eigenvalues, Cramer's Rule",
 keywords=['augmented matrix', 'row echelon form', 'Gaussian elimination', 'trivial solution', 'eigenvalue', 'eigenvector', "Cramer's rule"],
 files=['Topic 3/EMII_Week3_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('上一节用逆矩阵解方程，但求逆代价高且只适用于方阵。本节给出更通用的工具：高斯消元能解任意规模的方程组，并从消元结果直接读出「有唯一解 / 无穷多解 / 无解」。随后引入特征值——让 <code>Ax</code> 与 <code>x</code> 平行的那些特殊方向。')
  + p('学完本节你应当能够：')
  + ck('写出增广矩阵并用初等行变换化成行阶梓形',
     '由秩判定方程组解的情况',
     '区分平凡解与非平凡解',
     '求 2×2、3×3 矩阵的特征值与特征向量',
     '用克莱姆法则写出解的公式')),
 detail=(h3('5.1 增广矩阵与初等行变换')
  + p('把 <code>Ax = b</code> 的系数与常数项并排写成<b>增广矩阵</b>（augmented matrix）<code>[A | b]</code>。允许的三种初等行变换：')
  + ol('交换两行', '某行乘以非零常数', '某行加上另一行的倍数')
  + p('这三种变换不改变方程组的解集，而能把矩阵化为<b>行阶梓形</b>（row echelon form，REF）：每行首个非零元（主元 pivot）逐行右移，主元下方全为 0。')
  + h3('5.2 高斯消元与解的情况')
  + p('步骤：自上而下消元 → 得到上三角 → 自下而上回代（back substitution）。')
  + p('解的情况由<b>秩</b>（rank，非零行数）决定：')
  + tb(('关系', '结论', '几何'),
       ('rank(A) = rank([A|b]) = n', '唯一解', '直线/平面交于一点'),
       ('rank(A) = rank([A|b]) &lt; n', '无穷多解（含 n − rank 个自由变量）', '交于一条线或一个面'),
       ('rank(A) &lt; rank([A|b])', '无解', '平行不相交'))
  + cal('warn', '关键判别', '看最后一列能不能出现主元。若消元后出现形如 <code>[0 0 … 0 | c]</code> 且 <code>c ≠ 0</code> 的行，即为 <code>0 = c</code> 矛盾，立刻无解。')
  + h3('5.3 齐次方程组与平凡解')
  + p('形如 <code>Ax = 0</code> 的方程组称<b>齐次</b>（homogeneous）。它永远有<b>平凡解</b>（trivial solution）<code>x = 0</code>。')
  + p('<b>存在非平凡解</b>（non-trivial solution）的充要条件是 <code>det(A) = 0</code>（对方阵），等价于 <code>rank(A) &lt; n</code>。这一条与下一小节的特征值方程同构，非常重要。')
  + h3('5.4 特征值与特征向量')
  + p('若存在非零向量 x 与标量 λ 使 <b><code>Ax = λx</code></b>，则 λ 为<b>特征值</b>（eigenvalue），x 为对应的<b>特征向量</b>（eigenvector）。')
  + p('把式子移项：<code>(A − λI)x = 0</code>。要求有非零解，由上节结论得 <b><code>det(A − λI) = 0</code></b>——这就是<b>特征方程</b>（characteristic equation）。')
  + p('求解顺序：解特征方程得 λ → 每个 λ 代回 <code>(A − λI)x = 0</code> → 解齐次方程组得特征向量（只到比例常数，归一化即可）。')
  + cal('tip', '快速验算', '所有特征值之和 = 主对角线之和（迹 trace）；所有特征值之积 = 行列式。这两条能在考试中立刻发现算错。')
  + h3("5.5 克莱姆法则 Cramer's rule")
  + p('若 A 为 n×n 且 det(A) ≠ 0，则 <code>Ax = b</code> 的解为')
  + p('<b><code>x_i = det(A_i) / det(A)</code></b>，其中 A_i 是把 A 的第 i 列换成 b 得到的矩阵。')
  + p('优点：直接给出公式，不用消元。缺点：需要算 n+1 个行列式，n ≥ 3 时比消元慢；且只适用于「方程数 = 未知数且 det ≠ 0」的情形。'),
 kws=K(('augmented matrix', '增广矩阵', 'The matrix [A | b].'),
       ('elementary row operation', '初等行变换', 'Swap, scale, or add a multiple of a row.'),
       ('row echelon form', '行阶梓形', 'Pivots move right as you go down.'),
       ('pivot', '主元', 'The first non-zero entry of a row.'),
       ('rank', '秩', 'The number of non-zero rows after elimination.'),
       ('trivial solution', '平凡解', 'x = 0 always solves Ax = 0.'),
       ('eigenvalue', '特征值', 'λ with det(A − λI) = 0.'),
       ('characteristic equation', '特征方程', 'det(A − λI) = 0.'),
       ("Cramer's rule", '克莱姆法则', 'x_i = det(A_i)/det(A).')),
 examples=(qa('例 1　解 x + 2y + z = 4、2x + 5y + 3z = 11、x + y = 3。',
   p('增广矩阵：<code>[1 2 1 | 4; 2 5 3 | 11; 1 1 0 | 3]</code>。')
   + p('R2 − 2R1：<code>[0 1 1 | 3]</code>；R3 − R1：<code>[0 −1 −1 | −1]</code>。')
   + p('R3 + R2：<code>[0 0 0 | 2]</code>，出现 <code>0 = 2</code>，矛盾 → <b>无解</b>。')
   + p('几何解释：三个平面没有公共交点。'))
  + qa('例 2　求 A = [[3,1],[0,2]] 的特征值与特征向量。',
   p('特征方程 <code>|3−λ, 1; 0, 2−λ| = (3−λ)(2−λ) = 0</code>，得 λ = 3 或 2。')
   + p('λ = 3：<code>(A−3I)x = [[0,1],[0,−1]]x = 0</code> 得 <code>y = 0</code>，取 x = (1,0)。')
   + p('λ = 2：<code>[[1,1],[0,0]]x = 0</code> 得 <code>x + y = 0</code>，取 (1,−1)。')
   + p('验算：迹 = 5 = 3+2 ✓；行列式 = 6 = 3·2 ✓。'))
  + qa('例 3　用克莱姆法则解 2x + y = 5、x + 3y = 10。',
   p('<code>det(A) = 5</code>。<code>det(A₁) = |5 1; 10 3| = 15−10 = 5</code>，故 <code>x = 1</code>。')
   + p('<code>det(A₂) = |2 5; 1 10| = 20−5 = 15</code>，故 <code>y = 3</code>。'))),
 practice=(ol('判断 <code>x+y=2</code>、<code>2x+2y=4</code> 的解的情况。',
        '求 <code>[[2,0],[0,3]]</code> 的特征值。',
        '求 <code>[[1,2],[2,1]]</code> 的特征值与特征向量。',
        '用消元法解 <code>x + y + z = 6</code>、<code>2x − y = 0</code>、<code>y + 2z = 8</code>。')
  + det('答案与思路',
   p('<b>1.</b> 第二式是第一式两倍，rank = 1 &lt; 2，<b>无穷多解</b>：<code>y = 2 − x</code>，x 自由。')
   + p('<b>2.</b> 对角阵的特征值就是对角元：2 与 3，特征向量 e₁、e₂。')
   + p('<b>3.</b> <code>(1−λ)² − 4 = 0</code> 得 <code>λ² − 2λ − 3 = 0</code>，λ = 3 或 −1。λ=3 得 (−1,1)… 具体：<code>(A−3I) = [[−2,2],[2,−2]]</code>，得 <code>x = y</code>，取 (1,1)；λ=−1 得 <code>x = −y</code>，取 (1,−1)。')
   + p('<b>4.</b> 由第二式 <code>x = y/2</code>。代入第一式：<code>3y/2 + z = 6</code>。与第三式联立：<code>y + 2z = 8</code>。解得 <code>y = 2, z = 3, x = 1</code>。验算全部成立。')),
 exam=(p(badge('bad', '必考') + '消元判解的情况、特征值特征向量的完整流程、克莱姆法则公式。')
  + p(badge('warn', '易错 1') + '<b>把「无穷多解」写成「无解」</b>。看到全零行且常数也为 0，是无穷多解，不是无解。')
  + p(badge('warn', '易错 2') + '<b>特征向量忘了求全部</b>。求出 λ 后必须回代解齐次方程，只写 λ 不完整。')
  + p(badge('warn', '易错 3') + '<b>克莱姆法则用在 det = 0 的矩阵上</b>。此时法则失效，须改用消元。')
  + p(badge('mute', '进阶') + '特征值在工程上对应「主方向与主伸缩」：振动模态、主成分分析、稳定性判定都靠它。')),
 checklist=(h2('解方程组与特征值清单')
  + st('写成增广矩阵，标出目标：上三角 or 行阶梓形',
       '选主元：优先选绝对值大且便于消元的行',
       '逐列向下消元，记录每步行变换',
       '消完看最后几行：全零行为自由变量行；<code>[0…0|c]</code> 为无解',
       '回代求各变量',
       '特征值题：先写 det(A−λI)=0 展开，再用迹与行列式验算')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture2.pdf', '全篇', '高斯消元、行阶梓形、平凡/非平凡解、特征值与特征向量、克莱姆法则'),
   ('（补充）', '—', '秩与解的情况对应表、迹与行列式验算法为补充'))))

# ============================================================ 4
LEC.append(L(
 slug='t3-determinant-inverse',
 tzh='Topic 3 · 行列式、伴随矩阵与逆矩阵',
 ten='Determinant, Adjugate and Inverse of Square Matrix, System of Linear Equations',
 keywords=['determinant', 'cofactor', 'adjugate', 'inverse matrix', 'singular matrix', 'system of linear equations'],
 files=['Topic 3/EMII_Week3_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('上一节说矩阵「能乘」，这一节回答「能不能除」。方阵可逆的充要条件是行列式非零，而逆矩阵又可以直接写出线性方程组的解。三件事——行列式、伴随、逆——是一条链。')
  + p('学完本节你应当能够：')
  + ck('用展开法算 2×2、3×3 及更高阶行列式',
     '求余子式、代数余子式与伴随矩阵',
     '用 <code>A⁻¹ = adj(A)/det(A)</code> 求二阶三阶逆阵',
     '用逆矩阵解 <code>Ax = b</code> 型方程组')),
 detail=(h3('4.1 行列式的定义与性质')
  + p('行列式 det(A) 或 |A| 是方阵到实数的一个函数，几何意义是「该线性变换对面积/体积的伸缩倍数」，符号表示是否保向。')
  + p('二阶：<b><code>|a b; c d| = ad − bc</code></b>。这是后面所有公式的基石。')
  + p('三阶可用对角线法则（Sarrus）：主对角三积之和，减去副对角三积之和。')
  + p('高阶用<b>余子式展开</b>（cofactor expansion），沿任意一行或一列展开结果相同：')
  + p('<b><code>det(A) = Σ_j a_ij · C_ij</code></b>，其中 <code>C_ij = (−1)^{i+j} M_ij</code>，M_ij 是删去第 i 行第 j 列后的子行列式。')
  + p('必记性质：')
  + ul('两行互换 → 行列式变号',
      '某行乘 k → 行列式乘 k',
      '两行成比例（含某行为零） → 行列式为 0',
      '某行加上另一行的倍数 → 行列式不变',
      '<code>det(AB) = det(A)det(B)</code>',
      '<code>det(Aᵀ) = det(A)</code>',
      '三角阵（上或下）的行列式 = 主对角线元素之积')
  + cal('tip', '计算策略', '永远先用行变换把矩阵化成三角阵，再把对角线相乘。直接展开 4×4 要算 24 项，用行变换只需几次加减。')
  + h3('4.2 伴随矩阵与逆矩阵')
  + p('逆矩阵 A⁻¹ 满足 <code>AA⁻¹ = A⁻¹A = I</code>。存在条件：<b>det(A) ≠ 0</b>（此时称 A 非奇异 non-singular）。')
  + p('伴随矩阵 adj(A) 是「代数余子式矩阵的转置」：<code>adj(A)_ij = C_ji</code>。注意转置这一步最容易被漏。')
  + p('<b><code>A⁻¹ = adj(A) / det(A)</code></b>')
  + p('二阶有速算式：若 <code>A = [[a,b],[c,d]]</code>，则 <code>A⁻¹ = (1/(ad−bc))·[[d,−b],[−c,a]]</code>——主对角互换、副对角变号、除以行列式。')
  + p('性质：<code>(A⁻¹)⁻¹ = A</code>、<code>(AB)⁻¹ = B⁻¹A⁻¹</code>、<code>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</code>、<code>det(A⁻¹) = 1/det(A)</code>。')
  + h3('4.3 用逆矩阵解方程组')
  + p('把 <code>a₁₁x + a₁₂y = b₁</code>、<code>a₂₁x + a₂₂y = b₂</code> 写成 <code>Ax = b</code>。若 det(A) ≠ 0，两边左乘 A⁻¹：')
  + p('<b><code>x = A⁻¹ b</code></b>')
  + p('注意左乘而非右乘——矩阵乘法不交换。这也解释了为何 A 必须可逆：det(A) = 0 时变换把平面压成一条线，信息丢失，无法反推。'),
 kws=K(('determinant', '行列式', 'det(A) measures the scaling factor of the transformation.'),
       ('minor', '余子式', 'M_ij is the determinant after deleting row i and column j.'),
       ('cofactor', '代数余子式', 'C_ij = (−1)^{i+j} M_ij.'),
       ('adjugate matrix', '伴随矩阵', 'The transpose of the cofactor matrix.'),
       ('inverse matrix', '逆矩阵', 'A⁻¹ exists iff det(A) ≠ 0.'),
       ('singular', '奇异的', 'A square matrix with det(A) = 0.'),
       ('non-singular', '非奇异的', 'A square matrix with det(A) ≠ 0.'),
       ('cofactor expansion', '余子式展开', 'Expand along any row or column.')),
 examples=(qa('例 1　求 A = [[1,2,3],[0,1,4],[5,6,0]] 的行列式。',
   p('沿第一列展开：<code>det = 1·|1 4; 6 0| − 0·|2 3; 6 0| + 5·|2 3; 1 4|</code>。')
   + p('<code>= 1·(0−24) − 0 + 5·(8−3) = −24 + 25 = 1</code>。')
   + p('行列式非零，故 A 可逆。'))
  + qa('例 2　求 A = [[2,1],[1,3]] 的逆矩阵，并用它解 2x+y=5、x+3y=10。',
   p('<code>det = 2·3 − 1·1 = 5</code>。二阶速算：主对角互换、副对角变号 → <code>[[3,−1],[−1,2]]</code>，除 5 得 <code>A⁻¹ = (1/5)[[3,−1],[−1,2]]</code>。')
   + p('<code>x = A⁻¹b = (1/5)(3·5 − 1·10, −1·5 + 2·10) = (1/5)(5, 15) = (1, 3)</code>。')
   + p('验算：2·1 + 3 = 5 ✓；1 + 3·3 = 10 ✓。'))
  + qa('例 3　求点 (2,1) 关于直线 y = x 的对称点。',
   p('反射矩阵 <code>R = [[0,1],[1,0]]</code>，<code>R(2,1)ᵀ = (1,2)ᵀ</code>。')
   + p('也可用「det = −1 表示反向」自检：反射把面积取向翻转。'))),
 practice=(ol('求 <code>|3 1; 2 4|</code> 与 <code>|1 0 2; 0 3 0; 4 0 1|</code>。',
        '求 <code>[[1,2],[3,4]]</code> 的伴随矩阵与逆矩阵。',
        'k 取何值时 <code>[[k,2],[3,6]]</code> 不可逆？',
        '验证 <code>det(AB) = det(A)det(B)</code>，其中 A = [[1,2],[3,4]]、B = [[0,1],[1,1]]。')
  + det('答案与思路',
   p('<b>1.</b> <code>3·4 − 1·2 = 10</code>；第二个沿第二行展开：<code>3·|1 2; 4 1| = 3·(1−8) = −21</code>（注意符号 (−1)^{2+2} = +1）。')
   + p('<b>2.</b> det = 4−6 = −2。代数余子式矩阵 <code>[[4,−3],[−2,1]]</code>，转置得 adj = <code>[[4,−2],[−3,1]]</code>，除 −2 得 <code>[[−2,1],[1.5,−0.5]]</code>。')
   + p('<b>3.</b> det = 6k − 6 = 0 → k = 1。此时两行成比例。')
   + p('<b>4.</b> det(A) = −2，det(B) = −1，AB = [[2,3],[4,7]]，det(AB) = 14−12 = 2 = (−2)(−1) ✓。')),
 exam=(p(badge('bad', '必考') + '3×3 行列式计算、二阶逆矩阵公式、判断可逆性、用逆阵解二元方程组。')
  + p(badge('warn', '易错 1') + '<b>伴随矩阵忘了转置</b>。adj(A) 是代数余子式矩阵的<b>转置</b>。')
  + p(badge('warn', '易错 2') + '<b>行变换后忘了记录符号变化</b>。换行变号、乘行变倍数，要用笔记下来。')
  + p(badge('warn', '易错 3') + '<b>解方程时右乘 A⁻¹</b>。必须左乘。')
  + p(badge('mute', '进阶') + '克莱姆法则（下节）本质就是 <code>x_i = det(A_i)/det(A)</code>，与逆矩阵公式同源。')),
 checklist=(h2('行列式与逆矩阵清单')
  + st('先看阶数：2×2 直接 ad−bc；3×3 优先行变换化三角',
       '行变换三种操作分别对应「变号 / 乘倍数 / 不变」',
       '化成三角后对角线连乘得 det',
       'det = 0 → 停止，直接答「不可逆」',
       '求逆：算代数余子式 → 排成矩阵 → 转置 → 除以 det',
       '最后用 <code>AA⁻¹ = I</code> 验算一两个元素')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture1.pdf', '全篇', '行列式定义与性质、余子式与代数余子式、伴随矩阵、逆矩阵、线性方程组'),
   ('（补充）', '—', '二阶速算公式与「左乘」提醒为实操性补充'))))

# ============================================================ 5
LEC.append(L(
 slug='t3-gauss-eigen',
 tzh='Topic 3 · 高斯消元、特征值与克莱姆法则',
 ten="Gaussian Elimination, Trivial and Non-trivial Solutions, Eigenvalues, Cramer's Rule",
 keywords=['augmented matrix', 'row echelon form', 'Gaussian elimination', 'trivial solution', 'eigenvalue', 'eigenvector', "Cramer's rule"],
 files=['Topic 3/EMII_Week3_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('上一节用逆矩阵解方程，但求逆代价高且只适用于方阵。本节给出更通用的工具：高斯消元能解任意规模的方程组，并从消元结果直接读出「有唯一解 / 无穷多解 / 无解」。随后引入特征值——让 <code>Ax</code> 与 <code>x</code> 平行的那些特殊方向。')
  + p('学完本节你应当能够：')
  + ck('写出增广矩阵并用初等行变换化成行阶梓形',
     '由秩判定方程组解的情况',
     '区分平凡解与非平凡解',
     '求 2×2、3×3 矩阵的特征值与特征向量',
     '用克莱姆法则写出解的公式')),
 detail=(h3('5.1 增广矩阵与初等行变换')
  + p('把 <code>Ax = b</code> 的系数与常数项并排写成<b>增广矩阵</b>（augmented matrix）<code>[A | b]</code>。允许的三种初等行变换：')
  + ol('交换两行', '某行乘以非零常数', '某行加上另一行的倍数')
  + p('这三种变换不改变方程组的解集，而能把矩阵化为<b>行阶梓形</b>（row echelon form，REF）：每行首个非零元（主元 pivot）逐行右移，主元下方全为 0。')
  + h3('5.2 高斯消元与解的情况')
  + p('步骤：自上而下消元 → 得到上三角 → 自下而上回代（back substitution）。')
  + p('解的情况由<b>秩</b>（rank，非零行数）决定：')
  + tb(('关系', '结论', '几何'),
       ('rank(A) = rank([A|b]) = n', '唯一解', '直线/平面交于一点'),
       ('rank(A) = rank([A|b]) &lt; n', '无穷多解（含 n − rank 个自由变量）', '交于一条线或一个面'),
       ('rank(A) &lt; rank([A|b])', '无解', '平行不相交'))
  + cal('warn', '关键判别', '看最后一列能不能出现主元。若消元后出现形如 <code>[0 0 … 0 | c]</code> 且 <code>c ≠ 0</code> 的行，即为 <code>0 = c</code> 矛盾，立刻无解。')
  + h3('5.3 齐次方程组与平凡解')
  + p('形如 <code>Ax = 0</code> 的方程组称<b>齐次</b>（homogeneous）。它永远有<b>平凡解</b>（trivial solution）<code>x = 0</code>。')
  + p('<b>存在非平凡解</b>（non-trivial solution）的充要条件是 <code>det(A) = 0</code>（对方阵），等价于 <code>rank(A) &lt; n</code>。这一条与下一小节的特征值方程同构，非常重要。')
  + h3('5.4 特征值与特征向量')
  + p('若存在非零向量 x 与标量 λ 使 <b><code>Ax = λx</code></b>，则 λ 为<b>特征值</b>（eigenvalue），x 为对应的<b>特征向量</b>（eigenvector）。')
  + p('把式子移项：<code>(A − λI)x = 0</code>。要求有非零解，由上节结论得 <b><code>det(A − λI) = 0</code></b>——这就是<b>特征方程</b>（characteristic equation）。')
  + p('求解顺序：解特征方程得 λ → 每个 λ 代回 <code>(A − λI)x = 0</code> → 解齐次方程组得特征向量（只到比例常数，归一化即可）。')
  + cal('tip', '快速验算', '所有特征值之和 = 主对角线之和（迹 trace）；所有特征值之积 = 行列式。这两条能在考试中立刻发现算错。')
  + h3("5.5 克莱姆法则 Cramer's rule")
  + p('若 A 为 n×n 且 det(A) ≠ 0，则 <code>Ax = b</code> 的解为')
  + p('<b><code>x_i = det(A_i) / det(A)</code></b>，其中 A_i 是把 A 的第 i 列换成 b 得到的矩阵。')
  + p('优点：直接给出公式，不用消元。缺点：需要算 n+1 个行列式，n ≥ 3 时比消元慢；且只适用于「方程数 = 未知数且 det ≠ 0」的情形。'),
 kws=K(('augmented matrix', '增广矩阵', 'The matrix [A | b].'),
       ('elementary row operation', '初等行变换', 'Swap, scale, or add a multiple of a row.'),
       ('row echelon form', '行阶梓形', 'Pivots move right as you go down.'),
       ('pivot', '主元', 'The first non-zero entry of a row.'),
       ('rank', '秩', 'The number of non-zero rows after elimination.'),
       ('trivial solution', '平凡解', 'x = 0 always solves Ax = 0.'),
       ('eigenvalue', '特征值', 'λ with det(A − λI) = 0.'),
       ('characteristic equation', '特征方程', 'det(A − λI) = 0.'),
       ("Cramer's rule", '克莱姆法则', 'x_i = det(A_i)/det(A).')),
 examples=(qa('例 1　解 x + 2y + z = 4、2x + 5y + 3z = 11、x + y = 3。',
   p('增广矩阵：<code>[1 2 1 | 4; 2 5 3 | 11; 1 1 0 | 3]</code>。')
   + p('R2 − 2R1：<code>[0 1 1 | 3]</code>；R3 − R1：<code>[0 −1 −1 | −1]</code>。')
   + p('R3 + R2：<code>[0 0 0 | 2]</code>，出现 <code>0 = 2</code>，矛盾 → <b>无解</b>。')
   + p('几何解释：三个平面没有公共交点。'))
  + qa('例 2　求 A = [[3,1],[0,2]] 的特征值与特征向量。',
   p('特征方程 <code>|3−λ, 1; 0, 2−λ| = (3−λ)(2−λ) = 0</code>，得 λ = 3 或 2。')
   + p('λ = 3：<code>(A−3I)x = [[0,1],[0,−1]]x = 0</code> 得 <code>y = 0</code>，取 x = (1,0)。')
   + p('λ = 2：<code>[[1,1],[0,0]]x = 0</code> 得 <code>x + y = 0</code>，取 (1,−1)。')
   + p('验算：迹 = 5 = 3+2 ✓；行列式 = 6 = 3·2 ✓。'))
  + qa('例 3　用克莱姆法则解 2x + y = 5、x + 3y = 10。',
   p('<code>det(A) = 5</code>。<code>det(A₁) = |5 1; 10 3| = 15−10 = 5</code>，故 <code>x = 1</code>。')
   + p('<code>det(A₂) = |2 5; 1 10| = 20−5 = 15</code>，故 <code>y = 3</code>。'))),
 practice=(ol('判断 <code>x+y=2</code>、<code>2x+2y=4</code> 的解的情况。',
        '求 <code>[[2,0],[0,3]]</code> 的特征值。',
        '求 <code>[[1,2],[2,1]]</code> 的特征值与特征向量。',
        '用消元法解 <code>x + y + z = 6</code>、<code>2x − y = 0</code>、<code>y + 2z = 8</code>。')
  + det('答案与思路',
   p('<b>1.</b> 第二式是第一式两倍，rank = 1 &lt; 2，<b>无穷多解</b>：<code>y = 2 − x</code>，x 自由。')
   + p('<b>2.</b> 对角阵的特征值就是对角元：2 与 3，特征向量 e₁、e₂。')
   + p('<b>3.</b> <code>(1−λ)² − 4 = 0</code> 得 <code>λ² − 2λ − 3 = 0</code>，λ = 3 或 −1。λ=3 得 (−1,1)… 具体：<code>(A−3I) = [[−2,2],[2,−2]]</code>，得 <code>x = y</code>，取 (1,1)；λ=−1 得 <code>x = −y</code>，取 (1,−1)。')
   + p('<b>4.</b> 由第二式 <code>x = y/2</code>。代入第一式：<code>3y/2 + z = 6</code>。与第三式联立：<code>y + 2z = 8</code>。解得 <code>y = 2, z = 3, x = 1</code>。验算全部成立。')),
 exam=(p(badge('bad', '必考') + '消元判解的情况、特征值特征向量的完整流程、克莱姆法则公式。')
  + p(badge('warn', '易错 1') + '<b>把「无穷多解」写成「无解」</b>。看到全零行且常数也为 0，是无穷多解，不是无解。')
  + p(badge('warn', '易错 2') + '<b>特征向量忘了求全部</b>。求出 λ 后必须回代解齐次方程，只写 λ 不完整。')
  + p(badge('warn', '易错 3') + '<b>克莱姆法则用在 det = 0 的矩阵上</b>。此时法则失效，须改用消元。')
  + p(badge('mute', '进阶') + '特征值在工程上对应「主方向与主伸缩」：振动模态、主成分分析、稳定性判定都靠它。')),
 checklist=(h2('解方程组与特征值清单')
  + st('写成增广矩阵，标出目标：上三角 or 行阶梓形',
       '选主元：优先选绝对值大且便于消元的行',
       '逐列向下消元，记录每步行变换',
       '消完看最后几行：全零行为自由变量行；<code>[0…0|c]</code> 为无解',
       '回代求各变量',
       '特征值题：先写 det(A−λI)=0 展开，再用迹与行列式验算')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture2.pdf', '全篇', '高斯消元、行阶梓形、平凡/非平凡解、特征值与特征向量、克莱姆法则'),
   ('（补充）', '—', '秩与解的情况对应表、迹与行列式验算法为补充'))))

# ============================================================ 4
LEC.append(L(
 slug='t3-determinant-inverse',
 tzh='Topic 3 · 行列式、伴随矩阵与逆矩阵',
 ten='Determinant, Adjugate and Inverse of Square Matrix, System of Linear Equations',
 keywords=['determinant', 'cofactor', 'adjugate', 'inverse matrix', 'singular matrix', 'system of linear equations'],
 files=['Topic 3/EMII_Week3_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('上一节说矩阵「能乘」，这一节回答「能不能除」。方阵可逆的充要条件是行列式非零，而逆矩阵又可以直接写出线性方程组的解。三件事——行列式、伴随、逆——是一条链。')
  + p('学完本节你应当能够：')
  + ck('用展开法算 2×2、3×3 及更高阶行列式',
     '求余子式、代数余子式与伴随矩阵',
     '用 <code>A⁻¹ = adj(A)/det(A)</code> 求二阶三阶逆阵',
     '用逆矩阵解 <code>Ax = b</code> 型方程组')),
 detail=(h3('4.1 行列式的定义与性质')
  + p('行列式 det(A) 或 |A| 是方阵到实数的一个函数，几何意义是「该线性变换对面积/体积的伸缩倍数」，符号表示是否保向。')
  + p('二阶：<b><code>|a b; c d| = ad − bc</code></b>。这是后面所有公式的基石。')
  + p('三阶可用对角线法则（Sarrus）：主对角三积之和，减去副对角三积之和。')
  + p('高阶用<b>余子式展开</b>（cofactor expansion），沿任意一行或一列展开结果相同：')
  + p('<b><code>det(A) = Σ_j a_ij · C_ij</code></b>，其中 <code>C_ij = (−1)^{i+j} M_ij</code>，M_ij 是删去第 i 行第 j 列后的子行列式。')
  + p('必记性质：')
  + ul('两行互换 → 行列式变号',
      '某行乘 k → 行列式乘 k',
      '两行成比例（含某行为零） → 行列式为 0',
      '某行加上另一行的倍数 → 行列式不变',
      '<code>det(AB) = det(A)det(B)</code>',
      '<code>det(Aᵀ) = det(A)</code>',
      '三角阵（上或下）的行列式 = 主对角线元素之积')
  + cal('tip', '计算策略', '永远先用行变换把矩阵化成三角阵，再把对角线相乘。直接展开 4×4 要算 24 项，用行变换只需几次加减。')
  + h3('4.2 伴随矩阵与逆矩阵')
  + p('逆矩阵 A⁻¹ 满足 <code>AA⁻¹ = A⁻¹A = I</code>。存在条件：<b>det(A) ≠ 0</b>（此时称 A 非奇异 non-singular）。')
  + p('伴随矩阵 adj(A) 是「代数余子式矩阵的转置」：<code>adj(A)_ij = C_ji</code>。注意转置这一步最容易被漏。')
  + p('<b><code>A⁻¹ = adj(A) / det(A)</code></b>')
  + p('二阶有速算式：若 <code>A = [[a,b],[c,d]]</code>，则 <code>A⁻¹ = (1/(ad−bc))·[[d,−b],[−c,a]]</code>——主对角互换、副对角变号、除以行列式。')
  + p('性质：<code>(A⁻¹)⁻¹ = A</code>、<code>(AB)⁻¹ = B⁻¹A⁻¹</code>、<code>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</code>、<code>det(A⁻¹) = 1/det(A)</code>。')
  + h3('4.3 用逆矩阵解方程组')
  + p('把 <code>a₁₁x + a₁₂y = b₁</code>、<code>a₂₁x + a₂₂y = b₂</code> 写成 <code>Ax = b</code>。若 det(A) ≠ 0，两边左乘 A⁻¹：')
  + p('<b><code>x = A⁻¹ b</code></b>')
  + p('注意左乘而非右乘——矩阵乘法不交换。这也解释了为何 A 必须可逆：det(A) = 0 时变换把平面压成一条线，信息丢失，无法反推。'),
 kws=K(('determinant', '行列式', 'det(A) measures the scaling factor of the transformation.'),
       ('minor', '余子式', 'M_ij is the determinant after deleting row i and column j.'),
       ('cofactor', '代数余子式', 'C_ij = (−1)^{i+j} M_ij.'),
       ('adjugate matrix', '伴随矩阵', 'The transpose of the cofactor matrix.'),
       ('inverse matrix', '逆矩阵', 'A⁻¹ exists iff det(A) ≠ 0.'),
       ('singular', '奇异的', 'A square matrix with det(A) = 0.'),
       ('non-singular', '非奇异的', 'A square matrix with det(A) ≠ 0.'),
       ('cofactor expansion', '余子式展开', 'Expand along any row or column.')),
 examples=(qa('例 1　求 A = [[1,2,3],[0,1,4],[5,6,0]] 的行列式。',
   p('沿第一列展开：<code>det = 1·|1 4; 6 0| − 0·|2 3; 6 0| + 5·|2 3; 1 4|</code>。')
   + p('<code>= 1·(0−24) − 0 + 5·(8−3) = −24 + 25 = 1</code>。')
   + p('行列式非零，故 A 可逆。'))
  + qa('例 2　求 A = [[2,1],[1,3]] 的逆矩阵，并用它解 2x+y=5、x+3y=10。',
   p('<code>det = 2·3 − 1·1 = 5</code>。二阶速算：主对角互换、副对角变号 → <code>[[3,−1],[−1,2]]</code>，除 5 得 <code>A⁻¹ = (1/5)[[3,−1],[−1,2]]</code>。')
   + p('<code>x = A⁻¹b = (1/5)(3·5 − 1·10, −1·5 + 2·10) = (1/5)(5, 15) = (1, 3)</code>。')
   + p('验算：2·1 + 3 = 5 ✓；1 + 3·3 = 10 ✓。'))
  + qa('例 3　求点 (2,1) 关于直线 y = x 的对称点。',
   p('反射矩阵 <code>R = [[0,1],[1,0]]</code>，<code>R(2,1)ᵀ = (1,2)ᵀ</code>。')
   + p('也可用「det = −1 表示反向」自检：反射把面积取向翻转。'))),
 practice=(ol('求 <code>|3 1; 2 4|</code> 与 <code>|1 0 2; 0 3 0; 4 0 1|</code>。',
        '求 <code>[[1,2],[3,4]]</code> 的伴随矩阵与逆矩阵。',
        'k 取何值时 <code>[[k,2],[3,6]]</code> 不可逆？',
        '验证 <code>det(AB) = det(A)det(B)</code>，其中 A = [[1,2],[3,4]]、B = [[0,1],[1,1]]。')
  + det('答案与思路',
   p('<b>1.</b> <code>3·4 − 1·2 = 10</code>；第二个沿第二行展开：<code>3·|1 2; 4 1| = 3·(1−8) = −21</code>（注意符号 (−1)^{2+2} = +1）。')
   + p('<b>2.</b> det = 4−6 = −2。代数余子式矩阵 <code>[[4,−3],[−2,1]]</code>，转置得 adj = <code>[[4,−2],[−3,1]]</code>，除 −2 得 <code>[[−2,1],[1.5,−0.5]]</code>。')
   + p('<b>3.</b> det = 6k − 6 = 0 → k = 1。此时两行成比例。')
   + p('<b>4.</b> det(A) = −2，det(B) = −1，AB = [[2,3],[4,7]]，det(AB) = 14−12 = 2 = (−2)(−1) ✓。')),
 exam=(p(badge('bad', '必考') + '3×3 行列式计算、二阶逆矩阵公式、判断可逆性、用逆阵解二元方程组。')
  + p(badge('warn', '易错 1') + '<b>伴随矩阵忘了转置</b>。adj(A) 是代数余子式矩阵的<b>转置</b>。')
  + p(badge('warn', '易错 2') + '<b>行变换后忘了记录符号变化</b>。换行变号、乘行变倍数，要用笔记下来。')
  + p(badge('warn', '易错 3') + '<b>解方程时右乘 A⁻¹</b>。必须左乘。')
  + p(badge('mute', '进阶') + '克莱姆法则（下节）本质就是 <code>x_i = det(A_i)/det(A)</code>，与逆矩阵公式同源。')),
 checklist=(h2('行列式与逆矩阵清单')
  + st('先看阶数：2×2 直接 ad−bc；3×3 优先行变换化三角',
       '行变换三种操作分别对应「变号 / 乘倍数 / 不变」',
       '化成三角后对角线连乘得 det',
       'det = 0 → 停止，直接答「不可逆」',
       '求逆：算代数余子式 → 排成矩阵 → 转置 → 除以 det',
       '最后用 <code>AA⁻¹ = I</code> 验算一两个元素')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture1.pdf', '全篇', '行列式定义与性质、余子式与代数余子式、伴随矩阵、逆矩阵、线性方程组'),
   ('（补充）', '—', '二阶速算公式与「左乘」提醒为实操性补充'))))

# ============================================================ 5
LEC.append(L(
 slug='t3-gauss-eigen',
 tzh='Topic 3 · 高斯消元、特征值与克莱姆法则',
 ten="Gaussian Elimination, Trivial and Non-trivial Solutions, Eigenvalues, Cramer's Rule",
 keywords=['augmented matrix', 'row echelon form', 'Gaussian elimination', 'trivial solution', 'eigenvalue', 'eigenvector', "Cramer's rule"],
 files=['Topic 3/EMII_Week3_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('上一节用逆矩阵解方程，但求逆代价高且只适用于方阵。本节给出更通用的工具：高斯消元能解任意规模的方程组，并从消元结果直接读出「有唯一解 / 无穷多解 / 无解」。随后引入特征值——让 <code>Ax</code> 与 <code>x</code> 平行的那些特殊方向。')
  + p('学完本节你应当能够：')
  + ck('写出增广矩阵并用初等行变换化成行阶梓形',
     '由秩判定方程组解的情况',
     '区分平凡解与非平凡解',
     '求 2×2、3×3 矩阵的特征值与特征向量',
     '用克莱姆法则写出解的公式')),
 detail=(h3('5.1 增广矩阵与初等行变换')
  + p('把 <code>Ax = b</code> 的系数与常数项并排写成<b>增广矩阵</b>（augmented matrix）<code>[A | b]</code>。允许的三种初等行变换：')
  + ol('交换两行', '某行乘以非零常数', '某行加上另一行的倍数')
  + p('这三种变换不改变方程组的解集，而能把矩阵化为<b>行阶梓形</b>（row echelon form，REF）：每行首个非零元（主元 pivot）逐行右移，主元下方全为 0。')
  + h3('5.2 高斯消元与解的情况')
  + p('步骤：自上而下消元 → 得到上三角 → 自下而上回代（back substitution）。')
  + p('解的情况由<b>秩</b>（rank，非零行数）决定：')
  + tb(('关系', '结论', '几何'),
       ('rank(A) = rank([A|b]) = n', '唯一解', '直线/平面交于一点'),
       ('rank(A) = rank([A|b]) &lt; n', '无穷多解（含 n − rank 个自由变量）', '交于一条线或一个面'),
       ('rank(A) &lt; rank([A|b])', '无解', '平行不相交'))
  + cal('warn', '关键判别', '看最后一列能不能出现主元。若消元后出现形如 <code>[0 0 … 0 | c]</code> 且 <code>c ≠ 0</code> 的行，即为 <code>0 = c</code> 矛盾，立刻无解。')
  + h3('5.3 齐次方程组与平凡解')
  + p('形如 <code>Ax = 0</code> 的方程组称<b>齐次</b>（homogeneous）。它永远有<b>平凡解</b>（trivial solution）<code>x = 0</code>。')
  + p('<b>存在非平凡解</b>（non-trivial solution）的充要条件是 <code>det(A) = 0</code>（对方阵），等价于 <code>rank(A) &lt; n</code>。这一条与下一小节的特征值方程同构，非常重要。')
  + h3('5.4 特征值与特征向量')
  + p('若存在非零向量 x 与标量 λ 使 <b><code>Ax = λx</code></b>，则 λ 为<b>特征值</b>（eigenvalue），x 为对应的<b>特征向量</b>（eigenvector）。')
  + p('把式子移项：<code>(A − λI)x = 0</code>。要求有非零解，由上节结论得 <b><code>det(A − λI) = 0</code></b>——这就是<b>特征方程</b>（characteristic equation）。')
  + p('求解顺序：解特征方程得 λ → 每个 λ 代回 <code>(A − λI)x = 0</code> → 解齐次方程组得特征向量（只到比例常数，归一化即可）。')
  + cal('tip', '快速验算', '所有特征值之和 = 主对角线之和（迹 trace）；所有特征值之积 = 行列式。这两条能在考试中立刻发现算错。')
  + h3("5.5 克莱姆法则 Cramer's rule")
  + p('若 A 为 n×n 且 det(A) ≠ 0，则 <code>Ax = b</code> 的解为')
  + p('<b><code>x_i = det(A_i) / det(A)</code></b>，其中 A_i 是把 A 的第 i 列换成 b 得到的矩阵。')
  + p('优点：直接给出公式，不用消元。缺点：需要算 n+1 个行列式，n ≥ 3 时比消元慢；且只适用于「方程数 = 未知数且 det ≠ 0」的情形。'),
 kws=K(('augmented matrix', '增广矩阵', 'The matrix [A | b].'),
       ('elementary row operation', '初等行变换', 'Swap, scale, or add a multiple of a row.'),
       ('row echelon form', '行阶梓形', 'Pivots move right as you go down.'),
       ('pivot', '主元', 'The first non-zero entry of a row.'),
       ('rank', '秩', 'The number of non-zero rows after elimination.'),
       ('trivial solution', '平凡解', 'x = 0 always solves Ax = 0.'),
       ('eigenvalue', '特征值', 'λ with det(A − λI) = 0.'),
       ('characteristic equation', '特征方程', 'det(A − λI) = 0.'),
       ("Cramer's rule", '克莱姆法则', 'x_i = det(A_i)/det(A).')),
 examples=(qa('例 1　解 x + 2y + z = 4、2x + 5y + 3z = 11、x + y = 3。',
   p('增广矩阵：<code>[1 2 1 | 4; 2 5 3 | 11; 1 1 0 | 3]</code>。')
   + p('R2 − 2R1：<code>[0 1 1 | 3]</code>；R3 − R1：<code>[0 −1 −1 | −1]</code>。')
   + p('R3 + R2：<code>[0 0 0 | 2]</code>，出现 <code>0 = 2</code>，矛盾 → <b>无解</b>。')
   + p('几何解释：三个平面没有公共交点。'))
  + qa('例 2　求 A = [[3,1],[0,2]] 的特征值与特征向量。',
   p('特征方程 <code>|3−λ, 1; 0, 2−λ| = (3−λ)(2−λ) = 0</code>，得 λ = 3 或 2。')
   + p('λ = 3：<code>(A−3I)x = [[0,1],[0,−1]]x = 0</code> 得 <code>y = 0</code>，取 x = (1,0)。')
   + p('λ = 2：<code>[[1,1],[0,0]]x = 0</code> 得 <code>x + y = 0</code>，取 (1,−1)。')
   + p('验算：迹 = 5 = 3+2 ✓；行列式 = 6 = 3·2 ✓。'))
  + qa('例 3　用克莱姆法则解 2x + y = 5、x + 3y = 10。',
   p('<code>det(A) = 5</code>。<code>det(A₁) = |5 1; 10 3| = 15−10 = 5</code>，故 <code>x = 1</code>。')
   + p('<code>det(A₂) = |2 5; 1 10| = 20−5 = 15</code>，故 <code>y = 3</code>。'))),
 practice=(ol('判断 <code>x+y=2</code>、<code>2x+2y=4</code> 的解的情况。',
        '求 <code>[[2,0],[0,3]]</code> 的特征值。',
        '求 <code>[[1,2],[2,1]]</code> 的特征值与特征向量。',
        '用消元法解 <code>x + y + z = 6</code>、<code>2x − y = 0</code>、<code>y + 2z = 8</code>。')
  + det('答案与思路',
   p('<b>1.</b> 第二式是第一式两倍，rank = 1 &lt; 2，<b>无穷多解</b>：<code>y = 2 − x</code>，x 自由。')
   + p('<b>2.</b> 对角阵的特征值就是对角元：2 与 3，特征向量 e₁、e₂。')
   + p('<b>3.</b> <code>(1−λ)² − 4 = 0</code> 得 <code>λ² − 2λ − 3 = 0</code>，λ = 3 或 −1。λ=3 得 (−1,1)… 具体：<code>(A−3I) = [[−2,2],[2,−2]]</code>，得 <code>x = y</code>，取 (1,1)；λ=−1 得 <code>x = −y</code>，取 (1,−1)。')
   + p('<b>4.</b> 由第二式 <code>x = y/2</code>。代入第一式：<code>3y/2 + z = 6</code>。与第三式联立：<code>y + 2z = 8</code>。解得 <code>y = 2, z = 3, x = 1</code>。验算全部成立。')),
 exam=(p(badge('bad', '必考') + '消元判解的情况、特征值特征向量的完整流程、克莱姆法则公式。')
  + p(badge('warn', '易错 1') + '<b>把「无穷多解」写成「无解」</b>。看到全零行且常数也为 0，是无穷多解，不是无解。')
  + p(badge('warn', '易错 2') + '<b>特征向量忘了求全部</b>。求出 λ 后必须回代解齐次方程，只写 λ 不完整。')
  + p(badge('warn', '易错 3') + '<b>克莱姆法则用在 det = 0 的矩阵上</b>。此时法则失效，须改用消元。')
  + p(badge('mute', '进阶') + '特征值在工程上对应「主方向与主伸缩」：振动模态、主成分分析、稳定性判定都靠它。')),
 checklist=(h2('解方程组与特征值清单')
  + st('写成增广矩阵，标出目标：上三角 or 行阶梓形',
       '选主元：优先选绝对值大且便于消元的行',
       '逐列向下消元，记录每步行变换',
       '消完看最后几行：全零行为自由变量行；<code>[0…0|c]</code> 为无解',
       '回代求各变量',
       '特征值题：先写 det(A−λI)=0 展开，再用迹与行列式验算')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture2.pdf', '全篇', '高斯消元、行阶梓形、平凡/非平凡解、特征值与特征向量、克莱姆法则'),
   ('（补充）', '—', '秩与解的情况对应表、迹与行列式验算法为补充'))))

# ============================================================ 4
LEC.append(L(
 slug='t3-determinant-inverse',
 tzh='Topic 3 · 行列式、伴随矩阵与逆矩阵',
 ten='Determinant, Adjugate and Inverse of Square Matrix, System of Linear Equations',
 keywords=['determinant', 'cofactor', 'adjugate', 'inverse matrix', 'singular matrix', 'system of linear equations'],
 files=['Topic 3/EMII_Week3_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('上一节说矩阵「能乘」，这一节回答「能不能除」。方阵可逆的充要条件是行列式非零，而逆矩阵又可以直接写出线性方程组的解。三件事——行列式、伴随、逆——是一条链。')
  + p('学完本节你应当能够：')
  + ck('用展开法算 2×2、3×3 及更高阶行列式',
     '求余子式、代数余子式与伴随矩阵',
     '用 <code>A⁻¹ = adj(A)/det(A)</code> 求二阶三阶逆阵',
     '用逆矩阵解 <code>Ax = b</code> 型方程组')),
 detail=(h3('4.1 行列式的定义与性质')
  + p('行列式 det(A) 或 |A| 是方阵到实数的一个函数，几何意义是「该线性变换对面积/体积的伸缩倍数」，符号表示是否保向。')
  + p('二阶：<b><code>|a b; c d| = ad − bc</code></b>。这是后面所有公式的基石。')
  + p('三阶可用对角线法则（Sarrus）：主对角三积之和，减去副对角三积之和。')
  + p('高阶用<b>余子式展开</b>（cofactor expansion），沿任意一行或一列展开结果相同：')
  + p('<b><code>det(A) = Σ_j a_ij · C_ij</code></b>，其中 <code>C_ij = (−1)^{i+j} M_ij</code>，M_ij 是删去第 i 行第 j 列后的子行列式。')
  + p('必记性质：')
  + ul('两行互换 → 行列式变号',
      '某行乘 k → 行列式乘 k',
      '两行成比例（含某行为零） → 行列式为 0',
      '某行加上另一行的倍数 → 行列式不变',
      '<code>det(AB) = det(A)det(B)</code>',
      '<code>det(Aᵀ) = det(A)</code>',
      '三角阵（上或下）的行列式 = 主对角线元素之积')
  + cal('tip', '计算策略', '永远先用行变换把矩阵化成三角阵，再把对角线相乘。直接展开 4×4 要算 24 项，用行变换只需几次加减。')
  + h3('4.2 伴随矩阵与逆矩阵')
  + p('逆矩阵 A⁻¹ 满足 <code>AA⁻¹ = A⁻¹A = I</code>。存在条件：<b>det(A) ≠ 0</b>（此时称 A 非奇异 non-singular）。')
  + p('伴随矩阵 adj(A) 是「代数余子式矩阵的转置」：<code>adj(A)_ij = C_ji</code>。注意转置这一步最容易被漏。')
  + p('<b><code>A⁻¹ = adj(A) / det(A)</code></b>')
  + p('二阶有速算式：若 <code>A = [[a,b],[c,d]]</code>，则 <code>A⁻¹ = (1/(ad−bc))·[[d,−b],[−c,a]]</code>——主对角互换、副对角变号、除以行列式。')
  + p('性质：<code>(A⁻¹)⁻¹ = A</code>、<code>(AB)⁻¹ = B⁻¹A⁻¹</code>、<code>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</code>、<code>det(A⁻¹) = 1/det(A)</code>。')
  + h3('4.3 用逆矩阵解方程组')
  + p('把 <code>a₁₁x + a₁₂y = b₁</code>、<code>a₂₁x + a₂₂y = b₂</code> 写成 <code>Ax = b</code>。若 det(A) ≠ 0，两边左乘 A⁻¹：')
  + p('<b><code>x = A⁻¹ b</code></b>')
  + p('注意左乘而非右乘——矩阵乘法不交换。这也解释了为何 A 必须可逆：det(A) = 0 时变换把平面压成一条线，信息丢失，无法反推。'),
 kws=K(('determinant', '行列式', 'det(A) measures the scaling factor of the transformation.'),
       ('minor', '余子式', 'M_ij is the determinant after deleting row i and column j.'),
       ('cofactor', '代数余子式', 'C_ij = (−1)^{i+j} M_ij.'),
       ('adjugate matrix', '伴随矩阵', 'The transpose of the cofactor matrix.'),
       ('inverse matrix', '逆矩阵', 'A⁻¹ exists iff det(A) ≠ 0.'),
       ('singular', '奇异的', 'A square matrix with det(A) = 0.'),
       ('non-singular', '非奇异的', 'A square matrix with det(A) ≠ 0.'),
       ('cofactor expansion', '余子式展开', 'Expand along any row or column.')),
 examples=(qa('例 1　求 A = [[1,2,3],[0,1,4],[5,6,0]] 的行列式。',
   p('沿第一列展开：<code>det = 1·|1 4; 6 0| − 0·|2 3; 6 0| + 5·|2 3; 1 4|</code>。')
   + p('<code>= 1·(0−24) − 0 + 5·(8−3) = −24 + 25 = 1</code>。')
   + p('行列式非零，故 A 可逆。'))
  + qa('例 2　求 A = [[2,1],[1,3]] 的逆矩阵，并用它解 2x+y=5、x+3y=10。',
   p('<code>det = 2·3 − 1·1 = 5</code>。二阶速算：主对角互换、副对角变号 → <code>[[3,−1],[−1,2]]</code>，除 5 得 <code>A⁻¹ = (1/5)[[3,−1],[−1,2]]</code>。')
   + p('<code>x = A⁻¹b = (1/5)(3·5 − 1·10, −1·5 + 2·10) = (1/5)(5, 15) = (1, 3)</code>。')
   + p('验算：2·1 + 3 = 5 ✓；1 + 3·3 = 10 ✓。'))
  + qa('例 3　求点 (2,1) 关于直线 y = x 的对称点。',
   p('反射矩阵 <code>R = [[0,1],[1,0]]</code>，<code>R(2,1)ᵀ = (1,2)ᵀ</code>。')
   + p('也可用「det = −1 表示反向」自检：反射把面积取向翻转。'))),
 practice=(ol('求 <code>|3 1; 2 4|</code> 与 <code>|1 0 2; 0 3 0; 4 0 1|</code>。',
        '求 <code>[[1,2],[3,4]]</code> 的伴随矩阵与逆矩阵。',
        'k 取何值时 <code>[[k,2],[3,6]]</code> 不可逆？',
        '验证 <code>det(AB) = det(A)det(B)</code>，其中 A = [[1,2],[3,4]]、B = [[0,1],[1,1]]。')
  + det('答案与思路',
   p('<b>1.</b> <code>3·4 − 1·2 = 10</code>；第二个沿第二行展开：<code>3·|1 2; 4 1| = 3·(1−8) = −21</code>（注意符号 (−1)^{2+2} = +1）。')
   + p('<b>2.</b> det = 4−6 = −2。代数余子式矩阵 <code>[[4,−3],[−2,1]]</code>，转置得 adj = <code>[[4,−2],[−3,1]]</code>，除 −2 得 <code>[[−2,1],[1.5,−0.5]]</code>。')
   + p('<b>3.</b> det = 6k − 6 = 0 → k = 1。此时两行成比例。')
   + p('<b>4.</b> det(A) = −2，det(B) = −1，AB = [[2,3],[4,7]]，det(AB) = 14−12 = 2 = (−2)(−1) ✓。')),
 exam=(p(badge('bad', '必考') + '3×3 行列式计算、二阶逆矩阵公式、判断可逆性、用逆阵解二元方程组。')
  + p(badge('warn', '易错 1') + '<b>伴随矩阵忘了转置</b>。adj(A) 是代数余子式矩阵的<b>转置</b>。')
  + p(badge('warn', '易错 2') + '<b>行变换后忘了记录符号变化</b>。换行变号、乘行变倍数，要用笔记下来。')
  + p(badge('warn', '易错 3') + '<b>解方程时右乘 A⁻¹</b>。必须左乘。')
  + p(badge('mute', '进阶') + '克莱姆法则（下节）本质就是 <code>x_i = det(A_i)/det(A)</code>，与逆矩阵公式同源。')),
 checklist=(h2('行列式与逆矩阵清单')
  + st('先看阶数：2×2 直接 ad−bc；3×3 优先行变换化三角',
       '行变换三种操作分别对应「变号 / 乘倍数 / 不变」',
       '化成三角后对角线连乘得 det',
       'det = 0 → 停止，直接答「不可逆」',
       '求逆：算代数余子式 → 排成矩阵 → 转置 → 除以 det',
       '最后用 <code>AA⁻¹ = I</code> 验算一两个元素')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture1.pdf', '全篇', '行列式定义与性质、余子式与代数余子式、伴随矩阵、逆矩阵、线性方程组'),
   ('（补充）', '—', '二阶速算公式与「左乘」提醒为实操性补充'))))

# ============================================================ 5
LEC.append(L(
 slug='t3-gauss-eigen',
 tzh='Topic 3 · 高斯消元、特征值与克莱姆法则',
 ten="Gaussian Elimination, Trivial and Non-trivial Solutions, Eigenvalues, Cramer's Rule",
 keywords=['augmented matrix', 'row echelon form', 'Gaussian elimination', 'trivial solution', 'eigenvalue', 'eigenvector', "Cramer's rule"],
 files=['Topic 3/EMII_Week3_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('上一节用逆矩阵解方程，但求逆代价高且只适用于方阵。本节给出更通用的工具：高斯消元能解任意规模的方程组，并从消元结果直接读出「有唯一解 / 无穷多解 / 无解」。随后引入特征值——让 <code>Ax</code> 与 <code>x</code> 平行的那些特殊方向。')
  + p('学完本节你应当能够：')
  + ck('写出增广矩阵并用初等行变换化成行阶梓形',
     '由秩判定方程组解的情况',
     '区分平凡解与非平凡解',
     '求 2×2、3×3 矩阵的特征值与特征向量',
     '用克莱姆法则写出解的公式')),
 detail=(h3('5.1 增广矩阵与初等行变换')
  + p('把 <code>Ax = b</code> 的系数与常数项并排写成<b>增广矩阵</b>（augmented matrix）<code>[A | b]</code>。允许的三种初等行变换：')
  + ol('交换两行', '某行乘以非零常数', '某行加上另一行的倍数')
  + p('这三种变换不改变方程组的解集，而能把矩阵化为<b>行阶梓形</b>（row echelon form，REF）：每行首个非零元（主元 pivot）逐行右移，主元下方全为 0。')
  + h3('5.2 高斯消元与解的情况')
  + p('步骤：自上而下消元 → 得到上三角 → 自下而上回代（back substitution）。')
  + p('解的情况由<b>秩</b>（rank，非零行数）决定：')
  + tb(('关系', '结论', '几何'),
       ('rank(A) = rank([A|b]) = n', '唯一解', '直线/平面交于一点'),
       ('rank(A) = rank([A|b]) &lt; n', '无穷多解（含 n − rank 个自由变量）', '交于一条线或一个面'),
       ('rank(A) &lt; rank([A|b])', '无解', '平行不相交'))
  + cal('warn', '关键判别', '看最后一列能不能出现主元。若消元后出现形如 <code>[0 0 … 0 | c]</code> 且 <code>c ≠ 0</code> 的行，即为 <code>0 = c</code> 矛盾，立刻无解。')
  + h3('5.3 齐次方程组与平凡解')
  + p('形如 <code>Ax = 0</code> 的方程组称<b>齐次</b>（homogeneous）。它永远有<b>平凡解</b>（trivial solution）<code>x = 0</code>。')
  + p('<b>存在非平凡解</b>（non-trivial solution）的充要条件是 <code>det(A) = 0</code>（对方阵），等价于 <code>rank(A) &lt; n</code>。这一条与下一小节的特征值方程同构，非常重要。')
  + h3('5.4 特征值与特征向量')
  + p('若存在非零向量 x 与标量 λ 使 <b><code>Ax = λx</code></b>，则 λ 为<b>特征值</b>（eigenvalue），x 为对应的<b>特征向量</b>（eigenvector）。')
  + p('把式子移项：<code>(A − λI)x = 0</code>。要求有非零解，由上节结论得 <b><code>det(A − λI) = 0</code></b>——这就是<b>特征方程</b>（characteristic equation）。')
  + p('求解顺序：解特征方程得 λ → 每个 λ 代回 <code>(A − λI)x = 0</code> → 解齐次方程组得特征向量（只到比例常数，归一化即可）。')
  + cal('tip', '快速验算', '所有特征值之和 = 主对角线之和（迹 trace）；所有特征值之积 = 行列式。这两条能在考试中立刻发现算错。')
  + h3("5.5 克莱姆法则 Cramer's rule")
  + p('若 A 为 n×n 且 det(A) ≠ 0，则 <code>Ax = b</code> 的解为')
  + p('<b><code>x_i = det(A_i) / det(A)</code></b>，其中 A_i 是把 A 的第 i 列换成 b 得到的矩阵。')
  + p('优点：直接给出公式，不用消元。缺点：需要算 n+1 个行列式，n ≥ 3 时比消元慢；且只适用于「方程数 = 未知数且 det ≠ 0」的情形。'),
 kws=K(('augmented matrix', '增广矩阵', 'The matrix [A | b].'),
       ('elementary row operation', '初等行变换', 'Swap, scale, or add a multiple of a row.'),
       ('row echelon form', '行阶梓形', 'Pivots move right as you go down.'),
       ('pivot', '主元', 'The first non-zero entry of a row.'),
       ('rank', '秩', 'The number of non-zero rows after elimination.'),
       ('trivial solution', '平凡解', 'x = 0 always solves Ax = 0.'),
       ('eigenvalue', '特征值', 'λ with det(A − λI) = 0.'),
       ('characteristic equation', '特征方程', 'det(A − λI) = 0.'),
       ("Cramer's rule", '克莱姆法则', 'x_i = det(A_i)/det(A).')),
 examples=(qa('例 1　解 x + 2y + z = 4、2x + 5y + 3z = 11、x + y = 3。',
   p('增广矩阵：<code>[1 2 1 | 4; 2 5 3 | 11; 1 1 0 | 3]</code>。')
   + p('R2 − 2R1：<code>[0 1 1 | 3]</code>；R3 − R1：<code>[0 −1 −1 | −1]</code>。')
   + p('R3 + R2：<code>[0 0 0 | 2]</code>，出现 <code>0 = 2</code>，矛盾 → <b>无解</b>。')
   + p('几何解释：三个平面没有公共交点。'))
  + qa('例 2　求 A = [[3,1],[0,2]] 的特征值与特征向量。',
   p('特征方程 <code>|3−λ, 1; 0, 2−λ| = (3−λ)(2−λ) = 0</code>，得 λ = 3 或 2。')
   + p('λ = 3：<code>(A−3I)x = [[0,1],[0,−1]]x = 0</code> 得 <code>y = 0</code>，取 x = (1,0)。')
   + p('λ = 2：<code>[[1,1],[0,0]]x = 0</code> 得 <code>x + y = 0</code>，取 (1,−1)。')
   + p('验算：迹 = 5 = 3+2 ✓；行列式 = 6 = 3·2 ✓。'))
  + qa('例 3　用克莱姆法则解 2x + y = 5、x + 3y = 10。',
   p('<code>det(A) = 5</code>。<code>det(A₁) = |5 1; 10 3| = 15−10 = 5</code>，故 <code>x = 1</code>。')
   + p('<code>det(A₂) = |2 5; 1 10| = 20−5 = 15</code>，故 <code>y = 3</code>。'))),
 practice=(ol('判断 <code>x+y=2</code>、<code>2x+2y=4</code> 的解的情况。',
        '求 <code>[[2,0],[0,3]]</code> 的特征值。',
        '求 <code>[[1,2],[2,1]]</code> 的特征值与特征向量。',
        '用消元法解 <code>x + y + z = 6</code>、<code>2x − y = 0</code>、<code>y + 2z = 8</code>。')
  + det('答案与思路',
   p('<b>1.</b> 第二式是第一式两倍，rank = 1 &lt; 2，<b>无穷多解</b>：<code>y = 2 − x</code>，x 自由。')
   + p('<b>2.</b> 对角阵的特征值就是对角元：2 与 3，特征向量 e₁、e₂。')
   + p('<b>3.</b> <code>(1−λ)² − 4 = 0</code> 得 <code>λ² − 2λ − 3 = 0</code>，λ = 3 或 −1。λ=3 得 (−1,1)… 具体：<code>(A−3I) = [[−2,2],[2,−2]]</code>，得 <code>x = y</code>，取 (1,1)；λ=−1 得 <code>x = −y</code>，取 (1,−1)。')
   + p('<b>4.</b> 由第二式 <code>x = y/2</code>。代入第一式：<code>3y/2 + z = 6</code>。与第三式联立：<code>y + 2z = 8</code>。解得 <code>y = 2, z = 3, x = 1</code>。验算全部成立。')),
 exam=(p(badge('bad', '必考') + '消元判解的情况、特征值特征向量的完整流程、克莱姆法则公式。')
  + p(badge('warn', '易错 1') + '<b>把「无穷多解」写成「无解」</b>。看到全零行且常数也为 0，是无穷多解，不是无解。')
  + p(badge('warn', '易错 2') + '<b>特征向量忘了求全部</b>。求出 λ 后必须回代解齐次方程，只写 λ 不完整。')
  + p(badge('warn', '易错 3') + '<b>克莱姆法则用在 det = 0 的矩阵上</b>。此时法则失效，须改用消元。')
  + p(badge('mute', '进阶') + '特征值在工程上对应「主方向与主伸缩」：振动模态、主成分分析、稳定性判定都靠它。')),
 checklist=(h2('解方程组与特征值清单')
  + st('写成增广矩阵，标出目标：上三角 or 行阶梓形',
       '选主元：优先选绝对值大且便于消元的行',
       '逐列向下消元，记录每步行变换',
       '消完看最后几行：全零行为自由变量行；<code>[0…0|c]</code> 为无解',
       '回代求各变量',
       '特征值题：先写 det(A−λI)=0 展开，再用迹与行列式验算')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture2.pdf', '全篇', '高斯消元、行阶梓形、平凡/非平凡解、特征值与特征向量、克莱姆法则'),
   ('（补充）', '—', '秩与解的情况对应表、迹与行列式验算法为补充'))))

# ============================================================ 4
LEC.append(L(
 slug='t3-determinant-inverse',
 tzh='Topic 3 · 行列式、伴随矩阵与逆矩阵',
 ten='Determinant, Adjugate and Inverse of Square Matrix, System of Linear Equations',
 keywords=['determinant', 'cofactor', 'adjugate', 'inverse matrix', 'singular matrix', 'system of linear equations'],
 files=['Topic 3/EMII_Week3_Lecture1.pdf'],
 overview=(h2('本节定位')
  + p('上一节说矩阵「能乘」，这一节回答「能不能除」。方阵可逆的充要条件是行列式非零，而逆矩阵又可以直接写出线性方程组的解。三件事——行列式、伴随、逆——是一条链。')
  + p('学完本节你应当能够：')
  + ck('用展开法算 2×2、3×3 及更高阶行列式',
     '求余子式、代数余子式与伴随矩阵',
     '用 <code>A⁻¹ = adj(A)/det(A)</code> 求二阶三阶逆阵',
     '用逆矩阵解 <code>Ax = b</code> 型方程组')),
 detail=(h3('4.1 行列式的定义与性质')
  + p('行列式 det(A) 或 |A| 是方阵到实数的一个函数，几何意义是「该线性变换对面积/体积的伸缩倍数」，符号表示是否保向。')
  + p('二阶：<b><code>|a b; c d| = ad − bc</code></b>。这是后面所有公式的基石。')
  + p('三阶可用对角线法则（Sarrus）：主对角三积之和，减去副对角三积之和。')
  + p('高阶用<b>余子式展开</b>（cofactor expansion），沿任意一行或一列展开结果相同：')
  + p('<b><code>det(A) = Σ_j a_ij · C_ij</code></b>，其中 <code>C_ij = (−1)^{i+j} M_ij</code>，M_ij 是删去第 i 行第 j 列后的子行列式。')
  + p('必记性质：')
  + ul('两行互换 → 行列式变号',
      '某行乘 k → 行列式乘 k',
      '两行成比例（含某行为零） → 行列式为 0',
      '某行加上另一行的倍数 → 行列式不变',
      '<code>det(AB) = det(A)det(B)</code>',
      '<code>det(Aᵀ) = det(A)</code>',
      '三角阵（上或下）的行列式 = 主对角线元素之积')
  + cal('tip', '计算策略', '永远先用行变换把矩阵化成三角阵，再把对角线相乘。直接展开 4×4 要算 24 项，用行变换只需几次加减。')
  + h3('4.2 伴随矩阵与逆矩阵')
  + p('逆矩阵 A⁻¹ 满足 <code>AA⁻¹ = A⁻¹A = I</code>。存在条件：<b>det(A) ≠ 0</b>（此时称 A 非奇异 non-singular）。')
  + p('伴随矩阵 adj(A) 是「代数余子式矩阵的转置」：<code>adj(A)_ij = C_ji</code>。注意转置这一步最容易被漏。')
  + p('<b><code>A⁻¹ = adj(A) / det(A)</code></b>')
  + p('二阶有速算式：若 <code>A = [[a,b],[c,d]]</code>，则 <code>A⁻¹ = (1/(ad−bc))·[[d,−b],[−c,a]]</code>——主对角互换、副对角变号、除以行列式。')
  + p('性质：<code>(A⁻¹)⁻¹ = A</code>、<code>(AB)⁻¹ = B⁻¹A⁻¹</code>、<code>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</code>、<code>det(A⁻¹) = 1/det(A)</code>。')
  + h3('4.3 用逆矩阵解方程组')
  + p('把 <code>a₁₁x + a₁₂y = b₁</code>、<code>a₂₁x + a₂₂y = b₂</code> 写成 <code>Ax = b</code>。若 det(A) ≠ 0，两边左乘 A⁻¹：')
  + p('<b><code>x = A⁻¹ b</code></b>')
  + p('注意左乘而非右乘——矩阵乘法不交换。这也解释了为何 A 必须可逆：det(A) = 0 时变换把平面压成一条线，信息丢失，无法反推。'),
 kws=K(('determinant', '行列式', 'det(A) measures the scaling factor of the transformation.'),
       ('minor', '余子式', 'M_ij is the determinant after deleting row i and column j.'),
       ('cofactor', '代数余子式', 'C_ij = (−1)^{i+j} M_ij.'),
       ('adjugate matrix', '伴随矩阵', 'The transpose of the cofactor matrix.'),
       ('inverse matrix', '逆矩阵', 'A⁻¹ exists iff det(A) ≠ 0.'),
       ('singular', '奇异的', 'A square matrix with det(A) = 0.'),
       ('non-singular', '非奇异的', 'A square matrix with det(A) ≠ 0.'),
       ('cofactor expansion', '余子式展开', 'Expand along any row or column.')),
 examples=(qa('例 1　求 A = [[1,2,3],[0,1,4],[5,6,0]] 的行列式。',
   p('沿第一列展开：<code>det = 1·|1 4; 6 0| − 0·|2 3; 6 0| + 5·|2 3; 1 4|</code>。')
   + p('<code>= 1·(0−24) − 0 + 5·(8−3) = −24 + 25 = 1</code>。')
   + p('行列式非零，故 A 可逆。'))
  + qa('例 2　求 A = [[2,1],[1,3]] 的逆矩阵，并用它解 2x+y=5、x+3y=10。',
   p('<code>det = 2·3 − 1·1 = 5</code>。二阶速算：主对角互换、副对角变号 → <code>[[3,−1],[−1,2]]</code>，除 5 得 <code>A⁻¹ = (1/5)[[3,−1],[−1,2]]</code>。')
   + p('<code>x = A⁻¹b = (1/5)(3·5 − 1·10, −1·5 + 2·10) = (1/5)(5, 15) = (1, 3)</code>。')
   + p('验算：2·1 + 3 = 5 ✓；1 + 3·3 = 10 ✓。'))
  + qa('例 3　求点 (2,1) 关于直线 y = x 的对称点。',
   p('反射矩阵 <code>R = [[0,1],[1,0]]</code>，<code>R(2,1)ᵀ = (1,2)ᵀ</code>。')
   + p('也可用「det = −1 表示反向」自检：反射把面积取向翻转。'))),
 practice=(ol('求 <code>|3 1; 2 4|</code> 与 <code>|1 0 2; 0 3 0; 4 0 1|</code>。',
        '求 <code>[[1,2],[3,4]]</code> 的伴随矩阵与逆矩阵。',
        'k 取何值时 <code>[[k,2],[3,6]]</code> 不可逆？',
        '验证 <code>det(AB) = det(A)det(B)</code>，其中 A = [[1,2],[3,4]]、B = [[0,1],[1,1]]。')
  + det('答案与思路',
   p('<b>1.</b> <code>3·4 − 1·2 = 10</code>；第二个沿第二行展开：<code>3·|1 2; 4 1| = 3·(1−8) = −21</code>（注意符号 (−1)^{2+2} = +1）。')
   + p('<b>2.</b> det = 4−6 = −2。代数余子式矩阵 <code>[[4,−3],[−2,1]]</code>，转置得 adj = <code>[[4,−2],[−3,1]]</code>，除 −2 得 <code>[[−2,1],[1.5,−0.5]]</code>。')
   + p('<b>3.</b> det = 6k − 6 = 0 → k = 1。此时两行成比例。')
   + p('<b>4.</b> det(A) = −2，det(B) = −1，AB = [[2,3],[4,7]]，det(AB) = 14−12 = 2 = (−2)(−1) ✓。')),
 exam=(p(badge('bad', '必考') + '3×3 行列式计算、二阶逆矩阵公式、判断可逆性、用逆阵解二元方程组。')
  + p(badge('warn', '易错 1') + '<b>伴随矩阵忘了转置</b>。adj(A) 是代数余子式矩阵的<b>转置</b>。')
  + p(badge('warn', '易错 2') + '<b>行变换后忘了记录符号变化</b>。换行变号、乘行变倍数，要用笔记下来。')
  + p(badge('warn', '易错 3') + '<b>解方程时右乘 A⁻¹</b>。必须左乘。')
  + p(badge('mute', '进阶') + '克莱姆法则（下节）本质就是 <code>x_i = det(A_i)/det(A)</code>，与逆矩阵公式同源。')),
 checklist=(h2('行列式与逆矩阵清单')
  + st('先看阶数：2×2 直接 ad−bc；3×3 优先行变换化三角',
       '行变换三种操作分别对应「变号 / 乘倍数 / 不变」',
       '化成三角后对角线连乘得 det',
       'det = 0 → 停止，直接答「不可逆」',
       '求逆：算代数余子式 → 排成矩阵 → 转置 → 除以 det',
       '最后用 <code>AA⁻¹ = I</code> 验算一两个元素')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture1.pdf', '全篇', '行列式定义与性质、余子式与代数余子式、伴随矩阵、逆矩阵、线性方程组'),
   ('（补充）', '—', '二阶速算公式与「左乘」提醒为实操性补充'))))

# ============================================================ 5
LEC.append(L(
 slug='t3-gauss-eigen',
 tzh='Topic 3 · 高斯消元、特征值与克莱姆法则',
 ten="Gaussian Elimination, Trivial and Non-trivial Solutions, Eigenvalues, Cramer's Rule",
 keywords=['augmented matrix', 'row echelon form', 'Gaussian elimination', 'trivial solution', 'eigenvalue', 'eigenvector', "Cramer's rule"],
 files=['Topic 3/EMII_Week3_Lecture2.pdf'],
 overview=(h2('本节定位')
  + p('上一节用逆矩阵解方程，但求逆代价高且只适用于方阵。本节给出更通用的工具：高斯消元能解任意规模的方程组，并从消元结果直接读出「有唯一解 / 无穷多解 / 无解」。随后引入特征值——让 <code>Ax</code> 与 <code>x</code> 平行的那些特殊方向。')
  + p('学完本节你应当能够：')
  + ck('写出增广矩阵并用初等行变换化成行阶梓形',
     '由秩判定方程组解的情况',
     '区分平凡解与非平凡解',
     '求 2×2、3×3 矩阵的特征值与特征向量',
     '用克莱姆法则写出解的公式')),
 detail=(h3('5.1 增广矩阵与初等行变换')
  + p('把 <code>Ax = b</code> 的系数与常数项并排写成<b>增广矩阵</b>（augmented matrix）<code>[A | b]</code>。允许的三种初等行变换：')
  + ol('交换两行', '某行乘以非零常数', '某行加上另一行的倍数')
  + p('这三种变换不改变方程组的解集，而能把矩阵化为<b>行阶梓形</b>（row echelon form，REF）：每行首个非零元（主元 pivot）逐行右移，主元下方全为 0。')
  + h3('5.2 高斯消元与解的情况')
  + p('步骤：自上而下消元 → 得到上三角 → 自下而上回代（back substitution）。')
  + p('解的情况由<b>秩</b>（rank，非零行数）决定：')
  + tb(('关系', '结论', '几何'),
       ('rank(A) = rank([A|b]) = n', '唯一解', '直线/平面交于一点'),
       ('rank(A) = rank([A|b]) &lt; n', '无穷多解（含 n − rank 个自由变量）', '交于一条线或一个面'),
       ('rank(A) &lt; rank([A|b])', '无解', '平行不相交'))
  + cal('warn', '关键判别', '看最后一列能不能出现主元。若消元后出现形如 <code>[0 0 … 0 | c]</code> 且 <code>c ≠ 0</code> 的行，即为 <code>0 = c</code> 矛盾，立刻无解。')
  + h3('5.3 齐次方程组与平凡解')
  + p('形如 <code>Ax = 0</code> 的方程组称<b>齐次</b>（homogeneous）。它永远有<b>平凡解</b>（trivial solution）<code>x = 0</code>。')
  + p('<b>存在非平凡解</b>（non-trivial solution）的充要条件是 <code>det(A) = 0</code>（对方阵），等价于 <code>rank(A) &lt; n</code>。这一条与下一小节的特征值方程同构，非常重要。')
  + h3('5.4 特征值与特征向量')
  + p('若存在非零向量 x 与标量 λ 使 <b><code>Ax = λx</code></b>，则 λ 为<b>特征值</b>（eigenvalue），x 为对应的<b>特征向量</b>（eigenvector）。')
  + p('把式子移项：<code>(A − λI)x = 0</code>。要求有非零解，由上节结论得 <b><code>det(A − λI) = 0</code></b>——这就是<b>特征方程</b>（characteristic equation）。')
  + p('求解顺序：解特征方程得 λ → 每个 λ 代回 <code>(A − λI)x = 0</code> → 解齐次方程组得特征向量（只到比例常数，归一化即可）。')
  + cal('tip', '快速验算', '所有特征值之和 = 主对角线之和（迹 trace）；所有特征值之积 = 行列式。这两条能在考试中立刻发现算错。')
  + h3("5.5 克莱姆法则 Cramer's rule")
  + p('若 A 为 n×n 且 det(A) ≠ 0，则 <code>Ax = b</code> 的解为')
  + p('<b><code>x_i = det(A_i) / det(A)</code></b>，其中 A_i 是把 A 的第 i 列换成 b 得到的矩阵。')
  + p('优点：直接给出公式，不用消元。缺点：需要算 n+1 个行列式，n ≥ 3 时比消元慢；且只适用于「方程数 = 未知数且 det ≠ 0」的情形。'),
 kws=K(('augmented matrix', '增广矩阵', 'The matrix [A | b].'),
       ('elementary row operation', '初等行变换', 'Swap, scale, or add a multiple of a row.'),
       ('row echelon form', '行阶梓形', 'Pivots move right as you go down.'),
       ('pivot', '主元', 'The first non-zero entry of a row.'),
       ('rank', '秩', 'The number of non-zero rows after elimination.'),
       ('trivial solution', '平凡解', 'x = 0 always solves Ax = 0.'),
       ('eigenvalue', '特征值', 'λ with det(A − λI) = 0.'),
       ('characteristic equation', '特征方程', 'det(A − λI) = 0.'),
       ("Cramer's rule", '克莱姆法则', 'x_i = det(A_i)/det(A).')),
 examples=(qa('例 1　解 x + 2y + z = 4、2x + 5y + 3z = 11、x + y = 3。',
   p('增广矩阵：<code>[1 2 1 | 4; 2 5 3 | 11; 1 1 0 | 3]</code>。')
   + p('R2 − 2R1：<code>[0 1 1 | 3]</code>；R3 − R1：<code>[0 −1 −1 | −1]</code>。')
   + p('R3 + R2：<code>[0 0 0 | 2]</code>，出现 <code>0 = 2</code>，矛盾 → <b>无解</b>。')
   + p('几何解释：三个平面没有公共交点。'))
  + qa('例 2　求 A = [[3,1],[0,2]] 的特征值与特征向量。',
   p('特征方程 <code>|3−λ, 1; 0, 2−λ| = (3−λ)(2−λ) = 0</code>，得 λ = 3 或 2。')
   + p('λ = 3：<code>(A−3I)x = [[0,1],[0,−1]]x = 0</code> 得 <code>y = 0</code>，取 x = (1,0)。')
   + p('λ = 2：<code>[[1,1],[0,0]]x = 0</code> 得 <code>x + y = 0</code>，取 (1,−1)。')
   + p('验算：迹 = 5 = 3+2 ✓；行列式 = 6 = 3·2 ✓。'))
  + qa('例 3　用克莱姆法则解 2x + y = 5、x + 3y = 10。',
   p('<code>det(A) = 5</code>。<code>det(A₁) = |5 1; 10 3| = 15−10 = 5</code>，故 <code>x = 1</code>。')
   + p('<code>det(A₂) = |2 5; 1 10| = 20−5 = 15</code>，故 <code>y = 3</code>。'))),
 practice=(ol('判断 <code>x+y=2</code>、<code>2x+2y=4</code> 的解的情况。',
        '求 <code>[[2,0],[0,3]]</code> 的特征值。',
        '求 <code>[[1,2],[2,1]]</code> 的特征值与特征向量。',
        '用消元法解 <code>x + y + z = 6</code>、<code>2x − y = 0</code>、<code>y + 2z = 8</code>。')
  + det('答案与思路',
   p('<b>1.</b> 第二式是第一式两倍，rank = 1 &lt; 2，<b>无穷多解</b>：<code>y = 2 − x</code>，x 自由。')
   + p('<b>2.</b> 对角阵的特征值就是对角元：2 与 3，特征向量 e₁、e₂。')
   + p('<b>3.</b> <code>(1−λ)² − 4 = 0</code> 得 <code>λ² − 2λ − 3 = 0</code>，λ = 3 或 −1。λ=3 得 (−1,1)… 具体：<code>(A−3I) = [[−2,2],[2,−2]]</code>，得 <code>x = y</code>，取 (1,1)；λ=−1 得 <code>x = −y</code>，取 (1,−1)。')
   + p('<b>4.</b> 由第二式 <code>x = y/2</code>。代入第一式：<code>3y/2 + z = 6</code>。与第三式联立：<code>y + 2z = 8</code>。解得 <code>y = 2, z = 3, x = 1</code>。验算全部成立。')),
 exam=(p(badge('bad', '必考') + '消元判解的情况、特征值特征向量的完整流程、克莱姆法则公式。')
  + p(badge('warn', '易错 1') + '<b>把「无穷多解」写成「无解」</b>。看到全零行且常数也为 0，是无穷多解，不是无解。')
  + p(badge('warn', '易错 2') + '<b>特征向量忘了求全部</b>。求出 λ 后必须回代解齐次方程，只写 λ 不完整。')
  + p(badge('warn', '易错 3') + '<b>克莱姆法则用在 det = 0 的矩阵上</b>。此时法则失效，须改用消元。')
  + p(badge('mute', '进阶') + '特征值在工程上对应「主方向与主伸缩」：振动模态、主成分分析、稳定性判定都靠它。')),
 checklist=(h2('解方程组与特征值清单')
  + st('写成增广矩阵，标出目标：上三角 or 行阶梓形',
       '选主元：优先选绝对值大且便于消元的行',
       '逐列向下消元，记录每步行变换',
       '消完看最后几行：全零行为自由变量行；<code>[0…0|c]</code> 为无解',
       '回代求各变量',
       '特征值题：先写 det(A−λI)=0 展开，再用迹与行列式验算')),
 mapping=tb(('源文件', '位置', '覆盖内容'),
   ('Topic 3/EMII_Week3_Lecture2.pdf', '全篇', '高斯消元、行阶梓形、平凡/非平凡解、特征值与特征向量、克莱姆法则'),
   ('（补充）', '—', '秩与解的情况对应表、迹与行列式验算法为补充'))))

print('lectures:', len(LEC))
