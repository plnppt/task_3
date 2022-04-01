from scipy.linalg import solve_triangular
import numpy as np


def print_matrix(A, b):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print("{:3.0f}".format(A[i][j]), end=" ")
        print('')

    for i in range(len(b)):
        print("{:15.0f}".format(b[i]))
    print('')


def method_cholesky(A, b):
    for i in range(10000):
        L = np.linalg.cholesky(A)
        y = solve_triangular(L, b, lower=True)
        x = solve_triangular(L, y, lower=True, trans=1)
    print(x)


if __name__ == '__main__':
    A = np.array([[81, -45, 45],
                  [-45, 50, -15],
                  [45, -15, 38]])

    b = np.array([531, -460, 193])

    print('\n' + 'the original SLAE:' + '\n')
    print_matrix(A, b)
    print('\n' + "the vector by Cholesky's method:" + '\n')
    method_cholesky(A, b)
