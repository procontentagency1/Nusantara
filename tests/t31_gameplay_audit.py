from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""()=>{
 newGame('Majapahit');beginGame();G.rs='islam';fixSave();newGame('Majapahit');const religion=G.rs==='siwa';
 G.treasury=10000;const id=+Object.keys(G.pv)[0],cost=bCost(BUILD.pasar);act.build({dataset:{id:String(id),k:'pasar'}});act.build({dataset:{id:String(id),k:'pasar'}});const building=G.pv[id].cons.length===1&&G.treasury===10000-cost;
 G.ev=[];pushEvent({t:'Audit',x:'Test',o:[['Done','ok',{}]]});const uid=String(G.ev[0].uid);paused=true;act.spd({dataset:{s:'5'}});const modalPause=paused;act.ev({dataset:{event:uid,i:'0'}});act.ev({dataset:{event:uid,i:'0'}});const eventSafe=G.ev.length===0;
 G.al=[];G.subj={};G.tributaries={};const w=declareWar(G.nat,'Sunda',{k:'nocb'});const target=OWNED.Sunda[0];w.goals=[target];const occupation=!demandable(w,target,G.nat);CTRL[target]=G.nat;const occupied=demandable(w,target,G.nat);const surrender=aiAccept(w,'att',100,100);applyPeace(w,'att',{gold:20});const cash=G.treasury;applyPeace(w,'att',{gold:20});const once=G.treasury===cash;
 G.mana=[999,999,999];EF.mana(0,25);const mana=G.mana[0]===999;
 let kingdoms=true;for(const n of Object.keys(NATS)){newGame(n);const e=econ();if(!Number.isFinite(e.net)||!capOf(n)||new Set(activeMissions().map(m=>m.id)).size!==activeMissions().length)kingdoms=false;}
 newGame('Majapahit');beginGame();for(let i=0;i<365*12;i++){dayTick();let guard=0;while(G.ev.length&&guard++<20){showEvent();const ev=G.ev[0];act.ev({dataset:{event:String(ev.uid),i:'0'}});}}
 const sane=Number.isFinite(G.treasury)&&G.mana.every(v=>Number.isFinite(v)&&v>=0&&v<=999)&&G.armies.every(a=>PROV[a.loc]&&a.regs>=0)&&G.wars.every(w=>!w.att.some(n=>w.def.includes(n)));
 return {religion,building,modalPause,eventSafe,occupation,occupied,surrender,once,mana,kingdoms,sane,year:G.y};
 }""")
 print(result);assert all(v for k,v in result.items() if k!='year')
 page.screenshot(path='/tmp/nusantara-audit.png')
 assert not errors,errors
 b.close()
s.shutdown()
