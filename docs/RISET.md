<!-- Salinan faithful dari dokumen riset (Docs artifact 'Riset Misi & Event — Nusantara 1350') per 2026-11-09. Bagian 1-4. -->
# Riset Misi & Event — Nusantara 1350

 · 

Misi di EU4 adalah pohon tugas dengan syarat dan hadiah tetap, sedangkan event adalah kejadian acak atau terpicu yang memberi pilihan. Dokumen ini merangkum cara kerjanya, sejarah Majapahit 1350–1450, dan rancangan misi serta event untuk game kita.

## Cara kerja misi di EU4

Misi EU4 (sistem sejak versi 1.25) adalah pohon tugas: tiap misi punya syarat selesai dan hadiah, dan misi baru baru terbuka setelah misi prasyaratnya selesai.

- Struktur: misi dikelompokkan dalam series yang menempati satu kolom (slot) dan baris (tier). Panah hanya vertikal atau horizontal, jadi prasyarat bisa di baris mana pun di atasnya dalam kolom yang sama, atau di kolom mana pun pada baris tepat di atasnya.
- Siapa dapat apa: tiap series punya syarat potential yang dicek saat game mulai atau saat negara dibentuk. Misi khusus negara menimpa misi generik di slot yang sama.
- Tiga cabang generik: militer, diplomasi, dan ekonomi, untuk semua negara tanpa pohon sendiri.
- Komponen satu misi: ikon, required_missions, trigger (syarat selesai, dicek terus), effect (hadiah), dan provinces_to_highlight (provinsi yang disorot di peta saat kursor di atas misi).
- Hadiah khas: poin monarki, klaim permanen atas satu area, modifier negara berdurasi (misalnya 25 tahun), prestise, atau event lanjutan yang memberi pilihan cabang.
- Pola desain yang sering dipakai: bangun ibu kota → dapat klaim → taklukkan area klaim itu → dapat bonus → jadi rival kekuatan besar.

Kelemahan yang diakui Paradox sendiri: pohon yang kaku membuat misi klaim rentan urutan (menaklukkan "dalam urutan salah" bisa kehilangan hadiah), dan misi generik lebih sulit dirancang serta kurang seru dibanding pohon unik per negara. Sebelum 1.25, EU3/EU4 memakai satu misi acak per waktu, yang sering dikeluhkan terlalu bunuh diri atau tak masuk akal.

Pelajaran untuk game kita: pohon kecil (8–15 misi) per negara besar, dengan syarat yang bisa dicek dari data yang sudah kita punya, hadiah yang terasa, dan beberapa cabang pilihan supaya tidak linear.

## Cara kerja event di EU4

Event adalah jendela kejadian dengan judul, teks, syarat, dan beberapa pilihan. Dua cara munculnya:

| Jenis | Cara kerja |
|---|---|
| MTTH (acak) | Dicek tiap bulan selama trigger benar. mean_time_to_happen adalah waktu di mana peluang muncul 50%, bisa diubah modifier (faktor ×0,5 jika tahun tertentu, dst). |
| Triggered only | Hanya muncul bila dipanggil event/keputusan/misi lain, atau lewat pulse (on_action) yang memilih satu event dari daftar berbobot. |

- Bagian event: trigger, fire_only_once, immediate (efek langsung sebelum pemain memilih, mencegah curang), lalu 2–4 option.
- Option: tiap pilihan punya efek sendiri dan ai_chance agar AI memilih dengan bobot (contoh: 95/5 untuk reformasi vs alternatif).
- Rantai: satu option bisa memicu event lain beberapa hari kemudian, termasuk ke negara lain (target menerima/menolak).
- Event sejarah dinamis: event khusus negara dan tahun, jarang tapi berbobot, yang mengikat game ke sejarah (contoh Italian Wars, pembentukan reformasi).
- Bencana (disaster): syarat awal terpenuhi lalu peluang kecil naik seiring jumlah syarat; punya event mulai dan akhir.
- Kritik umum: event sejarah yang muncul tanpa sebab di timeline game terasa "rel kereta". Solusinya: syaratnya dihubungkan ke kondisi nyata di dalam game.

Pelajaran untuk game kita: event harus punya syarat dari state kita (stabilitas, perang, relasi, tahun), pilihan dengan trade-off nyata, dan pemicu berantai; jangan sekadar muncul karena tanggal.

## Sejarah 1350–1450 sebagai bahan skenario

Game mulai 1350, tahun Hayam Wuruk naik takhta dan Majapahit di puncak. Kerangka waktunya:

| Tahun | Peristiwa | Catatan untuk game |
|---|---|---|
| 1334/36 | Gajah Mada diangkat mahapatih, mengucap Sumpah Palapa | Dasar misi penyatuan Nusantara |
| 1343 | Bali (Bedahulu/Bedulu) ditaklukkan setelah sekitar tujuh bulan | Sudah dikuasai; basis penempatan wangsa di Bali |
| 1350 | Hayam Wuruk (16 tahun) naik takhta; serangan armada ke Samudra Pasai | Awal skenario |
| 1357 | Perang Bubat dengan Sunda: Dyah Pitaloka dan rombongan tewas | Event besar; relasi Sunda rusak; Gajah Mada diturunkan |
| 1365 | Nagarakretagama ditulis Mpu Prapanca; daftar daerah bawahan | Dasar daftar vasal/klaim |
| 1377 | Majapahit menghukum pemberontakan Palembang; para bangsawan Palembang tersebar | Pemicu munculnya Parameswara |
| 1389 | Hayam Wuruk wafat; Wikramawardhana naik | Krisis suksesi |
| sekitar 1398–1400 | Parameswara lari dari Palembang, lalu mendirikan Malaka | Pesaing maritim baru |
| 1404–1406 | Perang Regreg (Paregreg): istana barat vs timur (Bhre Wirabhumi) | Perang saudara; melemahkan kendali vasal |
| 1405–1433 | Ekspedisi Zheng He singgah di Jawa; komunitas Muslim di Tuban, Gresik, Surabaya | Awal islamisasi pesisir |
| 1429–1447 | Era Suhita; Kertawijaya (Brawijaya I) menyusul | Kemunduran |
| 1478–1527 | Konflik Demak–Majapahit | Di luar jangkauan game (setelah 1450) |

