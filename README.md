# LUT 课程讲义站

把 `学习资料`（LUT，12 门课）与 `hebut/学习资料`（河北工大双学位，3 门课）共 15 门课的原始资料，整理成「课程 → 章节 → 讲次」三层结构的离线复习网页。

## 打开方式

双击 `index.html` 即可打开（纯静态，样式内联，无 CDN、无字体外链，断网可用）。

- `index.html` — 课程总览：每门课一张卡片，卡片内按章节列出全部讲次
- `c/<课程ID>/index.html` — 单门课页面（按章节分组）
- `c/<课程ID>/part-N.html` — 章节页（该章全部讲次）
- `c/<课程ID>/<slug>.html` — 单个讲次的完整讲义
- `review.html` — 期末总复习考点提醒清单（可勾选，进度存在浏览器 localStorage）
- `extend.html` — 知识拓展汇总页：全站「拓展框」与 mapping 补充条目按课程集中，点击回讲次
- `all.html` — 全站合订本，所有讲次连排，适合打印/通读
- `upload.html` — 实时资料上传中心：支持按「课程 → 章节」上传 PDF/PPTX/DOCX/图片/代码文件或撰写 Markdown 补充笔记

## 在线托管与实时更新（GitHub Pages + Supabase）

- 本仓库已配置 `.github/workflows/deploy.yml`：每次推送到 `main` 分支自动校验、构建并部署到 GitHub Pages。
- 每个课程页（`c/<课程ID>/index.html`）、章节页（`c/<课程ID>/part-N.html`）以及 `upload.html` 都内置了章节资料上传与实时展示面板。
- 开启全员免登录实时同步只需 2 分钟，详见 [SETUP_REALTIME.md](SETUP_REALTIME.md)。

全站右上角 `◐` 按钮切换配色（跟随系统 → 浅色 → 深色）；每讲正文上方有八个板块的快捷跳转条。

## 规模

15 门课 · 57 章 · 124 讲。每讲固定 8 个板块：

`overview`（本节定位与学习目标）→ `detail`（知识点主体）→ `keywords`（英文术语表）→ `examples`（例题与完整解法）→ `practice`（练习，答案折叠）→ `exam`（必考 / 易错 / 进阶）→ `checklist`（方法清单）→ `mapping`（与原始文件的对应）。

## 目录结构

```
study-site/
  index.html  all.html  review.html  extend.html
  assets/style.css        全站样式（构建时内联进每个页面；含浅/深色主题）
  content/<课程ID>.json   课程内容（唯一内容源）
  extensions/<课程ID>.json 知识拓展源数据（按 slug 注入 detail 末尾）
  add_extensions.py       拓展注入器（幂等，带 data-ext 标记）
  fix_symbols.py / fix_symbols2.py  一次性符号修复脚本（已跑过，保留备查）
  gen/*.py                各课生成脚本
  genlib.py               片段库
  build.py                静态生成器
  text/<课程ID>/*.txt     从 PDF/PPTX/DOCX 抽取的纯文本（供撰写与核对）
  c/<课程ID>/             生成的课程页、章节页、讲次页
```

## 后续补充新内容

1. 已有课程加一讲：在 `content/<课程ID>.json` 的 `lectures` 末尾追加一个对象，写 `slug / title_zh / title_en / keywords / source_files / part / html`，`html` 里放 8 个 `<section class="card" data-type="...">`，并写 `part` 指定所属章节（同名 part 自动归入同一章）。
2. 新增一门课：新建 `content/<新ID>.json`，写 `id / order / name_zh / name_en / source_dir / summary / lectures`。
3. 在 `study-site` 目录运行：

```bash
python build.py          # 重建全部页面
python build.py --check  # 检查每讲 8 个板块是否齐全
```

新讲会自动出现在总览、课程页、章节页、考点清单和合订本里，不必手改 HTML。

## 更新记录

### 2026-11-20 · Moodle 增量刷新

管线在 `../moodle-updates/2026-11-20/`（不进本目录，避免与站点文件混放）：

