"""
EPL (Every Python Library) - rmath

This module is a collection of functions that are used in the field of mathematics.

"""

from typing import overload, List


def add(*v):
    for i in v:
        if type(i) != int and type(i) != float:
            raise TypeError("All arguments must be integers or floats.")
    return sum(v)


def pi(n_terms=100_000_000, use_accuracy=False):
    """
    Returns the value of pi (π).

    Done by dividing the circumference of a circle by its diameter.

    :arg n_terms: int - The number of terms to use in the approximation. Default is 100_000_000.
    :arg use_accuracy: bool -
    If True, the function will use the number of terms to approximate pi. Default is False, which return a constant
    value of pi at 50 decimal places.
    """
    if use_accuracy:
        pi_approx = 0
        for i in range(n_terms):
            pi_approx += (-1) ** i / (2 * i + 1)
        return pi_approx * 4
    return 3.14159265358979323846264338327950288419716939937510


def e(n_terms=100_000_000, use_accuracy=False):
    """
    Returns the value of Euler's number (e).

    Done by taking the limit of (1 + 1/n)^n as n approaches infinity.

    :arg n_terms: int - The number of terms to use in the approximation. Default is 100_000_000.
    :arg use_accuracy: bool -
    If True, the function will use the number of terms to approximate e. Default is False, which return a constant
    value of e at 50 decimal places.
    """
    if use_accuracy:
        e_approx = 0
        for i in range(n_terms):
            e_approx += 1 / (i + 1)
        return e_approx
    return 2.71828182845904523536028747135266249775724709369995


def factorial(n):
    """
    Returns the factorial of a number.

    Done by multiplying all positive integers up to the number.

    :arg n: int - The number to find the factorial of.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Returns the nth term in the Fibonacci sequence.

    Done by adding the two previous terms to get the next term.

    :arg n: int - The term to find in the Fibonacci sequence.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def integral(func, a, b, n=1000):
    """
    Returns the integral of a function.

    Done by approximating the area under the curve of a function.

    :arg func: function - The function to find the integral of.
    :arg a: int - The lower limit of the integral.
    :arg b: int - The upper limit of the integral.
    :arg n: int - The number of rectangles to use in the approximation. Default is 1000.
    """
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        integral_sum += func(a + i * h) * h
    return integral_sum


def vector_sum(*vectors):
    """
    Returns the sum of vectors.

    Done by adding the corresponding components of each vector.

    :arg vectors: List[List[int]] - The vectors to sum.
    """
    counter = 0
    for vector in vectors:
        if not isinstance(vector, list):
            raise TypeError("All arguments must be lists.")

    return [sum(vector[i] for vector in vectors) for i in range(len(vectors[0]))]
