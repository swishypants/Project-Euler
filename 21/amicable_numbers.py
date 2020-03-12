"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time

start_time = time.time()

def amicable(i, j):
    return i + j if divisors(i) == j and divisors(j) == i else 0


def divisors(num):
    divisor_sum = 1
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            divisor_sum += i + (num / i)
    if num / int(num ** 0.5) == int(num ** 0.5):
        divisor_sum += int(num ** 0.5)
    return divisor_sum


amicable_sum = 0
for i in range(1, 9999):
    for j in range(i + 1, 10000):
        amicable_sum += amicable(i, j)
print(amicable_sum)

print("Took %s seconds to complete" % (time.time() - start_time))
