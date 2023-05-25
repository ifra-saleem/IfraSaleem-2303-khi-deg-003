"""
This module provides a function for adding two numbers.
"""

def add(a, b):
    """
    Adds two numbers and returns their sum as a float.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float: The sum of the two numbers.

    Examples:
        >>> add(3, 4)
        7.0
        >>> add(2.5, 1.5)
        4.0
    """
    return float(a + b)
