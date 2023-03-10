Nama=''
NIM= 1022
tinggi=1.71
berat=53
Tahunlahir=2003
Aku=(Tahunlahir, berat, tinggi, NIM, Nama)
Data=[Tahunlahir, berat, tinggi, NIM, Nama]
a = NIM % 4


print(type(Aku))        #Bertype tuple  karena nilainya yang tidak dapat diubah
print(Aku[0])           #Hasilnya 2003 karena indeks ke-0 adalah 2003
print(Aku[a])           #Hasilnya 1015 karena a=3 dan indeks ke-3 dari Aku adalah 1015
print(type(Aku[a]))     #Bertype integer karena angka bil bulat    
print(Aku[a:4])         #Hasilnya (1015,) karena dimulai dari indeks ke-3 dan berakhir di indeks ke-4 yang tidak ikut dituliskan
print(type(Aku[4]))     #Bertyoe string karena dalam indeks ke-4 itu adalah nama
#print(Aku[0])= 'oke'   #Eror karena indeks ke-0 ber type integer dan tidak senilai dengan 'oke'


print(type(Data))       #Bertype list karena nilainya dapat diubah dan memiliki urutan penulisan
print(Data[4])          #Hasilnya Faza Rizqy Septin Rezsuwandi karena indeks ke-4 dari data
print(Data[4][5])       #Hasilnya adalah R karena indeks ke-4 karakter ke-5 adalah R  


print(Data[4][a:6])     #Hasilnya a dan R karena indeks ke-4 dan karakter ke-6 
#print(Data[0])= 'ok'   #Eror karena nilainya tidak sebanding
print(Data[-a])         #Hasilnya 1.71 karena indeks nya ke- (-3)
print(range(a))         #Hasilnya (0,3) karena range dari variabel a

#Catatan yang print(Aku[0])= 'oke' dan print(Data[0])= 'ok' diberi tanda komentar karena eror dan nantinya jika program dijalanan tidak bisa
