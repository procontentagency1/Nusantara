from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for size in [{'width':360,'height':800},{'width':720,'height':1280}]:
  page=b.new_page(viewport=size,device_scale_factor=3,is_mobile=True,has_touch=True);errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(800);page.locator('#btnStart').tap()
  result=page.evaluate("""()=>{cancelAnimationFrame(anim);const p=byName('Wilwatikta');centerOn(p.lab[0],p.lab[1],2);renderDetail();const c=mainCtx,original=c.drawImage,stats={world:0,detail:0,integer:true,unscaled:true};c.drawImage=function(img,...args){if(img===worldCache.c)stats.world++;if(img===detail.c){stats.detail++;stats.integer&&=Number.isInteger(args[0])&&Number.isInteger(args[1]);stats.unscaled&&=args.length===2;}return original.call(this,img,...args);};const start=view.tx;for(let i=1;i<=12;i++){view.tx=start+i*.71;clampView();frame();}const small={world:stats.world,detail:stats.detail,integer:stats.integer,unscaled:stats.unscaled};view.tx=start+detail.padX/dpr+20;clampView();frame();const largeFallback=stats.world>0;c.drawImage=original;return {...small,largeFallback,pad:detail.padX,canvas:detail.c.width*detail.c.height,viewport:cvs.width*cvs.height};}""")
  print(size,result,flush=True);assert result['world']==0 and result['detail']==12 and result['integer'] and result['unscaled'] and result['largeFallback'] and result['pad']>0 and result['canvas']<=1905000,result
  page.wait_for_function('detail.ok&&detail.tx===view.tx&&detail.ty===view.ty',timeout=5000)
  if size['width']==360:
   cdp=page.context.new_cdp_session(page);before=page.evaluate('view.tx');x=size['width']/2;y=size['height']/2
   cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]});cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x,'y':y+35}]});cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]});assert page.evaluate('view.tx')>before+20
  page.screenshot(path='/tmp/nusantara-drag-cache-%d.png'%size['width']);assert not errors,errors;page.close()
 b.close()
s.shutdown();print('PASS: sharp pixel-aligned padded cache during small pans, bounded memory, eventual redraw')
