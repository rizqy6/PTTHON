#Nomor 2
import re
f = open('indonesia.txt', 'r', encoding='latin1')
b = []
teks = f.read()
f.close()
p = r'\s(di\w+)'
cocok = re.findall(p, teks)
b.append(cocok)
print(b)

