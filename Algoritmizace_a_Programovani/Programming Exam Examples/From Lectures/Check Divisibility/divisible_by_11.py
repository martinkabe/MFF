# Python 3 code program to find if a number
# is divisible by 11 or not
 
 
# Function to find that number divisible by
#  11 or not
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
 
# Driver code
st = "76945"
if(check(st)) :
    print( "Yes")
else :
    print("No ")