def check(x):
    return len(x) == len(set(x))

if __name__ == '__main__':
    print(check(input()))