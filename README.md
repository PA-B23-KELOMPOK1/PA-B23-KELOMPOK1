# Kelompok1PACapstoneDBMSxASD
## **Project Akhir (PA) Capstone Praktikum Database Management System & Algoritma Struktur Data (Kelompok 1)**

**-  Achmad Rizqy Pranata
   (2209116086)**

**-  Julia Fatikhah Noor
   (2309116069)**

**-  Muhammad Danil Pratama
(2309116091)**

**-  Seokapriyono Bilo
   (2309116095)**

**-  Rizal Paskah Anugrah
   (2309116093)**

## **Deskripsi Program**

Program ini merupakan program Python yang memanfaatkan basis data MySQL untuk mengelola informasi tentang produk pertanian dan petani. Program ini memiliki beberapa komponen utama, termasuk koneksi ke basis data, kelas untuk representasi linked list, fungsi-fungsi untuk otentikasi admin dan pengguna, serta operasi-operasi untuk menambah, melihat, mengubah, dan menghapus data produk dan petani.

Selain itu, program ini menyediakan fitur otentikasi pengguna, di mana pengguna dapat masuk (sign in) atau mendaftar (sign up) untuk mengakses fungsionalitas yang disediakan. Pengguna juga dapat menjelajahi daftar produk, melakukan pencarian berdasarkan nama produk, menambah produk ke dalam keranjang belanja, melihat isi keranjang, dan melakukan proses checkout.

Program ini dirancang untuk memisahkan antara fungsionalitas admin dan pengguna biasa. Admin memiliki akses penuh untuk mengelola data produk dan petani, sementara pengguna biasa memiliki akses terbatas untuk melihat dan membeli produk yang tersedia.

Sistem keranjang belanja memungkinkan pengguna untuk menambahkan beberapa produk sebelum melakukan checkout. Setelah checkout, transaksi akan dicatat di basis data dan stok produk akan diperbarui secara otomatis.

Secara keseluruhan, program ini menyediakan platform yang lengkap untuk mengelola informasi produk pertanian dan memfasilitasi transaksi jual beli antara pengguna dan sistem.

