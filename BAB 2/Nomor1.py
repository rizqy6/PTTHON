class Pesan(object):
    def __init__(self,a):
        self.a = a
    def apakahTerkandung(self, b):
        return b in self.a
    def hitungKonsonan(self):
        itung = 0
        vokal = ["a","i","u","e","o","A","I","U","E","O"]
        for i in self.a:
            if i not in vokal:
                itung+=1
        return itung
    def hitungVokal(self):
        itung = 0
        vokal = ["a","i","u","e","o","A","I","U","E","O"]
        for i in self.a:
            if i in vokal:
                itung+=1
        return itung

p9 = Pesan('Indonesia adalah negeri yang indah')
print(p9.apakahTerkandung('ndo'))
print(p9.apakahTerkandung('eka'))

p10 = Pesan('Surakarta')
print(p10.hitungKonsonan())
print(p10.hitungVokal())