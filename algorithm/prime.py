from datetime import datetime

student_id = (353552211) % 100


# เอาชื่อใส่มาในไฟล์ด้วยยยยยยยยยยย

def find_prime(target):
    total_steps = 0
    start = datetime.now()
    prime_count = 0
    current_number = 2
    while True:
        is_prime_bool, steps = is_prime(current_number)
        total_steps = total_steps + steps
        if is_prime_bool:
            prime_count = prime_count + 1
        if prime_count == target:
            end = datetime.now()
            return target, current_number, end - start, total_steps
        current_number = current_number + 1


def run_find_prime():
    print(find_prime(100 + student_id))
    print(find_prime(200 + student_id))
    print(find_prime(300 + student_id))
    print(find_prime(400 + student_id))
    print(find_prime(500 + student_id))
    print(find_prime(600 + student_id))
    print(find_prime(700 + student_id))
    print(find_prime(800 + student_id))
    print(find_prime(900 + student_id))
    print(find_prime(1000 + student_id))
    print(find_prime(2000 + student_id))
    print(find_prime(3000 + student_id))
    print(find_prime(4000 + student_id))
    print(find_prime(5000 + student_id))
    print(find_prime(6000 + student_id))
    print(find_prime(7000 + student_id))
    print(find_prime(8000 + student_id))
    print(find_prime(9000 + student_id))
    print(find_prime(10000 + student_id))


# version 4
from datetime import datetime
import math


def is_prime(N):
    count_step = 0
    for i in range(2, round(math.sqrt(N) + 1), 2):
        count_step = count_step + 1
        if N % i == 0:
            return False, count_step
    return True, count_step


run_find_prime()

print(find_prime(1000000))
