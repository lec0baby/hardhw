import pytest
from general.ex4_2 import fact


@pytest.mark.parametrize(
    ('n', 'result'),
    [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1)
    ]
)
def test(n, result):
    assert fact(n) == result