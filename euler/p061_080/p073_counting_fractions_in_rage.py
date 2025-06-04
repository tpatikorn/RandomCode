import math

from euler.util import totient_from_factors, get_prime_list, factorize_range

print("ready")
max_number = 12000
factors = factorize_range(max_number)

ct = 0
for denominator in range(2, max_number + 1):
    if denominator % 1000 == 0:
        print(denominator)
    for numerator in range(math.floor(denominator / 3) + 1, math.ceil(denominator / 2)):
        if (numerator / denominator) <= 1 / 3:  # double check it because I'm an idiot
            print(numerator, denominator, "continue")
            continue
        if (numerator / denominator) >= 1 / 2:  # double check it because I'm an idiot
            print(numerator, denominator, "break")
            break
        # if 0 in this list, it means numerator and denominator aren't relative prime
        if 0 not in [numerator % prime for prime in factors[denominator]]:
            ct += 1
print(ct)