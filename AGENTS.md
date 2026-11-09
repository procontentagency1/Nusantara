# AGENTS.md — Panduan untuk AI / developer yang melanjutkan proyek ini

Dokumen ini adalah serah-terima lengkap. Baca seluruhnya sebelum mengubah kode. Untuk riset EU4 dan sejarah lihat `docs/RISET.md`; untuk rencana tahap berikutnya lihat `docs/RENCANA.md`.

## 1. Apa proyek ini

**Nusantara 1350** adalah game strategi grand-strategy bergaya **Europa Universalis 4 (EU4)**, berlatar Nusantara pada era Majapahit (mulai 1 Januari 1350). Dimainkan di HP (utama) dan desktop. Seluruh game adalah **satu file HTML** (canvas 2D, JavaScript klasik, tanpa framework, tanpa backend). Pemain memilih satu kerajaan, mengelola ekonomi, tenaga manusia, bangunan, teknologi, diplomasi, agama, dan berperang di peta ±130 provinsi.

- Pemilik proyek: **Ardy** (Ardy Studio, Indonesia). Dia bukan programmer penuh; dia merancang lewat percakapan dan menguji di HP.
- Versi hidup: artifact Claude "Nusantara 1350 · Peta Majapahit" (publik); setelah GitHub Pages aktif, situs resmi = URL Pages repo ini.
- Repo: https://github.com/procontentagency1/Nusantara

## 2. Aturan kerja dengan pemilik (WAJIB diikuti)

- **Bahasa:** balas dalam **Bahasa Indonesia**, santai ("bro" boleh), singkat. Bahasa Inggris hanya untuk istilah teknis. Semua teks di dalam game juga Bahasa Indonesia.
- **Bangun bertahap.** Satu tahap kecil, bisa dimainkan dan dites sendiri, baru lanjut. Jangan membangun semuanya sekaligus.
- **Tiru EU4 bila ragu.** Riset cara kerja di EU4 dulu (wiki `eu4.paradoxwikis.com`), lalu sederhanakan secukupnya.
- **UI kecil, rapi, tidak ramai.** Mobile dulu (layar ±780×360 landscape sampai portrait HP). Tombol cukup besar untuk jari. Bandingkan dengan gambar referensi yang diberikan pemilik.
- **Selalu tes sebelum lapor** (lihat bagian 9) dan cek visual lewat screenshot ukuran HP.
- **Jujur soal batas:** sebut apa yang belum dites di HP sungguhan, dan apa yang belum diimplementasikan.
- Jangan mengubah gaya visual (tema kerajaan Indonesia: merah bata, emas, batik/kawung, ornamen kain) tanpa diminta.

## 3. Arsitektur dan build

```
src/template.html     SUMBER KEBENARAN. Semua CSS, HTML, JS game (±3150 baris). Berisi placeholder __MAP__.
data/map-data.json    Data peta hasil generator (provinsi, bangsa, sungai, danau, tetangga, selat). ±340 KB.
data/icons.json       Ikon kecil.
tools/make.mjs        Menyisipkan map-data.json ke __MAP__ lalu menulis index.html di root.
tools/build-map.mjs   Generator peta: world-atlas + d3-geo + Delaunay + polygon-clipping -> data/map-data.json.
tools/seeds.mjs       112 baris seed: [nama, lon, lat, bangsa, status, medan, rank] + laut. Edit ini untuk mengubah provinsi.
index.html            HASIL BUILD (±580 KB). Jangan diedit tangan. Ini yang dipublish / dilayani GitHub Pages.
tests/*.py            Tes Playwright (Python) yang memainkan game di Chrome headless.
docs/                 Riset dan rencana.
```

Perintah (dari root repo):

```bash
npm install                 # hanya perlu untuk build:map
node tools/make.mjs         # = npm run build -> menulis index.html
node tools/build-map.mjs    # hanya bila seeds/peta berubah -> data/map-data.json
```

**Alur kerja yang benar:** edit `src/template.html` -> `node tools/make.mjs` -> jalankan tes -> commit `src/template.html` DAN `index.html` bersama.

