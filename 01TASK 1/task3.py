Nama=''
NIM=''
x='1' + NIM[7:]
a= int(x)
b= len(Nama)
c = 12.5

print(type(a))          #Bernilai integer karena nim yang diinputkan merupakan bil bulat
print(type(b))          #Bernilai integer karena dikonversi dari string menjadi bil bulat/angka
print(a/b)              #Hasilnya 36.25 karena pembagian antara 1015 dan 28  
print(a//b)             #Hasilnnya 36 karena pembagian bulat antara 1015 dan 28
print(10 * (a - 999))   #Hasilnya 160 karena dari operasi seperti disamping
print(b ** 2)           #Hasilnya 784 karena pangkat dari 28
print( a % b)           #Hasilnya 7 karena sisa bagi dari 1015 dan 28



print(type(c))          #bertype float karena angkanya bernilai desimal
print(a/c)              #Hasilnya 81.2 pembagian antara 1015 dan 12.5
print(a//c)             #Hasilnya 81 pembagian bulat antara 1015 dan 12.5
print( a % c)           #Hasilnya 7 sisa bagi dari 1015 dan 12.5

print( c > b)           #Bernilai false karena c lebih kecil dari b
print(type(c > b))      #Bertype bool karena menentukan nilai benar atau salah
print(a>b)and(b>c)      #Bernilai benar karena kedua operator and bernilai benar
print(a>1100)or(b<10)   #Bernilai false karena salah satunya bernilai false sehingga operator or akan menilai false


