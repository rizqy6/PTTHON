def jumlahHurufKonsonan(x): #Nomor3 b
    vokal = "aiueoAIUEO"
    a = 0
    hasil = 0

    for i in x:
        if i in vokal:
            a = a+1
    hasil = len(x),len(x)-a
    return hasil

print(jumlahHurufKonsonan('surakarta'))