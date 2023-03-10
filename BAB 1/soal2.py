def gambarlahPersegiEmpat(a,b):  #Nomor2
    for i in range(a):
        if(i==0):
            print(b*"@")
        elif(i==a-1):
            print(b*"@")
        else:
            print("@" + " " * (b-2) + "@")

print(gambarlahPersegiEmpat(5, 6))