# // Algoritma:
# Menentukan Bilangan Positif, Negatif, atau Nol

def CekBilangan (number):
    number = int(input("Masukan angka apa saja: "))
    if number > 0 :
        print(f"Angka {number} bilangan Positif")
    elif number < 0 :
        print(f"Angka {number} bilangan Negatif")
    else:
        print(f"Angka {number} bilangan Nol")

CekBilangan (10)