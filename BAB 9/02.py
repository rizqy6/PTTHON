class _SimpulPohonBiner(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuran(akar, count=0):
    if akar is None:
        return count
    return ukuran(akar.kiri, ukuran(akar.kanan, count+1))
A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enkerang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera Timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

print('Ukuran pohon biner adalah',ukuran(A))