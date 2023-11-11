from random import randint

pc_num = randint(0, 100)
user_num = int(input())

while pc_num != user_num:
    if pc_num > user_num:
        print('Загаданное число больше!')
    else:
        print('Загаданное число меньше!')
    user_num = int(input())

print('Вы угадали число!')