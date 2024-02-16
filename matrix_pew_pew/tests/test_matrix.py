import pytest
from mtr import Matrix

def test_init():
    m1 = Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    m2 = Matrix(2, 2, [[1, 1],[1, 1]])
    m3 = Matrix(3, 2, [[1, 1], [1, 1], [1, 1]])
    assert m1.rows == 3
    assert m1.elements == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert m2.columns == 2
    assert m2.elements == [[1, 1],[1, 1]]
    assert m3.rows == 3
    assert m3.columns == 2