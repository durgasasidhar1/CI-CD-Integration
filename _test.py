import pytest

def square(n):
    """Returns the square of a number."""
    return n * n

def cube(n):
    """Returns the cube of a number."""
    return n ** 3

def fith_power(n):
    """Returns the fifth power of a number."""
    return n ** 5

def test_square():
    assert square(2) == 4, "Test failed: Square of 2 should be 4 "

    assert square(3) == 9, "Test failed: Square of 3 should be 9"

def test_cube():
    assert cube(2) == 8, "Test failed: Cube of 2 should be 8"

    assert cube(3) == 27, "Test failed: Cube of 3 should be 27"

def test_fith_power():
    assert fith_power(2) == 32, "Test failed: Fifth power of 2 should be 32"

    assert fith_power(3) == 243, "Test failed: Fifth power of 3 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("a")