Peta kekuatan sekitar:

- Daerah bawahan (Nagarakretagama): Sumatra (Jambi, Palembang, Dharmasraya, Minangkabau, Haru, Samudra), Kalimantan, Sulawesi, Maluku, Nusa Tenggara, Papua barat. Para sejarawan sepakat pengaruh di luar Jawa sebagian bersifat simbolik, jadi cocok dimodelkan sebagai vasal longgar dan upeti.
- Rival: Sunda, Malaka (sejak sekitar 1400), Ayutthaya (sejak 1351), Champa sebagai sekutu dekat menurut sumber Jawa.
- Kekuatan luar: Dinasti Ming (hubungan upeti sejak 1369) memberi jalur alternatif bagi negara kecil untuk lepas dari pengaruh Majapahit.

Catatan akurasi: angka tahun beberapa peristiwa berbeda antarsumber (Sumpah Palapa 1334 atau 1336; Perang Regreg 1404–1406 vs 1405–1406). Kita pakai tahun yang paling banyak dikutip dan menyebut ketidakpastiannya di teks event bila perlu.

## Rancangan pohon misi Majapahit

Usulan 12 misi dalam tiga cabang, satu per kolom. Syarat memakai data yang sudah ada di game (provinsi dimiliki, vasal, aliansi, perang, bangunan, tech, stabilitas). Angka masih draf untuk disetel saat uji main.

| # | Cabang | Misi | Syarat selesai | Hadiah |
|---|---|---|---|---|
| 1 | Penyatuan | Sumpah Palapa | Miliki seluruh provinsi Jawa Timur dan Madura | Klaim permanen atas Sunda; +prestise |
| 2 | Penyatuan | Pulau Dewata | Miliki Bali dan Lombok | Modifier 25 tahun: pendapatan pajak naik |
| 3 | Penyatuan | Armada Nusantara | Punya armada/resimen laut sesuai batas dan 3 vasal | Klaim permanen atas Sumatra selatan dan Kalimantan barat |
| 4 | Penyatuan | Mandala Maritim | 5 vasal non-upeti | Daya diplomasi tambahan; integrasi vasal lebih murah |
| 5 | Penyatuan | Cakrawala Timur | Vasal atau pemilik di Maluku dan Nusa Tenggara | Bonus perdagangan rempah |
| 6 | Istana | Kota Trowulan | Bangunan tingkat tinggi di ibu kota | Hadiah dukat dan stabilitas |
| 7 | Istana | Naskah Prapanca | Tech administrasi sesuai tingkat tertentu | +legitimasi, daya administrasi |
| 8 | Istana | Pernikahan Kerajaan | Pernikahan dengan satu negara tetangga | Hubungan +dan klaim suksesi pada negara itu |
| 9 | Istana | Persatuan Dua Istana | Stabilitas ≥ +1 selama 5 tahun, tanpa perang saudara | Kurangi risiko event suksesi |
| 10 | Dagang | Bandar Tuban dan Gresik | Bangun pelabuhan di tiga provinsi pesisir Jawa | Pendapatan dagang naik |
| 11 | Dagang | Utusan ke Tiongkok | Relasi positif dengan negara luar yang punya akses Ming | Dukat dan hubungan baik |
| 12 | Dagang | Penjaga Selat | Kuasai atau jadikan vasal negara di selat barat | Klaim atas Malaka jika muncul |

Cabang pilihan (mengikuti pola "Face the Empire" Prancis): misi 3 memicu event dengan dua jalan: Mandala Longgar (vasal membayar upeti, risiko pemberontakan rendah) atau Kekaisaran Terpusat (integrasi penuh, biaya dan ekspansi agresif lebih tinggi).

Pohon untuk negara lain (kecil, 4–6 misi): Sunda (bertahan dari Majapahit, kuasai pesisir barat), Bali (pertahankan identitas), Brunei (perluasan Kalimantan, mengikuti sejarah penaklukan pesisir), dan satu pohon generik untuk negara tanpa pohon sendiri.

## Rancangan event bersejarah

Event dibagi dua: yang terikat tanggal sejarah tapi dengan syarat dari state game, dan yang acak (MTTH) untuk warna.

