
# A list comprehension
print("max in list:", max([num * 2 - 3 for num in range(7)]))
# A generator expression
print("max in gen:", max(num*2-3 for num in range(7)))

# A generator function
def genfunc(limit):
    num = 0
    while num < limit:
        yield num
        num += 1

print(genfunc(7))
# iteration using generator function
print("Iteration over generator")
for num in genfunc(7):
    print(num, end=" ")

# Pass to functions expecting a sequence
print('\n')
print("max in gen func:", max(genfunc(7)))

# use return to end generator
def genfunc2(endfunc):
    num = 0
    while True:
        if endfunc(num):
            print(f"\nDone, because num = {num}")
            return
        yield num
        num += 1

def endfunc(num):
    if num == 7:
        return True
    return False

for num in genfunc2(endfunc):
    print(num, end=" ")
