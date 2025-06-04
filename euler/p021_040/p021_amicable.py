from euler.util import get_prime_list
import math

target = 10000
divisors = {1: set()}
prime_list = get_prime_list(limit=target)


def find_divisors(num, proper=False):
    if proper:
        return find_divisors(num, False) - {num}
    try:
        return divisors[num]
    except KeyError:
        divisors[num] = {1, num}
        for p in range(2, math.ceil(math.sqrt(num))):
            if num % p == 0:
                divisors[num] = divisors[num].union(find_divisors(p)).union(find_divisors(int(num / p)))
        return divisors[num]


amicable = set()
for i1 in range(2, target):
    i2 = sum(find_divisors(i1, True))
    if sum(find_divisors(i2, True)) == i1 and not i1 == i2:
        amicable = amicable.union({i1, i2})

print(sum(amicable), amicable)

print(find_divisors(220, True), sum(find_divisors(220, True)))
print(find_divisors(284, True), sum(find_divisors(284, True)))