| Event | Pemicu | Pilihan utama |
|---|---|---|
| Pernikahan Hayam Wuruk (1357) | Tahun 1355–1358, Majapahit punya relasi dengan Sunda | A) Terima rombongan sebagai tamu setara: Sunda jadi sekutu, Gajah Mada kecewa. B) Tuntut mereka tunduk sebagai vasal: pecah Perang Bubat, Sunda menjadi musuh, prestise turun di mata kerajaan lain |
| Gajah Mada dicopot | Setelah pilihan B | Pensiunkan dengan hormat atau pertahankan sebagai panglima (bonus militer, risiko stabilitas) |
| Pemberontakan Palembang (1377) | Palembang vasal dan lemah | Kirim armada hukuman (perang) atau terima upeti lebih kecil. Kalau dihukum, muncul negara pelarian baru |
| Parameswara mendirikan Malaka (sekitar 1400) | Setelah event Palembang | Pesaing maritim muncul sebagai negara baru, dengan klaim pada selat |
| Krisis suksesi (1389) | Raja wafat, stabilitas rendah | Dukung pewaris resmi, atau bagi kekuasaan antara istana barat dan timur |
| Perang Regreg (1404–1406) | Krisis suksesi tidak diredam | Perang saudara: negara terbelah jadi dua, vasal luar melemah (bagian dari kemunduran) |
| Kunjungan Zheng He (1405 dst) | Pelabuhan Jawa utara berkembang | Terima perdagangan (dukat naik, komunitas Muslim bertambah) atau batasi |
| Pesisir Islam menguat | Banyak pelabuhan beragama Islam | Toleransi (pendapatan naik, legitimasi turun) atau pertahankan tradisi (stabilitas naik, dagang turun) |
| Panen raya / gagal panen, wabah | MTTH, tiap negara | Dua pilihan trade-off dukat vs stabilitas |
| Gempa dan letusan gunung | MTTH, provinsi | Biaya perbaikan atau penurunan pembangunan sementara |

Aturan desain: setiap event punya minimal dua pilihan dengan akibat nyata, ai_chance untuk AI, fire_only_once untuk event sejarah, dan syarat yang bergantung pada kondisi game. Kalau pemain sudah membuat kondisinya berbeda (misalnya sudah menaklukkan Sunda), event Bubat tidak muncul dan diganti event lain.

## Rencana implementasi di game

Urutan kerja yang aku usulkan, kecil dulu supaya bisa diuji tiap tahap:

- Mesin event: daftar event berisi trigger(G), mtth (bulan), once, options[{teks, efek, aiChance}]. Dicek tiap bulan untuk pemain dan AI. Jendela event bergaya Indonesia (bingkai emas, batik tipis di header) memakai UI event yang sudah ada.
- Mesin misi: tab baru "Misi" di rail, grid slot × tier dengan panah, status (terkunci, aktif, selesai), tombol sorot provinsi, dan klaim hadiah otomatis saat trigger benar. Simpan di G.msn.
- Hadiah: reuse sistem yang ada: klaim permanen, modifier berdurasi, dukat, mana, legitimasi, prestise.
- Konten: 12 misi Majapahit + 8–10 event pertama dari tabel di atas; lalu pohon kecil Sunda, Bali, Brunei.
- Pengujian: simulasi 20 tahun tanpa error, lalu cek event sejarah muncul dalam jendela tahun yang benar.

Keputusan yang perlu kamu pilih sebelum mulai: (a) apakah event sejarah boleh "menyimpang" ketika pemain mengubah kondisi (aku sarankan ya), (b) apakah misi harus selesai berurutan atau boleh paralel (aku sarankan paralel per cabang), (c) seberapa besar hadiah, karena game ini belum diseimbangkan lewat main beneran.

## Sumber

EU4 (mekanik):

- Mission modding — EU4 Wiki
- Event modding — EU4 Wiki
- Generic missions — EU4 Wiki
- How 1.25 mission system works — taw's blog
- EU4 Dev Diary 13 Feb 2018 (sistem misi baru)
- EU4 Dev Diary 19 Mar 2019 (sejarah dan filosofi misi)
- French missions — EU4 Wiki

Sejarah:

- Majapahit — Wikipedia
- Hayam Wuruk · Gajah Mada · Battle of Bubat
- Regreg War
- Territories of Majapahit
- Malacca Sultanate · Malacca–Majapahit conflict
- Demak Sultanate
- Britannica: Southeast Asia, the classical period

Catatan: aku membaca potongan hasil pencarian, belum membuka tiap halaman penuh. Angka tahun dan nama pada tabel sejarah sebaiknya dicek ulang sebelum dipakai di teks event final.

## Bagian 2 — Tech tree di EU4

Sejak versi 1.18, teknologi EU4 tidak lagi ditentukan oleh tech group; yang menentukan biayanya adalah institusi.

- Tiga jalur: administrasi, diplomasi, militer, dibeli satu level per kali dengan poin monarki kategori yang sama. Tiap level membuka bangunan, unit, atau bonus.
- Institusi: kemajuan besar (feodalisme, renaisans, dst) muncul di satu provinsi yang memenuhi syarat, lalu menyebar pelan ke provinsi di sekitarnya. Pemilik provinsi asalnya dapat prestise dan poin monarki.
- Penalti: negara yang belum mengadopsi institusi yang sudah ada mendapat biaya tech lebih mahal (penalti bisa puluhan persen, tergantung institusi dan wilayah). Mengadopsi institusi memerlukan biaya dan menghapus penalti itu.
- Tech lebih cepat dari waktunya juga dikenai biaya tambahan (ahead of time), dan biaya naik seiring level.
- Kritik: sistem lama dianggap kaku dan Eropa-sentris; sistem institusi lebih dinamis tapi tetap membuat wilayah yang jauh dari pusat institusi harus bekerja lebih keras.

Untuk game kita: sistem tech yang sudah ada (3 jalur, level 1–30 di G.tech) cukup. Tambahan kecil yang masuk akal untuk 1350–1450: satu atau dua institusi lokal (misalnya Irigasi Subak dan Perdagangan Samudra) yang menyebar dari pelabuhan atau lumbung padi, dan memberi bonus lebih besar kalau diadopsi lebih awal.

## Konversi agama di EU4

Setiap negara punya satu true faith (agama negara). Agama lain dibagi dua: heretik (satu kelompok agama, aliran lain) dan heathen (kelompok agama lain).

