from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1200)
 result=page.evaluate("""()=>{
 newGame('Majapahit');beginGame();const out={};let f=G.fleets.find(f=>f.nat===G.nat);out.initial=f.ships.length===6&&!!f.port;out.kingdoms=Object.keys(NATS).every(n=>!!portsOf(n).length===G.fleets.some(f=>f.nat===n));
 out.cost=econ().navalCost>0;const g=navalGrid(),target=SEA_PROVS.find(p=>p.id!==f.sea);orderFleet(f,target.id);out.route=f.path.length>0&&f.path.every(p=>g.wet[Math.floor(p[1]/g.cell)*g.w+Math.floor(p[0]/g.cell)]);for(let i=0;i<400&&f.path.length;i++)navyDay();out.arrived=f.sea===target.id&&!f.path.length;
 fleetHome(f);for(let i=0;i<400&&f.path.length;i++)navyDay();out.docked=!!f.port;
 f.ships[0].hp=40;navyMonth();out.repair=f.ships[0].hp===55;
 const port=f.port;G.treasury=1000;G.resourceStocks[G.nat].wood=100;G.resourceStocks[G.nat].iron=100;const count=f.ships.length,cash=G.treasury;act.buildship({dataset:{port:String(port),type:'patrol'}});act.buildship({dataset:{port:String(port),type:'patrol'}});out.queue=G.shipQueue.length===1&&G.treasury===cash-18;for(let i=0;i<4;i++)navyMonth();out.built=f.ships.length===count+1&&G.shipQueue.length===0;
 act.fleettrade({dataset:{id:String(f.id)}});for(let i=0;i<400&&f.path.length;i++)navyDay();const node=seaTradeNode(f.sea),power=tradeSnapshot().nodes[node].raw[G.nat];f.mission='hold';out.patrol=power>tradeSnapshot().nodes[node].raw[G.nat];
 G.al=[];G.subj={};G.tributaries={};declareWar(G.nat,'Sunda',{k:'nocb'});const enemy=G.fleets.find(f=>f.nat==='Sunda');enemy.port=null;enemy.path=[];enemy.x=f.x;enemy.y=f.y;enemy.retreat=0;f.port=null;f.path=[];f.retreat=0;const hp=f.ships.reduce((s,x)=>s+x.hp,0);navyDay();out.battle=f.ships.reduce((s,x)=>s+x.hp,0)<hp&&f.battleDays>0&&SFX.scene==='battle';
 enemy.retreat=20;const safe=enemy.ships.reduce((s,x)=>s+x.hp,0);navyDay();out.retreat=enemy.ships.reduce((s,x)=>s+x.hp,0)===safe;
 applyPeace(G.wars[0],'att',{white:true});out.peaceMusic=f.battleDays===0&&SFX.scene==='peace';
 saveGame(true);const saved=JSON.parse(localStorage.getItem(SAVE_KEY));out.saved=Array.isArray(saved.fleets)&&saved.fleets.length>0;delete G.fleets;fixNavy();out.migrated=G.fleets.some(f=>f.nat===G.nat);const migrated=G.fleets.length;fixNavy();out.noDuplicate=G.fleets.length===migrated;
 const province=PROV[portsOf(G.nat)[0]];setMode('pol');const pol=polFill(province);setMode('religion');const rel=polFill(province);setMode('resources');const res=polFill(province);setMode('trade');const trade=polFill(province);out.filters=new Set([pol,rel,res,trade]).size===4;
 out.noMini=!document.querySelector('#mini,#mm,#mmToggle,#modes');out.oneControl=document.querySelectorAll('#mapViewToggle').length===1;setMode('pol');winMode='navy';renderWin();return out;
 }""")
 print(result,flush=True);assert all(result.values()),result
 page.wait_for_timeout(4000);page.screenshot(path='/tmp/nusantara-navy.png')
 page.locator('#mapViewToggle').click();assert page.locator('#mapViewMenu').is_visible()
 page.locator('[data-mapmode=resources]').click();assert not page.locator('#mapViewMenu').is_visible();assert page.locator('#mapViewToggle').inner_text()=='Peta: Sumber daya ▾'
 page.locator('#mapViewToggle').click();page.keyboard.press('Escape');assert not page.locator('#mapViewMenu').is_visible()
 page.locator('#mapViewToggle').click();page.screenshot(path='/tmp/nusantara-map-dropdown.png')
 page.locator('[data-mapmode=pol]').click()
 page.evaluate("winMode='fleet';const f=G.fleets.find(f=>f.nat===G.nat);G.selFleet=f.id;centerOn(f.x,f.y,fitS*3);renderWin();request()")
 page.wait_for_timeout(500);page.screenshot(path='/tmp/nusantara-fleet-map.png')
 assert not errors,errors
 b.close()
s.shutdown()
