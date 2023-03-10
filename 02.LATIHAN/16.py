import shelve
berkas = open("L200210015", "r")
nim = berkas.readline()
tgl = berkas.readline()
nma = berkas.readline()
kta = berkas.readline()
berkas = shelve.open("Faza Rizqy")
berkas ["biodata"] = [nim, tgl, nma, kta]
berkas.close()

berkas = shelve.open("Faza Rizqy")
print("Tanggal Lahir    : "+berkas["biodata"][1])
print("Nama             : "+berkas["biodata"][2])
print("Kota Asal        : "+berkas["biodata"][3])
berkas.close()