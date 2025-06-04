import math
n = 0
for i in range(1, 100000):
    n = n + i
    c = 0
    for _ in range(1, math.floor(math.sqrt(n))):
        if n % _ == 0:
            c = c + 2
    if c > 500:
        print(i, n, c)
        break
