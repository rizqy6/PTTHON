# Modul fungsi dengan 7 Kunci

data = {
    "Nama"       : "Rizqy",
    "Usia"       : "18",
    "Alamat"     : "Jepara",
    "Kode Pos"   : "",
    "NIM"        : "",
    "Mata Kuliah": "Praktikum Algoritma dan Pemrograman",
    "Kelas"      : "A",
    "Fakultas"   : "FKI",
    }

#fungsi data diri

def tampilkanNama():
    nama = data["Nama"]
    print ("Nama \t: ", nama)
def tampilkanUsia():
    usia = data["Usia"]
    print ("Usia \t: ", usia)

def tampilkanAlamat():
    alamat = data["Alamat"]
    print ("Alamat \t: ", alamat)

def tampilkanKode_Pos():
    kodepos = data["Kode Pos"]
    print ("Kode Pos \t: ", kodepos)

def tampilkanNIM():
    nim = data["NIM"]
    print ("NIM \t: ", nim)

def tampilkanMata_Kuliah():
    matakuliah = data["Mata Kuliah"]
    print ("Mata Kuliah \t: ", matakuliah)

def tampilkanKelas():
    kelas = data["Kelas"]
    print ("Kelas \t: ", kelas)

def tampilkanFakultas():
    fakultas = data["Fakultas"]
    print ("Fakultas \t: ", fakultas)

def show_menu():
    print('\n')
    print('-----Pilihan-----')
    print("""\
        [1] Nama
        [2] Usia
        [3] Alamat
        [4] Kode pos
        [5] NIM
        [6] Mata Kuliah
        [7] Kelas
        [8] Fakultas
        [9] Keluar
        """)

    menu = int(input('Pilihan Daftar> '))
    print('\n')
    if   menu == 1:
        tampilkanNama()
    elif menu == 2:
        tampilkanUsia()
    elif menu == 3:
        tampilkanAlamat()
    elif menu == 4:
        tampilkanKode_Pos()
    elif menu == 5:
        tampilkanNIM()
    elif menu == 6:
        tampilkanMata_Kuliah()
    elif menu == 7:
        tampilkanKelas()
    elif menu == 8:
        tampilkanFakultas()
    elif menu == 9:
        print('Anda telah keluar')
    else:
        print('Masukan input dengan benar')
        
if __name__ == "__main__":
    show_menu()