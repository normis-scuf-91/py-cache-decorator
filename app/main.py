import functools
from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache_results = {}
    functools.wraps(func)

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_results:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_results[args] = result
            return result
        print("Getting from cache")
        return cache_results[args]

    return wrapper
