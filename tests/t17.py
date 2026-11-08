from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--disable-gpu'])
    pg = b.new_page(viewport={'width':800,'height':360})
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + __import__('os').path.abspath('index.html')); pg.wait_for_timeout(2500)
    pg.evaluate("() => { selectNation('Majapahit'); $('btnStart').click(); paused = true; }")
    r = pg.evaluate("""() => { const t0 = performance.now(); let nb = 0, ev = 0; const seen = new Set();
      for (let i = 0; i < 365*8; i++) { dayTick(); for (const b of G.battles) seen.add(b.id); if (G.ev.length) { G.ev = []; } }
      return { ms: Math.round(performance.now()-t0), year: G.y, wars: G.wars.length, battlesSeen: seen.size, live: G.battles.length, armies: G.armies.length,
        wexMax: Math.max(0,...Object.values(G.wex||{})), aeMax: Math.max(0,...Object.values(G.ae||{})), owners: new Set(Object.values(OWNR)).size, log: G.log.slice(0,4) }; }""")
    print(r); print(errs); b.close()
