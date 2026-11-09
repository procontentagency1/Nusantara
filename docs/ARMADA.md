# Armada awal dan kontrol view peta

## Armada yang tersedia

Kerajaan dengan provinsi berpantai mendapat satu armada pada awal kampanye. Pantai memakai geometri `p.cd`, bukan label medan saja: daerah pegunungan di pulau seperti Bali tetap bisa memiliki pelabuhan. Negara tanpa pantai tidak mendapat kapal. Kelompok awal menurut jumlah provinsi pesisir:

| Provinsi pesisir | Armada awal |
|---|---|
| 5 atau lebih | 2 jung tempur, 3 patroli, 1 perahu dayung |
| 2–4 | 1 jung tempur, 1 patroli, 1 perahu dayung |
| 1 | 1 patroli, 1 perahu dayung |

Majapahit mendapat enam kapal di Tuban. Armada sendiri terlihat sebagai kapal layar dengan angka jumlah kapal, dapat diketuk dan dipilih melalui **Militer → Armada kapal**. Armada lain ditampilkan ketika zoom mendekat atau sedang bermusuhan. Gambar adalah simbol kelompok, bukan satu gambar per kapal.

Pemilihan pelabuhan awal mengutamakan medan pesisir, rank kota lalu ID. Jumlah kapal adalah angka desain untuk mengawali permainan, bukan klaim daftar armada sejarah tahun 1350. Sumber riset sejarah dan EU4 tetap di `ARMADA_DAN_PASUKAN.md`.

## Pelayaran dan pengelolaan

Pilih armada lalu ketuk laut untuk berlayar, atau provinsi pantai sendiri yang tidak diduduki untuk sandar. Panel armada juga menyediakan daftar laut, kembali ke pelabuhan, siaga dan jaga perdagangan. Lokasi ikon saat sandar adalah titik air terdekat dari provinsi pelabuhan.

Navigasi memakai mask daratan dari geometri peta pada grid 8 satuan dunia. Hanya air yang terhubung dengan batas samudra dapat dilalui; danau tertutup tidak menjadi jalur laut. Pencarian jalur delapan arah melarang diagonal yang memotong sudut daratan. Kecepatan 12 satuan dunia per hari. Rute tetap di atas air menurut grid; ini bukan simulasi kedalaman, angin atau arus. Simbol kapal dapat menutupi garis pantai karena ukuran gambarnya, tetapi titik/rute navigasinya di air.

| Jenis | Dukat | Kayu | Besi | Waktu | Pemeliharaan/bulan | Kekuatan |
|---|---:|---:|---:|---:|---:|---:|
| Jung tempur | 30 | 8 | 2 | 6 bulan | 0,25 | 5 |
| Kapal patroli | 18 | 4 | 0 | 4 bulan | 0,12 | 2 |
| Perahu dayung | 12 | 3 | 0 | 3 bulan | 0,08 | 2,5 |

Satu pembangunan aktif per pelabuhan. Biaya dibayar sekali ketika antrean dibuat. Pendudukan menunda pekerjaan; kehilangan kepemilikan membatalkan antrean tanpa refund. Kapal selesai masuk armada yang sedang sandar di situ atau membentuk kelompok baru. Perbaikan di pelabuhan sendiri yang tidak diduduki memulihkan 15 poin lambung per kapal per bulan, tanpa biaya reparasi tambahan. Pemeliharaan masuk `e.navalCost` dan saldo kas bulanan, terpisah dari pemeliharaan tentara.

Menjaga perdagangan memberi **+2 kekuatan dagang per kapal patroli × kondisi lambung**, setelah tiba di node laut tujuan dan tidak bersandar/mundur. Armada tidak menambah kekuatan selama perjalanan. Node laut memakai pemetaan eksplisit ke tujuh node dagang yang sudah ada. Ini tugas menjaga satu perairan, belum loop patroli beberapa laut.

## Pertempuran dasar dan AI

Armada musuh yang sama-sama di laut, tidak sedang mundur dan berjarak maksimal 22 satuan dunia bertukar kerusakan harian. Kekuatan dibobot kondisi lambung; kerusakan = 1,5×kekuatan lawan dan dibagikan dari kapal terdepan. Kapal nol lambung tenggelam. Satu kelompok melawan satu kelompok per hari; belum ada pertempuran gabungan atau panel taktik laut EU4.

Armada mencoba mundur ketika kehilangan separuh jumlah kapal saat mulai pertempuran atau rata-rata lambung di bawah 35%. Masa mundur 20 hari mencegah serangan dan intersepsi ulang. Armada bersandar tidak bertempur. Kapal yang kehilangan pelabuhan keluar dari status sandar. Aneksasi penuh membersihkan armada negara yang lenyap.

AI berangkat menjaga perdagangan saat damai, kembali memperbaiki kapal yang rusak, serta mengejar armada musuh di laut ketika perkiraan kekuatannya memadai. Ekonomi pembangunan kapal AI belum setara pemain dan kapal tenggelam belum otomatis diganti. Angkutan resimen, blokade, pelaut, laksamana, penangkapan kapal, naval force limit dan bonus perahu dayung menurut jenis laut belum tersedia. Hubungan selat untuk tentara tetap berfungsi sampai transportasi laut lengkap.

## Save

`G.fleets` menyimpan identitas, negara, pelabuhan/laut, posisi, jalur, misi, lambung tiap kapal dan status mundur/pertempuran. `G.shipQueue` menyimpan antrean pembangunan. `fixNavy` memberi armada awal sekali kepada save lama yang belum memiliki field armada; kampanye yang sudah memiliki array kosong tidak diisi ulang. Armada memakai `G.nid` bersama agar ID unik. Grid navigasi dibuat sekali per halaman dan tidak masuk save; jalur disimpan sebagai koordinat dunia.

## View peta tanpa minimap

Canvas minimap, tombol collapse, lima tombol mode lama, drag handler dan proses render minimap dihapus. Penggantinya satu tombol **Peta: … ▾** di kanan bawah. Dropdown menyediakan Politik, Medan, Agama, Sumber daya dan Perdagangan; tidak ada tombol placeholder nonaktif. Memilih mode menutup dropdown; klik di luar atau Escape juga menutupnya. Tombol menyatakan `aria-expanded`, dan pilihan menyatakan `aria-pressed`.

Mode agama mewarnai agama provinsi; sumber daya mewarnai pangan/kayu/besi/rempah; perdagangan mewarnai tujuh node. Legenda ringkas berada dalam dropdown. Pilihan menghapus cache warna dan merender ulang peta. View bukan perubahan kepemilikan atau ekonomi.

## Verifikasi dan batas

`tests/t36_navy_mapviews.py` memeriksa armada awal kerajaan pesisir, biaya, rute air, kedatangan, sandar, perbaikan, antrean/biaya sekali, pembangunan selesai, bonus dagang, pertempuran/mundur, save/migrasi tanpa duplikat, warna filter, penghapusan minimap serta interaksi dropdown/Escape. Screenshot viewport HP 780×360 mencakup panel armada, kapal di peta dan dropdown. `t27_trade` diperbarui untuk komponen biaya laut yang disengaja; seluruh regresi melalui `npm test`. Belum dites pada HP fisik atau penyeimbangan kampanye panjang pemain.
