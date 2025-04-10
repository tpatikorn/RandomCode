max_i, max_cnt = 0, 0
for i in range(10, 1000):
    cnt = 0
    for a in range(1, i):
        for b in range(a + 1, i):
            c = i - a - b
            if c < b:
                break
            if c ** 2 == a ** 2 + b ** 2:
                # print(i, a, b, c)
                cnt = cnt + 1
    if cnt >= max_cnt:
        max_i = i
        max_cnt = cnt
        print(max_i, max_cnt)
