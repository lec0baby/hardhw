from ex3_1 import frik

def move(k: int, pos: list):
    pos = pos[-k:] + pos[:-k]
    return pos

if __name__ == '__main__':
    print(move(int(input()), frik(int(input()))))