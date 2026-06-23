results = {1: 1, 89: 89}

for i in range(1, 10_000_000):
    # print(i, ": ", end="")
    current = i
    while current not in results:
        current = sum([int(_)**2 for _ in str(current)])
        # print(current, end=" => ")
    results[i] = results[current]
    # print(results[current])

print(len([_ for _ in results.values() if _ == 89]))