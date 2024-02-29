class Matrix: 
    def __init__(self, rows = 0, columns = 0, elements = []):
        self.rows = rows
        self.columns = columns
        self.elements = elements

    def input_matrix(self): 
        self.elements = []
        while True:
            try:
                print('Введите  числа:')
                self.rows, self.columns = int(input('Кол-во строк = ')), int(input('Кол-во столбцов = '))
            except ValueError:
                continue 
            else:
                break
        for i in range(self.rows):
            self.elements.append(list(map(float, input(f'Введите элементы строки №{i+1}: ').split())))                  
            if len(self.elements[i]) != self.columns:
                raise ValueError('Некорректно введены элементы строки')
        
    def __str__(self):
        output = ''
        for j in range(self.rows):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output
    
    
class Matrix3x3(Matrix):
    def determinant(self):
        return self.elements[0][0] * self.elements[1][1] * self.elements[2][2] + self.elements[1][0] * self.elements[2][1] * self.elements[0][2] + self.elements[0][1] * self.elements[1][2] * self.elements[2][0] - self.elements[2][0] * self.elements[1][1] * self.elements[0][2] - self.elements[0][1] * self.elements[1][0] * self.elements[2][2] - self.elements[1][2] * self.elements[2][1] * self.elements[0][0]
    

if __name__ == "__main__":
    n = Matrix3x3()
    n.input_matrix()
    print(n.determinant())