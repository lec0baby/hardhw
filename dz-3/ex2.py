n = int(input())
def wssa(n):
    if (n > 0 and n < 3) or n == 12:
        return 'Зима'
    elif (n > 2 and n < 6):
        return 'Весна'
    elif (n > 5 and n < 9):
        return 'Лето'
    else:
        return 'Осень'
print (wssa(n))

