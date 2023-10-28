import pytest
from dz4.ex4_3 import is_unique

@pytest.mark.parametrize(
    ('x'),
    [
        ([1, 2, 'Hi', False]),
        ({1, 3, 'Bye', False}),
        ('true'),
        ([1, True])
    ]
)

def test_true(x):
    assert is_unique(x) is True
    
@pytest.mark.parametrize(
    ('x'),
    [
        ([1, 2, 3, 4, 1]),
        ([1, 2, 2, 3, 'OO']),
        ('Hello')
    ]
)

def test_false(x):
    assert is_unique(x) is False