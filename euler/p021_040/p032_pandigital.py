from euler import util

pan_digital = set()

for i in range(2, 999999):
    if not util.unique_digits_non_zero(i):
        continue
    for j in range(i + 1, 999999):
        if not util.unique_digits_non_zero(j):
            continue
        # print(i, j, i * j)
        new_str = str(i) + str(j) + str(i * j)
        if len(new_str) > 9:
            break
        elif len(new_str) < 9:
            continue
        elif util.is_pandigital(new_str):
            print(i, j, i * j)
            pan_digital.add(i * j)
print(sum(pan_digital))
