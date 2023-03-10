def apakah_kabisat (tahun):
    habis_dibagi_400 = tahun % 400 == 0
    habis_dibagi_100 = tahun % 100 == 0
    habis_dibagi_4 = tahun % 4 == 0

    return  habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100)

tahun_awal = int(input('Masukan tahun awal \t: '))
tahun_akhir= int(input('Masukan tahun akhir \t: '))

tahun_kabisat = []

for tahun in range(tahun_awal, tahun_akhir + 1):
    if apakah_kabisat(tahun):
        tahun_kabisat.append(tahun)

print('Tahun kabisat : ')
print(tahun_kabisat)

#membuat rumus menggunkan tipe bolean



