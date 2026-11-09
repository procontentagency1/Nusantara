# Ekspansi Asia Timur — paket awal 1350

Riset: [RISET_ASIA_TIMUR.md](RISET_ASIA_TIMUR.md). Data: `data/east-asia.json`; geografi: `tools/seeds.mjs`. Peta baru berisi 228 provinsi (187 darat, 41 laut), 86 negara; bertambah 85 daratan, 13 lautan dan 17 negara. Seluruh 130 ID lama dipertahankan.

## Negara dan konten

Negara baru: Yuan, Goryeo, Ashikaga, Yoshino, Hokuzan, Chuzan, Nanzan, Komunitas Ainu, Komunitas Taiwan, Dai Viet, Sukhothai, Lan Na, Muang Sua, Pinya, Sagaing, Hanthawaddy, Mong Mao. Profil Siam, Khmer dan Champa turut diperluas. Semua dapat dipilih melalui dropdown kerajaan di layar awal. Menu peta mempunyai pintasan Nusantara, Tiongkok dan Jepang/Korea.

Dua puluh profil menyediakan budaya, pusat politik, busana, pemerintahan dan konteks teknologi ADM/DIP/MIL. Gambar memakai sembilan kelompok regional: Tiongkok, Korea, Jepang, Ryukyu, Ainu, Taiwan, Vietnam, daratan Asia Tenggara, Champa. Pasukan dan bangunan dibedakan dalam siluet; arsitektur Majapahit dan Nusantara yang sudah ada tetap tersedia. Agama negara/provinsi serta warna/label mencakup tradisi Tionghoa, Vajrayana, Shinto-Buddha, Ryukyu dan Ainu. Goryeo memulai sebagai negara upeti Yuan, bukan vasal.

Setiap profil mendapat empat misi tambahan, total 80. Misi memakai stok pangan, teknologi ADM, kiriman sumber daya yang benar-benar tiba, stabilitas/integrasi; Jepang dan Ryukyu mempunyai sasaran penyatuan serta hadiah klaim. Perebutan sasaran oleh negara ketiga tidak menyelesaikan misi penyatuan pemain. Hadiah sekali: mana/prestise, biaya teknologi −5% lima tahun, atau efisiensi dagang +10% lima tahun. Tradisi awal per profil memberi modifier kecil; semua mulai teknologi 3 untuk keseimbangan.

Tambahan 42 event / 84 pilihan: dua per profil dan dua khusus Jikji 1377 serta Yuan pasca-1368. Biaya pendapatan/mana dan perubahan stabilitas/legitimasi/modifier diterapkan ke state permainan. Pilihan reformasi Goryeo setelah 1351 mengganti penguasa menjadi Gongmin dan tersimpan. Event what-if diberi konteks; belum ada kemunculan otomatis Ming/Joseon atau perang Nanbokucho otomatis. Dua puluh profil memakai kerangka mekanis yang serupa dengan judul/konteks lokal; belum dua puluh sistem politik unik.

Jaringan dagang bertambah dari tujuh menjadi sepuluh node: Nippon dan Korea mengalir ke Hangzhou, kemudian Siam/Malaka. Negara AI memakai sumber daya, armada, diplomasi dan keputusan dinamis yang sudah ada; pencapaian misi regional memeriksa kondisi kampanye dan muncul di Kabar Kerajaan. Simulasi AI tetap abstrak: tidak mendapat seluruh mana, pilihan event dan pohon misi interaktif yang identik dengan pemain.

## Migrasi dan pengujian

`G.mapVersion` dan `DATA.legacyTransform` menangani perubahan ukuran peta. Migrasi menambahkan wilayah/negara baru, mempertahankan kepemilikan, bangunan, klaim dan progres lama, mengubah koordinat kapal dan merencanakan ulang jalurnya. Jangan mengalokasikan ulang ID provinsi saat membangun peta. Jangan menambahkan ulang pasukan pada save yang sudah dimigrasi. Save versi lama tidak dapat dibuka kembali dengan kode peta sebelum ekspansi.

`tests/fixtures/legacy-east-save.json` adalah save sintetis yang dibuat memakai build sebelum ekspansi; tidak memuat data pemain. `t38_east_asia.py` memeriksa migrasi, seluruh profil, 84 pilihan, hadiah sekali, kronologi, reset penguasa, syarat penyatuan, aktivitas AI, navigasi dan pemilihan negara. `t29` mengukur skala/hitbox setelah peta membesar dan membandingkan gaya bangunan; tes dagang diperbarui ke sepuluh node. Screenshot menggunakan Chromium pada viewport 780×360; belum pengujian HP fisik atau keseimbangan kampanye panjang.

Batas sejarah: provinsi hasil pembagian geometris, bukan batas terverifikasi 1350; daerah Ainu/Taiwan mewakili komunitas majemuk. Penguasa yang belum terverifikasi memakai profil dewan bertanda contoh. Busana/bangunan adalah interpretasi kecil untuk peta, bukan rekonstruksi setiap suku. Angka teknologi dan efek tradisi adalah rancangan permainan.
