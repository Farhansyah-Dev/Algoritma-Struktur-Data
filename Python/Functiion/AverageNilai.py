# #studi kasus menghitung rata-rata
# #Algoritma sederhana

# jumlahBilangan = int(input("Berapa banyak nilai: "))

# total = 1

# while total <= jumlahBilangan :
#     bil = int(input((f'Masukan bilangan ke-{total}: ')))
#     total += 1
        
# Average = bil/total
# print(f'Rata-rata Nilai: {Average}')

def AverageNilai (bnykNilai) :
    start = 1
    total = 0
    while start <= bnykNilai:
        bil = int(input(f"Masukin nilai ke {start} "))
        total += bil
        start += 1
    
    average = total / bnykNilai
    print(f'Rata-rata Nilai {average}')
    
JumlahNilaiUser = int(input("Berapa banyak nilai: "))
AverageNilai (JumlahNilaiUser)