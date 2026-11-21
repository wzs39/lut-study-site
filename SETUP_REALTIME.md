# 共享资料连接与检查

站点有 15 门课、68 章、133 讲。课程页、章节页和 `upload.html` 使用同一资料库接口；发布记录保留署名、发布时间和原始文件名。同一课程/章节/形式的同名资料默认显示最近记录，可展开较早记录。这是发布历史，不是正文差异比较。

## 当前配置与本机试用

`assets/config.js` 默认没有项目地址或公开密钥，因此本机发布保存在 IndexedDB，其他浏览器看不到。该模式可试用上传、笔记、预览、下载与同名记录。个人学习进度另存在 localStorage，不上传到资料库。

资料共享需要实际的 Supabase 项目。维护者在项目中运行 [`supabase/schema.sql`](supabase/schema.sql)，确认资料表 `chapter_materials`、存储桶 `materials` 及读写策略已创建。本地代码不会自动创建项目或预置凭据。

## 先在当前浏览器检查

1. 通过本地 HTTP 服务或已部署站点打开 `upload.html`。本地可执行 `python -m http.server 8000`，然后打开 `http://localhost:8000/upload.html`。
2. 展开「共享连接设置与检查」，填写 HTTPS 项目根地址和公开 `sb_publishable_…` 密钥，或角色为 `anon` 的旧式 JWT。
3. 点击「只读检查连接」。检查只发 GET，不上传测试资料；通过只代表资料表可读，尚未验证写入权限。
4. 点击「保存本机连接并刷新」。公开配置存在当前浏览器的 `lut-public-sharing-v1`，不改变其他访问者的配置；「清除本机覆盖设置」可恢复站点配置。
5. 选择课程与章节，手动发布实际资料。只有接口返回成功才显示「云端已收录」；再从另一浏览器查看，确认真实共享。读权限通过、写权限未配置时，发布仍会报错。

页面拦截 secret / service_role 密钥；这些服务端密钥不应填入 HTML、仓库或浏览器。公开密钥校验不替代服务端权限控制，真实读写仍受项目策略约束。

## 为所有访问者启用

把项目地址和公开客户端密钥填入 `assets/config.js` 的既有字段，保留其余文件大小、扩展名与仓库设置：

```js
supabaseUrl: "https://YOUR_PROJECT.supabase.co",
supabaseAnonKey: "sb_publishable_YOUR_PUBLIC_CLIENT_KEY",
storageBucket: "materials",
tableName: "chapter_materials",
requirePasscode: false,
```

运行 README 中的检查与构建，审阅改动后再提交部署。实际部署时间与服务额度以项目和运行结果为准。站点使用轮询刷新资料列表；连接标记说明采用云端配置，不代表健康检查或写入已成功。

## 可选班级口令（沿用现有接口）

`supabase/schema.sql` 保留 `submit_material` RPC。若维护者选择口令提交：

1. 在服务端修改函数中的示例口令，并重新创建函数。
2. 删除开放的元数据直接插入策略：

```sql
drop policy if exists "Public can insert chapter materials" on public.chapter_materials;
```

3. 在 `assets/config.js` 设置 `requirePasscode: true`，重新检查发布。

口令仅保护采用 RPC 的元数据提交；这不等同于账户认证，存储桶写入策略仍需按实际使用范围配置。本次界面改动未调整服务端认证、策略或示例口令。

## 仓库资料与自动验证

入库附件放在 `uploads/<course_id>/part-<N>/`，由 `build.py` 生成 `data/uploads.json`。讲义来源 PDF/页码可按 README 登记到 `data/source-metadata.json`。不要把未准备公开的工作目录整体复制到站点。

`tests/browser_smoke.py` 检查本机发布、刷新保留、同名历史、笔记转义、公开密钥校验、只读检查与模拟云端 POST。测试拦截模拟域名，不向真实服务发资料；实际项目连通与跨浏览器共享需按上面步骤验证。