Catatan teknis penting:
- Skrip game adalah **script klasik** (bukan module). Fungsi top-level adalah global dan bisa di-reassign untuk menimpa/menyambung perilaku (pola "wrapper": `const _x = fn; fn = function () { ...; return _x(); }`). Ada beberapa pola begini di blok "kait ke fungsi lama".
- Deklarasi `let`/`const` ganda di level top-level = **SyntaxError yang mematikan seluruh skrip** (layar kosong). Cek nama sebelum menambah (`grep -c "\bnama\b" src/template.html`). Contoh nama yang SUDAH dipakai: `FX` (partikel; efek event memakai `EF`), `lim`, `clamp01`, `row`, `btn`, `hd`.
- Tes memakai `file://` ke `index.html`, jadi tidak perlu server.
- `__MAP__` diganti dengan fungsi (`replace('__MAP__', () => data)`) supaya karakter `$` di JSON tidak ditafsirkan.

## 4. Peta template.html (blok berdasarkan komentar `/* ---------- ... ---------- */`)

| Blok | Isi |
|---|---|
| (awal) | CSS (beberapa lapisan override berurutan: base, tema Indonesia, "v20 kontrol waktu HP", "v21 event"), markup `#app`, `#top`, `#rail`, `#win`, `#prov`, `#modal`, `#toasts`, dll. |
| data | `DATA` (peta), `PROV`, `NATS`, `RELIG`, `GOODS`, `BUILD`, `TECH_*`, `SAVE_KEY`, `MONTHS`, `MDAYS` |
| state | `newGame(nat)`, `econ()` (ekonomi bulanan), `devCost`, `slotsOf` |
| time | `dayTick`, `monthTick`, `saveGame`, `loadSave`, `toast` |
| top bar | chip sumber daya, `updateTop()`, kontrol waktu (play/pause + dropdown kecepatan) |
| windows | `renderWin()` + `provHTML`, jendela kerajaan/ekonomi/tech/militer dst; `row()`, `btn()`, `hd()` pembangun HTML |
| actions | objek `act` (handler tombol berdasarkan `data-act`) |
| hubungan / perang struktur | `rel`, `atWar`, `warScore`, `addLog` |
| peristiwa (modal) | `pushEvent`, `showEvent`, objek `EVA` (aksi pilihan modal). `G.ev` = antrean modal |
| pasukan | `mkArmy`, `orderMove`, `pathTo`, `armiesDay`, `occupy`, pengepungan dasar |
| AI | `aiArmies`, `aiMonth`, `declareWar`, `applyPeace`, `diplomacyMonth`, `dipChance`, `availableCBs`, `claimable` |
| gambar pasukan, UI pasukan/perang/diplomasi | render peta pasukan, jendela perang/damai/diplomasi |
| map interaction | gestur geser/cubit/ketuk (`onMapTap`), seleksi, `deselectArmy` |
| partikel, sprite, interpolasi, pengepungan fx, pertempuran di peta, lapisan bawah, ambient | semua animasi canvas (api, panah, asap, awan, kilau laut). Array partikel bernama `FX` |
| panel ringkasan pertempuran, spanduk | UI hasil perang |
| kait ke sistem lama + war2 | `wexOf/AE/coalition/fab/supply/attrition`, `claimCost`, `siegeNeed`, `war2Month` (sistem perang kompleks) |
| diplomat (dipl) | `dipMax`, `dipFree`, `MIS_KIND`, `sendDiplomat`, `misArrive`, `misDay`, `netOf/netCost`, `drawEnvoys` |
| Tahap A+B | ekonomi, pinjaman, inflasi, bangkrut, modifier (`G.mod`), flag, **mesin event** (`EVT`, `defEvent`, `fireEvent`, `EF`) |
| Tahap C | agama (`RELS`, toleransi, `unity`, misionaris, Islam menyebar) |
| Tahap D | tech (`techBreak`), lembaga (`INST`), ide nasional (`IDEAS`) |
| start screen | pilih negara, lanjut/mulai, `beginGame` |
| suara | sintesis WebAudio bernuansa gamelan (`SFX`), musik latar |

Untuk menemukan sesuatu: `grep -n "function namaFungsi" src/template.html`.

## 5. Model data dan state

### 5.1 Data statis
- `DATA` = isi `map-data.json`: `provinces` (id, nama `n`, jenis `k` = `L` darat / `S` laut, medan `t` = plains/coast/jungle/mountain, status `st`, bangsa asal `nat`, posisi label `lab`, rank `r`), `nations`, `adj/edges/straits` (tetangga; `LINK[id]` = daftar `{to, strait}`), sungai, danau.
- `NATS[nama]`: `ids` (provinsi awal), `capital` (objek provinsi), `ruler {name,a,d,m,real}`, `relig`, `gov`, `title`, `rank`, `dev`.
- `PROV[id]`; `OWNR[id]` pemilik sekarang; `CTRL[id]` pengendali (bila diduduki); `BASE_OWN` pemilik awal; `OWNED[nat]`.
- Saat ini ±69 bangsa dan 112+ provinsi darat (peta seluruh Nusantara + sekitarnya).

