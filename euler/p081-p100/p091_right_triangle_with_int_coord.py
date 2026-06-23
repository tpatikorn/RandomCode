max_x = 50
max_y = 50

# right angle on x but NOT on y
triangle_count_x = max_x * max_y
print(triangle_count_x)

# right angle on y but NOT on x
triangle_count_y = max_x * max_y
print(triangle_count_y)

# right angle on origin
triangle_count_xy = max_x * max_y
print(triangle_count_xy)

triangle_count_x2 = 0
# right angle on x side but not on axis
tested_pairs = set()
for ix in range(1, max_x):
    for iy in range(1, max_y):
        for mult1 in range(1, max_x):
            p1 = (ix * mult1, iy * mult1)
            if (p1 not in tested_pairs) and (0 <= p1[0] <= max_x) and (0 <= p1[1] <= max_y):
                for mult2 in range(1, max_x):
                    tested_pairs.add(p1)
                    p2 = (ix * mult1 - iy * mult2,  iy * mult1 + ix * mult2)
                    if (0 <= p2[0] <= max_x) and (0 <= p2[1] <= max_y):
                        # print(p1, p2)
                        triangle_count_x2 += 1
                    else:
                        break
print(triangle_count_x2)

# right angle on y side but not on axis
triangle_count_y2 = triangle_count_x2
print(triangle_count_y2)

print(triangle_count_x + triangle_count_y +
      triangle_count_xy +
      triangle_count_x2 + triangle_count_y2)
