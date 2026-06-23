from math import sqrt
from typing import Dict, List

from euler.util import is_prime


# N is small enough. start by factorizing numbers.
# MAX_N is for k. A simple observation is easy to see that.
# the len of min product sum does not exceed 2*MAX_N.
# so, loop through all number from 1 to 2*MAX_N to find all possible factorization.
# Then, loop through factorization, and count the number of factors.
MAX_N = 12000

factors: Dict[int, List[List[int]]] = {2: [[2]],
                                       3: [[3]],
                                       4: [[2, 2], [4]]}

for n in range(5, MAX_N * 2):
    factors[n] = [[n]]
    if is_prime(n):
        continue
    for divider in range(2, int(sqrt(n)) + 1):
        if n % divider == 0:
            leftover = n // divider
            n_leftover_factor: List[List[int]] = [_ + [divider] for _ in factors[leftover]]
            factors[n] += n_leftover_factor

# print(factors)
min_product_sum = [MAX_N * 10 for _ in range(MAX_N * 2)]

for n in factors:
    for factorized in factors[n]:
        ones = n - sum(factorized)
        k = len(factorized) + ones
        min_product_sum[k] = min(n, min_product_sum[k])

print(min_product_sum)
print(sum(set(min_product_sum[2: MAX_N + 1])))