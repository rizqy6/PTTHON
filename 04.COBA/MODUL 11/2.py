from tkinter import *
 
window = Tk()
window.title("Kalkulator GUI Dengan Python")
window.geometry('300x300')
 
lbl = Label(window, text="Angka 1 ",anchor="e",width=20)
lbl.place(x = -60, y = 20)
 
nilai1 = Entry(window,width=15)
nilai1.place(x =120, y = 20)
 
 
lbl2 = Label(window, text="Angka 2 ",anchor="e",width=20)
lbl2.place(x = -60, y = 60)
 
nilai2 = Entry(window,width=15)
nilai2.place(x =120, y= 60)
 
lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.place(x = -60, y = 150)
 
hasil = Label(window, text="0",anchor="w",width=10)
hasil.place(x = 100, y = 150)
 
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))

btn = Button(window, text="+", command=tambah,width = 3)
btn.place(x = 180, y = 100)
 
btn = Button(window, text="-", command=kurang,width = 3)
btn.place(x = 140, y = 100)
btn = Button(window, text="x", command=kali,width = 3)
btn.place(x =100, y = 100)
btn = Button(window, text=":", command=bagi,width = 3)
btn.place(x = 60, y = 100)

window.mainloop()

