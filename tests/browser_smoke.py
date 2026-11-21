"""Browser acceptance checks. CI launches Chromium; local work may attach to owned CDP."""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import json
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextmanager
def site():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield "http://127.0.0.1:%d/" % server.server_port
    finally:
        server.shutdown()
        server.server_close()


def check_learning(context, base):
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(base + "index.html")
    page.locator("#q").fill("二进制浮点")
    page.wait_for_function("document.querySelectorAll('#search-result-list li').length>0")
    assert page.locator("#search-result-list mark").count() > 0
    page.locator("#search-result-list a").first.click()
    page.wait_for_selector("article[data-lecture-id]")
    assert page.locator(".search-jump").is_visible()
    lecture_id = page.locator("article[data-lecture-id]").get_attribute("data-lecture-id")
    lecture_url = page.url.split("?")[0].split("#")[0]
    page.get_by_role("radio", name="已掌握", exact=True).check()
    page.goto(base + "review.html")
    checkbox = page.locator('input.tick[data-study-id="%s"]' % lecture_id)
    assert checkbox.is_checked()
    checkbox.uncheck()
    page.goto(lecture_url)
    assert page.get_by_role("radio", name="待复习", exact=True).is_checked()

    page.locator(".reader-options summary").click()
    page.locator("#reader-font").select_option("22")
    page.locator("#reader-line").select_option("2.1")
    page.reload()
    assert page.locator("#reader-font").input_value() == "22"
    assert page.locator("#reader-line").input_value() == "2.1"
    page.locator("#focus-reading").click()
    assert not page.locator(".page-side").is_visible()
    assert page.locator("#focus-exit").is_visible()
    page.locator("#focus-exit").click()
    assert page.locator(".page-side").is_visible()
    context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base.rstrip("/"))
    page.locator(".copy-code").first.click()
    page.wait_for_function("document.querySelector('#study-notice').textContent.includes('代码已复制')")
    image = page.locator(".page-content img").first
    image.scroll_into_view_if_needed()
    image.click()
    assert page.locator(".image-viewer").is_visible()
    page.keyboard.press("Escape")
    assert not page.locator(".image-viewer").is_visible()

    question = page.locator("select[data-practice-id]").first
    question.select_option("wrong")
    page.goto(base + "index.html")
    page.locator("#practice-book summary").click()
    assert int(page.locator("#practice-book-count").text_content()) >= 1
    page.locator(".practice-book-item a").first.click()
    assert page.url.endswith("#practice-1")
    assert page.locator("select[data-practice-id]").first.input_value() == "wrong"
    page.wait_for_function("Object.values(JSON.parse(localStorage.getItem('lut-learning-v1')).lectures).some(x=>x.anchor)")
    page.goto(base + "index.html")
    assert page.locator(".continue-link").is_visible()

    page.locator("#q").fill('<img src=x onerror="window.__searchAttack=1">')
    page.locator("#search-form button[type=submit]").click()
    page.wait_for_function("document.querySelector('#search-status').textContent.includes('没有匹配')")
    assert page.evaluate("window.__searchAttack") is None
    # Content updates keep the learning status but invalidate the old reading anchor.
    page.evaluate('(id)=>{var s=JSON.parse(localStorage.getItem("lut-learning-v1"));s.lectures[id].revision="000000000000";s.lectures[id].anchor="sec-practice";localStorage.setItem("lut-learning-v1",JSON.stringify(s));}',lecture_id)
    page.goto(lecture_url+'?resume=1#sec-practice')
    page.wait_for_function('location.hash==="#sec-overview"')
    assert page.get_by_role('radio',name='待复习',exact=True).is_checked()
    assert not errors, errors
    page.close()
    print("PASS: full-text deep links, progress/review, resume, preferences/focus, code copy, image dialog, practice and query text safety", flush=True)


def check_offline(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto((ROOT / "index.html").as_uri())
    page.locator("#q").fill("二进制浮点")
    page.wait_for_function("document.querySelectorAll('#search-result-list li').length>0")
    context.close()
    print("PASS: offline file:// full-text search", flush=True)


def check_layout(context, base):
    catalogue=json.loads((ROOT/'data/learning-catalog.js').read_text(encoding='utf-8').split('=',1)[1].rstrip(';\n'))
    first=catalogue['lectures'][0];course=first['course'];lecture=first['url']
    paths=['index.html','review.html','extend.html','all.html','upload.html',f'c/{course}/index.html',f'c/{course}/part-1.html',lecture,f'c/{course}/reader.html']
    page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    for width in [320,768,1024,1440]:
        page.set_viewport_size({'width':width,'height':1000})
        for path in paths:
            page.goto(base+path)
            page.wait_for_function('window.LUTLearning !== undefined')
            assert page.locator('nav[aria-label="站点导航"] a').count()==5,(path,width)
            assert page.locator('#directory-toggle').count()==1
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),(path,width,page.evaluate('document.documentElement.scrollWidth'))
            if width==320:
                page.locator('#directory-toggle').click()
                assert page.locator('#directory-content').is_visible()
                page.locator('#directory-toggle').click()
        page.goto(base+lecture)
        page.locator('.reader-options summary').click()
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),('expanded preferences',width)
    page.goto(base+lecture)
    assert '未记录' in page.locator('.lecture-sources').text_content()
    assert '未附原文件' in page.locator('.lecture-sources').text_content()
    image_lecture=next((c['id'],l['slug']) for path in sorted((ROOT/'content').glob('*.json')) for c in [json.loads(path.read_text(encoding='utf-8'))] for l in c['lectures'] if '<img ' in l.get('html',''))
    page.goto(base+'c/%s/%s.html'%image_lecture)
    image=page.locator('.page-content img').first
    assert int(image.get_attribute('width'))>0 and image.get_attribute('data-full-src')
    image.scroll_into_view_if_needed();image.click()
    assert page.locator('.image-viewer img').get_attribute('src')==page.evaluate('(source)=>new URL(source,location.href).href',image.get_attribute('data-full-src'))
    page.keyboard.press('Escape')
    trigger=image.locator('..');trigger.focus();page.keyboard.press('Enter')
    assert page.locator('.image-viewer').is_visible()
    page.keyboard.press('Escape')
    assert trigger.evaluate('(el)=>document.activeElement===el')
    assert not errors,errors
    if os.environ.get('QA_OUTPUT'):
        output=Path(os.environ['QA_OUTPUT']);output.mkdir(parents=True,exist_ok=True)
        for width in [320,1440]:
            page.set_viewport_size({'width':width,'height':1000});page.goto(base+lecture)
            page.screenshot(path=str(output/f'lecture-{width}.png'))
        page.goto(base+'index.html');page.screenshot(path=str(output/'home-1440.png'))
        page.emulate_media(color_scheme='dark');page.reload()
        assert page.evaluate('getComputedStyle(document.documentElement).getPropertyValue("--bg").trim()')=='#12161c'
        page.screenshot(path=str(output/'home-dark-1440.png'))
    page.close();print('PASS: 9 page types × 4 viewport widths, unified navigation, provenance and original-image access',flush=True)


