import math


# using continued fraction to find the solution. apparently it works this way

def continued_fraction(n, max_iter=100, just_a=True):
    # the format is b / sqrt(23) - c --> d + sqrt(23) - e / f
    a0 = math.floor(math.sqrt(n))
    b0 = 1
    c0 = math.floor(math.sqrt(n))
    a, b, c = a0, b0, c0
    history = []

    for i in range(1, max_iter):
        f = (n - c * c) / b  # 7
        d = math.floor((math.sqrt(n) + c) / f)
        e = d * f - c  # 1 * 7 - 4 = 3
        if just_a:
            history.append(a)
        else:
            history.append([a, b, c, d, e, f])
        a = d  # 1
        b = f  # 7
        c = e  # 3
    return history


max_x = 0
max_x_D = 0
for D in [_ for _ in range(2, 1001) if _ != math.isqrt(_) ** 2]:
    print(D, end="\t")
    cf = continued_fraction(D, 1000)
    p, po, poo = 0, 0, 0
    q, qo, qoo = 0, 0, 0
    for a_ in cf:
        if p == 0:
            p = a_
            q = 1
            po = 1
        else:
            po, poo = p, po
            qo, qoo = q, qo
            p, q = po * a_ + poo, qo * a_ + qoo

        # check if current numerator and denominator satisfy the property
        if p ** 2 - D * q ** 2 == 1:
            print(f"found (+1)! D: {D} x {p}, y {q}")
            if p > max_x:
                max_x = p
                max_x_D = D
            break
        elif p ** 2 - D * q ** 2 == -1:
            print(f"found (-1)! D: {D} x {p ** 2 + D * q ** 2}, y {2 * p * q}")
            if p ** 2 + D * q ** 2 > max_x:
                max_x = p ** 2 + D * q ** 2
                max_x_D = D
            break
    else:
        print(f"not found D: {D}, continued fractions = {cf}")
print(f"max_x_D = {max_x_D}")
