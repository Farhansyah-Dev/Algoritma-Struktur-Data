#Program Menghitung Frekuensi

def hitungFrekuensi (teks):
    tabelHash = {}
    kataList = teks.split()
    
    for kata in kataList:
        if kata in tabelHash:
            tabelHash [kata] += 1
        else:
            tabelHash [kata] = 1
    return tabelHash

if __name__=="__main__":
    teks = 'Hari ini hari yang cerah dan hari yang boring.'
    
    print(hitungFrekuensi(teks))