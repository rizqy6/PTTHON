class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)

class mahasiswa(manusia):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama + "" +'Nim'+str(self.nim)+ "" +'kota'+self.kota+ "" +'uang saku'+self.uangsaku+'/bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilKotaTinggal(self):
        return self.kota
    def ambilUangSaku(self):
        return self.uangsaku
    def perbaruiKotaTinggal(self,b):
        self.kota=b
    def tambahUangSaku(self,c):
        self.uangsaku+=c
m9 = mahasiswa('Rizqy', 'L200210015', 'Jepara', 50000)
print(m9.ambilKotaTinggal())
m9.perbaruiKotaTinggal('Solo')
print(m9.ambilKotaTinggal())
print(m9.ambilUangSaku())
m9.tambahUangSaku(100000)
print(m9.ambilUangSaku())