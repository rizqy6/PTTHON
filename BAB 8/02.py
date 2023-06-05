##Nomor 1
class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self, data):
        self.items.append(data)

def cetakHexa(b):
    f = Stack()
    if b == 0:
        f.push(0)
    while b !=0:
        sisa = b%16
        b = b//16
        f.push(sisa)
        hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    hasil = ""
    for i in range (len(f)):
        hasil += str(hexa[f.pop()])
    return hasil


##Nomor 2
nilai = Stack()         #membuat sebuah objek dari kelas Stack yang disimpan di variabel "nilai"
for i in range(16):     #untuk i dalam range 16
    if i % 3 == 0:      #jika i habis dibagi 3, maka:
        nilai.push(i)   #meletakkan i di variabel "nilai"

print(nilai.items)