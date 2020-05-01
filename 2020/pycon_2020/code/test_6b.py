import csv
import pytest
from triangle import triangle_type

def many_triangles():
    with open('triangle_data.csv') as csvfile:
        for a, b, c, expected in csv.reader(csvfile):
            yield (int(a), int(b), int(c), expected)

@pytest.mark.parametrize( 'a, b, c, expected', many_triangles())
def test_func(a, b, c, expected):
    assert triangle_type(a, b, c) == expected


