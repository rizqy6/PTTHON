#Membuat list angka
angka = [70, 38, 192, 23, 122, 38]
 
#Menambahkan satu elemen 44 setelah elemen terakhir list angka
angka.append(44)
 
#Mencetak list angka
print(angka)
 
#Menghitung jumlah elemen 38 dalam list angka
print(angka.count(38))
 
#Menambahkan satu elemen list [1,2,3] setelah elemen terakhir list angka
angka.append([1,2,3])
 
#Menambahkan item-item satu persatu dari elemen list [4,5,6] setelah elemen terakhir list angka
angka.extend([4,5,6])
 
#Mencetak list angka
print(angka)
 
#Mengembalikan indeks pertama dimana elemen 38
#Meskipun ada >1 elemen 38, yang dikembalikan hanyalah indeks pertamanya saja
print(angka.index(38))
 
#Memasukkan nilai 65 ke dalam list sebagai elemen indeks ke-2 yang baru
#Elemen indeks 2 yang lama bergeser ke kanan, bersama dengan elemen indeks setelahnya
angka.insert(2, 65)
 
#Mencetak list angka
print(angka)
 
#Menghapus dan mengambil elemen indeks ke-8, kemudian nilainya tersimpan pada variabel ambil
ambil = angka.pop(8)
print(ambil)
 
#Mencetak list angka
print(angka)
 
#Menyalin isi list angka ke dalam variabel list balik
balik = angka.copy()
 
#Elemen dari variabel balik, urutan elemennya akan dibalik
balik.reverse()
 
#Mencetak list angka
print(angka)
 
#Mencetak list balik
print(balik)
 
#Menyalin isi list angka ke dalam variabel list urut
urut = angka.copy()
 
#Mengurutkan isi list balik dar nilai terkecil hingga nilai terbesar
urut.sort()
 
#Mencetak list urut
print(urut)


nilai_genap_besar = []
nilai_genap_kecil = []
nilai = [37, 99, 48, 55, 12, 20, 90, 47, 21, 30, 80]
batas = 50
 
for i in nilai:
    if i > batas and i%2 == 0:
        nilai_genap_besar.append(i)
    elif i <= batas and i%2 == 0:
        nilai_genap_kecil.append(i)
 
 
print(nilai_genap_besar)
print(nilai_genap_kecil)