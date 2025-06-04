from math import factorial

FAST_FACTORIAL = [factorial(_) for _ in range(10)]

factorial_chain = {}


def digit_factorial(n):
    return sum([FAST_FACTORIAL[int(_)] for _ in str(n)])


ct = 0
for i in range(1, 1000000):
    df = digit_factorial(i)
    this_chain = {i}
    while df not in this_chain:
        this_chain.add(df)
        factorial_chain[df] = df = digit_factorial(df)  # right most is the value. assign order from left to right
    if len(this_chain) > 59:
        print(i, len(this_chain), this_chain)
        ct += 1
print(ct, factorial_chain)
