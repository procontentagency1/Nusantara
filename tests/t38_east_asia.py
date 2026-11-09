from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 fixture=json.loads(Path('tests/fixtures/legacy-east-save.json').read_text())
 migration=page.evaluate("""f=>{G=f.save;fixSave();beginGame();const fleet=G.fleets.find(x=>x.id===f.expected.fleet),tr=DATA.legacyTransform;const once=G.armies.length;fixSave();return {version:G.mapVersion===2,ids:f.oldProvinces.every(p=>PROV[p.id]?.n===p.n&&PROV[p.id]?.k===p.k),money:G.treasury===f.expected.treasury,mana:G.mana[1]===f.expected.mana,pv:G.pv[1].p===f.expected.production&&G.pv[1].bld.includes('pasar'),claim:G.claims.includes(88),ownership:OWNR[93]===G.nat,newLand:OWNR[NATS.Yuan.capital.id]==='Yuan',newArmy:armiesOf('Yuan').length>0&&armiesOf('Goryeo').length>0,noDuplicate:G.armies.length===once,ships:G.fleets.some(f=>f.nat==='Yuan'),boatCoordinates:Math.hypot(fleet.x-f.expected.x*tr.scale,fleet.y-(f.expected.y*tr.scale+tr.offsetY))<20,cargo:G.resourceOrders.length===f.expected.orders,uniqueIds:new Set([...G.armies,...G.fleets].map(x=>x.id)).size===G.armies.length+G.fleets.length};}""",fixture)
 print('migration',migration,flush=True);assert all(migration.values()),migration
 result=page.evaluate("""()=>{const r={};let nations=true,missions=true,faith=true,styles=true,finite=true,traditions=true;
 for(const n of Object.keys(EAST_PROFILE)){newGame(n);const e=econ();nations&&=NATS[n].playable&&!!capOf(n);missions&&=activeMissions().length===12&&new Set(activeMissions().map(m=>m.id)).size===12;faith&&=!!RELS[G.rs]&&Object.values(G.pr).every(k=>!!RELS[k]);styles&&=cityStyle(n)===EAST_PROFILE[n].region&&regionalStyle(n)===EAST_PROFILE[n].region;finite&&=Number.isFinite(e.net);traditions&&=G.mod.some(m=>m.id==='east_tradition');}
 r.nations=nations;r.missions=missions;r.faith=faith;r.styles=styles;r.finite=finite;r.traditions=traditions;
 let choices=0;for(const [id,event] of Object.entries(EVT).filter(([id])=>id.startsWith('east_'))){for(const option of event.o){const n=id.startsWith('east_goryeo_jikji')?'Goryeo':id.startsWith('east_yuan_mandat')?'Yuan':Object.keys(EAST_PROFILE).find(n=>id.startsWith('east_'+n+'_'));newGame(n);beginGame();const before=JSON.stringify(G);option.fx();if(JSON.stringify(G)===before||!Number.isFinite(G.treasury))throw Error(id+' missing effect');choices++;}}
 r.eventChoices=choices===84;
 newGame('Goryeo');beginGame();G.y=1350;r.goryeoDate=!EVT['east_Goryeo_dewan'].cond();G.y=1351;r.goryeoTrigger=EVT['east_Goryeo_dewan'].cond();EVT['east_Goryeo_dewan'].o[0].fx();saveGame(true);const saved=JSON.parse(localStorage.getItem(SAVE_KEY));G=saved;fixSave();r.ruler=NATS.Goryeo.ruler.name==='Gongmin';newGame('Goryeo');r.resetRuler=NATS.Goryeo.ruler.name==='Chungjeong';
 newGame('Yuan');r.noEarlyMing=!NATS.Ming&&NATS.Yuan.ruler.name==='Toghon Temur';G.y=1350;r.revoltDate=!EVT['east_Yuan_dewan'].cond();G.y=1351;r.revoltTrigger=EVT['east_Yuan_dewan'].cond();G.y=1377;G.tech[0]=4;newGame('Goryeo');G.y=1377;G.tech[0]=4;r.jikji=EVT.east_goryeo_jikji.cond();
 newGame('Ashikaga');r.japanSplit=alive('Yoshino')&&NATS.Ashikaga.capital.n==='Kyoto'&&NATS.Yoshino.capital.n==='Yoshino';const m=activeMissions().find(m=>m.id==='east_Ashikaga_m0');G.resourceStocks[G.nat].food=50;const mil=G.mana[2];completeMission(m.id);completeMission(m.id);r.rewardOnce=G.mana[2]===mil+25&&G.claims.some(id=>OWNR[id]==='Yoshino');
 newGame('Ashikaga');const unify=EAST_PROFILE.Ashikaga.missions[3];for(const id of NATS.Yoshino.ids)G.own[id]='Yuan';setWorld();r.thirdPartyConquest=!eastMissionReady(unify);
 r.nodes=TRADE_NODES.length===10&&tradeNode(NATS.Yuan.capital)==='hangzhou'&&tradeNode(NATS.Goryeo.capital)==='korea'&&tradeNode(NATS.Ashikaga.capital)==='nippon';
 newGame('Majapahit');for(let i=0;i<48;i++){G.mo=i%12;G.y=1350+Math.floor(i/12);resourcesMonth();G.d=5;for(let j=0;j<10;j++)navyDay();aiContentMonth();}r.ai=Object.keys(EAST_PROFILE).filter(n=>alive(n)).every(n=>G.aiContent[n].missions.some(id=>id.startsWith('east_')));return r;}""")
 print('content',result,flush=True);assert all(result.values()),result
 page.evaluate("newGame('Ashikaga');beginGame();winMode='culture';renderWin()")
 page.wait_for_timeout(1600);page.screenshot(path='/tmp/nusantara-east-japan.png')
 page.evaluate("newGame('Yuan');beginGame();winMode='missions';missionBranch='Istana';renderWin()")
 page.wait_for_timeout(1000);page.screenshot(path='/tmp/nusantara-east-yuan.png')
 page.evaluate("winMode=null;renderWin();showStart()")
 assert page.locator('#stList, #nationPicker').count()==0
 page.evaluate("cancelAnimationFrame(anim);centerOn(NATS.Goryeo.capital.lab[0],NATS.Goryeo.capital.lab[1],2)")
 page.wait_for_timeout(500);page.screenshot(path='/tmp/nusantara-start-map-only.png')
 page.mouse.click(390,180);assert page.evaluate('selNat')=='Goryeo'
 page.locator('#btnStart').click();assert page.evaluate('G.nat')=='Goryeo'
 page.locator('#mapViewToggle').click();page.locator('[data-mapregion=japan]').click();assert not page.locator('#mapViewMenu').is_visible()
 page.wait_for_timeout(600);page.screenshot(path='/tmp/nusantara-east-overview.png')
 assert not errors,errors
 print('PASS: old save migration, 20 profiles, 80 missions, 42 events/84 choices, chronology, ruler reset, AI and region navigation',flush=True)
 b.close()
s.shutdown()
