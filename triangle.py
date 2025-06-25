def is_triangle(a, b, c):
    """Returns True if a, b, c can form a triangle."""
    return a + b > c and a + c > b and b + c > a
