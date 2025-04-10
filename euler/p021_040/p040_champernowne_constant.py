import functools

x = functools.reduce(lambda a, b: a + b, [str(i) for i in range(1, 200000)])
print(functools.reduce(lambda a, b: a * b, [int(x[10 ** i - 1]) for i in range(0, 7)]))
