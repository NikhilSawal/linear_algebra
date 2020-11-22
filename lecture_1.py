class Matrix:

    def __init__(self, array, rows, columns):

        self.array = array
        self.rows = rows
        self.columns = columns

    # Lecture 1 - Linear Algebra
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
            return matrix

        else:
            # If matrix is square
            matrix = []
            for i in range(self.rows):
                temp_list = []
                for j in range(self.columns):
                    temp_list.append(self.array[self.rows * i + j])
                matrix.append(temp_list)
            return matrix

    # Lecture 2 - Linear Algebra
    def swap_rows(self, x, y):

        matrix = self.create_matrix()
        matrix[x], matrix[y] = matrix[y], matrix[x]
        return matrix

    def check_triangular(self):

        matrix = self.create_matrix()
        if self.rows != self.columns:
            return "Not a square matrix"
        else:
            for i in range(1, self.rows):
                for j in [j for j in range(self.columns) if j < i]:
                    if matrix[i][j] > 0:
                        return False
            return True

    def make_triangular(self):
        pass
