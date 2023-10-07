str = input()
k = num = int(input())

for i in str:
    if i.isdigit():
        k -= 1
        if k == 0:
            print('Цифра под номером', num, 'это', i)