### 5.2 State permainan `G` (disimpan ke `localStorage['nusantara1350_save_v2']` sebagai JSON)
`nat` (negara pemain), `y/mo/d` tanggal (mulai 1350-Jan-1), `treasury`, `mana[3]` (ADM/DIP/MIL), `stab` (-3..+3), `prestige` (-100..100), `legit` (0..100), `tech[3]` (mulai 3, maks 32), `mp` (tenaga), `regs` (resimen), `pv[id]` (`{t,p,m,bld[],cons[],nc?}` = pajak/produksi/tenaga dasar, bangunan jadi/dibangun, bulan belum inti), `armies[]`, `wars[]`, `rel` (hubungan antarnegara), `al` (aliansi), `mar` (pernikahan), `acc` (akses militer), `truce`, `claims[]`, `subj` (vasal), `imp` (improve relations), `siege`, `battles`, `wex` (war exhaustion), `ae` (agresi ekspansi), `coal` (koalisi), `fab[]` (klaim sedang difabrikasi), `mis[]` (diplomat), `net` (jaringan diplomat per negara), `ev[]` (antrean modal), `log[]`, `nid`, `sel`.
Tahap A–D menambah: `flags{}`, `mod[]` (modifier), `fired[]` (event sekali-jalan), `evq[]` (event tertunda `{id,at}`), `evx{}` (data sementara event), `infl`, `ln[]` (pinjaman `{a,left}`), `loans` (= jumlah `ln`, dijaga `syncLoans`), `bank` (sisa bulan bangkrut), `pr{id:kunciAgama}`, `rs` (agama negara), `miss[]` (misionaris `{pid,p}`), `inst{}` (lembaga), `ideas[]`.

**Kompatibilitas save:** setiap field baru WAJIB diberi default di `fixSave()` / `fixRel()` (dipanggil di `newGame` dan saat Lanjut). Tanpa itu save lama rusak. Jangan menaikkan `v` tanpa migrasi.

## 6. Mekanisme (cara kerja yang sudah ada)

### 6.1 Waktu
`dayTick()` memajukan 1 hari: pasukan, perang, diplomat. Saat ganti bulan memanggil `monthTick()`. 5 kecepatan (×1..×5), tombol play/pause besar, dropdown kecepatan. Game berhenti otomatis saat modal event muncul.
`monthTick()` urutan: `econ()` -> kas += saldo -> `ecoMonth()` (pinjaman jatuh tempo, bangkrut) -> mana += -> tenaga -> bangunan -> penyusutan prestise tiap Januari -> `diplomacyMonth/aiMonth` -> `modMonth, relMonth, instMonth, evMonth` -> simpan otomatis.

### 6.2 Ekonomi (`econ()`)
- Pajak = Σ(pajak dasar × faktor agama) × 0,09 × (1+0,04×(tech ADM−3)) × (1+0,03×stab) × (1+mod.tax).
- Produksi = Σ(produksi × harga barang `GOODS` × faktor agama) × 0,04 × (1+0,04×(tech DIP−3)) × (1+0,03×stab) × (1+mod.prod).
- Pengeluaran: pasukan `regs×0,2×(1+kelebihan/forceLimit)×inflasi×(1+mod.army)`, misionaris 5 dukat/tahun/misionaris, bunga pinjaman.
- Mana per bulan = 3 + skill penguasa (+ mod.adm/dip/mil). Tenaga maks = (1+Σtenaga×0,25)×(1+0,05×(tech MIL−3))×(1+mod.mpmax); pulih /120 per bulan; 0 saat bangkrut.
- **Pinjaman:** ukuran = max(20, ½ total development); maks 5; bunga 4%/tahun (+1% per poin stabilitas negatif, +5% bangkrut, +mod.int); tiap pinjaman +0,5% inflasi; 60 bulan; saat jatuh tempo dilunasi otomatis bila kas cukup, jika tidak diperpanjang 5 tahun (+0,5% inflasi).
- **Inflasi** `G.infl` (%): mengalikan biaya pasukan, bangunan (`bCost`), rekrut (`recCost`). Turun 1% dengan 50 ADM.
- **Bangkrut:** kas minus & pinjaman penuh -> pinjaman dihapus, inflasi ×0,75, 60 bulan: tenaga tidak pulih, biaya tech +50%, bunga +5%. (Penalti moral dan biaya penasihat dari EU4 BELUM diimplementasikan.)
- Pembangunan: Kuil (+1 pajak), Pasar (+1 produksi), Barak (+1 tenaga); slot per provinsi `slotsOf`.
- Development: naikkan pajak/produksi/tenaga dengan mana (`devCost = 50+5×level`).

