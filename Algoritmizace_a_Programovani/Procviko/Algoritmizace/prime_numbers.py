def is_prime_number(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# prime(3)

for i in range(2, 24):
    print(f"{i}: {is_prime_number(i)}")