from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""() => {
newGame('Majapahit');beginGame();G.al=[];G.subj={};const target='Sunda';const id=claimable(target)[0];if(id==null)throw Error('no neighbor');G.net[target]=100;G.mana[1]=0;act.dact({dataset:{k:'claim',n:target,id:String(id)}});const instant=G.claims.includes(id)&&G.mana[1]===0;
act.dact({dataset:{k:'war',n:target}});const preview=G.wars.length===0&&winMode==='declare'&&WAR_DRAFT.kind==='claim';const stab=G.stab;act.back();const cancel=G.wars.length===0&&G.stab===stab;openDeclaration(target);act.warconfirm();const w=G.wars[0];const cb=w.cb.k==='claim'&&w.goal===id&&G.stab===stab;CTRL[id]=G.nat;war2Month();const tick=w.goalScore>0;
G.armies=[];G.battles=[];const edge=LINK[id].find(l=>PROV[l.to].k==='L');const a=mkArmy(G.nat,4,edge.to),b=mkArmy(target,4,id);a.path=[id];b.path=[edge.to];a.prog=stepDays(a.loc,id)*.5;b.prog=stepDays(b.loc,edge.to)*.5;armiesDay();const crossing=!!a.bt&&a.bt===b.bt;
let effects=0;for(const e of EXTRA_EVENTS)for(let i=0;i<2;i++){newGame('Majapahit');beginGame();const before=JSON.stringify(G);EVT['tamb_'+e[0]].o[i].fx();if(before===JSON.stringify(G))throw Error('no effect '+e[0]);if(!Number.isFinite(G.treasury))throw Error('nan');effects++;}
newGame('Majapahit');beginGame();G.al=[];G.subj={};G.claims=[id];openDeclaration(target);G.claims=[];act.warconfirm();const stale=G.wars.length===0;openDeclaration(target);const st=G.stab;act.warconfirm();const nocb=G.stab===Math.max(-3,st-2)&&G.wars[0].cb.k==='nocb';newGame('Majapahit');beginGame();G.al=[];G.subj={};declareWar(G.nat,target,{k:'nocb'});G.armies=[];G.battles=[];const aa=mkArmy(G.nat,4,id),bb=mkArmy(target,4,id);aa.path=[edge.to];bb.path=[edge.to];armiesDay();const colocated=!!aa.bt&&aa.bt===bb.bt;newGame('Majapahit');beginGame();G.al=[];G.subj={};G.claims=[id];openDeclaration(target);renderWin();return {instant,preview,cancel,cb,tick,crossing,effects,stale,nocb,colocated};
}""")
 print(result);assert all(result[k] for k in ['instant','preview','cancel','cb','tick','crossing','stale','nocb','colocated']) and result['effects']==48
 page.wait_for_timeout(4000)
 page.screenshot(path='/tmp/nusantara-war-preview.png')
 assert not errors,errors
 b.close()
s.shutdown()
