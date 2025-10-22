import numpy as np
import scipy.linalg as linalg
import sympy as sp

# compute rank to get dimensionality, then perform row reduction to get vectors for basis
def getDimensionality(a):
    a_matrix = sp.Matrix(a)

    rref_matrix, pivot_cols = a_matrix.rref()

    rank = np.linalg.matrix_rank(a)
    print(f"Dimensionality: {rank}")
    print(f"Basis: {rref_matrix}")

    return rank
