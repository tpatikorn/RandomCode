import random


def bubble_sort(array):
    compare_count = 0
    swap_count = 0
    swap = True
    while swap:
        swap = False
        for i in range(0, len(array) - 1):
            compare_count = compare_count + 1
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
                swap_count = swap_count + 1
                swap = True
    print(compare_count, swap_count)


for array_size in range(1000, 10000, 1000):
    input_array = list(range(array_size, 0, -1))
    #random.shuffle(input_array)
    # print(input_array)
    print(array_size)
    bubble_sort(input_array)
    # print(input_array)
