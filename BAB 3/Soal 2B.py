#Nomor 2B
def buatIdentitas(m):
    n = m
    print("membuat matriks identitas dengan ordo"+str(n)+"x"+str(n))
    matriks = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matriks)

buatIdentitas(4)
buatIdentitas(5)