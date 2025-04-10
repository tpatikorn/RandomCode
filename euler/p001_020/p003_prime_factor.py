from math import sqrt, floor

primes = [2, 3]
n = 600851475143
for i in range(3, floor(sqrt(n)), 2):
    sqrt_i = sqrt(i)
    for p in primes:
        if i % p == 0:
            break
        if p > sqrt_i:
            if n % i == 0:
                n = n / i
                print("n is divisible by", i, "remaining", n)
                if n < i:
                    exit()
            primes.append(i)
            break

