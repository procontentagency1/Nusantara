from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 page.evaluate("newGame('Majapahit'); beginGame(); paused=true")
 result=page.evaluate("""() => { const n=activeMissions().length; completeMission('jawa'); const locked=!G.missions.includes('jawa'); G.regs=Math.ceil(econ().fl); completeMission('prajurit'); G.prestige=20; completeMission('palapa'); const claims=missionTargets(['Sunda','Bali']).every(p=>G.claims.includes(p.id)||OWNR[p.id]===G.nat); const before=G.claims.length; completeMission('palapa'); const once=G.claims.length===before; G.subj.Sunda=G.nat; G.subj.Bali=G.nat; completeMission('jawa'); const subject=G.missions.includes('jawa'); saveGame(true); const saved=JSON.parse(localStorage.getItem(SAVE_KEY)).missions.includes('jawa'); newGame('Sunda'); const generic=activeMissions().length; completeMission('palapa'); const exclusive=!G.missions.includes('palapa'); return {n,locked,claims,once,subject,saved,generic,exclusive}; }""")
 print(result); assert result['n']==12 and result['generic']==6 and all(result[k] for k in ['locked','claims','once','subject','saved','exclusive'])
 page.evaluate("winMode='missions'; missionBranch='Ekspansi'; renderWin()")
 page.screenshot(path='/tmp/missions-expanded.png')
 assert not errors,errors
 b.close()
s.shutdown()
