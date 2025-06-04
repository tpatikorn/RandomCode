numerator = 1
denominator = 2

more_digit_count = 0
print(0, numerator + denominator, denominator)
for i in range(1, 1001):
    numerator, denominator = denominator, numerator + 2 * denominator
    print(i, numerator + denominator, denominator)
    if len(str(numerator + denominator)) > len(str(denominator)):
        more_digit_count += 1
print(more_digit_count)
