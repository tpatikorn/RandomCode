from euler import util
import functools
result = []
for n in range(52102, 100_000_000, 4):
    divisors = util.find_divisors(n)
    if functools.reduce(lambda a, b: a and b, [util.is_prime(d + int(n/d)) for d in divisors]):
        result.append(n)
        print(n)
print(sum(result))
