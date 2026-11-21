# -*- coding: utf-8 -*-
"""30565 数学A · 并入 Week 11 作业解答（Exercise set 11，2026-11-21 抓取）。

来源：moodle-updates/2026-11-21/verify/30565/Week 11/Homework 11 solutions.pdf
（文本：moodle-updates/2026-11-21/text/30565/Homework 11 solutions.pdf.txt）
做法：supp-exercises 追加 set 11 逐题解答；primes-and-modular-arithmetic 补 Euclid 大数实例。
"""
import io
import json
import os
import sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SITE)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from genlib import h2, h3, p, ul, ol, ck, st, tb, cal, qa, det, badge  # noqa: E402

CONTENT = os.path.join(SITE, 'content', '30565.json')
BACKUP = CONTENT + '.before-hw11'
SRC = 'moodle-updates/2026-11-21/verify/30565/Week 11/Homework 11 solutions.pdf'
TXT = 'moodle-updates/2026-11-21/text/30565/Homework 11 solutions.pdf.txt'

with io.open(CONTENT, encoding='utf-8') as fh:
    data = json.load(fh)
if not os.path.exists(BACKUP):
    with io.open(BACKUP, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    print('[backup] 30565.json.before-hw11')


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


gcd_chain = ('561 752 = 2·260 712 + 40 328<br>'
             '260 712 = 6·40 328 + 18 744<br>'
             '40 328 = 2·18 744 + 2 840<br>'
             '18 744 = 6·2 840 + 1 704<br>'
             '2 840 = 1·1 704 + 1 136<br>'
             '1 704 = 1·1 136 + 568<br>'
             '1 136 = 2·568 + 0 → <b>gcd = 568</b>')

hw11_detail = (
    h3('7. Exercise set 11 逐题解答（16.–20.11. 习题课，2026-11-21 抓取）')
    + cal('tip', '来源', '<code>' + SRC + '</code>（提取文本 <code>' + TXT + '</code>）。解答册原版为英文，此处保留原始推导并加中文注。')
    + p('<b>Ex 1 · 质因数分解（用 √n 上限检验）：</b>'
        '143：√143≈11.96 → 只需试 2,3,5,7,11 → 143 = 11·13；'
        '561：数字和 12 → 3 | 561，561/3 = 187，1−8+7 = 0 → 11 | 187，187/11 = 17 → 561 = 3·11·17；'
        '588：末两位 88 = 4·22 → 2² | 588，588/4 = 147，1+4+7 = 12 → 3 | 147，147/3 = 49 = 7² → 588 = 2²·3·7²。')
    + p('<b>Ex 2 · 最大公约数（两条路）：</b>'
        'a) 28 = 2²·7，−35 = −5·7 → gcd 按质因子取指数较小者且<b>忽略符号</b> → gcd(28, −35) = 7。'
        'b) 120 = 2³·3·5，132 = 2²·3·11 → gcd = 2²·3 = 12。'
        'c) 260 712 = 2³·3³·17·71，561 752 = 2³·23·43·71 → 按分解得 2³·71 = 568，'
        '但手算难凑 17/43/71，改用 Euclid 更稳：')
    + '<table><tr><th>Euclid 辗转相除</th></tr><tr><td>' + gcd_chain + '</td></tr></table>'
    + p('<b>Ex 3 · 同余运算规则：</b>x ≡ 9 (mod 24) ⟹ 7x ≡ 63 ≡ 63−2·24 = 15 (mod 24) ⟹ '
        '7x + 4 ≡ <b>19 (mod 24)</b>。规则：同余式两边可同乘、同加。')
    + p('<b>Ex 4 · 阶乘和模 21（1!+2!+⋯+9001! mod 21）：</b>逐项算到 6!：'
        '1!≡1, 2!≡2, 3!≡6, 4!≡24≡3, 5!≡5·3≡15, 6!≡6·15≡90≡6 (mod 21)。'
        '<b>关键转折：</b>7! = 7·6! 含因子 7 与 3（即 21）⟹ 7! ≡ 0，其后所有 n! (n ≥ 7) 都 ≡ 0。'
        '求和 1+2+6+3+15+6 = 33 ≡ <b>12 (mod 21)</b>。')
    + p('<b>Ex 5 · 线性同余方程的三种解法：</b>'
        'a) 5x ≡ 6 (mod 7)：枚举 {0..6} 得 x ≡ <b>4 (mod 7)</b>；Euclid 回代：1 = 3·5 − 2·7 → 两边乘 6 → '
        'x₀ = 18 ≡ 4；乘法逆元：5·3 ≡ 1 → x ≡ 3·6 ≡ 18 ≡ 4。三法同答案。'
        'b) 14x ≡ 12 (mod 16)：gcd(14,16) = 2 | 12 → 两解 x ≡ 2 与 x ≡ 10 (mod 16)，合并为 <b>x ≡ 2 (mod 8)</b>；'
        '或约分 7x ≡ 6 (mod 8)，7 ≡ −1 → 7² ≡ 1，7 自乘即逆元 → x ≡ 7·6 ≡ 42 ≡ 2 (mod 8)。'
        'c) x³ − 10x ≡ 1 (mod 11)：多项式同余只能枚举 {0..10}，代入得 x ≡ <b>9 (mod 11)</b>'
        '（验算：9³ − 90 = 639 = 58·11 + 1 ✓；x = 31 同样满足 ✓）。'
        '<b>方法适用性：</b>枚举法全能；Euclid/逆元只适用于线性方程（c 项三次多项式不适用）。')
    + p('<b>Ex 6 · 数字判别与弃九验算：</b>'
        'a) 判据：9 | n ⟺ 数字和（可随时把 9 当 0）≡ 0 (mod 9)；11 | n ⟺ 交错和（首位加、次位减…）是 11 的倍数。'
        '3515215：数字和 21≡3？逐位 3+5+1+5+2+1+5 = 22 ≡ 4 ≠ 0 → 9 不整除；'
        '交错和 3−5+1−5+2−1+5 = 0 → 11 整除 ✓。1535450：数字和 23 ≡ 5 ≠ 0；交错和 1−5+3−5+4−5+0 = −7 → 9、11 都不整除。'
        'b) 三个大乘法找错：先弃九（mod 9），前两题左边 ≡ 右边验不出，第三题 0·8 ≢ 1 → <b>第 3 题错</b>；'
        '再用奇偶：第 1 题两因子都是奇数（末位 3、1）而「积」末位 2 是偶数——奇×奇≠偶 → <b>第 1 题也错</b>。'
        '<b>通用思路：</b>弃九先筛，筛不出换模 2（看末位奇偶），还可换 mod 11 交错和。')
    + cal('tip', '解答册自带提示（Hints）',
          '① Ex1 必须把 2 ≤ p ≤ √n 的<b>所有</b>质数都试完才算分解完成；'
          '② gcd 可用分解或 Euclid；'
          '③ Ex3 记住同余两边可乘可加；'
          '④ Ex4 检查哪些项含 21 = 3·7；'
          '⑤ Ex5 三法任选：枚举 / Euclid / 乘法逆元（进阶）；'
          '⑥ Ex6b 用 mod 9 比对等号两边。')
)
hw11_practice = (
    qa('练 · 奇偶性验算（Ex6b 的第二把刀）',
       p('不用计算器判断：485 845 416 843 583 × 5 414 518 454 648 546 841 的乘积末位可能是 2 吗？')
       + det('参考答案',
             p('不可能。两因子末位分别是 3 和 1，都是奇数；奇 × 奇 = 奇，而 2 是偶数。'
               '所以「积 = …2」必有错误（这正是解答册里第 1 个乘法算式的错处）。'
               '通用顺序：先弃九（快、但可能验不出），再奇偶（末位一眼定），必要时 mod 11。'))))
apply('supp-exercises',
      [('detail', hw11_detail), ('practice', hw11_practice)],
      files=['11-exercise-solutions.pdf (Homework 11 solutions.pdf)'],
      keywords=['Euclid', 'casting out nines'])

# primes-and-modular-arithmetic：补一个大数 Euclid 实例 + 阶乘置零技巧
primes_extra = (
    h3('Euclid 实战：六位数级的 gcd（Week 11 解答册）')
    + p('课堂例题的数字偏小；set 11 的 Ex2c 给出一个 6–7 位数的实战：'
        'gcd(260 712, 561 752)。按质因数分解要走 17、43、71 这类大因子，手算不现实；'
        'Euclid 辗转相除七步即达：' + gcd_chain)
    + cal('tip', '何时换用 Euclid',
          '两数都很大、且看不出公因子时，Euclid 每一步都是「大数 ÷ 余数」，'
          '余数严格递减，必然收敛——比硬凑质因子更稳。')
    + h3('阶乘模的「置零」技巧（Ex4）')
    + p('求 1! + 2! + ⋯ + 9001! 除以 21 的余数：一旦 n ≥ 7，n! 必含因子 7×6×…且其中含 3 → '
        '21 = 3·7 | n! → n! ≡ 0 (mod 21)。于是无穷和塌缩为前六项：'
        '1+2+6+3+15+6 = 33 ≡ 12 (mod 21)。'
        '<b>迁移：</b>凡 mod m 的阶乘和，先找使 m | n! 的最小 n，其后项全部置零。')
)
apply('primes-and-modular-arithmetic',
      [('detail', primes_extra)],
      files=['11-exercise-solutions.pdf (Homework 11 solutions.pdf)'],
      keywords=['Euclid algorithm', 'factorial modulo'])

with io.open(CONTENT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
print('[ok] 30565 hw11 merged')
