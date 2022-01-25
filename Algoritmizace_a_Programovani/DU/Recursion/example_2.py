# n = 1 + 2 + 3 + ... + n

def sum_nums_math(n):
    return int(n * (n + 1) / 2)

def sum_nums(n, result):
    if n < 1:
        print(result)
        return
    sum_nums(n-1, n + result)

def sum_nums_2(n):
    if n == 0:
        return 0
    else:
        return n + sum_nums_2(n-1)


num = 10
sum_nums(num, 0)
print(sum_nums_math(num))
print(sum_nums_2(num))