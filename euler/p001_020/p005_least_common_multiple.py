numbers = list(range(1, 21))
result = 1

for i in range(0, len(numbers)):
    n = numbers[i]
    numbers = [_ / n if _ % n == 0 else _ for _ in numbers]
    print(n, numbers)
    result = result * n

print(result)
