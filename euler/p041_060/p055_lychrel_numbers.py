from euler.util import int_reverse, is_palindrome


def reverse_add(n: int):
    return n + int_reverse(n)


lychrel_count = 0
for base_n in range(1, 10_001):
    n = base_n
    n += int_reverse(n) # need this first to exclude palindrome lychrel numbers
    for i in range(0, 50):
        if is_palindrome(n):
            # print(i, base_n, n)
            break
        n += int_reverse(n)
    else:
        print("---------", base_n)
        lychrel_count += 1
print(lychrel_count)
