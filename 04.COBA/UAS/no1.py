def nilai_maksimal (list):
  nilai_terbesar = list[0]

  if len(list) > 1:
    next_nilai_terbesar = nilai_maksimal(list[1:])

    if next_nilai_terbesar > nilai_terbesar:
      nilai_terbesar = next_nilai_terbesar

  return nilai_terbesar


a = [3, 6, 10, 1, 5]
print(a)
print('Nilai terbesar:', nilai_maksimal(a))

jumlah = sum(a)
print ("jumlahnya adalah :", jumlah)