| Konsep | Cara kerja |
|---|---|
| Toleransi | Tiga nilai nasional: toleransi true faith, heretik, heathen. Makin tinggi, makin kecil kerusuhan di provinsi beragama itu (sekitar 2 poin kerusuhan per poin toleransi, menurut pemain). |
| Persatuan agama | Persentase basis pajak yang menganut agama negara. Memengaruhi risiko pemberontakan dan biaya stabilitas. Persatuan rendah bisa memicu bencana krisis agama. |
| Misionaris | Utusan yang mengonversi satu provinsi ke agama negara. Kecepatan tergantung kekayaan, budaya, stabilitas, penasihat, dan ide agama. Selama berjalan, provinsi itu mendapat risiko pemberontakan tambahan. |
| Cara lain | Perang, event dan keputusan, atau kebijakan dagang Propagate Religion (agama menyebar lewat pengaruh dagang) |
| Ganti agama negara | Biasanya lewat pemberontak religius atau event; seluruh provinsi lama mendadak jadi heretik/heathen |

Khusus Asia Tenggara dan Majapahit (EU4 versi 1.30+):

- Majapahit mulai Hindu; ada event "Spread of Islam" dan bencana "Fall of Majapahit" yang berpusat pada tarik-menarik antara Islam dan Hindu-Buddha. Pemain Hindu bisa memilih dewa pribadi untuk penguasa.
- Pesisir Malaya dan Indonesia yang awalnya Hindu atau Buddha punya keputusan untuk pindah ke Sunni bila Islam sudah dominan.
- Malaka bisa menyebarkan Islam lewat kebijakan dagang dengan syarat kekuatan dagang lebih rendah (35% setelah misi Porch of Mecca).
- Pengembang sendiri mengakui bahwa sinkretisme Hindu-Buddha-animisme di wilayah ini sulit digambarkan dengan sistem agama biasa.

Untuk game kita: tiap provinsi punya agama (Hindu-Buddha/Syiwa-Buddha, Islam, animisme), negara punya agama resmi, dan ada dua angka: toleransi dan persatuan agama. Islam menyebar pelan dari pelabuhan yang dikunjungi pedagang Muslim, dipercepat oleh Malaka dan peristiwa Zheng He.

## Mekanisme ekonomi di EU4

Ekonomi EU4 adalah pemasukan dan pengeluaran bulanan, tanpa pembayaran tahunan.

|  | Komponen |
|---|---|
| Pemasukan | Pajak (dari development pajak), produksi (dari barang yang dihasilkan provinsi dan harganya), perdagangan, emas (tambang, memengaruhi inflasi), dan lain-lain seperti subsidi dan tarif |
| Pengeluaran | Pemeliharaan pasukan, armada, benteng; gaji penasihat; bunga pinjaman |

- Development tiga jenis (pajak, produksi, manpower) menaikkan pemasukan. Bangunan seperti workshop, manufactory, marketplace, dan counting house menambah produksi atau kekuatan dagang.
- Otonomi provinsi menurunkan produksi, nilai dagang, dan kekuatan dagang; makanya negara disarankan menyisakan sebagian tanah langsung milik mahkota.
- Pinjaman: tiap pinjaman menaikkan inflasi 0,1 dan berjangka 5 tahun; memperpanjang menambah inflasi lagi. Inflasi menaikkan biaya rekrut dan bangunan.
- Stabilitas dan korupsi memengaruhi efisiensi pajak, produksi, dan dagang.
- Cara cepat dapat uang: menguasai node dagang asal, menjual perdamaian ke kekuatan besar, dan mengembangkan provinsi.
- Kebangkrutan membawa penalti serius, jadi pinjaman harus dikelola, bukan dihindari mentah-mentah.

Untuk game kita: ekonomi yang ada (dukat, tenaga, bangunan) sudah dekat dengan ini. Yang bisa ditambah: inflasi sederhana (naik dengan pinjaman dan tambang emas), otonomi provinsi taklukan, dan kategori pemasukan yang terpisah (pajak, produksi, dagang) di jendela ekonomi supaya pemain melihat dari mana uang datang.

## Perdagangan di EU4

Perdagangan adalah sistem terpisah dari pajak dan produksi, dan sering jadi sumber uang terbesar.

- Nilai dagang dihasilkan provinsi dari barangnya, lalu mengalir hilir antar-trade node (sekitar 80 node di peta) lewat rute tetap sampai node akhir.
- Kekuatan dagang (trade power) tiap negara di sebuah node menentukan porsi nilai yang bisa ia ambil. Sumbernya: provinsi di node, bangunan, kapal ringan yang melindungi dagang, dan bonus.
- Pedagang (merchant) punya dua tugas utama: collect (mengambil uang di node itu) atau steer/transfer (mengalirkan nilai ke node berikutnya, dengan bonus trade steering).
- Home node adalah node tempat ibu kota; di sana negara biasanya paling kuat dan bisa mengumpulkan paling efisien. Menguasai node hulu dan hilir lewat steering menarik nilai ke home node.
- Pilihan: collect di semua node memberi uang langsung, tapi campuran collect dan steer biasanya optimal ketika kekuatan dagang sudah dominan.
- Persaingan: peperangan bisa memaksa lawan menyerahkan kekuatan dagang sebagai syarat damai; kapal dan bajak laut memengaruhi node.

Hubungan dengan Nusantara: di EU4, Selat Malaka adalah titik sempit tempat dagang dari Barat mengalir lewat, dan Maluku (cengkeh, pala) punya barang langka; Ternate dan Tidore memegang monopoli cengkeh sejak 1444 di game. Malaka kuat karena posisi node ini, sedangkan Majapahit lebih kuat di pertanian dan armada.

