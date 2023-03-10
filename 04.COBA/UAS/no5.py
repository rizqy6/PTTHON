def simpanProduk():
    n = 4
    key = ["nama_produk", "id_produk", "jumlah_produk"]
    tempat1 = []
    tempat2 = []
    tempat3 = []
    tempat  = []
    for i in range(1, n):
        s = input("input iterasi ke-{i} \n".format(i=i))
        listak = s.split(" / ")
        for j in range(len(listak)):
            newlist = listak[j].split(" : ")
            values = str(newlist[1])
            if i  == 1:
                tempat1.append(values)
            elif i == 2:
                tempat2.append(values)
            elif i == 3:
                tempat3.append(values)

    isi1 = dict(zip(key, tempat1))
    isi2 = dict(zip(key, tempat2))
    isi3 = dict(zip(key, tempat3))

    tempat.append(isi1)
    tempat.append(isi2)
    tempat.append(isi3)
    return tempat

print(simpanProduk())