### 6.3 Modifier, flag, event (mesin Tahap A)
- `addMod(id, nama, bulan, fx)`; `bulan = -1` permanen. `fx` kunci: `tax prod army mp mpmax tech int adm dip mil dipl tolT tolH tolN misn`. `modSum(k)` menjumlahkan. Modifier berakhir sendiri (`modMonth`).
- `setFlag(k, bulan)`, `hasFlag(k)`.
- Event didefinisikan dengan `defEvent({id, t, x, mtth?, once?, cond?, o:[{l, tip, fx}]})`:
  - `t` judul, `x` teks (string atau fungsi), `mtth` = rata-rata bulan sampai muncul (peluang bulanan `1-0.5^(1/mtth)`), tanpa `mtth` = hanya dipicu (`EF.fire`, `EF.fireIn(id, bulan)`, atau misi nanti).
  - `once` default **true** (dicatat di `G.fired`); isi `once:false` untuk event berulang.
  - `cond()` syarat; `o[]` pilihan: `l` label, `tip` ringkasan akibat (tampil kecil di bawah label), `fx()` efek.
  - Maksimal 1 event acak per bulan. Modal pakai antrean `G.ev` dan `EVA.gev`.
- Efek siap pakai `EF`: `gold, mana(i,n), stab, prestige, legit, infl, mod, flag, fire, fireIn`. `grossInc()` = pendapatan kotor bulanan untuk menskalakan hadiah.
- Event bawaan sekarang: `panen_raya`, `wabah_pesisir`, `saudagar_asing`, `keluhan_bupati`, `islam_menyebar`. **Event sejarah belum ada** (Tahap F).
- Debug di konsol: `fireEvent('id')`.

### 6.4 Agama (Tahap C)
- Agama: `siwa` (Siwa-Buddha), `hindu`, `mahayana`, `thera`, `islam`, `animis`; rumpun `dharma` / `muslim` / `pagan` (`RELS`). Provinsi punya agama sendiri di `G.pr[id]` (awal dari bangsa asal); tetap saat direbut.
- Toleransi: iman sendiri 3 (+1 Siwa/Hindu); bidaah (rumpun sama) 0 (+1 untuk Siwa-Buddha); kafir (rumpun lain) −1; modifikasi lewat mod `tolT/tolH/tolN`.
- Toleransi negatif: pajak & produksi provinsi −10% per poin (min ×0,5) lewat `relFac(id)` di `econ()`.
- `unity()` = persentase development beragama negara (non-iman menyumbang 25/50/75/100% sesuai toleransi 0/≤1/≤2/>2; negatif 0). Biaya stabilitas `stabCost() = 100×(1+(100−unity)/100)`.
- `unrestOf(id)` hanya tampil sebagai angka (keresahan = −1,25×toleransi negatif + 6 bila ada misionaris). **Belum memicu pemberontak** (Tahap H).
- Misionaris: `misMaxR()` = 1 (+1 bila ADM penguasa ≥5). Kirim dari jendela provinsi; progres bulanan `misStr()` = 2 + 0,5×stab positif + mod.misn (+1 bila rumpun sama); 100% = provinsi pindah ke agama negara.
- Ganti agama negara (`chRel`): 150 ADM, stabilitas −2, mod pajak −10% 24 bulan; hanya ke agama yang ada di provinsimu.
- Islam menyebar: provinsi pesisir AI dengan tetangga Islam pindah pelan setelah 1380 (`relMonth`); untuk provinsi pemain lewat event `islam_menyebar` dengan 3 pilihan.

### 6.5 Teknologi, lembaga, ide (Tahap D)
- 3 jalur (ADM/DIP/MIL), level 3..32, beli dengan mana jalur yang sama. `techBreak(i)`: biaya = max(30, 600×(1 + lembaga + waktu + lebihCepat − tetangga − ide + lain)).
  - lembaga: +25% per lembaga yang sudah muncul tapi belum diadopsi.
  - waktu: 0..30% linear dari `techYear(level)`; `techYear(L) = 1350 + 13×(L−3)`.
  - lebihCepat: +10% per tahun jika `techYear(level sekarang) > tahun game`.
  - tetangga: −5% per tingkat tertinggal dari `aiTech() = 3 + floor((tahun−1358)/14)` (maks −75%).
  - ide: −2% per ide; lain: `mod.tech` + 50% saat bangkrut.
  - Efek level: +4% pajak (ADM), +4% produksi (DIP), +5% tenaga & force limit (MIL) per level.
