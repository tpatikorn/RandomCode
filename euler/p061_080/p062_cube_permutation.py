from collections import Counter

cubes = [[_**3, "".join(sorted(list(str(_**3))))] for _ in range(100, 10000)]

ct5 = [_ for _ in Counter([_[1] for _ in cubes]).items() if _[1] == 5]

for ct in ct5:
    subset = sorted([_ for _ in cubes if _[1] == ct[0]], key=lambda _: _[0])
    print(subset)
