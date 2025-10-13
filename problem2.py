import numpy as np
import scipy.linalg as linalg



# go to office hours for this maybe cause id 
# @param a change of basis matrix
# @param is input column vector
# multiplies change of basis matrix and column vector to produce vector in new basis
def newBasisVector(a, b):
    vectorNewBasis = a @ b
    return vectorNewBasis


# x
x = np.array([[-18], [8], [5]])

# [x]B
xB = np.array([[-2], [6], [1]])

changeMatrix = [[0, -4, 6], [-1, 0, 6], [-1, 0, 3]]

newVector = newBasisVector(changeMatrix, xB)

# convert 
# newVectorB = 

print("[x]B -> x: ")
print(newVector)

print("\n[x] -> [x]b: ")