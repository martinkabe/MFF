def bubble_sort(arr):
    n = len(arr)
    for j in range(0, n-1):
        for i in range(j+1, n):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

arr = [2,5,8,-10,100,1]
print(*bubble_sort(arr))