# Audit perdagangan awal

Pemeriksaan pada build peta Asia Timur, kampanye baru 1 Januari 1350, sebelum waktu berjalan. Angka adalah contoh desain, bukan perkiraan sejarah; keputusan negara, harga, perang, modifier dan perilaku AI mengubah hasil.

## Hasil yang sudah bekerja

- Jaringan sepuluh node menghitung nilai lokal/masuk, pangsa dan pendapatan bulanan. Pedagang tiba setelah 30 hari, dapat mengumpulkan atau mengarahkan nilai; provinsi, pasar, pendudukan dan kapal patroli memengaruhi kekuatan. Income masuk anggaran kerajaan pemain.
- Stok pangan, kayu, besi dan rempah diproduksi serta dipakai. Kiriman antarkerajaan memakai harga menurut stok mitra, dana, jarak, ongkos dan waktu; perang membatalkan dan mengembalikan escrow. Kiriman berhasil memberi hubungan diplomatik dan dapat membuka jalur pengaruh komunitas serta penyebaran lembaga selama lima tahun.
- Armada patroli memberi kekuatan dagang ketika sudah tiba di laut tujuan. Wabah global memiliki dampak pada perdagangan dan sumber daya. Semua ini adalah mekanisme aktual, bukan angka dekoratif.

## Angka contoh Majapahit

Ekonomi awal: pajak 6,67, produksi 7,70, dagang 3,70 dukat/bulan; surplus 15,71 setelah komponen lain termasuk hubungan bawahan dan biaya. Menempatkan pedagang pada node utama dan menunggu tiba meningkatkan dagang sekitar 0,42/bulan dalam snapshot itu. Satu pasar di Wilwatikta seharga 100 menambah sekitar 0,13 dagang dan 0,08 produksi/bulan: balik modal sederhana sekitar 39 tahun setelah selesai, jika keadaan lain tetap.

Tiga kapal patroli awal yang sudah dimiliki dan menjaga node Jawa menambah sekitar 0,14 dagang/bulan pada snapshot itu. Pemeliharaan tiga kapal tersebut 0,36/bulan; membangun tiga kapal baru hanya untuk manfaat tersebut akan merugi pada kondisi awal yang diuji, belum termasuk harga pembangunan. Bila sudah memiliki kapal, kenaikan itu merupakan tambahan pendapatan dengan biaya tetap armada yang sudah dibayar. Nilai berubah sesuai persaingan dan node.

## Keterbatasan dan prioritas

1. UI belum menunjukkan pratinjau perubahan pendapatan atau perkiraan balik modal sebelum menugaskan pedagang/kapal atau membangun pasar; strategi sulit dinilai tanpa membandingkan angka manual.
2. Kekuatan dagang AI ada, tetapi aliran AI tanpa perintah mengikuti keluaran pertama node. `tradeSnapshot().incomes` menghitung pendapatan AI, namun tidak membayar kas penuh AI; dana dagang dan dana pengembangan AI masih dua anggaran abstrak. AI belum berdagang sumber daya secara otomatis dengan AI lain.
3. Jalur kiriman adalah abstraksi jarak dan waktu, bukan kapal kargo yang dapat dicegat. Belum ada embargo terpisah, pembajakan atau blokade. Perang membatalkan pengiriman dan mengembalikan escrow penuh.
4. Harga mitra dipengaruhi stok, tetapi belum ada harga pasar global yang berubah akibat permintaan seluruh kerajaan, kontrak jangka panjang atau aliran pasokan otomatis. Pasar lokal tetap tersedia instan dengan spread lebih besar.
5. Sepuluh node dan dua pedagang awal memberi pilihan dasar, tetapi sasaran dagang, persaingan diplomatik dan dampak kelangkaan masih sederhana. Keseimbangan perlu sesi kampanye sungguhan, bukan dianggap selesai dari tes fungsi.

Urutan pengembangan yang disarankan: tampilkan dampak/ongkos dulu; kemudian berikan AI anggaran dan keputusan dagang yang sungguh memakai hasil dagang; baru tambahkan risiko jalur/blokade dan kontrak, beserta penyeimbangan serta migrasi save. Hindari memberikan AI kas tambahan dua kali dari snapshot; stok/escrow harus tetap dijaga.
