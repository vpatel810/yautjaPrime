import math


def power(base: float, exponent: float) -> float:
    """
    Calculate the power of a number.

    Args:
        base (float): The base number.
        exponent (float): The exponent to raise the base to.

    Returns:
        float: The result of base raised to the power of exponent.
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative number.")
    return math.pow(base, exponent)


def square_root(number: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        number (float): The number to find the square root of.

    Returns:
        float: The square root of the number.
    """
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(number)
