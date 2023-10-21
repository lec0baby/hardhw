import pytest
from dz4.ex4_3 import check

@pytest.mark.parametrize(
    ('x'),
    [
        ([1, 2, 'Hi', False]),
        ({1, 3, 'Bye', False}),
        ('true')
    ]
)

def test_true(x):
    assert check(x) is True
    
@pytest.mark.parametrize(
    ('x'),
    [
        ([1, 2, 3, 4, 1]),
        ([1, 2, 2, 3, 'OO']),
        ('Hello')
    ]
)

def test_false(x):
    assert check(x) is False