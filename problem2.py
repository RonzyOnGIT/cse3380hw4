import numpy as np
import scipy.linalg as linalg

def getDimensionality(a):
    rank = np.linalg.matrix_rank(a)
    return rank

# @param a change of basis matrix
# @param is input column vector
# @param is whether the input vector is in the same basis as change of basis matrix
# following formula of x = B[x]B to calculate new coordinates
def newBasisVector(a, b, sameBasis: bool):
    if sameBasis:
        return a @ b
    else:
        return np.linalg.solve(a, b)


# x
x = np.array([[-18], [8], [5]])

# [x]B
xB = np.array([[-2], [6], [1]])

changeMatrix = [[0, -4, 6], [-1, 0, 6], [-1, 0, 3]]

# this should output (-2, 6, 1)
newVector = newBasisVector(changeMatrix, x, False)
print(newVector)

print("\n")

# this should print (-18, 8, 5)
newVector = newBasisVector(changeMatrix, xB, True)
print(newVector)

print(getDimensionality(changeMatrix))

