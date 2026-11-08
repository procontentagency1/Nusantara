from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""() => { const ids=Object.keys(EVT).filter(id=>EVT[id].historical); let tested=0; const years={sej_bubat:1357,sej_dewan:1357,sej_mada:1364,sej_prapanca:1365,sej_palembang:1377,sej_suksesi:1389,sej_paregreg:1405,sej_zheng:1410}; for (const id of ids) for(let i=0;i<EVT[id].o.length;i++) {newGame('Majapahit');beginGame();G.y=years[id];G.tech[0]=4;G.legit=50;G.subj.Palembang=G.nat;setFlag('bubat_sengketa',-1);if(!fireEvent(id))throw Error(id+' condition');if(!paused)throw Error('not paused');if(fireEvent(id))throw Error('repeated');const e=G.ev.shift();EVA[e.o[i][1]](e.o[i][2]);if(!Number.isFinite(G.treasury)||G.stab < -3||G.stab>3)throw Error('invalid effects');tested++;} newGame('Sunda');G.y=1357;const foreignBlocked=!fireEvent('sej_bubat');newGame('Majapahit');const dateBlocked=!fireEvent('sej_mada');G.y=1357;fireEvent('sej_bubat');G.ev.shift();gevPick({id:'sej_bubat',i:1});const queued=G.evq.some(q=>q.id==='sej_dewan');G.mo=1;evMonth();const chain=G.fired.includes('sej_dewan');saveGame(true);const saved=JSON.parse(localStorage.getItem(SAVE_KEY)).fired.includes('sej_dewan');return {count:ids.length,tested,foreignBlocked,dateBlocked,queued,chain,saved}; }""")
 print(result);assert result['count']==8 and result['tested']==16 and all(result[k] for k in ['foreignBlocked','dateBlocked','queued','chain','saved'])
 page.evaluate("G.ev=[];G.fired=[];G.y=1357;fireEvent('sej_bubat')")
 page.screenshot(path='/tmp/nusantara-event.png')
 assert not errors,errors
 b.close()
s.shutdown()
