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


#Nomor 8
print(
"""ada dua pola
pertama menggunakan konsep Big-O. Dimana yang dipakai
adalah rumus O(log n) dengan rincian 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
Di mana log berasal dari pangkat log berbasis 2. Dengan begitu dapat mengetahui jumlah
maksimal tebakan.
Untuk pola sendiri:
        apabila ingin menebak angka 70
        
        a = nilai tebakan pertama // 2
        tebakan selanjutnya = nilai tebakan "lebih dari" + a
        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
        tetap nilai lebih dari sebelumnya*
        a = a // 2
    Simulasi
        tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "lebih dari itu"
        tebakan ke 2: 75 (dari 50 + 25) jawaban = "kurang dari itu"
        tebakan ke 3: 62 (dari 50 + 12) jawaban = "lebih dari itu"
        tebakan ke 4: 68 (dari 62 + 6) jawaban = "lebih dari itu"
        tebakan ke 5: 71 (dari 68 + 3) jawaban = "kurang dari itu"
        tebakan ke 6: 69 (dari 68 + 1) jawaban = "lebih dari itu"
        tebakan ke 7: antara 71 dan 69 hanya ada 1 angka = 70!!!
        
kedua menggunakan barisan geometri Sn = 2^n
        barisan yang terjadi adalah : 2, 4, 8, 16, 32, 64
        Misal angka yang akan diebak adalah 68
        Tebakan ke-1 : 64 dijawab lebih dari itu
        Tebakan ke-2 : 96(dari 64 + 32) dijawab "Kurang dari itu"
        Tebakan ke-3 : 80(dari 64 + 16) dijawab "Kurang dari itu"
        Tebakan ke-4 : 72(dari 64 + 8) dijawab "Kurang dari itu"
        Tebakan ke-5 : 68(dari 64 + 4) dijawab "Lebih dari itu"
        Tebakan ke-6 : 70(dari 68 + 2) dijawab "TEPAT"
        """)