// Menyisipkan data peta ke template dan menulis index.html (jalankan dari root repo: node tools/make.mjs)
import fs from 'fs';
const tpl = fs.readFileSync('src/template.html', 'utf8');
const data = fs.readFileSync('data/map-data.json', 'utf8');
fs.writeFileSync('index.html', tpl.replace('__MAP__', () => data).replace('__EAST_ASIA__',()=>fs.readFileSync('data/east-asia.json','utf8')).replace('__WORLD_SYSTEMS__',()=>fs.readFileSync('src/world-systems.js','utf8')));
console.log('ok', fs.statSync('index.html').size);
