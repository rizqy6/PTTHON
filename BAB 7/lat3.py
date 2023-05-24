#Nomor 3
import re
f = open('indonesia.txt', 'r', encoding='latin1')
c = []
teks = f.read()
f.close()
p = r'\s(di\s\w+)'
cocok = re.findall(p, teks)
c.append(cocok)
print(c)
print('------------------oleh L200210054---------------')
