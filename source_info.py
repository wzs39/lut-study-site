"""Truthful optional provenance, with validated public attachment paths."""
from datetime import date
import hashlib
import html
import json
from pathlib import Path
from urllib.parse import quote, urlsplit


class SourceCatalogue:
    def __init__(self, root):
        self.root = Path(root).resolve()
        path = self.root / 'data/source-metadata.json'
        data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'version':1,'lectures':{}}
        if data.get('version') != 1 or not isinstance(data.get('lectures'), dict):
            raise ValueError('Invalid source metadata schema')
        self.lectures = data['lectures']

    def get(self, lecture_id):
        row = self.lectures.get(lecture_id, {})
        reviewed = row.get('reviewed_at')
        if reviewed and date.fromisoformat(reviewed) > date.today():
            raise ValueError('Review date is in the future: ' + lecture_id)
        for source in row.get('sources', []):
            if source.get('path'):
                path = Path(source['path'])
                target = (self.root / path).resolve()
                if path.is_absolute() or '..' in path.parts or not target.is_relative_to(self.root) or path.parts[0] not in ('sources','uploads') or not target.is_file():
                    raise ValueError('Missing or nonpublic source: ' + str(path))
                if target.suffix.lower() not in ('.pdf','.pptx','.ppt','.docx','.doc','.txt','.md','.png','.jpg','.jpeg','.webp','.zip','.py','.ipynb','.xlsx','.csv'):
                    raise ValueError('Unsupported attachment type')
            if source.get('url'):
                url = urlsplit(source['url'])
                if url.scheme != 'https' or not url.hostname or url.username or url.password:
                    raise ValueError('Source URL must use HTTPS')
            if 'page' in source and (type(source['page']) is not int or source['page'] < 1):
                raise ValueError('Source page must be a positive integer')
        return row


def source_panel(course, lecture, catalogue, prefix='../../'):
    row = catalogue.get(course['id'] + '/' + lecture['slug'])
    sources = row.get('sources') or [{'name':name} for name in lecture.get('source_files', [])]
    attached = sum(bool(item.get('path') or item.get('url')) for item in sources)
    esc = lambda value: html.escape(str(value), quote=True)
    items = []
    for source in sources:
        name = source.get('name') or source.get('path') or source.get('url')
        url = prefix + quote(source['path'].replace('\\','/'), safe='/') if source.get('path') else source.get('url')
        if url:
            if source.get('page') and urlsplit(url).path.lower().endswith('.pdf'):
                url = url.split('#')[0] + '#page=' + str(source['page'])
            items.append('<li><a href="%s" target="_blank" rel="noopener">%s%s ↗</a></li>' % (esc(url),esc(name), ' · 第 %d 页' % source['page'] if source.get('page') else ''))
        else:
            items.append('<li><code>%s</code> <span class="sub">未附原文件</span></li>' % esc(name))
    revision = hashlib.sha256(lecture.get('html','').encode()).hexdigest()[:12]
    return ('<details class="lecture-sources"><summary>资料来源 · %d 项 / 已附 %d 项</summary>'
            '<dl class="source-metadata"><dt>资料版本</dt><dd>%s</dd><dt>最近核对</dt><dd>%s</dd>'
            '<dt>整理内容指纹</dt><dd><code>%s</code>（用于识别内容变更）</dd></dl><ul>%s</ul>'
            '<p class="sub">未附文件仅列原始名称；版本与核对日期由维护者登记。</p></details>') % (
                len(sources), attached, esc(row.get('source_version') or '未记录'), esc(row.get('reviewed_at') or '未记录'), revision, ''.join(items))
