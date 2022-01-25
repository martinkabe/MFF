def binsearch(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right-left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [-1,2,5,8,11,15,22,31,47,100]
result = binsearch(nums, -10)
print(result)