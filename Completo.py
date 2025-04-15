import numpy as np
import time

def generate_matrix(n):
    return np.random.randint(0, 10, (n, n))

def multiply_traditional(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add_matrix(A, B):
    return A + B

def subtract_matrix(A, B):
    return A - B

def split_matrix(A):
    n = A.shape[0] // 2
    return A[:n, :n], A[:n, n:], A[n:, :n], A[n:, n:]

def multiply_dac(A, B):
    n = len(A)
    if n == 1:
        return A * B
    else:
        A11, A12, A21, A22 = split_matrix(A)
        B11, B12, B21, B22 = split_matrix(B)

        C11 = multiply_dac(A11, B11) + multiply_dac(A12, B21)
        C12 = multiply_dac(A11, B12) + multiply_dac(A12, B22)
        C21 = multiply_dac(A21, B11) + multiply_dac(A22, B21)
        C22 = multiply_dac(A21, B12) + multiply_dac(A22, B22)

        top = np.hstack((C11, C12))
        bottom = np.hstack((C21, C22))
        return np.vstack((top, bottom))

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

def measure_time(func, A, B):
    start = time.time()
    func(A, B)
    end = time.time()
    return end - start

def main():
    sizes = [2**i for i in range(1, 8)]  # desde 2 hasta 128
    print(f"{'n':>4} {'Tradicional':>15} {'Divide y vencerás':>20} {'Strassen':>15}")
    for n in sizes:
        A = generate_matrix(n)
        B = generate_matrix(n)
        t1 = measure_time(multiply_traditional, A, B)
        t2 = measure_time(multiply_dac, A, B)
        t3 = measure_time(multiply_strassen, A, B)
        print(f"{n:>4} {t1:>15.6f} {t2:>20.6f} {t3:>15.6f}")

if __name__ == "__main__":
    main()
