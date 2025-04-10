from euler import util

for i in range(8_000_001, 1, -2):
    if i % 10000 == 1:
        print(i)
    if util.is_pandigital(i) and util.is_prime(i):
        print(i)
        break
