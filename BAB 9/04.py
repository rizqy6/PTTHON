class _SimpulPohonBiner(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def cetakLevel(akar, count=0):
    if akar is not None:
        print(akar.data+ ', level '+ str(count)) 
        (cetakLevel(akar.kiri, count+1),cetakLevel(akar.kanan, count+1))
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

datalist = [A.data, B.data, C.data, D.data, E.data, F.data, G.data, H.data]
level = []

def traverse(root):
    lvlist =[]
    current_level = [root]
    lv = 0
    while current_level:
        next_level = list()
        for n in current_level:
            if n.kiri:
                next_level.append(n.kiri)
                level.append(lv+1)
            if n.kanan:
                next_level.append(n.kanan)
                level.append(lv+1)
            current_level = next_level
        lv+=1
        lvlist.append(lv)
    return lvlist

def cetak(root):
    traverse(A)
    print(root.data,', Level 0')
    for i in range(len(level)):
        print(datalist[i+1],', Level', level[i])

cetak(A)