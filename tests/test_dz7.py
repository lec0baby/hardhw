import pytest
from dz7.ex7_1 import search_width


@pytest.mark.parametrize(
    ('g', 's', 't', 'forward'),
    [
        ({'A':[],'B':[]'C':[]}, 'A', 'C', None),
        ({'A':['B', 'C'], 'B':['A', 'D'], 'C':['A', 'D'], 'D':['B', 'C', 'E'], 'E':['D']}, 'A', 'E', 3),
        ({'A': ['B', 'C'], 'B':['D', 'F'], 'C':['D', 'E'], 'D':['E']}, 'A', 'A', 0) 
    ]
)

def test(g, s, t, forward):
    assert search_width(g, s, t) == forward