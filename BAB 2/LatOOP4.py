from LatOOP3 import Manusia

class Mahasiswa(Manusia):
    """class mahasiswa yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini mentutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM: ' + str(self.NIM)\
            + ', tinggal di : ' + str(self.kotaTinggal)\
                + ', uang saki RP: ' + str(self.uangSaku)\
                    +', tiap bulannya'
        return s

    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        print('Saya baru saja makan',s,"sambil belajar")
        self.keadaan = 'kenyang'
m1 = Mahasiswa("rizqy", 'L200210015', "Jepara", 100000000)
m2 = Mahasiswa("Andi", 'L200210016', "Magelang", 200000000)
m3 = Mahasiswa("Sra", 'L200210017', "Yogyakarta", 300000000)
print(m1.ambilNama())
print(m2.ambilNIM())
m3.ucapkanSalam
m3.makan('pecel')
print(m3.keadaan)
print(m3)