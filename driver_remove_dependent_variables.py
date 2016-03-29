import numpy as np

def remove_dependent_variables(x, tol = np.finfo(np.float).eps):
    """
    Find independent columns using QR decomposition. The returned solution might
    not unique. There might be other subset of independent columns. Strict 
    condition number of rows (m) > number of columns (n)
    :param x: The input numpy array
    :param tol: Tolerance, variables less than tol are removed
    :return: The linearly independent subset of variables
    """
    r = np.linalg.matrix_rank(x)
    n = x.shape[1]
    assert(r is not n), 'Matrix is already linearly independent'
    q, r = np.linalg.qr(x)
    ind  = np.where(np.abs(r.diagonal()) > tol)[0]
    return(ind, x[:, ind])

if __name__ == '__main__':
    """
    Simple use case
    """
    print('Define Matrix')
    
    A = np.array([[2, 4, 1, 3], [-1, -2, 1, 0], [0, 0, 4, 4], [3, 6, 2, 5]])
    
    print(A)
    
    print(' Output Matrix ')
    
    i, Y = remove_dependent_variables(A)
    
    print(Y)
    