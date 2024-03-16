import pytest
from mtr import Matrix, Matrix3x3

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
    mocker.patch('builtins.input', side_effect=['2', '3', '1 2 3', '4 5 6'])
    matrix = Matrix()
    matrix.input_matrix()
    assert matrix.rows == 2
    assert matrix.columns == 3
    assert matrix.elements == [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
        
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
    
@pytest.mark.parametrize(
        ('elements', 'result'),
        [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
        ([[3, 3, 3], [3, 3, 3], [3, 3, 3]], 0),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0),
        ([[8, 9, 2], [7, 2, 8], [1, 6, 4]], -420.0),
        ([[17, 7, 1], [9, 10, 4], [3, 13, 18]], 1213.0),
        ([[9.7, 6.3, 1.2], [5.2, 11.9, 7.4], [6.4, 3.1, 1.1]], 94.739)
        ]
)

def test_determinant(elements, result):
    m = Matrix3x3(elements)
    assert m.determinant() == result

def test_init_3x3():
    m = Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert m.rows == 3
    assert m.columns == 3
    assert m.elements == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    
def test_input_3x3(mocker):
    mocker.patch('builtins.input', side_effect = ['1 2 3', '4 5 6', '7 8 9'])
    matrix = Matrix3x3()
    matrix.input_matrix()
    assert matrix.rows == 3
    assert matrix.columns == 3
    assert matrix.elements == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix.determinant() == 0

@pytest.mark.xfail(raises=ValueError)
def test_elements_3x3():
    Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1, 1]])

@pytest.mark.parametrize(
        ('rows', 'columns', 'el1', 'el2', 'result'),
        [
        (3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]),
        (2, 2, [[2, 3], [1, 4]], [[5, 7], [3, 8]], [[7, 10], [4, 12]]),
        (4, 2, [[1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1]], [[2, 2], [2, 2], [2, 2], [2, 2]])
        ]
)

def test_add(rows, columns, el1, el2, result):
    assert Matrix(rows, columns, el1) + Matrix(rows, columns, el2) == Matrix(rows, columns, result)

@pytest.mark.parametrize( 
        ('rows', 'columns', 'el1', 'el2', 'result'),
        [
        (3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        (2, 2, [[2, 3], [1, 4]], [[5, 7], [3, 8]], [[-3, -4], [-2, -4]]),
        (4, 2, [[1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [0, 0], [0, 0], [0, 0]])
        ]
)

def test_sub(rows, columns, el1, el2, result):
    assert Matrix(rows, columns, el1) - Matrix(rows, columns, el2) == Matrix(rows, columns, result)
    
@pytest.mark.xfail(raises=ValueError)
def test_add_sub_errors():
    m1 = Matrix(2, 2, [[1, 1], [1, 1]])
    m2 = Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert m1 + m2
    assert m1 - m2
    assert m1 + 2
    assert m2 - 2

@pytest.mark.xfail(raises=ValueError)
def test_add_sub_errors_3x3():
    m1 = Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    m2 = Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert m1 + 2
    assert m2 - 2