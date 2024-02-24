import pytest
from mtr import Matrix

@pytest.mark.parametrize(
        ('rows', 'columns', 'elements'),
        [
        (2, 2, [[1, 1],[1, 1]])
        ]
)

def test_init(rows, columns, elements):
    m = Matrix(rows, columns, elements)
    assert m.rows == rows
    assert m.columns == columns
    assert m.elements == elements
    
def test_init_default():
    m1 = Matrix()
    assert m1.rows == 0
    assert m1.columns == 0
    assert m1.elements == []

def test_input(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '3', '1 2 3', '4 5 6'])
    matrix = Matrix()
    matrix.input_matrix()
    assert matrix.rows == 2
    assert matrix.columns == 3
    assert matrix.elements == [[1, 2, 3], [4, 5, 6]]
        
@pytest.mark.xfail(raises=ValueError)
def test_much_el(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '3', '1 2 3', '4 5 6 7'])
    matrix = Matrix()
    matrix.input_matrix()
    
@pytest.mark.parametrize(
        ('rows1', 'columns1', 'elements1', 'result'),
        [
        (2, 4, [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]], '1.0 1.0 1.0 1.0\n1.0 1.0 1.0 1.0\n'),
        (2, 3, [[3.14, 1.0, 1.0], [1.0, 1.0, 3.14]], '3.14 1.0 1.0\n1.0 1.0 3.14\n')
        ]
)

def test_output(rows1, columns1, elements1, result):
    assert str(Matrix(rows1, columns1, elements1)) == result