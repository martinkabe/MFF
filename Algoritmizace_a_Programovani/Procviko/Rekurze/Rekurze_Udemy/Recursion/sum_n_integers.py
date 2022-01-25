def sum_ints(n, sum=0):
    if n == 0:
        return n
    
    sum = n + sum_ints(n - 1)
    return sum

result = sum_ints(5)
print(result)