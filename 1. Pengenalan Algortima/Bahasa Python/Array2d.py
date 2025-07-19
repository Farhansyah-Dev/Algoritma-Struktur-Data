#studi kasus program untuk menyimpan data matriks 3x3 dan menghitung jumlah setiap baris

#Array 2 dimensi (matriks 3x3)
matriks = [
    [2, 4, 6],
    [3, 5, 7],
    [8, 6, 1]
]
#Menampilkan matriks dan menghitung jumlah setiap baris
for data in range(len(matriks)):
    total = sum(matriks[data])
    print(f'Baaris {data + 1}: {matriks[data]}, Jumlah: {total}')