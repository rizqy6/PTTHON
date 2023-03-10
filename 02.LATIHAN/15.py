#membuat data
berkas = open("L200210015", "w")
berkas.write("L200210015")
berkas.close

#menambahkakn data
berkas = open("L200210015", "a")
berkas.write("\n10-09-2003")
berkas.write("\nFaza Rizqy Septin Rezsuwandi")
berkas.close

#menambah kota
berkas = open("L200210015", "a")
berkas.write("\nJepara")
berkas.close

#menyimpan data
berkas = open("L200210015", "r")
nim = berkas.readline()
tgl = berkas.readline()
nma = berkas.readline()
kta = berkas.readline()

#slicing format tanggal
dd = tgl[:2]
mm = tgl [3:5]
yy = tgl [6:]

tgl = mm+"/"+dd+"/"+yy

print(nma)
print(kta,tgl)
print(nim)
berkas.close()