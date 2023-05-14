def perkalian_matriks(matriks1, matriks2):
    baris1 = len(matriks1)
    kolom1 = len(matriks1[0])
    baris2 = len(matriks2)
    kolom2 = len(matriks2[0])

    # Periksa apakah jumlah kolom matriks1 sama dengan jumlah baris matriks2
    if kolom1 != baris2:
        print("Error: Jumlah kolom matriks1 harus sama dengan jumlah baris matriks2")
        return None

    # Buat matriks hasil dengan ukuran yang sesuai
    matriks_hasil = [[0] * kolom2 for _ in range(baris1)]

    # Lakukan perkalian matriks
    for i in range(baris1):
        for j in range(kolom2):
            for k in range(kolom1):
                matriks_hasil[i][j] += matriks1[i][k] * matriks2[k][j]

    return matriks_hasil

# Matriks A (1x2)
matriks_a = [[1, 2]]

# Matriks B (2x3)
matriks_b = [[3, 4, 5],
             [6, 7, 8]]

# Memanggil fungsi perkalian matriks
matriks_c = perkalian_matriks(matriks_a, matriks_b)

# Menampilkan matriks C
if matriks_c:
    for baris in matriks_c:
        print(baris)
