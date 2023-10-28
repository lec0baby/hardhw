import pytest
from dz4.ex4_2 import fact


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
def test(n, result):
    assert fact(n) == result
