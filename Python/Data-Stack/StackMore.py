class Stack:
    def __init__(self):
        self.stack = []
        
    def kosong (self):
        #Mengecek apakah stack kosong
        return len(self.stack) == 0
    
    def addItem (self, item):
        #Menambahkan item kedalam stack
        self.stack.append(item)
        print(f'item {item} telah ditambahkan ke dalam tumpukan.')
        
    def popItem (self):
        #Mengambil item dari tumpukan (item yang terakhir yang di ambil)
        if not self.kosong():
            removeItem = self.stack.pop()
            print(f'Item {removeItem} telah diambil dari tumpukan.')
            return removeItem
        else:
            print(f'Tumpukan kosong. Tidak ada item untuk diambil.')
            return None
    
    def TopItem (self):
        #Melihat item teratas dari tumpukan tanpa mengambilnya
        if not self.kosong():
            top = self.stack[-1]
            print(f'Item {top} adalah item teratas pada tumpukan.')
            return top
        else:
            print(f'Tumpukan kosong. Tidak ada item teratas')
            return None
        
    def sizee (self):
        #Mendapatkan jumlah item dalam tumpukan
        return len(self.stack)
    
    def Display (self):
        #Menampilkan isi stack
        if not self.kosong():
            print(f'Isi Tumpukan: {self.stack}')
        else:
            print(f'Tumpukan kosong.')
            
if __name__ == "__main__":
    TumpukanAngka = Stack()
    TumpukanAngka.addItem('A')
    TumpukanAngka.addItem('B')
    TumpukanAngka.addItem('C')
    TumpukanAngka.addItem('D')
    TumpukanAngka.Display()
    TumpukanAngka.TopItem()
    TumpukanAngka.popItem()
    TumpukanAngka.Display()
    
    
            
        
    