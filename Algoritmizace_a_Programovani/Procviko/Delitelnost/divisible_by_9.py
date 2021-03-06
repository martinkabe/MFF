def check(st: str) -> bool: 
    # Compute sum of digits 
    n = len(st) 
    digitSum = 0
      
    for i in range(0,n) : 
        digitSum = digitSum + (int)(st[i]) 
  
    # Check if sum of digits is divisible by 9.
    return (digitSum % 9 == 0) 
  
# Driver code
if __name__ == '__main__':
    st = "99333"    
    if(check(st)) : 
        print("Yes") 
    else :  
        print("No") 