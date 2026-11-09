# Riset armada dan kesiapan pasukan

## Sumber dan batas sejarah

- [Manual resmi EU4](https://forumcontent.paradoxplaza.com/public/79250/EuropaUniversalisIV_Manual.pdf): pemisahan armada, komposisi kapal, laksamana, pertempuran laut dan penugasan perdagangan.
- [Manual resmi Cradle of Civilization](https://cdn.akamai.steamstatic.com/steam/apps/721340/manuals/PDX_EUIV_CoC_Manual_ENG.pdf?t=1646154511): latihan dan profesionalisme sebagai pembeda kesiapan tentara. Fitur EU4 berbeda menurut versi/DLC; angka Nusantara di bawah adalah rancangan lokal.
- [UNESCO, bukti arkeologi bawah air Teluk Siam](https://fr.unesco.org/silkroad/sites/default/files/knowledge-bank-article/evidence_from_the_underwater_archaeological_sites_in_the_gulf_of_siam.pdf): temuan kapal dagang abad XIV–XVII menunjukkan variasi lambung dan teknik pembuatan setempat. Istilah junk/jung tidak dengan sendirinya menetapkan asal Tiongkok atau fungsi tempur.
- [UNESCO, kontak perdagangan kepulauan Indonesia](https://en.unesco.org/silkroad/sites/default/files/knowledge-bank-article/trade_contacts_with_the_indonesian_archipelago.pdf): tradisi pembuatan kapal Asia Tenggara memiliki ciri teknik tersendiri dan berubah sepanjang waktu.
- [UNESCO, Sailing East to West](https://en.unesco.org/silkroad/sites/default/files/knowledge-bank-article/sailing%20east%20to%20west.pdf): jaringan pelayaran menghubungkan Jawa dan kawasan rempah melalui banyak bandar.

Penelusuran sumber tersebut mendukung keragaman tradisi kapal, bukan satu spesifikasi kapal Majapahit tahun 1350. Jangan memproyeksikan armada meriam abad XVI ke semua kerajaan pada awal permainan. Nama peran berikut adalah label desain, bukan klasifikasi sejarah yang pasti.

## Rancangan angkatan laut — belum diimplementasikan

| Peran EU4 | Label usulan Nusantara | Fungsi permainan |
|---|---|---|
| Heavy ship | Jung tempur | Lambung kuat, biaya tinggi, menjaga pertempuran laut terbuka |
| Light ship | Kapal patroli | Menambah kekuatan di node dagang yang dapat dijangkau |
| Galley | Perahu dayung | Murah, cocok untuk perairan pesisir tertentu; bonus harus mengikuti geografi |
| Transport | Jung angkut | Memindahkan pasukan, rentan tanpa pengawal |

Urutan pembangunan yang dapat diuji per tahap:

1. Simpan armada per negara, pelabuhan, antrean pembangunan, kekuatan lambung dan biaya. Kayu sebagai bahan utama, besi untuk perlengkapan tingkat lanjut; syarat dan angka harus terlihat sebelum membangun.
2. Bangun graph laut tersendiri, perintah berlayar, sandar dan perbaikan di pelabuhan ramah. Jangan memaksakan pathfinding tentara darat ke kapal.
3. Kapasitas angkut dalam resimen, embarkasi/disembarkasi dengan waktu perjalanan. Usulan awal satu kapasitas per resimen; ini aturan permainan, bukan ukuran kapal sejarah.
4. Pertempuran armada, mundur, blokade, intersepsi selat dan patroli node dagang. Kontrol selat baru membatasi rute darat setelah transportasi dan AI armada berfungsi.
5. AI menentukan kebutuhan transportasi, pengawalan, patroli, perbaikan dan biaya sebelum memulai perang lintas pulau.

Kapal tempur, kapal dagang dan angkutan harus bersaing untuk anggaran yang sama. Blokade sebaiknya mengurangi produksi/pajak pesisir dan membantu pengepungan secara terbatas, dengan kekuatan relatif serta opsi mematahkan blokade. Semua efek wajib masuk perhitungan ekonomi/perang, bukan sekadar ikon. Save lama harus mendapat armada kosong tanpa kehilangan tentara atau rute yang sedang berjalan.

Belum ada kapal, pelaut, blokade, laksamana atau angkutan laut di versi ini. Tentara masih melewati hubungan selat peta yang lama.

## Kesiapan pasukan — sudah diterapkan

- Pemeliharaan pemain 0/50/100%. Biaya dasar berturut-turut 50/75/100%; batas moral 50/75/100%. Moral pulih 0/6/12 poin persentase per bulan. Menaikkan anggaran tidak langsung memulihkan moral.
- Latihan hanya di wilayah sendiri yang tidak diduduki, saat diam dan di luar pertempuran, dengan pemeliharaan penuh. Latihan menambah biaya dasar pasukan yang dilatih 25%, membatasi moral 50%, menambah drill 2 per bulan hingga 100. Bergerak atau bertempur menghentikan latihan.
- Profesionalisme 0–100 per negara, bertambah sampai 0,1 poin/bulan bila seluruh tentara berlatih. Kontribusi tiap kelompok dibobot jumlah resimen, sehingga membagi kelompok tidak mempercepat profesionalisme.
- Drill penuh memberi kualitas tempur +10%, profesionalisme penuh +5%. Drill turun 0,5/bulan ketika tidak berlatih dan berkurang saat bertempur. AI berlatih saat damai di wilayah sendiri dan berhenti ketika berperang; pemeliharaan AI diasumsikan penuh karena kas AI belum menjadi ledger lengkap.
- Rekrut baru bermoral 50% dan drill nol. Gabung/rekrut membobot kesiapan menurut resimen; membagi pasukan mempertahankan kesiapan. Tidak bisa menggabung atau membagi kelompok yang sedang bertempur.
- Pertempuran membaca moral saat masuk dan mengembalikan sisa moral sesudah selesai. Bantuan yang datang membawa moralnya sendiri, dibobot dengan kekuatan pihak yang tersisa. Pulih dahulu sebelum perang berikutnya menjadi keputusan yang relevan.
- Lebar tempur = min(30, 8 + floor(teknologi MIL/2)) resimen. Damage harian dibatasi jumlah yang bisa bertempur, sehingga menumpuk tentara tidak terus melipatgandakan damage. Cadangan masih berupa total pasukan, bukan antrean resimen individual.
- Save lama mendapat pemeliharaan penuh, profesionalisme/drill nol dan moral penuh; tidak perlu memulai kampanye baru.

Fase tembak/adu, panglima, medan, pengepungan dan atrisi yang sudah ada tetap digunakan. Belum ada komposisi infanteri/kavaleri/artileri, unit pips, baris depan/belakang, flanking, atau penguatan resimen parsial seperti EU4. Itu perlu tahap lanjutan beserta penyeimbangan; tahap ini memperdalam kesiapan dan batas garis tempur terlebih dahulu.

## Suara dan verifikasi

Klik rutin memakai sinus pendek dengan attack lebih lembut, frekuensi lebih rendah dan gain puncak 0,012–0,025. Jeda bersama 100 ms menghindari tumpukan bunyi dari satu interaksi. Efek perang/event dan musik tetap punya karakter terpisah. Tes browser memeriksa gain klik, bukan penilaian kualitas suara di speaker HP sungguhan.

`tests/t33_military_audio.py` memeriksa anggaran, moral, latihan, profesionalisme, pembagian/penggabungan, save, lebar tempur dan audio WebAudio. Seluruh tes dijalankan melalui `npm test`. Screenshot diperiksa pada viewport HP landscape 780×360; belum dites pada perangkat fisik.
