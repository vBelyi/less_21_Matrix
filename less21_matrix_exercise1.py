class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

#додавання матриць
    def add_matrix(self):
        try:
            if len(self.list1) != len(self.list2) or len(self.list1[0]) != len(self.list2[0]):
                raise Exception
            for i in range(len(self.list1)):
                if len(self.list1[i]) != len(self.list2[i]):
                    raise Exception
            result = []
            for i in range(len(self.list1)):
                temp = []
                for j in range(len(self.list1[0])):
                    temp.append(self.list1[i][j] + self.list2[i][j])
                result.append(temp)
            return result
        except Exception:
            print('ERROR: please use equal matrices for adding')

#віднімання матриць
    def subtract_matrix(self):
        try:
            if len(self.list1) != len(self.list2) or len(self.list1[0]) != len(self.list2[0]):
                raise Exception
            for i in range(len(self.list1)):
                if len(self.list1[i]) != len(self.list2[i]):
                    raise Exception
            result = []
            for i in range(len(self.list1)):
                temp = []
                for j in range(len(self.list1[0])):
                    temp.append(self.list1[i][j] - self.list2[i][j])
                result.append(temp)
            return result
        except Exception:
            print('ERROR: please use equal matrices for subtraction')

# множення на число
    def mult_by_number(self, number):
        try:
            for i in self.list1:
                if len(self.list1[0]) != len(i):
                    raise Exception
            result = []
            for i in range(len(self.list1)):
                temp = []
                for j in range(len(self.list1[0])):
                    temp.append(self.list1[i][j] * number)
                result.append(temp)
            return result
        except Exception:
            print('ERROR, please use the lists that can be used to build the matrix, not a set of unequal lists.')

# множення матриці на матрицю
    def mult_matrix_matrix(self):
        try:
            for i in range(len(self.list1)):
                if len(self.list1[i]) != len(self.list2):
                    raise Exception
            for i in range(len(self.list2)):
                if len(self.list2[i]) != len(self.list1):
                    raise Exception
            result = []
            for i in range(len(self.list1)):
                temp = []
                for j in range(len(self.list2[0])):
                    sum = 0
                    for k in range(len(self.list2)):
                        sum += self.list1[i][k] * self.list2[k][j]
                    temp.append(sum)
                result.append(temp)
            return result
        except Exception:
            print('ERROR: try another matrices to multiply. Sizes to multiply do not match.')

# Транспонування матриць
    def transpose_matrix(self):
        try:
            for i in range(len(self.list1)):
                if len(self.list1[0]) != len(self.list1[i]):
                    raise Exception
            result = []
            for i in range(len(self.list1[0])):
                temp = []
                for j in range(len(self.list1)):
                    temp.append(self.list1[j][i])
                result.append(temp)
            return result
        except Exception:
            print('ERROR, please use the lists that can be used to build the matrix, not a set of unequal lists.')
#друк результату
    def print_matrix(self, matrix):
        if isinstance(matrix, list):
            for j in matrix:
                print(j)


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
m3 = [[1,2,3],[3,1,3]]
m4 = [[4,2],[3,1],[1,5]]

#додавання та віднімання матриць
matrix = Matrix(m1, m2)
add_result = matrix.add_matrix()
matrix.print_matrix(add_result)
sub_result = matrix.subtract_matrix()
matrix.print_matrix(sub_result)
#множення матриці на число
matrix = Matrix(m1, None)
result = matrix.mult_by_number(100)
matrix.print_matrix(result)
#множення матриці на матрицю
matrix = Matrix(m3,m4)
mult_matr_result = matrix.mult_matrix_matrix()
matrix.print_matrix(mult_matr_result)
#транспонування матриці
matrix = Matrix(m2,None)
transpose_result = matrix.transpose_matrix()
matrix.print_matrix(transpose_result)