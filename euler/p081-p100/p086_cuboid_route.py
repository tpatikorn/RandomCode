import math

max_c = 2000

# the checkpoint lags behind by 1 but the solution print is correct since it's checked after the iteration
LAST_BOUND_CHECKPOINT = {100: 1975,
                         200: 8828,
                         300: 21324,
                         400: 39803,
                         500: 63785,
                         600: 93489,
                         700: 130696,
                         800: 174583,
                         900: 224197,
                         1000: 280308,
                         1100: 343173,
                         1200: 412759,
                         1300: 491044,
                         1400: 574748,
                         1500: 666057,
                         1600: 766235,
                         1700: 868053,
                         1800: 977031}

last_bound_start = min(max(LAST_BOUND_CHECKPOINT.keys()), max_c)
cuboid_count = LAST_BOUND_CHECKPOINT[last_bound_start]

for last_bound in range(last_bound_start, max_c + 1, 1):
    print(last_bound, cuboid_count)
    for m1 in range(1, last_bound + 1):
        for m2 in range(m1, last_bound + 1):
            for m3 in range(max(last_bound, m2), last_bound + 1):
                cuboid_len_squared = (m3 ** 2) + ((m1 + m2) ** 2)
                if math.isqrt(cuboid_len_squared) ** 2 == cuboid_len_squared:
                    cuboid_count += 1
    if cuboid_count > 1_000_000:
        print(last_bound, cuboid_count)
        break
