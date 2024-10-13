import typing

@typing.overload
def add(*v: typing.Union[int, float]) -> float: ...
def add(*v: float) -> float: ...
def pi(n_terms: int = ..., use_accuracy: bool = ...) -> float:
    """
    Returns the value of pi (π).

    Done by dividing the circumference of a circle by its diameter.

    :arg n_terms: int - The number of terms to use in the approximation. Default is 100_000_000.
    :arg use_accuracy: bool -
    If True, the function will use the number of terms to approximate pi. Default is False, which return a constant
    value of pi at 50 decimal places.
    """
    ...

def e(n_terms: int = ..., use_accuracy: bool = ...) -> float:
    """
    Returns the value of Euler's number (e).

    Done by taking the limit of (1 + 1/n)^n as n approaches infinity.

    :arg n_terms: int - The number of terms to use in the approximation. Default is 100_000_000.
    :arg use_accuracy: bool -
    If True, the function will use the number of terms to approximate e. Default is False, which return a constant
    value of e at 50 decimal places.
    """
    ...

def factorial(n: int) -> int:
    """
    Returns the factorial of a number.

    Done by multiplying all positive integers up to the number.

    :arg n: int - The number to find the factorial of.
    """
    ...

def integral(
    f: typing.Callable[[float], float], a: float, b: float, n: int = ...
) -> float:
    """
    Approximates the integral of a function.

    :param f: The function to find the integral of.
    :param a: The lower bound of the integral.
    :param b: The upper bound of the integral.
    :param n: The number of subintervals to use in the approximation.
    :return: The approximate integral of the function.
    """
    ...

def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.

    :param n: The index of the Fibonacci number to find.
    :return: The nth Fibonacci number.
    """
    ...

def vector_sum(*v: typing.Union[int, float]) -> float:
    """
    Returns the sum of a list of numbers.

    :param v: The numbers to sum.
    :return: The sum of the numbers.
    """
    ...
