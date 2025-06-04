import math

from euler.util import totient_from_factors, get_prime_list, factorize_range

print("ready")
# print(counting_fractions(1_000_000))

max_number = 1_000_000
factors = factorize_range(max_number)
print(factors)

ct = 0
for _ in range(2, max_number + 1):
    ct += totient_from_factors(_, factors[_])

print(ct)
