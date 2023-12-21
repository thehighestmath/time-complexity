from random import choice
from string import ascii_letters

from decorators import timer


@timer
def f_slow(n: int, s: list[str]) -> dict:
    d = {}
    for x in s:
        d[x] = s.count(x)
    return d


@timer
def f_fast(n: int, s: list[str]) -> dict:
    d = {}
    for x in s:
        d[x] = d.get(x, 0) + 1
    return d


def generate_data(upper_border: int):
    data = []
    arr = []
    for _ in range(0, upper_border + 1, 1_000):
        arr.extend([choice(ascii_letters) for _ in range(1_000)])
        len_arr = len(arr)
        print(len_arr)
        fast_res, fast_meta = f_fast(len_arr, arr)
        slow_res, slow_meta = f_slow(len_arr, arr)
        data.append(fast_meta)
        data.append(slow_meta)
        assert fast_res == slow_res
    return data
