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

## Cache tajam saat digeser

Cache detail memiliki cadangan hingga 12% di tiap sisi dengan batas ukuran total sekitar 1,9 juta piksel. Selama geser pada zoom tetap masih berada di dalam cadangan, frame memakai cache detail satu kali pada koordinat piksel bulat tanpa menggambar ulang cache dunia atau memperbesar bitmap; tepi yang baru terbuka tetap sudah tercakup detail. Setelah gerakan berhenti, render detail tetap diperbarui setelah 130 ms. Pada geseran yang melewati cadangan atau saat pinch zoom, renderer kembali memakai cache dunia dan gambar detail sementara sampai render selesai, jadi transisi buram di area baru masih bisa terlihat.

Pada uji Chromium 360×800 DPR 3 terhadap 12 pergeseran kecil, build sebelumnya menggambar cache dunia 12 kali dan menggeser gambar detail pada pecahan piksel; build baru memakai satu blit detail selaras piksel per frame, tanpa cache dunia pada gerakan itu. Pada sampel delapan render ulang diam di Chromium yang sama, median naik sekitar 40 menjadi 50 ms karena area cache lebih besar; ini bukan benchmark HP atau jaminan FPS. Render ulang tetap sekali setelah gerakan, bukan di setiap frame. Cache viewport naik dari 648.000 menjadi 993.984 piksel pada ukuran tersebut; t39 mengukur peak backing canvas sekitar 27,7 MB pada viewport uji lebih besar, masih di bawah batas tes 32 MiB. tests/t44_map_drag_cache.py menguji dua ukuran, gesture sentuh, batas alokasi, dan render akhir.
