import re

s = ' Alamatku sri@google.com serta joko@abc.com ok bro. atau don@email.com, rizid@gmail.com'
pola = r'[\w\.-]+@[\w\.-]+'
e = re.findall(pola,s)
print(e)