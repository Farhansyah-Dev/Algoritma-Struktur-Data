#Program implementasi Linear Hash

def cariKontak (daftarKontak, namaDicari):
    for kontak in daftarKontak:
        if kontak == namaDicari:
            return (f'{namaDicari} ditemukan dalam daftar kontak.')
        return (f'{namaDicari} tidak ditemukan.')
    
if __name__=="__main__":
    kontak = ['Andi', 'Budi', 'Cantika', 'Dwi', 'Erlan', 'Fatur', 'Gilang', 'Hari',
              'Ibnu', 'Jajang', 'Mulyono', 'Nanang', 'Opik', 'Pardi', 'Queen', 'Rahmat', 'Siti', 'Tomi', 'Umi', 'Vivi', 'Yanti', 'Zahra']
    
    #nama yang dicari
    nama = 'budi'
    #Hasil pencarian
    print(cariKontak(kontak, nama))
    
