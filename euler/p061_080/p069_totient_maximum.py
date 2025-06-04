from euler.util import get_prime_list

total = 1
for i in get_prime_list(1000):
    if total * i > 10**6:
        break
    total *= i

print(total)
