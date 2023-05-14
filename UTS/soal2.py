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
matriks1 = [[1, 2, 3],
            [4, 5, 6]]

matriks2 = [[7, 8],
            [9, 10],
            [11, 12]]

hasil = perkalian_matriks(matriks1, matriks2)

if hasil:
    for baris in hasil:
        print(baris)
