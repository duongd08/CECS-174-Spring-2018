def mystery():
    mat = [[1, 2, 1],\
    [2, 1, 2],\
    [1, 2, 3]]

#len(mat) = 3

    plus = 0
    minus = 0

    for i in range(len(mat)): #for i in range(3):
        plus += mat[0][i] * mat[1][(i+1)%3] * mat[2][(i+2)%3] #Result is 11.
        minus += mat[2][i] * mat[1][(i+1)%3] * mat[0][(i+2)%3] #Result is 17.

    return plus - minus #Do the math operation: 11-17. -6 gets returned.

print(mystery()) # -6 is the result and gets printed.

