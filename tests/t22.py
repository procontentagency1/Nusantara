from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--disable-gpu'])
    pg = b.new_page(viewport={'width':780,'height':360}, device_scale_factor=2)
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + __import__('os').path.abspath('index.html')); pg.wait_for_timeout(1500)
    pg.evaluate("() => selectNation('Majapahit')"); pg.evaluate("() => $('btnStart').click()"); pg.wait_for_timeout(800)
    ev=lambda s: pg.evaluate(s)
    print('init', ev("() => [G.rs, Object.keys(G.pr).length, unity(), tolTrue(), tolHeretic(), tolHeathen(), econ().net.toFixed(2), stabCost()]"))
    print('religions owned', ev("() => { const o={}; for (const id in G.pv) o[relOf(id)]=(o[relOf(id)]||0)+1; return o; }"))
    # non-state prov penalty
    print('heathen', ev("() => { const id=+Object.keys(G.pv)[0]; const n0=econ().tax; G.pr[id]='islam'; const r=[relFac(id), unrestOf(id), unity(), stabCost(), econ().tax<n0]; return r; }"))
    # missionary conversion
    print('miss', ev("() => { const id=+Object.keys(G.pv)[0]; sendMiss(id); const r=[G.miss.length, unrestOf(id), econ().misCost.toFixed(2)]; for(let i=0;i<60;i++) relMonth(); return r.concat([relOf(id), G.miss.length]); }"))
    # state religion change
    print('chrel', ev("() => { const id=+Object.keys(G.pv)[0]; G.pr[id]='islam'; G.mana[0]=500; chRel('islam'); return [G.rs, NATS.Majapahit.relig, G.stab, G.mod.map(m=>m.id), G.mana[0]]; }"))
    ev("() => { G.rs='siwa'; NATS.Majapahit.relig='Siwa-Buddha'; for (const id in G.pv) G.pr[id]='siwa'; G.mod=[]; }")
    # islam event
    print('cand', ev("() => candIslam().length"))
    ev("() => { const id=+Object.keys(G.pv).find(i=>PROV[i].t==='coast'); const nb=LINK[id][0].to; G.pr[nb]='islam'; G.y=1400; }")
    print('cand2', ev("() => candIslam().length"), ev("() => fireEvent('islam_menyebar')")); pg.wait_for_timeout(200); pg.screenshot(path='z_isl.png')
    pg.click('#modal .mo button >> nth=0'); print('after islam', ev("() => [relOf(G.evx.islam), G.mod.map(m=>m.id)]"))
    # tech
    ev("() => { G.y=1350; }")
    print('tech cost', ev("() => [0,1,2].map(i=>techBreak(i))"))
    print('tech cost 1380', ev("() => { G.y=1380; return [techBreak(0), aiTech()]; }"))
    print('buy', ev("() => { G.mana[0]=2000; const c=techCost(0); act.tech({dataset:{i:0}}); return [G.tech[0], G.mana[0], c, techBreak(0).tot]; }"))
    # institutions
    ev("() => { G.y=1399; G.mo=11; }"); 
    print('inst', ev("() => { G.y=1400; instMonth(); return [G.inst.pelayaran.on, Object.keys(G.inst.pelayaran.pv).length, instPen(), techBreak(1).tot, instShare('pelayaran').toFixed(2)]; }"))
    print('spread', ev("() => { for(let i=0;i<200;i++) instMonth(); return [Object.keys(G.inst.pelayaran.pv).length, instShare('pelayaran').toFixed(2), embCost('pelayaran')]; }"))
    print('embrace', ev("() => { G.treasury=2000; const t=G.treasury, c=embCost('pelayaran'); embrace('pelayaran'); return [G.inst.pelayaran.emb, t-G.treasury==c, instPen(), modSum('prod'), G.mod.map(m=>m.id)]; }"))
    # ideas
    print('ideas', ev("() => { G.mana=[2000,2000,2000]; const r=[ideaSlots()]; buyIdea(); r.push(G.ideas.length); buyIdea(); r.push(G.ideas.length); G.tech=[6,6,6]; r.push(ideaSlots()); for(let i=0;i<8;i++) buyIdea(); r.push(G.ideas.length, modSum('tolT'), modSum('adm'), dipMax(), ideaName(0)); return r; }"))
    print('econ bankr tech', ev("() => { G.bank=60; return techCost(0); }"))
    # windows render
    for w in ['nation','rel','tech','ide','econ']:
        ev("() => { winMode='%s'; renderWin(); }"%w); pg.wait_for_timeout(250); pg.screenshot(path='z_w_%s.png'%w)
    ev("() => { winMode='prov'; winProv=+Object.keys(G.pv)[0]; G.pr[winProv]='hindu'; renderWin(); }"); pg.wait_for_timeout(250); pg.screenshot(path='z_w_prov.png')
    # save/load compat & monthTick
    print('monthTick', ev("() => { monthTick(); const s=JSON.parse(localStorage.getItem(SAVE_KEY)); return [!!s.pr, s.rs, s.ideas.length, Object.keys(s.inst)]; }"))
    print('old save', ev("() => { const g=JSON.parse(JSON.stringify(G)); delete g.pr; delete g.rs; delete g.miss; delete g.inst; delete g.ideas; const old=G; G=g; fixSave(); const r=[G.rs, Object.keys(G.pr).length, G.ideas.length]; G=old; return r; }"))
    ev("() => { paused=false; }")
    ev("() => { for (let i=0;i<1500;i++) { dayTick(); if (G.ev.length) G.ev.shift(); } }")
    print('4y', ev("() => [G.y, G.fired, Object.keys(G.inst).map(k=>G.inst[k].on), Object.keys(G.pr).filter(i=>G.pr[i]==='islam').length]"))
    print(errs); b.close()
