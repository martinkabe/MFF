def log_func(n: int, incr: int = 0):
    if n == 1:
        return incr
    n //= 2
    return log_func(n, incr + 1)

print(log_func(8))