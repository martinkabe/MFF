
def sum_of_digits_is_divisible_by_9(txt: str) -> bool:
    suma = 0
    for i in range(len(txt)):
        suma += int(txt[i])
    return suma % 9 == 0

def ends_with_even_number(txt: str) -> bool:
    return int(txt[len(txt)-1]) % 2 == 0

def is_divisible_by_18(txt: str) -> bool:
    return ends_with_even_number(txt) and sum_of_digits_is_divisible_by_9(txt)


result = is_divisible_by_18("128646")
print(result)