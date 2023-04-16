# L200210015 Faza Rizqy Septin R

def first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        elif arr[i] > x:
            return -1 
    return -1 


arr1 = [1, 2, 3, 3, 4, 4, 4, 5]
x1 = 4
print(first_occurrence(arr1, x1)) 

arr2 = [1, 1, 2, 3, 5, 8]
x2 = 1
print(first_occurrence(arr2, x2))

def find_peak(arr):
    n = len(arr)
    left, right = 0, n-1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    
    return left


arr1 = [0, 2, 4, 2, 0]
print(find_peak(arr1)) 

arr2 = [0, 5, 10, 20, 10, 2, 0]
print(find_peak(arr2)) 
