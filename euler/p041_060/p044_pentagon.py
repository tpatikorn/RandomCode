# a lot of math on paper to make it faster. mainly reverse pentagon function
# and function calculating the j pentagon from i
# specifically we need 4 pentagons
# i j x y
# px - pj = pi
# px + pj = py
# the answer is at i = 1992

import math


def pentagon(n):
    return (n * (3 * n - 1)) >> 1


def reverse_pentagon(n):
    return (1 + math.sqrt(1 + 24 * n)) / 6


# function returning the difference between pentagon(n) and pentagon(n + a)
def pentagon_diff(a):
    return lambda n: a * (6 * n + 3 * a - 1) / 2


def pentagon_sum(a):
    return lambda n: (6 * n * n + 6 * n * a + 3 * a * a - 2 * n - a) / 2


def find(start=2, end=10000):
    for i in range(start, end):
        for a in range(1, 2000):
            j = (3 * i * i - i + a - 3 * a * a) / (6 * a)
            if j > 0 and j.is_integer():
                j = int(j)
                x = j + a
                py = pentagon(j) + pentagon(x)
                if reverse_pentagon(py).is_integer():
                    return i, j, x, int(reverse_pentagon(py))
                if py < pentagon(x + 1):
                    break


result = find()
print(result)
print([pentagon(r) for r in result])
