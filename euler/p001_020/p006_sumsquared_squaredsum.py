# direct
max = 100
sum_squared = 0
squared_sum = 0
for i in range(1, max + 1):
    sum_squared = sum_squared + i ** 2
    squared_sum = squared_sum + i

squared_sum = squared_sum ** 2
print(squared_sum - sum_squared)

# map
numbers = list(range(1, max + 1))
sum_squared = sum(map(lambda _: _ ** 2, numbers))
squared_sum = sum(numbers) ** 2

print(squared_sum - sum_squared)

# math way
result = 0
for i in range(1, max + 1):
    for j in range(1, max + 1):
        if i == j:
            continue
        result = result + i * j
print(result)
