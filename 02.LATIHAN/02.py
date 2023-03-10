jumlah_barang = int(input('Masukan jumlah barang : '))

satuan_lusin = jumlah_barang / 12
satuan_kodi  = jumlah_barang / 20
satuan_gross = jumlah_barang / 144

#Pengkondisian konversi

if satuan_lusin % 1 == 0:
    satuan_lusin = int (satuan_lusin)
if satuan_kodi % 1 ==0:
    satuan_kodi = int(satuan_kodi)
if satuan_gross % 1 == 0:
    satuan_gross = int (satuan_gross)

print(f'{jumlah_barang} = {satuan_lusin} lusin ')
print(f'{jumlah_barang} = {satuan_kodi} kodi ')
print(f'{jumlah_barang} = {satuan_gross} gross')

