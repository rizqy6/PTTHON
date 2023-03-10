def Mengubah_Spasi(kata):
    """Kegunaan fungsi untuk mengubah spasi berlebih menjadi spasi tunggal, fungsi menerima argumen dari teks, dan mengembalikan teks dengan  tunggal jika teks yang diterima memiliki spasi berlebih. 
    Faza Rizqy Septin Rezsuwandi(L200210015)"""
    spasi = ""
    for z in kata:
        if z!= " " or spasi[-1] != " ":
            spasi += z
    return spasi


print("Program mengembalikan spasi berlebih dan diganti spasi tunggal")
kata = input("Masukkan kata yang baik \t: ")
Hasilnya = Mengubah_Spasi(kata)
print(Hasilnya)

def convert(x):
	return ([i for item in x for i in item.split()])

