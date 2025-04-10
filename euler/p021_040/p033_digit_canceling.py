numerators = []
denominators = []

for i in range(11, 100):
    if i % 10 == 0:
        continue
    for j in range(i + 1, 100):
        if j % 10 == 0:
            continue
        intersect = set(str(i)).intersection(set(str(j)))
        if len(intersect) == 0:
            continue
        else:
            new_i = set(str(i)).difference(intersect)
            if len(new_i) == 0:
                new_i = intersect
            new_i = int(list(new_i)[0])

            new_j = set(str(j)).difference(intersect)
            if len(new_j) == 0:
                new_j = intersect
            new_j = int(list(new_j)[0])
            if i / j == new_i / new_j:
                print(i, j)
                denominators.append(j)
                numerators.append(i)

n = 1
d = 1
for (i, j) in zip(numerators, denominators):
    n = n * i
    d = d * j

print(d / n)
