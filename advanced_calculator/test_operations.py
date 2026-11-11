import pytest
from operations import power, square_root

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    with pytest.raises(ValueError):
        power(2, -1)


def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(0) == 0
    with pytest.raises(ValueError):
        square_root(-1)
