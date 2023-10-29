import pytest 
from dz5.ex5_1 import binnary_search

@pytest.mark.parametrize(
   ('k', 'pos', 'result'),
   [
       (2, [1, 2, 3, 4, 5], 1),
       (-2, [-2, -1, 0, 1, 2, 3], 0),
       (0, [0, 0, 1, 2, 3, 4, 5], 0),
       (6, [6, 6, 6, 6, 6, 6, 6], 0),
       (-1, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 3),
       (-4, [-5, -4, -4, -4, 0, 1, 3], 1),
       (13, [1, 2, 3, 4, 4, 4, 6, 9, 13], 8),
       (7, [0, 1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7, 7, 10, 10, 11], 6)
   ] 
)

def test_binnary_search(k, pos, result):
    assert binnary_search(k, pos) == result