from euler.util import digit_count

total_count = 0
for i in range(1, 10):
    powerful_digit_count = [pow(i, _) for _ in range(1, 30) if digit_count(pow(i, _)) == _]
    print(i, len(powerful_digit_count), powerful_digit_count)
    total_count += len(powerful_digit_count)
print(total_count)