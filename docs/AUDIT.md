# Audit gameplay dan perluasan teknologi/sumber daya

Audit otomatis dan penelusuran kode mencakup ekonomi, perang, AI, diplomasi/bawahan, misi/event, teknologi/agama, perdagangan, UI dan save. Ini audit satu iterasi, bukan jaminan semua bug atau persoalan keseimbangan sudah hilang.

| Temuan | Perbaikan / bukti |
|---|---|
| Bangunan sama dapat masuk antrean berulang | Handler memeriksa bangunan dan antrean aktual; t31 |
| Event kosong/klik lama dapat merusak antrean | Token per event, validasi indeks, penyimpanan setelah pilihan; t31 |
| Kecepatan/space dapat melanjutkan waktu saat modal | Kontrol menolak saat antrean event aktif; t31 |
| Agama kampanye lama bocor lewat NATS | Reset agama statis sebelum kampanye baru; t31 |
| Klaim dianggap cukup untuk menuntut provinsi belum diduduki | Perdamaian memerlukan pendudukan; pilihan stale divalidasi ulang; t31 |
| Vasalisasi 100 poin ditolak pada warscore 100 | Penyerahan penuh diterima; t31 |
| Pemain anggota perang dapat memanggil handler negosiasi pemimpin | Handler memeriksa pemimpin sisi |
| Perdamaian sama dapat membayar emas berulang | Perang harus masih aktif; wrapper AE menghormati penolakan; t31 |
| Menyerang vasal melewati perjanjian dengan penguasanya | Validasi penguasa target sebelum deklarasi |
| Hadiah mana melewati batas 999 | Hadiah efek/misi dibatasi; t31 |
| Log AI menenggelamkan log pemain | worldLog tersendiri, maksimal 80 catatan |
| AI militer selalu level 3 | techOf memakai kurva AI yang dibatasi level 32 |
| Ahead-of-time dihitung dari tingkat yang sudah dimiliki | Menggunakan tahun tingkat berikutnya; t32 |
| Runner lama bergantung Chrome/file:// serta tidak mencakup tes baru | npm test memakai runner HTTP dan browser tersedia; semua berkas t17–t32 tercakup |

Validasi: 16 berkas tes lulus; legacy t17–t22 memeriksa smoke/simulasi dan pageerror, sedangkan tes baru juga memakai assertion. t31 menjalankan awal semua kerajaan dan simulasi 12 tahun dengan pilihan event. Tes t31, t32, dan t25 diulang setelah koreksi teknologi AI. Screenshot panel sumber daya dan gameplay diperiksa pada viewport HP. Belum memakai save asli pengguna atau HP fisik.

## Teknologi dan sumber daya: kontrak awal
Teknologi tetap tiga jalur ADM/DIP/MIL dengan biaya mana, institusi dan modifier yang sudah ada. Penalti terlalu maju menilai tahun target; diskon tetangga hanya tersedia bila ada tetangga darat/selat, menggunakan kurva tingkat AI yang masih disederhanakan. Panel menampilkan tahun tingkat berikutnya dan pembukaan pengolahan. Angka perkembangan 1350 tetap rancangan Nusantara, bukan salinan tanggal EU4.

Stok fisik pangan/kayu/besi/rempah disimpan per negara, kapasitas 500. Hasil provinsi mengikuti barang dan development produksi. Pengolahan biaya 50 dukat dan 5 kayu, selesai 6 bulan, menghasilkan ×2; butuh ADM 4 atau MIL 4 untuk besi. Bangunan tetap melekat pada provinsi saat pemilik berubah. Pendudukan memberi pengendali separuh produksi dan menghentikan pembangunan. Pangan dikonsumsi 0,1 per resimen +0,1 per provinsi per bulan; kekurangan pangan menambah biaya pasukan pemain 20%. Rekrut pemain mulai MIL 4 membutuhkan satu besi. Pasar sumber daya memakai harga beli/jual berbeda agar tidak mencetak uang gratis. Save lama diberi stok awal tanpa menghapus progres.

Ini adaptasi awal gagasan resource improvement/strategic supply Civilization ke peta provinsi Nusantara. Belum ada grid heksagonal, builder/worker, deposit habis, barter antarkerajaan, atau kelas unit berbasis banyak bahan. AI menerima produksi stok namun keputusan belanja/pembangunan/pemakaian perlengkapan sumber daya belum setara pemain; ekonomi AI lama tetap abstrak. Riset web tambahan tidak memberikan sumber terverifikasi baru pada sesi ini; formula di atas adalah rancangan implementasi lokal.
