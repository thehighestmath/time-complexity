from decorators import timer


@timer
def f_slow(n: int) -> int:
    def inner_f(n: int) -> int:
        if n < 2:
            return n
        return inner_f(n - 1) + inner_f(n - 2)
    return inner_f(n)


@timer
def f_fast(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def generate_data(upper_border: int):
    data = []
    arr = []
    for n in range(upper_border):
        print(n)
        fast_res, fast_meta = f_fast(n)
        slow_res, slow_meta = f_slow(n)
        data.append(fast_meta)
        data.append(slow_meta)
        assert fast_res == slow_res
    return data
