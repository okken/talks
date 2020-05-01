import pytest
from triangle_fixed import triangle_type

smoke = pytest.mark.smoke

many_triangles = [
    pytest.param(90, 60, 30, "right", marks=smoke),
    pytest.param(100, 40, 40, "obtuse", marks=smoke),
    (60, 60, 60, "acute"),
    pytest.param(0, 0, 0, "invalid", id='zeros'),
]


@pytest.mark.parametrize('a, b, c, expected', many_triangles)
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected



