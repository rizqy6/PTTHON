def apakahTerkandung(a,b):  #Nomor8
    x = True
    for i in range(len(b)):
        if a in b:
            x = True
        else:
            x = False
    return x

h = 'do'
k= 'indonesia tanah air beta'
print(apakahTerkandung(h,k))
print(apakahTerkandung('pusaka', k))