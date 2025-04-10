from euler.util import get_prime_list


def cycle_chars(s, times_limit=None):
    if times_limit is None:
        times_limit = len(s)
    if times_limit == 0:
        return []
    return [s] + cycle_chars(s[1:] + s[0], times_limit - 1)


good_digits = [1, 3, 7, 9]

prime_list = get_prime_list(limit=1000000)

count = 0
for p in prime_list:
    if p > 5 and "5" in str(p):
        continue
    circle = cycle_chars(str(p))
    if all(int(elt) in prime_list for elt in circle):
        print(p)
        count = count + 1

print("count", count)
