# def swap (A, p,q):
#     tmp = A[p]
#     A[p] = A[q]
#     A[q] = tmp

# K = [50, 20, 70, 10]
# swap(K, 1, 3)
# print(K)

# def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
#     PosisiYangTerkecil = dariSini
#     for i in range(dariSini+1, sampaiSini):
#         if A[i] < A [PosisiYangTerkecil]:
#             PosisiYangTerkecil = i
#     return PosisiYangTerkecil

# A = [18,13,44,25,66,107,78,89]
# j = cariPosisiYangTerkecil(A, 2, len(A))
# print(j)

def urut(a):
    n = len(a)
    for i in range (n-1):
        for j in range(n-i-1):
            if a[j]> a[j+1]:
                swap(a,j,j+1)
def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


L =[ 10,51,2,18,4,31,13,5,23,64,29]
urut(L)
print(L)