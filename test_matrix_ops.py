import unittest
from matrix_ops import Matrix

class TestMatrix(unittest.TestCase):

    def setUp(self):

        self.mat_1 = Matrix([-1, 1, 3, 7], 2, 2)
        self.mat_2 = Matrix([1, 2, 3, 0, 5, 6, 0, 0, 9], 3, 3)
        self.mat_3 = Matrix([1, 3, 5, 4], 3, 3)
        self.mat_4 = Matrix([1, 2, 3, 4, 5, 6], 1, 2)
        self.mat_5 = Matrix([1, 0, 1, 1], 2, 2)

    def tearDown(self):
        pass

    def test_create_matrix(self):

        self.assertEqual(self.mat_1.create_matrix(), [[-1, 1], [3, 7]])
        self.assertEqual(self.mat_2.create_matrix(), [[1, 2, 3], [0, 5, 6], [0, 0, 9]])
        self.assertEqual(self.mat_3.create_matrix(), "invalid input")
        self.assertEqual(self.mat_4.create_matrix(), "invalid input")

    def test_swap_rows(self):

        self.assertEqual(self.mat_1.swap_rows(0, 1), [[3, 7], [-1, 1]])
        self.assertEqual(self.mat_2.swap_rows(1, 2), [[1, 2, 3], [0, 0, 9], [0, 5, 6]])

    def test_check_triangular(self):

        self.assertEqual(self.mat_1.check_triangular('lower'), False)
        self.assertEqual(self.mat_2.check_triangular('lower'), True)
        self.assertEqual(self.mat_5.check_triangular('upper'), True)

    def test_transpose(self):

        self.assertEqual(self.mat_1.transpose(), [[-1, 3], [1, 7]])
        self.assertEqual(self.mat_2.transpose(), [[1, 0, 0], [2, 5, 0], [3, 6, 9]])

if __name__ == '__main__':
    unittest.main()
