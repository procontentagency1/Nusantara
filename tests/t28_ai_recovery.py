from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""() => {
 const reset=()=>{newGame('Majapahit');beginGame();G.al=[];G.ev=[];G.wars=[];G.battles=[];};
 reset();const a=G.armies.find(a=>a.nat==='Bali');const home=capOf('Bali').id;const camp=NATS.Majapahit.capital.id;a.loc=camp;a.path=[];a.prog=0;G.subj.Bali=G.nat;const w=declareWar(G.nat,'Sunda',{k:'nocb'});applyPeace(w,'att',{white:true});const alliedReturn=a.path.length>0&&a.returning&&access('Bali',camp);const p=G.armies.find(a=>a.nat===G.nat);const playerLoc=p.loc;aiArmies();const noPlayerMove=p.loc===playerLoc&&!p.returning;
 a.path=[];a.returning=false;a.bt=999999;aiArmies();const stale=!a.bt&&a.path.length>0;
 reset();const aa=G.armies.find(a=>a.nat==='Bali');G.subj={};G.tributaries={};G.acc=[];G.armies=[aa];aa.loc=camp;aa.path=[];aa.prog=0;const from=aa.loc;aiReturnHome(aa);const exiled=!!aa.exiled&&aa.loc===from&&aa.path.length>0;for(let i=0;i<240&&OWNR[aa.loc]!==aa.nat;i++){G.d=i%28+1;armiesDay();}armiesDay();const arrived=OWNR[aa.loc]===aa.nat&&!aa.exiled;
 reset();const ww=declareWar(G.nat,'Sunda',{k:'nocb'});const A=G.armies.find(a=>a.nat==='Bali'),B=G.armies.find(a=>a.nat==='Sunda');A.loc=camp;B.loc=camp;const bt=newBattle(camp,[A],[B],'A');applyPeace(ww,'att',{white:true});const unlocked=bt.done&&!A.bt&&!B.bt;
 reset();const wx=declareWar(G.nat,'Sunda',{k:'nocb'});const enemy=G.armies.find(a=>a.nat==='Sunda'),x=mkArmy('Bali',3,camp),y=mkArmy('Bali',3,camp);enemy.loc=camp;const live=newBattle(camp,[x,y],[enemy],'B');G.mo=0;const random=Math.random;Math.random=()=>1;aiMonth();Math.random=random;const notMerged=G.armies.includes(x)&&G.armies.includes(y)&&x.bt===live.id&&y.bt===live.id;
 reset();declareWar(G.nat,'Sunda',{k:'nocb'});const q1=mkArmy('Bali',20,camp),q2=mkArmy('Bali',20,camp);G.armies=[q1,q2];G.subjectData.Bali.extra=-1000;aiArmies();const spread=q1.path.length>0&&q2.path.length>0&&q1.path.at(-1)!==q2.path.at(-1);
 reset();declareWar(G.nat,'Sunda',{k:'nocb'});const small=mkArmy('Bali',2,camp);G.armies=[small];G.subjectData.Bali.extra=-1000;for(const id of OWNED.Sunda)mkArmy('Sunda',1000,id);aiArmies();const avoidSuicide=!small.path.length||!atWar(small.nat,OWNR[small.path.at(-1)]);
 return {avoidSuicide,spread,alliedReturn,noPlayerMove,stale,exiled,arrived,unlocked,notMerged};
 }""")
 print(result);assert all(result.values())
 simulation=page.evaluate("""() => {newGame('Majapahit');beginGame();paused=true;const start=performance.now();for(let i=0;i<365*2;i++){dayTick();G.ev=[];for(const n of Object.keys(G.subjectData))G.subjectData[n].pending=false;}return {year:G.y,armies:G.armies.length,stuck:G.armies.filter(a=>a.bt&&!G.battles.some(b=>b.id===a.bt&&!b.done)).length,invalid:G.armies.filter(a=>!PROV[a.loc]||!Number.isFinite(a.regs)).length,ms:Math.round(performance.now()-start)};}""")
 print(simulation);assert simulation['stuck']==0 and simulation['invalid']==0
 page.screenshot(path='/tmp/nusantara-ai-simulation.png')
 assert not errors,errors
 b.close()
s.shutdown()