| 脚本 | 作用 |
| --- | --- |
| `moodle_refresh.py` | 复用 `agent-browser` 会话 cookie 拉课程清单，写 `inventory.json` |
| `moodle_download_incremental.py` | 对每门课 POST `downloadcenter` 表单，按 sha256 与 `学习资料` 里的档案比对，只留新增/变化文件 |
| `extract_html.py` | 把每个 `materials/**/*.html` 的 `#region-main` 抽成纯文本到 `text/<课程ID>/`，带 `SOURCE` / `PAGE` 头 |
| `collect_linked_materials.py` | 抓 32632 页面里指向 SharePoint 的外链 PDF（本轮未成功，见下） |

结果：12 门课共 58 个新增/变化文件，56 个 HTML 页面抽出文本。按课程分布 —— 30565 1、32667 2、30361 10、33295 11、34583 14、32632 18。

处置结论：

- **30352**：新增的 `Project instructions Car rental management system.html` 与 `Tutorial instructors.html` 内容已由既有
  `supp-setup-and-project` 完整覆盖（四个数据文件、计费取整、菜单四项、输入校验、`project.py` 单文件约束、
  CodeGrade 两项预检、90/80/70/60/50 换算与 12 月 4 日补交上限 3 级、查重指纹），本轮未改动。
- **32632**：新增 18 页里有 11 页是 `Meeting N homework`。这些页面按会议编号排、交付通道分散
  （return box / Padlet / Office Forms / Moodle 录音 / Zoom），正文六讲按能力组织，覆盖不到「哪天交到哪」。
  本轮新增一讲 `supp-homework-map`（第 7 讲）：十三次课作业地图、五个交付通道、Forms 建测验八步与四个坑、
  词典与翻译工具的选源规则、11 月 18 日发音测试窗口、Yle 一页幻灯片模板。
  另把 `Resources/Online dictionaries`（Sanakirja / 六部英英词典 / 三个翻译工具）与
  `Food material`、`EXERCISE Computers / Phones` 这类「只有清单和外链」的素材页在 `mapping` 里标清。
- **30361 / 32667 / 30565 / 33295 / 34583**：新增页面与已整合内容重复（练习说明、作业页、课前须知），未产生新讲。

已知缺口：32632 的六份食物词汇册（蔬菜 33 / 谷物豆类坚果 33 / 水果浆果 45 / 动物制品及替代品 33 / 厨房用具 33 / 烹饪动词 24）
与四个 Cambridge 外部测验。核查结论分两层：

- **网络层**：`requests` / `curl` 对 `lut-my.sharepoint.com` 的 TLS 握手会被重置（`curl (35)`、`ConnectionResetError 10054`，
  连站点根路径也一样），但真实浏览器能正常建连并拿到 `login.microsoftonline.com` 的登录页 —— 所以不是域名被封。
- **认证层**：这六份 PDF 在教师个人 OneDrive 的 `:b:/g/personal/...` 分享里，匿名访问被重定向到 Microsoft 登录，
  必须有 LUT 账号才能取；四个测验在 Cambridge 站点，同样要联网打开。

因此本站只收标题与主题，图片与题面不打包；该讲 `mapping` 里已按「需登录后打开原页」标注，没有把缺口写成「无内容」。

顺带修掉生成器的一个 Windows 控制台问题：`build.py` 的 `check()` 直接 `print` 讲义标题，标题里出现 `⑪` 时
在 GBK 控制台下抛 `UnicodeEncodeError` 中断。现在启动时把 stdout/stderr 切到 UTF-8（`errors="replace"`），
`python build.py --check` 不再需要 `PYTHONUTF8=1` 前缀。

## 内容说明

- 知识点、例题、政策与日期均来自原始课程文件；`mapping` 板块逐讲标注了源文件与页码。
- 原文未提供的细节（如部分评分比例、图片型课件内容）不臆造，已在 `mapping` 中标注为「无文字层」或「补充拓展」。
- 内容为课程复习整理，不替代官方评分标准与课程公告。