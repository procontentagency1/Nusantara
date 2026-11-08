from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""() => {
const reset=(nat='Majapahit')=>{newGame(nat);beginGame();G.subj={};G.tributaries={};G.subjectData={};G.al=[];G.ev=[];G.wars=[];};
reset();setSubject('Bali',G.nat,'vassal',120);setSubject('Samudra',G.nat,'tributary',120);G.rel[pairKey('Bali',G.nat)]=200;G.rel[pairKey('Samudra',G.nat)]=200;
const distinct=subjectsOf(G.nat).includes('Bali')&&!subjectsOf(G.nat).includes('Samudra');const income=econ().vassalIncome>0;G.subjectData.Bali.extra=100;const refusal=econ().vassalIncome===0;G.prestige=50;const before=libertyDesire('Bali');act.subjectact({dataset:{n:'Bali',k:'placate'}});const placate=G.prestige===30 && G.subjectData.Bali.extra===90;G.subjectData.Bali.extra=-30;
const w=declareWar(G.nat,'Sunda',{k:'nocb'});const joined=w.att.includes('Bali')&&!w.att.includes('Samudra');G.wars=[];G.subjectData.Bali.scutage=true;const w2=declareWar(G.nat,'Sunda',{k:'nocb'});const scutage=!w2.att.includes('Bali');G.wars=[];
G.y++;const money=G.treasury;sendTribute('Samudra',true);const amount=tributeAmount('Samudra');sendTribute('Samudra',true);const annual=Math.abs(G.treasury-money-amount)<.001;G.y++;sendTribute('Samudra',false);const trust=G.subjectData.Samudra.trust===36;
G.subjectData.Bali.since=monthIdx()-120;G.subjectData.Bali.extra=-100;G.rel[pairKey('Bali',G.nat)]=200;const free=dipFree();act.subjectact({dataset:{n:'Bali',k:'integrate'}});const reserved=dipFree()===free-1;const dip=G.mana[1];subjectsMonth();const progress=G.subjectData.Bali.integration.spent===3&&G.mana[1]===dip-3;G.rel[pairKey('Bali',G.nat)]=100;subjectsMonth();const pause=G.subjectData.Bali.integration.spent===3;G.rel[pairKey('Bali',G.nat)]=200;G.subjectData.Bali.integration.spent=Math.ceil(natDev('Bali')*8)-1;subjectsMonth();const integrated=!alive('Bali')&&!G.subj.Bali;
reset('Sunda');setSubject('Sunda','Majapahit','tributary',120);G.subjectData.Sunda.tribute='dip';G.y++;G.mana[1]=100;const power=tributeAmount('Sunda');sendTribute('Sunda',true);const debit=G.mana[1]===100-power;
reset('Sunda');setSubject('Sunda','Majapahit','vassal',120);G.subjectData.Sunda.extra=100;EVA.subjectexit({n:'Sunda',o:'Majapahit'});const iw=G.wars[0];const independence=!!iw.independence&&!G.subj.Sunda;applyPeace(iw,'def',{white:true});const restored=G.subj.Sunda==='Majapahit';
reset();setSubject('Sunda','Majapahit','tributary',120);const pw=declareWar('Samudra','Sunda',{k:'nocb'});const call=G.ev.some(e=>e.t==='Lindungi Negara Upeti');EVA.tribdef({w:pw.id,n:'Sunda',yes:true});const protect=pw.def.includes(G.nat);saveGame(true);const sv=JSON.parse(localStorage.getItem(SAVE_KEY));const saved=sv.tributaries.Sunda==='Majapahit';delete G.subjectData;fixSave();const migrate=!!G.subjectData.Sunda;
return {distinct,income,refusal,placate,joined,scutage,annual,trust,reserved,progress,pause,integrated,debit,independence,restored,call,protect,saved,migrate};
}""")
 print(result);assert all(result.values())
 page.evaluate("G.ev=[];showEvent();G.wars=[];winMode='dipn';winProv='Sunda';renderWin()")
 page.screenshot(path='/tmp/nusantara-subjects.png')
 assert not errors,errors
 b.close()
s.shutdown()
