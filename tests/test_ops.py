from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(5,-7) == -2

def test_sub():
    assert sub(2,3) == -1
    assert sub(5,-7) == 12