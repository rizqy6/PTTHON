from datetime import date
hari = date.today()
print('Hari ini tanggal \t: ', hari)

GanjilGenap = str(hari.day)
print('Hari ini tanggal \t: ',GanjilGenap)
A = int(GanjilGenap)
if A % 2 == 0:
    print("Jadi hari ini tanggal Genap")
else :
    print("Jadi hari ini tanggal ganjil")