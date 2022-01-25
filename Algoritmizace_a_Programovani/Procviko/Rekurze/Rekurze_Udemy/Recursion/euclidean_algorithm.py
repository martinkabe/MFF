# greates common divisor
def GCD_recursive(x, y):
    if y == 0:
        return x
    return GCD_recursive(y, x % y)

def GCD_iterative(x, y):
    while x % y != 0:
        x, y = y, x % y
    return y

print(GCD_iterative(45, 10))
print(GCD_recursive(45, 10))