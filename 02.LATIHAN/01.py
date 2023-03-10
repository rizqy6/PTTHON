# Membuat sebuah fungsi menggunkan perulangan rekursif

def nilai_maksimal (list):
  nilai_terbesar = list[0]

  if len(list) > 1:
    # proses rekursif
    next_nilai_terbesar = nilai_maksimal(list[1:])

    if next_nilai_terbesar > nilai_terbesar:
      nilai_terbesar = next_nilai_terbesar

  return nilai_terbesar

def nilai_minimal(deret_bilangan):
  nilai_terkecil = deret_bilangan[0]

  for nilai in deret_bilangan:
    if nilai < nilai_terkecil:
      nilai_terkecil = nilai

  return nilai_terkecil

a = [3, 20, 100, -35, 50, 90, 45, 11, 23, 87, -78, 1009]
print(a)
print('Nilai terbesar:', nilai_maksimal(a))
print('Nilai terkecil:', nilai_minimal(a))


