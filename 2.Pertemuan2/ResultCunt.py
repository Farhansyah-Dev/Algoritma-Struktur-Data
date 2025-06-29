priceGuuds = int(input(f'Masukan Harga Barang Rp: '))
totalGuuds = int(input(f'Masukan Jumlah Barang: '))

if priceGuuds <= 0 and totalGuuds <= 0:
    print (f'Silahkan masukan harga dan jumlah barang yang valid.')
else:
    totalBelanja = priceGuuds * totalGuuds
    print(f'Total Belanja anda adalah: {totalBelanja}')
    