def selection_sort(array):
    for i in range(0, len(array)):
        min_elt = array[i]
        min_index = i
        for j in range(i, len(array)):
            if array[j] < min_elt:
                min_elt = array[j]
                min_index = j
        array[min_index] = array[i]
        array[i] = min_elt


input_array = [5, 3, 4, 1, 5, 6, 7, 1, 2, 7, 3]
selection_sort(input_array)
print(input_array)
