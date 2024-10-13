import time
from typing import Callable


def scache(maxsize=10):
    """
    Creates a simple cache for a function.

    Max size is the maximum size the cache can become (i.e., 10 indexes, 2 indexes, etc.) in terms of the number of indexes to store in the cache.

    Example usage:

    @scache(maxsize=10)
    def loop(n: int) -> int:
        for i in range(n):
            n += i
        return n


    print(loop(100000000))
    print(loop(100000000))
    print(loop(100000000))

    :param maxsize:
    :return:
    """

    def wrapper(func, *args, **kwargs):
        cache = {}

        def inner(*args, **kwargs):
            if args in cache:
                return cache[args]
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                cache.popitem()
            cache[args] = result
            return result

        return inner

    return wrapper


class TTLCache:
    def __init__(self, ttl: int = 60, maxsize: int = 10, when: bool = False) -> None:
        """
        A simple time-to-live cache for a function.

        The cache will store the result of a function for a certain amount of time before it expires.

        Example usage:

        @TTLCache(ttl=1, when=True)
        def loop(n: int) -> int:
            for i in range(n):
                n += i
            return n

        print(loop(100000000))
        print(loop(100000000))
        time.sleep(2)
        print(loop(100000000))

        :param ttl: int - The time-to-live of the cache in seconds. Default is 60.
        :param maxsize: int - The maximum size of the cache. Default is 10.
        :param when: bool - If True, the cache will print a message when it expires. Default is False.
        """

        self.cache = {}
        self.setttl = ttl  # Set TTL # NOQA
        self.maxsize = maxsize
        self.timestamps = {}
        self.when = when

    def __call__(self, func) -> Callable[..., int]:
        def wrapper(*args, **kwargs):
            if len(self.cache) >= self.maxsize:
                oldest_key = min(self.timestamps, key=self.timestamps.get)
                self.cache.pop(oldest_key)
                self.timestamps.pop(oldest_key)

            # If function is already timestamped and the time has expired
            try:
                if time.time() - self.timestamps[args] > self.setttl:
                    del self.cache[args]
                    del self.timestamps[args]
                    if self.when:
                        print("Cache expired")
                    return func(*args, **kwargs)
            except KeyError:
                pass

            # If function has not been called before
            if args not in self.cache:
                result = func(*args, **kwargs)
                self.cache[args] = result
                self.timestamps[args] = time.time()
                return result
            else:
                return self.cache[args]

        return wrapper
