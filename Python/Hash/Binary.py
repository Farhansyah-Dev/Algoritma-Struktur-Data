#Program Implementasi Pencarian Binary

def binarySearch (arr, target):
    low = 0
    high = len(arr) -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  #Mengembalikan index elemen yang sesuai
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1 #Mengembalikan -1 jika nilai tidak ditemukan

if __name__=="__main__":
    data = [2, 5, 6, 8, 12, 14]
    targetValue = 89
    
    result = binarySearch(data, targetValue)
    if result != -1:
        print(f'nilai {targetValue} ditemukan pada index {result}.')
    else:
        print(f'Nilai {targetValue} tidak ditemukan dalam dataset.')        