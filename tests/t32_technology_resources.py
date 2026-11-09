from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""()=>{newGame('Majapahit');beginGame();const early=techCost(0);G.y=techYear(4);const ontime=techCost(0);const timing=early>ontime;G.tech=[4,4,4];G.treasury=1000;const id=Object.keys(G.pv).find(id=>provinceResource(PROV[id])==='food'),stock=G.resourceStocks[G.nat];const wood=stock.wood;act.improveResource({dataset:{id}});act.improveResource({dataset:{id}});const duplicate=stock.wood===wood-5;for(let i=0;i<6;i++)resourcesMonth();const built=G.improvements[id].built;const y=resourceYield(id);G.improvements[id].built=false;const doubled=y===resourceYield(id)*2;G.improvements[id].built=true;const before=G.resourceStocks.Sunda.food;CTRL[id]='Sunda';resourcesMonth();const captured=G.resourceStocks.Sunda.food>before;delete CTRL[id];stock.food=0;const shortage=econ().supplyCost>0;stock.iron=0;const regs=G.regs;act.rec({dataset:{v:'1'}});const blocked=G.regs===regs;stock.iron=3;G.mp=10;act.rec({dataset:{v:'1'}});const iron=stock.iron===2;winMode='resources';renderWin();saveGame(true);return {timing,duplicate,built,doubled,captured,shortage,blocked,iron,saved:!!JSON.parse(localStorage.getItem(SAVE_KEY)).resourceStocks};}""")
 print(result);assert all(result.values())
 page.screenshot(path='/tmp/nusantara-resources.png')
 assert not errors,errors
 b.close()
s.shutdown()
