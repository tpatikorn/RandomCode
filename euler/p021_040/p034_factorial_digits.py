import math

all_sum = 0
for i in range(11, 99999):
    factorial_sum = sum([math.factorial(int(x)) for x in str(i)])
    if i == factorial_sum:
        print(i)
        all_sum = all_sum + factorial_sum

print(all_sum)
