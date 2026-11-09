from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""()=>{newGame('Majapahit');beginGame();const a=myArmies()[0];const normal=econ().armyCost;act.maintenance({dataset:{v:'0'}});const saving=econ().armyCost<normal;const moraleCap=a.morale<=.5;act.maintenance({dataset:{v:'1'}});act.drill({dataset:{id:String(a.id)}});militaryMonth();const trained=a.drill===2&&G.professionalism[G.nat]>0&&a.morale<=.5;const costly=econ().armyCost>normal;act.drill({dataset:{id:String(a.id)}});militaryMonth();const recovering=a.morale>.5;const power=armyQuality(a);a.drill=100;const quality=armyQuality(a)>power;const before=a.regs;a.morale=.3;act.asplit({dataset:{id:String(a.id)}});const split=myArmies().filter(x=>x.loc===a.loc).every(x=>x.morale===.3);act.amerge({dataset:{id:String(a.id)}});const merge=a.regs===before&&Math.abs(a.morale-.3)<.001;saveGame(true);const saved=JSON.parse(localStorage.getItem(SAVE_KEY)).maintenance===1;winMode='mil';renderWin();return {saving,moraleCap,trained,costly,recovering,quality,split,merge,saved,width:armyCombatWidth(G.nat)};}""")
 print(result);assert all(v for k,v in result.items() if k!='width')
 page.screenshot(path='/tmp/nusantara-military.png')
 combat=page.evaluate('''()=>{
 const a=myArmies()[0],enemy=G.armies.find(x=>x.nat!==G.nat),loc=a.loc;
 a.morale=.3;const entry=sideStats([a],loc,false).mor===.3;
 const random=Math.random;Math.random=()=>.5;
 function damage(regs){const A=sideStats([{...a,regs,morale:1}],loc,false),B=sideStats([{...enemy,regs:30,morale:1}],loc,true);const bt={id:-1,loc,day:0,A,B,h:[]};stepBattle(bt);return B.men0-B.men;}
 let width;try{const w=armyCombatWidth(a.nat);width=Math.abs(damage(w)-damage(w*2))<.001;}finally{Math.random=random;}
 delete G.maintenance;delete G.professionalism;delete a.morale;delete a.drill;fixMilitary();
 const migration=G.maintenance===1&&a.morale===1&&a.drill===0&&G.professionalism[G.nat]===0;
 CTRL[loc]=enemy.nat;act.drill({dataset:{id:String(a.id)}});const occupied=!a.drilling;delete CTRL[loc];
 return {entry,width,migration,occupied};}''')
 print('combat and migration',combat);assert all(combat.values())
 page.locator('#rail button[data-w=menu]').click()
 page.evaluate("SFX.setMus(false)")
 page.wait_for_timeout(150)
 audio=page.evaluate("""()=>{const peaks=[];const proto=AudioParam.prototype,old=proto.exponentialRampToValueAtTime;proto.exponentialRampToValueAtTime=function(v,t){peaks.push(v);return old.call(this,v,t);};SFX.play('tap');proto.exponentialRampToValueAtTime=old;return peaks;}""")
 print('tap gain envelope',audio);assert audio and max(audio)<=.03
 assert not errors,errors
 b.close()
s.shutdown()
