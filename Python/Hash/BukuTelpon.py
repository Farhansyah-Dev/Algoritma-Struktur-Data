# Program Implementasi Hash 
#Studi Kasus pencarian buku telepon

bukuTelepone = {
    'Andi' : '088245672456',
    'Wahyu': '088135798642',
    'Gorjia': '088323458881'
}

if __name__=="__main__":
    namaDicari = 'Wahyu'
    
    if namaDicari in bukuTelepone:
        print(f'Nomor {namaDicari} adalah {bukuTelepone [namaDicari]}.')
    else:
        print(f'{namaDicari} tidak ditemukan di buku telepone.')