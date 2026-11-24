# =====================================================
# File     : minuman.py
# Class    : Minuman
# Subclass : Menu
# =====================================================

from menu import Menu


# SUBCLASS 2: MINUMAN
class Minuman(Menu):

    # Constructor berparameter
    def __init__(self, kode, nama, harga, stok,
                 ukuran, suhu, jenis_minuman):

        # Memanggil constructor superclass Menu
        super().__init__(kode, nama, harga, stok)

        # Atribut private (Encapsulation)
        self.__ukuran = ukuran
        self.__suhu = suhu
        self.__jenis_minuman = jenis_minuman

    # Getter untuk mengakses atribut private
    def get_ukuran(self):
        return self.__ukuran

    def get_suhu(self):
        return self.__suhu

    def get_jenis_minuman(self):
        return self.__jenis_minuman

    # Method untuk mengubah suhu minuman
    def ubah_suhu(self, suhu):
        if suhu:
            self.__suhu = suhu

    # Method untuk mengubah ukuran minuman
    def ubah_ukuran(self, ukuran):
        if ukuran:
            self.__ukuran = ukuran

    # Method keterangan minuman
    def keterangan_minuman(self):
        return f"{self._jenis_minuman}, {self._suhu}"

    # Method overriding
    def get_jenis(self):
        return "Minuman"

    # Menampilkan informasi detail minuman
    def info_detail(self):
        return (
            f"{super().info_detail()} | "
            f"Ukuran: {self.__ukuran} | "
            f"Suhu: {self.__suhu} | "
            f"Jenis: {self.__jenis_minuman}"
        )
