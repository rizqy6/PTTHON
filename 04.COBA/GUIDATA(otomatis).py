from tkinter import *
import tkinter.font



root = Tk()
root.geometry("600x600")

changefont = tkinter.font.Font(size=20)
judul = Label(root, text  = "DATA DIRI",font = changefont)
judul.place(x = 20, y=5)


nama  = Label(root, text  = "Nama Lengkap \t\t\t:")
nim   = Label(root, text  = "Nomer Induk Mahasiswa \t\t:")
buku  = Label(root, text  = "Buku Favorit \t\t\t:")
idola = Label(root, text  = "Idola Sahabat Nabi Muhammad.saw \t:")
motto = Label(root, text  = "Motto Hidup \t\t\t:")

isinama = Label(root, text  = "Faza Rizqy Septin Rezsuwandi")
isinim  = Label (root, text   = "L200210015")
isibuku = Label(root, text  = "Mencari Jati Diri")
isiidola= Label(root, text  = "Umar bin Khatab")
isimotto= Label(root, text  = "Hiduplah seperti yang ditakdirkan")

nama.place(x = 20,y = 50)
nim.place(x = 20, y = 100)
buku.place(x = 20, y= 150)
idola.place(x = 20, y= 200)
motto.place(x = 20, y= 250)

isinama.place (x = 300, y = 50)
isinim.place  (x = 300, y = 100)
isibuku.place (x = 300, y = 150)
isiidola.place(x = 300, y = 200)
isimotto.place(x = 300, y = 250)



def tutup():
     root.destroy()

btn2 = Button(root, text="TUTUP", command=tutup).place(x =250,y=320)

        




root.mainloop()
