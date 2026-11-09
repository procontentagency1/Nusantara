from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""()=>{
 const checks={};
 function reset(n='Majapahit'){newGame(n);beginGame();G.al=[];G.subj={};G.tributaries={};G.mana=[999,999,999];G.ev=[];}
 function conquer(claim=true){reset();const id=claimable('Sunda')[0];if(claim)G.claims=[id];const w=declareWar(G.nat,'Sunda',{k:claim?'claim':'nocb',goal:id});CTRL[id]=G.nat;w.bp=100;const preview=peaceExpansion(w,[id],G.nat),d=G.mana[1];applyPeace(w,'att',{provs:[id]});return {id,w,preview,d};}
 reset();checks.minors=Object.keys(NATS).filter(n=>OWNED[n].length===1&&n!==G.nat).every(n=>provCost(OWNED[n][0],G.nat)<=100);
 let {id,preview}=conquer();let x=G.expansion[id];checks.conquest=OWNR[id]===G.nat&&!hasCore(id,G.nat)&&overextension()===preview.oe&&x.coreLeft===0&&G.pv[id].nc>0;
 checks.truce=G.truce[pairKey(G.nat,'Sunda')]===monthIdx()+peaceTruce(preview.score);
 checks.claimDip=preview.dip===0;const discounted=coreCost(id);G.claims=[];checks.claimAdm=discounted<coreCost(id);G.claims=[id];
 x.sep=0;x.autonomy=75;x.cooldown=120;x.local=-10;for(let i=0;i<40;i++)conquestMonth();checks.noAutoCore=!hasCore(id,G.nat)&&x.coreLeft===0;
 const adm=G.mana[0],cost=coreCost(id);act.coreit({dataset:{id:String(id)}});act.coreit({dataset:{id:String(id)}});checks.coreDebit=G.mana[0]===adm-cost&&x.coreLeft===24;
 CTRL[id]='Sunda';conquestMonth();checks.occupationPauses=x.coreLeft===24;delete CTRL[id];for(let i=0;i<24;i++)conquestMonth();checks.coreFinished=hasCore(id,G.nat)&&overextension()===0&&G.pv[id].nc===0;
 const prestige=G.prestige;completeConquestCore(id);checks.rewardOnce=G.prestige===prestige;
 checks.output=provinceControl(id)>.2;x.cooldown=0;x.autonomy=35;const before=provinceControl(id);act.autonomy({dataset:{id:String(id),v:'up'}});const autonomy=x.autonomy;act.autonomy({dataset:{id:String(id),v:'down'}});checks.autonomy=provinceControl(id)<before&&x.local===-10&&x.autonomy===autonomy&&x.cooldown===120;
 ({id}=conquer(false));x=G.expansion[id];checks.unjustified=G.mana[1]===999-provDev(id)*2;
 reset();id=claimable('Sunda')[0];let w=declareWar(G.nat,'Sunda',{k:'nocb'});CTRL[id]=G.nat;G.mana[1]=0;checks.noDip=applyPeace(w,'att',{provs:[id]})===false&&G.wars.includes(w)&&OWNR[id]==='Sunda';
 ({id}=conquer());x=G.expansion[id];G.armies=G.armies.filter(a=>a.loc!==id);x.resistance=99.9;conquestMonth();checks.uprising=x.revolt===6&&provinceControl(id)===0&&resourceYield(id)===0;
 const g=mkArmy(G.nat,revoltNeed(id),id);g.morale=1;for(let i=0;i<4;i++)conquestMonth();checks.garrison=!x.revolt&&x.resistance===0;
 x.resistance=99.9;x.sep=360;conquestMonth();G.armies=G.armies.filter(a=>a!==g);for(let i=0;i<6;i++)conquestMonth();checks.secession=OWNR[id]==='Sunda'&&!G.pv[id];
 ({id}=conquer());x=G.expansion[id];x.resistance=99.9;conquestMonth();act.autonomy({dataset:{id:String(id),v:'up'}});checks.negotiate=!x.revolt&&x.autonomy>=75&&provinceControl(id)>0;
 x.resistance=70;G.mana[2]=100;act.harshconquest({dataset:{id:String(id)}});act.harshconquest({dataset:{id:String(id)}});checks.harsh=x.resistance===40&&G.mana[2]===70;
 G.pv[id].p+=3;G.pv[id].bld.push('pasar');const dev=provDev(id);transferProv(id,'Sunda',true);rebuildOwned();transferProv(id,G.nat,true);rebuildOwned();checks.buildings=G.pv[id].bld.includes('pasar')&&provDev(id)===dev;
 checks.dynamicCore=hasCore(id,G.nat);transferProv(id,'Sunda',true);rebuildOwned();checks.reconquest=availableCBs('Sunda').some(c=>c.k==='core'&&c.ids.includes(id));
 reset();id=claimable('Sunda')[0];transferProv(id,'Bali');rebuildOwned();const ax=G.expansion[id];conquestMonth();checks.aiCore=ax.coreLeft===35;ax.revolt=6;ax.resistance=100;const aa=G.armies.find(a=>a.nat==='Bali');aa.loc=id;aa.path=[];checks.aiResponse=aiSuppressConquest(aa)&&!aa.drilling;
 reset();id=claimable('Sunda')[0];transferProv(id,G.nat);rebuildOwned();delete G.expansion;delete G.cores;G.pv[id].nc=10;fixExpansion();checks.migration=G.expansion[id].coreLeft===10;saveGame(true);const save=JSON.parse(localStorage.getItem(SAVE_KEY));checks.saved=!!save.expansion[id]&&!!save.cores[id];
 winMode='expansion';renderWin();checks.ui=document.querySelector('#win').innerText.includes('Overextension');
 reset();const bali=[...OWNED.Bali];G.claims=bali;w=declareWar(G.nat,'Bali',{k:'claim',goal:bali[0]});for(const pid of bali)CTRL[pid]=G.nat;const forecast=peaceExpansion(w,bali,G.nat);applyPeace(w,'att',{provs:bali});
 checks.annexation=!alive('Bali')&&!G.armies.some(a=>a.nat==='Bali')&&!G.subj.Bali;
 checks.fullAnnexTruce=G.truce[pairKey('Bali',G.nat)]===monthIdx()+peaceTruce(forecast.score);
 act.releaseconquest({dataset:{n:'Bali'}});const offer=G.ev.find(e=>e.t==='Pulihkan Bali?');checks.releaseConfirm=!!offer&&OWNR[bali[0]]===G.nat;
 if(offer){EVA.releaseConquest(offer.o[1][2]);const regs=regsOf('Bali');EVA.releaseConquest(offer.o[1][2]);checks.release=alive('Bali')&&G.subj.Bali===G.nat&&overextension()===0&&regsOf('Bali')===regs;}
 G.ev=[];showEvent();winMode='expansion';renderWin();return checks;
 }""")
 print(result);assert all(result.values()),result
 page.wait_for_timeout(5000)
 page.screenshot(path='/tmp/nusantara-expansion.png')
 # Peace preview uses the same figures as the actual settlement.
 page.evaluate("""()=>{newGame('Majapahit');beginGame();G.al=[];G.subj={};G.tributaries={};G.mana=[999,999,999];const id=claimable('Sunda')[0];G.claims=[id];const w=declareWar(G.nat,'Sunda',{k:'claim',goal:id});CTRL[id]=G.nat;w.bp=100;PD={w:w.id,sel:new Set([id]),gold:0,vas:false};winMode='peace';renderWin();}""")
 page.wait_for_timeout(5000)
 page.screenshot(path='/tmp/nusantara-peace-expansion.png')
 page.locator('#win').evaluate('(el)=>el.scrollTop=el.scrollHeight')
 page.screenshot(path='/tmp/nusantara-peace-expansion-bottom.png')
 assert not errors,errors
 b.close()
s.shutdown()
