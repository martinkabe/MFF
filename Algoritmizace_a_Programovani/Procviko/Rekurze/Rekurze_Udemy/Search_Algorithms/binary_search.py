from typing import List

def binarySearch_recursion(arr: List[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    
    mid = (right + left) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        print("Checking items on the left ...")
        return binarySearch_recursion(arr, target, left, mid - 1)
    else:
        print("Checking items on the right ...")
        return binarySearch_recursion(arr, target, mid + 1, right)


arr = [-4,-1,0,1,2,9,14,25,45,49,51,60]
res = binarySearch_recursion(arr, 14, 0, len(arr)-1)
print(res)