# 使用 Cloudflare R2 + GitHub Pages 托管原始课件与学习网站（零月租 + 0 流量费）

## 架构与成本

| 组件 | 托管位置 | 免费额度 |
|---|---|---|
| **静态网站与索引** | **GitHub Pages** (`wzs39/lut-study-site`) | 永久免费 HTTPS，推 `main` 自动构建发布 |
| **原始课件库（820 份 / 656 MB）** | **Cloudflare R2** | **10 GB / 月免费存储 + 永久 $0 出站流量费**（每月 100 万次写、1000 万次读免费） |

> 隐私保护：`tools/build_courseware_index.py` 与 `tools/sync_r2.py` **默认自动排除**所有 `Submissions/` 目录以及包含个人姓名/学号的文件（已过滤 25 份个人简历、作业、反馈和演讲视频，共 101.8 MB），仅同步公开教学课件。

---

## 3 分钟上线步骤

### 第 1 步：在 Cloudflare 控制台创建 R2 桶并开启公开访问

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → 左侧进入 **R2 Object Storage**（首次开通需绑定支付方式，10 GB 以内月账单为 `$0`）。
2. 点击 **Create bucket**：
   - Bucket name：例如 `lut-study-courseware`
   - Location：选择 **Western Europe (WEUR)** 或 **Eastern Europe (EEUR)**（离芬兰 LUT 延迟低）
3. 进入刚建好的桶 → **Settings**：
   - **Public Development URL (`r2.dev`)**：点击 **Enable**，记下生成的公开地址，例如：
     `https://pub-xxxxxxxxxxxxxxxx.r2.dev`
     （如果你有自己的域名托管在 Cloudflare，也可以绑定 Custom Domain，如 `https://files.yourdomain.com`，无速率限制更稳。）
   - **CORS Policy**：点击 **Add CORS policy**，粘贴：
     ```json
     [
       {
         "AllowedOrigins": ["https://wzs39.github.io", "http://127.0.0.1:*", "http://localhost:*"],
         "AllowedMethods": ["GET", "HEAD"],
         "AllowedHeaders": ["*"],
         "ExposeHeaders": ["Content-Type", "Content-Length", "Content-Range", "Accept-Ranges"],
         "MaxAgeSeconds": 3600
       }
     ]
     ```
4. 回到 **R2 Object Storage** 首页 → 右侧 **Manage R2 API Tokens** → **Create API Token**：
   - Permissions：选择 **Object Read & Write**
   - Specify bucket(s)：仅勾选 `lut-study-courseware`（最小权限原则）
   - 创建后复制页面展示的 3 个值（关闭页面后 Secret 不会再显示）：
     - **Account ID**（在 R2 首页右侧栏或 S3 Endpoint `https://<ACCOUNT_ID>.r2.cloudflarestorage.com` 中）
     - **Access Key ID**
     - **Secret Access Key**

---

### 第 2 步：运行零依赖 Python 增量上传脚本

无需安装 `awscli` 或 `rclone`，在 PowerShell 中直接运行（凭据只在当前终端会话生效，**绝不写入仓库**）：

```powershell
cd C:\Users\qwe\lut-moodle-review\study-site

$env:R2_ACCOUNT_ID        = "你的32位AccountID"
$env:R2_ACCESS_KEY_ID     = "你的AccessKeyID"
$env:R2_SECRET_ACCESS_KEY = "你的SecretAccessKey"
$env:R2_BUCKET            = "lut-study-courseware"
$PUBLIC_URL               = "https://pub-xxxxxxxxxxxxxxxx.r2.dev/courseware"

# 1. 先演练确认清单（不写入）
python tools/sync_r2.py --dry-run

# 2. 增量并发上传（自动比对 MD5 ETag，已上传且未改动的文件会自动跳过），并自动回填 assets/config.js
python tools/sync_r2.py --write-config $PUBLIC_URL
```

---

### 第 3 步：重建并推送到 GitHub Pages

```powershell
# 刷新索引与全部 236 个静态页面
python tools/build_courseware_index.py
python build.py

# 本地验收（可选，CI 推送时也会自动跑一遍）
python tools/check_site.py

# 提交并推送到 GitHub（自动触发 .github/workflows/deploy.yml 发布到 GitHub Pages）
git add .
git commit -m "feat: upgrade UI/navigation and enable Cloudflare R2 courseware links"
git push origin main
```

打开 `https://wzs39.github.io/lut-study-site/` 后：
- 按 `Ctrl+K` →「原版课件」或首页「原版课件源头速查」，即可搜全站 820 份原始课件并一键在线预览 PDF/图片/音频或下载 PPTX/DOCX/代码；
- 以后 Moodle 有新课件时，只需把新文件放进 `学习资料/` 对应课程目录，重跑 `python tools/sync_r2.py`（只传新增/改动文件）+ `python tools/build_courseware_index.py` + `python build.py` + `git push` 即可。
