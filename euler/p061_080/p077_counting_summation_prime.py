from euler.util import get_prime_list

num_highest_count = {(1, 1): 0,  #
                     (2, 1): 0,  #
                     (2, 2): 1,  # 2
                     (3, 1): 0,  #
                     (3, 2): 0,  #
                     (3, 3): 1,  # 3
                     (4, 1): 0,  #
                     (4, 2): 1,  # 2 2
                     (4, 3): 1,  # 2 2
                     (4, 4): 1,  # 2 2
                     (6, 2): 1,  # 2 2 2
                     (6, 3): 2,  # 3 3      2 2 2
                     (6, 6): 2}

prime_list = get_prime_list(1000)


def count_summation_prime(num, highest=None):
    if highest is None or highest >= num:
        highest = num
    if (num, highest) in num_highest_count.keys():
        return num_highest_count[(num, highest)]

    if num == 0:
        return 1

    if highest == 1:
        num_highest_count[(num, 1)] = 1
        return 1

    current_sum = 0
    for sub_highest in get_prime_list(limit=highest+1)[::-1]:
        new_num = num - sub_highest
        current_sum += count_summation_prime(new_num, sub_highest)
    num_highest_count[(num, highest)] = current_sum

    return num_highest_count[(num, highest)]


count_summation_prime(5)
# this function include the sum of 1 number (for convenience of calculation)
# the question ask for sum of at least 2 numbers, so subtract 1 from the answer
for i in range(100):
    temp = count_summation_prime(i)
    if temp >= 5000:
        print(i, temp)
        break
