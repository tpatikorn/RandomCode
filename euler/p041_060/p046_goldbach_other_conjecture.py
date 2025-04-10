from euler import util
import math

primes = util.get_prime_list(limit=1000000)

for i in range(1000):
    for j in range(i + 1, 1000):
        composite = 4 * i * j + 2 * i + 2 * j + 1
        for p in primes:
            if p > composite:  # if it doesn't break before p > composite, there's no combination
                print("composite", composite)
                break
            if math.sqrt((composite - p) / 2).is_integer():
                break
