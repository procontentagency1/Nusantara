# Rencana pembangunan Tahap A–H

> **Status 2026-11-09:** Fondasi A–G sudah tersedia; H dikerjakan bertahap. Catatan di bawah menyimpan rencana awal dan pembaruan berurutan. Implementasi terkini mencakup kesiapan tentara, sumber daya, integrasi/perlawanan daerah, audio adaptif dan armada awal. Kontrak terbaru: `docs/AUDIT.md`, `docs/ARMADA_DAN_PASUKAN.md`, `docs/ARMADA.md`, `docs/AUDIO.md`, dan `docs/EKSPANSI.md`. Angkutan tentara/blokade laut masih tahap lanjutan.

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

### Pembaruan implementasi Tahap E
Pohon awal sekarang berisi 12 misi Majapahit (Ekspansi, Diplomasi, Istana) dan enam generik. Prasyarat, klaim hadiah sekali, sasaran wilayah, vasal, serta kompatibilitas save sudah diuji. Berikutnya Tahap F (event sejarah), lalu G (dagang). Penyempurnaan E: sorot seluruh wilayah, lebih banyak misi khusus negara, dan penyeimbangan melalui permainan panjang.

### Tahap F: paket awal event sejarah
Delapan event sekali per kampanye: rombongan Sunda/Bubat, dewan setelah sengketa, warisan Gajah Mada, Nagarakretagama, tuntutan Palembang, suksesi istana, Paregreg, utusan Ming. Dua event generik berulang: musyawarah desa dan prajurit ingin pulang. Pemicu sejarah memeriksa negara, rentang tahun, dan kondisi aktual. Tes: tests/t24_history.py (16 pilihan, kondisi, rantai, save). Berikutnya Tahap G: perdagangan.

Batas implementasi: Paregreg memberi dampak ekonomi/stabilitas dan belum memunculkan pasukan pemberontak; suksesi belum mengganti penguasa karena belum ada sistem dinasti. Event Palembang belum menciptakan negara Malaka baru. Angka efek adalah rancangan game untuk diuji keseimbangannya.

### Perang dan perluasan event
Paket lanjutan menambahkan 24 event (total 39 definisi termasuk paket sejarah), persiapan deklarasi perang dengan sasaran, konfirmasi dan panggilan sekutu, klaim langsung memakai jaringan, serta pertempuran ketika pasukan berpapasan. Ticking score untuk sasaran pilihan disimpan dalam perang. Pengujian tests/t25_war_events.py mencakup klaim, batal, konfirmasi, sasaran berubah, perang tanpa alasan, pasukan sekotak/berpapasan, serta 48 pilihan event tambahan.

### Pendalaman hubungan bawahan
Vasal dan negara upeti kini terpisah: LD, pajak bulanan, upeti tahunan lima jenis, trust/penolakan, scutage, tawaran diplomatik, perlindungan, pelepasan, perang kemerdekaan dan integrasi bertahap. Panel Kerajaan → Bawahan membuka ringkasan; detail di diplomasi negara. Pengujian tambahan tests/t26_subjects.py; batas ekonomi AI dan penyesuaian angka dicatat di RISET.md.

### Tahap G: jaringan perdagangan awal selesai
Tujuh node, dua merchant dengan perjalanan 30 hari, pengumpulan otomatis di node utama, pengumpulan/steering manual, penalti luar node utama, pasar/pesisir/pusat kota sebagai kekuatan dagang, persaingan AI, pengaruh pendudukan, nilai rempah Maluku, dan pendapatan kas bulanan. Menu Ekonomi → Jaringan perdagangan. Pengujian tests/t27_trade.py: konservasi nilai, income, perhitungan murni, waktu perjalanan, slot merchant, penalti, steering, pasar, pendudukan, save/migrasi dan pembayaran kas.
Berikutnya Tahap H: angkatan laut dan blokade, lalu pemberontak serta penyeimbangan kampanye.

### Perbaikan AI: pulang dan pemulihan setelah perang
AI kini kembali ke wilayah sendiri setelah damai walaupun masih memiliki akses di wilayah sekutu/penguasa. Rute pulang tanpa akses memakai status exiled khusus AI (tidak bertempur/mengepung/atrisi) sampai mencapai tanah air, tanpa teleport. Tujuan kepungan dibagi berdasarkan pasukan yang sudah ditugaskan; AI mengutamakan sasaran perang dan pembebasan wilayah, menghindari musuh terlalu kuat, dan berkumpul dengan pasukan sendiri bila perlu. Perintah pemain tetap manual.
Penanda pertempuran basi dibersihkan, pertempuran yang tak lagi memiliki pihak bermusuhan dihentikan tanpa pemenang, dan penggabungan/rekrut AI tidak mengubah pasukan yang masih bertempur. tests/t28_ai_recovery.py mencakup sembilan pemeriksaan serta simulasi dua tahun. Ini belum merupakan AI strategi lengkap atau transportasi laut.