Untuk game kita (versi ringan): tiga atau empat zona dagang (Jawa utara, Selat Malaka, Maluku, Kalimantan–Sulawesi) yang menyambung searah; tiap negara punya kekuatan dagang dari pelabuhan yang dimiliki; satu atau dua pedagang yang bisa dikirim (mirip diplomat) untuk mengambil atau mengarahkan nilai. Cukup untuk membuat pelabuhan dan armada terasa penting tanpa menyalin 80 node.

## Sejarah ekonomi dan agama Majapahit untuk game

- Dua tulang punggung: padi dari lembah Jawa Timur yang diairi (bendungan dan saluran; Prasasti Canggu 1358 mencatat 42 tempat penyeberangan di Sungai Brantas) dan perdagangan laut lewat Tuban, Gresik, dan Surabaya.
- Barang: padi, rempah (cengkeh dan pala dari Maluku dan Banda), kayu jati, kain, dan kayu sappan; impor porselen, tekstil, dan logam dari Tiongkok dan India.
- Uang: ekonomi sebagian sudah bermoneter sejak abad ke-8; pada era Majapahit uang tembaga Tiongkok (kepeng) menjadi alat tukar harian.
- Kapal dan armada: kapal besar jong dan armada yang juga mengamankan jalur dari bajak laut.
- Sistem kekuasaan: mandala; kesetiaan melemah di pinggiran, bukan batas tetap. Cocok dimodelkan sebagai vasal longgar dengan upeti.
- Agama: Hindu-Siwa dan Buddha berbaur dengan kepercayaan lokal; Islam masuk lewat pelabuhan utara dan komunitas pedagang Tionghoa, Arab, dan Melayu, dipercepat Zheng He (1405–1433) dan Malaka.

## Usulan sistem untuk game

| Sistem | Usulan | Tingkat |
|---|---|---|
| Tech | Pertahankan sistem sekarang, tambah 2 institusi lokal yang menyebar | Kecil |
| Agama | Agama per provinsi dan negara, toleransi, persatuan agama, misionaris sederhana, Islam menyebar dari pelabuhan | Sedang |
| Ekonomi | Rincian pemasukan, inflasi, otonomi taklukan | Kecil–sedang |
| Dagang | 3–4 zona dagang searah, kekuatan dagang dari pelabuhan, pedagang yang dikirim | Sedang–besar |

Saran urutan: ekonomi dan agama dulu karena paling mudah terhubung dengan misi dan event yang sudah dirancang; dagang terakhir karena paling besar dan paling bergantung pada armada (yang belum ada).

### Sumber tambahan

- Tech dan institusi: EU4 Dev Diary 26 Mei 2016
- Agama: EU4 Dev Diary 8 (With God on Your Side)
- Agama Asia Tenggara: EU4 Dev Diary 11 Agu 2020 (Brunei, Malaka, Aceh)
- Majapahit di EU4: EU4 Dev Diary 28 Jul 2020
- Ekonomi: EU4 Dev Diary 4 (Your economy is about to change)
- Cara cari uang dan pinjaman di EU4
- Panduan dagang EU4 (forum Paradox)
- Cara membentuk Malaya di EU4
- Economic history of Indonesia — Wikipedia
- Peran maritim dan perdagangan Majapahit 1350–1389 (jurnal Sosioedukasi)

Catatan: bagian tech, agama, ekonomi, dan dagang disusun dari potongan hasil pencarian dan forum pemain, bukan dari wiki resmi EU4 yang dibuka penuh. Angka seperti penalti tech dan kerusuhan per toleransi perlu dicek di wiki sebelum dipakai sebagai angka game.

## Bagian 3 — Hasil baca langsung wiki EU4 (angka pasti)

Sumber: eu4.paradoxwikis.com (Trade, Economy, Technology, Institutions, Religion). Ini menggantikan angka dari snippet di Bagian 2 bila berbeda.

### Teknologi & institusi

- Biaya satu level tech = max(30, 600 × (100% + modifier umum + penalti institusi)). Ada 3 jalur (ADM/DIP/MIL), masing-masing 33 level.
- Penalti institusi: tech pertama sebuah institusi +15%, kedua +30%, sisanya +50%. Ada 8 institusi; tanpa satu pun di tahun 1821 penaltinya +400%.
- Kelompok tech tanpa Feudalism mulai dengan +50%. Kelompok Indian/Muslim/Chinese mulai +0% di level 3.
- Kenaikan seiring waktu: linear, 0% (acuan 1444) sampai 30% (acuan 1821).
- Bonus tetangga: -5% per level tertinggal dari tetangga paling maju (maks -75%).
- Ahead of time: +10% biaya per tahun lebih cepat dari kurva sejarah.
- Idea group: tiap ide terbuka -2% biaya tech (maks -14% per grup); Innovative punya -10% biaya tech dan -10% biaya embrace institusi.
- Embrace institusi: butuh minimal 10% development (setelah autonomy) sudah terkena institusi, lalu bayar 2,5 dukat per sisa development.
- Institusi 1066 Feudalism; mekanik Majapahit 1350 perlu "institusi" sendiri yang kita rancang (mis. Candi/Perdagangan Laut) karena Feudalism sudah terbawa.

### Agama

