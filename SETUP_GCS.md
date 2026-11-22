# 使用 Google Cloud Storage + GitHub Pages 托管全站与原始课件

## 架构说明

| 职责 | 平台 | 说明 |
|---|---|---|
| **网页前端与讲义站** | **GitHub Pages** (`wzs39/lut-study-site`) | 托管全部静态 HTML、CSS、JS、全文检索索引与原始课件目录（`data/courseware-index.js`），推送 `main` 即通过 `.github/workflows/deploy.yml` 自动构建部署 |
| **原始课件云端文件** | **Google Cloud Storage (GCS)** | 存放全部 15 门课的原始 PDF / PPTX / DOCX / 音视频 / 代码（约 758 MB），绕开 GitHub 单文件 100 MB 与 Pages 1 GB 限制，支持直链在线预览与下载 |

### 区域与费用参考

- **低延迟推荐（芬兰 `europe-north1`，离 LUT 最近）**：Standard Storage 约 `$0.02 / GB / 月`，存 1 GB 课件每月约 `$0.02`（极低成本）。
- **零月租免费额度（美国 `us-central1` / `us-west1` / `us-east1`）**：Google Cloud Always Free 提供 **5 GB Standard Storage 免费** + 每月一定额度免费出站流量。
- **如果还希望同学们在网页上直接实时上传新课件**：
  - 仅你自己维护更新：纯 GCS 桶即可，零后端、最稳；
  - 需同学免登录/登录从网页上传：可沿用 `SETUP_REALTIME.md` 的 Supabase 免费档，或改用同属 Google Cloud 的 **Firebase Storage + Firestore**（Spark 免费档）。

---

## 一键部署步骤（PowerShell）

### 1. 创建公开只读的 GCS 桶并配置 CORS

将 `YOUR_BUCKET_NAME` 换成全局唯一的桶名（例如 `lut-study-courseware-wzs39`）：

```powershell
$BUCKET = "lut-study-courseware-wzs39"
$REGION = "us-central1"   # 追求免费额度选 us-central1；追求芬兰低延迟选 europe-north1

# 创建存储桶（Uniform Bucket-Level Access）
gcloud storage buckets create "gs://$BUCKET" --location=$REGION --uniform-bucket-level-access

# 开启匿名只读（让 GitHub Pages 网页与浏览器可直接打开/下载原课件）
gcloud storage buckets add-iam-policy-binding "gs://$BUCKET" `
  --member="allUsers" `
  --role="roles/storage.objectViewer"

# 配置 CORS，允许 GitHub Pages 与本地预览做连接检查及在线预览
@'
[
  {
    "origin": ["https://wzs39.github.io", "http://127.0.0.1:*", "http://localhost:*"],
    "method": ["GET", "HEAD", "OPTIONS"],
    "responseHeader": ["Content-Type", "Content-Length", "Content-Range", "Accept-Ranges"],
    "maxAgeSeconds": 3600
  }
]
'@ | Set-Content -Encoding UTF8 cors.json

gcloud storage buckets update "gs://$BUCKET" --cors-file=cors.json
Remove-Item cors.json
```

> 提示：如果原始课件中包含不想被外部公开访问的个人作业或版权受限材料，不要开启 `allUsers`，改用受限访问或仅将允许共享的课件放入同步目录。

### 2. 整理并同步全部 15 门课原始课件到 GCS

在 `study-site` 目录运行：

```powershell
cd C:\Users\qwe\lut-moodle-review\study-site

# 1) 生成最新索引 data/courseware-index.js + 用硬链接整理干净的 <课程ID>/<相对路径> 目录（不占双倍磁盘空间）
python tools/build_courseware_index.py --stage ..\_gcs_stage --bucket $BUCKET

# 2) 增量同步到 Google Cloud Storage（以后有新课件时重复这两步即可）
gcloud storage rsync -r ..\_gcs_stage "gs://$BUCKET/courseware"
```

### 3. 在站点绑定 GCS 地址并推送到 GitHub Pages

1. 打开 `study-site/assets/config.js`，填入：
   ```js
   coursewareBaseUrl: "https://storage.googleapis.com/lut-study-courseware-wzs39/courseware",
   ```
   （也可以先在网页 `upload.html#courseware-cloud` 粘贴地址点击「抽检云端课件连接」测试无误后再写入 `config.js`。）
2. 重建并推送到 GitHub（自动触发 GitHub Actions 测试与 Pages 发布）：
   ```powershell
   python build.py
   git add .
   git commit -m "feat: connect Google Cloud Storage courseware hub"
   git push origin main
   ```
3. 在 GitHub 仓库 **Settings → Pages → Build and deployment → Source** 确认选择 **GitHub Actions**，发布后访问 `https://wzs39.github.io/lut-study-site/` 即可在：
   - 任意页面按 `Ctrl+K` →「原版课件」直查全站 845 份原始课件；
   - 首页「原版课件源头速查」按课程/类型搜索；
   - 每门课程页「本课原始课件总表」浏览；
   - 每篇讲义顶部「资料来源」一键在线打开或下载原 PDF/PPTX/代码。
