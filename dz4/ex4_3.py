def is_unique(x):
    s = set()
    for i in x:
        if i in s: 
            return False
        s.add(i)
    return True

if __name__ == '__main__':
    print(is_unique(input()))