- Toleransi iman sendiri dasar +3. Hindu/animis +1 tambahan; Jewish/Zoroastrian +2.
- Toleransi positif: -1 unrest lokal per poin. Negatif: +1,25 unrest, -10% pajak lokal, -10% produksi lokal per poin.
- Religious unity: provinsi iman negara 100%; heretik/heathen menyumbang 25/50/75/100% tergantung toleransi 0/≤1/≤2/≤3 (di bawah 0 = 0%).
- Unity di bawah 100%: +1% biaya stabilitas, +0,03 unrest nasional per poin kekurangan.
- Misionaris: tiap bulan kekuatan misionaris efektif ditambahkan ke progres provinsi; 100% = pindah agama. Misionaris aktif +6 unrest. Bonus: stabilitas positif +0,5% per poin, Inquisitor +2%, ulama/dewa tertentu +2%. Gaji misionaris dasar 5 dukat/tahun.
- Asia Tenggara: Javan "Candi Shrines" +20% unity, Balinese "Staunch Hindus" +2 toleransi, Khmer "Theravada Buddhism" +1 toleransi. Buddha punya Mahayana/Theravada/Vajrayana.
- Pemberontak religius bisa menunjuk agama baru jika agama itu dominan (development terbesar).

### Ekonomi

- Pajak provinsi tahunan = base tax × efisiensi pajak lokal. Produksi = harga barang × produksi dasar × efisiensi.
- Emas: 40 dukat/tahun per unit; inflasi +0,5%/tahun × porsi emas dalam pendapatan.
- Pinjaman: ukuran = floor(0,5 × total development) × (1 + efisiensi dagang); bunga dasar 4%/tahun, minimal 1%; tiap pinjaman +0,1 inflasi; kalau jatuh tempo, otomatis diperpanjang 5 tahun dan +0,1 inflasi lagi. Stabilitas negatif +1% bunga per poin.
- Bangkrut: pinjaman dihapus, inflasi -25%, efek 5 tahun: moral -50%, biaya penasihat +50%, biaya tech +50%, recovery manpower 0.
- Upkeep pasukan penuh: 2% biaya rekrut resimen per bulan. Fort mothball saat damai -50%.
- Penasihat: gaji = skill² (+0,5%/tahun sejak 1444), kena inflasi.
- Pendapatan vasal: berbasis pajak vasal, dimodifikasi legitimasi overlord.
- Biaya Root Out Corruption: 0–0,05 × development efektif per bulan.

### Perdagangan

- Kekuatan dagang provinsi: +0,2 per development; Center of Trade lv1 +5, lv2 +10, lv3 +25; muara sungai +10; pesisir +25%; Marketplace +50%, Trade Depot +100%, Stock Exchange +125%; diduduki -50%; dikepung -25%; autonomy maks -50%.
- Light ship +3 dagang per kapal (dasar); merchant yang hadir +2 dan +10% efisiensi.
- Nilai terkumpul = sisa nilai node × (kekuatan kita ÷ total kekuatan pengumpul). Pendapatan = terkumpul × (efisiensi + 10% bila ada merchant).
- Nilai keluar (forward) = nilai node × kekuatan transfer ÷ (transfer + kumpul). Tanpa ada yang steer, nilai dibagi rata ke node hilir.
- Collect di node selain node ibu kota: kekuatan dagang × 0,5.
- Boost merchant steering pada satu jalur: 1→+5%, 2→+7,5%, 3→+9,1%, 4→+10,3%, 5→+11,3% (maks 5 merchant).
- ±80 node dagang. Tiap negara dasar punya 2 merchant. Kerajaan di Malaka/Jawa biasanya berebut node yang sama, jadi merchant sangat terbatas.

### Terjemahan ke game kita

- Ekonomi: pisahkan pajak, produksi, dan dagang; tambah pinjaman dengan bunga 4% dan inflasi, bangkrut sebagai penalti 5 tahun.
- Agama: tiap provinsi punya agama (Hindu-Siwa, Buddha, animisme, kemudian Islam); toleransi mengurangi unrest; misionaris/ulama mengonversi lewat progres bulanan.
- Dagang: node kecil (Malaka, Jawa Utara, Maluku, Sumatra), kekuatan dagang dari provinsi pelabuhan, merchant terbatas, rempah Maluku bernilai tinggi.
- Tech: biaya naik dengan penalti kalau terlalu cepat, bonus kalau tertinggal dari tetangga; satu institusi buatan sendiri.

Catatan: halaman wiki terpotong sekitar 100 ribu karakter; detail unit/bangunan per level tech dan biaya ganti agama negara belum terbaca.

## Bagian 4 — Rencana pembangunan (berdasarkan semua riset)

Prinsip: bangun bertahap, tiap tahap bisa dimainkan dan dites sendiri, UI kecil dan rapi, tiru EU4 bila ragu. Urutan dipilih supaya tahap awal jadi fondasi tahap berikutnya.

### Tahap A — Mesin event dan misi (fondasi)

- Satu mesin bersama: trigger (syarat), effect (hadiah/akibat), options dengan ai_chance, fire_only_once.
- Event: dua jenis, acak per bulan (MTTH) dan dipicu event/misi lain. Muncul sebagai jendela kecil dengan 2–3 pilihan.
- State baru: G.ev (event sudah terpicu), G.mis2 (progres misi), G.flags, G.mod (modifier sementara dengan masa berlaku).
- Efek dasar yang dibutuhkan: mana, stabilitas, prestise, klaim permanen, modifier N tahun, ubah agama provinsi, tambah/kurangi dukat.
- Tes: satu event dummy dan satu misi dummy, simpan/muat tidak rusak.

### Tahap B — Ekonomi (angka dari wiki)

- Pendapatan dipecah: pajak, produksi, dagang, upeti vasal. Pengeluaran: pasukan (2% biaya rekrut/bulan), benteng, penasihat, bunga.
- Pinjaman: ukuran = floor(0,5 × total development); bunga 4%/tahun; tiap pinjaman +0,1 inflasi; diperpanjang otomatis 5 tahun (+0,1 inflasi lagi).
- Inflasi menaikkan semua biaya; tombol "Kurangi inflasi" memakai mana ADM.
- Bangkrut saat kas minus dan pinjaman maksimal: pinjaman terhapus, inflasi -25%, penalti 5 tahun (moral -50%, biaya tech +50%, recovery manpower 0).
- Panel Ekonomi di jendela negara: tabel pendapatan/pengeluaran, pinjaman, inflasi.
- Tes: ambil pinjaman sampai bangkrut, cek penalti hilang setelah 5 tahun.

