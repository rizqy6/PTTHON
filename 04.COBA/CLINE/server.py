import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind (("localhost",50004))
s.listen(5)
print("Server Siap")
perintah = ""
x = 0
while perintah.lower() != "keluar":
    komm, addr = s.accept()
    while perintah.lower() != "keluar":
        item = komm.recv(1024).lower().split("*").decode()
        perintah = item[0]
        if perintah == "keluar":
            komm.send("done")
            s.close()
            break
        print("Pesan : ",perintah)
        if len(item) == 2:
            if perintah == "sisi":o
                x = int(item[1])
                komm.send("sisi disimpan")
            else:
                komm.send("Perintah Tidak Diketahui")
        elif perintah == "hitung":
            L = float(1/3*x*x)
            response = "Luas piramida dengan sisi () adalah ()".format(x,L)
            komm.send(response)
        else:
            komm.send("Pesan tidak Diketahui")
