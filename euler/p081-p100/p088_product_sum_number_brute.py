from functools import reduce
from operator import mul


def product(l):
    return reduce(mul, l, 1)


def find_min_product_sum(length):
    # the queue of (list, ptr) where ptr tells which elt to explore next
    explore_queue = [([1 for _ in range(length)], 0)]
    while explore_queue:
        current_array, ptr = explore_queue.pop(0)
        current_array[ptr] += 1
        # if product exceeds sum, there's no coming back
        prod_minus_sum = product(current_array) - sum(current_array)
        if prod_minus_sum == 0:
            return current_array
        elif prod_minus_sum > 0:  # i.e. prod < sum
            continue
        elif ptr >= len(current_array):
            print("oh shit")
            continue
        else:
            if current_array[ptr] > current_array[ptr + 1]:
                explore_queue.append([current_array.copy(), ptr + 1])
            if ptr != 0:
                current_array[ptr] -= 1
                explore_queue.append([current_array.copy(), 0])


all_sums = set()
for k in range(2, 12000):
    sol = find_min_product_sum(k)
    print(k, sum(sol), sol)
    all_sums.add(sum(sol))
exit()
