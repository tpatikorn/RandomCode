num = 1000000
collatz = {1: 1}


def cal_collatz(n, step, verbose=False):
    if verbose:
        print(n)
    try:
        if verbose:
            print("skip!", collatz[n])
        return collatz[n], step + 1
    except KeyError:
        if n % 2 == 0:
            new_n = int(n / 2)
        else:
            new_n = n * 3 + 1
        sub_count, sub_step = cal_collatz(new_n, step + 1, verbose)
        collatz[n] = sub_count + 1
        return sub_count + 1, sub_step


for i in range(1, num):
    res, _ = cal_collatz(i, 0)
    # print("---", i, res)
print(max(collatz.keys()), max(collatz.values()))
collatz_bound = list(filter(lambda p: p[0] < num, collatz.items()))
collatz_max = max(map(lambda p: p[1], collatz_bound))
collatz_bound = list(filter(lambda p: p[1] == collatz_max, collatz_bound))
print(collatz_max, collatz_bound)

_ = int(input("?"))
print(cal_collatz(_, 0, verbose=True))
