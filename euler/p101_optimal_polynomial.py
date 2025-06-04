def fun(x, test=False):
    if test:
        return x ** 3
    else:
        return 1 - x + x ** 2 - x ** 3 + x ** 4 - x ** 5 + x ** 6 - x ** 7 + x ** 8 - x ** 9 + x ** 10


def seq_diff(seq):
    return [seq[_ + 1] - seq[_] for _ in range(0, len(seq) - 1)]


all_seq = []
all_seq.append([fun(_) for _ in range(1, 11)])
for i in range(0, len(all_seq[0]) - 1):
    all_seq.append(seq_diff(all_seq[i]))


def calculate_fit(seq_list, level, depth=0):
    if level == 1:
        return seq_list[depth][level - 1]
    else:
        return seq_list[depth][level - 1] + calculate_fit(seq_list, level - 1, depth + 1)


print(*all_seq, sep="\n")

sum_fit = 0
for i in range(1, len(all_seq) + 1):
    fit = calculate_fit(all_seq, i)
    print(i, fit)
    sum_fit = sum_fit + fit
print(sum_fit)
