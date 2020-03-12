"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
import time

start_time = time.time()


def sum_of_divisors(num):
    if num == 1:
        return 1
    elif num <= 0:
        return -1

    divisors = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors += i + (num / i)
    if num / int(math.sqrt(num)) == int(math.sqrt(num)):
        divisors -= int(math.sqrt(num))
    return divisors


def is_abundant(num):
    return True if sum_of_divisors(num) > num else False


def is_sum_of_abundant_numbers(num):
    for i in abundant_numbers:
        if num - i in abundant_numbers:
            return True
    return False


LOWER_LIMIT = 12
UPPER_LIMIT = 28123

# get all abundant numbers
abundant_numbers = set()
for i in range(1, UPPER_LIMIT + 1):
    if is_abundant(i):
        abundant_numbers.add(i)

# calculate by summing all numbers that can't be described as the sum of 2 abundant numbers
res = 0
for i in range(1, UPPER_LIMIT):
    if not is_sum_of_abundant_numbers(i):
        res += i
print(res)

print("Took %s seconds to complete" % (time.time() - start_time))
