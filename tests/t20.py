from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--disable-gpu'])
    pg = b.new_page(viewport={'width':800,'height':360})
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + __import__('os').path.abspath('index.html')); pg.wait_for_timeout(1500)
    pg.evaluate("() => selectNation('Majapahit')"); pg.evaluate("() => $('btnStart').click()"); pg.wait_for_timeout(800)
    pg.evaluate("() => selectArmy(myArmies()[0].id, true)"); pg.wait_for_timeout(900)
    print(pg.evaluate("() => [G.sel, $('desel').style.display]")); pg.screenshot(path='z_desel.png')
    pg.click('#desel'); print(pg.evaluate("() => [G.sel, $('desel').style.display]"))
    pg.evaluate("() => { const a=myArmies()[0]; selectArmy(a.id); onMapTap({k:'L',id:a.loc},0,0); }"); print(pg.evaluate("() => G.sel"))
    print(errs); b.close()
