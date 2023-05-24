class PersonalData:
    def __init__(self, nama, umur, warna_kulit):
        self.nama = nama
        self.umur = umur
        self.warna_kulit = warna_kulit

    def dataNama(self):
        print("Nama:", self.nama)

    def dataUmur(self):
        print("Umur:", self.umur)

    def dataWarnaKulit(self):
        print("Warna Kulit:", self.warna_kulit)


# Membuat objek personal data
data1 = PersonalData("John", 25, "Putih")
data2 = PersonalData("Sarah", 30, "Sawo Matang")
data3 = PersonalData("Michael", 40, "Kuning Langsat")
data4 = PersonalData("Emily", 28, "Putih")
data5 = PersonalData("Daniel", 35, "Sawo Matang")
data6 = PersonalData("Olivia", 32, "Putih")
data7 = PersonalData("William", 27, "Kuning Langsat")
data8 = PersonalData("Sophia", 22, "Putih")
data9 = PersonalData("James", 38, "Sawo Matang")
data10 = PersonalData("Ava", 29, "Putih")
data11 = PersonalData('sabillacantikeram', 10, 'sawokuninglangsatbersihsekali')

# Mengakses data dari objek personal data
data1.dataNama()
data1.dataUmur()
data1.dataWarnaKulit()

data11.dataNama()
data5.dataNama()
data5.dataUmur()
data5.dataWarnaKulit()

