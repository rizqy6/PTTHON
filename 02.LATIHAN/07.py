# Membuat pasword
pa = str(input(('Masukan Password \t: ')))
nama = 'Faza Rizqy Septin Rezsuwandi'
password = nama

if pa == password:
    print('Anda berhasil login')
else:
    print("Maaf, Anda salah memasukan password")
    pa = str(input(('Masukan Password \t:')))
    print("Maaf, Anda salah memasukan password")
    pa = str(input(('Masukan Password \t:')))
    print('Anda telah mencoba 3x. Akses anda ditolak.')

#membuat ucapaan dengan jam

waktu = ('pagi','siang','sore','petang','malam')
nama_asli = input(('Masukan nama Saudara \t: '))
jam =float(input('Pukul berapa sekarang? \t: '))

if 0 <= jam <= 11:
    print('Selamat', waktu[0], nama_asli)
elif 11 < jam <= 14:
    print('Selamat', waktu[1], nama_asli)
elif 14 < jam <= 17:
    print('Selamat', waktu[2], nama_asli)
elif 17 < jam <= 20:
    print('Selamat', waktu[2], nama_asli)
elif 20 < jam <= 24:
    print('Selamat', waktu[2], nama_asli)
else:
    print('Masukan jam hanya dari pukul 01.00-24.00')

#membuat dictonary

R = {
        'Segitiga'          : 'L = 0.5 *a * t',
        'Persegi '          : 'L = s **2',
        'Persegi Panjang'   : 'L = p * l',
        'Lingkaran'         : 'L = pi * r **2',
        'Jajar Genjang'     : 'L = a * t'
    }
print(f"""
No | Nama bangun     | Rumus Luas
---|-----------------|-----------------
1  | Segitiga        | {R['Segitiga']}
2  | Persegi         | {R['Persegi '] }
3  | Persegi panjang | {R['Persegi Panjang']}
4  | Lingkaran       | {R['Lingkaran']}
5  | Jajaran genjang | {R['Jajar Genjang']}
""" )   

