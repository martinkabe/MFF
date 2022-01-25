# Python 3 program to find
# if a number is divisible
# by 8 or not
 
 
# Function to find that
# number divisible by 8
# or not
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
 
 
# Driver code
st = "76952"
 
if(check(st)) :
    print("Yes")
else :
    print("No ")