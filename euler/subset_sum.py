from functools import reduce
import math


def compare_subset_sum(a: list[int], b: list[int]):
    return not (reduce(lambda x, y: x and y, [i < j for i, j in zip(a, b)]) or
                reduce(lambda x, y: x and y, [i > j for i, j in zip(a, b)]))


def _pick_n(digit_set: list, n: int) -> list[list[int]]:
    if n == 0:
        return []
    elif n == 1:
        return [[d] for d in digit_set]
    else:
        subsets = []
        for d in digit_set:
            digit_set.remove(d)
            for the_rest in _pick_n(digit_set, n - 1):
                subsets.append(sorted(the_rest + [d]))
    return subsets


def pick_n(digit_set: list, n: int) -> list[list[int]]:
    return _pick_n(digit_set, n)


def generate_special_subset_pairs(length: int) -> list[tuple[list[int], list[int]]]:
    pairs = []
    for set_len in range(1, math.floor(length / 2) + 1):
        for s in pick_n(list(range(length)), set_len):
            new_digits = list(range(length))
            for c in s:
                new_digits.remove(c)
            for j in pick_n(new_digits, set_len):
                pairs.append((s, j))
    return pairs


def remove_dupe_pairs(pairs: list):
    keep = []
    while len(pairs) > 0:
        p = pairs[0]
        keep.append(p)
        try:
            pairs.remove(p)
            pairs.remove((p[1], p[0]))
        except ValueError:
            continue
    return keep


def find_bad_pairs(max_len):
    subset_pairs = remove_dupe_pairs(generate_special_subset_pairs(max_len))
    return list(filter(lambda p: compare_subset_sum(p[0], p[1]), subset_pairs))


print(find_bad_pairs(5))
