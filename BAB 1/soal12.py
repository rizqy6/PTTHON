import random  #Nomor12
def tebak():
    a = random.randrange(1,101,1)
    b = -1
    n = 0
    print("Permainan Tebak Angka")
    print("Saya Menyimpan Sebuah Angka Bulat antara 1 sampai 100. Coba Tebak.")

    while(a != b):
        n = n + 1
        b = int(input("Masukkan Tebakan ke- " + str(n) + ":> "))
        if(b < a):
            print("Itu Terlalu Kecil. Coba lagi")
        elif(b > a):
            print("Itu Terlalu Besar. Coba lagi")
        else:
             print("Ya. Anda Benar.")
             break
print(tebak())