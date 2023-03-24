# string = "Ini adalah contoh sebuah string untuk mencari kata terpanjang"
string = input("Masukkan sebuah string: ")
# Memisahkan string menjadi kata individu
words = string.split()

#  variabel untuk menyimpan kata terpanjang
longest_word = ""

# Loop melalui setiap kata dalam string dan periksa apakah panjangnya lebih besar dari kata terpanjang saat ini
for word in words:
    if len(word) > len(longest_word):
        longest_word = word


print("Kata terpanjang dalam string adalah:", longest_word)
