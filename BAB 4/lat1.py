class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilKota(self):
        return self.kota
    def ambilUangSaku(self):
        return self.uangSaku
        
c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten', 240000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

target = 'Klaten'
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama+ ' tinggal di '+target)

def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1

    while low <=high:
        mid  = (high + low) //2
        if kumpulan[mid] < target:
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False


A = [10, 51,2,18,4,31,5,23,64,29]
print('------------------------------------------------------------')

print(cariLurus(A, 5))

print('------------------------------------------------------------')

B = [10, 51,2,18,4,31,5]
print(cariTerkecil(B))

print('------------------------------------------------------------')

C = [10, 51,2,18,4,31,5]
print(binSe(C, 51))

