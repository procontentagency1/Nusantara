# Label peta dan dagang sumber daya antarkerajaan

## Label sesuai view

View Politik tetap menampilkan nama kerajaan saat zoom jauh dan nama provinsi saat dekat. Agama memakai nama agama provinsi pada kedua rentang zoom; sumber daya memakai jenis sumber daya/barang, perdagangan memakai nama node, dan medan memakai jenis medan. Nama laut tetap menjadi penunjuk geografis.

`mapProvinceLabel` adalah sumber teks label tematik. Label besar dikelompokkan menurut tema, node geografis, dan komponen provinsi yang terhubung pada LINK. Agama yang sama di dua sisi wilayah agama lain mendapat label terpisah, sehingga nama tidak membentang di atas wilayah yang berbeda. Perubahan mode membersihkan cache label dan warna. Perubahan agama provinsi juga membatalkan cache view agama pada frame berikutnya, tanpa perlu mengganti filter kembali.

## Akses dan alur transaksi

Buka **Ekonomi → Sumber daya → Dagang antarkerajaan**, atau **Diplomasi → kerajaan → Dagang sumber daya**. Pilih mitra, jumlah **5/10/20 unit**, lalu Beli/Jual pada pangan, kayu, besi atau rempah. Tombol menyebut total pembayaran/penerimaan bersih. Mitra, stok kedua pihak, dana dagang mitra, lama pengiriman, ongkos dan alasan penolakan terlihat sebelum pesan. Ganti mitra kembali ke daftar tanpa memenuhi layar dengan seluruh daftar di bawah setiap penawaran.

Unit adalah jumlah stok abstrak dalam permainan, bukan ton atau jumlah kapal. Pangan dikonsumsi pasukan/provinsi, kayu dipakai pengolahan dan pembangunan kapal, besi dipakai kapal tertentu dan rekrut MIL 4+, sedangkan stok rempah terutama untuk diperdagangkan. Nilai dagang komoditas provinsi dihitung terpisah dari jumlah stok fisik.

Maksimal tiga kiriman aktif. Barang sumber dan pembayaran pembeli ditahan ketika pesanan disepakati. Harga dikunci selama perjalanan; saat tiba, barang masuk gudang pembeli dan penjual menerima pembayaran. Ekspor pemain menghasilkan dukat setelah tiba, bukan saat klik. Pembatalan manual, perang atau hilangnya kerajaan mitra mengembalikan barang dan pembayaran penuh. Perang diperiksa setiap hari permainan. Satu pesanan hanya dapat diselesaikan/dibatalkan sekali.

Pemesanan memakai stok fisik yang sudah ada. Bahan yang sedang dikirim tidak bisa sekaligus dipakai untuk kapal, bangunan atau rekrut. Ruang gudang dicadangkan pada pengirim (untuk kemungkinan refund) dan penerima (untuk kedatangan). Produksi dan pasar lokal menghormati kapasitas efektif ini; kapasitas kembali setelah kiriman selesai. Ini mencegah produksi mengisi ruang yang dibutuhkan untuk pengembalian atau pengiriman.

## Kesediaan dan jangkauan

- Kedua kerajaan masih hidup dan tidak berperang; hubungan harus lebih dari −75.
- Berbatasan melalui LINK darat/selat, atau kedua pihak memiliki provinsi berpantai.
- Jarak ibu kota maksimal `650 + 60×teknologi DIP` satuan dunia.
- Lama kiriman `ceil(jarak/16)+5` hari, dibatasi 10–60; ongkos `ceil(jarak/120)+1` dukat, dibatasi 2–8.
- Mitra menjaga cadangan ketika menjual: pangan minimal max(5, 0,3×resimen + 0,5×provinsi), kayu 3, besi 1; rempah tanpa batas cadangan tambahan.
- Stok, kas, dana mitra dan kapasitas diperiksa ulang saat klik. Jika harga berbeda dari yang ditampilkan, pesanan tidak dibuat dan penawaran harus diperiksa kembali.

