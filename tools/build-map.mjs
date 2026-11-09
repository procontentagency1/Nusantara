import fs from 'fs';
import * as topojson from 'topojson-client';
import { geoProjection, geoPath } from 'd3-geo';
import { Delaunay } from 'd3-delaunay';
import polygonClipping from 'polygon-clipping';
import { LAND, SEA } from './seeds.mjs';

const B = { x0: 92, x1: 146, y0: -11.5, y1: 46 };
// Lambert cylindrical equal-area: ukuran luas lintang utara dan tropis sebanding.
// Bentuk dan jarak tetap terdistorsi; garis bujur/lintang tetap lurus.
const RAD=Math.PI/180, scale=1600/((B.x1-B.x0)*RAD);
const proj=geoProjection((lambda,phi)=>[lambda,Math.sin(phi)])
 .scale(scale).translate([-scale*B.x0*RAD,scale*Math.sin(B.y1*RAD)]);
const W=1600, H=scale*(Math.sin(B.y1*RAD)-Math.sin(B.y0*RAD));
const P=(lo,la)=>proj([lo,la]);

// Daratan: potong dulu di koordinat geografis, lalu proyeksikan
const landTopo = JSON.parse(fs.readFileSync('node_modules/world-atlas/land-50m.json'));
const landGeo = topojson.feature(landTopo, landTopo.objects.land);
const landGeom = landGeo.type === 'FeatureCollection' ? landGeo.features[0].geometry : (landGeo.geometry || landGeo);
const clipGeo = polygonClipping.intersection(
  landGeom.type === 'Polygon' ? [landGeom.coordinates] : landGeom.coordinates,
  [[[B.x0,B.y0],[B.x1,B.y0],[B.x1,B.y1],[B.x0,B.y1],[B.x0,B.y0]]]);
const land = clipGeo.map(poly => poly.map(ring => ring.map(([lo,la]) => P(lo,la))));
const bboxR = [[[0,0],[W,0],[W,H],[0,H],[0,0]]];
const ocean = polygonClipping.difference(bboxR, land);

function cellsOf(seeds) {
  const pts = seeds.map(s => P(s[1], s[2]));
  const vor = Delaunay.from(pts).voronoi([0,0,W,H]);
  return pts.map((_, i) => {
    const poly = vor.cellPolygon(i);
    return poly ? [[poly.map(([x,y]) => [x,y])]].map(m => m)[0] : null;
  });
}
const round = v => Math.round(v*10)/10;
function toD(mp) {
  let d = '';
  for (const poly of mp) for (const ring of poly) {
    let prev = null;
    ring.forEach(([x,y], k) => {
      const X = round(x), Y = round(y);
      if (prev && prev[0]===X && prev[1]===Y) return;
      d += (k===0 || !prev ? 'M' : 'L') + X + ' ' + Y + ' ';
      prev = [X,Y];
    });
    d += 'Z ';
  }
  return d.trim();
}
function centroidLabel(mp, fallback) { return fallback; }

const provinces = [];
const landShapes = {};
const shapesByNat = {};
const previous=JSON.parse(fs.readFileSync('data/map-data.json','utf8'));
const stableIds=new Map(previous.provinces.map(p=>[p.k+'|'+p.n,p.id]));
let id=Math.max(...previous.provinces.map(p=>p.id));
const allocId=(kind,name)=>stableIds.get(kind+'|'+name)||++id;
const seedPts = LAND.map(s => P(s[1], s[2]));
const inRing = (ring, x, y) => { let c = false; for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) { const [xi, yi] = ring[i], [xj, yj] = ring[j]; if ((yi > y) !== (yj > y) && x < (xj - xi)*(y - yi)/(yj - yi) + xi) c = !c; } return c; };
const parts = LAND.map(() => []);
const orphans = [];
land.forEach(poly => {
  const inside = []; seedPts.forEach((pt, i) => { if (inRing(poly[0], pt[0], pt[1]) && !poly.slice(1).some(h => inRing(h, pt[0], pt[1]))) inside.push(i); });
  if (!inside.length) { orphans.push(poly); return; }
  if (inside.length === 1) { parts[inside[0]].push(poly); return; }
  const vor = Delaunay.from(inside.map(i => seedPts[i])).voronoi([0, 0, W, H]);
  inside.forEach((si, k) => {
    const cell = vor.cellPolygon(k); if (!cell) return;
    const sh = polygonClipping.intersection([cell.map(([x, y]) => [x, y])], poly);
    for (const m of sh) parts[si].push(m);
  });
});
for (const poly of orphans) {
  const c = poly[0].reduce((a, p) => [a[0] + p[0]/poly[0].length, a[1] + p[1]/poly[0].length], [0, 0]);
  let bi = 0, bd = 1e9; seedPts.forEach((pt, i) => { const d = Math.hypot(pt[0] - c[0], pt[1] - c[1]); if (d < bd) { bd = d; bi = i; } });
  parts[bi].push(poly);
}
LAND.forEach((s, i) => {
  const shape = parts[i]; if (!shape.length) { console.warn('kosong:', s[0]); return; }
  provinces.push({ id: allocId('L',s[0]), n: s[0], nat: s[3], st: s[4], t: s[5], r: s[6], k: 'L',
    lab: [round(seedPts[i][0]), round(seedPts[i][1])], d: toD(shape) });
  landShapes[provinces.at(-1).id] = shape;
  (shapesByNat[s[3]] ||= []).push(shape);
});
const seaCells = cellsOf(SEA);
SEA.forEach((s, i) => {
  const shape = polygonClipping.intersection([[seaCells[i][0]]], ocean);
  if (!shape.length) { console.warn('laut kosong:', s[0]); return; }
  provinces.push({ id: allocId('S',s[0]), n: s[0], nat: 'laut', st: 'sea', t: 'sea', r: 1, k: 'S',
    lab: [round(P(s[1],s[2])[0]), round(P(s[1],s[2])[1])], d: toD(shape) });
});

