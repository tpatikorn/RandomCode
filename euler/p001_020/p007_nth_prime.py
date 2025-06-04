from math import sqrt
from datetime import datetime
primes = [2, 3]
n = 1000001
start = datetime.now()
for i in range(5, n, 2):
    sqrt_i = sqrt(i)
    for p in primes:
        if i % p == 0:
            break
        if p > sqrt_i:
            primes.append(i)
            if len(primes) == 10001:
                print(i, primes)
                end = datetime.now()
                print(end - start)
                exit()
            break
