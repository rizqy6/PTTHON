nama = "Fulan"
s = 'Halo, ini sebuah string'
print(nama[0])   # menampilkan karakter ke-0 dari string nama
print(s[3])   # menampilkan karakter ke-3 dari string s
c = s[0] + nama[1] + nama[-2]  # mengambil beberapa karakter dari kedua string, kemudian menggabungkannya
print(s[0] + nama[1] + nama[-2])
print("nama", "saya")
angka = 3 * 4
print(angka)
garis = 50 * "="
sapa = "Halo " + nama + ", aku Python"  # variabel sapa menyimpan hasil penggabungan string
print(sapa)
print(garis)
bolean = 5.2 >= 5	
print(bolean)
bolean = "abu" > "abi"
print(bolean)
bolean = " aba " > " abe "
print(bolean)


matriks = [[1,2,3],[4,5,6],[7,8,9]]
 
for baris in matriks:
   for i in baris:
       if i % 2 != 0:
           print(i**2)

angka = 0
 
for angka in range(0,7):
   if angka == 6:
      break
 
   print('Angka adalah ', angka)
 
print('Perulangan selesai')

for i in range(0,4):
   for j in range(0,i):
      print(i, j)
     
aj = [1, 2, 3, 4, 5, 6, 7, 8, 9, "test"]
print(aj[-4:-2])

print("----------------------------------")
     
k = 10 / 5
type(k)
print(type(k))

self=str (input("Nama kamu siapa ya \t: "))
print(self)
umur =int (input("berapa umur anda \t: "))
if umur >=51:
   print("Hormat senior")
else:
   print("Haloo bro")

option = (input("Masukan nama anda \t: "))
optin = int(input ("Masukan umur anda \t: "))
if optin>=50:
   print("hormat lo ", option)
else:
   print("Halo ya", option)

minuman1= float (input("Harga minuman \t: "))
if minuman1<1000:
   print("Beli 3")
elif minuman1 > 3000: 
   print("Mahal amat")
else :
   print("Beli dua")

angka= int(input("Masukann angka : "))
if angka % 2 == 0:
   
   print("hasil bagi \t: ", angka // 4)
else:
   print("angka pangkat \t: ", angka ** 2)

print("-------------------------------------")
op = input("Masukan nama \t: ")
vokal = "aiueoAIUEO"
if op[0] in  vokal:
   print("Namamu di mulai di konsonan")
else:
   print("Namamu tidak dimulai dari konsonan")
