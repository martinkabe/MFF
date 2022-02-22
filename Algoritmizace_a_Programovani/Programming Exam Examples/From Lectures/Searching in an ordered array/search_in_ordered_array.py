def binary_search(array, value):
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
    return(position + 1)


def read_inputs(bound):
    vals = []
    while len(vals) < bound:
        vals += list(map(int, input().split()))
    return vals


if __name__ == '__main__':
    inputs = list(map(int, input().split()))
    if len(inputs) == 2:
        N, k = inputs

        if (N <= 1e6) and (k <= 1e6):
            if k > 0 and N == 0:
                print(*[0] * k, end= " ")
            else:
                cisla = read_inputs(N)
                dotazy = read_inputs(k)
                
                for dotaz in dotazy:
                    print(binary_search(cisla, dotaz), end=" ")