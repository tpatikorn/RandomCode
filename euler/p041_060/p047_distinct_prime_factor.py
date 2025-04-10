from euler import util

for i in range(134040, 140000):
    s0 = set(util.factorize(i))
    s1 = set(util.factorize(i + 1))
    s2 = set(util.factorize(i + 2))
    s3 = set(util.factorize(i + 3))
    if len(s0) == len(s1) == len(s2) == len(s3) == 4:
        print(i)
        break
print("done")
