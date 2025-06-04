from euler.p001_020 import p018_triangle_path

this_triangle = []
with open("../data/p067_triangle.txt") as data:
    for new_line in data:
        this_triangle.append([int(i) for i in new_line.split(" ")])

p018_triangle_path.find_path((0, 0), this_triangle)
