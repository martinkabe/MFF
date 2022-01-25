
def is_power(number):
    isExp = False
    result = temp = 0
    while temp < number:
        temp = 2**result
        result += 1

    if temp == number:
        isExp = True

    if (isExp):
        print(f"{number} is a power of two: {isExp} [2^{result}]")
    else:
        print(f"{number} is not a power of 2")

numbers = [32,2000,3000,512,544,2048,533,254,96,128,4096]

for num in numbers:
    is_power(num)
