# =====================================================================
# File: pesanan.py
# Association Class: Pesanan
#           - Mengelola pesanan pelanggan dan beberapa objek Menu
# =====================================================================
from menu import format_rupiah

class Pesanan:

    def __init__(self, kode_pesanan, pelanggan, tanggal):
        # Atribut Private
        self.__kose_pesanan = kode_pesanan
        self.__pelanggan = pelanggan          
        self.__tanggal = tanggal
        self.__daftar_menu = []

    # Getter
    def get_kode_pesanan(self):
        return self.__kode_pesanan

    def get_pelanggan(self):
        return self.__pelanggan

    def get_tanggal(self):
        return self.__tanggal

    # Getter dengan salinan list untuk menjaga encapsulation
    def get_daftar_menu(self):
        return self.__daftar_menu.copy()

    # Method tambahan 1: Menambahkan menu ke pesanan
    def tambah_menu(self, menu, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
        return False

        if menu.get_stok() < jumlah:
            print("Stok tidak mencukupi.")

        if not menu.kurangi_stok(jumlah):
            return False

        data = {
            "menu": menu, 
            "jumlah": jumlah,
            "subtotal": menu.get_harga() * jumlah 
        }

        self.__daftar_menu.append(data)
        print("Menu berhasil ditambahkan.")
        return True

    # Method tambahan 2: Menghitung total pembayaran
    def hitung_total(self):
        total = 0

        for data in self.__daftar_menu:
            total += data["subtotal"]

        return total

    # Method tambahan 3: Memeriksa status pesanan
    def cek_status(self):
        if self.__daftar_menu:
            return "Pesanan sudah dibuat"
        return "Pesanan masih kosong"

    #Method tambahan 4: Menampilkan detail pesanan 
    def tampilkan_pesanan(self):
        print("\n========== DETAIL PESANAN ==========")
        print("Kode pesanan :", self.__kode_pesanan)
        print("Pelanggan :", self.__pelanggan.get_nama())
        print("Tanggal :", self.__tanggal)

        if not self.__daftar_menu:
            print("Belum ada menu.")
            return

        for nomor, data in enumerate(self.__daftar_menu, 1):
            menu = data["menu"]

        print(f"\n{nomor}. {menu.get_nama()}")
        print("Jumlah :", data["jumlah"])
        print("Subtotal :", format_rupiah(data["subtotal"]))

        print("===========================================")
        print("Total Bayar  :", format_rupiah(self.hitung_total()))
        print("===========================================")