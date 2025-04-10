from euler import util


def euler_quad(n, a, b):
    return n * n + n * a + b


prime_list = util.get_prime_list(limit=10000)
b_list = util.get_prime_list(limit=1000)
best_count = 0
best_ab = (0, 0)
for _a in range(-999, 1000):
    for _b in b_list:
        prime_count = 0
        for _n in range(0, 1000):
            num = euler_quad(_n, _a, _b)
            if num in prime_list:
                prime_count = prime_count + 1
            elif num > max(prime_list):
                print("num!", num)
            else:
                break
        if prime_count > best_count:
            best_count = prime_count
            best_ab = (_a, _b)
            print(_a, _b, best_count)
print("best_count", best_count, "best_count_coef_prod", best_ab[0] * best_ab[1])
