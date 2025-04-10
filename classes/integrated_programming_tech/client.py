a = 2
b = 3
c = 8
d = 10
e = 14

for i in range(6, 1001):
    f = a + b + c + d + e
    a = b
    b = c
    c = d
    d = e
    e = f
    if i % 10 == 0 or i < 20:
        print(i, f)

print(i, f)
print(len(str(f)))
