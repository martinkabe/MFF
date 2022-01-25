def binaryToDecimal(binary):
    ar = [int(i) for  i in binary]
    ar  = ar[::-1]
    res = []
    for i in range(len(ar)):
        res.append(ar[i]*(2**i))
    sum_res = sum(res)      
    print(f'Decimal Number of binary {binary} is : ', sum_res)

numbers = ["11","1001","10000","00010001","00010011","10101100","100000000","11111111","1111111111111111","10000000000000001","0000000100000001"]

for num in numbers:
    binaryToDecimal(num)