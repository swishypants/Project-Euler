"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

start_time = time.time()

sum_multiples = 0

for num in range(1000):
    if num % 3 == 0 or num % 5 == 0 and num % 15 != 0:
        sum_multiples += num

print(sum_multiples)

print("Took %s seconds to complete" % (time.time() - start_time))
