# Audio situasional Nusantara

Audio dibuat langsung dengan WebAudio dan tetap bekerja tanpa mengunduh berkas musik. Musik memakai motif pentatonik yang terinspirasi gamelan, gong rendah, dan perkusi yang terinspirasi kendang. Ini komposisi prosedural untuk game, bukan rekaman instrumen asli atau rekonstruksi laras suatu daerah.

## Suasana

- **Damai/menu awal:** motif renggang, register lembut, gong sebagai penanda frasa.
- **Perang kerajaan pemain:** pola berulang pada register lebih rendah, pulsa bass, kendang lebih teratur dan isyarat tiup yang jarang.
- **Pertempuran pemain:** menambah lapisan ritme pada musik perang; kembali ke perang setelah pertempuran selesai, lalu damai setelah seluruh perang pemain berakhir.

Pengendali membaca `warsOf(G.nat)` dan pertempuran aktif yang melibatkan pemain. Perang sesama AI tidak mengubah suasana pemain. Waktu game yang dijeda tidak mematikan musik. Menyembunyikan tab menangguhkan konteks audio; kembali ke tab melanjutkannya sesuai kebijakan browser.

Satu scheduler 100 ms menjadwalkan maksimal 300 ms ke depan, dengan pulsa dasar 0,46 detik. Motif damai dimainkan lebih renggang pada pulsa yang sama, sehingga pergantian tetap berirama. Tiga bus suasana berpindah memakai ramp eksponensial dengan konstanta waktu 0,45–0,65 detik, bukan memotong suara lama. Musik merendah sementara saat notifikasi penting agar pesan terdengar jelas.

## Efek dan pencampuran

Klik/menu memakai nada pendek dengan attack lembut, harmonik rendah dan jalur kering. Efek bangunan, rekrut, diplomasi, perdagangan, inti, perang, hasil pertempuran dan event memiliki isyarat yang berbeda. Desis benturan dibatasi frekuensinya; tiupan memakai bentuk gelombang yang lebih halus. Toast umum tidak lagi selalu memicu bunyi.

Efek permainan dan musik melewati low-pass 6,2 kHz serta reverb pendek 0,9 detik dengan wet 10%. Klik menu tetap kering. Compressor dan limiter mengendalikan puncak campuran; master gain 0,7. Nilai ini adalah pengaturan engine, bukan jaminan loudness identik di semua speaker.

Bus terpisah untuk antarmuka, efek permainan dan musik mencegah perkusi musik masuk ke jalur efek. Ini memperbaiki kebocoran drum dari sistem sebelumnya. Batas jeda per efek dan keluarga mencegah klik/benturan/notifikasi bertumpuk terlalu cepat. Maksimal 56 sumber aktif, dengan oscillator, buffer source dan node pendukung diputus saat suara selesai. Generator acak audio memiliki seed sendiri agar tidak menghabiskan RNG gameplay.

## Kontrol

**Menu → Audio** menyediakan sakelar efek/musik serta slider 0–100 untuk klik/menu, efek permainan dan musik. Default masing-masing 65%, 65%, 40%. Nilai tersimpan dalam `nus_snd.levels`, terpisah dari save kampanye. Preferensi lama yang hanya punya `sfx`/`mus` tetap dihormati. Tombol speaker peta tetap menjadi kontrol hidup/mati cepat.

Audio baru dimulai setelah interaksi pengguna bila browser memerlukannya. Menonaktifkan musik menghentikan penjadwalan nada baru; sisa suara memudar lewat bus musik. `SFX.pauseAll` dipakai oleh perubahan visibilitas. Jangan membuat AudioContext atau interval baru setiap deklarasi perang.

## Verifikasi dan batas

`tests/t35_adaptive_audio.py` mengukur keluaran audio browser untuk damai, perang dan pertempuran, memeriksa mode, mengabaikan perang AI yang tidak terkait, menguji mute, slider/persistensi, preferensi lama, suspend/resume dan pembersihan sumber. `t33` tetap memeriksa amplitudo gain klik; inspeksinya kini membedakan parameter gain dari perubahan frekuensi. Seluruh regresi melalui `npm test` dan tampilan slider diperiksa pada viewport 780×360.

Pengukuran browser memeriksa keluaran non-senyap dan headroom pada sampel uji; belum merupakan audit LUFS atau penilaian musik lewat speaker/headphone fisik. Audio tetap sintesis, bukan orkestrasi atau sample instrumen akustik. Penyeimbangan persepsi pada HP sungguhan masih memerlukan umpan balik pemain.
