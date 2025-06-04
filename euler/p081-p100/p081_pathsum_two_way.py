from euler.util import get_euler_data_filepath

_memo = {}

matrix = []
with open(get_euler_data_filepath("p081_matrix.txt")) as data:
    for line in data.readlines():
        matrix.append([int(_) for _ in line.split(",")])


def path_sum_two_ways(i=0, j=0):
    if (i, j) in _memo.keys():
        return _memo[(i, j)]

    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        _memo[(i, j)] = matrix[i][j]
        return matrix[i][j]

    if i < len(matrix) - 1:
        right_path = matrix[i][j] + path_sum_two_ways(i + 1, j)
    else:
        right_path = 9999999999

    if j < len(matrix[0]) - 1:
        bottom_path = matrix[i][j] + path_sum_two_ways(i, j + 1)
    else:
        bottom_path = 9999999999

    _memo[(i, j)] = min(right_path, bottom_path)
    return min(right_path, bottom_path)


print(path_sum_two_ways())
