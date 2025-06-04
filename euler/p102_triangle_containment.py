from euler import util

with open("data/p102_triangle.txt") as data:
    cnt = 0
    for line in data:
        x1, y1, x2, y2, x3, y3 = [float(_) for _ in line.split(",")]
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)
        l12 = util.find_line(p1, p2)
        l23 = util.find_line(p2, p3)
        l31 = util.find_line(p3, p1)

        good_lines = []
        if y1 <= l12[1] <= y2 or y1 >= l12[1] >= y2:
            good_lines.append(l12)
        if y2 <= l23[1] <= y3 or y2 >= l23[1] >= y3:
            good_lines.append(l23)
        if y3 <= l31[1] <= y1 or y3 >= l31[1] >= y1:
            good_lines.append(l31)

        if len(good_lines) == 2 and good_lines[0][1] * good_lines[1][1] <= 0:
            print(p1, p2, p3)
            cnt = cnt + 1

print(cnt)
