def fact(n):
    if n < 0:
        return 'Не существует'
    elif n == 0:
        return 1
    else:
        f = 1
        while n:
            f = f * n
            n -= 1
        return f