f = 2.5
g = 7
d = [f, g, 3.9, 8, 'apakabar']
print(d)
print(type(d))

d[0] = 55
print(d)

for i in d:
    print(i)

# slicing
a = 'wacana keilmuan dan keislaman'
b = [43,44,45,46,47,48,49,50]

print(a[0:6])
print(a[7:15])
print(a[::-1])
print(a[-7:-2])
print(a[-7:100])
print(len(a))
print(a[0:29])
print(a[0:100])
print(a[0:29:2])
print(a[0:200:2])

print(b[0:6])
print(b[7:15])
print(b[::-1])
print(b[-7:-2])
print(b[-7:100])
print(len(b))
print(b[0:29])
print(b[0:100])
print(b[0:29:2])
print(b[0:200:2])