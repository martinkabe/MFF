# Python 3 Program to validate
# the above logic
 
# Function to check if the
# number is divisible by 17 or not
def isDivisible(n) :
 
    while(n // 100) :
 
        # Extracting the last digit
        d = n % 10
 
        # Truncating the number
        n //= 10
 
        # Subtracting the five times 
        # the last digit from the
        # remaining number
        n -= d * 5
 
    # Return n is divisible by 17
    return (n % 17 == 0)
 
# Driver Code
if __name__ == "__main__" :
 
    n = 19877658
     
    if isDivisible(n) :
        print("Yes")
    else :
        print("No")


def is_divisible_by_17(text: str) -> bool:
    reminder = (0 * 10 + int(text[0])) % 17
    for i in range(1, len(text)):
        reminder = (reminder * 10 + int(text[i])) % 17
    return reminder == 0

num = "34"
res = is_divisible_by_17(num)
print(res)
