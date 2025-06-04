target = 1000
for a in range(1, target):
    for b in range(a + 1, target - a):
        c = target - a - b
        if c < a or c < b:
            break
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c, a*b*c)
