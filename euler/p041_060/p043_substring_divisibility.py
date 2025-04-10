from typing import Tuple

from euler import util

divisors = util.get_prime_list(n_primes=7)


def check_level(curr: str, divisor_index: int, digits: set) -> Tuple[bool, str]:
    for d in digits:
        next_ = curr[1:] + str(d)
        if int(next_) % divisors[divisor_index] == 0:
            if divisor_index + 1 == len(divisors):
                return True, str(d)
            else:
                result = check_level(next_, divisor_index + 1, digits - {d})
                if result[0]:
                    return True, str(d) + result[1]
    return False, ""


num = []

for i in range(986, 100, -1):
    if util.unique_digits_non_zero(i):
        all_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
        all_digits = all_digits - set([int(_) for _ in str(i)])
        res = check_level(str(i), 0, all_digits)
        if res[0]:
            num.append(int(str(i) + res[1]))

print(sum(num))
