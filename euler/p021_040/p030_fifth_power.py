from math import floor

sum_sum_fifth = 0
for i in range(2, (9 ** 5) * 6):  # 9^5 = 59049, 6 digits = 354,294. The fifth power sum of 6 digits can't be any bigger
    temp = i
    sum_fifth = 0
    while temp > 0:
        sum_fifth = sum_fifth + (temp % 10) ** 5
        temp = floor(temp / 10)
    if sum_fifth == i:
        print(i)
        sum_sum_fifth = sum_sum_fifth + sum_fifth

print(sum_sum_fifth)
