
def is_palindrome_iter(inpt):
    i = 0
    j = len(inpt) - 1

    while i < j:
        if inpt[i] == inpt[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def is_palindrome(inpt):
    if len(inpt) <= 0:
        return True
    
    if inpt[0] == inpt[-1]:
        return is_palindrome(inpt[1:-1])

    return False


print(is_palindrome("repapera"))
print(is_palindrome_iter("repaper"))