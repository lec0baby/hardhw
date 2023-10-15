def check(x):
    return len(x) == len(set(x))

print(check(input()))