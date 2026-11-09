from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for size in [{'width':360,'height':800},{'width':780,'height':360}]:
  page=b.new_page(viewport=size,device_scale_factor=2,is_mobile=True,has_touch=True);errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(700)
  def bounds():
   return page.evaluate("""()=>{zoomAt(vw/2,vh/2,0);for(const [x,y] of [[9999,9999],[-9999,-9999],[9999,-9999],[-9999,9999]]){view.tx=x;view.ty=y;clampView();if(view.tx>.001||view.ty>.001||view.tx+WW*view.s<vw-.001||view.ty+WH*view.s<vh-.001)return false;}return true;}""")
  assert bounds();page.locator('#stPanelToggle').tap();point=page.evaluate("""()=>{cancelAnimationFrame(anim);const p=byName('Kaifeng');centerOn(p.lab[0],p.lab[1],minS);const x=view.tx+p.lab[0]*view.s,y=view.ty+p.lab[1]*view.s;return rot?[innerWidth-y,x]:[x,y];}""");page.wait_for_timeout(250);page.touchscreen.tap(*point);assert page.evaluate("selNat==='Yuan'")
  page.locator('#btnStart').tap();assert page.evaluate("G.nat==='Yuan'");assert bounds();page.screenshot(path='/tmp/nusantara-map-framing-%d.png'%size['width']);assert not errors,errors;page.close()
 b.close()
s.shutdown();print('PASS: no blank border at minimum zoom, panning and map selection on mobile')
