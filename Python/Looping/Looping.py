#Function Looping dari user

def LearnLoop (jumlahLoop): #Looping Function
    
    # Cara Alternative Menggunakan Ternary Operator
    TitikAwal = 0 if jumlahLoop %2 == 0 else 1
    jenisAngka = "genap" if jumlahLoop %2 == 0 else "ganjil"
    
    
    for i in range (TitikAwal, jumlahLoop+1 , 2) :
        print (f"Selamat Pagi User {jenisAngka} {i}")
    
    # Cara Biasa 
    if jumlahLoop %2 == 0 :
         for i in range (2, jumlahLoop+1, 2):
            print (f"Selamat Pagi User genap {i} ") 
         
    else : 
         for i in range (1, jumlahLoop+1, 2):
            print (f"Selamat Pagi User ganjil {i}") 
           
userInput = int (input ("Masukan Angka: "))
LearnLoop (userInput)

def MasakMie (indomie) :
    airMateng = 5 #menit
    
    if indomie < airMateng :
        print (f"Baru juga {indomie} belum {airMateng} menit air belum mateng dong")
        
    elif indomie > airMateng:
        print(f"Sudah lewat dari {airMateng} mienya kelembekan deh..")
        
    else:
        print(f"Air mateng tuh masukan mienya")

regis = int(input("Udah berapa lama masak air: "))
MasakMie(regis)

def jumlahPutaran ( name, putaran) :
    start = 1
    while start <= putaran:
        print(f"Jumlah putaran pelari {name}: {putaran} {start}")
        start += 1
        
berlari = int(input("berapa jumlah putaran berlari: "))
jumlahPutaran('ahmad',berlari)