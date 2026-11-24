# Identitas Mahasiswa
- *Nama:* Elsa Windi Liani
- *NIM:* 25552011146
- *Kelas:* TIF RP 25B
- *Mata Kuliah:* Pemrograman Berorientasi Objek I
- *Dosen Pengampu:* Gia Yuliana, S.Kom., M.Kom.

---

# 1. Deskripsi Aplikasi
RasaKita POS merupakan aplikasi kasir restoran berbasis Python yang dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Pemrograman Berorientasi Objek (PBO).

Aplikasi ini digunakan untuk mengelola menu makanan dan minuman, data pelanggan, serta transaksi pesanan restoran melalui Command Line Interface (CLI).

# 2. Fitur Aplikasi
- Menambahkan menu makanan dan minuman.
- Menampilkan daftar menu restoran.
- Mencari data menu.
- Mengubah data menu.
- Memeriksa status dan stok menu.
- Menambahkan data pelanggan.
- Menampilkan data pelanggan.
- Membuat pesanan pelanggan.
- Menghitung total pembayaran.
- Menampilkan daftar pesanan.

# 3. Penerapan Konsep Pemrograman Berorientasi Objek (PBO)

**a. Class dan Object**
Digunakan untuk membuat objek Menu, Makanan, Minuman, Pelanggan, dan Pesanan.

**b. Constructor**
Digunakan untuk menginisialisasi atribut setiap objek.

**c. Encapsulation**
Menggunakan atribut private dan getter untuk mengakses data objek.

**d. Inheritance**
Class Makanan dan Minuman merupakan turunan dari class Menu.

**e. Association**
Class Pesanan berhubungan dengan class Pelanggan dan dapat menampung beberapa objek Menu.

# 4. Struktur File Program
- main.py : Program utama dan menu interaktif.
- menu.py : Superclass Menu.
- makanan.py : Subclass Makanan.
- minuman.py : Subclass Minuman.
- pelanggan.py : Class Pelanggan.
- pesanan.py : Class Pesanan.

# 5. Bahasa Pemrograman
Python 3

# 6. Cara Menjalankan Program
1. Buka folder aplikasi di Visual Studio Code.
2. Buka Terminal.
3. Jalankan perintah berikut:

   python main.py