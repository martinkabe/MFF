from typing import List

def hodnota_polynomu(arr: List, val: int) -> int:
    n = len(arr)
    sum = arr[n-1]
    pol = 0
    for i in range(n-1, 0, -1):
        sum += arr[pol] * val**i
        pol += 1
    return sum

def horner(a,x):
    h = 0
    for i in range(len(a)):
        h = h*x + a[i]
    return h

# result = hodnota_polynomu([5, 0, 10, 1], 2)
# print(result)
print(horner([5, 0, 10, 1], 2))