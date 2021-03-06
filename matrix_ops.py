class Matrix:
    '''
    This class contains several matrix related operations.
    To create an instance of this class requires three arguments:
    Args:
        param1 (list): array
        param2 (int): number_of_rows as int
        param3 (int): number_of_columns as int

    Call:
        >> mat_1 = Matrix([-1, 1, 3, 7], 2, 2)

    Returns:
        matrix
    '''
    def __init__(self, array, rows, columns):

        self.array = array
        self.rows = rows
        self.columns = columns

    # Lecture 1 - Linear Algebra
    def create_matrix(self):
        '''
        This method creates a matrix as follows:
        eg.
        # create an instance of class Matrix by calling
        >> mat_1 = Matrix([-1, 1, 3, 7], 2, 2)

        # call the create_matrix() method, by passing mat_1 as the argument
        >> print(mat_1.create_matrix).

        Returns "invalid input" if the length of input array is not equal to product
        of n_rows and n_columns.
        '''
        if self.rows * self.columns != len(self.array):
            return 'invalid input'

        elif self.rows != self.columns:
            # If matrix is not square
            matrix = []
            for i in range(self.rows):
                temp_list = []
                for j in range(self.columns):
                    temp_list.append(float(self.array[self.columns * i + j]))
                matrix.append(temp_list)
            return matrix

        else:
            # If matrix is square
            matrix = []
            for i in range(self.rows):
                temp_list = []
                for j in range(self.columns):
                    temp_list.append(float(self.array[self.rows * i + j]))
                matrix.append(temp_list)
            return matrix

    # Lecture 2 - Linear Algebra
    def swap_rows(self, x, y):
        '''
        Swaps row for Gaussian Elimination.
        Args:
            param1 : Instance of class
            param2 (int): Index of row1
            param3 (int): Index of row2
        eg:
        >> mat_1.swap_rows(0, 1)

        where mat_1 is an instance of class Matrix and 0, 1 are the indexes of the rows
        that need to be swapped.
        '''
        matrix = self.create_matrix()
        matrix[x], matrix[y] = matrix[y], matrix[x]
        return matrix

    def check_triangular(self, method):
        '''
        Checks if a matrix is triangular or not.
        Args:
            param1 : Instance of class

        Call:
            >> mat_1.check_triangular()

        Returns:
            bool: True if matrix is upper triangular.
        '''
        matrix = self.create_matrix()
        if len(matrix) != len(matrix[0]):
            return 'Not a square matrix'

        elif method == 'lower':
            for row in range(1, self.rows):
                for col in [j for j in range(self.columns) if j < row]:
                    if matrix[row][col] > 0:
                        return False
            return True

        elif method == 'upper':
            for col in range(1, self.columns):
                for row in [j for j in range(self.rows) if j < col]:
                    if matrix[row][col] > 0:
                        return False
            return True

    def transpose(self):

        matrix = self.create_matrix()
        if len(matrix) != len(matrix[0]):
            return 'Not a square matrix'

        else:
            transpose = []
            for col in range(self.columns):
                temp_list = []
                for row in range(self.rows):
                    temp_list.append(matrix[row][col])
                transpose.append(temp_list)
            return transpose

    def make_triangular(self):

        matrix = self.create_matrix()
        if len(matrix) != len(matrix[0]):
            return 'Not a square matrix'

        else:
            for row in range(1, self.rows):
                for col in [i for i in range(self.columns) if i < row]:
                    if matrix[row][col] != 0:
                        mul = matrix[row][col]/matrix[col][col]
                        matrix[row] = [(a_i - (mul * b_i)) for a_i, b_i in zip(matrix[row], matrix[col])]
                    else:
                        pass
            return matrix
