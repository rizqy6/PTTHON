def bilanganPrima(n):  #Nomor6
    bawah = 2
    atas = 1000
    if(bawah >= 1 and atas > 1):
        for i in range(bawah,atas):
            prima = True
            for j in range(2,i):
                if(i%j==0):
                    prima=False
            if(prima == True):
                print(i)
    else:
        print("Bukan Bilangan Prima")

print(bilanganPrima(1000))
