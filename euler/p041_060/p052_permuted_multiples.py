def same_digits(a: int, b: int) -> bool:
    a, b = str(a), str(b)
    return len(a) == len(b) and sorted(a) == sorted(b)


for digit in range(10):
    print(digit)
    for i in range(int(10**(digit-1)), int(10**digit)):
        if len(str(6*i)) > digit:
            break
        if same_digits(i, 2*i) and same_digits(i, 3*i) and same_digits(i, 4*i) and same_digits(i, 5*i) and same_digits(i, 6*i):
            print(i)
            break
