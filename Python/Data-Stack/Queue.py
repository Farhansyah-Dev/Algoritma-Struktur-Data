class Queue:
    def __init__(self, capacity):
        """Inisialisasi queue dengan kapasitas tertentu."""
        
        self.queue = []
        self.capacity = capacity
        
    def insert (self, item):
        """Menambahkan elemen ke queue jika tidak penuh."""
        if not self.full():
            self.queue.append(item)
            print(f'Elemen {item} berhasil ditambahkan ke queue.')
        else:
            print(f'Queue penuh. Tidak dapat menambahkan elemen baru.')
        
    def remove (self):
        """Menghapus elemen pertama dari queue jika tidak kosong."""
        if not self.empty():
            removeItem = self.queue.pop(0)
            print(f'Elemen {removeItem} berhasil dihapus dari queue.')
            return removeItem
        else:
            print(f'Queue kosong. Tidak ada elemen yang dihapus.')
            return None
    def initialize(self):
        """Mengosongkan queue."""
        self.queue = []
        print(f'Queue telah diinisialisasi (dikosongkan).')
        
    def empty (self):
        """Memeriksa apakah queue kosong."""
        return len(self.queue) == 0
    
    def full (self):
        """Memeriksa apakah queue penuh."""
        return len(self.queue) >= self.capacity
    
    def show (self):
        """Menampilkan elemen-elemen dalam queue."""
        if self.empty():
            print("Queue kosong.")
        else:
            print(f'isi queue {self.queue}')
            
#Fungsi utama
def main():
    #Inisialisasi queue dengan kapasitas maksimum 3
    myQueue = Queue(capacity=3)
        
    #Menampilkan queue kosong 
    myQueue.show()
        
    #Menambahkan elemen ke queue
    myQueue.insert('A')
    myQueue.insert('B')
    myQueue.insert('C')
        
    #Menampilkan queue setelah beberapa insert
    myQueue.show()
        
    #Menambahkan elemen ke queue yang penuh
    myQueue.insert('D')
        
    #Menghapus elemen dari queue
    myQueue.remove()
        
    #Menampilkan queue setelah remove
    myQueue.show()
        
    #Menginisalisasi queue mengosongkan
    myQueue.initialize()
        
    #Menampilkan queue setelah diinisialisasi
    myQueue.show()
        
if __name__ == "__main__":
    main()
    