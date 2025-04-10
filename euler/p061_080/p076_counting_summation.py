num_highest_count = {(1, 1): 1,  # 1
                     (2, 1): 1,  # 1 1
                     (2, 2): 2,  # 1 1      , 2
                     (3, 1): 1,  # 1 1 1
                     (3, 2): 2,  # 1 1 1    , 2 1
                     (3, 3): 3,  # 1 1 1    , 2 1       , 3
                     (4, 1): 1,  # 1 1 1 1
                     (4, 2): 3,  # 1 1 1 1  , 2 2      , 2 1 1
                     (4, 3): 4,  # 1 1 1 1  , 2 2      , 2 1 1     , 3 1
                     (4, 4): 5}  # 1 1 1 1  , 2 2      , 2 1 1     , 3 1    , 4


def count_summation(num, highest=None):
    if highest is None or highest >= num:
        highest = num
    if (num, highest) in num_highest_count:
        return num_highest_count[(num, highest)]

    if num == 0:
        return 1

    if highest == 1:
        num_highest_count[(num, 1)] = 1
        return 1

    current_sum = 0
    for sub_highest in range(highest, 0, -1):
        new_num = num - sub_highest
        current_sum += count_summation(new_num, sub_highest)
    num_highest_count[(num, highest)] = current_sum

    return num_highest_count[(num, highest)]


# this function include the sum of 1 number (for convenience of calculation)
# the question ask for sum of at least 2 numbers, so subtract 1 from the answer
print(count_summation(100) - 1)
