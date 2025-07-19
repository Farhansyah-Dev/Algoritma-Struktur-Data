#Studi kasus Login 
#Contoh sederhana algoritma

username = 'farhan.wrdsyh'
password = 'HanInstagram13'


while True: 
    loginUsername = input("Masukan Username: ")
    LoginPassword = input("Masukan Password: ")

    if loginUsername != username and LoginPassword != password:
        print (f'Login gagal username dan password salah.')
    else :
        print(f"mengarahkan ke beranda Instagram.")