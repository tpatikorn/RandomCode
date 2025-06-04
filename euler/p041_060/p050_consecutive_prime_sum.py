from euler import util

primes = util.get_prime_list(limit=1_000_000)

max_len = 0
for i in range(0, 2000):
    for j in range(2000, 1, -1):
        if (j - i + 1) <= max_len:
            break
        elif sum(primes[i:j + 1]) < 1_000_000 and util.is_prime(sum(primes[i:j + 1])):
            max_len = j - i + 1
            print(i, j, sum(primes[i:j + 1]))
            break
