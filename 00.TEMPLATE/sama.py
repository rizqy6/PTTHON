def greetAlbert():
   print("Hi Albert")
   print("Nice to see you!")
 
def greetBryan():
   print("Hi Bryan")
   print("Nice to see you!")
 
def greetCharlie():
   print("Hi Charlie")
   print("Nice to see you!")
 
print(greetBryan())

prodi = "Informatika"
 
def isiKRS(nim):
    pesan = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mengisi KRS"
    print(pesan)
    return None
 
def cetakKHS(nim):
    pesan = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mencetak KHS"
    print(pesan)
    return None
 
isiKRS("ST001")
cetakKHS("ST001")

def luasSegitiga(alas, tinggi):
   """Mengembalikan luas segitiga dengan dengan input alas dan tinggi"""
   luas = 0.5 * alas * tinggi
   return luas
   a = '120'
   t = '150'
   print(f"luas segitiga dengan alas {a} dan tinggi {t} adalah {luas}")
   
def luasLingkaran(r):
    """Mengembalikan luas lingkaran berjari-jari r"""
    pi = 3.14159
    return pi * r ** 2
 
ls = luasLingkaran(14)
print(ls)

def factorial(angka):
    # base case
    if angka == 1 or angka == 0:
       return (angka)
 
    # recursive case
    else:
       return (angka*factorial(angka-1)) #step reduction
 
bil = int(input("Masukan Bilangan : "))
print("Nilai faktorial dari "+ str(bil) + " adalah : " + str(factorial(bil)))
 
   
