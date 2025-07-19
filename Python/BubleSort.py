#Program Python implementasi Buble Sort

#membuat function
def bubblesort (dataArray): #Fungsi untuk mengurutkan list menggunakan metode Bubble Sort.
    panjangData = len (dataArray)
    
    #Looping untuk setiap putaran pengurutan
    #Setiap satu putaran selesai, satu angka terbesar akan mengapung keposisi yang benar
    #Menelusuri semua elemen array
    for putaran in range (panjangData):
        ditukar = False
        
        #Looping untuk membandingkan elemen didalam list
        #index akan berjalan dari awal hingga batas yang belum terurut.
        for index in range (0, panjangData - putaran - 1):
            
            #Bandingkan elemen saat ini dengan elemen berikutnya.
            #Tukar jika elemen yang ditemukan lebih besar daripada elemen berikutnya
            
            if dataArray [index] > dataArray [index + 1]:
                #jika elemen saat ini lebih besar, tukar posisinya.
                dataArray [index], dataArray [index + 1] = dataArray [index + 1], dataArray [index]
                ditukar = True
        if (ditukar == False):
            break

#Kode untuk pengujian diatas

if __name__ == "__main__":
    dataArray = [64, 34, 25, 12, 22, 11, 90]
    print(f'Data sebelum diurutkan: {dataArray}')
    
    bubblesort (dataArray)
    print(f'Array terurut: {dataArray} ')
    
    # for i in range (len(dataArray)):
    #     print(f'%d' % dataArray [i], end=" ")