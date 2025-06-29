count = 0
result = 0



for i in range (1, 11):
    number = int(input(f'Masukan Bilangan ke {i}: '))
    result += number
    count += 1
    
average = result / 10
print(f'Rata rata dari 10 bilangan yang dimasukkan adalah: {average}')
    
	

