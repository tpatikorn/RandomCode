from euler.util import get_euler_data_filepath

matrix = []
with open(get_euler_data_filepath("p082_matrix.txt")) as data:
    for line in data.readlines():
        matrix.append([int(_) for _ in line.split(",")])

# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]

i_size = len(matrix)
j_size = len(matrix[0])

_memo = [[999999999 for _j in range(j_size)] for _i in range(i_size)]


def path_sum_three_ways_bottom_up():
    for i in range(0, i_size):
        _memo[i][j_size - 1] = matrix[i][j_size - 1]

    for j in range(j_size - 2, 0 - 1, -1):
        has_change = True
        while has_change:
            has_change = False
            for i in range(0, i_size):
                # print("<<< i, j", i, j)
                right = _memo[i][j + 1] if j < j_size - 1 else 999999999
                up___ = _memo[i - 1][j] if i > 0 else 999999999
                down_ = _memo[i + 1][j] if i < i_size - 1 else 999999999
                new_val = matrix[i][j] + min(right, down_, up___)
                if new_val < _memo[i][j]:
                    _memo[i][j] = new_val
                    has_change = True
    return _memo


path_sum_three_ways_bottom_up()
# print(*path_sum_three_ways_bottom_up(), sep="\n")
print(min([_[0] for _ in _memo]))
