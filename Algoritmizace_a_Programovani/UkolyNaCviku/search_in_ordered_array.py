def find(myList, target):
    for i in range(len(myList)):
        if myList[i] == target:
            yield i


def custom_search(arr, target) -> int:
    n = len(arr) + 1
    for i in range(1, n):
        if (arr[i-1] == target):
            return(i)
    return(0)


def custom_search_2(arr, target):
    try:
        return(arr.index(target)+1)
    except ValueError as e:
        return(0)


def custom_search_3(arr, target):
    f = (find(arr, target))
    ind = next(f, None)
    return(0 if ind == None else ind+1)


def give_numbers():
    inputs = list(map(int, input().split()))
    if len(inputs) != 2:
        return([], None, None)
    n, m = inputs
    if ((n < 1 or n > 1000000) or (m < 1 or m > 1000000)):
        return([], None, None)
    i = 2
    stuff = []
    while i >= 1:
        stuff.append(list(map(int, input().split())))
        i -= 1
    return(stuff, n, m)


inpt, n, m = give_numbers()
if len(inpt) != 0:
    N, k = inpt
    if n == len(N) and m == len(k):
        mapped = map(custom_search_2, N, k)
        print(list(mapped))

# _Input:_
#   8 5
#   2 5 6 6 6 9 13 18
#   6 2 3 18 9


# _Output:_
#   3 1 0 8 6
