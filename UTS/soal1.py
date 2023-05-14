# PERSEGI
def hitung_luas_persegi(): # membuat fungsi
    sisi1 = float(input("Masukkan panjang persegi: ")) # input sisi dengan tipe data float
    sisi2 = float(input("Masukkan lebar persegi: ")) # input sisi dengan tipe data float
    luas = sisi1 * sisi2 # menggunakan rumus persergi
    return luas # mengembalikan nilai untuk ditampung sementara

luas_persegi = hitung_luas_persegi() # memebuat tempat untuk hasil dari fungsi
print("Luas persegi adalah:", luas_persegi) # mencetak hasil


# LINGKARAN
def hitung_luas_lingkaran():
    jari = float(input("Masukkan jari jari lingkaran: ")) 
    luas =  3.14 * jari * jari
    return luas
luas_lingkaran = hitung_luas_lingkaran()
print("luas lingkaran adalah:", luas_lingkaran)



# SEGITIGA
def hitung_luas_segitiga():
    a = float(input("masukan alas segitiga:"))
    t = float(input("masukan tinggi segitiga: "))
    luas = 0.5 * a * t
    return luas
luas_segitiga = hitung_luas_segitiga()
print('luas segitiga adalah', luas_segitiga)



# BELAH KETUPAT
def hitung_luas_ketupat():
    d1 = float(input("masukan d1:"))
    d2 = float(input("masukan d2: "))
    luas = 0.5 * d1 * d2
    return luas
luas_ketupat = hitung_luas_ketupat()
print('luas segitiga adalah', luas_ketupat)

# untuk tipe data bisa disesuaikan karena disini saya pakai float agar biar dapat memuat angka pecahan agar hasil lebih akurat