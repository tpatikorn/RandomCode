import math
from math import gcd

# generating pythagorean triplets
# https://en.wikipedia.org/wiki/Pythagorean_triple

max_sum = 1_500_000

triplets = {}
for m in range(2, math.ceil(math.sqrt(max_sum))):
    for n in range(1, m):
        if gcd(m, n) > 1:
            continue
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        k = 1
        while a * k + b * k + c * k <= max_sum:
            triplet_sum = a * k + b * k + c * k
            if triplet_sum in triplets.keys():
                triplets[triplet_sum].add(frozenset([a * k, b * k, c * k]))
            else:
                triplets[triplet_sum] = {frozenset([a * k, b * k, c * k])}
            k += 1

unique_triplet = [_sum for _sum, _triplets in triplets.items() if len(_triplets) == 1]
print(unique_triplet)
