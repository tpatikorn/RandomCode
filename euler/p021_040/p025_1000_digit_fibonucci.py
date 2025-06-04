last = 1
this = 1
index = 2

while this < 10 ** (1000 - 1):  # 1000 digits are more than 10^999
    _ = this
    this = last + this
    last = _
    index = index + 1
    print(index, this, this / last)
print(index)
