def merge(arr1, arr2):
    n1 = len(arr1) - 1
    n2 = len(arr2) - 1
    i = j = k = 0
    arr_new = [None] * (len(arr1)+len(arr2))
    while i <= n1 and j <= n2:
        if arr1[i] < arr2[j]:
            arr_new[k] = arr1[i]
            i += 1
        else:
            arr_new[k] = arr2[j]
            j += 1
        k += 1
    
    while i <= n1:
        arr_new[k] = arr1[i]
        i, k = i+1, k+1
    while j <= n2:
        arr_new[k] = arr1[j]
        j, k = j+1, k+1
        
    return arr_new

a1 = [2,4,7,9]
a2 = [1,3,5,6]
res = merge(a1, a2)
print(res)