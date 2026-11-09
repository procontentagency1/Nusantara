from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1000)
 out=page.evaluate("""()=>{const results=[];for(const n of ['Majapahit','Samudra','Yuan','Goryeo','Ashikaga','Komunitas Ainu']){newGame(n);beginGame();for(let i=0;i<24;i++){G.y=1350+Math.floor(i/12);G.mo=i%12;monthTick();for(let guard=0;G.ev.length&&guard<5;guard++){showEvent();const e=G.ev[0];act.ev({dataset:{event:String(e.uid),i:'0'}});}}saveGame(true);const save=JSON.parse(localStorage.getItem(SAVE_KEY));G=save;fixSave();setWorld();const e=econ();results.push({nation:n,correct:G.nat===n,finite:Number.isFinite(e.net)&&G.mana.every(Number.isFinite)&&Number.isFinite(G.mp),world:!!G.world&&!!G.world.ai.Sunda,age:!!worldAge()?.name,faith:G.world.faith[n]===G.rs,stored:!!JSON.parse(localStorage.getItem(SAVE_KEY)).world});}return results;}""")
 print(out,flush=True);assert all(all(v for k,v in x.items() if k!='nation') for x in out) and not errors,errors
 b.close()
s.shutdown();print('PASS six campaigns for two years with save/load')
