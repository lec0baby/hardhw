from ex3_1 import frik
from collections import defaultdict

elements = frik(input())

ans = defaultdict(int)

for el in elements:
    ans[el] += 1

print('Элемент | Частота')
print(*[f'      {i} | {ans[i]}' for i in ans], sep = '\n')