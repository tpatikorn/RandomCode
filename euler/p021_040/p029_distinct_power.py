numbers = set()
for a in range(2, 101):
    for b in range(2, 101):
        numbers.add(a ** b)
        numbers.add(b ** a)
print(len(numbers))
