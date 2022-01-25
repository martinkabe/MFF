predchozi = 0, 0
def pohyb(x, y, kam):
    global predchozi
    if kam == ">":
        x += 1
        predchozi = 1, 0
        return(x, y)
    elif kam == "<":
        x -= 1
        predchozi = -1, 0
        return(x, y)
    elif kam == "v":
        y += 1
        predchozi = 0, 1
        return(x, y)
    elif kam == "^":
        y -= 1
        predchozi = 0, -1
        return(x, y)
    elif kam == "-":
        x += predchozi[0]
        y += predchozi[1]
        return(x, y)


sirka = int(input())
vyska = int(input())
sx = int(input())
sy = int(input())
parkoviste = [False]*vyska
for i in range(vyska):
    parkoviste[i] = [False] * sirka
parkoviste[sy][sx] = True
smer = input()
step = 0
vysledek = "OK"

while smer != "0":
        sx, sy = pohyb(sx, sy, smer)
        if sy >= vyska or sx >= sirka or sy < 0 or sx < 0:
            vysledek = "KO"
            step +=1
            while smer != "0":
                smer = input()
            break
        elif parkoviste[sy][sx] == True:
            vysledek = "KO"
            step +=1
            while smer != "0":
                smer = input()
            break
        parkoviste[sy][sx] = True
        step += 1
        smer = input()
print(step, vysledek)
