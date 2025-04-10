from euler.util import is_pandigital

best = 0
for i in range(91, 99999):
    curr = str(i)
    for mult in range(2, 10):
        curr = curr + str(i * mult)
        if len(curr) > 9:
            break
        elif len(curr) == 9:
            if is_pandigital(curr):
                if best < int(curr):
                    best = int(curr)
                    print(best)
