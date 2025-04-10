import datetime


def insertion_sort(array):
    swap_count = 0
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
            swap_count = swap_count + 1
        array[i + 1] = key
    return swap_count


for array_size in range(1000, 10000, 1000):
    input_array = list(range(array_size, 0, -1))
    # random.shuffle(input_array)
    # print(input_array)

    print(array_size)
    before = datetime.datetime.now()
    print(insertion_sort(input_array))
    after = datetime.datetime.now()
    print(after - before)
    # print(input_array)
