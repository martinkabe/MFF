def findSum(str1, str2):
    # Before proceeding further,
    # make sure length of str2 is larger.
    if (len(str1) > len(str2)):
        t = str1
        str1 = str2
        str2 = t
 
    # Take an empty string for
    # storing result
    str = ""
 
    # Calculate length of both string
    n1 = len(str1)
    n2 = len(str2)
 
    # Reverse both of strings
    str1 = str1[::-1]
    str2 = str2[::-1]
 
    carry = 0
    for i in range(n1):
         
        # Do school mathematics, compute
        # sum of current digits and carry
        sum = ((ord(str1[i]) - 48) +
              ((ord(str2[i]) - 48) + carry))
        str += chr(sum % 10 + 48)
 
        # Calculate carry for next step
        carry = int(sum / 10)
 
    # Add remaining digits of larger number
    for i in range(n1, n2):
        sum = ((ord(str2[i]) - 48) + carry)
        str += chr(sum % 10 + 48)
        carry = (int)(sum / 10)
 
    # Add remaining carry
    if (carry):
        str += chr(carry + 48)
 
    # reverse resultant string
    str = str[::-1]
 
    return str


def div_number(txt: str) -> bool:
    if txt == "19":
        return True
    if len(txt) >= 2:
        txt = findSum(txt[:len(txt)-1], str(2*int(txt[len(txt)-1])))
        return div_number(txt)
    
    return False


result = div_number("475")
print(result)