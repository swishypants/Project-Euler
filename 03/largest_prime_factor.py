"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time

start_time = time.time()

num = 600851475143

factor = 2
prime_factors = set()
product = 1

while product < 600851475143:
    while num % factor == 0:
        num /= factor
        product *= factor
        if factor not in prime_factors:
            prime_factors.add(factor)
    factor += 1

print(sorted(prime_factors)[-1])

print("Took %s seconds to complete" % (time.time() - start_time))
