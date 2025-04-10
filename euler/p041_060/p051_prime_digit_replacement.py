from euler.util import get_prime_list
from itertools import combinations


def make_number_template(base_number: int, repeat_digits: list):
    total_digits = len(str(base_number)) + len(repeat_digits)
    template = "".join("x" if _ in repeat_digits else "b" for _ in range(total_digits))

    for d in str(base_number):
        template = template.replace("b", d, 1)

    return template


def find_family(family_digit):
    for base_digit_count in range(1, family_digit):
        for base in range(10 ** (base_digit_count - 1), 10 ** base_digit_count):
            repeat_digits = family_digit - base_digit_count
            for combi in combinations(range(family_digit), repeat_digits):
                template = make_number_template(base, combi)
                strike = 0
                for i in range(10):
                    new_num = int(template.replace("x", str(i)))
                    if new_num not in prime_set:
                        strike += 1
                    if strike > 2:
                        break
                else:
                    print(template)


__digits = 6
prime_set = set([_ for _ in get_prime_list(limit=10**__digits) if _ >= 10 ** (__digits - 1)])
find_family(__digits)
