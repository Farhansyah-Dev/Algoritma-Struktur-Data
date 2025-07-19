#Program Implementasi For Loops

fruits = ['Banana', 'Grape', 'Apple']
for x in fruits: #Looping value array
    print(x)
    
for i in "Banana": #Looping String
    print(i)
    
for x in fruits:
    print(x) 
    if x == "Banana": #Jika looping sama dengan banana maka looping berhenti
        break
    

#Range Function    
for x in range (1, 10):
    print(f'Angka ke-{x}') #Jika Looping sama dengan 5 lanjutkan looping
    if x == 5:
        continue
    
for i in range(2, 10): #angka awal adalah start parameter angka kedua adalah sampai mana loopingnya
    print(f'{i}')
for i in range (1, 10, 2): #angka ketiga adalah increment + 2 default +1
    print(f'Angka ke-{i}')
    
for i in range (3):
    print (i)
else:
    print('Happy New Year')
    
for i in range(1,6):
    if i == 3: break
    print(i)
else:
    print('Looping Selesai.')
    
#Looping di dalam Looping
buah = ['Anggur', 'Apel', 'Mangga']
ukuran = ['Kecil', 'Sedang', 'Besar']
kondisi = ['Matang', 'Busuk', 'Mentah']

for i in buah:
    for y in ukuran:
        for d in kondisi:
            print(f'Keterangan buah: {i} {y} {d}')
            
for i, (b, u, k) in enumerate (zip(buah, ukuran, kondisi), start = 1):
    print(f'{i}. Buah: {b}, Ukuran: {u}, Kondisi: {k}')