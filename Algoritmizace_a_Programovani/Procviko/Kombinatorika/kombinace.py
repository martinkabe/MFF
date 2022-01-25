from typing import List

# kombinace bez opakovani
def komb(lst: List, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        for p in komb(remLst, n-1):
            l.append([m]+p)
             
    return l
 
# Driver code
if __name__=="__main__":
    arr ="abc"
    print(komb([x for x in arr], 2))