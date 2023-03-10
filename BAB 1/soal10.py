from math import sqrt as detr  #Nomor10
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = float(b*2 - 4*a*c)
    if(D < 0):
        hasil = "Determinan negatif, persamaan tidak mempunyai akar real"
        return hasil
    else:
        x1 = (-b + detr(D)) / (2*a)
        x2 = (-b + detr(D)) / (2*a)
        return hasil

print(selesaikanABC(2, 5, 7))