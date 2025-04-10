from functools import reduce
from typing import List

from euler.util import totient, get_prime_list, is_permutation, totient_from_factors

limit = 10_000_000
PRIME_LIST = get_prime_list(limit=limit // 2)
total = 1
LENGTH = len(PRIME_LIST)

lowest_ratio = 1000
lowest_ratio_n = 1


def is_prime_product_totient_permutation(_indices: List[int]) -> (bool, int, int):
    _subset = {PRIME_LIST[_] for _ in _indices}
    _prime_product = reduce(lambda x, y: x * y, _subset)
    _tt = totient_from_factors(_prime_product, _subset)
    _result = is_permutation(_prime_product, _tt)
    return _result, _prime_product, _tt


for i1 in range(LENGTH):
    indices = [i1]
    result, prime_product, tt = is_prime_product_totient_permutation(indices)
    if prime_product > limit:
        # print("break", indices, result, prime_product, tt)
        break
    if result and (prime_product / tt < lowest_ratio):
        lowest_ratio = prime_product / tt
        lowest_ratio_n = prime_product
        print("LOW", prime_product, tt, indices)
    for i2 in range(i1 + 1, LENGTH):
        indices = [i1, i2]
        result, prime_product, tt = is_prime_product_totient_permutation(indices)
        if prime_product > limit:
            # print("break", indices, result, prime_product, tt)
            break
        if result and (prime_product / tt < lowest_ratio):
            lowest_ratio = prime_product / tt
            lowest_ratio_n = prime_product
            print("LOW", prime_product, tt, indices)
        for i3 in range(i2 + 1, LENGTH):
            indices = [i1, i2, i3]
            result, prime_product, tt = is_prime_product_totient_permutation(indices)
            if prime_product > limit:
                # print("break", indices, result, prime_product, tt)
                break
            if result and (prime_product / tt < lowest_ratio):
                lowest_ratio = prime_product / tt
                lowest_ratio_n = prime_product
                print("LOW", prime_product, tt, indices)
            for i4 in range(i3 + 1, LENGTH):
                indices = [i1, i2, i3, i4]
                result, prime_product, tt = is_prime_product_totient_permutation(indices)
                if prime_product > limit:
                    # print("break", indices, result, prime_product, tt)
                    break
                if result and (prime_product / tt < lowest_ratio):
                    lowest_ratio = prime_product / tt
                    lowest_ratio_n = prime_product
                    print("LOW", prime_product, tt, indices)
                for i5 in range(i4 + 1, LENGTH):
                    indices = [i1, i2, i3, i4, i5]
                    result, prime_product, tt = is_prime_product_totient_permutation(indices)
                    if prime_product > limit:
                        # print("break", indices, result, prime_product, tt)
                        break
                    if result and (prime_product / tt < lowest_ratio):
                        lowest_ratio = prime_product / tt
                        lowest_ratio_n = prime_product
                        print("LOW", prime_product, tt, indices)
                    for i6 in range(i5 + 1, LENGTH):
                        indices = [i1, i2, i3, i4, i5, i6]
                        result, prime_product, tt = is_prime_product_totient_permutation(indices)
                        if prime_product > limit:
                            # print("break", indices, result, prime_product, tt)
                            break
                        if result and (prime_product / tt < lowest_ratio):
                            lowest_ratio = prime_product / tt
                            lowest_ratio_n = prime_product
                            print("LOW", prime_product, tt, indices)
                        for i7 in range(i6 + 1, LENGTH):
                            indices = [i1, i2, i3, i4, i5, i6, i7]
                            result, prime_product, tt = is_prime_product_totient_permutation(indices)
                            if prime_product > limit:
                                # print("break", indices, result, prime_product, tt)
                                break
                            if result and (prime_product / tt < lowest_ratio):
                                lowest_ratio = prime_product / tt
                                lowest_ratio_n = prime_product
                                print("LOW", prime_product, tt, indices)
                            for i8 in range(i7 + 1, LENGTH):
                                indices = [i1, i2, i3, i4, i5, i6, i7, i8]
                                result, prime_product, tt = is_prime_product_totient_permutation(indices)
                                if prime_product > limit:
                                    # print("break", indices, result, prime_product, tt)
                                    break
                                if result and (prime_product / tt < lowest_ratio):
                                    lowest_ratio = prime_product / tt
                                    lowest_ratio_n = prime_product
                                    print("LOW", prime_product, tt, indices)

print(total)
