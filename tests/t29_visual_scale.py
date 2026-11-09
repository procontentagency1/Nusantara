from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1500)
 result=page.evaluate("""() => {
 newGame('Majapahit');beginGame();paused=true;const a=G.armies.find(a=>a.nat===G.nat);G.armies=[a];a.path=[];
 const source=soldierSprite(natColor[a.nat],regionalStyle(a.nat)),outline=outlinedUnit(source);const pixels=c=>{const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let n=0;for(let i=3;i<d.length;i+=4)if(d[i])n++;return n;};const stroke=pixels(outline)>pixels(source),cached=outlinedUnit(source)===outline;
 const sizes=[],hits=[];const original=ctx.drawImage;let drawn=0;ctx.drawImage=function(c,...args){if(c===outline)drawn=Math.abs(this.getTransform().a)*args[2]/dpr;return original.call(this,c,...args);};
 for(const ratio of [.9,1,2,4,8,12]){view.s=fitS*ratio;view.tx=vw/2-PROV[a.loc].lab[0]*view.s;view.ty=vh/2-PROV[a.loc].lab[1]*view.s;ctx.setTransform(dpr,0,0,dpr,0,0);drawArmies();sizes.push(drawn);const h=ARM_HIT.find(h=>h.a===a);hits.push(h.x1-h.x0);if(Math.abs((h.x0+h.x1)/2-vw/2)>.01)throw Error('anchor drift');G.sel=null;onMapTap(PROV[a.loc],(h.x0+h.x1)/2,(h.y0+h.y1)/2);if(G.sel!==a.id)throw Error('hit missed '+ratio);}
 ctx.drawImage=original;
 const compact=sizes.at(-1)<28;const monotonic=sizes.every((n,i)=>!i||n>sizes[i-1])&&hits.every((n,i)=>!i||n>hits[i-1]);
 const coverage=Object.keys(NATS).every(n=>n==='Majapahit'||Object.values(CITY_STYLE_GROUPS).some(list=>list.includes(n)));
 const styles=['majapahit',...Object.keys(CITY_STYLE_GROUPS)];const unique=new Set(styles.map(style=>citySprite(1,0,style).toDataURL())).size===styles.length;
 G.wars=[];G.al=[];declareWar(G.nat,'Sunda',{k:'nocb'});const b=mkArmy('Sunda',4,a.loc);newBattle(a.loc,[a],[b],'A');const battles=[];for(const ratio of [1,4,12]){view.s=fitS*ratio;view.tx=vw/2-PROV[a.loc].lab[0]*view.s;view.ty=vh/2-PROV[a.loc].lab[1]*view.s;ctx.setTransform(dpr,0,0,dpr,0,0);drawArmies();battles.push(BT_HIT[0].x1-BT_HIT[0].x0);}const battleZoom=battles[0]<battles[1]&&battles[1]<battles[2];
 newGame('Majapahit');beginGame();return {sizes,hits,compact,stroke,cached,monotonic,coverage,unique,styles:styles.length,battleZoom};
 }""")
 print(result);assert all(result[k] for k in ['compact','stroke','cached','monotonic','coverage','unique','battleZoom'])
 page.wait_for_timeout(800)
 for ratio in [1,4,12]:
  page.evaluate("""ratio=>{view.s=fitS*ratio;const p=NATS.Majapahit.capital;view.tx=vw*.5-p.lab[0]*view.s;view.ty=vh*.6-p.lab[1]*view.s;winMode=null;renderWin();invalidate(true);}""",ratio)
  page.screenshot(path='/tmp/nusantara-units-zoom-'+str(ratio)+'.png')
 page.evaluate("""()=>{const styles=['majapahit',...Object.keys(CITY_STYLE_GROUPS)];const c=document.createElement('canvas');c.width=1000;c.height=500;c.style='position:fixed;inset:0;z-index:1000;width:1000px;height:500px';document.body.append(c);const g=c.getContext('2d');g.fillStyle='#143344';g.fillRect(0,0,1000,500);g.font='16px Georgia';g.fillStyle='#f1d38a';styles.forEach((s,i)=>{const x=i%5*200,y=Math.floor(i/5)*160;g.fillText(s,x+8,y+22);const img=citySprite(1,0,s);g.drawImage(img,x+15,y+35,img.width*1.7,img.height*1.7);});}""")
 page.locator('body > canvas').screenshot(path='/tmp/nusantara-regional-buildings.png')
 assert not errors,errors
 b.close()
s.shutdown()
