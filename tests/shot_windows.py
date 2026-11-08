from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--disable-gpu'])
    pg = b.new_page(viewport={'width':780,'height':360}, device_scale_factor=2)
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + __import__('os').path.abspath('index.html')); pg.wait_for_timeout(1500)
    pg.evaluate("() => selectNation('Majapahit')"); pg.evaluate("() => $('btnStart').click()"); pg.wait_for_timeout(800)
    pg.evaluate("() => { fireEvent('wabah_pesisir'); }"); pg.wait_for_timeout(300); pg.screenshot(path='z_ev.png')
    pg.click('#modal .mo button >> nth=0'); pg.wait_for_timeout(200)
    pg.evaluate("() => { takeLoan(false); winMode='econ'; renderWin(); }"); pg.wait_for_timeout(500); pg.screenshot(path='z_eco.png')
    print(errs); b.close()
