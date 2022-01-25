print('Program')

# divisible by 3
def check(num: int) -> bool:
    # Compute sum of digits 
    digitSum = 0
    while num != 0 : 
        digitSum += num % 10
        num //= 10
    # Check if sum of digits is divisible by 3. 
    return (digitSum % 3 == 0)

# divisible by 4
def check(st):
    n = len(st)
 
    # Empty string
    if (n == 0):
        return False
 
    # If there is single
    # digit
    if (n == 1):
        return ((st[0] - '0') % 4 == 0)
 
    # If number formed by
    # last two digits is
    # divisible by 4.
    last = (int)(st[n - 1])
    second_last = (int)(st[n - 2])
 
    return ((second_last * 10 + last) % 4 == 0)

# divisible by 5
def isDivisibleBy5(st) :
    n = len(st)
    return ( (st[n-1] == '0') or
           (st[n-1] == '5'))

# divisible by 6
def check(st) :
    n = len(st)
    # Return false if number
    # is not divisible by 2.
    if (((int)(st[n-1])%2) != 0) :
        return False
  
    # If we reach here, number
    # is divisible by 2. Now
    # check for 3.
  
    # Compute sum of digits
    digitSum = 0
    for i in range(0, n) :
        digitSum = digitSum + (int)(st[i])
  
    # Check if sum of digits
    # is divisible by 3
    return (digitSum % 3 == 0)


# divisible by 7
def isdivisible7(num):
    n = len(num)
    if (n == 0 and num[0] == '\n'):
        return 1
 
    # Append required 0s at the beginning.
    if (n % 3 == 1) :
        num = "00" + str(num)
        n += 2
     
    elif (n % 3 == 2) :
        num = "0" + str(num)
        n += 1
 
    # add digits in group of three in gSum
    GSum = 0
    p = 1
    i = n-1
    while i>=0 :
 
        # group saves 3-digit group
        group = 0
        group += ord(num[i]) - ord('0')
        i -= 1
        group += (ord(num[i]) - ord('0')) * 10
        i -= 1
        group += (ord(num[i]) - ord('0')) * 100
 
        GSum = GSum + group * p
 
        # generate alternate series of
        # plus and minus
        p *= (-1)
        i -= 1
 
    return (GSum % 7 == 0)

# divisible by 8
def check(st) :
    n = len(st)
     
    # Empty string
    if (n == 0) :
        return False
 
    # If there is single digit
    if (n == 1) :
        return ((int)(st[0]) % 8 == 0)
 
    # If there is double digit
    if (n == 2) :
        return ((int)(st[n - 2]) * 10 +
          ((int)(str[n - 1]) % 8 == 0))
 
    # If number formed by last
    # three digits is divisible
    # by 8.
    last = (int)(st[n - 1])
    second_last = (int)(st[n - 2])
    third_last = (int)(st[n - 3])
 
    return ((third_last*100 + second_last*10 +
                               last) % 8 == 0)

# divisible by 9
def check(st: str) -> bool: 
    # Compute sum of digits 
    n = len(st) 
    digitSum = 0
      
    for i in range(0,n) : 
        digitSum = digitSum + (int)(st[i]) 
  
    # Check if sum of digits is divisible by 9.
    return (digitSum % 9 == 0)


# divisible by 11
def check(st) :
    n = len(st)
 
    # Compute sum of even and odd digit
    # sums
    oddDigSum = 0
    evenDigSum = 0
    for i in range(0,n) :
        # When i is even, position of digit is odd
        if (i % 2 == 0) :
            oddDigSum = oddDigSum + ((int)(st[i]))
        else:
            evenDigSum = evenDigSum + ((int)(st[i]))
     
    # Check its difference is divisible by 11 or not
    return ((oddDigSum - evenDigSum) % 11 == 0)


# divisible by 12
def isDvisibleBy12( num):
 
    # if number greater then 3
    if (len(num) >= 3):
  
        # find last digit
        d1 = int(num[len(num) - 1])
  
        # no is odd
        if (d1 % 2 != 0):
            return False
  
        # find second last digit
        d2 = int(num[len(num) - 2])
  
        # find sum of all digits
        sum = 0
        for  i in range(0, len(num) ):
            sum += int(num[i])          
          
        return (sum % 3 == 0 and
               (d2 * 10 + d1) % 4 == 0)
    else :
          
        # f number is less then
        # r equal to 100
        number = int(num)
        return (number % 12 == 0)

# divisible by 13
def checkDivisibility( num):
    length = len(num)
    if (length == 1 and num[0] == '0'):
        return True
 
    # Append required 0s at the beginning.
    if (length % 3 == 1):
         
        # Same as strcat(num, "00");
        # in c.
        num = str(num) + "00"
        length += 2
     
    elif (length % 3 == 2):
         
        # Same as strcat(num, "0");
        # in c.
        num = str(num) + "0"
        length += 1
 
    # Alternatively add/subtract digits 
    # in group of three to result.
    sum = 0
    p = 1
    for i in range(length - 1, -1 , -1) :
         
        # Store group of three
        # numbers in group variable.
        group = 0
        group += ord(num[i]) - ord('0')
        i -= 1
        group += (ord(num[i]) - ord('0')) * 10
        i -= 1
        group += (ord(num[i]) - ord('0')) * 100
 
        sum = sum + group * p
 
        # Generate alternate series
        # of plus and minus
        p *= (-1)
    sum = abs(sum)
    return (sum % 13 == 0)


# divisible by 15
def accumulate(s):
    acc = 0
    for i in range(len(s)):
        acc += ord(s[i]) - 48
    return acc
 
def isDivisible(s):
    # length of string
    n = len(s)
 
    # check divisibility by 5
    if (s[n - 1] != '5' and s[n - 1] != '0'):
        return False
 
    # Sum of digits
    sum = accumulate(s)
     
    # if divisible by 3
    return (sum % 3 == 0)


# divisible by 16
def check(st) :
    n = len(st)
     
    # Empty string
    if (n == 0 and n == 1) :
        return False
  
    # If there is double digit
    if (n == 2) :
        return ((int)(st[n-2])*10 +
                ((int)(st[n-1])%16 == 0))
  
    # If there is triple digit
    if(n == 3) :
        return ( ((int)(st[n-3])*100 +
                   (int)(st[n-2])*10 +
                   (int)(st[n-1]))%16 == 0)


# divisible by 17
def is_divisible_by_17(text: str) -> bool:
    reminder = (0 * 10 + int(text[0])) % 17
    for i in range(1, len(text)):
        reminder = (reminder * 10 + int(text[i])) % 17
    return reminder == 0


# divisible by 18
def sum_of_digits_is_divisible_by_9(txt: str) -> bool:
    suma = 0
    for i in range(len(txt)):
        suma += int(txt[i])
    return suma % 9 == 0

def ends_with_even_number(txt: str) -> bool:
    return int(txt[len(txt)-1]) % 2 == 0

def is_divisible_by_18(txt: str) -> bool:
    return ends_with_even_number(txt) and sum_of_digits_is_divisible_by_9(txt)


# divisible by 19
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