# how heap works: https://www.youtube.com/watch?v=2DmK_H7IdTo&t=55s
from typing import List

def heapsort(A: List[int]):
    pass

def swap(A: List[int], i: int, j: int):
    A[i], A[j] = A[j], A[i]


def siftDown(A: List[int], i: int, upper: int):
    while True:
        l, r = i*2+1, i*2+2
        


if __name__=="__main__":
    arr = [2, 8, 5, 3, 9, 1]
    heapsort(arr)
    print(*arr, end=" ")