### Tahap C — Agama dan toleransi

- Tiap provinsi punya agama: Hindu-Siwa, Buddha, animisme, lalu Islam (Sunni). Negara punya agama resmi.
- Toleransi iman sendiri +3 (Hindu +1 lagi); toleransi heretik/heathen biasanya 0–1. Toleransi positif -1 unrest per poin, negatif +1,25 unrest dan -10% pajak/produksi per poin.
- Religious unity = porsi development yang beragama negara (heretik/heathen menyumbang 25–100% sesuai toleransi). Di bawah 100% menambah biaya stabilitas dan unrest.
- Misionaris (seperti diplomat, jumlah terbatas): ditugaskan ke provinsi, progres bulanan sampai 100%, +6 unrest selama bertugas, bergaji.
- Penyebaran Islam: dari pelabuhan dagang Pasai/Malaka, lewat event "Penyebaran Islam" dan modifier pelabuhan; pemain bisa menolak atau merangkul.
- Ganti agama negara memicu stabilitas turun dan unrest sementara.
- Tes: konversi satu provinsi, cek unity dan unrest berubah.

### Tahap D — Teknologi dan institusi

- Tiga jalur (ADM/DIP/MIL), pakai mana yang sudah ada. Biaya = 600 × (1 + modifier + penalti institusi), naik linear dengan waktu, -5% per level tertinggal dari tetangga, +10% per tahun bila terlalu cepat.
- Institusi buatan (3–4 saja, bukan 8): Candi dan Birokrasi (sudah ada di 1350), Pelayaran Jung (sekitar 1400), Bubuk Mesiu dan Meriam (sekitar 1500). Menyebar dari provinsi asal; negara bisa "embrace" bila ≥10% development terkena (bayar 2,5 dukat per sisa development).
- Level tech membuka bangunan, jenis pasukan, dan slot ide.
- Ide nasional: 7 ide per negara, 1 ide per level tertentu; Majapahit mendapat ide tema laut dan candi.
- Tes: majukan tech sampai penalti institusi muncul dan hilang setelah embrace.

### Tahap E — Misi (pohon misi per negara)

- Tampilan pohon dengan baris/kolom, panah hanya horizontal/vertikal; tiap misi punya potential, trigger, effect, dan menyorot provinsi saat disentuh.
- Majapahit: 12 misi dalam 3 cabang paralel (rekomendasiku), mis. cabang Jawa, cabang Laut, cabang Istana. Contoh isi: Sumpah Palapa (klaim Nusantara), Kuasai Selat Malaka, Tundukkan Bali, Jinakkan Sunda, Bangun Candi Agung, Kirim utusan ke Tiongkok.
- Hadiah: klaim permanen, modifier 25 tahun, mana, pembukaan event.
- Negara lain: set misi generik 4–6 buah (ekspansi, ekonomi, agama) supaya tidak kosong.
- Tes: selesaikan satu misi dan cek hadiah dan kunci misi lanjutan terbuka.

### Tahap F — Event sejarah dan generik

- 8–10 event sejarah Majapahit: Peristiwa Bubat, wafatnya Gajah Mada, Perang Paregreg, Penyebaran Islam, Pasai, Demak, Kejatuhan Majapahit (bencana), dll. Boleh menyimpang bila kondisi pemain berubah (rekomendasiku).
- Event generik: panen raya, wabah, pemberontak, utusan asing, bangkitnya ulama, upeti.
- Tiap event: syarat, deskripsi singkat, 2–3 pilihan dengan akibat jelas.
- Tes: paksa picu tiap event lewat tombol debug, cek tidak ada yang rusak.

### Tahap G — Perdagangan

- 5–8 node (Malaka, Jawa Utara, Maluku, Sumatra, Borneo, Siam, Tiongkok Selatan) dengan arah aliran ke Malaka.
- Kekuatan dagang provinsi: 0,2 per development, bonus pelabuhan/pasar; kekumpulan: bagian kekuatan kita di node.
- Merchant terbatas (2 awal); collect di node bukan ibu kota kekuatan × 0,5; boost steering 5%–11% (1–5 merchant).
- Rempah Maluku bernilai tinggi; pelabuhan Malaka sebagai titik sempit.
- Tes: kirim merchant, cek pendapatan dagang berubah sesuai rumus.

### Tahap H — Setelahnya

- Angkatan laut (diperlukan setelah dagang), pemberontak, penyeimbangan, ornamen layar awal.

### Urutan dan estimasi kasar

A → B → C → D → E → F → G → H. Tiap tahap kira-kira satu sesi kerja; A dan B boleh digabung. Aku sarankan jangan mulai dari misi dulu karena butuh mesin event dan agama untuk hadiah yang bermakna.

### Keputusan yang kuasumsikan (bisa kamu ubah)

- Event sejarah boleh menyimpang dari sejarah.
- Misi paralel per cabang, bukan berurutan satu garis.
- Hadiah kecil dan seimbang: klaim, modifier 25 tahun, sedikit mana.
- Institusi hanya 3–4 buatan sendiri, bukan 8 seperti EU4.

## Riset lanjutan: pohon misi EU4 dan penerapan Tahap E

Sumber primer: catatan pengembang Paradox 30 Januari dan 13 Februari 2018 tentang sistem misi versi 1.25, diterbitkan ulang di Steam:
- https://store.steampowered.com/news/posts/?appids=236850&enddate=1517932923
- https://store.steampowered.com/news/posts/?appids=236850&enddate=1519912880

