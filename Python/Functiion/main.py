#Program untuk membuat Function pada python

#def NameFunction (parameter variabel): jika tidak ada parameter tidak perlu di isi Variable
    #Statment
    #Algoritma 
    
#Cara pemanggila Function
#NameFunction (parameter) jika tidak ada parameter cukup NameFunction ()

#example Function No Parameter
def SayHello ():
    print('Hey, There Good Morning.')

SayHello()

#example Function Use Parameter
def SayHello (thisUser):
    print(f'Hey, {thisUser} Good Morning.')

SayHello('Andi')

#example Function default Parameter
def SayHello (thisUser, age= 20 ):
    print(f'{thisUser} yearsOld: {age} year')

SayHello('Josep')
SayHello('Kris', 30)

#example Function return Value
def sayHello (thisUser, age, tall):
    print(f'The Name: {thisUser}\nYersOld: {age}\nThe tall{tall}:')
    return print(f'Biodata {thisUser}')

sayHello ('Kris', 22, 180)

#example function jika jumlah parameter tidak diketahui
def sayHello (*thisUser): #tambakan * didepan parameter
    print(f'Warga Kampung Cikiwul: {thisUser}')
    
sayHello('Jack', 'Cris', 'Columbus', 'Mark', 'Kevin')

#example Function parameter kata kunci
def TheChildren (child1, child2, child3):
    listChild = [child1, child2, child3]
    
    for i, nama in enumerate(listChild, start= 1):
        print(f'Anak ke {i}: {nama}')
        
    print(f'The Child youngers {listChild[-1]}')
    
TheChildren (child1='Kevin', child2='Nadia', child3='Muklis')

#example Function parameter kata kunci sembarangan 
def sayHello (**students):
    print(f'jumlah murid SDN SumurBatu 1: {students['bawah100']}')
    
sayHello(bawah100 = 40, atas100 = 300)

#example daftar atau list di dalam Function
def myFruits (fruits):

    print('Macam-macam Buah: ')
    for i in range (len(fruits)):
        print(f'{i+1} buah: {fruits[i]}')
    
buah = ['Jeruk', 'Mangga', 'Alpukat']
myFruits (buah)


