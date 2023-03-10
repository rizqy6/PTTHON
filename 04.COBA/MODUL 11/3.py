from tkinter import *
from tkinter import constants
import tkinter.font
 
window = Tk()
window.title =("Menghitung luas")
window.geometry('900x600')

changefont = tkinter.font.Font(size=20)
judul  = Label(window,text="BANGUN GEOMETRI", font=changefont)
judul.place(x= 80, y = 5)

ket = Label(window,text="Piramida adalah bangun ruang yang beralas persegi dan mengerucut keatas, contohnya seperti piramida di mesir")
ket.place(x=80,  y=50)

lbl = Label(window ,text="Parameter Sisi \t: ",anchor='e',width=20)
lbl.place(x=15, y=90)

nilai1= Entry(window,width=10)
nilai1.place(x=180, y=90)

lbl2 = Label(window ,text="Parameter Tinggi \t: ",anchor='e',width=20)
lbl2.place(x=15, y =140)

nilai2= Entry(window,width=10)
nilai2.place(x=180, y = 140)

constants = float('0.3')


lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.place(x=15, y=180)
 
hasil = Label(window, text="0",anchor="w",width=10)
hasil.place(x= 180, y =180)

def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai1.get())*int(nilai2.get())*float(constants)))

btn = Button(window, text="Hitung Luas", command=kali)
btn.place(x= 25, y=175)
 
window.mainloop()
