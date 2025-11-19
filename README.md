QUEUE  
Queue = antrian  
Queue menggunakan metode **FIFO (First In First Out)** → yang masuk duluan, keluar duluan

1️ Membuat Queue
```
queue = []
```

2 Enqueue (Menambah Elemen)
Membuat queue kosong dengan tipe list.
```
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)
```
append() menambah elemen di belakang antrian.
Hasil output:
```
['A', 'B', 'C']
```

3️ Dequeue (Menghapus Elemen Depan)
```
element = queue.pop(0)
print("Dequeue: ", element)
```
pop(0) menghapus elemen pertama (index 0).
Nilai yang dihapus disimpan di variabel element.

4️ Peek (Melihat Elemen Depan Tanpa Menghapus)
```
frontElement = queue[0]
print("Peek: ", frontElement)
```
queue[0] mengambil elemen paling depan tanpa menghapusnya.

5️ isEmpty (Cek Queue Kosong atau Tidak)
```
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)
```
not bool(queue) → True jika queue kosong.

6️ Size (Jumlah Elemen)
```
print("Size: ", len(queue))
```
len(queue) menghitung jumlah elemen dalam queue.


STACK
Stack = tumpukan data
Stack menggunakan metode LIFO (Last In First Out) → yang masuk terakhir, keluar duluan.

1 membuat stack
```
stack = []
```
membuat stack  kosong

2️ Push (Menambah Elemen ke Atas Stack)
```
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)
```
append() menambah elemen ke atas tumpukan.
Hasil urutan stack:
```
['A', 'B', 'C']
```

3️ Pop (Menghapus Elemen Teratas)
```
element = stack.pop()
print("Pop: ", element)
```
pop() menghapus elemen terakhir (teratas).
Misal stack = ['A', 'B', 'C'] → yang keluar 'C'.

4️ Peek (Melihat Elemen Paling Atas)
```
topElement = stack[-1]
print("Peek: ", topElement)
```
stack[-1] mengambil elemen paling atas tanpa menghapus.

5️ isEmpty (Cek Stack Kosong)
```
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)
```
True jika stack kosong.

6️ Size (Jumlah Elemen di Stack)
```
print("Size: ", len(stack))
```
Menampilkan jumlah elemen dalam stack.

