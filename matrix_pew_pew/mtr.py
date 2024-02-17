class Matrix: 
    def __init__(self, rows = 0, columns = 0, elements = []):
        self.rows = rows
        self.columns = columns
        self.elements = elements

    
    def input_matrix(self): 
        self.elements = []
        self.rows, self.columns = int(input()), int(input())
        for i in range(self.rows):
            self.elements.append(list(map(int, input(f'Введите элементы строки №{i+1}: ').split())))        
        for j in range(self.rows):
            if len(self.elements[j]) != self.columns:
                return 'Ошибка: неверное кол-во элементов в строке'
        
    def __str__(self):
        output = ''
        for j in range(self.rows):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output + f'Количество строк: {self.rows}\n' + f'Количество столбцов: {self.columns}'

m = Matrix()
m.input_matrix()
#print(m)