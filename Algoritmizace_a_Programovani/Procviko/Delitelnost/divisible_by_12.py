# Python Program to check if
# number is divisible by 12
 
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
     
 
num = "12244824607284961224" 
if(isDvisibleBy12(num)):
       print("Yes")
else:
       print("No")