- Lembaga (`INST`): Pelayaran Jung (1400, asal ibu kota Majapahit, +10% produksi), Meriam & Mesiu (1450, asal ibu kota Samudra, +10% tenaga & force limit), Pasar Samudra (1500, asal ibu kota Malayu, +10% pajak). Menyebar tiap bulan ke tetangga darat (`.05×(1+dev/25)`). Adopsi: butuh ≥10% development pemain terkena; biaya `0,8 × dev yang belum terkena` dukat (min 20, ×inflasi).
- Ide nasional (`IDEAS`, 7 + Ambisi): dibuka berurutan, biaya `150+100n` mana jenis tertentu; slot `1 + floor((Σtech−9)/3)`. Majapahit punya nama sendiri (`IDEA_NAME`). Ide diterapkan sebagai modifier permanen `idea0..6`.

### 6.6 Diplomasi (`dipl` + `war2`)
- **Diplomat terbatas:** `dipMax() = 2 + (DIP penguasa ≥5 ? 1 : 0) + floor((tech DIP−3)/3) + mod.dipl`; `dipFree() = dipMax − misi aktif`.
- Misi `MIS_KIND`: `ally, marry, access, gift, improve, net`. Diplomat harus **berjalan dulu** (`travelDays` 12–90 hari menurut jarak ibu kota), tiba (`misArrive`), bekerja/langsung selesai, lalu pulang. Peluang `dipChance`. Marker diamond di peta (`drawEnvoys`).
- **Klaim wajib lewat "jaringan diplomat"** (`G.net[negara]`, 0–100): misi `net` menambah +0,5/hari; meluruh −1/bulan bila tak ada diplomat. Fabrikasi klaim butuh `netOf ≥ netCost` (30 + 10 × klaim yang sudah dimiliki atas negara itu) + mana DIP; hasilnya `G.fab` 8–30 bulan.

### 6.7 Perang (kompleks, gaya EU4)
- Pertempuran **multi-hari** di peta (fase tembak, adu, dadu), dengan animasi dan panel ringkasan; kepungan berfase (tiap 10 hari lempar dadu, `siegeNeed`); atrisi suplai (`supplyLim`, `attritionMonth`); kelelahan perang `wex`; agresi ekspansi `ae` dan koalisi `coal`; skor perang harus menduduki provinsi (`warScore`, `occVal`); biaya perdamaian (`provCost`, `autoDemands`); provinsi yang dicaplok butuh dijadikan inti (`coreCost`, `q.nc`).
- AI: `aiMonth`, `aiArmies`, `aiAccept`, `aiPeace`, `declareWar` memakai casus belli `availableCBs`; AI menawar damai ke pemain (`aiOffersToMe`).
- Catatan jujur: keseimbangan perang belum diuji panjang oleh pemain sungguhan.

### 6.8 UI
Bilah atas (kas, tenaga, ADM/DIP/MIL, stabilitas, ...), rail kiri (Kerajaan, Ekonomi, Teknologi, Militer, Diplomasi, Perang, Menu), jendela `#win` (kiri, 272 px), jendela provinsi, modal event `#modal`, toast kanan atas, minimap, tombol "✕ Batal pilih pasukan". Jendela baru dibuka lewat `act.win` dengan `data-w`: `nation, econ, tech, mil, dip, dipn, war, peace, rel, ide, prov, army, menu`. Tambah jendela baru = tambah cabang di `renderWin()` + fungsi `xxxHTML()`.
Pola HTML jendela: `hd(judul, sub) + row(label, nilai) + btn(label, 'aksi', {data}, enabled)`; aksi didaftarkan di objek `act`. Setelah aksi, `updateTop()` dan `renderWin()` dipanggil otomatis.

### 6.9 Render dan performa
Satu kanvas peta. Tekstur peta dirender terpisah ("detail render") dan dipakai ulang; timer idle merender detail hanya bila kunci tampilan (`tx|ty|s|mode|cacheVer|lebar`) berubah (perbaikan peta buram). Jangan menggambar per-frame sesuatu yang berat; pakai `request()` untuk meminta frame.

### 6.10 Suara
`SFX` memakai WebAudio: sintesis gong, bonang, kendang, tiupan tanduk; musik gamelan latar. `SFX.play('nama')` (mis. `event`, `alert`, `win`, `lose`, `horn`). Suara aktif setelah gestur pertama pengguna.

