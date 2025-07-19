#program untuk menyimpan data nilai ujian dalam 3 mata pelajaran untuk 2 kelas yang masing-masing memiliki 3 siswa

#Array 3 dimensi 2 kelas, 3 siswa perkelas, 3 mata pelajaran

nilaiUjian = [
    [
        [80, 90, 85], #Siswa 1 dikelas 1
        [78, 82, 88], #Siswa 2 dikelas 1
        [92, 85, 91]  #Siswa 3 dikelas 1
    ],
    [
        [88, 79, 84], #Siswa 1 dikelas 2
        [76, 85, 80], #Siswa 2 dikelas 2
        [89, 92, 81]  #Siswa 3 dikelas 2
    ]
]

#Menampilkan nilai setiap siswa disetiap kelas dan menghitung rata-rata tiap siswa

for kelas in range (len(nilaiUjian)):
    print(f'\nKelas {kelas + 1}')
    for siswa in range (len(nilaiUjian [kelas])):
        nilaiSiswa = nilaiUjian[kelas] [siswa]
        rataNilaiSiswa = sum (nilaiSiswa) / len (nilaiSiswa)
        print(f'Siswa {siswa + 1} Nilai: {nilaiSiswa}, rata-rata: {rataNilaiSiswa}',)