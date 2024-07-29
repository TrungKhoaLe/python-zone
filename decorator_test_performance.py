from functools import wraps
import tracemalloc
from time import perf_counter


def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f"Function: {func.__name__}")
        print(f"Method: {func.__doc__}")
        print(f"Memory usage: \t\t {current / 10**6:.6f} MB \n"
              f"Peak memory usage: \t {peak / 10**6:.6f} MB ")
        print(f"Time elapsed: {finish_time - start_time:.6f}")
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list_1():
    """Range"""
    my_list = list(range(100_000))


@measure_performance
def make_list_2():
    """List comprehension"""
    my_list = [l for l in range(100_000)]


@measure_performance
def make_list_3():
    """Append"""
    my_list = []
    for item in range(100_000):
        my_list.append(item)


@measure_performance
def make_list_4():
    """Concatenation"""
    my_list = []
    for item in range(100_000):
        my_list = my_list + [item]


if __name__ == "__main__":
    make_list_1()
    make_list_2()
    make_list_3()
    make_list_4()
