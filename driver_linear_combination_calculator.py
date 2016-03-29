"""
This is a code to find the linear independent linear combinations of columns of a matrix, which
are linearly dependent columns (). The intended use of the code is to find redundant combinations of features 
from the data
"""

import numpy as np

from sympy import Matrix

def find_symbolic_dependent_columns(x):
    """
    Find linearly dependent columns using symbolic calculations.
    :param x: The input numpy array
    :return: The linear combination matrix (Null Space of MAtrix).
    """
    x = Matrix(x)
    return(x.nullspace())

def find_numerically(x, tol = np.finfo(np.float).eps):
    """
    Find numerically using SVD decomposition. The returned solution will be nullspace
    of the matrix.
    :param x: The input numpy array
    :param tol: Tolerance varaibles less than tol are floored to zero.
    :return: The linear combination matrix (Null Space of the Matrix).
    """
    u, s, v = np.linalg.svd(x, full_matrices = True)
    zero_eigs = (np.abs(s) < tol)
    null_space = np.compress(zero_eigs, v, axis = 0).T
    return(null_space)

def find_dependent_rational_basis(x):
    """
    Find linearly dependent columns similar to MATLAB null(x, 'r').
    :param x: The input numpy array
    :return: The linear combination matrix (Null Space of Matrix).
    """
    m, n = x.shape
    x = Matrix(x)
    R = x.rref()
    r = len(R[1])
    nopiv = np.arange(0, n)
    p = np.array(R[1])
    a = np.array(R[0])
    nopiv = np.delete(nopiv, p, axis = 0)
    Z = np.zeros([n, n-r])
    if n > r:
        Z[nopiv, :] = np.eye(n-r, n-r)
        if r > 0:
            Z[p, :] = -a[0:r, nopiv]
    return(Z)

if __name__ == '__main__':
    """
    Simple use case.
    """
    print(' Define Matrix ')
    
    A = np.array([[2, 4, 1, 3], [-1, -2, 1, 0], [0, 0, 4, 4], [3, 6, 2, 5]])
    
    print(A)
    
    print(' Output Matrix ')
    
    U = find_symbolic_dependent_columns(A)
    
    print(U)
    
    print(' Using Numerical Approximation')
    
    V = find_numerically(A)
    
    print(V)
    
    print(' Matlab N null(x, 'r') ')
    
    W = find_dependent_rational_basis(A)
    
    print(W)






