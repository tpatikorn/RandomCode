from euler.util import count_partition, __partition_with_max

#
_memo_full = [1,  # 0
              1,  # 1
              2]  # 4
_memo_full += [0 for _ in range(10000)]
_memo_part = {(2, 1): 1}


def coin_partition_full(n):
    # print("==========doing n:", n)
    _memo_full[n] = 1
    all_parts = [0 for _ in range(0, n)]
    for part in range(1, n):
        new_n = n - part
        part = min(part, new_n)
        if part == new_n:
            this_part = _memo_full[part]
        else:
            # retrieve partial
            # print("popping", (new_n, part), _memo_part)
            this_part = _memo_part.pop((new_n, part))
        # print("partial: ", new_n, part, "=", this_part)
        for p in range(n - new_n, n):
            all_parts[p] += this_part
        _memo_full[n] += this_part
    # print("to return full and all parts", _memo_full[n], all_parts)
    for n_part, partial_sum in enumerate(all_parts):
        if n_part == 0:
            continue
        # print("adding", n, n_part, partial_sum)
        _memo_part[(n, n_part)] = partial_sum
    return _memo_full[n]


# 0, 1, 2, 3, 4, 5,  6,  7,  8,  9, 10, 11, 12,  13,  14,  15,  16,  17,  18,  19,  20,
# 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627,

# a bit of a cheat with Ramanujan's partition number property
# partition number must be = 4 mod (5) to have its partition number divisible by 5
for i in range(3, 100, 1):
    new_val = coin_partition_full(i)
    if new_val % 1_000 == 0:
        print("calculated:", i, "=", new_val)


# above is too long to run to find solution, sadly.
# Need to change to pentagonal number instead
# https://en.wikipedia.org/wiki/Integer_partition#Recurrence_formula
def pentagonal(n):
    return (3 * n * n - n) // 2


_coin_penta_memo = [1, 1, 2] + [-1 for _ in range(60000)]


def coin_partition_with_pentagonal(n):
    # print("==============doing", n)
    this_sum = 0
    p_i = 0
    while n > 0:
        penta_index = (1 if p_i % 2 == 0 else -1) * ((p_i + 2) // 2)
        penta_number = pentagonal(penta_index)
        new_n = n - penta_number
        if new_n < 0:
            break
        # print("test", p_i, penta_index, penta_number, new_n)
        if _coin_penta_memo[new_n] < 0:
            coin_partition_with_pentagonal(new_n)
        this_sum += (1 if p_i % 4 < 2 else -1) * _coin_penta_memo[new_n]
        p_i += 1
    # print("finalize", n, this_sum)
    _coin_penta_memo[n] = this_sum % 1_000_000  # faster ver.
    # _coin_penta_memo[n] = this_sum
    return this_sum


for k in range(1, 60000):
    result = coin_partition_with_pentagonal(k)
    if result % 10_000 == 0:
        print(k, result)
        if result % 1_000_000 == 0:
            break