## 7. Cara menambah konten

- **Event:** salin salah satu `defEvent` di blok Tahap A+B; beri `id` unik; `mtth` atau dipicu; efek lewat `EF`. Uji dengan `fireEvent('id')`.
- **Modifier:** `EF.mod('id','Nama',bulan,{tax:.05})`. Tambah kunci `fx` baru: tambahkan `modSum('kunci')` di tempat efeknya dipakai (biasanya `econ()`), dan label di `LB` pada `econHTML`.
- **Ide / lembaga / agama:** edit `IDEAS`, `INST`, `RELS` (+ `relKey` untuk memetakan teks `RELIG`).
- **Provinsi / bangsa:** edit `tools/seeds.mjs`, jalankan `node tools/build-map.mjs` lalu `node tools/make.mjs`.
- **Kolom state baru:** beri default di `fixSave`/`fixRel`.

## 8. Jebakan yang pernah terjadi
- Nama ganda `let/const` -> layar kosong. `FX` sudah dipakai partikel.
- Mengubah `econ()` memengaruhi bilah atas, jendela ekonomi, dan AI; tes setelah mengubah.
- Fungsi yang dipanggil sebelum `G` ada (mis. dari menu awal) harus aman terhadap `G` kosong (lihat `modSum`).
- `publish`/deploy: selalu build ulang `index.html` sebelum commit.
- Peta buram dulu disebabkan timer idle yang terus di-reset; jangan hapus `idleKey`.
- Klaim sempat bisa dibuat tanpa diplomat; kini harus lewat jaringan diplomat (`act.dact`).

## 9. Pengujian

Tes memakai Playwright Python + Chrome (`/usr/bin/google-chrome`, `--no-sandbox`). Jalankan dari **root repo** (`index.html` harus sudah dibangun):

```bash
pip install playwright     # lalu pastikan ada Chrome, atau ubah executable_path di tes
python3 tests/t22.py       # agama, tech, lembaga, ide, event Islam, save/load
python3 tests/t21.py       # event, pinjaman, inflasi, bangkrut, kompatibilitas save
python3 tests/t17.py       # regresi: simulasi 8 tahun perang AI
python3 tests/t18.py       # kontrol waktu, blur, misi diplomat
python3 tests/t19.py       # klaim butuh jaringan diplomat
python3 tests/t20.py       # deselect pasukan
python3 tests/shot_windows.py   # screenshot jendela (z_*.png) untuk cek visual HP
```
Semua tes harus mencetak `[]` untuk daftar `pageerror`. Tes memanggil fungsi game langsung lewat `page.evaluate` (mis. `selectNation('Majapahit')`, `fireEvent('x')`, `monthTick()`).
Tambah tes baru dengan pola yang sama; cek **screenshot** untuk semua UI baru pada viewport 780×360 (`device_scale_factor=2`).

## 10. Rencana (ringkas; rincian di `docs/RENCANA.md`)

Selesai: peta, kota, ekonomi, bangunan, militer, tech, perang/diplomasi/AI, tema Indonesia, suara, animasi, perang kompleks, diplomat+jaringan, **Tahap A+B** (event, ekonomi), **Tahap C** (agama), **Tahap D** (tech/lembaga/ide).
Berikutnya, berurutan:
- **E. Misi** — pohon misi per negara (Majapahit 12 misi, 3 cabang paralel; negara lain 4–6 generik), hadiah klaim/modifier/mana.
- **F. Event sejarah** — 8–10 event Majapahit (Bubat, wafatnya Gajah Mada, Paregreg, Islam, Pasai/Malaka, Demak, kejatuhan Majapahit) + event generik tambahan.
- **G. Dagang** — 5–8 node, kekuatan dagang provinsi, merchant terbatas, rempah Maluku.
- **H. Lain-lain** — angkatan laut, pemberontak (memakai keresahan), penyeimbangan, ornamen layar judul (belum ada), mode peta agama.

Keputusan desain yang diasumsikan (belum dikonfirmasi pemilik): event sejarah boleh menyimpang bila kondisi berubah; misi paralel per cabang; hadiah kecil & seimbang; lembaga hanya 3–4 buatan sendiri.

