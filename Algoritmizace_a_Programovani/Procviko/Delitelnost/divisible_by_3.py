def check(num: int) -> bool:
    # Compute sum of digits 
    digitSum = 0
    while num != 0 : 
        digitSum += num % 10
        num //= 10
    # Check if sum of digits is divisible by 3. 
    return (digitSum % 3 == 0)

 # main function
if __name__=="__main__":
    num = 1332
    if(check(num)) : 
        print ("Yes")
    else : 
        print ("No")