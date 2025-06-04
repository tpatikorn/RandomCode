from euler.util import find_divisors
from math import ceil

limit = 28123 + 1

abundant = [False for i in range(0, limit)]

for i in range(1, limit):
    divs = find_divisors(i, True)
    if sum(divs) > i:
        abundant[i] = True

sum_non_abundant = 0
for i in range(1, limit):
    is_abundant_sum = False
    for left in range(1, ceil(i / 2) + 1):
        if abundant[left]:
            if i - left > 0 and abundant[i - left]:
                is_abundant_sum = True
                break
        else:
            continue
    if not is_abundant_sum:
        sum_non_abundant = sum_non_abundant + i

print(sum_non_abundant)
