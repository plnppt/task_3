import unittest
import numpy as np
import main


class MyTestCase(unittest.TestCase):
    def test_method_1(self):
        A = np.array([[6, 15, 55],
                      [15, 55, 225],
                      [55, 225, 979]])

        b = np.array([76, 295, 1259])

        self.assertEqual(main.method_cholesky(A, b), None)

    def test_method_2(self):
        A = np.array([[15, 3, 4, 5],
                      [2, 16, 4, 5],
                      [2, 3, 17, 5],
                      [2, 3, 4, 18]])

        b = np.array([13, -1, 17, -50])

        self.assertEqual(main.method_cholesky(A, b), None)


if __name__ == '__main__':
    unittest.main()
