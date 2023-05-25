"""
This module provides a Calculator class for performing arithmetic operations.
"""

from common.constants import ERROR_VALUE
from arithmetic.sum import add
from arithmetic.product import multiply

class Calculator:
    """
    A class representing a calculator.

    Attributes:
        name (str): The name of the calculator.
        error (float): The error value used for indicating errors.

    Methods:
        add_positive(num1, num2): Adds two positive numbers.
        multiply_positive(num1, num2): Multiplies two positive numbers.
    """

    def __init__(self):
        """
        Initializes a new instance of the Calculator class.
        Sets the name attribute to "Positive calculator" and the error attribute to ERROR_VALUE.
        """
        self.name = "Positive calculator"
        self.error = ERROR_VALUE

    def add_positive(self, num1, num2):
        """
        Adds two positive numbers.

        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.

        Returns:
            float: The sum of the two numbers if both are positive, else returns the error value.

        Examples:
            >>> calc = Calculator()
            >>> calc.add_positive(3, 4)
            7.0
            >>> calc.add_positive(-2, 5)
            -1.0
        """
        if num1 > 0 and num2 > 0:
            return add(num1, num2)
        else:
            return self.error

    def multiply_positive(self, num1, num2):
        """
        Multiplies two positive numbers.

        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.

        Returns:
            float: The product of the two numbers if both are positive, else returns the error value.

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply_positive(2, 3)
            6.0
            >>> calc.multiply_positive(-4, 2)
            -1.0
        """
        if num1 > 0 and num2 > 0:
            return multiply(num1, num2)
        else:
            return self.error
