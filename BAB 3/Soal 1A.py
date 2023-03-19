a = [[1,2],[3,4],[5,6]]
b = [[7,8],[9,10]]
c = [[3,6],[5,2]]

#Nomor 1A
class matriks(object):
    def cetakmatriks(self, matriks):
        for i in matriks:
            print(i)
    def cekkonsisten(self, matriks):
        if len(matriks[0]) == len(matriks) :
            print ("matriks konsisten")
        else:
            print ("matriks tidak konsisten")

x = matriks()
x.cetakmatriks(a)
print(x.cekkonsisten(a))
y = matriks()
y.cetakmatriks(b)
print(y.cekkonsisten(b))

