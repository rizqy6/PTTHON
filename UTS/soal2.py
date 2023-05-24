# Matriks A
A = [[1, 2],
     [3, 4]]

# Matriks B
B = [[5, 6],
     [7, 8]]

# Inisialisasi matriks hasil perkalian dengan elemen 0
hasil = [[0, 0],
         [0, 0]]

# Perkalian matriks
for i in range(2):
    for j in range(2):
        for k in range(2):
            hasil[i][j] += A[i][k] * B[k][j]

# Menampilkan matriks hasil
for row in hasil:
    print(row)