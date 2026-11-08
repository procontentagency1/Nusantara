from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--disable-gpu'])
    pg = b.new_page(viewport={'width':800,'height':360})
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + __import__('os').path.abspath('index.html')); pg.wait_for_timeout(1500)
    pg.evaluate("() => selectNation('Majapahit')"); pg.evaluate("() => $('btnStart').click()"); pg.wait_for_timeout(800)
    ev=lambda s: pg.evaluate(s)
    e=ev("() => { const e=econ(); return {net:e.net,tax:e.tax,prod:e.prod,ls:e.loanSize,dev:e.totDev,rate:e.rate,t:G.treasury} }"); print('econ',e)
    # event
    print('fire', ev("() => fireEvent('panen_raya')"), ev("() => [$('modal').classList.contains('open'), paused, G.ev.length]"))
    pg.screenshot(path='z_ev.png')
    t0=ev("() => G.treasury"); pg.click('#modal .mo button >> nth=0'); print('after pick gold', ev("() => [G.treasury-%s, $('modal').classList.contains('open'), G.fired]"%t0))
    print('refire once=false', ev("() => fireEvent('panen_raya')")); pg.click('#modal .mo button >> nth=1'); print('mod', ev("() => [G.mod.map(m=>m.id), econ().tax]"))
    # mod expiry
    ev("() => { for (let i=0;i<12;i++) { G.mod.forEach(m=>{}); modMonth(); } }"); print('mods after 12m', ev("() => G.mod.length"))
    # loans
    ev("() => { winMode='econ'; renderWin(); }"); pg.wait_for_timeout(300); pg.screenshot(path='z_eco.png')
    print('loan', ev("() => { takeLoan(false); takeLoan(false); return [G.ln.length, G.loans, G.infl, econ().interest, econ().rate]; }"))
    print('repay', ev("() => { repayLoan(); return [G.ln.length, G.loans]; }"))
    print('expire renew', ev("() => { G.ln[0].left=1; const t=G.treasury; G.treasury=0; ecoMonth(); const r=[G.ln[0].left, G.infl]; G.treasury=t; return r; }"))
    print('expire pay', ev("() => { G.ln[0].left=1; G.treasury=1000; ecoMonth(); return [G.ln.length, G.treasury]; }"))
    # bankruptcy
    print('bank', ev("() => { G.infl=4; G.ln=[]; for(let i=0;i<5;i++) takeLoan(true); G.treasury=-5000; ecoMonth(); return [G.bank, G.ln.length, G.loans, G.infl, G.treasury, econ().mpRec, techCost(), loanRate()]; }"))
    print('modal', ev("() => [$('modal').classList.contains('open'), $('modal').textContent.slice(0,40)]")); pg.screenshot(path='z_bank.png')
    pg.click('#modal .mo button'); 
    # inflation affects costs
    print('infl cost', ev("() => { G.infl=10; return [recCost(), bCost(BUILD.kuil)]; }"))
    # monthTick full and save/load
    print('monthTick', ev("() => { G.treasury=100; monthTick(); const s=JSON.parse(localStorage.getItem(SAVE_KEY)); return [s.ln.length, s.bank, s.infl, 'flags' in s, 'mod' in s]; }"))
    # old save compat
    print('fixSave', ev("() => { const g=JSON.parse(JSON.stringify(G)); delete g.ln; delete g.mod; delete g.fired; delete g.evq; delete g.flags; g.loans=100; const old=G; G=g; fixSave(); const r=[G.ln, G.mod.length, G.fired.length]; G=old; return r; }"))
    # run game 2 years at max speed for random events + errors
    ev("() => { paused=false; speed=5; }"); pg.wait_for_timeout(100)
    ev("() => { for (let i=0;i<730;i++) { dayTick(); if (G.ev.length) { G.ev.shift(); } } }")
    print('2y', ev("() => [G.y, G.fired, Math.round(G.treasury), G.bank, G.ln.length]"))
    print(errs); b.close()
