# 学习功能升级验收记录

日期：2026-11-21。范围：用户确认的八项改进，保留既有统一导航与静态离线架构。改动已写入本地代码和生成页面；本记录不代表 GitHub 远端部署完成。

## 交付

| 改进 | 入口与行为 | 验证 |
|---|---|---|
| 全文搜索 | 首页正文搜索；课程/板块筛选；摘要高亮；跳到真实小节并高亮正文 | 索引 133 讲、3,338 个小节；恶意查询保持文本；file:// 可用 |
| 继续学习 | 首页继续学习、课程进度、四种讲义状态、上次小节、备份导入/导出 | 与旧复习勾选迁移/同步；内容变更保留学习状态并重新定位 |
| 来源信息 | 每讲可展开版本、核对日期、文件与 PDF 页码 | 缺失信息明确标记；有效文件、路径穿越、脚本 URL、未来日期有测试 |
| 自动检查 | GitHub Actions 在 Pages 发布前执行单元、构建、链接/媒体与浏览器检查 | 工作流已更新；下列命令已在本地执行；未声称远端 Actions 已运行 |
| 阅读工具 | 字号、行距、专注、复制代码、原图预览 | 设置刷新保留；Esc 退出；键盘打开大图并返回焦点 |
| 错题回顾 | 练习自评、收藏；首页课程/状态筛选、回原题、完成重做 | 原答案保留；题目自评刷新保留；不自动判分 |
| 图片与轻量阅读 | 原图保留、WebP 预览、固有尺寸、15 个课程合订本 | 477 张原图校验；374 张用更小预览；236 个页面检查 |
| 共享接入 | 上传中心设置/只读检查、本机覆盖配置、实际发布状态、同名历史 | 本地 IndexedDB 与模拟服务 GET/POST/失败路径验证；真实云端待配置 |

## 实测结果

- Python：16 项单元测试通过；Node：9 项测试通过。部署准备时增加了 CR/LF 示例的 HTML 实体等价测试，保留 DOM 文本并消除新增合订本的原始回车字符提交告警。
- `python build.py --check`：133 讲均具备八个必需板块，0 讲不完整。
- `python tools/check_site.py`：236 个页面、16,671 个本地引用、1,377 处图片引用，0 个链接/媒体错误。
- 浏览器：9 类页面 × 320 / 768 / 1024 / 1440 四种宽度，共 36 组布局检查；统一导航、展开目录及阅读设置无整页横向溢出。
- 功能回归：正文搜索/深链接/查询转义、状态与复习同步、阅读设置与专注、复制代码、大图及键盘焦点、错题、续读、内容变更定位、离线搜索通过。
- 共享验证：本机笔记、刷新保留、同名较早记录、文本转义、密钥校验、只读连接、模拟云端提交及 HTTP 403 保留草稿。模拟域名请求由测试拦截，不向真实项目上传资料。
- 完整性：56 份内容/拓展源文件 SHA256 保持不变；原图通过清单哈希校验；重复构建的 239 个 HTML/数据脚本/脚本包字节一致。
- 图片：原始总量 50,737,889 字节，预览引用总量 40,440,514 字节，减少 20.3%；这是图片预览集合的变化，不是整个仓库大小或加载耗时的测量。JPEG 转为 quality-90 WebP，图表使用无损编码；过大预览缩至 1,800 像素内，原图可打开。
- 每课合订本为 110,028–588,306 字节；全站合订本为 4,165,723 字节。全文索引按需加载，不加入首次打开首页的下载。
- Python 编译、11 个 JavaScript 文件语法检查及仓库正常行尾配置下的 `git diff --check` 通过。
- 搜索回归有效性：在临时副本中把多词 AND 改成 OR，原测试确实失败；真实源文件未修改。

## 仍需实际资料或服务配置

1. `assets/config.js` 的项目地址和公开客户端密钥仍为空，真实跨浏览器资料共享尚未启用。接入流程已完成；维护者需提供实际项目并按 `SETUP_REALTIME.md` 配置。只读检查通过不代表写入权限通过，页面也不作此承诺。
2. 目前 `data/source-metadata.json` 没有已登记条目。原文件名称来自既有内容，原始附件、版本、核对日期和精确页码需逐项登记；未登记项显示“未记录 / 未附原文件”，没有虚构日期或链接。
3. 学习状态与错题保存在当前浏览器，跨设备使用备份导出/导入；共享资料功能不会自动同步个人学习记录。

## 复现

```text
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python -m unittest discover -s tests -p "test_*.py" -v
node --test tests/*.test.cjs
python build.py --check
python build.py
python tools/check_site.py
python tests/browser_smoke.py
git diff --check
```

主要源码按责任拆分为 `learning_data.py`、`learning_views.py`、`source_info.py`、`media_assets.py` 及 `assets/` 下的搜索、存储、阅读、练习与共享脚本；`build.py` 负责装配。原先统一导航继续由 `site_navigation.py` / `assets/navigation.js` 维护。更新图片时先运行 `python tools/optimize_media.py`；原件不覆盖。

### Modern Web Guidance

- **`highlight-text-ranges`**：我使用 TreeWalker / Range 和原生 Highlight；缺少 API 时用安全的 mark 文本回退，避免重写讲义 DOM（“Use TreeWalker to collect text nodes — do not manipulate innerHTML.”）。
- **`typography`**：我将阅读字号设为 rem、行距设为无单位值，让大字设置能随文字继承缩放（“Use unitless numbers for `line-height`”）。
- **`forms`**：我为搜索、筛选、阅读和连接设置保留可见标签及状态信息，避免只靠提示文字说明用途（“do not rely on `placeholder` alone.”）。
- **`optimize-image-priority`**：我为正文图片预留尺寸并延迟加载屏外图片，保留作者显式的重要图片优先级；没有把所有图片设为低优先级（“Do not use `fetchpriority="low"` on standard below-the-fold images”）。
- **`dialog`**：我使用原生 modal、可见关闭按钮与浏览器焦点返回，并加滚动链隔离；旧浏览器只为大图的轻触关闭补回退（“DON'T add `role="dialog"`, `aria-modal`, a focus trap”）。
