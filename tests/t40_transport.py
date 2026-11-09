from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1000)
 result=page.evaluate("""()=>{newGame('Majapahit');beginGame();const f=G.fleets.find(f=>f.nat===G.nat),a=G.armies.find(a=>a.nat===G.nat);a.loc=f.port;a.regs=3;a.path=[];const n=regsOf(G.nat),id=a.id;
 const wrong=mkArmy('Sunda',1,f.port);if(embarkArmy(f,wrong))throw Error('foreign troop loaded');
 if(!embarkArmy(f,a)||G.armies.includes(a)||regsOf(G.nat)!==n)throw Error('embark');
 saveGame(true);G=JSON.parse(localStorage.getItem(SAVE_KEY));fixSave();setWorld();const boat=G.fleets.find(f=>f.nat===G.nat&&f.cargo?.id===id);if(!boat||regsOf(G.nat)!==n)throw Error('save');
 const neutral=NATS.Sunda.ids.find(id=>PROV[id].cd);if(!neutral||orderLanding(boat,neutral))throw Error('neutral landing');const target=portsOf(G.nat).find(p=>p!==boat.port&&navalPath(boat.x,boat.y,p)?.length);if(!target||!orderLanding(boat,target))throw Error('route');
 for(let i=0;i<2000&&boat.cargo;i++){G.d=1;navyDay();}if(boat.cargo||!G.armies.some(a=>a.id===id&&a.loc===target))throw Error('arrival');
 const a2=G.armies.find(a=>a.id===id);a2.loc=boat.port=target;boat.ships=[{type:'dayung',hp:100}];if(embarkArmy(boat,a2))throw Error('capacity');a2.regs=2;if(!embarkArmy(boat,a2))throw Error('load capacity');boat.ships=[];G.d=1;navyDay();if(G.fleets.includes(boat)||regsOf(G.nat)!==0)throw Error('sinking');newGame('Majapahit');beginGame();const invasion=G.fleets.find(f=>f.nat===G.nat),troop=G.armies.find(a=>a.nat===G.nat),shore=NATS.Sunda.ids.find(id=>PROV[id].cd);troop.loc=invasion.port;troop.regs=2;declareWar('Majapahit','Sunda',{k:'nocb'});mkArmy('Sunda',2,shore);if(!embarkArmy(invasion,troop)||!orderLanding(invasion,shore))throw Error('invasion order');for(let i=0;i<2000&&invasion.cargo;i++){G.d=1;navyDay();}if(invasion.cargo||!troop.bt||!G.battles.some(b=>!b.done&&b.loc===shore))throw Error('landing battle');newGame('Majapahit');beginGame();const ai=G.fleets.find(f=>f.nat==='Ashikaga'),aiArmy=G.armies.find(a=>a.nat==='Ashikaga');aiArmy.loc=ai.port;aiArmy.regs=1;aiArmy.path=[];declareWar('Ashikaga','Majapahit',{k:'nocb'});G.d=5;navyDay();if(!ai.cargo||!ai.landing)throw Error('AI did not embark for overseas invasion');return {embark:true,save:true,route:true,landing:true,capacity:true,sinking:true,landingBattle:true,ai:true};}""")
 print(result,flush=True);assert all(result.values()) and not errors,errors
 page.evaluate("newGame('Majapahit');beginGame();const f=G.fleets.find(f=>f.nat===G.nat),a=G.armies.find(a=>a.nat===G.nat);a.loc=f.port;a.regs=2;act.selfleet({dataset:{id:String(f.id)}});renderWin()")
 assert page.locator('[data-act=embark]').count()>0;page.screenshot(path='/tmp/nusantara-transport-panel.png');page.locator('[data-act=embark]').first.click();assert page.locator('[data-act=landarmy]').count()>0
 assert not errors,errors;b.close()
s.shutdown()
