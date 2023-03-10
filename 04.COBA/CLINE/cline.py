import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.connect((hostname,50004))
print ("Menghitung luas piramida")
while pesan.lower() != "quit":
    pesan = input("Command : ")
    s.send(pesan.encode())
    if pesan.lower() == "quit":
        s.close()
        break
    elif pesan.lower() != "quit":
        response = s.recv(1024).decode()
        print ("Response : ",response)
s.close()
