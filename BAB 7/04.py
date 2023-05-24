import re
cocok = re.findall(r'te+', 'ghdteeeh')
cocok = re.findall(r'e+', 'teeheeee') 
polanya = r'\d\s*\d\s*\d'

cocok = re.findall(polanya, 'xx1 2    3xx')
cocok = re.findall(polanya, 'xx12 3xx')
cocok = re.findall(polanya, 'xx123xx')

cocok = re.findall(r'k\w+', 'mejakursi')
cocok = re.findall(r'k[\w\s]+', 'mejakursi tamu saya')

print(cocok)
s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'\w+@\w+',s)
print(cocok[0])