def check_sharing(browser,base):
    context=browser.new_context();page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(base+'upload.html');page.wait_for_selector('.mat-form')
    page.locator('[data-mode="note"]').click()
    for number in [1,2]:
        page.locator('input[name="title"]').fill('Browser test note')
        page.locator('textarea[name="note_markdown"]').fill('Revision '+str(number)+' <img src=x onerror="window.__noteAttack=1">')
        page.locator('.mat-form button[type="submit"]').click()
        page.wait_for_function("document.querySelector('.mat-status').textContent.includes('仅当前浏览器可见')")
        page.wait_for_function("!document.querySelector('.mat-form button[type=submit]').disabled")
    page.wait_for_function("document.querySelectorAll('.mat-item').length===2")
    assert page.locator('.mat-item:visible').count()==1
    page.get_by_role('button',name='展开较早的同名记录',exact=False).click()
    assert page.locator('.mat-item:visible').count()==2
    page.locator('.mat-item button[data-act="preview"]').first.click()
    assert page.locator('dialog.mat-modal').is_visible()
    assert page.evaluate('window.__noteAttack') is None
    page.keyboard.press('Escape');assert not page.locator('dialog.mat-modal').is_visible()
    page.reload();page.wait_for_selector('.mat-item');assert page.locator('.mat-item').count()==2

    requests=[];cloud=[];service_state={'fail_post':False}
    def service(route):
        request=route.request;requests.append(request.method)
        assert request.headers.get('apikey')=='sb_publishable_test'
        assert 'authorization' not in request.headers
        if request.method=='POST' and service_state['fail_post']:
            route.fulfill(status=403,content_type='application/json',body='{"message":"test write denied"}')
            return
        if request.method=='POST':
            data=request.post_data_json;cloud.append({**data,'id':'contract-record','created_at':'2020-01-01T00:00:00Z'})
        route.fulfill(status=201 if request.method=='POST' else 200,content_type='application/json',body=json.dumps(cloud))
    context.route('https://learning-test.supabase.co/**',service)
    page.locator('#sharing-setup summary').click()
    page.locator('#sharing-url').fill('https://learning-test.supabase.co')
    page.locator('#sharing-key').fill('sb_secret_test')
    page.locator('#sharing-test').click()
    page.wait_for_function("document.querySelector('#sharing-status').textContent.includes('公开')")
    assert not requests
    page.locator('#sharing-key').fill('sb_publishable_test')
    page.locator('#sharing-test').click()
    page.wait_for_function("!document.querySelector('#sharing-save').disabled")
    assert requests==['GET']
    page.locator('#sharing-save').click();page.wait_for_selector('.mat-form')
    page.locator('[data-mode="note"]').click()
    page.locator('input[name="title"]').fill('Cloud contract test')
    page.locator('textarea[name="note_markdown"]').fill('Simulated service contract; no real upload')
    page.locator('.mat-form button[type="submit"]').click()
    page.wait_for_function("document.querySelector('.mat-status').textContent.includes('云端已收录')")
    assert len(cloud)==1 and cloud[0]['kind']=='note'
    service_state['fail_post']=True
    page.locator('input[name="title"]').fill('Rejected contract test')
    page.locator('textarea[name="note_markdown"]').fill('Keep this draft after a failed request')
    page.locator('.mat-form button[type="submit"]').click()
    page.wait_for_function("document.querySelector('.mat-status').textContent.includes('403')")
    assert page.locator('textarea[name="note_markdown"]').input_value()=='Keep this draft after a failed request'
    assert len(cloud)==1
    assert not errors,errors
    context.close();print('PASS: local publication/persistence/history, safe note preview, public-key validation, read-only connection and mocked cloud POST contract',flush=True)


def main():
    with site() as base, sync_playwright() as p:
        cdp = os.environ.get("BROWSER_CDP")
        browser = p.chromium.connect_over_cdp(cdp) if cdp else p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width":1440,"height":1000}, reduced_motion="reduce")
        try:
            check_learning(context, base)
            check_layout(context, base)
            check_sharing(browser, base)
            check_offline(browser)
        finally:
            context.close()
            if not cdp:
                browser.close()


if __name__ == "__main__":
    main()