Jalur dagang adalah abstraksi waktu/jangkauan, tidak menciptakan kapal pengangkut atau berjalan sebagai unit peta. Selat pendek dianggap perbatasan dagang. Hak akses militer bukan syarat perdagangan. Belum ada blokade, intersepsi kargo, privateer atau diplomasi embargo terpisah.

## Harga dan insentif

Harga dasar per unit: pangan 2, kayu 3, besi 5, rempah 6 dukat. Harga tengah mitra = dasar × clamp(1,4 − stok mitra/150, 0,65, 1,4). Harga beli pemain memakai pengali `1,15 − kedekatan`; harga jual memakai `0,75 + kedekatan`. Kedekatan = hubungan positif×0,0005, ditambah 0,04 untuk sekutu atau bawahan pemain, maksimal 0,12. Beli dibulatkan ke atas, jual ke bawah; ongkos ditambah untuk impor atau dikurangi dari hasil ekspor.

Surplus membuat barang murah, kelangkaan membuatnya mahal; hubungan baik memperkecil selisih beli/jual. Rute yang jauh lebih menguntungkan untuk kiriman besar karena ongkos tidak berlipat per unit. Perdagangan antar-mitra dapat memberi peluang arbitrase, tetapi dibatasi stok nyata, dana, waktu dan tiga kiriman, bukan uang tanpa batas dari satu tombol.

Pasar lokal yang sudah ada tetap menjadi alternatif instan: beli lima unit dengan harga dasar×1,8×5 (dibulatkan naik), jual dasar×0,45×5 (dibulatkan turun). Spread lebih lebar dan harga per barang menghindari pasar lama yang membeli/menjual semua bahan pada harga tetap, yang dapat merusak harga perdagangan antarkerajaan.

Setiap kiriman sukses memberi hubungan +2, maksimal +6 per mitra per tahun. Hadiah ini tidak berulang dari klik penyelesaian lama. Tiap enam bulan, AI dapat menawarkan sepuluh unit barang yang stok pemainnya rendah; dipilih dari mitra yang bersedia dan terjangkau dengan harga termurah. Tawaran dapat dilewati dan tidak mendebit apa pun sampai diterima serta divalidasi lagi.

## Ekonomi AI dan data

`G.resourceTradeGold` adalah dana khusus dagang AI: awal min(500, 80+2×development awal), bertambah max(2, 0,12×development aktual) per bulan sampai 2000 melalui pemulihan; pendapatan ekspor aktual bisa melampaui angka tersebut. Dana didebit saat AI membeli dan dikreditkan ketika AI menjual. Ini bukan ledger lengkap kas kerajaan AI.

`G.resourceOrders` menyimpan barang, negara sumber/tujuan, harga, ongkos, jumlah dan sisa waktu. `G.resourceTradeLog` menyimpan 20 catatan, dan `G.resourceGoodwill` membatasi hadiah hubungan tahunan. `fixResourceTrade` memigrasi save tanpa mengubah stok lama atau mengisi ulang dana AI yang sudah nol. Pesanan disimpan dan melanjutkan perjalanannya setelah Lanjut. Keputusan dagang AI pada tahap ini berupa penawaran/penilaian kepada pemain; perdagangan otomatis sesama AI, barter bahan, kontrak bulanan dan pasar harga global belum tersedia.

## Verifikasi

`tests/t37_resource_diplomacy_labels.py` memeriksa label besar/kecil, teks canvas aktual, pergantian filter, konversi agama, harga, stok dan escrow, pengiriman impor/ekspor, debit dana AI, penyelesaian sekali, refund manual/perang, kelangkaan, kapasitas/produksi gudang, spread, diskon hubungan, harga kedaluwarsa, tiga slot, save/migrasi, goodwill dan tawaran AI. UI pemesanan juga diklik melalui browser. Screenshot view Agama, panel mitra dan harga diperiksa pada 780×360. Seluruh regresi melalui `npm test`; belum dites pada HP fisik atau penyeimbangan kampanye panjang pemain.
