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

# ...

# Metode untuk mencari daftar orang dengan kulit sawo matang
def cari_orang_sawo_matang(data):
    orang_sawo_matang = []
    for personal_data in data:
        if personal_data.warna_kulit == "Sawo Matang":
            orang_sawo_matang.append(personal_data)
    return orang_sawo_matang

# Membuat daftar objek personal data
daftar_personal_data = [
    PersonalData("John", 25, "Putih"),
    PersonalData("Sarah", 30, "Sawo Matang"),
    PersonalData("Michael", 40, "Kuning Langsat"),
    PersonalData("Emily", 28, "Putih"),
    PersonalData("Daniel", 35, "Sawo Matang"),
    PersonalData("Olivia", 32, "Putih"),
    PersonalData("William", 27, "Kuning Langsat"),
    PersonalData("Sophia", 22, "Putih"),
    PersonalData("James", 38, "Sawo Matang"),
    PersonalData("Ava", 29, "Putih")
]

# Menampilkan daftar orang dengan kulit sawo matang
daftar_sawo_matang = cari_orang_sawo_matang(daftar_personal_data)
if len(daftar_sawo_matang) > 0:
    print("Daftar orang dengan kulit sawo matang:")
    for orang in daftar_sawo_matang:
        orang.dataNama()
        orang.dataUmur()
        orang.dataWarnaKulit()
        print("---")
else:
    print("Tidak ada orang dengan kulit sawo matang.")
