result = {(0, 0, 0): 0}


# A 0 0 2 ->


# A 0 1 x -> B 0 1 1 -> B lose  == A win
# A 1 1 x                       -> A win

# A 1 x x
# -> B 0 1 x -> B win           == A lose
# -> B 1 1 x -> B win           == A lose
# -> B 1 2 x ->


def nim_match(xi, xj, xk):
    if xi > xj:
        return nim_match(xj, xi, xk)
    elif xj > xk:
        return nim_match(xi, xk, xj)
    elif (xi, xj, xk) in result.keys():
        return result[(xi, xj, xk)]
    else:
        found = False
        result[(xi, xj, xk)] = 0
        for xi2 in range(0, xi):
            # print("trying", xi2, xj, xk)
            if nim_match(xi2, xj, xk) == 0:
                result[(xi, xj, xk)] = 1
                found = True
                break
        if not found:
            for xj2 in range(0, xj):
                # print("trying", xi, xj2, xk)
                if nim_match(xi, xj2, xk) == 0:
                    result[(xi, xj, xk)] = 1
                    found = True
                    break
        if not found:
            for xk2 in range(0, xk):
                # print("trying", xi, xj, xk2)
                if nim_match(xi, xj, xk2) == 0:
                    result[(xi, xj, xk)] = 1
                    break
        # print("found", result[(xi, xj, xk)])
        return result[(xi, xj, xk)]


limit = 100
for i in range(0, limit):
    print(i)
    j = 2 * i
    k = 3 * i
    if nim_match(i, j, k) == 0:
        print(i, j, k, nim_match(i, j, k))
