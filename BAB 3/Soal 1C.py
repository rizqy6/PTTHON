#Nomor 1C
a = [[1,2],[3,4],[5,6]]
b = [[7,8],[9,10]]
c = [[3,6],[5,2]]
def Ordo(matriks):
    return("Ordo Matriks = "+str(len(matriks))+" x "+str(len(matriks[0])))

def Jumlah(matriks1,matriks2):
    if Ordo(matriks1) == Ordo(matriks2):
        for x in range(0, len(matriks1)):
            for y in range(0, len(matriks1[0])):
                print(matriks1[x][y] + matriks2[x][y],' '),
            print()
    else:
        print("Matriks Tidak Sesuai")


Jumlah(a, b)
Jumlah(b, c)