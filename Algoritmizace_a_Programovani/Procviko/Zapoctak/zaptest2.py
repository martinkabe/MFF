# 5  1 2  1 2  2 3  2 17  2 17
vstup = list(map(int, input().split()))
n = vstup[0]
kocky = []
vstup.pop(0)
while len(kocky) < n:           #nacitanie vstupu
    if len(vstup) == 0:
        vstup = list(map(int, input().split()))

    kocky.append([vstup[0], vstup[1]])
    vstup.pop(0)
    vstup.pop(0)
    if len(kocky) == n:
        break
    if len(vstup)==0:
        vstup = list(map(int, input().split()))

pole = [[0 for i in range(39)] for j in range(39)]      #matica sousednosti

for i in range(n):
    pole[kocky[i][0]][kocky[i][1]] += 1
    pole[kocky[i][1]][kocky[i][0]] += 1

naj = 0

def Prehladavanie(matica, od, do, maximum):
    global naj
    for i in range(od, do):
        for j in range(1, 39):
            if matica[i][j] != 0:
                matica[i][j] -= 1
                matica[j][i] -= 1
                m = Prehladavanie(matica, j, j+1, maximum+1)
                if m > naj:
                    naj = m
                matica[i][j] += 1
                matica[j][i] += 1

    return maximum

Prehladavanie(pole, 0, 38, 0)

print(naj)