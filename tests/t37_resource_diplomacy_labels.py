from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1000)
 result=page.evaluate("""()=>{
 const out={};function reset(){newGame('Majapahit');beginGame();G.al=[];G.subj={};G.tributaries={};G.treasury=1000;G.rel[pairKey(G.nat,'Bali')]=50;G.resourceStocks.Bali.wood=100;G.resourceStocks[G.nat].wood=50;G.resourceTradeGold.Bali=1000;}
 reset();const p=PROV[OWNED[G.nat][0]];setMode('religion');buildCountryLabels();out.largeLabels=COUNTRY_LABELS.every(l=>Object.values(RELS).some(r=>r.n.toUpperCase()===l.name));out.smallLabel=mapProvinceLabel(p)===RELS[G.pr[p.id]].n;
 setMode('pol');buildCountryLabels();out.political=COUNTRY_LABELS.some(l=>l.name==='MAJAPAHIT');setMode('resources');out.resourceLabel=mapProvinceLabel(p)===(RESOURCE_NAMES[provinceResource(p)]||goodsOf(p));setMode('trade');out.tradeLabel=mapProvinceLabel(p)===TRADE_BY_ID[tradeNode(p)].n;
 setMode('religion');const proto=CanvasRenderingContext2D.prototype,raw=proto.fillText,seen=[];proto.fillText=function(t,...args){if(this.canvas===detail.c)seen.push(t);return raw.call(this,t,...args);};try{renderDetail();}finally{proto.fillText=raw;}out.drawnFaith=seen.some(t=>/SIWA|Siwa|HINDU|Hindu/.test(t))&&!seen.includes('MAJAPAHIT');
 G.pr[p.id]='islam';frame();out.conversionLabel=mapProvinceLabel(p)==='Islam Sunni'&&polFill(p)==='#548d65';setMode('pol');
 let q=resourceQuote('Bali','wood','buy',10);out.quote=!q.reason;const gold=G.treasury,wood=G.resourceStocks[G.nat].wood,ai=G.resourceStocks.Bali.wood,fund=G.resourceTradeGold.Bali;bookResourceTrade(q);out.escrow=G.treasury===gold-q.total&&G.resourceStocks[G.nat].wood===wood&&G.resourceStocks.Bali.wood===ai-10&&G.resourceTradeGold.Bali===fund;
 const order=G.resourceOrders[0];for(let i=0;i<q.days;i++)resourceTradeDay();out.delivered=G.resourceOrders.length===0&&G.resourceStocks[G.nat].wood===wood+10&&G.resourceTradeGold.Bali===fund+q.value;const once=G.treasury;settleResourceTrade(order.id);out.once=G.treasury===once;
 q=resourceQuote('Bali','wood','sell',10);const net=G.treasury,aiBefore=G.resourceStocks.Bali.wood,budget=G.resourceTradeGold.Bali;bookResourceTrade(q);out.sellFund=G.resourceTradeGold.Bali===budget-q.value&&G.treasury===net;for(let i=0;i<q.days;i++)resourceTradeDay();out.sold=G.treasury===net+q.total&&G.resourceStocks.Bali.wood===aiBefore+10;
 reset();q=resourceQuote('Bali','wood','buy',10);const money=G.treasury,stock=G.resourceStocks.Bali.wood;bookResourceTrade(q);const id=G.resourceOrders[0].id;settleResourceTrade(id,true);settleResourceTrade(id,true);out.cancel=G.treasury===money&&G.resourceStocks.Bali.wood===stock&&G.resourceOrders.length===0;
 q=resourceQuote('Bali','wood','buy',10);bookResourceTrade(q);declareWar(G.nat,'Bali',{k:'nocb'});resourceTradeDay();out.war=G.treasury===money&&G.resourceOrders.length===0&&!!resourceQuote('Bali','wood','buy',10).reason;
 reset();G.resourceStocks.Bali.wood=1;out.shortage=!!resourceQuote('Bali','wood','buy',10).reason;G.resourceStocks.Bali.wood=100;G.resourceStocks[G.nat].wood=495;out.full=!!resourceQuote('Bali','wood','buy',10).reason;
 G.resourceStocks[G.nat].wood=480;q=resourceQuote('Bali','wood','buy',20);bookResourceTrade(q);out.storage=resourceCapacity(G.nat,'wood')===480;resourcesMonth();out.productionCap=G.resourceStocks[G.nat].wood<=480;for(let i=0;i<q.days;i++)resourceTradeDay();out.noOverflow=G.resourceStocks[G.nat].wood<=500;
 reset();const ask=resourceQuote('Bali','wood','buy',10),bid=resourceQuote('Bali','wood','sell',10);out.spread=ask.total>bid.total;G.rel[pairKey(G.nat,'Bali')]=150;G.al=[pairKey(G.nat,'Bali')];out.friendly=resourceQuote('Bali','wood','buy',10).total<ask.total;G.resourceStocks.Bali.wood=20;out.scarcity=resourceQuote('Bali','wood','buy',10).total>ask.total;
 reset();q=resourceQuote('Bali','wood','buy',5);G.resourceStocks.Bali.wood=10;out.stale=bookResourceTrade(q)===false&&G.resourceOrders.length===0;
 reset();for(let i=0;i<3;i++)bookResourceTrade(resourceQuote('Bali','wood','buy',5));out.limit=G.resourceOrders.length===3&&!!resourceQuote('Bali','wood','buy',5).reason;
 saveGame(true);const sv=JSON.parse(localStorage.getItem(SAVE_KEY));out.saved=sv.resourceOrders.length===3;delete G.resourceTradeGold;fixResourceTrade();out.migration=G.resourceTradeGold.Bali>0&&G.resourceOrders.length===3;
 reset();for(let i=0;i<5;i++){q=resourceQuote('Bali','wood','buy',5);if(q.reason)throw Error(q.reason);bookResourceTrade(q);for(let j=0;j<q.days;j++)resourceTradeDay();}out.goodwill=G.resourceGoodwill.Bali.points===6;
 reset();G.resourceStocks.Bali.wood=100;G.mo=6;G.resourceStocks[G.nat].food=0;resourceTradeMonth();out.aiOffer=G.ev.some(e=>e.t.startsWith('Tawaran Pasokan'));
 G.ev=[];showEvent();RESOURCE_PARTNER='Bali';RESOURCE_QUANTITY=10;winMode='resourceTrade';renderWin();out.ui=document.querySelector('#win').innerText.toLowerCase().includes('mitra: bali')&&document.querySelector('#win').innerText.toLowerCase().includes('bukan ton atau jumlah kapal');return out;
 }""")
 print(result,flush=True);assert all(result.values()),result
 page.wait_for_timeout(6000);page.screenshot(path='/tmp/nusantara-resource-diplomacy.png')
 # Actual UI order with fresh quote and persisted delivery.
 page.locator('#win button[data-act=resourceorder][data-k=wood][data-kind=buy]').scroll_into_view_if_needed()
 page.screenshot(path='/tmp/nusantara-resource-quote.png')
 page.locator('#win button[data-act=resourceorder][data-k=wood][data-kind=buy]').click()
 assert page.evaluate('G.resourceOrders.length')==1
 assert page.locator('#win button[data-act=resourcecancel]').count()==1
 page.evaluate('for(let i=0;i<60&&G.resourceOrders.length;i++)resourceTradeDay()')
 assert page.locator('#win button[data-act=resourcecancel]').count()==0
 page.evaluate("winMode=null;renderWin();setMode('religion');const p=capOf(G.nat);centerOn(p.lab[0],p.lab[1],fitS*2.8);renderDetail()")
 page.wait_for_timeout(600);page.screenshot(path='/tmp/nusantara-faith-labels.png')
 assert not errors,errors
 b.close()
s.shutdown()
