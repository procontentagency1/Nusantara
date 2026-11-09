from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from pathlib import Path
from playwright.sync_api import sync_playwright
s=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler);Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':780,'height':360},device_scale_factor=2);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 # Inspect the actual output and oscillator routing, without exposing audio internals to game UI.
 page.add_init_script('''(()=>{const connect=AudioNode.prototype.connect;AudioNode.prototype.connect=function(dest,...args){if(dest instanceof AudioDestinationNode){window.audioContext=this.context;window.audioOutput=this;}return connect.call(this,dest,...args);};})();''')
 page.goto('http://127.0.0.1:%d/'%s.server_port);page.wait_for_timeout(1200)
 page.evaluate("newGame('Majapahit');beginGame();G.al=[];G.subj={};G.tributaries={};winMode='menu';renderWin()")
 page.locator('#sound-music').click()
 page.evaluate("SFX.setSfx(false);SFX.setMus(true);SFX.setLevel('music',65)")
 page.wait_for_timeout(3500)
 measured=page.evaluate('''async()=>{const analyser=audioContext.createAnalyser();analyser.fftSize=2048;audioOutput.connect(analyser);const d=new Float32Array(analyser.fftSize);let peak=0,energy=0;for(let i=0;i<10;i++){analyser.getFloatTimeDomainData(d);for(const x of d){peak=Math.max(peak,Math.abs(x));energy+=x*x;}await new Promise(r=>setTimeout(r,80));}analyser.disconnect();return {peak,rms:Math.sqrt(energy/(10*d.length))};}''')
 print('music output',measured);assert measured['rms']>.0001 and measured['peak']<.95,measured
 assert page.evaluate('SFX.scene')=='peace'
 page.evaluate("declareWar('Sunda','Bali',{k:'nocb'})")
 assert page.evaluate('SFX.scene')=='peace','Unrelated AI wars must not switch player music'
 page.evaluate("G.wars=[];declareWar(G.nat,'Sunda',{k:'nocb'})")
 assert page.evaluate('SFX.scene')=='war'
 page.wait_for_timeout(2000)
 war_output=page.evaluate('''async()=>{const a=audioContext.createAnalyser();a.fftSize=2048;audioOutput.connect(a);const d=new Float32Array(2048);let peak=0,sum=0;for(let i=0;i<12;i++){a.getFloatTimeDomainData(d);for(const x of d){peak=Math.max(peak,Math.abs(x));sum+=x*x;}await new Promise(r=>setTimeout(r,80));}a.disconnect();return {peak,rms:Math.sqrt(sum/(12*d.length))};}''')
 print('war music output',war_output);assert war_output['rms']>.0001 and war_output['peak']<.95
 page.evaluate("window.audioBattle=newBattle(capOf(G.nat).id,[myArmies()[0]],[G.armies.find(a=>a.nat==='Sunda')],'A')")
 assert page.evaluate('SFX.scene')=='battle'
 page.wait_for_timeout(1800)
 battle_output=page.evaluate('''async()=>{const a=audioContext.createAnalyser();a.fftSize=2048;audioOutput.connect(a);const d=new Float32Array(2048);let peak=0,sum=0;for(let i=0;i<12;i++){a.getFloatTimeDomainData(d);for(const x of d){peak=Math.max(peak,Math.abs(x));sum+=x*x;}await new Promise(r=>setTimeout(r,80));}a.disconnect();return {peak,rms:Math.sqrt(sum/(12*d.length))};}''')
 print('battle music output',battle_output);assert battle_output['rms']>.0001 and battle_output['peak']<.95
 page.evaluate("endBattle(audioBattle,null)")
 assert page.evaluate('SFX.scene')=='war'
 page.evaluate("applyPeace(G.wars[0],'att',{white:true})")
 assert page.evaluate('SFX.scene')=='peace'
 # No new music sources are created when muted (including the old leaked drum issue).
 page.evaluate("SFX.setMus(false)")
 muted=page.evaluate('''async()=>{let starts=0;const old=AudioScheduledSourceNode.prototype.start;AudioScheduledSourceNode.prototype.start=function(...args){starts++;return old.apply(this,args);};try{await new Promise(r=>setTimeout(r,2200));}finally{AudioScheduledSourceNode.prototype.start=old;}return {starts,voices:SFX.voices};}''')
 print('muted scheduler',muted);assert muted['starts']==0
 # Slider input, persistence and migration from old on/off preferences.
 page.evaluate("winMode='menu';renderWin()")
 page.locator('#sound-effects').fill('25');page.locator('#sound-effects').dispatch_event('input')
 assert page.evaluate("JSON.parse(localStorage.getItem('nus_snd')).levels.effects")==25
 assert page.locator('#sound-value-effects').inner_text()=='25%'
 page.evaluate("SFX.setLevel('music',200);SFX.setLevel('interface',-1)")
 assert page.evaluate('SFX.levels.music')==100 and page.evaluate('SFX.levels.interface')==0
 page.evaluate("SFX.pauseAll(true)");assert page.evaluate('audioContext.state')=='suspended'
 page.evaluate("SFX.pauseAll(false)");assert page.evaluate('audioContext.state')=='running'
 # Expired voices disconnect instead of accumulating indefinitely.
 page.evaluate("SFX.setSfx(true);SFX.setLevel('interface',65);SFX.play('tap')")
 page.wait_for_timeout(3200)
 assert page.evaluate('SFX.voices')==0
 page.evaluate("localStorage.setItem('nus_snd',JSON.stringify({sfx:false,mus:true}))")
 page.reload();assert page.evaluate('!SFX.sfx&&SFX.mus&&SFX.levels.music===40')
 page.evaluate("newGame('Majapahit');beginGame();winMode='menu';renderWin()")
 page.wait_for_timeout(2500);page.screenshot(path='/tmp/nusantara-audio-settings.png')
 assert not errors,errors
 print('PASS: peace/war/battle, unrelated wars, music output, mute routing, sliders, persistence, suspend/resume, voice cleanup, legacy preferences')
 b.close()
s.shutdown()
