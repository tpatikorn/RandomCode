import re
import sys
from itertools import combinations
from typing import Set

sys.setrecursionlimit(10000)

all_digits = {'0', '1', '2', '3', '4', '5', '7', '8', 'b'}

# note : found the issue
# digits on same die can't be the same
# but this approach will also remove both 6 and 9 on same die (but the can be on the same die!)

# digit_pairs = [list(f"{d * d:02d}") for d in range(1, 10)]

digit_pairs = [['0', '1'],
               ['0', '4'],
               ['0', 'a'],  # replace both 6 and 9 with 'a' as placeholder for flip-able 6/9
               ['1', 'a'],  # replace both 6 and 9 with 'a' as placeholder for flip-able 6/9
               ['2', '5'],
               ['3', 'a'],  # replace both 6 and 9 with 'a' as placeholder for flip-able 6/9
               ['4', 'a'],  # replace both 6 and 9 with 'a' as placeholder for flip-able 6/9
               # ['a', '4'],  # same pair as ['4', 'a']
               ['8', '1']]


def good_digit_set(_digits):
    return len(_digits) <= 6


def to_sorted_string(_digits: Set[str]) -> str:
    return "".join(sorted(list(_digits)))


min_len = 10

good_dice = {}


def upsert_dict(_l: Set[str], _r: Set[str]):
    global good_dice
    # but a and b are actually the same
    _l = to_sorted_string(_l).replace('b', 'a')
    _r = to_sorted_string(_r).replace('b', 'a')
    _l, _r = sorted({_l, _r})
    if _l in good_dice.keys():
        good_dice[_l].add(_r)
    else:
        good_dice[_l] = {_r}


def iterate_r_digits_4_to_6(_l: Set[str], _r: Set[str]):
    global good_dice
    if not good_digit_set(_l) or not good_digit_set(_r):
        return
    elif len(_l) == 6:
        if len(_r) == 6:
            upsert_dict(_l, _r)
        elif len(_r) == 5:
            for d in all_digits - _r:
                upsert_dict(_l, _r.union({d}))
        elif len(_r) == 4:
            for _d1 in all_digits - _r:
                for _d2 in all_digits - _r - {_d1}:
                    upsert_dict(_l, _r.union({_d1, _d2}))
    elif len(_l) == 5:
        for d in all_digits - _l:
            iterate_r_digits_4_to_6(_l.union({d}), _r)
    elif len(_l) == 4:
        for _d1 in all_digits - _l:
            for _d2 in all_digits - _l - {_d1}:
                iterate_r_digits_4_to_6(_l.union({_d1, _d2}), _r)


for r in range(0, 5):
    combi = combinations(digit_pairs, r)
    for normal_subset in combi:
        # l are used as is, r swap the digits
        swap_subset = [_ for _ in digit_pairs if _ not in normal_subset]
        # print(normal_subset, swap_subset)
        n1, n2 = zip(*normal_subset) if len(normal_subset) > 0 else [[], []]
        s2, s1 = zip(*swap_subset)  # swap
        # print(n1, n2, s1, s2)
        l_digits = set(n1).union(set(s1))
        r_digits = set(n2).union(set(s2))
        # print(l_digits, r_digits)
        iterate_r_digits_4_to_6(l_digits, r_digits)
        # print(len(good_dice.items()))

final_answer_count = 0
for d1, d2s in good_dice.items():
    for d2 in d2s:
        d1_69_count = len(re.findall(r'[ab]', d1))
        d2_69_count = len(re.findall(r'[ab]', d2))
        match d1_69_count:
            case 0:
                d1_count = 1
            case 1:
                d1_count = 2
            case 2:
                d1_count = 1
            case _:
                print("yo wtf", d1, d2)
                d1_count = 0
        match d2_69_count:
            case 0:
                d2_count = 1
            case 1:
                d2_count = 2
            case 2:
                d2_count = 1
            case _:
                print("yo wtf", d1, d2)
                d2_count = 0

        print(d1, d2, d1_count, d2_count)
        final_answer_count += d1_count * d2_count

print(final_answer_count)