## **Flowchart**
![kelompok1 drawio (3)](https://github.com/PA-B23-KELOMPOK1/PA-B23-KELOMPOK1/assets/146010899/1dfc7786-6ac1-469a-92e9-a4efb22e6cff)

## **Struktur Project**

Struktur project untuk program ini terdiri dari satu file Python dan file SQL untuk skema basis data yaitu:

- PACapsKelompok1.py: Ini adalah file utama yang berisi seluruh kode program yang diberikan. Semua logika aplikasi, termasuk koneksi database, definisi kelas, fungsi utilitas, dan antarmuka pengguna, terkandung dalam file ini.

- kelompok1_orppp.sql: File ini berisi skema basis data MySQL yang digunakan oleh program. Ini termasuk struktur tabel untuk menyimpan informasi tentang produk, petani, admin, dan transaksi, bersama dengan kunci asing dan indeks yang diperlukan.


## **Fitur**
Program ini adalah sebuah program manajemen data pertanian yang terdiri dari beberapa fitur yaitu:

1. **Manajemen Admin**:
   - **Login Admin**: Admin dapat melakukan login dengan memasukkan username dan password. Ini memungkinkan admin untuk mengakses menu dan fungsi khusus yang hanya tersedia untuk admin.
   - **Menu Admin**: Setelah login berhasil, admin dapat memilih berbagai opsi menu untuk mengelola data, seperti tambah data, lihat data, ubah data, dan hapus data.
   - **Tambahan Data**: Admin dapat menambahkan data baru tentang produk pertanian dan petani ke dalam basis data.
   - **Lihat Data**: Admin dapat melihat daftar produk pertanian dan petani yang tersimpan dalam basis data.
   - **Ubah Data**: Admin dapat mengubah informasi tentang produk pertanian dan petani yang sudah tersimpan dalam basis data.
   - **Hapus Data**: Admin dapat menghapus data tentang produk pertanian dan petani dari basis data.

2. **Manajemen User Biasa**:
   - **Sign Up**: Pengguna biasa dapat mendaftar (sign up) dengan membuat akun baru. Mereka diminta untuk memasukkan informasi seperti username, nomor telepon, alamat email, alamat, dan password.
   - **Sign In**: Pengguna biasa dapat melakukan login dengan memasukkan username dan password yang telah mereka daftarkan sebelumnya. Ini memberi akses kepada mereka untuk menggunakan fungsi-fungsi berikut.
   - **Lihat Data Produk Tersedia**: Pengguna biasa dapat melihat daftar produk pertanian yang tersedia dalam basis data.
   - **Cari Produk**: Pengguna dapat mencari produk tertentu berdasarkan nama produk.
   - **Beli Produk**: Pengguna dapat membeli produk tertentu dengan memasukkan ID produk dan jumlah yang ingin dibeli.
   - **Lihat Isi Keranjang**: Pengguna dapat melihat isi keranjang belanja mereka, yang berisi daftar produk yang akan dibeli beserta jumlahnya.
   - **Checkout**: Pengguna dapat melakukan proses checkout untuk membeli produk yang ada di keranjang mereka. Mereka dapat memilih metode pembayaran, dan setelah itu transaksi mereka akan disimpan dalam basis data.

3. **Utilitas Tambahan**:
   - **Get Product Name**: Fungsi ini mengambil ID produk sebagai masukan dan mengembalikan nama produk yang sesuai dari basis data.
   - **Cari Produk**: Fungsi ini mencari produk berdasarkan nama produk tertentu.
   
4. **Antarmuka Pengguna (CLI)**:
   - Program ini memiliki antarmuka pengguna berbasis teks (Command Line Interface/CLI), di mana pengguna berinteraksi dengan memasukkan perintah dan data melalui konsol atau terminal.

Dengan fitur-fitur ini, program ini memungkinkan admin untuk mengelola data tentang produk pertanian dan petani, sementara pengguna biasa dapat melakukan aktivitas seperti mencari, membeli, dan checkout produk pertanian yang mereka inginkan.

## **Fungsionalitas**

Codingan ini adalah sebuah program Python yang berfungsi sebagai sistem manajemen data untuk pertanian. Berikut adalah fungsionalitas utama dari program ini:

1. **Manajemen Admin**:
   - Admin dapat login ke dalam sistem dengan memasukkan username dan password.
   - Setelah login berhasil, admin dapat mengakses menu-menu untuk mengelola data produk dan petani.
   - Admin dapat menambah, melihat, mengubah, dan menghapus data produk dan petani dalam basis data.

2. **Manajemen User Biasa**:
   - Pengguna biasa dapat mendaftar (sign up) untuk membuat akun baru atau melakukan login ke dalam sistem.
   - Pengguna biasa dapat melihat daftar produk pertanian yang tersedia.
   - Mereka juga dapat mencari produk berdasarkan nama.
   - Pengguna dapat membeli produk yang mereka inginkan dengan memasukkan ID produk dan jumlah yang akan dibeli.
   - Mereka dapat melihat isi keranjang belanja mereka dan melakukan proses checkout untuk melakukan pembelian.

3. **Utilitas Tambahan**:
   - Fungsi `get_product_name(id_produk)`: Mengambil ID produk sebagai masukan dan mengembalikan nama produk yang sesuai dari basis data.
   - Fungsi `cari_produk(nama_produk)`: Mencari produk berdasarkan nama produk tertentu dalam basis data.

4. **Antarmuka Pengguna (CLI)**:
   - Program ini memiliki antarmuka pengguna berbasis teks (Command Line Interface/CLI), di mana pengguna dapat berinteraksi dengan memasukkan perintah dan data melalui konsol atau terminal.

5. **Interaksi dengan Database MySQL**:
   - Program ini terhubung ke database MySQL menggunakan modul `mysql.connector`.
   - Penggunaan SQL queries untuk mengeksekusi operasi-operasi seperti SELECT, INSERT, UPDATE, dan DELETE pada basis data.

Dengan fungsionalitas-fungsionalitas ini, program ini memberikan kemampuan bagi admin untuk mengelola data pertanian dan memungkinkan pengguna biasa untuk melakukan pembelian produk pertanian melalui antarmuka teks yang sederhana.

## **Cara Penggunaan**

Berikut adalah langkah-langkah cara penggunaan dari codingan yang kami buat:

1. **Persiapan Database**:
   - Pastikan memiliki instalasi XAMPP (MySQL Server) dan memiliki database yang sesuai dengan nama "kelompok1" di dalam phpmyadmin.
   - Sesuaikan informasi koneksi database seperti host, username, dan password sesuai dengan konfigurasi MySQL Server di codingan.

2. **Menjalankan Program**:
   - Jalankan program Python dengan menjalankan file yang bernama sesuai dengan codingan yang diberikan.
   - Misalnya, jika file disimpan dengan nama "farm_management_system.py", jalankan perintah `python farm_management_system.py` di terminal atau konsol.

3. **Login Sebagai Admin**:
   - Setelah program dijalankan, akan diminta untuk memilih jenis login: admin atau user biasa.
   - Jika memilih login sebagai admin, masukkan username dan password yang sesuai.

4. **Menu Admin**:
   - Setelah berhasil login sebagai admin, akan diberikan opsi menu untuk mengelola data:
     - Tambah data
     - Lihat data
     - Ubah data
     - Hapus data
     - Logout

5. **Menu Tambah Data**:
   - Pilih opsi untuk menambahkan data, baik produk maupun petani.
   - Ikuti instruksi untuk memasukkan informasi yang diminta, seperti nama produk, harga, stok, jenis produk, metode produksi, dan sertifikasi.

6. **Menu Lihat Data**:
   - Pilih opsi untuk melihat data produk atau petani.
   - Data akan ditampilkan sesuai dengan opsi yang dipilih, seperti ID, nama, harga, stok, dll.

7. **Menu Ubah Data**:
   - Pilih opsi untuk mengubah data produk atau petani.
   - Masukkan ID data yang ingin diubah, lalu masukkan informasi baru yang diperlukan.

8. **Menu Hapus Data**:
   - Pilih opsi untuk menghapus data produk atau petani.
   - Masukkan ID data yang ingin dihapus.

9. **Menu User Biasa**:
   - Jika memilih login sebagai user biasa, akan diminta untuk sign in atau sign up terlebih dahulu.
   - Setelah berhasil sign in, akan diberikan opsi menu untuk:
     - Melihat data produk tersedia
     - Mencari produk
     - Membeli produk
     - Melihat isi keranjang
     - Checkout

10. **Menu Cari Produk**:
   - Jika memilih opsi untuk mencari produk, masukkan nama produk yang ingin dicari.
   - Hasil pencarian akan ditampilkan berdasarkan keyword yang dimasukkan.

11. **Menu Beli Produk**:
   - Masukkan ID produk yang ingin dibeli dan jumlahnya.
   - Produk akan ditambahkan ke dalam keranjang belanja.

12. **Menu Checkout**:
   - Setelah selesai memilih produk, pilih opsi checkout untuk melakukan pembelian.
   - Pilih metode pembayaran yang diinginkan, lalu ikuti instruksi selanjutnya.

Dengan mengikuti langkah-langkah di atas, dapat menggunakan program ini untuk mengelola data pertanian dan melakukan pembelian produk secara interaktif melalui antarmuka teks.

