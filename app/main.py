import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}
    functools.wraps(func)

    def wrapper(*args) -> int:

        if args not in cache_results:
            print("Calculating new result")
            result = func(*args)
            cache_results[args] = result
            return result

        print("Getting from cache")
        return cache_results[args]

    return wrapper
