def bin2int(bin):
    n = len(bin)
    exp = n - 1
    sum = 0
    for i in range(n):
        sum += int(bin[i])*(2**exp)
        exp -= 1
    return sum

def int2bin(val: int, result: str) -> str:
    if val == 0:
        return result
    
    result = str(val % 2) + result
    return int2bin(val // 2, result)


print(int2bin(23, ""))
# print(bin2int("10111"))
