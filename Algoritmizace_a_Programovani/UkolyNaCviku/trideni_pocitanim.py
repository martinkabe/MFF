def trideni_pocitanim(a, k):
    c = [0] * (k+1)
    for x in a:
        c[x] += 1
    return(c)

a = [5,6,5,5,3,2,8,7,8,9]
k = 9
print(trideni_pocitanim(a, k))
