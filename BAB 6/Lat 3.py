def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 ) # memanggil quickSortBantu di

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir) # Atur elemen dan dapatkan titikBelah.
        quickSortBantu(A, awal, titikBelah - 1) # Ini rekursi untuk belah sisi kiri
        quickSortBantu(A, titikBelah + 1, akhir) # dan belah sisi kanan.

def partisi(A, awal, akhir):
    nilaiPivot = A[awal] # Di sini nilaiPivot kita ambil dari elemen yang paling kiri.

    penandaKiri = awal + 1 # Posisi awal penandaKiri. Lihat Gambar 6.3.
    penandaKanan = akhir # Posisi awal penandaKanan.

    selesai = False
    while not selesai: # loop di bawah adalah untuk mengatur ulang posisi semua elemen

        while penandaKiri <= penandaKanan and \
                A[penandaKiri] <= nilaiPivot: # sampai ketemu suatu nilai yang
            penandaKiri = penandaKiri + 1 # lebih besar dari nilaiPivot

        while A[penandaKanan] >= nilaiPivot and \
                penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1 

        if penandaKanan < penandaKiri: # Kalau dua penanda sudah bersilangan,
            selesai = True # selesai & lanjut ke penempatan pivot
        else:
            temp = A[penandaKiri] # Tapi kalau belum bersilangan,
            A[penandaKiri] = A[penandaKanan] # tukarlah isi yang ditunjuk oleh
            A[penandaKanan] = temp # penandaKiri dan penandaKanan

    temp = A[awal] # Kalau acara tukar menukar posisi sudah selesai,
    A[awal] = A[penandaKanan] # kita lalu menempatkan pivot pada posisi yang tepat,
    A[penandaKanan] = temp # yakni posisi penandaKanan. Lihat Gambar 6.3 dan 6.4.
    # Posisi penandaKanan adalah juga titikBelah.
    return penandaKanan # Fungsi ini mengembalikan titikBelah ke pemanggil

# alist = [54,26,93,17,77,31,44,55,20]
# partisi(54, 77, 20)
# print(alist)