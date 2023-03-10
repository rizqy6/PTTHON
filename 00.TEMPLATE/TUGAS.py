#Program menerima teks dan mengembalikan teks lain dengan spasi berlebih setelah menjadi spasi tunggal
Kata_Doa = "Nama     Saya    Faza  Rizqy  Septin Rezsuwandi"
def Mengubah_Spasi(str):
    spasi = ""
    for a in str:
        if a!=" " or spasi[-1] != " ":
            spasi += a
    return spasi
s = Mengubah_Spasi(Kata_Doa)
print(s)