def triangle_type(a, b, c):
    """
    Given three angles,
    return 'obtuse', 'acute', 'right', or 'invalid'.
    """
    angles = (a, b, c)
    if (sum(angles) == 180 and
        all([0 < a < 180 for a in angles])):
        if 90 in angles:
            return "right"
        if any([a > 90 for a in angles]):
            return "obtuse"
        if all([a < 90 for a in angles]):
            return "acute"
    return "invalid"




