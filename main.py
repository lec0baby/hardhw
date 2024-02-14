<<<<<<< HEAD
def input_matrix(k1, k2): 
    matr = [0] * k1
    for i in range(k1):
        matr[i] = input(f'Введите элементы строки №{i+1}: ').split()
        if len(matr[i]) != k2:
            return 'Error'
        return matr

print(input_matrix(3, 3))



'''mas = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in mas: 
    for i2 in i: 
        print(i2, end=' ') 
    print()'''
=======
def input_matrix(k1, k2):
    matr = [0] * k2
    for i in range(k2):
        matr[i] = input().split()
    return matr
    
print(input_matrix(3, 3))
>>>>>>> ba3d9abe8962529bd62aac1942ddf7e28cdcf20a
