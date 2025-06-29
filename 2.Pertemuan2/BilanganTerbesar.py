number1 = int(input('Masukan Bilangan Pertama: '))
number2 = int(input('Masukan Bilangan Kedua: '))
number3 = int(input('Masukan Bilangan Ketiga: '))

if number1 > number2 and number2 > number3:
    print(f'Bilangan Terbesar adalah: {number1}')
    
elif number2 > number1  and number2 > number3:
    print(f'Bilangan Terbesar adalah: {number2}')
    
else:
    print(f'Bilangan Terbesar adalah: {number3}')