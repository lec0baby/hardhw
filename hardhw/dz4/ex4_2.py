def fact(n):
    if n < 0:
        return 'Не существует'
    f = 1
    while n:
        f = f * n
        n -= 1
    return f

if __name__ == '__main__':
    print(fact(int(input())))