##linkedlist##
---

Linked List adalah struktur data yang terdiri dari node-node yang saling terhubung menggunakan pointer.  
Setiap **node** memiliki:
- `data` → nilai/data yang disimpan
- `next` → pointer menuju node berikutnya

Linked List digunakan ketika kita ingin struktur data yang fleksibel dan dinamis.

---
1. Class Node
```
class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.next = pointer
```
Penjelasan:
**Node** mewakili satu simpul dalam Linked List.
**data** menyimpan nilai.
**next** menunjuk ke node berikutnya.
Jika next = None, berarti node tersebut berada di akhir list.

2. Class LinkedList
```
class LinkedList:
    def __init__(self):
        self.head = None
```
Penjelasan:
head adalah node pertama dalam Linked List.
Jika head = None, berarti list masih kosong.

3. insert_at_first() — Menambah di Awal
```
def insert_at_first(self, data):
    node = Node(data, self.head)
    self.head = node
```
Penjelasan:
Membuat node baru lalu menunjuk head lama.
Node baru menjadi head (paling depan).

4. insert_at_last() — Menambah di Akhir
```
def insert_at_last(self, data):
    if self.head is None:
        self.head = Node(data)
    else:
        node_sekarang = self.head
        while node_sekarang.next:
            node_sekarang = node_sekarang.next
        node_sekarang.next = Node(data)
```
Penjelasan:
Jika kosong → node baru jadi head.
Jika tidak → loop sampai node terakhir (next = None)
Tambahkan node baru di akhir.

5. insert_at() — Menambah pada Index Tertentu
```
def insert_at(self, index, data):
    if index < 0 or index > self.length():
        print("index tidak valid")
    elif index == 0:
        self.insert_at_first(data)
    else:
        urutan = 0
        node_sekarang = self.head
        while urutan < index - 1:
            node_sekarang = node_sekarang.next
            urutan += 1
        node = Node(data, node_sekarang.next)
        node_sekarang.next = node
```
Penjelasan:
Jika index 0 → langsung panggil insert_at_first()
Jika index valid → pindah ke posisi sebelum index
Sisipkan node di tempat yang tepat.

6. remove_first() — Hapus Node Pertama
```
def remove_first(self):
    if self.head is None:
        print("tidak ada data yang bisa dihapus")
    else:
        self.head = self.head.next
```
Penjelasan:
Head baru akan menjadi node kedua.

7. remove_last() — Hapus Node Terakhir
```
def remove_last(self):
    if self.head is None:
        print("tidak ada data yang bisa dihapus")
    elif self.head.next is None:
        self.head = None
    else:
        node_sebelumnya = None
        node_sekarang = self.head
        while node_sekarang.next:
            node_sebelumnya = node_sekarang
            node_sekarang = node_sekarang.next
        node_sebelumnya.next = None
```
Penjelasan:
Jika hanya 1 node → hapus head.
Jika lebih → cari node terakhir dengan looping.
node_sebelumnya.next = None → menghapus node terakhir.

8. remove_at() — Hapus di Index Tertentu
```
def remove_at(self, index):
    if index < 0 or index >= self.length():
        print("index invalid")
    elif index == 0:
        self.remove_first()
    else:
        urutan = 0
        node_sekarang = self.head
        while urutan < index - 1:
            node_sekarang = node_sekarang.next
            urutan += 1
        node_sekarang.next = node_sekarang.next.next
```
Penjelasan:
Jika index = 0 → panggil remove_first()
Jika index tengah → lewati node target dan sambungkan ke node setelahnya.

9. length() — Hitung Jumlah Node
```
def length(self):
    count = 0
    node = self.head
    while node:
        count += 1
        node = node.next
    return count
```
Penjelasan:
Loop dari head sampai node terakhir.
Hitung jumlahnya.

10. print() — Menampilkan Isi Linked List
```
def print(self):
    if self.head is None:
        print("data kosong")
    else:
        text_print = ''
        node_sekarang = self.head
        while node_sekarang:
            text_print += str(node_sekarang.data) + " -> "
            node_sekarang = node_sekarang.next
        print(text_print)
```
Penjelasan:
Jika kosong → tampilkan pesan.
Jika ada → tampilkan semua data dalam bentuk:
```
10 -> 20 -> 30 ->
```
