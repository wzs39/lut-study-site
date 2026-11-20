# 课程讲义站 · 内容规范 (SPEC)

站点由 `build.py` 静态生成。你只需要产出 `content/<课程ID>.json`，其余（HTML、目录、导航、总览）全部自动生成。

---

## 1. 顶层结构

```json
{
  "id": "30352",
  "order": 6,
  "name_zh": "CT60A0250 编程基础",
  "name_en": "Fundamentals of Programming for International Programs",
  "source_dir": "CT60A0250 编程基础",
  "summary": "一句话说明这门课教什么、用什么语言、怎么考核。",
  "lectures": [ /* 见下 */ ]
}
```

- `id`：必须与文件名一致，且是站点唯一标识（LUT 用课程数字 id，HEBUT 用 62/80/86）。
- `order`：总览页排序用的小整数，LUT 用 1–12，HEBUT 用 20/21/22。
- `slug`：每讲的英文短链，只能含 `a-z0-9-`，在课程内唯一。

---

## 2. 每讲 (lecture) 结构

```json
{
  "slug": "ch2-strings",
  "title_zh": "第 2 章 · 注释与字符串",
  "title_en": "Comments and Strings",
  "keywords": ["string", "comment", "escape character", "concatenation"],
  "source_files": ["Ch 2 - Part 2 - Strings.pdf"],
  "html": "<section class=\"card\" data-type=\"overview\"> ... </section> ..."
}
```

`keywords` 前 8 个会显示在总览页，请把最重要的放前面。
`source_files` 写原始文件名（不含路径），用于溯源核对。

---

## 3. html 字段：必须包含 8 个 section

每个 `<section>` 都必须带 `class="card"` 和 `data-type="..."`，顺序固定：

| 顺序 | data-type | 内容要求 |
|---|---|---|
| 1 | `overview` | 本节在整门课里的位置、学完能做到什么（用「能够……」的动词句），以及本节与上/下讲的衔接 |
| 2 | `detail` | **主体**。把原始课件里的每个知识点逐条展开讲透，不跳步。 |
| 3 | `keywords` | 英文术语表：`<table>` 三列「英文 | 中文 | 说明/例句」 |
| 4 | `examples` | 例题，必须给完整解题过程（不只有答案） |
| 5 | `practice` | 练习题，答案/思路放进 `<details>` 折叠 |
| 6 | `exam` | 考点与难点：哪里最容易考、哪里最容易错 |
| 7 | `checklist` | 方法清单：`<ul class="checklist">` 或 `<ol class="steps">` |
| 8 | `mapping` | 与原始文件的对应：哪几页讲了哪个知识点、哪些是补充拓展 |

### 硬性内容要求（用户明确点名）

1. **不遗漏知识点和技巧**：原始课件里的定义、公式、语法、例子、提示、注意事项全部覆盖到。
2. **可适当拓展，但不脱离原文知识点**：可以补背景、补推导、补常见误解，但不得引入原文没有的新考点。
3. **补充英语关键词与英文表述**：每个知识点都要给出对应的英文说法，能写成英文句子的就写成句子（这对芬兰/英语授课的课尤其重要）。
4. **配例题和练习题，并给出通用解题思路**：通用思路要写成可迁移的步骤（例如「先判类型 → 再套公式 → 最后验算」），不能只解出这一道题。
5. **明确考点与难点**：`exam` 节必须分层写「必考」「易错」「进阶」。
6. **方法要用清单列出来**：凡是流程性的东西（安装步骤、解题步骤、调试顺序、语法检查清单）都用 `<ul class="checklist">` 或 `<ol class="steps">`。

---

## 4. 可用的 HTML 片段（样式已内置，直接用）

### 标题（会自动进右侧目录）
```html
<h2>一、字符串是什么</h2>
<h3>1.1 下标与切片</h3>
```
只用 h2 / h3，不要用 h1（h1 是页面标题）。

### 提示框
```html
<div class="callout"><b>要点</b>正文</div>
<div class="callout tip"><b>技巧</b>正文</div>
<div class="callout warn"><b>注意</b>正文</div>
<div class="callout exam"><b>必考</b>正文</div>
<div class="callout idea"><b>拓展</b>正文</div>
```
`<b>` 必须是第一个子元素，会被渲染成小标题。

### 关键词胶囊
```html
<span class="chip">iteration</span>
```

### 术语表
```html
<table>
<tr><th>English</th><th>中文</th><th>说明 / 例句</th></tr>
<tr><td>assignment</td><td>赋值</td><td>Assigning a value to a variable.</td></tr>
</table>
```

### 例题 / 练习
```html
<div class="qa"><div class="q">例 1</div><p>题干……</p><p><b>解：</b>分步写清楚。</p></div>
<details><summary>参考答案与思路</summary><div class="ans">……</div></details>
```

### 清单
```html
<ul class="checklist"><li>第一步</li><li>第二步</li></ul>
<ol class="steps"><li>先读题</li><li>再建模</li></ol>
```

### 代码
```html
<pre><code>print(&quot;hello&quot;)</code></pre>
<code>int</code> 或 <kbd>Ctrl</kbd>+<kbd>S</kbd>
```

---

## 5. 转义与格式纪律

- JSON 字符串里：`"` 写成 `\"`，反斜杠写成 `\\`，换行用真实换行或 `\n` 均可，但**不要出现裸 tab**。
- HTML 里的 `<pre><code>` 内容：`<` 写成 `&lt;`，`>` 写成 `&gt;`，`&` 写成 `&amp;`。
- 数学符号直接写 Unicode：`∈ ⊆ ∪ ∩ ¬ ∧ ∨ ∀ ∃ → ↔ ≤ ≥ ≠ ± √ ∑ ∫ ∞ π θ λ ∂ Δ`。避免用 LaTeX。
- 分数用 `a/b` 或 `(a+b)/(c-d)`，幂用 `x^2`，下标用 `a_1`。
- 不要写 `<html>`、`<body>`、`<head>`、`<script>`；只写片段。

---

## 6. 生成与自检

```powershell
cd <仓库>/study-site
python build.py                 # 全量重建
python build.py --course 30352  # 只重建一门课
python build.py --check         # 检查每讲 8 个 section 是否齐全
```

`--check` 必须全部 OK 才算完成。缺 section 的会被列出来。
