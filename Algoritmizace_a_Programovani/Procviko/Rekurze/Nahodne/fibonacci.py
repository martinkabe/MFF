cache = {}

def fib_recursive_memoize(n: int) -> int:
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    else:
        cache[n] = fib_recursive_memoize(n - 1) + fib_recursive_memoize(n - 2)

    return cache[n]

def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iter(n: int) -> int:
    prev_1 = 1
    prev_2 = 0
    curr = 0
    for i in range(1, n):
        curr = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = curr
    return curr


print(fib_iter(5))
print(fib_recursive_memoize(10))
# print(fib_recursive(40))