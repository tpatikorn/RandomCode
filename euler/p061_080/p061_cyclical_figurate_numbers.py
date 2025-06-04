import math
import itertools


def figurate(shape, n):
    match shape:
        case 3:
            return n * (n + 1) // 2
        case 4:
            return n * n
        case 5:
            return n * (3 * n - 1) // 2
        case 6:
            return n * (2 * n - 1)
        case 7:
            return n * (5 * n - 3) // 2
        case 8:
            return n * (3 * n - 2)


def list_figurate_numbers(shape, num_min=1000, num_max=10_000):
    _numbers = []
    for n in range(1, round(2 * math.sqrt(num_max))):
        new_num = figurate(shape, n)
        if new_num > num_max:
            break
        if new_num < num_min:
            continue
        _numbers.append([shape, n, new_num // 100, new_num % 100])
    return _numbers


all_numbers = []
for shape in [3, 4, 5, 6, 7, 8]:
    all_numbers += list_figurate_numbers(shape, num_min=1000, num_max=10000)

tracked_numbers = [[[3], [_]] for _ in all_numbers if _[0] == 3]

# repeat 5 times
for i in range(5):
    tracked_numbers = [[a[0] + [b[0]], a[1] + [b]]
                       for a, b in itertools.product(tracked_numbers, all_numbers)
                       if a[1][-1][3] == b[2] and b[0] not in a[0]]

tracked_numbers = [[a, b] for a, b in tracked_numbers if b[0][2] == b[-1][3]]

print(*tracked_numbers, sep="\n")

print(sum([c[2] * 100 + c[3] for a, b in tracked_numbers for c in b]))
