import pytest
from dz_8.ex8_1 import bubble_sort
from dz_8.ex8_1 import quick_sort
from dz_8.ex8_1 import stalin_sort

@pytest.mark.parametrize(
    ('start', 'end'),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
        ([5, 1, 4, 2, 3], [1, 2, 3, 4, 5]),
        ([2, 1], [1, 2])
    ]
)

def test_bubble_sort(start, end):
    assert bubble_sort(start) == end


@pytest.mark.parametrize(
    ('start1', 'end1'),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
        ([5, 1, 4, 2, 3], [1, 2, 3, 4, 5]),
        ([2, 1], [1, 2])
    ]
)

def test_quick_sort(start1, end1):
    assert quick_sort(start1) == end1
    

@pytest.mark.parametrize(
    ('start2', 'end2'),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1]),
        ([1, 2, 4, 3, 5], [1, 2, 3, 5]),
        ([5, 1, 4, 2, 3], [1, 2, 3]),
        ([2, 1], [1]),
        ([1, 2], [1, 2])
    ]
)

def test_stalin_sort(start2, end2):
    assert stalin_sort(start2) == end2