powerful_digit_sum = 0
for a in range(1, 101):
    for b in range(1, 101):
        digit_sum = sum([int(_) for _ in str(a ** b)])
        if powerful_digit_sum < digit_sum:
            powerful_digit_sum = digit_sum
            print(a, b, digit_sum)
print(powerful_digit_sum)
