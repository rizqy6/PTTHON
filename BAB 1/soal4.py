def rerata(b):  #Nomor4
    jumlah = 0
    for i in range(len(b)):
        jumlah += b[i]
    jumlah = jumlah/len(b)
    return jumlah

print(rerata([1,2,3,4,5,6]))