import pytest
from triangle import triangle_type

@pytest.mark.parametrize( 'a, b, c, expected', [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")])
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected


