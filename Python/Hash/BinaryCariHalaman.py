# Program Implementasi Binary Hash Algoritma
# Studi kasus Halaman pada buku

def cariHalaman (daftarHalaman, halamanDicari):
    kiri, kanan = 0, len(daftarHalaman) -1
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if daftarHalaman [tengah] == halamanDicari:
            return (f"Halaman {halamanDicari} di temukan pada index {tengah}.")
        elif daftarHalaman [tengah] < halamanDicari:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return (f'Halaman {halamanDicari} tidak ditemukan.')

if __name__=="__main__":
    #Halaman
    HalamanBuku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    yangDicari = 22
    
    print(cariHalaman(HalamanBuku, yangDicari))
    
  
            