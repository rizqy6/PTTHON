def ucapkanSalam():
    print('Assalamualaikum!')

def sapa(nama):
    ucapkanSalam()
    print('Halo',nama)
    print('Selamat Belajar!')

def kuadratkan(b):
    h = b*b
    return h

ucapkanSalam()
sapa('rizqy')
b = kuadratkan(5)
print(b)