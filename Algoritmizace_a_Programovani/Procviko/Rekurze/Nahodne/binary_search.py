from typing import List

def bin_search_recursive(arr: List, left: int, right: int, target: int) -> int:
    if (left > right):
        return -1
    
    mid = (left + right) // 2

    if target == arr[mid]:
        return mid
    
    if target > arr[mid]:
        return bin_search_recursive(arr, mid + 1, right, target)
    else:
        return bin_search_recursive(arr, left, mid - 1, target)


def bin_search_iterative(arr: List, target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [-1,0,2,5,10,15,20,100,200]
left = 0
right = len(arr) - 1

# print(bin_search_recursive(arr, left, right, 20))
print(bin_search_iterative(arr, 100))