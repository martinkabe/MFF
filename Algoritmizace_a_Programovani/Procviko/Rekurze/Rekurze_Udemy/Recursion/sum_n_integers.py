def sum_ints(n, sum=0):
    if n == 0:
        return sum
    
    return sum_ints(n-1, sum + n)
    
result = sum_ints(10)
print(result)