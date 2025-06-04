from functools import reduce

# one-liner
print(reduce(lambda a, b: (a + b) % 10**10, [i ** i % 10**10 for i in range(1, 1001)]))

# expanded
total = 0
for i in range(1, 1001):
    total = (total + i ** i) % 10**10

print(total)