// ---- adjacency + batas bersama + selat ----
const key = (x,y) => Math.round(x*5) + ',' + Math.round(y*5);
const ids = Object.keys(landShapes).map(Number);
const verts = {}, vset = {}, bbs = {};
for (const i of ids) {
  const pts = []; const set = new Set();
  for (const poly of landShapes[i]) for (const ring of poly) for (const [x,y] of ring) { pts.push([x,y]); set.add(key(x,y)); }
  verts[i] = pts; vset[i] = set;
  const xs = pts.map(p=>p[0]), ys = pts.map(p=>p[1]);
  bbs[i] = [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)];
}
const adj = {}, edges = [];
for (const i of ids) adj[i] = [];
for (let a = 0; a < ids.length; a++) for (let b = a+1; b < ids.length; b++) {
  const i = ids[a], j = ids[b], A = bbs[i], B2 = bbs[j];
  if (A[2] < B2[0]-1 || B2[2] < A[0]-1 || A[3] < B2[1]-1 || B2[3] < A[1]-1) continue;
  let shared = 0; for (const k of vset[i]) if (vset[j].has(k)) shared++;
  if (shared < 2) continue;
  // polyline bersama
  let d = '', last = null, cnt = 0;
  for (const poly of landShapes[i]) for (const ring of poly) {
    for (let k = 0; k < ring.length - 1; k++) {
      const p = ring[k], q = ring[k+1];
      if (vset[j].has(key(p[0],p[1])) && vset[j].has(key(q[0],q[1]))) {
        if (last && last === key(p[0],p[1])) d += 'L' + round(q[0]) + ' ' + round(q[1]) + ' ';
        else d += 'M' + round(p[0]) + ' ' + round(p[1]) + ' L' + round(q[0]) + ' ' + round(q[1]) + ' ';
        last = key(q[0],q[1]); cnt++;
      }
    }
  }
  if (!cnt) continue;
  adj[i].push(j); adj[j].push(i); edges.push([i, j, d.trim()]);
}
// selat: pulau berbeda yang berdekatan
const comp = {}; let cc = 0;
for (const i of ids) if (!(i in comp)) { cc++; const st = [i]; comp[i] = cc; while (st.length) { const u = st.pop(); for (const v of adj[u]) if (!(v in comp)) { comp[v] = cc; st.push(v); } } }
const samp = {}; for (const i of ids) { const v = verts[i], st = Math.max(1, Math.floor(v.length/40)); samp[i] = v.filter((_, k) => k % st === 0); }
const cand = [];
for (let a = 0; a < ids.length; a++) for (let b = a+1; b < ids.length; b++) {
  const i = ids[a], j = ids[b]; if (comp[i] === comp[j]) continue;
  const A = bbs[i], B2 = bbs[j];
  if (A[2] < B2[0]-45 || B2[2] < A[0]-45 || A[3] < B2[1]-45 || B2[3] < A[1]-45) continue;
  let m = 1e9; for (const p of samp[i]) for (const q of samp[j]) m = Math.min(m, Math.hypot(p[0]-q[0], p[1]-q[1]));
  if (m < 40) cand.push([i, j, m]);
}
cand.sort((x,y) => x[2]-y[2]);
const straits = [], deg = {};
for (const [i, j] of cand) { if ((deg[i]||0) >= 3 || (deg[j]||0) >= 3) continue; straits.push([i, j]); deg[i] = (deg[i]||0)+1; deg[j] = (deg[j]||0)+1; }
// pastikan semua komponen utama terhubung minimal ke yang terdekat
console.log('adjacency pairs', edges.length, 'selat', straits.length, 'komponen', cc);


