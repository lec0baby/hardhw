from ex1 import frik`
from collections import defaultdict

print('Элемент | Частота')
elements = frik(input())

ans = defaultdict(int)

for el in elements:
    ans[el] += 1

print(*[f'{i} | {ans[i]}' for i in ans], sep = '\n')