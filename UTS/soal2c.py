def buat_matriks_identitas(ordo):
    matriks_identitas = [[0] * ordo for _ in range(ordo)]
    for i in range(ordo):
        matriks_identitas[i][i] = 1
    return matriks_identitas

# Membuat matriks identitas dengan ordo (7x7)
matriks_identitas = buat_matriks_identitas(7)

# Menampilkan matriks identitas
for baris in matriks_identitas:
    print(baris)
