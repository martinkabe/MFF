
def find_first_appearence(array, value):
    if len(array) == 0:
        return 0

    position = 0
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = int(left + (right - left) / 2)
        if array[middle] >= value:
            right = middle - 1
            position = middle
        else:
            left = middle + 1
    if array[position] != value:
        return 0
    return(position+1)
        

if __name__ == '__main__':
    inputs = list(map(int, input().split()))
    if len(inputs) == 2:

        N, k = inputs

        data = []
        while len(data) < (N+k):
            inpt = list(map(int, input().split()))
            data += inpt

        data = data[:(N+k)]
        cisla = data[:N]
        dotazy = data[N:]

        if len(dotazy) > 0 and len(cisla) == 0:
            for i in range(len(dotazy)):
                print(0, end= " ")

        elif len(cisla) > 0 and len(dotazy) > 0:
            if (len(cisla) <= 1e6) and (len(dotazy) <= 1e6):
                for dotaz in dotazy:
                    print(find_first_appearence(cisla, dotaz), end=" ")
