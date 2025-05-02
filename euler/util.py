import math
from math import sqrt, inf, ceil, floor
from typing import List

__divisors = {1: set()}
__primes = [2, 3]
__highest_tested = 4
__factor_chain = {1: [None, None]}
__partition_with_max = {(1, 1): 1}
__partition_with_max_prime = {(1, 1): 0}


def is_palindrome(obj):
    obj = str(obj)
    for i in range(0, floor(len(obj) / 2)):
        if obj[i] != obj[len(obj) - i - 1]:
            return False
    return True


def is_prime(number):
    get_prime_list(limit=number)
    return number in __primes


# test using miller rabin test
def is_probable_prime(n, num_bases=7, minimum=1_000):
    if n < minimum:
        return is_prime(n)

    s = 0
    bases = get_prime_list(num_bases)
    d = n - 1
    while d % 2 == 0:
        d = d // 2
        s += 1
    for a in bases:
        a_to_d = pow(a, d, n)
        if a_to_d % n == 1 or a_to_d % n == n - 1:
            continue
        else:
            for r in range(s - 1):
                a_to_d = pow(a_to_d, 2, n)
                if a_to_d == n - 1:
                    break
            else:
                return False  # if not break, then definitely composite
    return True


def get_prime_list(limit=None, n_primes=None):
    global __highest_tested, __primes
    if limit is not None and n_primes is None:
        n_primes = 999999999
    if n_primes is not None and limit is None:
        limit = 999999999
    if n_primes <= len(__primes):
        return __primes[0: n_primes]
    if limit <= __highest_tested:
        return [_ for _ in __primes if _ < limit]
    return _get_prime_list(limit, n_primes)


def _get_prime_list(limit, n_primes):
    global __highest_tested, __primes
    limit = round(limit)
    if __highest_tested % 2 == 0:
        __highest_tested += 1  # or the for loop might break lol
    for i in range(__highest_tested, limit + 1, 2):
        sqrt_i = sqrt(i)
        for p in __primes:
            if i % p == 0:
                break
            if p > sqrt_i:
                __primes.append(i)
                if len(__primes) >= n_primes:
                    return __primes
                break
    __highest_tested = limit
    return __primes


def find_divisors(num, proper=False):
    if proper:
        return find_divisors(num, False) - {num}
    try:
        return __divisors[num]
    except KeyError:
        __divisors[num] = {1, num}
        for p in range(2, ceil(sqrt(num)) + 1):
            if num % p == 0:
                __divisors[num] = __divisors[num].union(find_divisors(p)).union(find_divisors(int(num / p)))
        return __divisors[num]


def __trace_factor_chain(num: int):
    factors = set()
    curr = num
    while (curr != 1) and (curr is not None):
        factors.add(__factor_chain[curr][0])
        curr = __factor_chain[curr][1]
    return factors


def factorize(num):
    try:
        if is_prime(num):
            __factor_chain[num] = [num, None]
            return [num]
        return __trace_factor_chain(num)
    except KeyError:
        curr = num
        for p in get_prime_list(limit=int(sqrt(num) + 1)):
            __factor_chain[p] = [p, None]
            if curr % p == 0:
                factor_queue = [curr]
                curr = curr // p
                while curr % p == 0 and curr > 1:
                    factor_queue.append(curr)
                    curr = curr // p
                for in_queue in factor_queue:
                    __factor_chain[in_queue] = [p, curr] if curr > 1 else [p, None]
                if is_prime(curr):
                    __factor_chain[curr] = [curr, None]
                    break
        return __trace_factor_chain(num)


def factorize_range(max_number):
    prime_list = get_prime_list(max_number)
    factors = [set() for _ in range(max_number + 1)]
    for prime in prime_list:
        max_mult = math.floor(max_number / prime)
        for _ in range(1, max_mult + 1):
            factors[_ * prime].add(prime)
    return factors


def unique_digits_non_zero(s: int | str):
    return len(set(str(s)) - {0}) == len(str(s))


def is_pandigital(s: int | str):
    return {int(_) for _ in str(s)} == set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0][0:len(str(s))])


def slope(src, dst):
    if src[0] == dst[0]:
        if dst[1] < src[1]:
            return -inf
        else:
            return inf
    return (dst[1] - src[1]) / (dst[0] - src[0])


def is_permutation(a: List[int] | int, b: List[int] | int) -> bool:
    if type(a) is int:
        a = [int(_) for _ in str(a)]
    if type(b) is int:
        b = [int(_) for _ in str(b)]
    return sorted(a) == sorted(b)


def point_in_angle(src, dst_a, dst_b, test):
    s_test = slope(src, test)
    s_a = slope(src, dst_a)
    s_b = slope(src, dst_b)
    return (s_a <= s_test <= s_b) or (s_a >= s_test >= s_b)


def find_line(p1, p2):
    m = slope(p1, p2)
    b = p1[1] - (m * p1[0])
    return m, b


def int_reverse(n: int):
    return int(str(n)[::-1])


def digit_count(n: int):
    return len(str(n))


def totient(n: int) -> int:
    factors = set(factorize(n))
    return totient_from_factors(n, factors)


def totient_from_factors(n: int, prime_factors: set[int]) -> int:
    val = n
    for f in prime_factors:
        val *= f - 1
        val //= f
    return val


def count_partition(num, highest=None):
    if num == 0 or num == 1 or highest == 1:
        return 1

    if highest is None or highest > num:
        highest = num
    if (num, highest) in __partition_with_max.keys():
        return __partition_with_max[(num, highest)]

    # print("calculating", num, highest)
    result = count_partition(num - highest, highest) + count_partition(num, highest - 1)
    __partition_with_max[(num, highest)] = result
    return result


# ---------------------- these are for testing stuff ------------------


# comparison
import timeit
import random

test_input = [random.randint(int(1), int(10e9)) for _ in range(10_000)]

max_sqrt = 1_000_000
squares = {_ ** 2 for _ in range(2, max_sqrt)}


def fun1():
    s = 0
    for n in test_input:
        if n > max_sqrt ** 2:
            print("what")
        if n not in squares:
            return -1
        else:
            return n
    return s


def fun2():
    s = 0
    for n in test_input:
        curr = 1
        while n > 0:
            n -= curr
            if n == 0:
                return (curr + 1) // 2
            curr += 2
        return -1
    return s


if __name__ == '__main__':
    # Measure execution time of function2
    random.seed(1)
    time1 = timeit.timeit(f'fun1()', globals=globals(), number=1000)
    print(f"Total execution time of function1: {time1:.5f} seconds")

    # Measure execution time of function1
    time2 = timeit.timeit(f'fun2()', globals=globals(), number=1000)
    print(f"Total execution time of function2: {time2:.5f} seconds")
