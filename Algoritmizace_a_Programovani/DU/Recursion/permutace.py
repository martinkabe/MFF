from typing import List

def perm(arr: List, end: List) -> List:
    if len(arr) == 0:
        print( end )
    
    results = []
    for i in range(len(arr)):
        perm(arr[:i] + arr[i+1:], end + arr[i:i+1])

# perm([1,2,3], [])

def perm2(arr: List, i: int) -> None:
    if i == (len(arr)-1):
        print(arr)
    
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        perm2(arr, i + 1)
        arr[i], arr[j] = arr[j], arr[i]

perm2([1,2,3], 0)