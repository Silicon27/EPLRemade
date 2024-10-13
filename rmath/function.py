"""
function.py - This file contains the function class which is used to represent a function in the rmath library.
"""


class Function:
    """
    This class is used to represent a function in the rmath library.
    """

    def __init__(self, function: str):
        self.function = function

    def __str__(self):
        return f"Function({self.function})"

    def __repr__(self):
        return str(self.function)
