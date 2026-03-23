import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    N = len(A)
    M = len(A[0])
    T_size = (M, N)

    zero = np.zeros(T_size)


    for i in range(M):
        for j in range(N):
            zero[i][j] = A[j][i]

    
    return (zero)

    pass
