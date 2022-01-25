# https://www.techiedelight.com/calculate-sum-elements-sub-matrix-constant-time/

def preprocess(mat):
    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))
 
    # preprocess the matrix `mat` such that `s[i][j]` stores
    # sum of elements in the matrix from (0, 0) to (i, j)
    s = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
    s[0][0] = mat[0][0]
 
    # preprocess the first row
    for j in range(1, len(mat[0])):
        s[0][j] = mat[0][j] + s[0][j - 1]
 
    # preprocess the first column
    for i in range(1, len(mat)):
        s[i][0] = mat[i][0] + s[i - 1][0]
 
    # preprocess the rest of the matrix
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            s[i][j] = mat[i][j] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
 
    return s

# Calculate the sum of all elements in a submatrix in constant time
def findSubmatrixSum(mat, p, q, r, s):
 
    # base case
    if not mat or not len(mat):
        return 0
 
    # preprocess the matrix
    mat = preprocess(mat)
 
    # `total` is `mat[r][s] - mat[r][q-1] - mat[p-1][s] + mat[p-1][q-1]`
    total = mat[r][s]
 
    if q - 1 >= 0:
        total -= mat[r][q - 1]
 
    if p - 1 >= 0:
        total -= mat[p - 1][s]
 
    if p - 1 >= 0 and q - 1 >= 0:
        total += mat[p - 1][q - 1]
 
    return total
 
 
if __name__ == '__main__':
 
    mat = [
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0]
    ]
 
    # (p, q) and (r, s) represent top-left and bottom-right
    # coordinates of the submatrix
    p = 2
    q = 1
    r = 4
    s = 3
 
    # calculate the submatrix sum
    print(findSubmatrixSum(mat, p, q, r, s))
