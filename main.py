import numpy as np
import time
from traditional import multiply_traditional
from dac import multiply_dac
from strassen import multiply_strassen

def generate_matrix(n):
    return np.random.randint(0, 10, (n, n))

def measure_time(func, A, B):
    start = time.time()
    func(A, B)
    end = time.time()
    return end - start

def main():
    sizes = [2**i for i in range(1, 8)]  # 2 to 128
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
