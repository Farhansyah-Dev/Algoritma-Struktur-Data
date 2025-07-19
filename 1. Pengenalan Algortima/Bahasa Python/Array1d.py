#Studi kasus program untuk menyimpan dan menampilkan daftar nilai ujian 5 siswa.

#Array 1 dimensi untuk menyimpan nilai ujian 5 siswa
nilaiUjianSiswa = [85, 90, 78, 92, 88]

#Menampilkan nilai setiap siswa
for nilai in range(len(nilaiUjianSiswa)):
    print(f'Nilai siswa ke- {nilai+1}: {nilaiUjianSiswa[nilai]}')
    
#Menghitung nilai rata rata
average = sum(nilaiUjianSiswa) / len(nilaiUjianSiswa)
print(f'Nilai rata rata: {average}')