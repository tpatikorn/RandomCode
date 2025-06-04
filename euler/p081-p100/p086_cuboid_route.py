import math

max_c = 100

triplets = set()
for m in range(2, math.isqrt(max_c) + 1000):
    for n in range(1, m):
        if math.gcd(m, n) > 1:
            continue
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        k = 1
        while c * k <= max_c and b * k <= max_c:
            trip = tuple(sorted([a * k, b * k, c * k]))
            triplets.add(trip)
            k += 1

print(triplets)

cuboid_count = 0
for trip in triplets:
    x, y, z = trip
    if 2*x < y:
        continue
    elif x > y:
        cuboid_count += y // 2
    else:
        cuboid_count += x - (y - 1) // 2

print(len(triplets), cuboid_count)
