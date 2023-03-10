from tkinter import *
import tkinter.font



root = Tk()
root.geometry("700x700")

changefont = tkinter.font.Font(size=20)
judul = Label(root, text  = "DATA DIRI",font = changefont)
judul.place(x = 80, y=5)

labelfr= LabelFrame(root, text  = "result",padx = 20, pady = 20)
labelfr.place(x = 60, y = 380)

nama  = Label(root, text  = "Nama Lengkap")
nim   = Label(root, text  = "Nomer Induk Mahasiswa")
buku  = Label(root, text  = "Buku Favorit")
idola = Label(root, text  = "Idola Sahabat Nabi Muhammad.saw")
motto = Label(root, text  = "Motto Hidup")

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)


nama.place(x = 20,y = 50)
nim.place(x = 20, y = 100)
buku.place(x = 20, y= 150)
idola.place(x = 20, y= 200)
motto.place(x = 20, y= 250)

e1.place(x = 20, y= 70)
e2.place(x = 20, y= 120)
e3.place(x = 20, y= 170)
e4.place(x = 20, y= 220)
e5.place(x = 20, y= 270)


r = StringVar()
r.set("male")
rb = Radiobutton(root,text = "male",variable=r,value ="male").place(x = 20, y=310)
rb2 = Radiobutton(root,text = "female",variable=r,value ="female").place(x = 80, y=310)

def cetak():
    class orang:
        def __init__(self, nama, nim,buku, idola, motto,gender):
            self.nama  = nama
            self.nim   = nim
            self.buku  = buku
            self.idola = idola
            self.motto = motto
            self.gender  = gender
        def hasil(self):
            lbl = Label(labelfr, text ="nama ="+self.nama+"\nnim ="+self.nim+"\nbuku="+self.buku+
            "\nidola ="+self.idola+"\nmotto ="+self.motto).grid()
    ditampilkan = orang(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),r.get())
    ditampilkan.hasil()

def tutup():
     root.destroy()

btn2 = Button(root, text="STOP", command=tutup).place(x =100,y=390)

        



btn = Button(root,text = "submit", command=cetak).place(x = 100,y = 350)
#btn2= Button(root,text = "Stop",command=root.quit).place(x =100,y=390)

root.mainloop()
