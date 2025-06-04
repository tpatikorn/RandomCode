from euler import util

total = 0
for i in range(0, 1000000):
    if util.is_palindrome(i) and util.is_palindrome(bin(i)[2:]):
        print(i)
        total = total + i

print("total:", total)
