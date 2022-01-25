# Python program to find if a number is
# divisible by 5 or not
 
# Function to find that number divisible
# by 5 or not. The function assumes that
# string length is at least one.
def isDivisibleBy5(st) :
    n = len(st)
    return ( (st[n-1] == '0') or
           (st[n-1] == '5'))
  
# Driver code
st = "76955"
if isDivisibleBy5(st) :
    print "Yes"
else :
    print "No "