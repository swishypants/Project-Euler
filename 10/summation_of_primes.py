"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
import time

start_time = time.time()


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


sum_primes = 0
for i in range(2, 2000000):
    if is_prime(i):
        sum_primes += i
print(sum_primes)

print("Took %s seconds to complete" % (time.time() - start_time))
