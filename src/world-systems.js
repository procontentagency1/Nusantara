/* Sistem dunia: komunitas pelabuhan, lembaga, era dan keputusan AI. */
const WORLD_AGES=[
 {name:'Era Mandala dan Bandar',year:1350,objectives:[
  {id:'ports',name:'Jaringan Bandar',desc:'Kuasai dua provinsi pesisir',test:n=>(OWNED[n]||[]).filter(id=>PROV[id].cd).length>=2,fx:{trade:.05}},
  {id:'stable',name:'Tata Negeri',desc:'Stabilitas minimal +2 dan tidak bangkrut',test:n=>n===G.nat?G.stab>=2&&!G.bank:!warsOf(n).length,fx:{tax:.04}},
  {id:'exchange',name:'Pertukaran Pengetahuan',desc:'Teknologi ADM tingkat 4',test:n=>worldAiLevel(n,0)>=4,fx:{tech:-.03}}]},
 {name:'Era Pelayaran dan Pertukaran',year:1400,objectives:[
  {id:'institution',name:'Pengetahuan Berlayar',desc:'Adopsi lembaga Pelayaran Jung',test:n=>worldAdopted('pelayaran',n),fx:{prod:.05}},
  {id:'trade',name:'Dua Pesisir',desc:'Kuasai pelabuhan pada dua node perdagangan',test:n=>new Set((OWNED[n]||[]).filter(id=>PROV[id].cd).map(id=>tradeNode(PROV[id]))).size>=2,fx:{trade:.08}},
  {id:'army',name:'Angkatan Siap',desc:'Capai 80% batas pasukan',test:n=>regsOf(n)>=Math.ceil((n===G.nat?econ().fl:aiFl(n))*.8),fx:{army:-.05}}]},
 {name:'Era Perubahan Kekuasaan',year:1450,objectives:[
  {id:'gunpowder',name:'Pengetahuan Mesiu',desc:'Adopsi lembaga Meriam & Mesiu',test:n=>worldAdopted('mesiu',n),fx:{mpmax:.05}},
  {id:'diplomacy',name:'Jaringan Diplomasi',desc:'Miliki satu aliansi',test:n=>G.al.some(k=>k.split('|').includes(n)),fx:{dipl:1}},
  {id:'technology',name:'Pembaharuan Pemerintahan',desc:'Teknologi ADM tingkat 8',test:n=>worldAiLevel(n,0)>=8,fx:{tech:-.04}}]}
];
function worldAge(){return WORLD_AGES[G.world?.era||0];}
function worldAdopted(k,n){const s=G.inst[k];return !!s&&(n===G.nat?!!s.emb:!!s.aiEmb?.[n]);}
function worldAverageTech(){const ns=Object.keys(NATS).filter(n=>alive(n));return ns.length?(ns.reduce((sum,n)=>sum+[0,1,2].reduce((a,i)=>a+worldAiLevel(n,i),0)/3,0)/ns.length).toFixed(1):'3.0';}
function worldAiLevel(n,i){return n===G?.nat?G.tech[i]:(G?.world?.ai?.[n]?.tech?.[i]??aiTech());}
function worldCommunity(id){return G.world?.communities?.[id]?.islam||0;}
function worldIsCoast(p){return !!p?.cd;}
function worldLinked(a,b){if(!a||!b||a===b)return false;const until=G.world.tradeLinks[pairKey(a,b)];return Number.isFinite(until)&&until>monthIdx();}
function worldNodesAdjacent(a,b){return a===b||!!TRADE_BY_ID[a]?.out.includes(b)||!!TRADE_BY_ID[b]?.out.includes(a);}
function fixWorld(){
 if(!G.world){
  const migrated=G.y>1350||G.mo>0||G.d>1;G.world={version:1,communities:{},policy:{},faith:{},ai:{},era:0,claims:{},events:{},tradeLinks:{}};
  for(const p of provs)if(p.k==='L'&&G.pr[p.id]==='islam')G.world.communities[p.id]={islam:100};
  for(const [name,v] of [['Samudra',100],['Quanzhou',28],['Brunei',12],['Vijaya',12],['Tumasik',10]]){const p=byName(name);if(p&&G.pr[p.id]!=='islam')G.world.communities[p.id]={islam:v};}
  if(migrated){if(G.y>=1450&&G.inst.mesiu?.on)G.world.era=2;else if(G.y>=1400&&G.inst.pelayaran?.on)G.world.era=1;G.world.events.bandar=G.y>=1370;G.world.events.wabah=G.y>=1380;G.world.events.krisis=G.y>=1420;}
 }
 const w=G.world;w.communities||={};w.policy||={};w.faith||={};w.ai||={};w.claims||={};w.events||={};w.tradeLinks||={};w.era=Math.max(0,Math.min(WORLD_AGES.length-1,w.era||0));
 for(const n of Object.keys(NATS)){w.faith[n] ||= n===G.nat?G.rs:relKey(RELIG[n]);const a=w.ai[n] ||= {funds:Math.min(500,40+NATS[n].dev),tech:[aiTech(),aiTech(),aiTech()],points:[0,0,0]};a.funds=Number.isFinite(a.funds)?a.funds:40;a.tech ||= [aiTech(),aiTech(),aiTech()];a.points ||= [0,0,0];w.policy[n] ||= 'balance';if(n!==G.nat&&RELS[w.faith[n]])NATS[n].relig=RELS[w.faith[n]].n;}
 w.faith[G.nat]=G.rs;
 for(const I of INST){const s=G.inst[I.k];if(!s)continue;s.pv ||= {};s.progress ||= {};s.aiEmb ||= {};for(const id of Object.keys(s.pv))s.progress[id]=100;}
}
function worldOwnIds(n){return (OWNED[n]||[]).filter(id=>PROV[id]?.k==='L');}
function worldShare(n,k){const s=G.inst[k],ids=worldOwnIds(n);let have=0,total=0;for(const id of ids){const d=provDev(id);total+=d;if(s?.pv[id])have+=d;}return total?have/total:0;}
function worldInstitutionPenalty(s,I){const start=Number.isFinite(s.started)?s.started:Math.max(0,(I.y-1350)*12);return Math.min(.5,Math.max(0,monthIdx()-start)/1200);}
function worldInstitutionMonth(){
 fixWorld();
 for(const I of INST){
  const s=G.inst[I.k] ||= {on:false,pv:{},emb:false,progress:{},aiEmb:{}};s.pv||={};s.progress||={};s.aiEmb||={};
  if(!s.on&&G.y>=I.y){s.on=true;s.started=monthIdx();const id=orgProv(I.org);s.pv[id]=1;s.progress[id]=100;addWorldLog('Lembaga '+I.n+' muncul di '+PROV[id].n+'.');toast('Lembaga '+I.n+' muncul di '+PROV[id].n+'.');}
  if(!s.on)continue;
  const source=Object.keys(s.pv).map(Number),routes=source.filter(id=>worldIsCoast(PROV[id])).map(id=>({node:tradeNode(PROV[id]),owner:OWNR[id]}));
  for(const p of provs){if(p.k!=='L'||s.pv[p.id])continue;const owner=OWNR[p.id],near=(LINK[p.id]||[]).some(l=>s.pv[l.to]);const maritime=worldIsCoast(p)&&routes.some(r=>r.owner&&!atWar(owner,r.owner)&&(worldNodesAdjacent(r.node,tradeNode(p))||worldLinked(owner,r.owner)));if(!near&&!maritime)continue;
   const market=G.pv[p.id]?.bld.includes('pasar')?0.3:0,merchant=(owner===G.nat&&G.trade?.merchants.some(m=>!m.left&&m.node===tradeNode(p))) ? 0.25 : 0;
   const patrol=(G.fleets||[]).some(f=>f.nat===owner&&f.mission==='trade'&&!f.path.length&&!f.port&&seaTradeNode(f.sea)===tradeNode(p)) ? 0.15 : 0;
   const gain=(near ? 0.8 : 0)+(maritime ? 0.35 : 0)+market+merchant+patrol+Math.min(.35,provDev(p.id)/100);s.progress[p.id]=Math.min(100,(s.progress[p.id]||0)+gain);if(s.progress[p.id]>=100)s.pv[p.id]=1;
  }
 }
}
function worldAiMonth(){
 for(const n of Object.keys(NATS)){if(n===G.nat||!alive(n))continue;const a=G.world.ai[n];a.funds=Math.min(2000,a.funds+(1+natDev(n)*.035)*(G.world.policy[n]==='welcome'?1.05:G.world.policy[n]==='restrict' ? 0.95 : 1));
  for(const I of INST){const s=G.inst[I.k];if(!s?.on||s.aiEmb[n]||worldShare(n,I.k)<.1)continue;const cost=Math.max(20,Math.round(.8*natDev(n)*(1-worldShare(n,I.k))));if(a.funds>=cost){a.funds-=cost;s.aiEmb[n]=true;addWorldLog(n+' mengadopsi lembaga '+I.n+'.');}}
  for(let i=0;i<3;i++){a.points[i]=Math.min(1600,a.points[i]+3+([NATS[n].ruler.a,NATS[n].ruler.d,NATS[n].ruler.m][i]||3));const penalty=INST.reduce((sum,I)=>{const s=G.inst[I.k];return sum+(s?.on&&!s.aiEmb[n]?worldInstitutionPenalty(s,I):0);},0);const ahead=.1*Math.max(0,techYear(a.tech[i]+1)-G.y),cost=Math.round(600*(1+penalty+ahead));if(a.tech[i]<TL_MAX&&a.points[i]>=cost){a.points[i]-=cost;a.tech[i]++;}}
 }
}
function worldCommunityMonth(){
 const w=G.world,sources=provs.filter(p=>p.k==='L'&&worldIsCoast(p)&&(worldCommunity(p.id)>=25||G.pr[p.id]==='islam'));
 for(const p of provs){if(p.k!=='L'||!worldIsCoast(p)||G.pr[p.id]==='islam')continue;const owner=OWNR[p.id];if(!owner||!alive(owner))continue;const policy=w.policy[owner]||'balance';
  const routes=sources.filter(q=>q.id!==p.id&&!atWar(owner,OWNR[q.id])&&(worldNodesAdjacent(tradeNode(p),tradeNode(q))||worldLinked(owner,OWNR[q.id])));const exposure=routes.length>0;const linked=routes.some(q=>worldLinked(owner,OWNR[q.id]));const activeMerchant=owner===G.nat&&G.trade?.merchants.some(m=>!m.left&&m.node===tradeNode(p));const patrol=(G.fleets||[]).some(f=>f.nat===owner&&f.mission==='trade'&&!f.path.length&&!f.port&&seaTradeNode(f.sea)===tradeNode(p));const local=(LINK[p.id]||[]).some(l=>G.pr[l.to]==='islam'||worldCommunity(l.to)>=60);
  const prior=worldCommunity(p.id);let delta=(exposure ? 0.02 : 0)+(local ? 0.035 : 0)+(exposure&&linked ? 0.015 : 0)+(exposure&&activeMerchant ? 0.01 : 0)+(exposure&&patrol ? 0.01 : 0)+(policy==='welcome'&&(prior>0||exposure||local) ? 0.06 : policy==='restrict' ? -0.06 : 0);if(!exposure&&!local&&policy!=='welcome')delta-=.005;
  if(delta===0&&!prior)continue;const value=Math.max(0,Math.min(100,prior+delta));if(value>0)(w.communities[p.id] ||= {}).islam=value;else if(w.communities[p.id])delete w.communities[p.id].islam;
  if(value>=90&&policy==='welcome'&&!(CTRL[p.id]&&CTRL[p.id]!==owner)){G.pr[p.id]='islam';addWorldLog('Islam menjadi agama dominan di '+p.n+'.');if(owner===G.nat)toast('Islam menjadi agama dominan di '+p.n+'.');}
 }
 // AI weighs community strength against war; a conversion is a visible, lasting decision.
 if(G.mo===0)for(const n of Object.keys(NATS)){if(n===G.nat||!alive(n))continue;const ids=worldOwnIds(n),total=ids.reduce((s,id)=>s+provDev(id),0),muslim=ids.reduce((s,id)=>s+provDev(id)*(G.pr[id]==='islam'?1:worldCommunity(id)/100),0),share=total?muslim/total:0;
  if(w.faith[n]!=='islam'&&share>=.6&&!warsOf(n).length&&ids.some(id=>G.pr[id]==='islam')){w.faith[n]='islam';NATS[n].relig=RELS.islam.n;w.policy[n]='welcome';addWorldLog(n+' memeluk Islam setelah pertumbuhan komunitas.');}
  else if(w.faith[n]==='islam')w.policy[n]='welcome';else if(share>=.18&&NATS[n].ruler.a<=2&&!warsOf(n).length)w.policy[n]='restrict';else if(share>=.4&&!warsOf(n).length)w.policy[n]='welcome';else w.policy[n]='balance';
 }
}
function worldEraMonth(){
 const w=G.world,current=w.era,next=current+1,I=next===1?G.inst.pelayaran:next===2?G.inst.mesiu:null,need=next===1?8:12;
 if(I&&G.y>=WORLD_AGES[next].year&&I.on&&Object.keys(I.pv).length>=need){w.era=next;G.mod=G.mod.filter(m=>!m.id.startsWith('age_'));addWorldLog('Dunia memasuki '+worldAge().name+'.');toast('Dunia memasuki '+worldAge().name+'.');}
 if(G.mo!==0)return;
 for(const n of Object.keys(NATS)){if(n===G.nat||!alive(n))continue;const key=n+'|'+w.era,done=w.claims[key] ||= [];for(const o of worldAge().objectives)if(!done.includes(o.id)&&o.test(n)){done.push(o.id);const stock=G.resourceStocks[n];if(stock)stock.food=Math.min(resourceCapacity(n,'food'),stock.food+5);}}
}
function worldClaim(id){const o=worldAge().objectives.find(o=>o.id===id),key=G.nat+'|'+G.world.era,done=G.world.claims[key] ||= [];if(!o||done.includes(id)||!o.test(G.nat))return;done.push(id);addMod('age_'+G.world.era+'_'+id,o.name,-1,o.fx);toast('Tujuan era tercapai: '+o.name+'.');saveGame(true);}
function worldGlobalMonth(){
 const w=G.world,nodes=new Set(provs.filter(p=>p.k==='L'&&worldIsCoast(p)&&worldCommunity(p.id)>=20).map(tradeNode));
 if(!w.events.bandar&&G.y>=1370&&nodes.size>=2){w.events.bandar=true;for(const n of Object.keys(NATS)){if(!alive(n)||n===G.nat)continue;const a=w.ai[n],stock=G.resourceStocks[n];a.funds=Math.min(2000,a.funds+15);if(stock){const k=stock.food<15?'food':'wood';stock[k]=Math.min(resourceCapacity(n,k),stock[k]+5);a.lastDecision=k==='food'?'Menambah lumbung':'Mendukung galangan';}}addWorldLog('Pertukaran bandar antarkawasan berkembang; kerajaan lain mendapat dana pengetahuan.');pushEvent({t:'Pertukaran Bandar Antarkawasan',x:'Jaringan pelaut dan pedagang menghubungkan semakin banyak bandar. Kerajaan lain memperoleh dana pengembangan. Dewan Anda harus menentukan prioritas.',o:[['Biayai pengetahuan · −30 dukat, +40 ADM','worldGlobal',{choice:'knowledge'}],['Dukung pasar · +10% dagang 5 tahun; −10 DIP (atau −15 dukat bila kurang)','worldGlobal',{choice:'trade'}]]});}
 const fleetNodes=new Set((G.fleets||[]).filter(f=>f.mission==='trade'&&!f.port&&!f.path.length&&!f.retreat).map(f=>seaTradeNode(f.sea)));
 if(!w.events.wabah&&G.y>=1380&&fleetNodes.size>=3){w.events.wabah=true;for(const n of Object.keys(NATS)){if(n===G.nat||!alive(n)||!portsOf(n).length)continue;const stock=G.resourceStocks[n],a=w.ai[n];if(stock){if(a.funds>=10&&stock.food>=5){a.funds-=10;stock.food=Math.max(0,stock.food-2);a.lastDecision='Membatasi bandar saat wabah';}else{stock.food=Math.max(0,stock.food-5);a.lastDecision='Menjaga pelayaran saat wabah';}}}addWorldLog('Wabah hipotetis mengganggu bandar yang terhubung oleh kapal dagang.');if(portsOf(G.nat).length)pushEvent({t:'Wabah di Bandar',x:'Wabah hipotetis mengikuti jaringan pelayaran aktif. Kerajaan pesisir lain memilih pembatasan bandar atau menanggung kehilangan persediaan. Pilih cara melindungi penduduk.',o:[['Batasi pelabuhan · −0,5K tenaga; dagang −10% selama 3 tahun','worldGlobal',{choice:'quarantine'}],['Pertahankan pelayaran · −1,5K tenaga','worldGlobal',{choice:'openport'}]]});else toast('Wabah mengganggu kerajaan pesisir lain.');}
 if(!w.events.krisis&&G.y>=1420&&w.era>=1&&nodes.size>=3){w.events.krisis=true;for(const n of Object.keys(NATS)){if(n===G.nat||!alive(n)||!G.resourceStocks[n])continue;const stock=G.resourceStocks[n],a=w.ai[n];if(stock.food>=8){stock.food-=8;a.lastDecision='Membuka lumbung';}else if(a.funds>=15){a.funds-=15;a.lastDecision='Membiayai pelayaran darurat';}else{stock.food=0;a.lastDecision='Menghabiskan cadangan pangan';}}addWorldLog('Gangguan pelayaran menekan persediaan pangan di kerajaan-kerajaan.');pushEvent({t:'Gangguan Pelayaran',x:'Cuaca dan gangguan jalur laut menekan persediaan di seluruh kawasan. Kerajaan lain memilih memakai lumbung atau membiayai pelayaran darurat.',o:[['Buka lumbung · hingga −8 pangan','worldGlobal',{choice:'food'}],['Bayar pelayaran darurat · −30 dukat','worldGlobal',{choice:'relief'}]]});}
}
EVA.worldGlobal=a=>{if(a.choice==='knowledge'){EF.gold(-30);EF.mana(0,40);}else if(a.choice==='trade'){if(G.mana[1]>=10)EF.mana(1,-10);else EF.gold(-15);EF.mod('world_trade','Pasar antarkawasan',60,{trade:.1});}else if(a.choice==='food'){G.resourceStocks[G.nat].food=Math.max(0,G.resourceStocks[G.nat].food-8);}else if(a.choice==='relief')EF.gold(-30);else if(a.choice==='quarantine'){G.mp=Math.max(0,G.mp-.5);EF.mod('world_quarantine','Pembatasan wabah',36,{trade:-.1});}else if(a.choice==='openport')G.mp=Math.max(0,G.mp-1.5);};
function worldSystemsMonth(){fixWorld();worldCommunityMonth();worldAiMonth();worldEraMonth();worldGlobalMonth();}
const _worldSettleResourceTrade=settleResourceTrade;settleResourceTrade=function(id,cancel=false){const order=G.resourceOrders?.find(o=>o.id===id);const done=_worldSettleResourceTrade(id,cancel);if(done&&!cancel&&order&&G.world){G.world.tradeLinks[pairKey(order.from,order.to)]=monthIdx()+60;saveGame(true);}return done;};
function worldReligionHTML(){const ids=Object.keys(G.pv).map(Number).filter(id=>worldCommunity(id)>0&&G.pr[id]!=='islam').sort((a,b)=>worldCommunity(b)-worldCommunity(a));let h='<div class="sec">Komunitas Muslim di bandar</div>'+(ids.length?ids.slice(0,8).map(id=>'<div class="r"><span>'+PROV[id].n+' · '+Math.round(worldCommunity(id))+'/100</span>'+btn('Dukung · 50 DIP','worldcommunity',{id},G.mana[1]>=50&&!(CTRL[id]&&CTRL[id]!==G.nat))+'</div>').join(''):'<p class="note">Belum ada komunitas yang tercatat di wilayah Anda.</p>');const pol=G.world.policy[G.nat]||'balance';h+='<p class="note">Angka adalah indeks pengaruh, bukan persentase penduduk. Jalur dagang, kiriman berhasil, pedagang dan kapal patroli mempercepat pertumbuhan. Penerimaan memberi dagang +5% dan toleransi agama lain +1 serta mempercepat pertumbuhan; pada 90 komunitas dapat menjadi agama dominan provinsi. Pembatasan menurunkan komunitas dan mengurangi efisiensi dagang 5%.</p><div class="r">'+[['balance','Seimbang'],['welcome','Terima'],['restrict','Batasi']].map(([k,l])=>btn((pol===k?'✓ ':'')+l,'worldpolicy',{k},pol!==k)).join('')+'</div>';if(G.rs!=='islam'&&ids.some(id=>worldCommunity(id)>=60))h+='<div class="r">'+btn('Peluk Islam · 150 ADM','worldconvert',{},G.mana[0]>=150)+'</div>';return h;}
function worldConvertIslam(){if(G.rs==='islam'||G.mana[0]<150||!Object.keys(G.pv).some(id=>worldCommunity(id)>=60))return;G.mana[0]-=150;G.rs='islam';G.world.faith[G.nat]='islam';NATS[G.nat].relig=RELS.islam.n;G.miss=[];EF.stab(-2);addMod('chrel','Perubahan keyakinan',24,{tax:-.10});addLog('Kerajaan memeluk Islam melalui komunitas bandar.');toast('Agama negara kini Islam Sunni.');saveGame(true);}
function worldBonusText(fx){return Object.entries(fx).map(([k,v])=>({trade:'dagang',tax:'pajak',prod:'produksi',tech:'biaya teknologi',army:'biaya pasukan',mpmax:'batas tenaga',dipl:'diplomat'}[k]||k)+' '+(v>0?'+':'')+(k==='dipl'?v:Math.round(v*100)+'%')).join(', ');}
function worldEraHTML(){const age=worldAge(),key=G.nat+'|'+G.world.era,done=G.world.claims[key]||[];let h=hd('Era Dunia',age.name)+'<p class="note">Era berganti ketika tahun minimum dan penyebaran lembaga terpenuhi. Bonus tujuan berlaku sampai era berikutnya.</p>';for(const o of age.objectives){const got=done.includes(o.id);h+='<div class="sec">'+o.name+'</div><div class="r"><span>'+o.desc+'<br><small>Hadiah: '+worldBonusText(o.fx)+'</small></span>'+(got?'<b>✓ Selesai</b>':btn('Ambil','worldobjective',{id:o.id},o.test(G.nat)))+'</div>';}const next=WORLD_AGES[G.world.era+1];if(next){const s=G.inst[G.world.era===0?'pelayaran':'mesiu'];h+='<div class="sec">Era berikutnya</div>'+row(next.name,'≥ '+next.year)+row('Provinsi terjangkau lembaga',Object.keys(s?.pv||{}).length+' / '+(G.world.era===0?8:12));}h+='<div class="sec">Peristiwa dunia</div>'+row('Pertukaran bandar',G.world.events.bandar?'Terjadi':'Belum terjadi')+row('Wabah bandar',G.world.events.wabah?'Terjadi':'Belum terjadi')+row('Gangguan pelayaran',G.world.events.krisis?'Terjadi':'Belum terjadi');return h;}
act.worldpolicy=b=>{const k=b.dataset.k;if(!['balance','welcome','restrict'].includes(k))return;G.world.policy[G.nat]=k;G.mod=G.mod.filter(m=>m.id!=='world_restrict'&&m.id!=='world_welcome');if(k==='welcome')addMod('world_welcome','Bandar terbuka',-1,{trade:.05,tolN:1});if(k==='restrict')addMod('world_restrict','Pembatasan bandar',-1,{trade:-.05});saveGame(true);};
act.worldcommunity=b=>{const id=+b.dataset.id;if(!G.pv[id]||!worldIsCoast(PROV[id])||worldCommunity(id)<=0||G.pr[id]==='islam'||G.mana[1]<50||CTRL[id]&&CTRL[id]!==G.nat)return;G.mana[1]-=50;(G.world.communities[id] ||= {}).islam=Math.min(100,worldCommunity(id)+10);toast('Komunitas di '+PROV[id].n+' mendapat dukungan.');saveGame(true);};
act.worldconvert=()=>worldConvertIslam();
act.worldobjective=b=>worldClaim(b.dataset.id);
const _worldRelHTML=relHTML;relHTML=function(){return _worldRelHTML() + worldReligionHTML();};
const _worldRelRow=relRow;relRow=function(id){const value=worldCommunity(id);if(!value||relOf(id)==='islam')return _worldRelRow(id);return _worldRelRow(id)+row('Pengaruh komunitas Muslim',Math.round(value)+'/100')+(G.pv[id]&&worldIsCoast(PROV[id])?'<div class="r">'+btn('Dukung komunitas · 50 DIP','worldcommunity',{id},G.mana[1]>=50&&!(CTRL[id]&&CTRL[id]!==G.nat))+'</div>':'');};
const _worldForeignProvHTML=foreignProvHTML;foreignProvHTML=function(p){const value=worldCommunity(p.id);return _worldForeignProvHTML(p)+(value>0&&relOf(p.id)!=='islam'?row('Pengaruh komunitas Muslim',Math.round(value)+'/100'):'');};
const _worldTechHTML=techHTML;techHTML=function(){let h=_worldTechHTML();for(const I of INST){const s=G.inst[I.k];if(!s?.on||s.emb)continue;const ids=worldOwnIds(G.nat).filter(id=>!s.pv[id]&&(s.progress?.[id]||0)>0).sort((a,b)=>s.progress[b]-s.progress[a]);if(ids.length)h+='<div class="sec">Penyebaran '+I.n+'</div>'+ids.slice(0,5).map(id=>row(PROV[id].n,Math.floor(s.progress[id])+'%')).join('');}return h+'<p class="note">Lembaga menyebar dari wilayah yang sudah menerimanya lewat tetangga dan node pelabuhan yang terhubung; pasar, pedagang dan kapal patroli aktif mempercepat penyebaran. AI menabung dan mengadopsi secara terpisah.</p>';};
