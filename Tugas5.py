def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid-1] != target:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def peak_index_mountain_array(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    
# Program untuk mencari kemunculan pertama suatu elemen
arr1 = [1, 2, 3, 3, 4, 4, 4, 5]
target1 = 4
print(first_occurrence(arr1, target1))  # Output: 4

arr2 = [1, 1, 2, 3, 5, 8]
target2 = 1
print(first_occurrence(arr2, target2))  # Output: 0

# Program untuk mencari titik puncak mountain array
arr3 = [0, 2, 4, 2, 0]
print(peak_index_mountain_array(arr3))  # Output: 2

arr4 = [0, 5, 10, 20, 10, 2, 0]
print(peak_index_mountain_array(arr4))  # Output: 3
