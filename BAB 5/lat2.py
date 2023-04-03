def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    PosisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A [PosisiYangTerkecil]:
            PosisiYangTerkecil = i
    return PosisiYangTerkecil

A = [18,13,44,25,66,107,78,89]
j = cariPosisiYangTerkecil(A, 2, len(A))
print(j)

