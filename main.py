from scipy.linalg import solve_triangular
import numpy as np


def print_matrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print("{:3.0f}".format(A[i][j]), end=" ")
        print('')

    for i in range(len(B)):
        print("{:15.0f}".format(B[i]))
    print('')


def method_cholesky(A, B):
    for i in range(10000):
        L = np.linalg.cholesky(A)
        Y = solve_triangular(L, B, lower=True, check_finite=False)
        X = solve_triangular(L, Y, lower=True, trans=1, check_finite=False)
    print(X)


if __name__ == '__main__':
    A = np.array([[81, -45, 45],
                  [-45, 50, -15],
                  [45, -15, 38]])

    B = np.array([531, -460, 193])

    print('\n' + 'The original SLAE:' + '\n')
    print_matrix(A, B)
    print('\n' + "The vector by Cholesky's method:" + '\n')
    method_cholesky(A, B)
