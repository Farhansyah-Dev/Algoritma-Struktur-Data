#Program implementasi Stack

class Stack:
    def __init__ (self):
        #Inisialisasi tumpukan kosong
        self.items = []
        
  
    def stackKosong(self):
        #Memeriksa apakah tumpukan piring kosong
        return len(self.items) == 0
    
    def menambahkanItem (self, item):
        #Menambahkan piring baru ke dalam tumpukan
        self.items.append(item)
        print(f'{item} piring ditambakan dalam tumpukan piring.')
    
    def hapusItem (self):
        #Menghapus piring paling atas stack (tumpukan)
        if self.stackKosong ():
            print(f'Tumpukan piring kosong. Tidak ada piring yang bisa dihapus.')
            return None
        return self.items.pop()
        
    def peek(self):
        #Melihat piring paling atas tanpa menghapusnya
        if self.stackKosong():
            print(f'Tumpukan piring kosong. Tidak ada piring yang bisa dilihat.')
            return None
        return self.items[-1]
    
    def size(self):
        #Mengembalikan ukuran ukuran tumpukan
        return len(self.items)
    
#Penggunaan Stack
if __name__=="__main__":
    tumpukanPiring = Stack()
    tumpukanPiring.menambahkanItem(1) #Menambahkan item 10 ke tumpukanPiring
    tumpukanPiring.menambahkanItem(2) #menambahkan item 20 ke tumpukanPiring
    tumpukanPiring.menambahkanItem(3) #Menambahkan item 30 ke tumpukanPiring
    
    print(f'piring paling atas: {tumpukanPiring.peek()}') #Melihat item paling atas
    print(f'Menghapus Item: {tumpukanPiring.hapusItem()}') #Menhapus item paling atas
    print(f'Ukuran Stack: {tumpukanPiring.size()}') #Mengecek ukuran Stack
