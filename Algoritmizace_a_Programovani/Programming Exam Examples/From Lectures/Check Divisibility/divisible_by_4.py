# Python 3 program to find
# if a number is divisible
# by 4 or not
 
# Function to find that
# number divisible by
# 4 or not
 
 
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
 
 
# Driver code
st = "76952"
 
# Function call
if(check(st)):
    print("Yes")
else:
    print("No ")