def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

A = [10, 51,2,18,4,31,5,23,64,29]
print(cariLurus(A, 31))
print(cariLurus(A, 8))

