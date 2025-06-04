def cnr(_n: int, _r: int):
    total = 1
    for i in range(_n, _r, -1):
        total *= i
    for i in range(1, _n - _r + 1):
        total //= i
    return total


lim = 1e6
over_lim = 0
for n in range(1, 101):
    this_over_lim = 0
    if n % 2 == 0 and cnr(n, n // 2) > lim:
        this_over_lim += 1
        # print(n, n // 2)
    r = (n - 1) // 2
    while r > 0:
        if cnr(n, r) > lim:
            this_over_lim += 2
            # print(n, r)
            r -= 1
        else:
            break
    over_lim += this_over_lim
print(over_lim)
