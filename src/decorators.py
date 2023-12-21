from time import time


def timer(func):
    def wrapper(n, *args, **kwargs):
        t1 = time()
        res = func(n, *args, **kwargs)
        t2 = time()
        meta_data = {
            "func_name": func.__name__,
            "seconds": round(t2 - t1, 4),
            "n": n,
        }
        return res, meta_data

    return wrapper
