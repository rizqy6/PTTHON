from LatOOP4 import m1, m2, m3


def __str__(self):
    return self.nama

print('----------------------------------')

daftar = [m1,m2,m3]
for i in daftar:
    print(i.NIM)
print('----------------------------------')
for i in daftar:
    print(i)
print('----------------------------------')
print(daftar[2].ambilNama())