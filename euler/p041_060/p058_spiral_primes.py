from euler.util import is_probable_prime, get_prime_list

limit = 30_000
start = 3
spiral_primes = 0
for i in range(start, limit, 2):
    total_count = i * 2 - 1
    if is_probable_prime(i * i - 1 * (i - 1)):
        spiral_primes += 1
    if is_probable_prime(i * i - 2 * (i - 1)):
        spiral_primes += 1
    if is_probable_prime(i * i - 3 * (i - 1)):
        spiral_primes += 1
    if i % 200 == 1:
        print(i, spiral_primes, total_count, spiral_primes / total_count)
    if spiral_primes / total_count < 0.1:
        print(i, spiral_primes, total_count, spiral_primes / total_count)
        break
