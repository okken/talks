import pytest
from triangle import triangle_type

many_triangles = [
    (100, 40, 40, "obtuse"),
    ( 60, 60, 60, "acute"),
    ( 90, 60, 30, "right"),
    (  0,  0,  0, "invalid"),
]

@pytest.mark.parametrize('a, b, c, expected', many_triangles)
def test_type(a, b, c, expected):
    assert triangle_type(a, b, c) == expected

