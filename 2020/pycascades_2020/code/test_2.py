from triangle import triangle_type


def test_type():
    many_triangles = [
        (90, 60, 30, "right"),
        (100, 40, 40, "obtuse"),
        (60, 60, 60, "acute"),
        (0, 0, 0, "invalid")
    ]
    for a, b, c, expected in many_triangles:
        assert triangle_type(a, b, c) == expected


