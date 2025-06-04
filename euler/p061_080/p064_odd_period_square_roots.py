import math
from typing import List


def square_root_continued_fraction(n: int, max_iter=10000):
    # the format is b / sqrt(23) - c --> d + sqrt(23) - e / f
    a0 = math.floor(math.sqrt(n))
    b0 = 1
    c0 = math.floor(math.sqrt(n))
    a, b, c = a0, b0, c0
    history = []

    for i in range(1, max_iter):
        f = (n - c * c) / b  # 7
        d = math.floor((math.sqrt(n) + c) / f)
        e = d * f - c  # 1 * 7 - 4 = 3
        this_iter = [a, b, c, d, e, f]
        if this_iter in history:
            start = history.index(this_iter)
            end = len(history)
            period = end - start
            print(f"n={n}, period={period}")
            return period
        history.append(this_iter)
        a = d  # 1
        b = f  # 7
        c = e  # 3


count_odd_period = 0
for i in range(1, 10_000):
    try:
        this_period = square_root_continued_fraction(i)
        if this_period % 2 == 1:
            count_odd_period += 1
    except ZeroDivisionError:
        print("bad i", i)
print(count_odd_period)