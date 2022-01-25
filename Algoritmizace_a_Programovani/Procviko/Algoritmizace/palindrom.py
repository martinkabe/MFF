def is_palindrom(text: str) -> bool:
    if len(text) <= 1:
        return True
    
    if text[0] == text[len(text)-1]:
        return is_palindrom(text[1:-1])
    
    return False

res = is_palindrom("raaccaar")
print(res)