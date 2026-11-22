/* LUT Study Site — Cloud Courseware (Cloudflare R2 / GCS) & Live Upload Configuration
 *
 * 1. Original Courseware Cloud (Recommended: Cloudflare R2 — 10 GB free + $0 egress):
 *    Upload original course files via `python tools/sync_r2.py`,
 *    then set `coursewareBaseUrl` to your public R2 (or GCS/custom domain) prefix, e.g.:
 *      "https://pub-xxxxxxxxxxxxxxxx.r2.dev/courseware"
 *    See SETUP_R2.md (or SETUP_GCS.md) for exact commands.
 *
 * 2. Real-time browser uploads (optional, Supabase):
 *    Leave supabaseUrl empty to run in Local Preview Mode (IndexedDB) + GitHub Issue fallback.
 *    See SETUP_REALTIME.md for setup details.
 */
window.STUDY_SITE_CONFIG = {
  coursewareBaseUrl: "https://pub-38a7790f275347929341e0a0a8d5f151.r2.dev/courseware",
  supabaseUrl: "",
  supabaseAnonKey: "",
  storageBucket: "materials",
  tableName: "chapter_materials",
  requirePasscode: false,
  githubRepo: "wzs39/lut-study-site",
  maxFileSizeMB: 25,
  allowedExtensions: [
    ".pdf", ".pptx", ".ppt", ".docx", ".doc",
    ".md", ".txt", ".png", ".jpg", ".jpeg", ".webp",
    ".zip", ".py", ".ipynb", ".xlsx", ".csv"
  ]
};
