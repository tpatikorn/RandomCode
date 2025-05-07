_memo = [[0 for _w in range(2000)] for _h in range(2000)]


def count_rectangle(width, height):
    if width * height == 0:
        return 0
    if width == 1:
        return height * (height + 1) // 2
    if height == 1:
        return width * (width + 1) // 2

    if height > width:
        width, height = height, width

    if _memo[width][height] > 0:
        return _memo[width][height]

    rectangles = ((width * height)
                  + count_rectangle(width - 1, height)
                  + count_rectangle(width, height - 1)
                  - count_rectangle(width - 1, height - 1))
    _memo[width][height] = rectangles
    return rectangles


best_i = -1
best_j = -1
best = 1_999_000
for i in range(2000):
    for j in range(2000):
        new_count = count_rectangle(i, j)
        if abs(new_count - 2_000_000) < abs(best - 2_000_000):
            best_i, best_j, best = i, j, new_count
            print(i, j, new_count, "i*j = ", i * j)
        if new_count > 2_000_000:
            break
