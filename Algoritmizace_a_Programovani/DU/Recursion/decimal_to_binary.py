
def dec_to_bin(dec_num, result):
    if dec_num == 0:
        return result
    
    result = f"{dec_num % 2}{result}"
    return dec_to_bin(dec_num // 2, result)


print(dec_to_bin(256, ""))
