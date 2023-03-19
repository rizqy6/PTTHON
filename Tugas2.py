# l200210015
# Faza Rizqy Septin R

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5
        
    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance(p2))  # output: 5.0
print(p1)  # output: (2, 3)