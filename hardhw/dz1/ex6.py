#n1 = float(input())
#if n1 % 1 == 0:
#    print('Целое')
#else:
#    print('Дробное')
num = input()
if '.' not in num:
    num = num + '.0'
spl = num.split('.')
num1 = '.'.join(spl[1:])
if int(num1) == 0:
    print('Целое')
else:
    print('Дробное')