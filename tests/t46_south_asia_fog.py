from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
fixture=json.loads(Path('tests/fixtures/equal-area-v3-save.json').read_text())
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2,is_mobile=True,has_touch=True);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1000)
 checks=page.evaluate('''fixture=>{
  G=fixture.save;fixSave();setWorld();const e=fixture.expected,f=G.fleets.find(x=>x.id===e.fleet),shift=25*1600/54;
  const out={version:G.mapVersion===4,ids:fixture.provinceIds.every(p=>PROV[p[0]]?.n===p[1]),cargo:f.cargo?.id===e.army,position:Math.hypot(f.x-e.x-shift,f.y-e.y)<20,route:f.landing===e.target&&f.path.length>0,knownOld:!!G.explored[byName('Bali').id],newHidden:!G.explored[byName('Delhi').id],states:SOUTH_NATIONS.every(n=>NATS[n]&&alive(n)&&G.armies.some(a=>a.nat===n))};
  const count=G.armies.length,ships=G.fleets.length;fixSave();out.idempotent=G.armies.length===count&&G.fleets.length===ships;
  for(let i=0;i<2000&&f.cargo;i++){G.d=1;navyDay();}out.arrival=!f.cargo&&G.armies.some(a=>a.id===e.army&&a.loc===e.target);
  newGame('Komunitas Taiwan');beginGame();const home=NATS[G.nat].capital,far=byName('Bali');out.fogHome=explored(home.id);out.fogFar=!explored(far.id)&&!knownNation('Bali')&&!!resourceRoute('Bali').reason;
  const sea=SEA_PROVS.find(p=>!explored(p.id)&&navalPath(G.fleets.find(f=>f.nat===G.nat).x,G.fleets.find(f=>f.nat===G.nat).y,p.id)?.length);
  const boat=G.fleets.find(f=>f.nat===G.nat);out.destination=!!sea&&orderFleet(boat,sea.id);for(let i=0;i<3000&&boat.path.length&&!explored(sea.id);i++){G.d=1;navyDay();revealExploration();}out.discovery=explored(sea.id);saveGame(true);G=JSON.parse(localStorage.getItem(SAVE_KEY));fixSave();out.saved=explored(sea.id);
  newGame('Vijayanagara');beginGame();out.india=NATS.Vijayanagara.playable&&capOf(G.nat).n==='Vijayanagara'&&activeMissions().some(m=>m.id==='east_Vijayanagara_m0')&&EVT.east_Vijayanagara_dewan.cond()&&tradeNode(capOf(G.nat))==='bengal';out.temple=cityStyle(G.nat)==='india_south';return out;
 }''',fixture)
 print(checks,flush=True);assert all(checks.values()),checks;assert not errors,errors
 page.evaluate("newGame('Komunitas Taiwan');beginGame();winMode=null;renderWin();cancelAnimationFrame(anim);zoomAt(vw/2,vh/2,0);request()")
 page.wait_for_timeout(800);page.screenshot(path='/tmp/nusantara-south-fog-mobile.png')
 page.locator('#mapViewToggle').tap();assert 'Kabut menutupi' in page.locator('#mapViewMenu').inner_text();page.locator('[data-mapregion=india]').tap();assert page.locator('#mapViewMenu').is_hidden()
 page.evaluate("showStart()");page.wait_for_timeout(400);page.locator('#stPanelToggle').tap();point=page.evaluate("()=>{cancelAnimationFrame(anim);const p=byName('Vijayanagara');centerOn(p.lab[0],p.lab[1],2);const x=view.tx+p.lab[0]*view.s,y=view.ty+p.lab[1]*view.s;return rot?[innerWidth-y,x]:[x,y];}");page.wait_for_timeout(200);page.touchscreen.tap(*point);assert page.evaluate("selNat==='Vijayanagara'");page.locator('#btnStart').tap();assert page.evaluate("G.nat==='Vijayanagara'");assert not errors,errors;b.close()
s.shutdown()
