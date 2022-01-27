def string_rev(text: str) -> str:
    if text == "":
        return ""
    
    rev_str = string_rev(text[1:]) + text[0]
    return rev_str
    
rev_string = string_rev("hello")
print(rev_string)