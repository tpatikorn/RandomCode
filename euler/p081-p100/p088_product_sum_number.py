import math

factors = {1: {1}}

for i in range(2, 24001):
    factors[i] = set()
    for j in range(1, math.isqrt(i) + 1):
        if i % j == 0:
            factors[i].add(j)
            factors[i].add(i // j)

print(factors)

for prod in factors:
    print(prod)
