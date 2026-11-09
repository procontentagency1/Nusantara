# Penaklukan dan penataan wilayah

## Riset dan pilihan desain

[Manual resmi EU4, Stability and Expansion, sekitar halaman 50](https://forumcontent.paradoxplaza.com/public/79250/EuropaUniversalisIV_Manual.pdf) menghubungkan wilayah noninti, overextension, biaya administrasi dan pemberontakan; panel mengizinkan pemain memantau pembentukan inti serta tuntutan pemberontak. Ini mendasari siklus **pilih sasaran → menang perang → pilih tuntutan → tata wilayah → lanjut ekspansi**. Cuplikan bagian ini dapat dibaca melalui penelusuran; pembukaan PDF penuh melewati batas ukuran alat. Wiki Overextension/Local Autonomy mengembalikan 401 pada sesi riset ini.

[Catatan developer Paradox tentang Age of Absolutism](https://store.steampowered.com/news/posts/?appids=236850&enddate=1484648480&feed=steam_community_announcements) menunjukkan otonomi, penanganan keras dan penerimaan tuntutan pemberontak sebagai tindakan politik yang berbeda. Nusantara memakai pilihan tersebut tanpa menyalin sistem absolutisme era 1600-an ke tahun 1350.

[Catatan resmi EU4 1.35](https://store.steampowered.com/news/posts/?appids=236850&enddate=1681831257&feed=all) juga memperlihatkan hubungan administrasi provinsi, otonomi dan biaya pemerintahan. Angka pada implementasi di bawah adalah rancangan Nusantara, bukan klaim menyalin formula atau versi/DLC EU4 tertentu.

Peta Nusantara sudah berisi kerajaan dan masyarakat. Paket ini memperdalam penaklukan serta integrasi wilayah yang ada; tidak menganggap daerah berpenduduk sebagai tanah kosong untuk kolonisasi.

## Alur yang dapat dimainkan

Menu **Kerajaan → Ekspansi & integrasi** merangkum beban ekspansi, wilayah bermasalah dan peluang perbatasan. Peluang mengutamakan inti yang hilang, klaim dan barang bernilai. Memilihnya membuka provinsi/diplomasi yang sudah ada. Sasaran tetap dipilih pemain; ini bukan perintah menaklukkan otomatis.

Layar damai menampilkan biaya skor perang, AE, biaya ADM untuk inti nanti, DIP tuntutan tanpa klaim, overextension sesudah perjanjian, perkiraan calon koalisi di sekitar, dan masa gencatan. Daftar tuntutan tidak lagi dibatasi 14 provinsi. Perkiraan dan pelaksanaan memakai fungsi yang sama. Tawaran damai dari AI menyebut biaya wilayah yang diterima. Semua penyerahan diperiksa ulang terhadap pendudukan dan pihak perang aktual.

| Keputusan | Konsekuensi aktual |
|---|---|
| Menuntut wilayah tanpa klaim/inti | 2 DIP/development, diperiksa saat pelaksanaan |
| Memiliki klaim | Diskon biaya inti 25%, tidak memakai DIP tuntutan wilayah tersebut |
| Merebut inti sendiri | AE 25% dari development, tanpa overextension, langsung berstatus inti |
| Aneksasi baru | Separatisme 30 tahun, otonomi 35%, belum inti |
| Mulai inti | Bayar ADM sekali, proses 24 bulan; berhenti sementara saat diduduki atau perlawanan aktif |
| Menyelesaikan inti | Menghapus overextension wilayah, menghilangkan penalti hasil noninti; +3 prestise dan +10 ADM sekali per negara/provinsi |
| Otonomi +25 | Hasil turun; keresahan −10 selama 120 bulan; perubahan berikutnya setelah 120 bulan |
| Otonomi −25 | Hasil naik; keresahan +5 selama 120 bulan dengan cooldown yang sama |
| Penanganan keras | 30 MIL untuk −30 progres perlawanan, jeda 6 bulan; tidak bisa menghentikan pemberontakan yang sudah aktif |
| Pulihkan kerajaan taklukan sebagai vasal | Memerlukan damai, penguasa merdeka, calon kerajaan sudah lenyap dan masih punya inti di tanah pemain; konfirmasi menyebut seluruh wilayah. Ibu kota pemain dikecualikan. Vasal kemudian mengikuti aturan kesetiaan/integrasi yang sudah ada |

Biaya provinsi sekarang berdasarkan development absolut: `5 + 2×development + 8 bila ibu kota`, diskon inti 50%, klaim 15%, sasaran terpilih 10%; hasil 6–100 poin. Formula lama berdasar persentase development seluruh negara bisa membuat satu ibu kota kecil berharga lebih dari 100 poin. Aneksasi kerajaan kecil kini mungkin, sedangkan kerajaan besar tetap dapat memerlukan beberapa perang.

Gencatan 60–180 bulan menurut nilai tuntutan, termasuk ganti rugi/vasalisasi. Perdamaian putih tetap lima tahun. Daftar pihak disalin sebelum negara lenyap agar truce tidak hilang ketika daftar peserta dibersihkan. AE lokal: reconquest 0,25×development, penaklukan beralasan 1×, tanpa alasan 1,25×; vasalisasi +8. Klaim biasa tidak menghapus AE. Koalisi kini membuang anggota yang lenyap, menjadi bawahan/sekutu, memiliki truce, atau hubungan membaik melewati ambang.

## Pengelolaan dan perlawanan

Overextension = 4% per development noninti. Tambahan keresahan daerah taklukan = OE×0,05; di atas 100%, progres perlawanan tumbuh 50% lebih cepat. Hasil pajak, produksi dan tenaga = `(1 − otonomi/100) × (inti ? 1 : 0,5)`. Development asli tidak dikurangi; dasar pinjaman tetap menggunakan development asli. Otonomi turun 0,1/bulan saat damai tanpa perlawanan.

Keresahan daerah mempertimbangkan sisa separatisme/24, +4 bila noninti, OE, kelelahan perang, stabilitas, agama, perubahan otonomi dan garnisun. Garnisun menekan sampai 5 keresahan; pasukan harus diam, tidak bertempur, tidak berlatih, moral minimal 50% dan pemeliharaan minimal 50%. Progres bulanan = keresahan positif×0,35 (dengan penalti OE di atas), atau turun 3 bila keresahan tidak positif.

Pada 70%, peringatan yang menghentikan waktu menawarkan meninjau daerah. Pada 100%, perlawanan aktif menghentikan pajak/produksi/tenaga, kontribusi dagang dan sumber daya serta menunda inti. Ini **perlawanan provinsi abstrak**, belum pasukan pemberontak bergerak dengan pertempuran individual. Pemain dapat:

- Mengirim 2–6 resimen siap tempur sesuai development. Garnisun cukup menurunkan perlawanan 25 poin/bulan sampai padam.
- Menerima tuntutan: perlawanan selesai dengan otonomi minimal 75%, keresahan turun sementara dan sisa separatisme berkurang lima tahun. Opsi ini tetap tersedia bila perubahan otonomi biasa sedang cooldown.
- Membiarkan enam bulan tanpa garnisun cukup: provinsi kembali ke negara asal yang tercatat, yang dapat bangkit lagi. Truce lima tahun terbentuk; tentara penguasa yang tertinggal pulang sebagai exiled.

Pendudukan asing menunda proses lokal dan timer tuntutan. Keadaan tidak menghasilkan perlawanan instan tanpa progres/peringatan. Separatisme tidak langsung hilang saat inti selesai; stabilisasi masih bernilai setelah kemenangan administratif.

AI otomatis memulai inti 36 bulan tanpa ledger ADM penuh, memberi otonomi saat gejolak tinggi, mengirim tentara ke perlawanan saat damai, dan menahan perang baru di atas 80% OE, AE 50, atau saat ada perlawanan aktif. Tuntutan AI memprioritaskan inti, sasaran, klaim, perbatasan dan barang, dengan batas proyeksi OE 120%. Ini penyederhanaan ekonomi/strategi AI; belum setara seluruh keputusan pemain.

## Data, kompatibilitas dan batas

`G.cores[id]` menyimpan inti per negara, termasuk inti baru setelah penaklukan, sehingga reconquest tidak hanya mengenal peta 1350. `G.expansion[id]` menyimpan otonomi, separatisme, progres/timer perlawanan, timer inti, cooldown dan negara tujuan pemisahan. `G.integrationRewards` mencegah hadiah berulang lewat perebutan ulang. `G.provinceArchive` mempertahankan development/bangunan pemain setelah transfer dan perebutan ulang; pengolahan sumber daya juga tetap melekat pada provinsi.

Save lama dengan `q.nc` positif meneruskan hitungan lama tanpa harus membayar lagi; wilayah lama yang sudah inti tetap inti. Penaklukan baru harus memulai administrasi secara eksplisit. Integrasi vasal memberi inti langsung karena biaya DIP integrasi sudah dibayar melalui sistem sebelumnya.

AE masih satu nilai per penakluk, bukan matriks pendapat tiap pengamat dengan budaya/agama/jarak seperti EU4. Belum ada governing capacity, state/territory, budaya diterima, separate peace, transfer occupation, pelepasan negara sebagai tuntutan damai, atau colonist. Armada/angkut masih tahap terpisah. Daftar calon koalisi adalah perkiraan berdasarkan posisi/hubungan saat ini. Tidak ada klaim bahwa keseimbangan final atau rasa bermain sudah identik dengan EU4.

## Pengujian

`tests/t34_conquest.py` memeriksa biaya aneksasi kecil, pratinjau vs pelaksanaan, ADM/DIP, larangan inti otomatis, pendudukan yang menunda inti, hadiah sekali, otonomi/cooldown, perlawanan/garnisun/pemisahan, negosiasi, penanganan keras, bangunan yang bertahan, inti dinamis/reconquest, respons AI, migrasi, aneksasi penuh tanpa pasukan hantu, truce, dan pelepasan vasal dengan konfirmasi. Screenshot panel serta bagian bawah layar damai diperiksa pada viewport HP 780×360. Seluruh regresi melalui `npm test`; belum diuji di HP fisik atau kampanye panjang pemain.
