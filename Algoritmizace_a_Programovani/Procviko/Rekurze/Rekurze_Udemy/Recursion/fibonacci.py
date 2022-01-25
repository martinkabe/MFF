from typing import List

def fib_memo(n: int, dict: dict={}) -> int:
    if n <= 1:
        return n
    if n in dict:
        return dict[n]
    
    fib_num = fib_memo(n-1) + fib_memo(n-2)
    dict[n] = fib_num
    return dict[n]

def fib_head(n):
    if n <= 1:
        return n
    
    return fib_head(n-1) + fib_head(n-2)

def fib_tail(n: int, a: int = 0, b:int = 1) -> int:
    if n == 0: return a
    if n == 1: return b

    return fib_tail(n-1, b, a+b)


def print_fibs(fib: List[int]):
    for f in fib:
        print(f, end=" ")

def fib_iter(n: int):
    fib = [0,1]
    prev, curr = fib[0], fib[1]
     
    for _ in range(n-1):
        next = prev + curr
        fib.append(next)
        prev, curr = fib[len(fib)-2], fib[len(fib)-1]
    
    return fib


result = fib_iter(10)
print_fibs(result)
# print(fib_tail(10))