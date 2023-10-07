n = int(input())

def fib(n):
    k1 = 0
    k2 = 1
    f = 0
    for i in range(1, n + 1):
        f = k1 + k2
        print(f, end=' ')
        k2 = k1
        k1 = f
fib(n)



