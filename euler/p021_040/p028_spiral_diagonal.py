total = 1
curr = 1
for i in range(3, 1002, 2):
    for _ in range(0, 4):
        curr = curr + i - 1
        total = total + curr
    print(i, total)
