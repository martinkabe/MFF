
def print_in_loop(n: int):
    if n >= 0:
        print(n)
    else:
        return
        
    print_in_loop(n-1)

print_in_loop(5)

