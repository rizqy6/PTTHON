B = [[0 for j in range(3)] for i in range(3)]
print(B)

c = [x**2 for x in range (0,7)]
print(c)

class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


