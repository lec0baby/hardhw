from dz3.ex1 import frik

def move(k):
    lst = frik(input())
    lst = lst[-k:] + lst[:-k]
    return lst

print(move(int(input())))