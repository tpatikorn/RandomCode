from euler.util import get_prime_list
import math

upper_limit = 50_000_000
prime_list = get_prime_list(limit=math.sqrt(upper_limit))

triple_power = set()
for a in prime_list:
    for b in prime_list:
        for c in prime_list:
            new_num = a ** 2 + b ** 3 + c ** 4
            if new_num < upper_limit:
                triple_power.add(new_num)
            else:
                break

print(triple_power)
print(len(triple_power))
