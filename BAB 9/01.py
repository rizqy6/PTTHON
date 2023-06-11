class _SimpulPohonBiner(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

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

# Preoder Traversal
def preoderTrav(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preoderTrav(subpohon.kiri)
        preoderTrav(subpohon.kanan)
preoderTrav(B)


print('==================================================================')
# Inorder Traversal
def inoderTrav (subpohon):
    if subpohon is not None:
        inoderTrav(subpohon.kiri)
        print(subpohon.data)
        inoderTrav(subpohon.kanan)

inoderTrav(G)
print('==================================================================')
# Postoder Traversal
def postoderTrav(subpohon):
    if subpohon is not None:
        postoderTrav(subpohon.kiri)
        postoderTrav(subpohon.kanan)
        print(subpohon.data)
postoderTrav(C)
