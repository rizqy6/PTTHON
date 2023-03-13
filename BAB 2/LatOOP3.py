class Manusia(object):
    """
        Class 'Manusia' dengan inisaisi 'nama'
    """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan',s)
        self.keadaan = 'kenyang'
    def olaraga(self, k):
        print('saya baru latihan',k)
        self.keadaan = 'lapar'
    def mengalihkanDenganDua(self,n):
        return n*2

p1 = Manusia('rizqy')
p1.ucapkanSalam()

