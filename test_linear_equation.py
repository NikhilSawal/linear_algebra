import unittest
from linear_equation import LinearEquation

class TestLinearEquation(unittest.TestCase):

    def setUp(self):

        self.eq_1 = LinearEquation([1, 2, 3, 1, 5, 6, 4, 3, 9], 3, 3)
        self.eq_2 = LinearEquation([1, 2, 3, 1, 5, 6, 4, 3, 9, 4, 2, 6, 2 , 5, 4, 4], 4, 4)

    def test_LU_decomposition(self):

        self.assertEqual(self.eq_1.LU_decomposition(), ([[1, 0, 0], [1, 1, 0], [4, -3, 1]], [[1, 2, 3], [0, 3, 4], [0, 0, 9]]))
        self.assertEqual(self.eq_2.LU_decomposition(), ([[1, 0, 0, 0], [5, 1, 0, 0], [9, 5, 1, 0], [2, -1, -1, 1]], [[1, 2, 3, 1], [0, -4, -6, -7], [0, 0, 5, 9], [0, 0, 0, 4]]))

if __name__ == '__main__':
    unittest.main()
