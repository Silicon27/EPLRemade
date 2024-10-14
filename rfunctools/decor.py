import time
from customerrors import (
    TimeoutError,
    RetryError,
    DebounceError,
    ArgumentNotAllowed
)
from typing import Callable, Any, List, Dict, Union

def timeout(seconds: int = 10) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.time()
            result = func(*args, **kwargs)
            if time.time() - start > seconds:
                raise TimeoutError(
                    f"Function `{func.__name__}` exceeded {seconds} seconds"
                )
            return result

        return wrapper

    return decorator

def retry(attempts: int = 3, delay: float = 1) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception: {e}")
                    time.sleep(delay)
            raise RetryError(
                f"Function `{func.__name__}` failed after {attempts} attempts"
            )

        return wrapper

    return decorator

def debounce(delay: float = 1) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        last_invocation: float = 0

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_invocation
            if time.time() - last_invocation > delay:
                last_invocation = time.time()
                return func(*args, **kwargs)
            raise DebounceError(
                f"Function `{func.__name__}` invoked before {delay} seconds"
            )

        return wrapper

    return decorator

def check_args(check_for: Union[List[Any], None] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Not well tested, use with caution.

    Checks for values in arguments that are not allowed.

    :param check_for: List of values to check for in arguments
    :return: Decorated function
    """
    if check_for is None:
        check_for = []

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Dict[str, Any]) -> Any:
            def check_args_for(check_arg: Any) -> None:
                for iarg in check_for:
                    if iarg == check_arg:
                        raise ArgumentNotAllowed(
                            f"Value `{iarg}` not allowed in function `{func.__name__}` as an argument"
                        )

            for arg in args:
                if isinstance(arg, dict):
                    for value in arg.values():
                        check_args_for(value)
                elif isinstance(arg, list):
                    for value in arg:
                        check_args_for(value)
                else:
                    check_args_for(arg)

            for _, value in kwargs.items():
                check_args_for(value)

            return func(*args, **kwargs)

        return wrapper

    return decorator


# @retry(attempts=5, delay=1)
# def unreliable_function():
#     import random
#     if random.choice([True, False]):
#         return "Success"
#     else:
#         raise Exception("Failure")
#
# unreliable_function()
#
#
# @timeout(2)
# def slow_function():
#     time.sleep(1)
#     print("Function completed")
#
# slow_function()
#
#
# @debounce(delay=2)
# def debounce_function():
#     print("Function invoked")
#
# debounce_function()
# time.sleep(2)
# debounce_function()
#
#
# @check_args(check_for=[1, 2])
# def check_args_function(a, b):
#     return a + b
#
# print(check_args_function(3, 4))
