"""
Created on Jul 22, 2020

@author: toni
"""

from functools import wraps
import time

# def PrintTimeit(func):
#     """This decorator prints the execution time for the decorated function."""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         times_ = []
#         for i in range(1, 13):
#             start = time.time()
#             try:
#                 result = func(*args, **kwargs)
#             finally:
#                 end = time.time()
#                 times_.append(end-start)
#         average_time = round(sum(times_)/i, 5)
#         print("{} ran {} times with an average runtime of {}s".format(
#             func.__name__, i, average_time))
#         return result
#     return wrapper


def PrintTimeit(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
        finally:
            end = time.time()
            print(f"{func.__name__} ran in {round(end - start, 5)}s")
        return result

    return wrapper


@PrintTimeit
def slower_func():
    list_ = [[i * j for j in range(2 ** 12)] for i in range(2 ** 12)]

    return list_


def main():
    slower_func()


if __name__ == "__main__":
    main()
