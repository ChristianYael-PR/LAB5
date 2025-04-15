import numpy as np

def add_matrix(A, B):
    return A + B

def subtract_matrix(A, B):
    return A - B

def split_matrix(A):
    n = A.shape[0] // 2
    return A[:n, :n], A[:n, n:], A[n:, :n], A[n:, n:]

def multiply_strassen(A, B):
    n = len(A)
    if n == 1:
        return A * B
    else:
        A11, A12, A21, A22 = split_matrix(A)
        B11, B12, B21, B22 = split_matrix(B)

        M1 = multiply_strassen(add_matrix(A11, A22), add_matrix(B11, B22))
        M2 = multiply_strassen(add_matrix(A21, A22), B11)
        M3 = multiply_strassen(A11, subtract_matrix(B12, B22))
        M4 = multiply_strassen(A22, subtract_matrix(B21, B11))
        M5 = multiply_strassen(add_matrix(A11, A12), B22)
        M6 = multiply_strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
        M7 = multiply_strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        top = np.hstack((C11, C12))
        bottom = np.hstack((C21, C22))
        return np.vstack((top, bottom))
