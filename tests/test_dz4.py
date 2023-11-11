import pytest
from dz4.ex4_1 import move
from dz4.ex4_2 import fact
from dz4.ex4_3 import is_unique

# the first task
@pytest.mark.parametrize(
    ('k', 'pos', 'result'),
    [
        (2, [1, 2, 3, 4, 5], [4, 5, 1, 2, 3]),
        (3, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        (0, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (7, [1, 2, 3, 4, 5], [4, 5, 1, 2, 3]),
    ]
)

def test_move(k, pos, result):
    assert move(k, pos) == result

# the second task
@pytest.mark.parametrize(
    ('n', 'result'),
    [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
        (-1, 'Не существует')
    ]
)
def test_fact(n, result):
    assert fact(n) == result

# the third task
@pytest.mark.parametrize(
    ('x'),
    [
        ([1, 2, 'Hi', False]),
        ({1, 3, 'Bye', False}),
        ('true'),
        ([1, True])
    ]
)

def test_unique_true(x):
    assert is_unique(x) is True
    
@pytest.mark.parametrize(
    ('x'),
    [
        ([1, 2, 3, 4, 1]),
        ([1, 2, 2, 3, 'OO']),
        ('Hello')
    ]
)

def test_unique_false(x):
    assert is_unique(x) is False