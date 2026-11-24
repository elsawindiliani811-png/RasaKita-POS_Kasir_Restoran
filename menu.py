# =====================================================================
# File    : menu.py
# Class   : Menu (Superclass)
# Deskripsi: Mengelola data dasar menu restoran
# =====================================================================

def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")


class Menu:

    def __init__(self, kode, nama, harga, stok):
        # Atribut Private
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Getter
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    # Method 1: Mengubah data menu
    def ubah_data(self, nama, harga):
        if nama:
            self.__nama = nama

        if harga > 0:
            self.__harga = harga

    # Method 2: Menambahkan stok
    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah

    # Method 3: Mengurangi stok
    def kurangi_stok(self, jumlah):
        if 0 < jumlah <= self.__stok:
            self.__stok -= jumlah
            return True

        return False

    # Method 4: Memeriksa status stok
    def cek_status(self):
        if self.__stok > 0:
            return "Tersedia"

        return "Habis"

    # Method 5: Menampilkan informasi menu
    def info_detail(self):
        return (
            f"Kode: {self.__kode} | "
            f"Nama: {self.__nama} | "
            f"Harga: {format_rupiah(self.__harga)} | "
            f"Stok: {self.__stok}"
        )

    def tampilkan_info(self):
        print(self.info_detail())
        print("Jenis  :", self.get_jenis())
        print("Status :", self.cek_status())

    # Method untuk jenis menu
    def get_jenis(self):
        return "Menu"
   
