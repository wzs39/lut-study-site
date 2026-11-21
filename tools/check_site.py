"""Validate generated local links, anchors, scripts and measured image assets."""
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self,path):
        super().__init__(convert_charrefs=True)
        self.ids=set();self.links=[];self.images=[]
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self,tag,attrs):
        row=dict(attrs)
        if row.get('id'):self.ids.add(row['id'])
        if tag in ('a','link') and row.get('href'):self.links.append(row['href'])
        if tag in ('img','script','iframe') and row.get('src'):self.links.append(row['src'])
        if tag=='img':self.images.append(row)


def check(root=ROOT):
    files=sorted(root.glob('*.html'))+sorted((root/'c').glob('*/*.html'))
    pages={path.resolve():Page(path) for path in files}
    errors=[];links=images=0
    for path,page in pages.items():
        for href in page.links:
            links+=1;url=urlsplit(href)
            if url.scheme or url.netloc:continue
            target=(path.parent/unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append('%s: missing/nonpublic target %s' % (path.relative_to(root),href));continue
            if url.fragment and target.suffix=='.html':
                if target not in pages:pages[target]=Page(target)
                if unquote(url.fragment) not in pages[target].ids:errors.append('%s: missing anchor %s' % (path.relative_to(root),href))
        for image in page.images:
            images+=1
            if image.get('src','').startswith(('http:','https:','data:')):continue
            if not all(image.get(key,'').isdigit() and int(image[key])>0 for key in ('width','height')):
                errors.append('%s: image missing intrinsic dimensions %s' % (path.relative_to(root),image.get('src')))
    manifest=root/'assets/media-manifest.json'
    if manifest.exists():
        for name,row in json.loads(manifest.read_text(encoding='utf-8')).items():
            source=root/name;preview=root/row['preview']
            if not preview.is_file() or preview.stat().st_size!=row['previewBytes']:errors.append('Preview missing/stale: '+name)
            if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest()!=row['sha256']:errors.append('Original missing/changed: '+name)
    return {'pages':len(files),'links':links,'images':images,'errors':errors}


if __name__=='__main__':
    result=check();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
