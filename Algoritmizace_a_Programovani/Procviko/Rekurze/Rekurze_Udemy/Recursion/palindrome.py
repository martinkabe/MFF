def is_palindrome(text):
    if len(text) < 2:
        return True
    
    if text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])

print(is_palindrome("a"))
print(is_palindrome("martinitram"))
print(is_palindrome("america"))