"""
EPL (Every Python Library) - rtype

This module is a collection of types that can be assigned to variables.
"""

class Callable:
    """
    This class is used to check if a variable is callable.

    :arg var: any - The variable to check if it is callable.
    """

    def __init__(self, var):
        self.var = var

    def __bool__(self):
        return callable(self.var)

    def __str__(self):
        return f"Callable({self.var})"

    def __repr__(self):
        return f"Callable({self.var})"

class Any:
    """
    This class is used to check if a variable is any.

    :arg var: any - The variable to check if it is any.
    """

    def __init__(self, var):
        self.var = var

    def __bool__(self):
        return True

    def __str__(self):
        return f"Any({self.var})"

    def __repr__(self):
        return f"Any({self.var})"

class Iterable:
    """
    This class is used to check if a variable is iterable.

    :arg var: any - The variable to check if it is iterable.
    """

    def __init__(self, var):
        self.var = var

    def __bool__(self):
        try:
            iter(self.var)
            return True
        except TypeError:
            return False

    def __str__(self):
        return f"Iterable({self.var})"

    def __repr__(self):
        return f"Iterable({self.var})"


class Number:
    """
    This class is used to check if a variable is a number.

    :arg var: any - The variable to check if it is a number.
    """

    def __init__(self, var):
        self.var = var

    def __bool__(self):
        return type(self.var) == int or type(self.var) == float

    def __str__(self):
        return f"Number({self.var})"

    def __repr__(self):
        return f"Number({self.var})"


class DictFuncs:
    """
    This type is for creating a dictionary with functions as values.

    Accessing the key of a DictFuncs object will run the function corresponding to the key.
    """

    def __init__(self, **kwargs):
        self.funcs = kwargs

    def __getitem__(self, key, *args):
        return self.funcs[key](*args)  # Run the function

    def __setitem__(self, key, value):
        self.funcs[key] = value

    def __delitem__(self, key):
        del self.funcs[key]

    def __str__(self):
        return f"DictFuncs({self.funcs})"


class ModFunc:
    """
    ModFunc is a class that takes a function and mod it with another function.
    """

    def __init__(self, func1, mod):
        self.func1 = func1
        self.mod = mod

    def __call__(self, *args):
        return self.mod(self.func1(*args))

    def __str__(self):
        return f"ModFunc({self.func1}, {self.mod})"


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(f):
    return f


p: Iterable = Iterable(12)
o: Number = Number(12)
i: DictFuncs = DictFuncs(a=lambda x: x + 1, b=lambda: 2)
k: ModFunc = ModFunc(add, sub)


print(o)
print(Number("a"))
print(i.__getitem__("a", 7))  # 2

print(p)
print(Iterable([1, 2, 3]))  # Iterable([1, 2, 3])
print(i)  # Iterable(12)
print(mul(k(1, 2)))  # (1, 2, 3, 4)

a = i
print(a)
