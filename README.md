Nama : Olav Dendy Christian Manullang
NPM : 2306230590
Kelas : PBP A

LINK PWS : https://pbp.cs.ui.ac.id/web/project/olav.dendy/shopaholic

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
   
   Kegunaan penggunaan dari JavaScript dalam pengembangan aplikasi web adalah, kita bisa memperbarui konten halaman tanpa perlu memuat ulang seluruh halaman, JavaScript dapat digunakan untuk memvalidasi data yang    dimasukkan pengguna ke dalam formulir sebelum dikirim ke server. Hal ini mengurangi beban server, AJAX (Asynchronous JavaScript and XML) atau Fetch API, JavaScript memungkinkan aplikasi untuk mengambil data       dari server tanpa memuat ulang halaman, sehingga aplikasi web terasa lebih responsif.
   
2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
   
   fetch(): Fungsi ini mengembalikan sebuah promise, yang berarti operasi pengambilan data dilakukan secara asinkron. await digunakan untuk memberitahu JavaScript agar menunggu sampai promise dari fetch()            selesai. Jika kita tidak menggunakan await, fetch() tetap mengembalikan sebuah promise, tetapi kode tidak akan menunggu promise tersebut diselesaikan.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

   Ketika mengirimkan permintaan AJAX POST dari halaman web, Django secara otomatis akan memeriksa token CSRF yang terkait dengan permintaan tersebut. Jika permintaan tidak menyertakan token yang benar,              Django akan menolak permintaan tersebut. Penggunaan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST dalam aplikasi Django dilakukan untuk menghindari pengecekan CSRF (Cross-Site Request        Forgery) pada view tersebut.
   
4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

   Frontend dapat dimanipulasi: Validasi dan pembersihan data yang dilakukan di frontend bisa dengan mudah dilewati oleh pengguna berbahaya. Melindungi dari serangan berbahaya: Serangan yang umum seperti Cross-      Site Scripting (XSS) dan SQL Injection dapat dicegah dengan memastikan bahwa semua input yang diterima oleh server diproses dan dibersihkan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

   pertama kita perlu untuk memahami bagaimana cara kerja AJAX pada pengembangan web yang kita lakukan, kemudian kita membuat fungsi AJAX untuk menjalankan proses yang nantinya bisa membuat web kita berjalan         seperti asynchronus, contohnya seperti method get dan post. GET untuk mengambil sebuah data dan POST untuk mengupdate data. Selanjutnya kita membuat fungsi baru yang bertujuan untuk menambahkan produk baru        yang akan masuk ke dalam basis data di dalam view, setelah membuat di view pastikan untuk mengimport fungsi tersebut di dalam urls dan membuat path nya, karena produk ditambahkan menggunakan AJAX jadi produk      sekarang tidak perlu di refresh lagi untuk melihat kemunculan card tersebut.