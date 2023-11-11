def f(n):
    return sum(n) / len(n)

n = [int(n) for n in input().split()]
print(f(n))