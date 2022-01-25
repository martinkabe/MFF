from math import factorial, floor

# compute the k-th permutation of S (all indices are zero-based)
# all elements in S must be unique

def kthperm(S, k):  #  nonrecursive version
    P = []
    while S != []:
        f = factorial(len(S)-1)
        i = int(floor(k/f))
        x = S[i]
        k = k%f
        P.append(x)
        S = S[:i] + S[i+1:]
    return P


def kthpermrec(S, k):   # recursive version
    P = []
    if S == []:
        return []
    else:
        f = factorial(len(S)-1)
        i = int(floor(k/f))
        return [S[i]] + kthpermrec(S[:i] + S[i+1:], k%f)


if __name__ == "__main__":
    # This creates the k-th permutations for k=0..len(S)!, and then checks that the result is indeed in lexicographic order.

    nrElements = 10
    printout = True
    result = [] # the list of permutations
    for k in range(factorial(nrElements)): # loop over all k=0..len(S)!
        S = range(nrElements)    # [0, 1, 2, 3, ... , nrElements-1] 
        p1 = kthperm(S, k)    # compute k-th permutation iteratively
        p2 = kthpermrec(S, k)    # compute k-th permutation recursively
        assert p1==p2       # make sure the recursive and non-recursive function yield the same permutation
        if printout:
            print (p1)
        result.append(p1)    # add to list of permutations

    for i in range(len(result)-1):    # check that permutations are in lexicographic order.
        assert result[i] < result[i+1], "Permutations are not sorted, the code is incorrect."
        assert len(set(result[i])) == len(result[i]), "Permutation contains multiple copies of an element, the code is incorrect."
    assert len(set(result[-1])) == len(result[-1]), "Permutation contains multiple copies of an element, the code is incorrect."    # check on last element
    print ("The code is correct for |S| = %d." % nrElements)    # This line is only reached if no assertion failed, i.e. all permutations are in lexicographic order.


    print (kthperm([1, 2, 3, 5, 4], 1))
# print (kthperm(range(10), 1000001))