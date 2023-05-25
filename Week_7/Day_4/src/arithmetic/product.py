"""
This module provides a function for multiplying two numbers.
"""

def multiply(a, b):
    """
    Multiplies two numbers and returns their product as a float.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float: The product of the two numbers.

    Examples:
        >>> multiply(2, 3)
        6.0
        >>> multiply(-4, 2)
        -8.0
    """
    return float(a * b)
