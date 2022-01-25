# https://www.youtube.com/watch?v=IJDJ0kBx2LM

def recursion(val, i):
    if i > val:
        return
    
    print(i)
    return recursion(val, i + 1)

# recursion(10, 1)


def recursion2(n: int) -> None:
    if n > 0:
        recursion2( n - 1 )
        print( n )

recursion2(10)
