-- ============================================================================
-- LUT Study Site — Supabase Free-Tier Real-Time Uploads Schema
-- Paste this entire file into Supabase Dashboard -> SQL Editor -> Run
-- ============================================================================

-- 1. Materials metadata table
create table if not exists public.chapter_materials (
  id uuid primary key default gen_random_uuid(),
  course_id text not null,
  part_index integer not null check (part_index >= 1),
  part_name text not null,
  title text not null check (char_length(title) between 1 and 200),
  description text default '' check (char_length(description) <= 500),
  kind text not null check (kind in ('file', 'note')),
  file_name text,
  file_path text,
  file_size bigint check (file_size is null or (file_size >= 0 and file_size <= 26214400)),
  mime_type text,
  note_markdown text check (note_markdown is null or char_length(note_markdown) <= 50000),
  uploader text not null default '同学' check (char_length(uploader) <= 60),
  created_at timestamptz not null default now()
);

create index if not exists idx_chapter_materials_lookup
  on public.chapter_materials (course_id, part_index, created_at desc);

-- 2. Enable Row Level Security (public read + public insert)
alter table public.chapter_materials enable row level security;

drop policy if exists "Public can read chapter materials" on public.chapter_materials;
create policy "Public can read chapter materials"
  on public.chapter_materials for select
  to anon, authenticated
  using (true);

drop policy if exists "Public can insert chapter materials" on public.chapter_materials;
create policy "Public can insert chapter materials"
  on public.chapter_materials for insert
  to anon, authenticated
  with check (true);

-- 3. Optional: Passcode-protected insert RPC
-- If you want to require a class passcode for uploads:
--   (a) Drop the "Public can insert chapter materials" policy above
--   (b) Change 'LUT2026' below to your secret class passcode
--   (c) Set requirePasscode: true in assets/config.js
create or replace function public.submit_material(
  p_passcode text,
  p_course_id text,
  p_part_index integer,
  p_part_name text,
  p_title text,
  p_description text,
  p_kind text,
  p_file_name text,
  p_file_path text,
  p_file_size bigint,
  p_mime_type text,
  p_note_markdown text,
  p_uploader text
) returns public.chapter_materials
language plpgsql
security definer
as $$
declare
  v_row public.chapter_materials;
begin
  if p_passcode <> 'LUT2026' then
    raise exception 'Invalid class passcode / 班级口令错误';
  end if;

  insert into public.chapter_materials (
    course_id, part_index, part_name, title, description, kind,
    file_name, file_path, file_size, mime_type, note_markdown, uploader
  ) values (
    p_course_id, p_part_index, p_part_name, p_title, coalesce(p_description, ''), p_kind,
    p_file_name, p_file_path, p_file_size, p_mime_type, p_note_markdown, coalesce(nullif(p_uploader, ''), '同学')
  )
  returning * into v_row;

  return v_row;
end;
$$;

grant execute on function public.submit_material to anon, authenticated;

-- 4. Public Storage bucket for lecture files (up to 25 MB)
insert into storage.buckets (id, name, public, file_size_limit)
values ('materials', 'materials', true, 26214400)
on conflict (id) do update set public = true, file_size_limit = 26214400;

drop policy if exists "Public read materials bucket" on storage.objects;
create policy "Public read materials bucket"
  on storage.objects for select
  to anon, authenticated
  using (bucket_id = 'materials');

drop policy if exists "Public upload materials bucket" on storage.objects;
create policy "Public upload materials bucket"
  on storage.objects for insert
  to anon, authenticated
  with check (bucket_id = 'materials');

-- 5. Enable Realtime publication
alter publication supabase_realtime add table public.chapter_materials;
