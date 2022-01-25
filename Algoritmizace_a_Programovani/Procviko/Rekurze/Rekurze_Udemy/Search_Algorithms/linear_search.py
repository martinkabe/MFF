from typing import List
from collections import deque

def linearSearch_iterative(arr: List[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linearSearch_recursive_1(arr: deque[int], target: int, indx: int = 0) -> int:
    if len(arr) == 0:
        return -1
    
    val = arr.popleft()
    if val == target:
        return indx
    else:
        return linearSearch_recursive_1(arr, target, indx+1)

def linearSearch_recursive_2(arr: List[int], target: int, indx: int = 0) -> int:
    if indx >= len(arr):
        return -1
    
    if arr[indx] == target:
        return indx
    else:
        return linearSearch_recursive_2(arr, target, indx + 1)


arr = [1, 5, -3, 10, 55, 100]
# q = deque(arr)
print(linearSearch_recursive_2(arr, 100))