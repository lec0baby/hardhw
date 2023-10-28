import pytest
from dz4.ex4_1 import move

@pytest.mark.parametrize(
    ('k', 'pos', 'result'),
    [
        (2, [1, 2, 3, 4, 5], [4, 5, 1, 2, 3]),
        (3, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        (0, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (7, [1, 2, 3, 4, 5], [4, 5, 1, 2, 3]),
    ]
)

def test(k, pos, result):
    assert move(k, pos) == result