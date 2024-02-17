class Matrix: 
    def __init__(self, rows, columns, elements):
        self.rows = rows
        self.columns = columns
        self.elements = elements
    
    def input_matrix(k1, k2): 
        matr = []
        for i in range(k1):
            matr.append(list(map(int, input(f'Введите элементы строки №{i+1}: ').split())))        
            if len(matr[i]) != k2:
                return 'Error'
        return matr
        
    def __str__(self):
        output = ''
        for j in range(self.rows):
            output += ' '.join(str(i) for i in self.elements[j])
            output += '\n'
        return output + f'Количесвто строк: {self.rows}\n' + f'Количество столбцов: {self.columns}'