## 11. Batasan yang diketahui
- Belum dites di HP sungguhan (hanya viewport emulasi).
- Keseimbangan (jumlah diplomat, kecepatan jaringan, biaya, pinjaman, perang) belum diuji oleh pemain dalam sesi panjang.
- Belum ada: angkatan laut, pemberontak, event sejarah, misi, dagang, mode peta agama, penalti moral saat bangkrut, ornamen judul di layar mulai.
- Nama dan kemampuan beberapa penguasa masih contoh (`ruler.real` false).
- Save hanya di browser perangkat itu (localStorage); berganti alamat situs = save tidak terbawa.

## 12. Deploy (GitHub Pages)
`index.html` di root adalah situs. Aktifkan Settings -> Pages -> Deploy from branch `main` / folder `/ (root)`. Update = `node tools/make.mjs`, commit, push.

## Pembaruan sesi: event dan deklarasi perang
- Misi sudah tersedia (12 Majapahit / 6 generik). Event berjumlah 39: 8 sejarah sekali, 7 generik awal, 24 tambahan. Rincian skenario dan batas ada di docs/RISET.md.
- `WAR_DRAFT`, `openDeclaration`, `declarationHTML`: persiapan terpisah dari konfirmasi. `w.goal` adalah sasaran tunggal ticking score; `w.goals` tetap daftar tuntutan berklaim untuk biaya perdamaian.
- `interceptArmies` menangkap pasukan lawan di ruas berlawanan. `resolveBattles` juga berjalan sebelum gerak harian.
- Fabrikasi klaim sekarang langsung memakai jaringan, tanpa mana DIP; antrean save lama tetap ditangani `war2Month`.
- Tes HTTP Chromium tambahan: `tests/t23_missions.py`, `tests/t24_history.py`, `tests/t25_war_events.py`. Jalankan dari root repo.

## Pembaruan hubungan bawahan
`G.subj` hanya vasal; `G.tributaries` menyimpan penguasa negara upeti; `G.subjectData` metadata. Panggil `setSubject` saat membentuk hubungan, `fixSubjects` pada migrasi. `subjectBudget` diterapkan di wrapper ekonomi terakhir; `subjectsMonth` menangani upeti, LD dan integrasi. `w.independence` menjaga pemulihan vasal saat pemberontak kalah. Akses panel dari Kerajaan → Bawahan. Tambahkan pengujian `tests/t26_subjects.py` saat mengubah diplomasi, ekonomi atau perang. Jangan menggabungkan tributary dalam `subjectsOf` atau syarat kepemilikan misi.

## Pembaruan perdagangan
`G.trade={home,merchants[]}`; merchant menyimpan node/mode/to/left. `fixTrade` migrasi, `tradeDay` perjalanan, `tradeSnapshot` menghitung seluruh jaringan secara murni tanpa menulis kas. `subjectBudget` menggabungkan e.trade ke e.net; jangan menambah kas dari panel UI. Graph TRADE_NODES harus urutan topologis, rute tanpa siklus. Properti `raw` adalah kekuatan provinsi sebelum merchant/penalti. `trade` pada modifier adalah tambahan efisiensi, bukan nilai lokal produksi. Gunakan tests/t27_trade.py saat mengubah ekonomi/rute/perjalanan. Sistem ini belum punya kapal dagang/blokade.

## Pemulihan pasukan AI
`repairBattleLocks` berjalan sebelum gerak harian dan setelah damai. `aiReturnHome` memilih wilayah sendiri dan merencanakan rute, termasuk `distMap(...,true)` khusus pulang tanpa akses. `a.exiled` mencegah pertempuran, kepungan dan atrisi selama pulang; dihapus saat masuk wilayah sendiri. Jangan memberi akses militer global dari flag ini. `a.returning` mencegah pembatalan rute oleh logika vasal tak setia. Penggabungan/rekrut bulanan harus mengecualikan `a.bt`. Pengujian: tests/t28_ai_recovery.py.

## Skala pasukan dan bangunan regional
Gunakan armyVisualScale untuk pasukan peta dan pertempuran; ARM_HIT/BT_HIT harus mengikuti transformasi yang sama. outlinedUnit memakai WeakMap dari sprite asli ke sprite ber-outline. CITY_STYLE_GROUPS/cityStyle hanya untuk arsitektur; jangan mengganti REGIONAL_STYLE karena dipakai busana dan klasifikasi perdagangan. tests/t29_visual_scale.py mengukur lebar gambar aktual dan hitbox pada enam zoom serta memastikan seluruh negara mendapat gaya eksplisit.

