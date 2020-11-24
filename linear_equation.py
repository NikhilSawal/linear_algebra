from matrix_ops import Matrix

class LinearEquation:

    def __init__(self, arr1, n1, p1):
        self.arr1 = arr1
        self.nRows = n1
        self.nCols = p1

    def LU_decomposition(self):

        inp_mat_1 = Matrix(self.arr1, self.nRows, self.nCols)
        mat_1 = inp_mat_1.create_matrix()

        # create identity matrix for the L component
        l_comp = [[0 for x in range(self.nCols)] for y in range(self.nRows)]
        for i in range(self.nRows):
            for j in range(self.nCols):
                if i == j:
                    l_comp[i][j] = 1
                pass

        # create matrix for U component
        u_comp = [[0 for x in range(self.nCols)] for y in range(self.nRows)]
        for k in range(self.nRows):
            u_comp[k][k] = mat_1[k][k]
            for i in range(k + 1, self.nRows):
                l_comp[i][k] = mat_1[i][k] / u_comp[k][k]
                u_comp[k][i] = mat_1[k][i]
            for i in range(k + 1, self.nRows):
                for j in range(k + 1, self.nRows):
                    mat_1[i][j] = mat_1[i][j] - l_comp[i][k] * u_comp[k][i]
        return l_comp, u_comp


eq_1 = LinearEquation([1, 2, 3, 1, 5, 6, 4, 3, 9], 3, 3)
print(eq_1.LU_decomposition())

eq_2 = LinearEquation([1, 2, 3, 1, 5, 6, 4, 3, 9, 4, 2, 6, 2 , 5, 4, 4], 4, 4)
print(eq_2.LU_decomposition())
