# ==========================================================
# File    : pelanggan.py
# Isi     : Class Pelanggan
# ==========================================================

class Pelanggan:

    def __init__(self, id_pelanggan, nama, nomor_hp):
        # Atribut private
        self.__id_pelanggan = id_pelanggan
        self.__nama = nama
        self.__nomor_hp = nomor_hp

    # GETTER
    def get_id_pelanggan(self):
        return self.__id_pelanggan

    def get_nama(self):
        return self.__nama

    def get_nomor_hp(self):
        return self.__nomor_hp

    # METHOD MENGUBAH DATA
    def ubah_nama(self, nama):
        if nama:
            self.__nama = nama

    def ubah_nomor_hp(self, nomor_hp):
        if nomor_hp:
            self.__nomor_hp = nomor_hp

    # METHOD MENAMPILKAN INFORMASI
    def tampilkan_info(self):
        print("ID Pelanggan :", self.__id_pelanggan)
        print("Nama         :", self.__nama)
        print("Nomor HP     :", self.__nomor_hp)

