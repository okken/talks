from triangle import triangle_type

def test_right():
    assert triangle_type(90, 60, 30) == "right"


def test_obtuse():
    assert triangle_type(100, 40, 40) == "obtuse"


def test_acute():
    assert triangle_type(60, 60, 60) == "acute"


def test_invalid_zeros():
    assert triangle_type(0, 0, 0) == "invalid"


def test_invalid_too_big():
    assert triangle_type(90, 90, 90) == "invalid"
