import pytest
from matrix_pew_pew.mtr import Matrix

def test_init():
    m = Matrix(2, 2, [[1, 1],[1, 1]])
    assert m.rows == 2
    assert m.columns == 2
    assert m.elements == [[1, 1],[1, 1]]
    m1 = Matrix()
    assert m1.rows == 0
    assert m1.columns == 0
    assert m1.elements == []