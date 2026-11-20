# 讲义编写任务书（BRIEF）

你的任务：为**一门课**产出全套逐节讲义，写成一个 JSON，交给已有的生成器渲染成网页。

工作目录：`C:\Users\qwe\lut-moodle-review`（下称 REPO）。站点在 `REPO\study-site`。

---

## 0. 先读这三份

1. `REPO\study-site\SPEC.md` —— JSON 契约与可用 HTML 片段（必读）。
2. `REPO\study-site\genlib.py` —— 渲染库，提供 `L()` / `emit()` / `ul()` / `ol()` / `ck()` / `tbl()` / `qa()` / `det()` / `callout()` / `kw()` / `code()`。
3. `REPO\study-site\text\<课程ID>\*.txt` —— 已抽取的源文本（PDF/PPTX/DOCX/HTML 全部转成纯文本，带 `[pN]` 页码标记）。

参考范例（HDD4010 已完成）：`REPO\study-site\gen_62.py`。照它的写法即可。

---

## 1. 产出物（只允许写这两个文件）

1. `REPO\study-site\gen_<课程ID>.py` —— 你的生成脚本。
2. `REPO\study-site\content\<课程ID>.json` —— 运行脚本后产出。

**严禁**修改 `build.py`、`assets/style.css`、`SPEC.md`、`genlib.py`，以及任何别的 `content\*.json` 或 `text\` 下的文件。

运行方式（在 REPO 根目录）：

```powershell
python study-site\gen_<课程ID>.py
```

---

## 2. 讲义粒度

**一节讲义 = 一个源文件（或一组同主题源文件）**。

- 源目录里 `Week 3\1_SE - Lecture 2 - 2026.pdf` 这种，就是独立一节。
- 同一周有多份（Lecture + Exercise Session + 案例），合并成一节，在 mapping 里列清各份的来源。
- 习题集/解答单独成节（“习题课”），讲通用解法而不是逐题抄答案。
- 跳过 `_info\` 开头的文件（那是 Moodle 页面快照）、跳过纯图片、跳过与教学无关的行政页面。
- 宁少勿滥：某目录只有一句“课程须知”就并为 1 节“课程说明与考核”，不要硬凑。

---

## 3. 每节必须有的 8 个 section

顺序固定，缺一不可（否则 `build.py --check` 会报错）。

| data-type | 写什么 |
|---|---|
| `overview` | 本节在整门课里的位置；学完能做什么（用“能够……”的动词句，3–6 条 `<ul class="checklist">`）；前置/后续衔接 |
| `detail` | **主体，篇幅最大**。源文件里每个知识点逐条展开：定义 → 性质 → 公式/语法 → 典型用法 → 常见误解。
| `keywords` | 英文术语表，`kw()` 生成三列表“English / 中文 / 说明或例句” |
| `examples` | **2–4 道例题，每题给完整解题过程**（不只有答案）。用 `qa()` 包题干与解答 |
| `practice` | **3–6 道练习**，答案与思路放 `det()` 折叠里 |
| `exam` | 分三层：`<span class="badge bad">必考</span>`、`<span class="badge warn">易错</span>`、`<span class="badge mute">进阶</span>` |
| `checklist` | **方法清单**：流程性内容用 `ol(...,"steps")` 或 `ck(...)` 列出 |
| `mapping` | 与源文件的对应表：`tbl(["源文件","位置","覆盖内容"], ...)`，注明哪些是补充拓展 |

---

## 4. 质量硬要求（用户明确点名）

1. **不遗漏知识点和技巧**：定义、公式、语法、例子、提示、注意事项全要覆盖。宁可 detail 写长。
2. **可适当拓展，但不脱离原文**：可补背景、推导、常见误解、前后衔接；**不得引入原文没有的新考点**。拓展在 mapping 里标注“补充”。
3. **补英语关键词与英文表述**：每个知识点给英文说法；能用完整英文句子就用句子。
4. **配例题和练习题，并给通用解题思路**：思路写成可迁移步骤。
5. **明确考点与难点**：`exam` 三层齐全。
6. **方法用清单列出**。

---

## 5. 格式与转义纪律

- 只写 HTML **片段**，不要 `<html>`/`<body>`/`<script>`。标题只用 `<h2>` `<h3>`。
- **禁用 MathJax / KaTeX / 任何 CDN**。数学只用 Unicode：`∈ ⊆ ∪ ∩ ¬ ∧ ∨ ∀ ∃ → ↔ ≤ ≥ ≠ ± √ ∑ ∫ ∞ π θ λ ∂ Δ α β γ ε`，配合 `<sup>`/`<sub>`。
- 代码放 `<pre><code>`，用 `code()` 自动转义。
- Python 脚本一律 `# -*- coding: utf-8 -*-` 开头，`sys.stdout.reconfigure(encoding='utf-8', errors='replace')`。
- 中文正文用全角标点；英文术语保留原文。

---

## 6. 自检（必须做）

```powershell
cd C:\Users\qwe\lut-moodle-review
python study-site\gen_<课程ID>.py
python -c "import json,re;d=json.load(open(r'study-site/content/<课程ID>.json',encoding='utf-8'));print(d['id'],len(d['lectures']));bad=[l['slug'] for l in d['lectures'] if len(re.findall(r'data-type=',l['html']))!=8];print('BAD',bad);print('chars',sum(len(l['html']) for l in d['lectures']))"
```

要求：讲义数符合预期、`BAD []`、每节 html ≥ 3000 字符（数学/编程课建议 ≥ 5000）。

---

## 7. 汇报格式（≤ 20 行）

- 课程 ID / 中文名 / 讲义节数 / 总字符数
- 逐节标题列表（`slug | 中文标题 | 源文件`）
- 自检命令真实输出
- 覆盖盲区（哪些源文件没进讲义、为什么）
