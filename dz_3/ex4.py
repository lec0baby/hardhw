#from ex1 import func
from collections import Counter 

#ls = func(input())
ls = ['a', 'a', 'b', 1, 1, 2, 3, 3, 3]
a = dict(Counter(ls))

print(a)
