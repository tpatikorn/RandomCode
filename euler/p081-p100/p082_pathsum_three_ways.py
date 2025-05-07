from euler.util import get_euler_data_filepath

_memo = {}

matrix = []
with open(get_euler_data_filepath("p082_matrix.txt")) as data:
    for line in data.readlines():
        matrix.append([int(_) for _ in line.split(",")])

matrix = [[131, 673, 234, 103, 18],
          [201, 96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524, 37, 331]]


def path_sum_three_ways_top_down(i=0, j=0):
    print("<<< i, j", i, j)
    if (i, j) in _memo.keys():
        return _memo[(i, j)]

    if j == len(matrix) - 1:
        _memo[(i, j)] = matrix[i][j]
        return matrix[i][j]

    if j < len(matrix[0]) - 1:
        right_path = matrix[i][j] + path_sum_three_ways_top_down(i, j + 1)
    else:
        right_path = 9999999999

    if i < len(matrix) - 1:
        down_path = matrix[i][j] + path_sum_three_ways_top_down(i + 1, j)
    else:
        down_path = 9999999999

    if i > 0:
        up_path = matrix[i][j] + path_sum_three_ways_top_down(i - 1, j)
    else:
        up_path = 9999999999

    _memo[(i, j)] = min(right_path, down_path, up_path)
    return min(right_path, down_path, up_path)



min_path = 9999999999
for k in range(len(matrix)):
    _memo = {}
    result = path_sum_three_ways_top_down(k, 0)
    if result < min_path:
        min_path = result
        print(min_path)
