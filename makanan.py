# =====================================================================
# File    : makanan.py
# Class   : Makanan (Subclass dari Menu)
# Deskripsi: Mengelola data makanan restoran
# =====================================================================

from menu import Menu


class Makanan(Menu):

    def __init__(self, kode, nama, harga, stok,
                 kategori, tingkat_pedas, porsi):

        # Memanggil constructor superclass Menu
        super().__init__(kode, nama, harga, stok)

        # Atribut Private
        self.__kategori = kategori
        self.__tingkat_pedas = tingkat_pedas
        self.__porsi = porsi

    # Getter
    def get_kategori(self):
        return self.__kategori

    def get_tingkat_pedas(self):
        return self.__tingkat_pedas

    def get_porsi(self):
        return self.__porsi

    # Method 1: Mengubah tingkat kepedasan
    def ubah_tingkat_pedas(self, tingkat_pedas):
        if tingkat_pedas:
            self.__tingkat_pedas = tingkat_pedas

    # Method 2: Mengubah ukuran porsi
    def ubah_porsi(self, porsi):
        if porsi:
            self.__porsi = porsi

    # Method 3: Menampilkan keterangan makanan
    def keterangan_makanan(self):
        return (
            f"{self.__kategori}, "
            f"{self.__tingkat_pedas}, "
            f"{self.__porsi}"
        )

    # Method 4: Menentukan jenis menu
    def get_jenis(self):
        return "Makanan"

    # Method 5: Menampilkan informasi lengkap makanan
    def info_detail(self):
        return (
            f"{super().info_detail()} | "
            f"Kategori: {self.__kategori} | "
            f"Tingkat Pedas: {self.__tingkat_pedas} | "
            f"Porsi: {self.__porsi}"
        )

