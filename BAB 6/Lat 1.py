def gabungkanDuaListUrut(A, B):
    la = len(A); lb = len(B)
    C = list() 
    i = 0 ; j= 0
    while i < la and j < lb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < la: 
        C.append(A[i]) 
        i += 1

    while j < lb: 
        C.append(B[j]) 
        j += 1 

    return C
    
P =[2,8,15,23,37]
Q = [4,6,15,20]
R = gabungkanDuaListUrut(P, Q)
print(R)