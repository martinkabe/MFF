import sys

a = -sys.maxsize-1
max_num = a

while a != -1:
    a = int(input())    
    if a > max_num:
        max_num = a

print(max_num)