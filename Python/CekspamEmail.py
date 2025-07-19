#Studi kasus email spam
#Algoritma sederhana

def CekSpamEmail (email):
    #Membuat daftar kata spam
    kataSpam = [
        'gratis', 'menang hadiah', 'transfer uang', 'klik link', 'promo', 'diskon', 'pinjaman cepat', 'uang tunai', 'dapatkan segera', 'tanpa biaya'
    ]
    #konversi email ke huruf kecil agar pencocokan email tidak case -sensitive
    emailLower = email.lower()
    
    #cek apakah terdapat kata spam didalam emaiil
    
    for kata in kataSpam:
        if kata in emailLower:
            return "Email mengandung spam."
    return 'Email bebas dari kata spam.'

#contoh
emailAndi = 'selamat! anda mendapatkan uang tunai sebesar 1jt rupiah. klik link dibawah ini.'

emailRehan = 'Selamat siang kak rehan terkait proposal seminar sudah sampai mana ya?.'

print(f'Cek email andi:', CekSpamEmail(emailAndi))

print(f'Cek email Rehan: ', CekSpamEmail(emailRehan))