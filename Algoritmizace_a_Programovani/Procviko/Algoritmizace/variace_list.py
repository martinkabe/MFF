def variace(n, k):
    def var(i):
        for j in range(1,n+1):
            v[i] = j
            if i < k-1: # nejsme hotovi
                var(i+1)
            else: # hotová variace
                vysledek.append(list(v))
    v = [0] * k # pole pro generování
    vysledek = [] # výstup do seznamu
    var(0)
    return vysledek

result = variace(3, 5)
print(result)