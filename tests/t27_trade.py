from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""() => {
 newGame('Majapahit');beginGame();paused=true;
 const snap=tradeSnapshot(),values=Object.values(snap.nodes);const conservation=Math.abs(values.reduce((s,n)=>s+n.local+n.bonus-n.collected-n.retained,0))<1e-8;
 const home=G.trade.home,base=snap.income;const automatic=home==='jawa'&&base>0;
 const treasury=G.treasury;econ();econ();const pure=G.treasury===treasury;const e=econ();const budget=Math.abs(e.net-(e.tax+e.prod+e.trade+e.vassalIncome-e.subjectTax-e.armyCost-e.misCost-e.interest))<1e-8;
 act.merchant({dataset:{node:home,mode:'collect'}});const travel=G.trade.merchants[0].left===30&&tradeSnapshot().income===base;for(let i=0;i<30;i++)tradeDay();const bonus=tradeSnapshot().income>base;
 act.merchant({dataset:{node:'malaka',mode:'collect'}});G.trade.merchants.find(m=>m.node==='malaka').left=0;const off=tradeSnapshot().nodes.malaka;const penalty=Math.abs(off.powers[G.nat]-((off.raw[G.nat]||0)+2)*.5)<1e-8;
 act.merchant({dataset:{node:'borneo',mode:'steer',to:'jawa'}});const cap=G.trade.merchants.length===2&&!G.trade.merchants.some(m=>m.node==='borneo');act.merchant({dataset:{node:'malaka',mode:'recall'}});act.merchant({dataset:{node:'borneo',mode:'steer',to:'jawa'}});G.trade.merchants.find(m=>m.node==='borneo').left=0;const steering=tradeSnapshot().nodes.borneo.bonus>0;
 const pv=Object.keys(G.pv).find(id=>!G.pv[id].bld.includes('pasar'));const node=tradeNode(PROV[pv]),before=tradeSnapshot().nodes[node].raw[G.nat];G.pv[pv].bld.push('pasar');const market=tradeSnapshot().nodes[node].raw[G.nat]>before;CTRL[pv]='Sunda';const occupied=tradeSnapshot().nodes[node].raw[G.nat]<before;delete CTRL[pv];
 saveGame(true);const saved=JSON.parse(localStorage.getItem(SAVE_KEY)).trade.merchants.length===2;delete G.trade;fixSave();const migration=G.trade.home==='jawa'&&G.trade.merchants.length===0;
 const start=G.treasury,expected=econ().net,random=Math.random;Math.random=()=>1;monthTick();Math.random=random;const paid=Math.abs(G.treasury-start-expected)<1e-6;
 winMode='trade';renderWin();return {nodes:TRADE_NODES.length,conservation,automatic,pure,budget,travel,bonus,penalty,cap,steering,market,occupied,saved,migration,paid};
 }""")
 print(result);assert result['nodes']==7 and all(v for k,v in result.items() if k!='nodes')
 page.screenshot(path='/tmp/nusantara-trade.png')
 assert not errors,errors
 b.close()
s.shutdown()
