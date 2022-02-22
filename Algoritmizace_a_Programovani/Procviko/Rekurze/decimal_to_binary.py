def dec_to_bin(dec: int, result: str) -> str:
    if dec == 0:
        return result
    
    result = str(dec % 2) + result
    return dec_to_bin(dec // 2, result)
    

print(dec_to_bin(233, ""))