## Audit, teknologi, dan sumber daya
`npm test` menjalankan tests/run_all.py: HTTP lokal, browser tersedia, legacy smoke dan assertion t23+. Rincian audit dan batas ada di docs/AUDIT.md. Event button memiliki token uid; jangan konsumsi event dari tombol lama. Perdamaian menuntut pendudukan, bukan klaim saja. G.resourceStocks/G.improvements menyimpan stok negara/pengolahan provinsi; fixResources migrasi, resourcesMonth sekali per bulan. e.supplyCost masuk anggaran. Rekrut mulai MIL 4 membutuhkan besi pemain. Pengolahan tidak boleh dihapus ketika transferProv. worldLog memisahkan keputusan AI dari catatan pemain. Ahead-of-time memakai tahun target tingkat teknologi.

## Kesiapan militer dan riset armada
`fixMilitary` migrasi G.maintenance/G.professionalism dan a.morale/drill. mkArmy memberi default langsung karena dipanggil sesudah fixSave saat newGame. `militaryMonth` latihan/pemulihan; `blendReadiness` wajib saat gabung/rekrut agar kesiapan tidak dibuat ulang. sideStats/endBattle membawa moral masuk/keluar pertempuran. Lebar tempur membatasi damage, belum ada komposisi atau baris resimen. tests/t33_military_audio.py memeriksa biaya, kesiapan, migrasi, damage dan gain suara. Rancangan kapal serta batas implementasi ada di docs/ARMADA_DAN_PASUKAN.md; armada belum diimplementasikan. Jangan memblokir hubungan selat sebelum transportasi/AI laut berfungsi.

## Siklus penaklukan dan integrasi
Kontrak angka/batas di docs/EKSPANSI.md. `G.cores` menyimpan inti dinamis; gunakan hasCore untuk reconquest. transferProv mempertahankan arsip development/bangunan dan memanggil registerConquest; argumen peaceful=true untuk integrasi vasal/pemulihan negara. applyPeace wajib rebuildOwned sebelum cek alive/rute agar aneksasi penuh membersihkan tentara. `peaceExpansion` dipakai pratinjau dan debit DIP; jangan memberi wilayah dari tombol event tanpa memeriksa pendudukan lagi. `conquestMonth` mengganti inti otomatis: pemain membayar ADM untuk mulai 24 bulan, AI 36 bulan abstrak. `G.expansion` menyimpan separatisme/otonomi/perlawanan; perlawanan abstrak mematikan hasil dan bisa mengembalikan provinsi setelah timer, belum army pemberontak. provinceControl memengaruhi ekonomi; development mentah tetap utuh. `tests/t34_conquest.py` mencakup alur perang sampai vasal serta migrasi. Gencatan memakai snapshot peserta sebelum finishNationCheck membersihkan negara yang lenyap.

## Audio adaptif
Kontrak di docs/AUDIO.md. SFX mengelola satu AudioContext/scheduler, bus UI/efek/musik terpisah dan lapisan damai/perang/pertempuran dengan crossfade. Semua perkusi musik wajib menerima bus tujuan, bukan default fx. Suasana hanya mengikuti perang/pertempuran pemain; pause game tidak sama dengan suspend audio saat tab tersembunyi. nus_snd.levels menyimpan tiga volume terpisah dan memigrasi preferensi on/off lama. Jangan memakai Math.random gameplay untuk sintesis. Sumber audio wajib disconnect saat selesai dan tunduk pada batas suara/jeda. t35 mengukur keluaran tiga suasana, mute, preferensi dan lifecycle; t33 memeriksa gain klik tanpa mencampur parameter frekuensi.

## Armada awal dan penghapusan minimap
Kontrak di docs/ARMADA.md. `fixNavy` membuat G.fleets/G.shipQueue sekali pada kampanye baru/save lama tanpa field, memakai G.nid. portsOf memakai geometri pantai p.cd. Navigasi adalah mask air grid 8 satuan, jangan mengganti dengan garis langsung yang menyeberangi daratan. navyDay menangani gerak/pertempuran/AI, navyMonth perbaikan/antrean. e.navalCost masuk saldo dan daftar pengeluaran. tradeSnapshot memasukkan kekuatan kapal patroli yang benar-benar tiba/bertugas. drawFleets/FLEET_HIT memakai posisi dan skala sama. Armada bersandar aman; mundur tidak bisa menyerang. Minimap dan handler/render-nya sudah dihapus; satu dropdown #mapviews mengatur lima MAP_VIEWS. Saat mode berubah, cache warna provinsi wajib dibersihkan. t36 menguji kapal dan kontrol view; t27 mencakup biaya laut pada identitas anggaran. Angkutan tentara/blokade/laksamana belum tersedia.
