import itertools

def _add(a, b):
    return a + b

def _mul(a, b):
    return a * b

def _sub(a, b):
    return a - b

def _sub_r(a, b):
    return b - a

def _div(a, b):
    return a / b

def _div_r(a, b):
    return b / a

all_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
expr = [_add, _mul, _sub, _sub_r, _div, _div_r]

for four_digits in itertools.combinations(all_digits, 4):
    results = []
    for digits in itertools.permutations(four_digits):
        for e1 in expr:
            for e2 in expr:
                for e3 in expr:
                    try:
                        result = e3(e2(e1(digits[0], digits[1]), digits[2]), digits[3])
                        results.append(result)
                    except ZeroDivisionError:
                        pass

    results = [int(_) for _ in set(results) if _.is_integer() and _ > 0]
    results.sort()
    if {_ for _ in range(1, 50)} <= set(results):
        print(four_digits, results)
