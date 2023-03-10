# Untuk mengacak angka menggunakan random
# Fungsi radiant akan dipanggil random yang bertugas untuk mengacak angka bilangan bulat sesuai argumen yang diberikan
# Fungsi radiant  menerima 2 argumen nilai atas dan bawah

#import random
#print (random.randint(1, 100))

import random
angka_rahasia = random.randint(10, 40)

print('# ' * 27)
print('Saya sudah menyimpan angkanya, Silahkan kalian tebak !')
print('# ' * 27)

batas_percobaan = 5

for percobaan in range(batas_percobaan):
    Jawaban = int(input(f'\n [percobaan {percobaan +1} ] Masukan angka : '))

    if Jawaban == angka_rahasia:
        print('Selamat, Anda mendapat hadiah dari Bapak Husni')
        break
    else:
        print(
            'Tebakanmu terlalu' , 'kecil' if Jawaban < angka_rahasia else 'besar'
        )
else: 
    print(f'\nBukan maen, kamu sudah salah menebak sebanyak {batas_percobaan}x!')
    
print("Inilah jawabannya = ", angka_rahasia)