# Real-Time Uploads Setup Guide / 实时资料上传配置指南

This site works out-of-the-box on GitHub Pages with:
- All 15 courses, 56 chapters, 123 lectures built automatically via GitHub Actions (`.github/workflows/deploy.yml`).
- Chapter-level & course-level upload widgets + a global **Upload Center** (`upload.html`).
- Static repo uploads (`uploads/<course_id>/part-<N>/`) automatically indexed by `build.py`.

## Enable Live Shared Uploads for Everyone (2 Minutes, Free)

To let **anyone** upload PDFs, PPTX, DOCX, images, or Markdown notes directly on the website **without a GitHub account** and have everyone see updates in real time:

1. **Create a free Supabase project** at [supabase.com](https://supabase.com) (free tier: 500 MB database + 1 GB file storage).
2. Open **SQL Editor** in your Supabase dashboard, paste the full contents of [`supabase/schema.sql`](supabase/schema.sql), and click **Run**.
3. Go to **Project Settings → API** and copy:
   - **Project URL** (`https://xxxxx.supabase.co`)
   - **anon / public key** (`eyJ...`)
4. Paste them into [`assets/config.js`](assets/config.js):
   ```js
   window.STUDY_SITE_CONFIG = {
     supabaseUrl: "https://xxxxx.supabase.co",
     supabaseAnonKey: "eyJ...",
     storageBucket: "materials",
     tableName: "chapter_materials",
     requirePasscode: false, // set true to require a class passcode
     githubRepo: "YOUR_USER/YOUR_REPO",
     maxFileSizeMB: 25,
     ...
   };
   ```
5. Commit and push to `main`. GitHub Actions will automatically redeploy GitHub Pages in ~30 seconds, and the site badge will turn green (**● 实时云端同步已开启**).

### Optional: Require a Class Passcode
1. In Supabase SQL Editor, run:
   ```sql
   drop policy if exists "Public can insert chapter materials" on public.chapter_materials;
   ```
2. Update `'LUT2026'` inside `submit_material` in `supabase/schema.sql` to your preferred passcode and re-run that function.
3. Set `requirePasscode: true` in `assets/config.js`.
