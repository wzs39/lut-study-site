/* LUT Study Site — Live Upload & Sync Configuration
 *
 * To enable real-time shared uploads for EVERYONE (no GitHub account needed):
 * 1. Create a free Supabase project at https://supabase.com
 * 2. Run supabase/schema.sql in the Supabase SQL Editor
 * 3. Paste your Project URL and Publishable/Anon Key below, then commit & push.
 *
 * Leave supabaseUrl empty to run in Local Preview Mode (IndexedDB) + GitHub Issue fallback.
 */
window.STUDY_SITE_CONFIG = {
  supabaseUrl: "",
  supabaseAnonKey: "",
  storageBucket: "materials",
  tableName: "chapter_materials",
  requirePasscode: false,
  githubRepo: "overthinknow/lut-study-site",
  maxFileSizeMB: 25,
  allowedExtensions: [
    ".pdf", ".pptx", ".ppt", ".docx", ".doc",
    ".md", ".txt", ".png", ".jpg", ".jpeg", ".webp",
    ".zip", ".py", ".ipynb", ".xlsx", ".csv"
  ]
};
