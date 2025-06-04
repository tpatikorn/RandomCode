from math import sqrt, floor


def find_palindrome_6():
    for p1 in range(9, 0, -1):
        for p2 in range(9, -1, -1):
            for p3 in range(9, -1, -1):
                n = p1 * 100001 + p2 * 10010 + p3 * 1100
                for i in range(floor(sqrt(n)), 100, -1):
                    if n % i == 0 and n / i <= 999:
                        return n, i, n / i


print(find_palindrome_6())
