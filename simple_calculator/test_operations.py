from operations import addition, subtraction, multiplication


def test_addition():
    assert addition(3, 2) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0


def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(0, 5) == -5
    assert subtraction(-1, -1) == 0


def test_multiplication():
    assert multiplication(4, 3) == 12
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0
