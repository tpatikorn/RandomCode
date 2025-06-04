from euler.util import get_euler_data_filepath

matrix = [[131, 673, 234, 103, 18],
          [201, 96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524, 37, 331]]

matrix = []
with open(get_euler_data_filepath("p083_matrix.txt")) as data:
    for line in data.readlines():
        matrix.append([int(_) for _ in line.split(",")])

_memo = [[9999999 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

i_size = len(matrix)
j_size = len(matrix[0])

_memo[i_size - 1][j_size - 1] = matrix[i_size - 1][j_size - 1]
queue = [(i_size - 1, j_size - 1)]

while queue:
    i, j = queue.pop(0)
    adj = []
    if i == j == 0:
        continue
    if i > 0:
        adj.append((i - 1, j))
    if i < i_size - 1:
        adj.append((i + 1, j))
    if j > 0:
        adj.append((i, j - 1))
    if j < j_size - 1:
        adj.append((i, j + 1))

    for _adj in adj:
        if _memo[i][j] + matrix[_adj[0]][_adj[1]] < _memo[_adj[0]][_adj[1]]:
            _memo[_adj[0]][_adj[1]] = _memo[i][j] + matrix[_adj[0]][_adj[1]]
            queue.append(_adj)
    # print(*_memo, sep='\n')
    # print("---------------")

print(*_memo, sep='\n')
print(_memo[0][0])
