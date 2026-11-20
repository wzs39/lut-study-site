# -*- coding: utf-8 -*-
"""Append the locally archived Moodle set-proof handout as one focused lesson."""
import json
import sys
from pathlib import Path
from genlib import L, h2, h3, p, ul, ck, st, tb, K, qa, det, badge, cal

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent
SLUG = 'supp-set-proof-workshop'
SOURCE = '070 Guide to Set Theory Proofs.pdf'


def lesson():
    item = L(
        slug=SLUG,
        tzh='补充专题 · 集合证明工作坊：从定义到完整论证',
        ten='Set Proof Workshop: Definitions, Cases and Double Inclusion',
        keywords=['element chasing', 'arbitrary element', 'subset', 'proof by cases', 'double inclusion', 'power set', 'biconditional'],
        files=[SOURCE],
        overview=h2('本讲定位与学习目标') + p(
            '本讲依据课程资料中保存的十页 Guide to Proofs on Sets 编写，承接集合运算、命题逻辑与证明方法，重点练习如何把直观理解写成逐步可检查的正式证明。它是原课知识的深化练习，不代表新增官方考点，也不改变课程评分要求。',
            '复习时先读目标句，再决定证明结构；不要先写一串集合符号，最后才猜这串符号是否说明了结论。文氏图有助于猜测关系，正式论证则需要解释任意元素为什么满足目标条件。') + ck(
            '能够把子集、并集、交集、差集、对称差和幂集转换成元素层面的条件。',
            '能够区分“已知某性质时可推出什么”与“为证明某性质必须完成什么”。',
            '能够为并集条件建立覆盖所有情况的分类证明。',
            '能够将集合相等拆成双向包含，将当且仅当拆成两个方向。',
            '能够检查变量引入、假设作用范围、空集情况及循环论证。'),
        detail=h2('一、核心视角：集合由元素决定') + p(
            '指南第 1 页强调：集合完全由其中的元素决定。因此，证明集合关系时，常常需要引入题目中原本没有出现的元素变量 x。引入 x 不是增加一个额外条件，而是把一个整体命题展开成可以操作的元素命题。',
            'S ⊆ T 的含义是：对任意 x，只要 x ∈ S，就有 x ∈ T。写作“取任意 x ∈ S”，意味着后续推理只依赖 x 属于 S 这一事实，不能偷偷选一个特别方便的元素。例如取 S 中最小的元素，既可能没有定义，也不能代表 S 的所有元素。',
            '如果 S 是空集，则不存在反例元素，S ⊆ T 仍然成立。这里不需要另行断言 S 非空。若证明中出现“因为 S 非空，取 x”，就应检查题目是否真的给出了非空条件。') +
            h2('二、两套方向不同的规则') + tb(
                ['形式', '作为已知条件使用', '作为待证目标处理'],
                ['S ⊆ T', '已有 x ∈ S 时，推出 x ∈ T。', '取任意 x ∈ S，证明 x ∈ T。'],
                ['x ∈ S ∪ T', '得到 x ∈ S 或 x ∈ T，通常分类讨论。', '证明 x 至少属于其中一个集合。'],
                ['x ∈ S ∩ T', '同时得到 x ∈ S 与 x ∈ T。', '分别证明两个成员条件。'],
                ['x ∈ S − T', '得到 x ∈ S 且 x ∉ T。', '既要证明属于 S，也要排除属于 T。'],
                ['x ∈ S Δ T', 'x 恰好属于 S、T 中的一个。', '证明一个成员条件成立，另一个不成立。'],
                ['S = T', '成员与非成员关系可以在两集合之间替换。', '证明 S ⊆ T 以及 T ⊆ S。'],
                ['A ∈ P(B)', '按幂集定义得到 A ⊆ B。', '转而证明 A ⊆ B。']) + p(
            '这些规则不是可随意倒转的箭头。已知 x ∈ S ∪ T，不能指定 x 一定属于 S；目标为 x ∈ S ∩ T，也不能只完成属于 S 的一半。遇到卡住的证明，先检查是否把“或”读成了“且”，或把“足够的条件”误写成了“所有情况下都成立的事实”。',
            '使用子集假设不必再引入新的任意元素。例如已经有 x ∈ B 且 B ⊆ D，直接推出同一个 x ∈ D。若这时另取 y ∈ B，再证明 y ∈ D，就丢失了当前需要追踪的元素。') +
            h2('三、把证明写成“假设表＋目标树”') + st(
            '列出已知条件，例如 A ⊆ B ∪ C、B ⊆ D、C ⊆ E。',
            '读目标最外层：要证 A ⊆ D ∪ E，先取任意 x ∈ A。',
            '从已知条件向前推：得到 x ∈ B ∪ C，再得到 x ∈ B 或 x ∈ C。',
            '按这个或条件分情况；两种情况都要回到同一个目标 x ∈ D ∪ E。',
            '合并情况后，用 x 的任意性收束为集合包含关系。') + p(
            '前向推理使用已有信息；后向拆解解释目标需要什么。两者应在中间接上。例如目标是进入 D ∪ E，于是只要能进入 D 或 E；假设恰好提供 B 到 D、C 到 E 的两条路径。这里的分类由来源 B ∪ C 决定，不是凭空增加一种限制。',
            '分类不要求互斥。一个元素可能同时属于 B 和 C；只要所有可能都覆盖，且每个分支均能推出目标，证明就有效。不要为避免重叠，额外加入题目中不存在的 B ∩ C = ∅。') +
            h2('四、集合相等和逻辑等价不是同一层拆分') + p(
            '集合等式 S = T 可以拆成两个包含关系，这是 double inclusion。逻辑等价 P ↔ Q 则拆成“假设 P 证明 Q”和“假设 Q 证明 P”。两种拆分可能嵌套：一个方向里的目标仍可能是集合等式，因此还要继续拆分。',
            '例如 A ∩ B = A ↔ A ∈ P(B)，有两个逻辑方向。正向由等式推出 A ⊆ B；反向由 A ⊆ B 推出等式，后者又包括 A ∩ B ⊆ A 与 A ⊆ A ∩ B 两个子目标。所以正式证明共要完成三个包含论证，而不是写完一个方向就结束。',
            '两个方向的临时假设必须隔离。正向可使用 A ∩ B = A；反向则只能使用 A ∈ P(B) 及共同定义。不能把正向已经假设的等式带入反向证明，否则就是直接假设了目标。') +
            h2('五、幂集的类型检查') + p(
            'P(B) 的元素本身是集合，定义为 P(B) = {T | T ⊆ B}。因此 A ∈ P(B) 与 A ⊆ B 等价。元素属于与集合包含的符号不同，但幂集定义正好提供两者之间的桥梁。',
            '取 B = {1, 2} 时，P(B) = {∅, {1}, {2}, {1, 2}}。于是 {1} ∈ P(B) 为真，1 ∈ P(B) 为假。∅ ∈ P(B) 永远成立，因为空集是任何集合的子集。P(B) 中的成员数量在有限情形为 2 的 |B| 次幂；这里的计数只是连接既有幂集知识，不是本指南证明步骤的替代。',
            '写证明时在草稿边上标注对象类型：x 是元素、A 和 B 是集合、P(B) 是集合的集合。若你写出 x ⊆ B，就先检查 x 是否确实被定义成集合；若你写 A ∈ B，也不能仅凭 A ⊆ B 推出它。') +
            h2('六、如何校正看似明显的证明') + ul(
            '“画图可知”只说明直观，不解释任意元素的条件。将图中的每一步改写为成员条件。',
            '“由 A ⊆ B，可知 A ∩ B = A”可作为已证明定理使用；若题目本来要求证明此定理，就必须补上双向包含。',
            '“取 x ∈ S ∪ T，因此 x ∈ S”遗漏另一种情况。修正为分类讨论，或者显式保留或命题。',
            '“A ⊆ B，所以 A ∈ B”混淆层级。应检查目标是否其实是 A ∈ P(B)。',
            '“任取 x，再设 x 满足结论”把目标偷放进了假设。开始时只假设定义允许的来源条件。') + cal('tip', '英文证明句型',
            'Let x be an arbitrary element of A. / We proceed by cases. / Both cases imply that x belongs to D ∪ E. / We prove both inclusions. / Since x was arbitrary, the desired inclusion follows.'),
        kws=h2('英文术语与表达') + K(
            ['element chasing', '逐元素追踪', '跟踪同一个任意元素在集合之间的成员关系。'],
            ['arbitrary', '任意的', '不施加题目未给出的特殊限制。'],
            ['assumption / goal', '假设／目标', '假设供使用，目标需要证明。'],
            ['proof by cases', '分类证明', '每个分支均须完成同一目标，全部情况要覆盖。'],
            ['double inclusion', '双向包含', 'S ⊆ T and T ⊆ S imply S = T.'],
            ['power set', '幂集', 'A ∈ P(B) if and only if A ⊆ B.'],
            ['biconditional', '双条件／当且仅当', '证明正向与反向两个蕴含。'],
            ['axiom of extensionality', '外延公理', '具有相同元素的两个集合相等。'],
            ['symmetric difference', '对称差', 'Elements belonging to exactly one of two sets.']),
        examples=h2('例题：从拆解到收束') + qa(
            '例 1 · 指南中的并集与子集链', p(
            '已知 A ⊆ B ∪ C、B ⊆ D、C ⊆ E，证明 A ⊆ D ∪ E。',
            '取任意 x ∈ A。由第一个包含关系，x ∈ B ∪ C，所以 x ∈ B 或 x ∈ C。情况一：若 x ∈ B，由 B ⊆ D 得 x ∈ D，进而 x ∈ D ∪ E。情况二：若 x ∈ C，由 C ⊆ E 得 x ∈ E，进而 x ∈ D ∪ E。',
            '两种情况均得到同一个结论。因 x 任意，所以 A ⊆ D ∪ E。这里没有假设 B 与 C 不相交，也没有假设 A 非空。通用路径是：任取来源元素 → 展开并集 → 分支使用子集 → 放入目标并集。')) + qa(
            '例 2 · 指南中的等式、幂集和双条件', p(
            '证明 A ∩ B = A 当且仅当 A ∈ P(B)。',
            '正向：假设 A ∩ B = A。取任意 x ∈ A，由等式可得 x ∈ A ∩ B，因此 x ∈ B。于是 A ⊆ B，按定义得到 A ∈ P(B)。',
            '反向：假设 A ∈ P(B)，则 A ⊆ B。先证 A ∩ B ⊆ A：任取 x ∈ A ∩ B，由交集定义即有 x ∈ A。再证 A ⊆ A ∩ B：任取 y ∈ A，由 A ⊆ B 得 y ∈ B，故 y ∈ A ∩ B。双向包含说明 A ∩ B = A。',
            '两方向合在一起完成等价。注意反向中的第二个包含确实需要 A ⊆ B；一般情况下若 B = ∅、A 非空，它并不成立。')) + qa(
            '例 3 · 迁移练习：分配律的双向包含', p(
            '证明 A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)。这是运用指南规则编写的补充例题。',
            '左到右：取 x ∈ A ∩ (B ∪ C)，得到 x ∈ A，且 x ∈ B 或 x ∈ C。若 x ∈ B，则 x ∈ A ∩ B；若 x ∈ C，则 x ∈ A ∩ C。两种情况都给出 x ∈ (A ∩ B) ∪ (A ∩ C)。',
            '右到左：取 y ∈ (A ∩ B) ∪ (A ∩ C)。若 y ∈ A ∩ B，则 y ∈ A 且 y ∈ B ∪ C；若 y ∈ A ∩ C，也有同一结论。故 y ∈ A ∩ (B ∪ C)。两向成立，等式成立。')),
        practice=h2('独立练习与参考思路') + p('先独立写出证明开头、已知条件和目标，再展开答案核对。以下练习为本讲编写的迁移题，不是新增的官方作业。') +
            qa('练习 1 · 子集的传递性', p('已知 A ⊆ B 且 B ⊆ C，证明 A ⊆ C。') + det('答案与思路', p('取任意 x ∈ A。由 A ⊆ B 得 x ∈ B，再由 B ⊆ C 得 x ∈ C。因 x 任意，A ⊆ C。不能只写“包含关系具有传递性”，因为此题要求的正是解释传递性。'))) +
            qa('练习 2 · 交集的单调性', p('已知 A ⊆ B，证明 A ∩ C ⊆ B ∩ C。') + det('答案与思路', p('取任意 x ∈ A ∩ C，得到 x ∈ A 且 x ∈ C。由 A ⊆ B 得 x ∈ B，保留 x ∈ C，合并即得 x ∈ B ∩ C。最后用任意性收束。'))) +
            qa('练习 3 · 幂集判断', p('若 B = {1, 2}，判断 ∅ ∈ P(B)、{1} ∈ P(B)、1 ∈ P(B)、{{1}} ⊆ P(B)。') + det('答案与思路', p('依次为真、真、假、真。最后一个命题检查 {{1}} 的唯一元素 {1} 是否属于 P(B)，答案为是。不要把 {{1}} 与 {1} 当成同一集合。'))) +
            qa('练习 4 · 差集转换', p('证明 A − B = A 当且仅当 A ∩ B = ∅。') + det('答案与思路', p('正向：若交集有元素 x，则 x ∈ A 且 x ∈ B；由 A = A − B 又得 x ∉ B，矛盾，所以交集为空。反向：A − B ⊆ A 按定义成立；任取 x ∈ A，由交集为空得 x ∉ B，否则 x 属于交集。因此 x ∈ A − B。双向包含得等式。'))) +
            qa('练习 5 · 修复错误证明', p('错误论证：“取 x ∈ A ∪ B，则 x ∈ A，所以 A ∪ B ⊆ A。”指出缺失条件并给出反例。') + det('答案与思路', p('并集只给出或条件。取 A = ∅、B = {1}，则 A ∪ B = {1} 并非 A 的子集。若增加 B ⊆ A，则分类后两支都能得 x ∈ A，结论才成立。'))),
        exam=h2('复习重点与常见失分点') + p(
            '下面按站点既有标签组织复习，不构成教师对出题范围或分值的承诺。') +
            p(badge('bad', '必考（基础复习）') + '掌握元素法证明子集、并交差的逻辑翻译、集合相等的双向包含，以及 A ∈ P(B) 与 A ⊆ B 的转换。') +
            p(badge('warn', '易错') + '从或条件擅选一个分支；交集目标只证一半；等价命题只证一个方向；把 ∈ 写成 ⊆；将一个方向的临时假设带入另一个方向；忽略空集。') +
            p(badge('mute', '进阶') + '在同一题中嵌套使用双条件拆分、双向包含和分类证明；说明每一个局部结论依赖哪些假设，审查是否存在循环论证。'),
        checklist=h2('可迁移的证明清单') + st(
            '圈出结论最外层符号：⊆、=、↔ 或 ∈ P(B)，先确定证明骨架。',
            '把所有已知条件单列；每个方向新开一组局部假设。',
            '证明子集时引入任意来源元素；保持跟踪同一个变量。',
            '将集合运算逐层展开成且、或、非；遇到或考虑分类。',
            '从已有成员关系与子集假设推到目标需要的成员关系。',
            '逐一关闭分支、包含方向和蕴含方向，不能只完成最难的一支。',
            '核对空集、交叠情况、元素层级和符号；检查没有假设目标。',
            '最后明确写出：由任意性得到包含，由双向包含得到相等。'),
        mapping=h2('来源与补充边界') + tb(
            ['源文件', '位置', '覆盖内容'],
            [SOURCE, '第 1 页', '元素视角；集合由其元素决定。'],
            [SOURCE, '第 2—5 页', '子集证明与使用规则；并交差及对称差；分类证明；例 1。'],
            [SOURCE, '第 5—6 页', '集合相等、外延性、双向包含与幂集定义。'],
            [SOURCE, '第 6—10 页', '双条件与双向包含的嵌套；例 2 的完整论证。'],
            ['本讲补充编写', '类型检查、英文句型、例 3、练习 1—5', '只迁移已给出的集合与证明规则；不是原卷题目或官方新增考点。']) + p(
            '来源为工作区既有 Moodle 资料归档，本轮未重新下载。指南第 9 页的一处解释把交集过滤的对象写成 B，本讲按实际目标 A ⊆ A ∩ B 解说为“没有 A 中元素被过滤”；正式证明按元素定义核对。')
    )
    item['part'] = '补充专题与习题训练'
    return item


def main():
    path = ROOT / 'content' / '30565.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    existing = [x for x in data['lectures'] if x['slug'] == SLUG]
    if existing:
        print('Already present; no changes made.')
        return
    original = path.read_bytes()
    backup = path.with_name(path.name + '.before-set-proofs')
    if not backup.exists():
        backup.write_bytes(original)
    item = lesson()
    assert len(item['html']) >= 5000
    data['lectures'].append(item)
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    temporary.replace(path)
    result = json.loads(path.read_text(encoding='utf-8'))
    assert result['lectures'][:-1] == json.loads(original)['lectures']
    print(json.dumps({'course': data['id'], 'lectures': len(result['lectures']), 'added': SLUG, 'html_chars': len(item['html'])}, ensure_ascii=False))


if __name__ == '__main__':
    main()
