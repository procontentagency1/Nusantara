from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--disable-gpu'])
    pg = b.new_page(viewport={'width':800,'height':360})
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + __import__('os').path.abspath('index.html')); pg.wait_for_timeout(1500)
    pg.evaluate("() => selectNation('Majapahit')"); pg.evaluate("() => $('btnStart').click()"); pg.wait_for_timeout(800)
    r=pg.evaluate("""() => { G.mana[1]=500; const t=Object.keys(NATS).find(n=>n!==G.nat&&alive(n)&&claimable(n).length); const id=claimable(t)[0];
      act.dact({dataset:{k:'claim',n:t,id}}); const a=G.fab.length;
      act.dact({dataset:{k:'net',n:t}});
      for(let i=0;i<30;i++) dayTick(); const b=netOf(t);
      for(let i=0;i<120;i++) dayTick(); const c=netOf(t);
      act.dact({dataset:{k:'claim',n:t,id}});
      return {t,fabBefore:a,net30:b,net150:c,fabAfter:G.fab.length,netNow:netOf(t),mis:G.mis.map(m=>m.st)}; }""")
    print(r, errs); b.close()
