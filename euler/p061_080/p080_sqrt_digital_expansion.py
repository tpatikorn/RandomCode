from decimal import Decimal, getcontext
from math import isqrt

getcontext().prec = 102

total_digit_sum = 0
for i in range(1, 101):
    if isqrt(i) ** 2 == i:
        continue
    decimal_sqrt = Decimal(i).sqrt()
    digits = [int(_) for _ in str(decimal_sqrt) if _ != "."][0:100]
    total_digit_sum += sum(digits)
    # print(i, sum(digits), len(digits), digits)

print(total_digit_sum)
