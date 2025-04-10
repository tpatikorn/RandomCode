last = 1
fib = 2
s = 0
while fib < 10000000:
    if fib % 2 == 0:
        s = s + fib
    _ = last
    last = fib
    fib = _ + last
    print(fib)
print(s)
