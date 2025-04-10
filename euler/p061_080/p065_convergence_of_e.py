import math


# not actually used because the precision isn't enough for 100
def e_continued_fraction(max_iter=100):
    # the format is b / sqrt(23) - c --> d + sqrt(23) - e / f
    a0 = math.floor(math.e)
    b0 = 1
    c0 = math.floor(math.e)
    a, b, c = a0, b0, c0
    history = []

    for i in range(1, max_iter):
        f = (math.e * math.e - c * c) / b  # 7
        d = math.floor((math.e + c) / f)
        e = d * f - c  # 1 * 7 - 4 = 3
        this_iter = [a, b, c, d, e, f]
        history.append(this_iter)
        a = d  # 1
        b = f  # 7
        c = e  # 3
    return history


this_history = [2 * (_ + 1) // 3 if _ % 3 == 2 else 1 for _ in range(100)]
this_history[0] = 2
print(*[_ for _ in this_history])

numerators = []
denominators = []

# use different code from p066 because this one I process in reverse. it's actually genius of me :p
for max_i in range(100):
    curr_num = 0
    curr_den = 0
    for i in this_history[max_i::-1]:
        print(i, this_history[max_i::-1])
        if curr_num == 0:
            curr_num = i
            curr_den = 1
        else:
            curr_num, curr_den = curr_den, curr_num
            curr_num, curr_den = i * curr_den + curr_num, curr_den
    numerators.append(curr_num)
    denominators.append(curr_den)

for a, b in zip(numerators, denominators):
    print(a, b)

print(sum([int(_) for _ in str(numerators[-1])]))
