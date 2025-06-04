from functools import reduce
from operator import mul


def find_min_product_sum(current_array=None):
    if current_array is None:
        return None
    if max(current_array) > len(current_array):
        return None

    best_solution = None
    for _ in range(min(len(current_array), 10)):
        if _ > 0 and current_array[_] == current_array[_-1]:
            continue
        new_array = current_array.copy()
        new_array[_] += 1
        prd_arr = reduce(mul, new_array, 1)
        sum_arr = sum(new_array)
        if prd_arr == sum_arr:
            if best_solution is None:
                best_solution = new_array
            elif sum(best_solution) > sum_arr:
                # print("BEST!", best_solution)
                best_solution = new_array
        elif prd_arr > sum_arr:
            continue
        else:
            new_solution = find_min_product_sum(new_array)
            if new_solution is not None:
                if best_solution is None:
                    best_solution = new_solution
                elif sum(best_solution) > sum_arr:
                    # print("BEST!", best_solution)
                    best_solution = new_solution
    return best_solution


all_sums = set()
for k in range(2, 12000):
    sol = find_min_product_sum([1 for _ in range(k)])
    print(k, sum(sol), sol)
    all_sums.add(sum(sol))
