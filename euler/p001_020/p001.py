s = 0
for i in range(0, 1000):
    if i % 3 == 0:
        s = s + i
    elif i % 5 == 0:
        s = s + i
print(s)
