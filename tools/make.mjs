// Menyisipkan data peta ke template dan menulis index.html (jalankan dari root repo: node tools/make.mjs)
import fs from 'fs';
const tpl = fs.readFileSync('src/template.html', 'utf8');
const data = fs.readFileSync('data/map-data.json', 'utf8');
fs.writeFileSync('index.html', tpl.replace('__MAP__', () => data));
console.log('ok', fs.statSync('index.html').size);
