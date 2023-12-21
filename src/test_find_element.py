from random import choice, randint

from decorators import timer


@timer
def f_slow(n: int, arr: list[int], element: int) -> int:
    for i, el in enumerate(arr):
        if el == element:
            return i
    return -1


@timer
def f_fast(n: int, arr: list[int], element: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == element:
            return middle
        elif arr[middle] > element:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def generate_data(upper_border: int):
    data = []
    arr = []
    for _ in range(0, upper_border + 1, 10_000):
        arr.extend([randint(0, 10_000_000) for _ in range(10_000)])
        arr = sorted(set(arr))
        element = choice(arr[-10_000:])
        len_arr = len(arr)
        print(len_arr)
        fast_res, fast_meta = f_fast(len_arr, arr, element)
        slow_res, slow_meta = f_slow(len_arr, arr, element)
        data.append(fast_meta)
        data.append(slow_meta)
        assert fast_res == slow_res
    return data
