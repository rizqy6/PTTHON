# L200210015
# Faza Rizqy Septin Rezsuwandi

selesai = False

while not selesai:
    bilangan = int(input("Masukkan sebuah bilangan: "))
    if bilangan % 2 == 0:
        print(bilangan, "adalah bilangan genap")
    else:
        print(bilangan, "adalah bilangan ganjil")
    
    jawaban = input("Apakah Anda ingin memeriksa bilangan lain? (ya/tidak) ")
    if jawaban.lower() == "tidak":
        selesai = True