def is_palindrome(text: str) -> bool:
    if len(text) == 0 or len(text) == 1:
        return True
    
    if text[0] == text[len(text)-1]:
        return is_palindrome(text[1:-1])
    
    return False

print(is_palindrome('racecat'))