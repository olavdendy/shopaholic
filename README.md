Nama : Olav Dendy Christian Manullang
NPM : 2306230590
Kelas : PBP A

LINK PWS : https://pbp.cs.ui.ac.id/web/project/olav.dendy/shopaholic

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Dari segi penggunaan antara keduanya cukup berbeda dimana penggunaan HttpResponseRedirect() perlu memasukkan URL yang valid sebagai argumennya, dan untuk redirect() ada beberapa yang bisa dimasukkan sebagai argumennya, antara lain URL, nama URL pattern ataupun objek model. redirect() lebih fleksibel dalam membuat redirect, namun apabila kita ingin mengarahkan pengguna ke dalam sbeuah URL tertentu maka kita dapat menggunakan HttpResponseRedirect().

2. Jelaskan cara kerja penghubungan model Product dengan User!
karena kita menggunakan ForeignKey yang menghubungkan model product dengan user maka itu berarti kita dapat bahwa setiap product hanya dimiliku oleh satu user namun user dapat memiliki lebih dari satu product. Cara kerja nya dengan setiap produk akan memiliki sebuah referensi ke satu user yang merupakan pemiliki produk tersebut, maka nanti yang akan terjadi adalah, jika kita login dengan user A maka product yang ada adalah apa yang sudah didaftarkan oleh user A tersebut, namun apabila kita login dengan user B maka product yang ada pastilah bukan product dari user A melainkan product yang sudah didaftarkan oleh user B.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah sebuah proses yang terjadi saat user ingin login, proses tersebut berjalan dengan cara memeriksa atau memverifikasi identitas pengguna untuk memastikan apakah identitas pengguna tersebut telah terdaftar di dalam sistem atau bukan, proses ini biasa berjalan disaat pengguna ingin memasukkan username dan password. Authorization adalah pemeriksaan hak akses pengguna, proses ini berjalan setelah pengguna melewati Authentication, ibaratnya Authorization membedakan fitur-fitur yang dapat dipakai yang sudah diberikan oleh sistem, misalnya apabila seorang pembeli login akan diberikan fitur yang berbeda dengan saat seorang penjual login. Django menyediakan view login (LoginView) dan form yang digunakan untuk menangani login. Proses autentikasi dapat dilakukan dengan metode authenticate() dan login(). authenticate() memverifikasi apakah username dan password cocok.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan SessionMiddleware untuk menangani sesi pengguna. Django juga mengatur dimana sesi akan disimpan, contohnya di dalam setting.py terdapat konfigurasi database untuk menyimpan sesi. kegunaan cookies antara lain untuk meningkatkan preferensi pengguna, menyimpan data sementara, melacak aktivitas pengguna untuk meningkatkan pengalaman personal. Tidak semua cookies aman, semua tergantung bagaimana cookies itu di konfigurasi, apabila cookies tidak dilindungi dengan baik maka terdapat kemungkinan akan dicuri.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama pahami terlebih dahulu apa saja yang harus diimplementasikan di dalam tugas tersebut. Setelahnya saya mencoba dengan mengimplementasikan fungsi-fungsi awal seperti login, register dan logout, selanjutnya saya mencoba membuat akun dan memasukkan data product, ternyata user lain memiliki product yang sama dengan user lainnya, disitu saya menyadari kesalahan saya karena saat itu ProductEntry yang masih belum dihubungkan dengan tiap user, selanjutnya saya mencoba untuk memahami alur last login ataupun sesi terakhir berjalan dan mengimplementasikan nya untuk membuat sebuah notifikasi kapan terakhir kali user tersebut masuk ke dalam sistem.

