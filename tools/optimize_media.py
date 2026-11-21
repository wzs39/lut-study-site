"""Create separate WebP previews (lossless diagrams, quality-90 JPEG conversions). Requires Pillow."""
import hashlib
from io import BytesIO
import json
from pathlib import Path
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parents[1]


def main():
    result={};source_bytes=preview_bytes=0;optimized=0
    for path in sorted((ROOT/'assets').rglob('*')):
        if not path.is_file() or 'optimized' in path.parts or path.suffix.lower() not in ('.jpg','.jpeg','.png','.webp','.gif'):continue
        raw=path.read_bytes();relative=path.relative_to(ROOT).as_posix()
        with Image.open(path) as image:
            if getattr(image,'n_frames',1)>1:continue
            image=ImageOps.exif_transpose(image)
            if image.mode not in ('RGB','RGBA'):image=image.convert('RGBA' if 'transparency' in image.info else 'RGB')
            # Lossless preserves small diagram text; only oversized raster pages are resized.
            image.thumbnail((1800,1800),Image.Resampling.LANCZOS)
            output=BytesIO();image.save(output,format='WEBP',lossless=path.suffix.lower() not in ('.jpg','.jpeg'),quality=90,method=4)
            preview=output.getvalue();target=relative
            if len(preview)<len(raw)*.9:
                digest=hashlib.sha256(raw).hexdigest()[:20]
                target='assets/optimized/'+digest+'.webp'
                destination=ROOT/target;destination.parent.mkdir(parents=True,exist_ok=True)
                if not destination.exists() or destination.read_bytes()!=preview:destination.write_bytes(preview)
                optimized+=1
                width,height=image.size
            else:
                preview=raw
                with Image.open(path) as original:width,height=original.size
            source_bytes+=len(raw);preview_bytes+=len(preview)
            result[relative]={'preview':target,'width':width,'height':height,'sourceBytes':len(raw),'previewBytes':len(preview),'sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'assets/media-manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'images':len(result),'optimized':optimized,'sourceBytes':source_bytes,'previewBytes':preview_bytes,'savedPercent':round((1-preview_bytes/source_bytes)*100,1)}))


if __name__=='__main__':main()
