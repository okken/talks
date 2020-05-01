import csv
import pytest
from triangle import triangle_type

def many_triangles():
    with open('triangle_data.csv') as csvfile:
        for a, b, c, expected in csv.reader(csvfile):
            yield (a, b, c, expected)

@pytest.fixture()
def int_convert(request):
    return int(request.param)

@pytest.fixture()
def a(request):
    return int(request.param)

@pytest.fixture()
def b(request):
    return int(request.param)

@pytest.fixture()
def c(request):
    return int(request.param)

@pytest.mark.parametrize('a, b, c, expected', many_triangles(),
                         indirect=['a', 'b', 'c'])
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected


