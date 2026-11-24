# ==========================================================
# Program : RasaKita POS
# Deskripsi: Aplikasi Kasir Restoran Berbasis Python
# File    : main.py
# ==========================================================

# IMPORT SEMUA CLASS
from menu import Menu, format_rupiah
from makanan import Makanan
from minuman import Minuman
from pelanggan import Pelanggan
from pesanan import Pesanan

# DATA APLIKASI

daftar_menu = []
daftar_pelanggan = []
daftar_pesanan = []

# ==========================================================
# DATA AWAL MENU RESTORAN
# ==========================================================

daftar_menu.append(
    Makanan("M001", "Nasi Goreng", 18000, 20,
            "Makanan Berat", "Sedang", "Reguler")
)

daftar_menu.append(
    Makanan("M002", "Mie Goreng", 15000, 15,
            "Makanan Berat", "Tidak Pedas", "Reguler")
)

daftar_menu.append(
    Minuman("D001", "Es Teh", 5000, 30,
            "Regular", "Dingin", "Teh")
)

daftar_menu.append(
    Minuman("D002", "Jus Alpukat", 12000, 15,
            "Large", "Dingin", "Jus")
)

# FUNGSI PENCARIAN MENU

def cari_menu(kode):
    for menu in daftar_menu:
        if menu.get_kode().lower() == kode.lower():
            return menu
    return None

# ==========================================================
# MENAMPILKAN DAFTAR MENU
# ==========================================================

def tampilkan_menu():
    print("\n========== DAFTAR MENU RASAKITA ==========")

    if not daftar_menu:
        print("Belum ada data menu.")
        return

    for menu in daftar_menu:
        print(menu.info_detail())
        print("Jenis  :", menu.get_jenis())
        print("Status :", menu.cek_status())
        print("-" * 50)

# MENAMBAHKAN MENU

def tambah_menu():
    print("\n========== TAMBAH MENU ==========")

    jenis = input("Jenis (1=Makanan, 2=Minuman): ")
    kode = input("Kode menu: ")
    nama = input("Nama menu: ")

    if cari_menu(kode):
        print("Kode menu sudah digunakan.")
        return

    try:
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))

        if harga <= 0 or stok < 0:
            print("Harga harus positif dan stok tidak boleh negatif.")
            return

        if jenis == "1":
            kategori = input("Kategori: ")
            pedas = input("Tingkat pedas: ")
            porsi = input("Porsi: ")

            menu = Makanan(
                kode, nama, harga, stok,
                kategori, pedas, porsi
            )

        elif jenis == "2":
            ukuran = input("Ukuran: ")
            suhu = input("Suhu: ")
            jenis_minuman = input("Jenis minuman: ")

            menu = Minuman(
                kode, nama, harga, stok,
                ukuran, suhu, jenis_minuman
            )

        else:
            print("Jenis menu tidak valid.")
            return

        daftar_menu.append(menu)
        print("Menu berhasil ditambahkan.")

    except ValueError:
        print("Harga dan stok harus berupa angka.")


# MENCARI DATA MENU

def cari_data_menu():
    print("\n========== CARI MENU ==========")

    kode = input("Masukkan kode menu: ")
    menu = cari_menu(kode)

    if menu:
        menu.tampilkan_info()
    else:
        print("Menu tidak ditemukan.")

# MENGUBAH DATA MENU

def ubah_data_menu():
    print("\n========== EDIT MENU ==========")

    kode = input("Masukkan kode menu: ")
    menu = cari_menu(kode)

    if menu:
        print("Data saat ini:")
        menu.tampilkan_info()

        nama = input("Nama baru (kosong jika tetap): ")

        try:
            harga_input = input("Harga baru (0 jika tetap): ")
            harga = int(harga_input) if harga_input else 0

            menu.ubah_data(nama, harga)

            print("Data menu berhasil diperbarui.")

        except ValueError:
            print("Harga harus berupa angka.")

    else:
        print("Menu tidak ditemukan.")

# MEMERIKSA STATUS MENU

def cek_status_menu():
    print("\n========== CEK STATUS MENU ==========")

    kode = input("Masukkan kode menu: ")
    menu = cari_menu(kode)

    if menu:
        print("Nama  :", menu.get_nama())
        print("Stok  :", menu.get_stok())
        print("Status:", menu.cek_status())
    else:
        print("Menu tidak ditemukan.")


# ==========================================================
# MENAMBAHKAN DATA PELANGGAN
# ==========================================================

def tambah_pelanggan():
    print("\n========== TAMBAH PELANGGAN ==========")

    id_pelanggan = input("ID pelanggan: ")

    for pelanggan in daftar_pelanggan:
        if pelanggan.get_id_pelanggan() == id_pelanggan:
            print("ID pelanggan sudah digunakan.")
            return

    nama = input("Nama pelanggan: ")
    nomor_hp = input("Nomor HP: ")

    pelanggan = Pelanggan(
        id_pelanggan, nama, nomor_hp
    )

    daftar_pelanggan.append(pelanggan)

    print("Pelanggan berhasil ditambahkan.")


# ==========================================================
# MENAMPILKAN DATA PELANGGAN
# ==========================================================

def tampilkan_pelanggan():
    print("\n========== DAFTAR PELANGGAN ==========")

    if not daftar_pelanggan:
        print("Belum ada pelanggan.")
        return

    for pelanggan in daftar_pelanggan:
        pelanggan.tampilkan_info()
        print("-" * 35)


# ==========================================================
# MEMBUAT PESANAN PELANGGAN
# ==========================================================

def buat_pesanan():
    print("\n========== BUAT PESANAN ==========")

    if not daftar_pelanggan:
        print("Tambahkan pelanggan terlebih dahulu.")
        return

    tampilkan_pelanggan()

    id_pelanggan = input("Masukkan ID pelanggan: ")

    pelanggan_dipilih = None

    for pelanggan in daftar_pelanggan:
        if pelanggan.get_id_pelanggan() == id_pelanggan:
            pelanggan_dipilih = pelanggan
            break

    if pelanggan_dipilih is None:
        print("Pelanggan tidak ditemukan.")
        return

    kode_pesanan = input("Kode pesanan: ")

    for pesanan in daftar_pesanan:
        if pesanan.get_kode_pesanan() == kode_pesanan:
            print("Kode pesanan sudah digunakan.")
            return

    tanggal = input("Tanggal pesanan: ")

    pesanan = Pesanan(
        kode_pesanan,
        pelanggan_dipilih,
        tanggal
    )

    while True:
        tampilkan_menu()

        kode = input(
            "Masukkan kode menu (0 untuk selesai): "
        )

        if kode == "0":
            break

        menu = cari_menu(kode)

        if menu is None:
            print("Menu tidak ditemukan.")
            continue

        try:
            jumlah = int(input("Jumlah pesanan: "))
            pesanan.tambah_menu(menu, jumlah)

        except ValueError:
            print("Jumlah harus berupa angka.")

    if pesanan.get_daftar_menu():
        daftar_pesanan.append(pesanan)

        print("\nPesanan berhasil disimpan.")
        pesanan.tampilkan_pesanan()

    else:
        print("Pesanan tidak disimpan karena belum ada menu.")


# ==========================================================
# MENAMPILKAN SEMUA PESANAN
# ==========================================================

def tampilkan_semua_pesanan():
    print("\n========== DAFTAR PESANAN ==========")

    if not daftar_pesanan:
        print("Belum ada pesanan.")
        return

    for pesanan in daftar_pesanan:
        pesanan.tampilkan_pesanan()

#=================================================================
# MENU UTAMA RASAKITA POS
#=================================================================

def main():

    print("=" * 55)
    print("                 RASAKITA POS")
    print("          RESTAURANT CASHIER SYSTEM")
    print("       Sistem Kasir Restoran Berbasis Python")
    print("=" * 55)

    while True:

        print("\n============== MENU UTAMA ==============")
        print("1. Tambah Menu")
        print("2. Tampilkan Menu")
        print("3. Cari Menu")
        print("4. Edit Menu")
        print("5. Cek Status Menu")
        print("6. Tambah Pelanggan")
        print("7. Tampilkan Pelanggan")
        print("8. Buat Pesanan")
        print("9. Tampilkan Pesanan")
        print("0. Keluar")
        print("=" * 40)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_menu()

        elif pilihan == "2":
            tampilkan_menu()

        elif pilihan == "3":
            cari_data_menu()

        elif pilihan == "4":
            ubah_data_menu()

        elif pilihan == "5":
            cek_status_menu()

        elif pilihan == "6":
            tambah_pelanggan()

        elif pilihan == "7":
            tampilkan_pelanggan()

        elif pilihan == "8":
            buat_pesanan()

        elif pilihan == "9":
            tampilkan_semua_pesanan()

        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan RasaKita POS!")
            print("Selamat berkunjung kembali.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba kembali.")


# MENJALANKAN PROGRAM

if __name__ == "__main__":
    main()