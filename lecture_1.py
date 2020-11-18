class Matrix:

    def __init__(self, array, rows, columns):
        self.array = array
        self.rows = rows
        self.columns = columns

    def create_matrix(self):

        if self.rows * self.columns != len(self.array):
            return "invalid input"
        elif self.rows != self.columns:
            # If matrix is not square
            matrix = []
            for i in range(self.rows):
                temp_list = []
                for j in range(self.columns):
                    temp_list.append(self.array[self.columns * i + j])
                matrix.append(temp_list)
            return(matrix)
        else:
            # If matrix is square
            matrix = []
            for i in range(self.rows):
                temp_list = []
                for j in range(self.columns):
                    temp_list.append(self.array[self.rows * i + j])
                matrix.append(temp_list)
            return(matrix)


mat_1 = Matrix([-1, 1, 3, 7], 2, 2)
print(mat_1.create_matrix())

mat_2 = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(mat_2.create_matrix())

mat_3 = Matrix([1, 3, 5, 4], 3, 3)
print(mat_3.create_matrix())

mat_4 = Matrix([1, 2, 3, 4, 5, 6], 2, 3)
print(mat_4.create_matrix())