// jalur pantai per provinsi: segmen yang tidak dibagi dengan tetangga
const coastD = {};
for (const i of ids) {
  const nb = new Set(); for (const j of adj[i]) for (const k of vset[j]) nb.add(k);
  let d = '', last = null;
  for (const poly of landShapes[i]) for (const ring of poly) for (let k = 0; k < ring.length - 1; k++) {
    const p = ring[k], q = ring[k+1];
    if((Math.abs(p[0])<.01&&Math.abs(q[0])<.01)||(Math.abs(p[0]-W)<.01&&Math.abs(q[0]-W)<.01)||(Math.abs(p[1])<.01&&Math.abs(q[1])<.01)||(Math.abs(p[1]-H)<.01&&Math.abs(q[1]-H)<.01)){last=null;continue;}
    if (nb.has(key(p[0],p[1])) && nb.has(key(q[0],q[1]))) { last = null; continue; }
    if (last && last === key(p[0],p[1])) d += 'L' + round(q[0]) + ' ' + round(q[1]) + ' ';
    else d += 'M' + round(p[0]) + ' ' + round(p[1]) + ' L' + round(q[0]) + ' ' + round(q[1]) + ' ';
    last = key(q[0],q[1]);
  }
  coastD[i] = d.trim();
}
for (const p of provinces) if (p.k === 'L') p.cd = coastD[p.id] || '';

// Batas negara = gabungan provinsi per bangsa
const nations = Object.entries(shapesByNat).map(([nat, shapes]) => {
  const u = shapes.length > 1 ? polygonClipping.union(...shapes) : shapes[0];
  return { nat, d: toD(u) };
});
// Garis pantai terpisah (dipakai untuk outline daratan)
const coast = toD(land);
// Sungai besar (perkiraan koordinat lon,lat) dan danau
const RIVERS = [
  [[111.0,-7.95],[111.4,-7.55],[111.9,-7.15],[112.25,-6.9],[112.6,-6.88]],            // Bengawan Solo
  [[112.45,-8.0],[112.2,-7.6],[112.45,-7.3],[112.72,-7.38]],                           // Brantas
  [[107.35,-7.0],[107.3,-6.5],[107.55,-6.1]],                                          // Citarum
  [[103.2,-3.3],[104.0,-3.0],[104.8,-2.95]],                                           // Musi
  [[101.6,-1.8],[102.8,-1.9],[103.7,-1.5],[104.2,-1.0]],                               // Batanghari
  [[101.2,0.4],[102.2,0.5],[103.2,0.5]],                                               // Indragiri/Kampar
  [[100.4,2.2],[99.6,2.7],[98.9,3.3]],                                                 // Asahan/Barumun (kasar)
  [[112.0,0.9],[111.0,0.25],[110.0,0.0],[109.2,-0.05]],                                // Kapuas
  [[114.6,0.9],[115.6,0.3],[116.4,-0.5],[117.2,-0.55]],                                // Mahakam
  [[114.5,-1.4],[114.65,-2.5],[114.55,-3.6]],                                          // Barito
  [[138.0,-3.5],[137.7,-2.9],[137.95,-2.2]],                                           // Mamberamo
  [[139.5,-5.5],[139.2,-6.5],[139.0,-7.6]],                                            // Digul (kasar)
];
const rivers = RIVERS.map(r => { let d=''; r.forEach(([lo,la],i)=>{ const [x,y]=P(lo,la); d += (i?'L':'M')+round(x)+' '+round(y)+' '; }); return d.trim(); });
const lakes = [[98.85,2.65,.28,.14]].map(([lo,la,rx,ry]) => { let d=''; for (let i=0;i<24;i++){ const a=i/24*Math.PI*2; const [x,y]=P(lo+Math.cos(a)*rx, la+Math.sin(a)*ry); d += (i?'L':'M')+round(x)+' '+round(y)+' '; } return d+'Z'; });
provinces.sort((a,b)=>a.id-b.id);
const out = {mapVersion:3,projection:'cylindrical-equal-area',geo:B,legacyTransform:previous.legacyTransform, W: round(W), H: round(H), coast, provinces, nations, rivers, lakes, adj, edges, straits };
fs.writeFileSync('data/map-data.json', JSON.stringify(out));
console.log('provinsi:', provinces.length, 'W', W.toFixed(1), 'H', H.toFixed(1), 'bytes', JSON.stringify(out).length);
