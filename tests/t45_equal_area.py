from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

fixture = json.loads(Path('tests/fixtures/mercator-v2-save.json').read_text())
s = ThreadingHTTPServer(('127.0.0.1', 0), SimpleHTTPRequestHandler)
Thread(target=s.serve_forever, daemon=True).start()
with sync_playwright() as p:
 b = p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
 page = b.new_page(viewport={'width': 780, 'height': 360}, is_mobile=True, has_touch=True)
 errors = []
 page.on('pageerror', lambda e: errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/' % s.server_port)
 page.wait_for_timeout(700)
 result = page.evaluate('''fixture => {
  const rad=Math.PI/180,scale=1600/(54*rad),top=46*rad;
  const oldY=lat=>scale*(Math.log(Math.tan(Math.PI/4+top/2))-Math.log(Math.tan(Math.PI/4+lat*rad/2)));
  const equalY=lat=>mercatorV2ToEqualArea(0,oldY(lat))[1];
  const area=(fn,lat)=>Math.abs(fn(lat+1)-fn(lat))/(Math.sin((lat+1)*rad)-Math.sin(lat*rad));
  const oldRatio=area(oldY,40)/area(oldY,0),newRatio=area(equalY,40)/area(equalY,0);
  G=fixture.save;fixSave();setWorld();const e=fixture.expected,f=G.fleets.find(x=>x.id===e.fleet);
  const xy=mercatorV2ToEqualArea(e.x,e.y);
  const checks={projection:DATA.mapVersion===4&&DATA.projection==='cylindrical-equal-area',oldDistorted:oldRatio>1.65,equalArea:Math.abs(newRatio-1)<1e-10,
   ids:fixture.provinceIds.every(p=>PROV[p[0]]?.n===p[1]&&PROV[p[0]]?.k===p[2]),version:G.mapVersion===4,position:Math.hypot(f.x-xy[0]-25*1600/54,f.y-xy[1])<20,cargo:f.cargo?.id===e.army,route:f.landing===e.target&&f.path.length>0,
   economy:G.treasury===e.treasury&&G.mana[1]===e.mana&&G.pv[1].p===e.production&&G.resourceOrders.length===e.orders,faith:G.pr[1]===e.rels,era:G.world.era===e.era};
  const n=G.fleets.length,x=f.x,y=f.y;fixSave();checks.idempotent=G.fleets.length===n&&f.x===x&&f.y===y;
  for(let i=0;i<2000&&f.cargo;i++){G.d=1;navyDay();}
  checks.arrival=!f.cargo&&G.armies.some(a=>a.id===e.army&&a.loc===e.target);
  return {checks,oldRatio,newRatio};
 }''', fixture)
 print(result, flush=True)
 assert all(result['checks'].values()), result
 assert not errors, errors
 page.evaluate("newGame('Majapahit');beginGame();zoomAt(vw/2,vh/2,0)")
 page.screenshot(path='/tmp/nusantara-equal-area-overview.png')
 b.close()
s.shutdown()
