def input_matrix(k1, k2):
    matr = [0] * k2
    for i in range(k2):
        matr[i] = input().split()
    return matr
    
print(input_matrix(3, 3))
