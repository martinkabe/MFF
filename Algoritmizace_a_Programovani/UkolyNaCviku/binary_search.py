def binary_search(arr, target):
    last = len(arr) - 1
    first = 0

    while first <= last:
        midpoint = first + (last - first) // 2
        if arr[midpoint] == target:
            return True
        if (arr[midpoint] > target):
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr, 100))