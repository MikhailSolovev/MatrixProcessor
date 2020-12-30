import copy


class Matrix:

    def __init__(self, row_num, column_num=None, matrix=None):
        self.row_num = row_num
        if column_num is None:
            self.column_num = row_num
        else:
            self.column_num = column_num
        if matrix is None:
            self.matrix = []
            for _ in range(self.row_num):
                self.matrix.append([0 for _ in range(self.column_num)])
        else:
            self.matrix = matrix

    def __str__(self):
        str_ = ''
        for row in self.matrix:
            for el in row:
                if el == -0:
                    el = 0
                str_ += str(el) + ' '
            str_ += '\n'
        return str_

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.row_num == other.row_num and self.column_num == other.column_num:
                result = Matrix(self.row_num, self.column_num)
                for r in range(self.row_num):
                    for c in range(self.column_num):
                        result.matrix[r][c] = self.matrix[r][c] + other.matrix[r][c]
                return result
            else:
                return 'The operation cannot be performed.'

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return 'The operation cannot be performed.'
        elif isinstance(other, Matrix):
            if self.column_num == other.row_num:
                result = Matrix(self.row_num, other.column_num)
                for r in range(self.row_num):
                    for c_2 in range(other.column_num):
                        el = 0
                        for c_1 in range(self.column_num):
                            el += self.matrix[r][c_1] * other.matrix[c_1][c_2]
                        result.matrix[r][c_2] = el
                return result
            else:
                return 'The operation cannot be performed.'

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            result = Matrix(self.row_num, self.column_num)
            for r in range(self.row_num):
                for c in range(self.column_num):
                    result.matrix[r][c] = self.matrix[r][c] * other
            return result

    def mdg_transpose(self):
        result = Matrix(self.row_num, self.column_num)
        for r in range(self.row_num):
            for c in range(self.column_num):
                result.matrix[c][r] = self.matrix[r][c]
        return result

    def sdg_transpose(self):
        result = Matrix(self.row_num, self.column_num)
        for r in range(self.row_num - 1, -1, -1):
            for c in range(self.column_num - 1, -1, -1):
                result.matrix[self.column_num - 1 - c][self.row_num - 1 - r] = self.matrix[r][c]
        return result

    def vl_transpose(self):
        result = Matrix(self.row_num, self.column_num)
        for r in range(self.row_num):
            for c in range(self.column_num):
                result.matrix[r][self.column_num - 1 - c] = self.matrix[r][c]
        return result

    def hl_transpose(self):
        result = Matrix(self.row_num, self.column_num)
        for r in range(self.row_num):
            for c in range(self.column_num):
                result.matrix[self.row_num - 1 - r][c] = self.matrix[r][c]
        return result

    @property
    def determinant(self):
        sum_ = 0
        if self.row_num != self.column_num:
            return 'The operation cannot be performed.'
        elif self.row_num == 1:
            return self.matrix[0][0]
        else:
            if self.column_num == 2:
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            else:
                for c in range(self.column_num):
                    cof = copy.deepcopy(self.matrix[1:][:])
                    for r in range(self.row_num - 1):
                        cof[r].pop(c)
                    sum_ += (-1) ** (2 + c) * self.matrix[0][c] * Matrix(self.row_num - 1, self.column_num - 1,
                                                                         cof).determinant
                return sum_

    @property
    def cofactor(self):
        result = Matrix(self.row_num, self.column_num)
        for r in range(self.row_num):
            for c in range(self.column_num):
                cof = []
                for i in range(self.row_num):
                    if i != r:
                        tmp = []
                        for j in range(self.column_num):
                            if j != c:
                                tmp.append(self.matrix[i][j])
                        cof.append(tmp)
                result.matrix[r][c] = (-1) ** (r + c) * Matrix(self.row_num - 1, self.column_num - 1, cof).determinant
        return result

    @property
    def inverse(self):
        if (self.determinant is None) or (self.determinant == 0):
            return "This matrix doesn't have an inverse."
        else:
            print('The result is:')
            return (1 / self.determinant) * self.cofactor.mdg_transpose()

    @staticmethod
    def new_matrix(str_=''):
        n, m = map(int, input('Enter size of {} matrix: > '.format(str_)).split())
        print('Enter {} matrix:'.format(str_))
        cof = [list(map(float, input('> ').split())) for _ in range(n)]
        return Matrix(n, m, cof)


while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    choice = input('Your choice: > ')
    if choice == '1':
        A = Matrix.new_matrix('first')
        B = Matrix.new_matrix('second')
        print('The result is:')
        print(A + B)
    elif choice == '2':
        A = Matrix.new_matrix()
        scalar = float(input('Enter constant: > '))
        print('The result is:')
        print(scalar * A)
    elif choice == '3':
        A = Matrix.new_matrix('first')
        B = Matrix.new_matrix('second')
        print('The result is:')
        print(A * B)
    elif choice == '4':
        print('''\n1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        choice = input('Your choice: > ')
        A = Matrix.new_matrix()
        print('The result is:')
        if choice == '1':
            print(A.mdg_transpose())
        elif choice == '2':
            print(A.sdg_transpose())
        elif choice == '3':
            print(A.vl_transpose())
        elif choice == '4':
            print(A.hl_transpose())
    elif choice == '5':
        A = Matrix.new_matrix()
        print('The result is:')
        print(A.determinant)
        print()
    elif choice == '6':
        A = Matrix.new_matrix()
        print(A.inverse)
    elif choice == '0':
        exit()
