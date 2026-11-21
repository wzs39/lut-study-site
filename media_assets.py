"""Apply measured image metadata to generated HTML, never to source content."""
import html
import json
from pathlib import Path
import re


class MediaAssets:
    def __init__(self, root, manifest=None):
        self.root=Path(root).resolve()
        path=self.root/'assets/media-manifest.json'
        self.manifest=manifest if manifest is not None else (json.loads(path.read_text(encoding='utf-8')) if path.exists() else {})
        for original,row in self.manifest.items():
            for name in (original,row['preview']):
                target=(self.root/name).resolve()
                if not target.is_relative_to(self.root) or not target.is_file():
                    raise ValueError('Missing or escaping image: '+name)
            if row['width']<1 or row['height']<1:raise ValueError('Invalid image dimensions')

    def render(self, body, prefix=''):
        def replace(match):
            tag=match.group(0)
            source=re.search(r'\bsrc="([^"]+)"',tag)
            if not source:return tag
            src=html.unescape(source[1])
            original=src[len(prefix):] if prefix and src.startswith(prefix) else src
            row=self.manifest.get(original)
            if not row:return tag
            # Keep existing semantic classes, alternate text and intentional priority.
            tag=re.sub(r'\s(?:width|height|decoding|data-full-src)="[^"]*"','',tag)
            tag=tag.replace(source[0],'src="'+html.escape(prefix+row['preview'],quote=True)+'"',1)
            attrs=' width="%d" height="%d" decoding="async" data-full-src="%s"' % (row['width'],row['height'],html.escape(src,quote=True))
            if not re.search(r'\bloading=',tag) and 'fetchpriority="high"' not in tag:attrs+=' loading="lazy"'
            return tag.rstrip('/> ')+attrs+'>'
        return re.sub(r'<img\b[^>]*>',replace,body,flags=re.I)
