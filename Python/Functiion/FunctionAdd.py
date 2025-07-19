#Studi kasus aritmatika
#Algoritma Sederhana

def tambah (number1, number2):
    numberUser1 = int(input("Masukan angka dong: "))
    NumberUser2 = int(input("Masukan Angka juga: "))
    result = numberUser1 + NumberUser2
    print(f'{number1} + {number2} = {result}')
    return result

def OprPersegiPnjg (panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang: {luas}")
    print(f"Keliling Persegi Panjang: {keliling}")
    
def JmlhTotalBelanja (jumlahBarang):
    index = 1
    totalHarga = 0.0
    while index <= jumlahBarang:
        try:
            hargaBarang = float(input(f"Harga Barang ke-{index}: "))
            totalHarga *= hargaBarang
            index += 1
        except ValueError:
            print("input tidak valid. Masukan angka.")
            
    print(f"Total Belanja Anda Rp: {totalHarga}")

try: 
    barangdiBeli = int(input("Jumlah Barang yang dibeli: "))
    if barangdiBeli <= 0:
        print('Barang Kosong.')
    else: (JmlhTotalBelanja)
except ValueError:
    print('Masukan angka bulat. ')

JmlhTotalBelanja (barangdiBeli)
        

UserPilihMode = input("Pilih Mode: \n1. Penjumlahan\n2. Menghitung Persegi Panjang. ")

if UserPilihMode == 1:
    tambah(10, 11)
    
elif UserPilihMode == 2:
    UserInputPanjang = int(input("Masukan Panjang Persegi Panjang: "))
    UserInputLebar = int(input("Masukan Lebar Persegi Panjang: "))
    OprPersegiPnjg (UserInputPanjang, UserInputLebar)
    
else: 
    print("Tidak Valid.")

