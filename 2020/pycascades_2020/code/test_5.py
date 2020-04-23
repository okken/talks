import pytest
from triangle import triangle_type


def many_triangles():
    return [ (90, 60, 30, "right"),
             (100, 40, 40, "obtuse"),
             (60, 60, 60, "acute"),
             (0, 0, 0, "invalid") ]

@pytest.mark.parametrize( 'a, b, c, expected', many_triangles())
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected


