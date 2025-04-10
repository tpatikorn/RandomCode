import math
from euler import util

best_n = 2
best = 1
for i in util.get_prime_list(limit=1000):
    if i % 2 == 0 or i % 5 == 0:
        continue  # because 2 and 5 will always remain on top of 1/99...99
    base = 9
    while True:
        if base % i == 0:
            this = round(math.log(base, 10))
            if this > best:
                print("better!", i, this)
                best = this
                best_n = i
            break
        base = base * 10 + 9
print(best_n, best)
