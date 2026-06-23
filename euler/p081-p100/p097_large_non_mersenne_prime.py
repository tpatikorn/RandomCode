power_left = 7830457
current_base = 2
all_mult_leftover = 1

while power_left > 1:
    if power_left % 2 == 1:
        all_mult_leftover = all_mult_leftover * current_base % 10_000_000_000
    current_base = (current_base * current_base) % 10_000_000_000
    power_left = power_left // 2
    print(power_left, current_base, all_mult_leftover)

print((28433 * current_base * all_mult_leftover) % 10_000_000_000 + 1)
