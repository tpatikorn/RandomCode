import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

target = 1000000 - 1  # -1 because it starts at 0

cursor = 0
result = []
while len(digits) > 0:
    if math.factorial(len(digits) - 1) > target:
        result.append(digits.pop(cursor))
        cursor = 0
    else:
        target = target - math.factorial(len(digits) - 1)
        cursor = cursor + 1

print(*result, sep="")
