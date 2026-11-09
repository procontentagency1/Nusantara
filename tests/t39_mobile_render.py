"""Constrain canvas allocations like a small mobile renderer, then exercise resize/save recovery."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
probe="""(()=>{const live=new Set();window.renderProbe={peak:0,rejected:0,writes:0};const p=HTMLCanvasElement.prototype;
for(const key of ['width','height']){const d=Object.getOwnPropertyDescriptor(p,key);Object.defineProperty(p,key,{...d,set(v){d.set.call(this,v);live.add(this);renderProbe.writes++;renderProbe.peak=Math.max(renderProbe.peak,[...live].reduce((sum,c)=>sum+c.width*c.height*4,0));}});}
const get=p.getContext;p.getContext=function(...args){if(this.width*this.height>2000000){renderProbe.rejected++;return null;}return get.apply(this,args);};})();"""
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for size in [{'width':360,'height':800},{'width':720,'height':1280}]:
  page=b.new_page(viewport=size,device_scale_factor=3,is_mobile=True,has_touch=True);errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.add_init_script(probe)
  page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1600)
  metrics=page.evaluate("""()=>({probe:renderProbe,texture:TEX.tw*TEX.th,world:worldCache.c.width*worldCache.c.height,main:cvs.width*cvs.height,ready:TEX.ready})""")
  print(size,metrics,flush=True)
  assert metrics['ready'] and metrics['probe']['rejected']==0
  assert metrics['probe']['peak']<32*1024*1024 and metrics['texture']<1010000 and metrics['world']<1010000
  page.locator('#btnStart').click();page.wait_for_timeout(700)
  page.evaluate("G.treasury=543;saveGame(true)")
  page.evaluate("""()=>{const before=renderProbe.writes;for(let i=0;i<20;i++)onResize();if(renderProbe.writes!==before)throw Error('Unchanged resize reallocates canvas');}""")
  # Both orientations and Android URL-bar height changes invalidate the viewport cache.
  for viewport in [dict(width=800,height=360),dict(width=800,height=330),size]:
   page.set_viewport_size(viewport);page.wait_for_timeout(400)
   assert page.evaluate('detail.ok&&detail.h===cvs.height&&detail.w===cvs.width')
  page.evaluate("cvs.dispatchEvent(new Event('contextlost',{cancelable:true}));cvs.width=cvs.width;cvs.dispatchEvent(new Event('contextrestored'))")
  page.wait_for_timeout(500)
  assert page.evaluate("G.treasury===543&&JSON.parse(localStorage.getItem(SAVE_KEY)).treasury===543&&detail.ok")
  assert page.evaluate("(()=>{const d=mainCtx.getImageData(Math.floor(cvs.width/2),Math.floor(cvs.height/2),1,1).data;return d[3]===255&&d[0]+d[1]+d[2]>20;})()")
  page.screenshot(path='/tmp/nusantara-mobile-render-%d.png'%size['width']);assert not errors,errors;page.close()
 # A texture allocation/read failure must leave the base map and game usable.
 page=b.new_page(viewport={'width':780,'height':360});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.add_init_script("const get=CanvasRenderingContext2D.prototype.getImageData;CanvasRenderingContext2D.prototype.getImageData=function(...a){if(this.canvas.width*this.canvas.height>500000)throw Error('Simulated texture allocation failure');return get.apply(this,a);}")
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1000)
 page.locator('#btnStart').click();page.wait_for_timeout(500)
 assert page.evaluate("!TEX.ready&&phase==='game'&&detail.ok") and not errors,errors
 b.close()
s.shutdown();print('PASS: bounded mobile canvas memory, portrait/landscape/URL-bar resize, context recovery, save preservation and texture fallback')
