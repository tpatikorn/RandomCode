triangle_numbers = [_ * (_ + 1) / 2 for _ in range(1, 100)]

cnt = 0
with open("../data/p042_words.txt") as data:
    words = data.readline().replace("\"", "").split(",")
    for word in words:
        val = sum([ord(_) - 64 for _ in str(word)])
        if val in triangle_numbers:
            # print(val)
            cnt = cnt + 1
print(cnt)
