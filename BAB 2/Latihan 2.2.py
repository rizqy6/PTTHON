class Pesan(object):
    """
        Sebuah class bernama pesam.
        Untuk memahami konsep Class dan Obejct
    """
    def __init__(self,sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakekHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai',len(self.teks),'karakter')
    def perbarui(self,stringBaru):
        self.teks = stringBaru

pesanA = Pesan('Aku suka kuliah ini')
pesanB = Pesan('Surakarta: the spirit of java')

pesanA.cetakIni()
pesanA.cetakPakekHurufKapital()
pesanA.cetakPakaiHurufKecil()
pesanA.jumKar()
pesanA.cetakJumlahKarakterku()
pesanA.perbarui('Andaiku bisa kembali')
pesanA.cetakIni()