Nama : Olav Dendy Christian Manullang
NPM : 2306230590
Kelas : PBP A

LINK PWS : https://pbp.cs.ui.ac.id/web/project/olav.dendy/shopaholic

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
   Jika beberapa selector berbasis tag digunakan pada elemen yang sama, urutan yang muncul terakhir dalam kode CSS akan diterapkan, karena CSS mengikuti prinsip cascade. Contoh misalkan kita menggunakan tag selector yaitu <p>.Contoh:
   p {
     color: blue;
   }
   p {
     color: red;
   }
maka warna yang akan digunakan adalah red (merah) karena css menggunakan prinsip cascade.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
   Karena web dapat diakses dimana saja seperti laptop, komputer dan handphone, dimana semua gadget tersebut memiliki ukuran layar yang berbeda, maka responsive design sangat penting untuk membuat web yang diakses terlihat optimal, nyaman dan dapat diakses dengan baik. contoh aplikasi yang sudah menerapkan responsive design adalah youtube, netflix dan bagi yang belum menerapkan responsive design adalah aplikasi-aplikasi jadul yang sudah lama tidak di update dan dipakai.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
   margin itu seperti ruang tempat beradanya elemen, contohnya seperti tata letak untuk meletakkan teks ataupun gambar. Border adalah garis batas di sekitar elemen yang dapat memiliki tebal serta warna. Padding adalah Padding adalah ruang di dalam elemen, antara konten elemen dan border-nya. Padding memperbesar jarak antara konten dengan tepi elemen, namun tetap berada di dalam border. Untuk mengimplementasikan ketiganya kita bisa menggunakan nya seperti ini:
   margin: 20px; #untuk membuat jarak 20 piksel
   border: 2px solid black; #untuk membuat border dengan ketebalan 2 pixel dan gaya solid
   padding: 15px; #untuk membuat jarak 15 piksel dadri bagian dalam elemen
   
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   Flexbox adalah model tata letak yang digunakan untuk mengatur elemen secara satu dimensi, horizontal (baris) atau vertikal (kolom). Grid Layout adalah model tata letak yang lebih kompleks dan digunakan untuk menyusun elemen dalam dua dimensi (baris dan kolom). Grid memungkinkan kita membuat tata letak yang lebih rumit dengan baris dan kolom yang teratur, seperti tabel atau struktur halaman web yang lebih kompleks (misalnya header, sidebar, dan footer).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   pertama kita perlu untuk membuat fungsi yang berguna untuk menghapus dan mengedit product, implementasikan kode kode yang sesuai dengan logic untuk menghapus dan mengedit product yang telah ada di dalam product entries. Kedua, menentukan mau memakai tailwind, bootstrap atau yang lain, disini saya memakai tailwind, maka kita perlu mengimplementasikan kode yang sesuai dengan tailwind itu sendiri. gunakan desing-design seperti membuat border, margin dan yang lainnya untuk mendekorasi file-file html yang lain seperti login, register, edit dan delete product serta yang lainnya. untuk mengimplementasikan setiap button di setiap product kita perlu mengimplementasikan kode yang sesuai di file yang sesuai untuk setiap product. Untuk membuat navbar kita memerlukan file baru berupa html dan mengimplementasikan kode disana.
