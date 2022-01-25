from typing import List

def selectionsort(arr: List) -> List:
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

arr = [-10,15,100,4,2,3,6,9,7]
arr_new = selectionsort(arr)
print(arr_new)