import pytest
from triangle_fixed import triangle_type


many_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid"),
]


@pytest.fixture()
def expected(request):
    if request.param == 'obtuse':
        print('\nthis is one of the obtuse cases')
    return request.param


@pytest.mark.parametrize('a, b, c, expected', many_triangles,
                         indirect=['expected'])
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected


