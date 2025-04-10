import random
import math
import datetime


def merge_sort(input):
    if len(input) <= 1:
        return input
    # divide
    pivot = math.floor(len(input) / 2)
    left = input[0:pivot]  # 0...pivot-1 (ไม่รวม pivot)
    right = input[pivot: len(input)]  # pivot..สุดท้าย = pivot ... len-1 = ไม่รวมตัวที่ len

    # conquer
    left = merge_sort(left)
    right = merge_sort(right)

    # combine
    combined = []
    while True:
        if len(left) == 0:
            combined = combined + right
            break
        if len(right) == 0:
            combined = combined + left
            break
        if left[0] <= right[0]:
            combined.append(left[0])
            left.remove(left[0])
        else:
            combined.append(right[0])
            right.remove(right[0])
    return combined


for power in range(2, 8):
    maximum_number = 1000
    n = 10 ** power
    sample = [random.randint(0, maximum_number) for _ in range(n)]
    # print(sample)
    start = datetime.datetime.now()
    s = merge_sort(sample)
    sorted(sample)
    end = datetime.datetime.now()
    print(len(s), (end - start).microseconds)
