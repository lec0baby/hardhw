x = input()

def func(x):
    s = []
    while x:
        s.append(x)
        x = input()
    return s

print (func(x))