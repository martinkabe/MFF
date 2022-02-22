# Input: system of N linear equations with N unknown with coefficients as integers.
# The first row represents number of N.
# The second N rows describe equations by N+1 numbers separated by spaces.

# Find the solution (for example using Gaussian elimination) and write it down. 
# Let the value of the i-th variable (as an integer or a decimal number) be on the i-th line of the output.

# e.g. following system of linear equations: x1 + x2 = 3, 2x1 - x2 = 0
# 2
# 1 1 3
# 2 -1 0

# correct output is x1 = 1, x2 = 2 and printed as
# 1.0
# 2.0

# We guarantee that all test inputs will have regular systems with integer solutions. When eliminating, pay attention to the zeros on the diagonal.

### SOLUTION ###
def gauss(A):
    n = len(A)

    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def read_data():
    n_equations = int(input())
    i = 0
    mat = []
    while i < n_equations:
        mat.append(list(map(int, input().split())))
        i+=1
    return mat


if __name__ == "__main__":

    A = read_data()
    x = gauss(A)
    for el in x:
        print(el)