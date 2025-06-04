from euler import util


def check_left_truncate(n):
    if n < 10:
        return util.is_prime(n)
    elif util.is_prime(n):
        return check_left_truncate(int(str(n)[1:]))
    else:
        return False


def check_right_truncate(n):
    if n < 10:
        return util.is_prime(n)
    elif util.is_prime(n):
        return check_right_truncate(n // 10)
    else:
        return False


truncatable = []

base = [1, 2, 3, 4, 5, 6, 7, 8, 9]

viable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while len(viable) > 0:
    curr = viable.pop(0)
    for i in base:
        new = curr * 10 + i
        if check_right_truncate(new):
            viable.append(new)
            if check_left_truncate(new):
                print(new)
                truncable.append(new)
    if len(truncable) >= 11:
        break

print(truncable)
print(sum(truncable))
