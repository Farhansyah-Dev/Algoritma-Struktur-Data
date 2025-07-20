def linearSearch (arr, target):
    for i in range (len(arr)):
        if arr [i] == target:
            return i #Mengembalikan index yang dicari
    return -1 #Jika elemen tidak ditemukan

if __name__ == "__main__":
    
    dataArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 45
    
    hasil = (linearSearch(dataArray, target))
    if hasil != -1:
        print(f'{target} ditemukan pada index {hasil}.')
    else:
        print(f'{target} tidak ditemukan.')
    