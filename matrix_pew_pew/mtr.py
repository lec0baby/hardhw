class Matrix: 
    def __init__(self, rows=0, columns=0, elements=None):
        if elements is None:
            elements = []
        self.rows = rows
        self.columns = columns
        self.elements = elements
    
    def _input_size(self):
        while True:
            try:
                print('Введите  числа:')
                self.rows, self.columns = int(input('Кол-во строк = ')), int(input('Кол-во столбцов = '))
            except ValueError:
                continue 
            else:
                break
    
    def _input_elements(self):
        self.elements = []
        for i in range(self.rows):
            self.elements.append(list(map(float, input(f'Введите элементы строки №{i+1}: ').split())))                  
            if len(self.elements[i]) != self.columns:
                raise ValueError('Некорректно введены элементы строки')
            
    def input_matrix(self):
        self._input_size()
        self._input_elements()

    def _plus(self, other1, other2):
        if other1.rows == other2.rows and other1.columns == other2.columns:    
            new_elements = []
            for i in range(other1.rows):
                help_el = []
                for j in range(other1.columns):
                    help_el.append(other1.elements[i][j] + other2.elements[i][j])
                new_elements.append(help_el)
            return new_elements
        else:
            raise ValueError('Матрицы должны быть одного размера')
        
    def _minus(self, other1, other2):
        if other1.rows == other2.rows and other1.columns == other2.columns:    
            new_elements = []
            for i in range(other1.rows):
                help_el = []
                for j in range(other1.columns):
                    help_el.append(other1.elements[i][j] - other2.elements[i][j])
                new_elements.append(help_el)
            return new_elements
        else:
            raise ValueError('Матрицы должны быть одного размера') 
        
    def __add__(self, other):
        if isinstance(other, Matrix3x3):
            return Matrix3x3(self._plus(self, other))
        elif isinstance(other, Matrix):
            return Matrix(self.rows, self.columns, self._plus(self, other))
        else:
            raise ValueError('Операция сложения невозможна')
        
    def __sub__(self, other):
        if isinstance(other, Matrix3x3):
            return Matrix3x3(self._minus(self, other))
        elif isinstance(other, Matrix):
            return Matrix(self.rows, self.columns, self._minus(self, other))
        else:
            raise ValueError('Операция вычитания невозможна')
        
    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.elements == other.elements
        else:
            raise ValueError('Невозможно сравнить')
        
    def __str__(self):
        output = ''
        for j in range(self.rows):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output
        
class Matrix3x3(Matrix):
    def __init__(self, elements=None):
        if elements is None:
            elements = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super().__init__(3, 3, elements)
        for i in range(self.rows):
            if len(self.elements[i]) != self.columns:
                raise ValueError('Каждая строка должна содержать ровно 3 элемента')

    def input_matrix(self):
        print('Матрица размерами 3x3')
        super()._input_elements()
            
    def determinant(self):
        return (
            self.elements[0][0] * self.elements[1][1] * self.elements[2][2] 
            + self.elements[1][0] * self.elements[2][1] * self.elements[0][2]
            + self.elements[0][1] * self.elements[1][2] * self.elements[2][0]
            - self.elements[2][0] * self.elements[1][1] * self.elements[0][2]
            - self.elements[0][1] * self.elements[1][0] * self.elements[2][2]
            - self.elements[1][2] * self.elements[2][1] * self.elements[0][0]
        )
    

if __name__ == "__main__":
    m1 = Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    m2 = Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    m3 = Matrix3x3([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
    '''if m1 + m2 == m3:
        print('да')
    else:
        print('нет')'''
    print(isinstance(m1, Matrix3x3))