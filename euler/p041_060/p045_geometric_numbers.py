import math

for n in range(100000):
    k = (-2 * n - 1 + math.sqrt(12 * n * n - 4 * n + 1)) / 2
    if k.is_integer() and (n + k) % 2 == 1:
        print("triangle", n + k, (n + k) * (n + k + 1) / 2)
