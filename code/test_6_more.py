import pytest
from triangle import triangle_type

triangles = [
    (178,  1,  1, "obtuse"), # big angles
    (  1, 1, 178, "obtuse"), # different order
    ( 91, 44, 45, "obtuse"), # just over 90
    (0.01, 0.01, 179.98, "obtuse"), # decimals work?

    (90, 60, 30, "right"), # check 90 for each angle
    (10, 90, 80, "right"),
    (85,  5, 90, "right"),

    (89, 89,  2, "acute"), # just under 90
    (60, 60, 60, "acute"),

    (0, 0, 0, "invalid"),     # zeros
    (90, 90, 90, "invalid"),  # sum > 180
    (180, 0, 0, "invalid"),   # more zeros
    (61, 60, 60, "invalid"),  # sum > 180
    (90, 91, -1, "invalid"),  # negative numbers
]

@pytest.mark.parametrize('a, b, c, expected', triangles)
def test_type(a, b, c, expected):
    assert triangle_type(a, b, c) == expected

