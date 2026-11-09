# Perbaikan kedipan dan layar hitam setelah ekspansi peta

Peta Asia Timur memperbesar luas dunia dari sekitar 1,1 menjadi 3 juta unit persegi. Tekstur memakai faktor tetap 1,2 dan cache dunia 1,25, sehingga beberapa canvas mencapai 4,3–4,7 megapiksel. Selain backing store, generator memakai ImageData dan tiga Float32Array berukuran sama. Pengujian desktop sebelumnya tidak membatasi alokasi ini.

Pengukuran instrumen canvas di Chromium, viewport 360×800, DPR 3: jumlah backing store canvas pada startup build sebelumnya mencapai 100.536.896 byte; sesudah perbaikan 19.075.428 byte. Ini hitungan ukuran RGBA canvas yang dialokasikan, bukan pengukuran seluruh RAM/GPU perangkat. Dengan simulasi penolakan permukaan lebih dari 2 megapiksel, build lama gagal membuat context; build baru berjalan tanpa penolakan. Ini bukti masalah alokasi yang diperbaiki, bukan bukti bahwa crash pada HP pemilik mempunyai penyebab tunggal yang sama.

Perbaikan:
- Tekstur daratan dan cache dunia masing-masing sekitar satu megapiksel, air 0,4 megapiksel, terlepas dari pertumbuhan luas peta.
- Detail batas, teks dan objek tetap digambar pada resolusi viewport. DPR layar sentuh maksimal 1,5; backing store utama sekitar 1,5 megapiksel maksimal.
- Canvas sementara dilepas segera; kegagalan pembuatan tekstur beralih ke warna peta dasar.
- Resize yang tidak mengubah ukuran tidak mengalokasikan ulang canvas. Event resize digabung per frame; cache memeriksa tinggi sekaligus lebar, termasuk perubahan bilah alamat Android.
- Context utama yang pulih memicu pembuatan ulang pola/cache. Tidak mengubah field gameplay atau menghapus localStorage.

`tests/t39_mobile_render.py` menjalankan viewport portrait 360×800 dan 720×1280 dengan DPR 3 dan touch, batas canvas, rotasi, perubahan tinggi viewport, pemulihan context sintetis, pemeriksaan piksel, keutuhan save dan kegagalan tekstur. Bukan tes pada HP fisik atau simulasi crash seluruh proses browser.
