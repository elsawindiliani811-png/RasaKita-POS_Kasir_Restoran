# ======================================================================
# File    : makanan.py
# Fungsi  : Subclass makanan turunan dari class Menu 
# =====================================================================
from menu import Menu

class Makanan(Menu):
   
    def __init__(self, kode, nama, harga, stok, kategori, tingkat_pedas, porsi):
        # Memanggil constructor superclass untuk mengisi atribut bawaan
        super().__init__(kode, nama, harga, stok)

        # Atribut private khusus makanan
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

    # Method Tambahan
    def ubah_tingkat_pedas(self, tingkat):
        self.__tingkat_pedas = tingkat

    def keterangan_pedas(self):
        return f"Tingkat pedas: {self.__tingkat_pedas}"

    # Method overriding
    def get_jenis(self):
        return "Makanan"

    def info_detail(self):
        return (
             f"[MAKANAN] {super().info_detail()} | "
             f"Kateori: {self.__kategori} | "
             f"Pedas: {self.tingkat_pedas} | "
             f"Porsi: {self._porsi}"

        )
