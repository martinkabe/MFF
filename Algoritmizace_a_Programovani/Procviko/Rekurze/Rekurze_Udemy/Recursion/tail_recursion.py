def tail(n):
    if n == 0:
        return
    
    tail(n-1)
    print(f"n = {n}")

tail(5)