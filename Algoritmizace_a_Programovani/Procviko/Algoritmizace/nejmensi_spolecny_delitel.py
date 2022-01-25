def euklid0(x,y):
    while x != y:
        if x > y:
            x -= y # x = x-y
        else:
            y -= x # y = y-x
    return x

def nsd_rekurze(x, y):
    if x-y == 0:
        return x
    
    if x > y:
        return nsd_rekurze(x-y, y)
    
    if x < y:
         return nsd_rekurze(x, y-x)

print(nsd_rekurze(16, 18))
# print(euklid0(30, 24))