# Nusantara 1350

Game strategi bergaya Europa Universalis 4, berlatar Nusantara era Majapahit (1350). Satu file HTML (canvas 2D, tanpa framework), ramah HP, UI Bahasa Indonesia.

**Fitur:** peta ±130 provinsi, ekonomi & pinjaman & inflasi, tenaga manusia, bangunan, teknologi, lembaga & ide nasional, agama & misionaris, diplomasi dengan diplomat, perang kompleks (suplai, pengepungan, pertempuran multi-hari, koalisi), event acak, suara gamelan.

## Main
Buka `index.html` di browser (atau situs GitHub Pages repo ini). Save otomatis di localStorage.

## Pengembangan
```bash
node tools/make.mjs        # src/template.html + data/map-data.json -> index.html
npm install && node tools/build-map.mjs   # hanya jika mengubah tools/seeds.mjs (peta)
pip install playwright && python3 tests/t22.py   # tes (butuh Chrome)
```
Edit **src/template.html**, bangun ulang, commit keduanya. Jangan edit `index.html` langsung.

## Struktur
- `src/template.html` — seluruh game
- `data/` — data peta hasil generator
- `tools/` — build & generator peta
- `tests/` — tes Playwright
- `docs/RISET.md` — riset EU4 & sejarah; `docs/RENCANA.md` — rencana Tahap E–H

## Deploy
Settings → Pages → Deploy from branch `main` / root.

**Penting untuk AI/kontributor:** baca `AGENTS.md` dulu.
