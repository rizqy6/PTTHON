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

# Menyimpan data personal dalam sebuah list
personal_data_list = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

# Fungsi untuk mengurutkan personal data berdasarkan umur
def urutkan_data_berdasarkan_umur(personal_data_list):
    n = len(personal_data_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if personal_data_list[j].umur > personal_data_list[j + 1].umur:
                personal_data_list[j], personal_data_list[j + 1] = personal_data_list[j + 1], personal_data_list[j]

# Mengurutkan data berdasarkan umur
urutkan_data_berdasarkan_umur(personal_data_list)

# Menampilkan data personal yang sudah diurutkan
for data in personal_data_list:
    data.dataNama()
    data.dataUmur()
    data.dataWarnaKulit()
    print()
