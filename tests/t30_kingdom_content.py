from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""()=>{newGame('Sunda');beginGame();const count=activeMissions().length;const local=activeMissions().filter(m=>m.id.includes('_Sunda')).length;for(let i=0;i<60;i++)aiContentMonth();const states=Object.values(G.aiContent);saveGame(true);winMode='worldcontent';renderWin();return {count,local,decisions:states.reduce((n,s)=>n+s.events,0),saved:!!JSON.parse(localStorage.getItem(SAVE_KEY)).aiContent,kingdoms:Object.keys(G.aiContent).length};}""")
 print(result);assert result['count']==8 and result['local']==2 and result['decisions']>0 and result['saved']
 page.screenshot(path='/tmp/kingdom-content.png')
 assert not errors,errors
 b.close()
s.shutdown()
