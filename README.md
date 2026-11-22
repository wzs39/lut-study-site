# LUT 课程讲义站

> 🌐 **在线阅读站点**：[https://wzs39.github.io/lut-study-site/](https://wzs39.github.io/lut-study-site/)
>
> 📖 本站已配置自动部署，包含 LUT（12 门）与河北工大双学位（3 门）共 15 门核心课程的体系化讲义、原理推导、代码实现与交互式复习。

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
- `c/<课程ID>/reader.html` — 单门课合订本，减少一次加载的内容
- `upload.html` — 实时资料上传中心：支持按「课程 → 章节」上传 PDF/PPTX/DOCX/图片/代码文件或撰写 Markdown 补充笔记

## 在线托管与实时更新（GitHub Pages + Supabase）

- 本仓库已配置 `.github/workflows/deploy.yml`：每次推送到 `main` 分支自动校验、构建并部署到 GitHub Pages。
- 每个课程页（`c/<课程ID>/index.html`）、章节页（`c/<课程ID>/part-N.html`）以及 `upload.html` 都内置了章节资料上传与实时展示面板。
- 云端配置与只读连接检查详见 [SETUP_REALTIME.md](SETUP_REALTIME.md)。未配置项目时仅保存到本机，配置字段默认留空。

全站右上角 `◐` 按钮切换配色。各模块统一使用「顶部模块导航 → 当前位置 → 页面目录 → 正文」的导航结构。

### 统一导航与讲义阅读界面

- 顶部始终按相同顺序显示「课程总览 / 期末考点清单 / 知识拓展 / 全站合订本 / 上传资料」，当前模块有底线和加粗标记；手机端完整换行显示。
- 所有页面共用同一种「页面目录」：桌面显示在左侧，屏宽不超过 980px 时收为可展开的吸顶按钮。编号、缩进、展开箭头、键盘操作和阅读位置高亮一致。
- 课程、章节和讲义页共享相同的课程树。面包屑完整显示「课程总览 → 课程 → 章节 → 讲义」；「本页内容」用于页内定位，「课程目录」用于打开其他页面，当前页显示文字标记。点击文字跳转，点击右侧箭头展开子目录。
- 讲义的八个板块、知识点小节，以及合订本和拓展页目录均归入统一目录；章节与讲义页共用「上一章/讲 → 返回目录 → 下一章/讲」导航。
- 首页全文搜索覆盖正文、术语、例题与折叠答案，可按课程/板块筛选；摘要高亮并链接到真实小节。查询保留在地址栏，离线直接打开也可搜索。
- 讲义页集中显示课程、讲次、章节和中英文标题；原始文件清单可展开查看。
- 宽表格在独立区域横向滚动，键盘用户可通过 Tab 聚焦后使用方向键滚动。
- 界面继续支持离线打开、浅色/深色配色及系统减少动态效果设置。

导航由 `site_navigation.py` 统一生成，交互来自 `assets/navigation.js`（构建时内联，无需 CDN）。修改源码后运行 `python build.py` 更新生成的 HTML。验证命令：

```bash
python -m unittest discover -s tests -v
python build.py --check
```

### 学习记录、阅读与错题

- 讲义有「未开始 / 学习中 / 待复习 / 已掌握」四种状态，与复习页勾选及课程进度共用记录；首页提供继续学习入口。
- 自动保存上次阅读小节；整理正文发生变化后保留学习状态，并提示重新定位。字号、行距和专注模式也可保存。
- 支持复制代码、键盘打开图片大图、Esc 关闭；练习提供逐题自评与收藏，首页可筛选错题/待重做/收藏并回到原题。练习不自动判分。
- 记录保存在 `lut-learning-v1`，兼容原 `lut-review-v1`，不清空旧记录。首页支持导出 JSON 备份与合并导入；保存失败会提示。不同浏览器不会自动同步个人记录，跨设备请导出/导入。
- 讲义来源面板显示真实登记的版本、核对日期和附件；未知项显示「未记录 / 未附原文件」。不使用生成日期代替复核日期。

### 资料来源与图片维护

真实来源可登记到 `data/source-metadata.json`，键为 `<课程ID>/<讲义slug>`：

```json
{
  "version": 1,
  "lectures": {
    "COURSE/LECTURE": {
      "source_version": "原文件标注的版本",
      "reviewed_at": "2026-11-21",
      "sources": [{"name": "original.pdf", "path": "sources/COURSE/original.pdf", "page": 3}]
    }
  }
}
```

示例键需换成实际讲义，日期填实际核对日期；`path` 必须指向仓库内存在的 `sources/` 或 `uploads/` 文件，或改用 HTTPS `url`。只有 PDF 登记页码时才生成 `#page=N`。不自动发布工作区外的原始资料。

`assets/media-manifest.json` 记录原图 SHA256、预览尺寸与大小。生成页使用优化预览及固有尺寸，并保留大图原件入口；原图不覆盖。更新图片后执行 `python tools/optimize_media.py`（需要 Pillow），再构建。

### 自动检查

```bash
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python -m unittest discover -s tests -p "test_*.py" -v
node --test tests/*.test.cjs
python build.py --check
python build.py
python tools/check_site.py
python tests/browser_smoke.py
```

CI 在部署前执行单元、链接/媒体与浏览器检查。浏览器检查覆盖 320/768/1024/1440 宽度，验证搜索、记录、阅读、错题、本地发布与模拟服务读写；模拟服务通过不表示真实云端已启用。详细契约见 [docs/LEARNING_UPGRADE.md](docs/LEARNING_UPGRADE.md)。

## 规模

15 门课 · 68 章 · 133 讲。每讲固定 8 个板块：

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
