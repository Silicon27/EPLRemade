"""
Derivative of a function.

To create a function, use the `Function` class provided via the `function` module.

Not done!
"""

from function import Function
import re


class Derivative:
    """
    This class is used to represent the derivative of a function.
    """

    def __init__(self, function: Function):
        self.function = function
        self.derivative = None

    def calculate(self):
        """
        This method is used to calculate the derivative of the function.

        note NOT DONE!
        """

        def split_function():

            pattern = r"\b\d*[a-zA-Z]\^\d+\b|\b\d+[a-zA-Z]\b|[+-]"

            matches = re.findall(pattern, self.function.function)
            if matches[-1] in ["+", "-"]:
                del matches[-1]

            return matches

        # Derivatives of standalone variables without coefficients/exponents is 1
        if self.function.function.isalpha():
            self.derivative = "1"
            return

        # Derivatives of constants is 0
        if self.function.function.isdigit():
            self.derivative = "0"
            return

        result = list()
        for j, i in enumerate(split_function()):
            if any(char.isalpha() for char in i):
                # if i[-1] == "^":
                #     result.append(i[:-1] + str(int(i[-1]) - 1))
                # else:
                #     result.append(i[:-1] + "^" + i[-1] + i[-1])
                pass


class Sderive:
    """
    Single derivative aka, derivative for a single term.
    """

    def __init__(self, function: Function):
        self.function = function
        self.derivative = None

    def calculate(self):
        if self.function.function.isalpha():
            self.derivative = "1"
            return

        if self.function.function.isdigit():
            self.derivative = "0"
            return

        if "^" not in self.function.function:
            self.derivative = re.sub(r"[a-zA-Z]", "", self.function.function)
            return
        else:
            # get where a character is in a string
            positions = [
                pos for pos, char in enumerate(self.function.function) if char == "^"
            ]

            # get the variable before the "^"
            var = self.function.function[positions[0] - 1]

            # The exponent is the rest of the string after the "^"
            exponent = self.function.function[positions[0] + 1 :]

            try:
                # Get the coefficient
                if self.function.function[positions[0] - 2] == "-":
                    coefficient = -int(self.function.function[: positions[0] - 1])

                if self.function.function == "":
                    coefficient = 1
                else:
                    coefficient = int(self.function.function[: positions[0] - 1])
            except Exception as e:
                coefficient = 1

            if int(exponent) - 1 == 1:
                self.derivative = f"{coefficient * int(exponent)}{var}"
                return

            if int(exponent) == 0:
                self.derivative = "0"
                return

            self.derivative = f"{coefficient * int(exponent)}{var}^{int(exponent) - 1}"
            return

    def __repr__(self):
        return str(self.derivative)


myfunc = Function("x^2")  # derivative is 6x

myderivative = Sderive(myfunc)

myderivative.calculate()

print(myderivative)
