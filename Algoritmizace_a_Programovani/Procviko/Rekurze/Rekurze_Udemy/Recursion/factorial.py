def fact(n, result=1):
    if n == 0:
        return result
    
    return fact(n-1, n*result)

def factorial_head(n):
    if n == 1:
        return 1
    
    result1 = factorial_head(n-1)
    result2 = n * result1
    return result2

def factorial_tail(n, accumulator=1):
    if n == 1:
        return accumulator
    
    return factorial_tail(n-1, n * accumulator)


res = factorial_tail(4)
print(res)