Penelusuran mengonfirmasi peralihan ke pohon misi. Akses langsung ke halaman Missions, Generic missions, dan Majapahit missions di wiki Paradox mengembalikan 401 pada sesi riset ini; angka syarat dan hadiah di bawah adalah rancangan Nusantara, bukan kutipan angka EU4 atau salinan pohon DLC Majapahit.

Penerapan: tiga cabang paralel, misi prasyarat wajib sudah diambil, syarat diperiksa ulang saat klaim hadiah, sekali per kampanye, hadiah mana/klaim/modifier 25 tahun. Ada 12 misi Majapahit dan enam generik. Sasaran memakai provinsi asal sehingga tidak berubah saat pemilik berganti; vasal memenuhi misi wilayah tetapi pendudukan musuh tidak. Syarat kas/stabilitas tidak dikonsumsi. Save lama memakai ID kas/bangun/stabil yang sama.

Batas: klaim dalam mesin sekarang belum membedakan klaim biasa dan permanen maupun biaya coring EU4; hadiah memakai sistem klaim yang tersedia. Belum ada angkatan laut, perdagangan ber-node, atau hubungan tributari terpisah; misi tidak mensyaratkan sistem yang belum ada. Tombol sasaran memusatkan peta dan menyorot satu provinsi yang belum dipenuhi. Tampilan cabang memakai tab agar muat di HP.

## Penerapan event sejarah Tahap F
Paket awal menggunakan kronologi dan catatan ketidakpastian pada bagian sejarah dokumen ini. Bubat diperlakukan sebagai kisah yang mengilhami pilihan diplomatik; tahun 1355–1360 adalah jendela skenario, bukan tanggal kejadian baru. Pergantian generasi, Paregreg, dan kunjungan Ming dapat terpicu hanya pada jendela tahun serta kondisi yang sesuai. Pilihan alternatif adalah fiksi sejarah untuk kampanye pemain.

Mesin mengikuti pola trigger, event sekali, pilihan berakibat, modifier berdurasi, dan rantai tertunda. Efek hanya memakai sistem yang telah ada. MTTH tetap menggunakan peluang bulanan 1−0,5^(1/bulan), sehingga parameter ini adalah waktu median; bukan jaminan event muncul pada tanggal tertentu. Riset daring tambahan untuk kronologi tidak memberikan sumber baru yang dapat diverifikasi pada sesi ini; paket tidak mengklaim menambah temuan sejarah baru. Rujukan pola EU4 tetap catatan developer pada bagian sebelumnya.

## Riset perang dan event lanjutan
Sumber primer: manual resmi Europa Universalis IV, bagian Warfare, Casus Belli dan War Goal:
https://forumcontent.paradoxplaza.com/public/79250/EuropaUniversalisIV_Manual.pdf
Hasil penelusuran menampilkan penjelasan bahwa panel deklarasi memisahkan CB dan tujuan perang serta bahwa tujuan memberi ticking warscore. Dokumen penuh terlalu besar untuk dibaca lewat pembuka web pada sesi ini. Halaman wiki tetap terbatas aksesnya. Klaim kesetaraan angka di seluruh sistem tidak dibuat.

Penerapan: layar persiapan, konfirmasi, pilihan provinsi klaim/inti, daftar pihak lawan dan pilihan sekutu. Penaklukan memakai satu sasaran untuk ticking score ±0,4/bulan sampai ±25, terpisah dari daftar klaim untuk biaya perdamaian. Perang tanpa alasan mengurangi stabilitas 2 dan prestise 10 serta menambah AE 6; angka AE adalah rancangan lokal. AI masih memakai sistem alasan perang sederhana.

Fabrikasi sekarang langsung menambahkan klaim dengan jaringan 20 + 5 per klaim di negara target, tanpa biaya DIP. Ini menggantikan pengerjaan lokal 8–30 bulan; antrean save lama tetap dapat selesai. Label menunjukkan biaya jaringan. Klaim save dinormalisasi ke ID angka. Pasukan bermusuhan berhadapan di jalur yang sama ditangkap pada hari pertemuan; pertempuran ditambatkan ke provinsi tujuan penyerang, sesuai mesin berbasis provinsi.

Tambahan 24 event memakai konteks kehidupan agraris, perkumpulan pengrajin, jaringan bandar, budaya naskah, dewan mandala, dan pembiayaan pasukan sebagai bahan fiksi. Bukan klaim bahwa kejadian spesifik tersebut tercatat pada tahun tertentu. Tiga skenario alternatif bergantung pada pilihan Bubat, warisan Gajah Mada, dan penyelesaian Paregreg dari paket sejarah. Efek memakai ekonomi, mana, inflasi, legitimasi, toleransi, diplomat dan modifier yang benar-benar dibaca mesin game. Belum ada simulasi kapal/perdagangan node/pemberontak baru.

## Visual kota Majapahit
Referensi: pengajuan Indonesia tentang Trowulan pada daftar tentatif UNESCO, https://whc.unesco.org/en/tentativelists/5466/ . Sumber mencatat peninggalan candi, gapura, struktur air, dan unsur permukiman. Ikon Majapahit kini memakai siluet candi bata bertingkat, gapura terbelah yang terinspirasi Wringin Lawang, paviliun terbuka, dan pelataran/kolam. Ini interpretasi visual untuk peta kecil, bukan rekonstruksi persis sebuah situs atau klaim semua kota memiliki monumen yang sama. Gaya ditentukan asal provinsi, sehingga penaklukan tidak langsung mengganti bangunan.
