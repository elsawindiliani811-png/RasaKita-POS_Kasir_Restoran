# =====================================================================
# File    : menu.py
# Superclass: Menu
# =====================================================================
def format_rupiah(angka):
    return "Rp{:,.0f}".format(angka).replace(",",".")

class Menu:
    def __init__(self, kode, nama, harga, stok):
        # Atribut private
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

# Method tambahan 1
def ubah_data(self, nama, harga):
   if nama:
      self.__nama = nama
   if harga > 0:
      self.__harga = harga

# Method tambahan 2
def tambah_stok(self, jumlah):
   if jumlah > 0:
      self.__stok += jumlah

# Method tambahan 3
def kurangi_stok(self, jumlah):
   if 0 < jumlah <= self.__stok:
      self.__stok -= jumlah
      return True
   return False

# Method tambahn 4
def cek_status(self):
   if self.__stok > 0:
      return "Tersedia"
   return "Habis"

def get_jenis(self):
   return "Menu"

def info_detail(self):
   return (
       f"Kode: {self.__kode} | "
       f"Nama: {self.__nama} | "
       f"Harga: {format_rupiah(self.__harga)} | "
       f"Stok: {self.__stok}"
       
   )

def tampilkan_info(self):
   print(self.info_detail())
   