"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143

factor = 2
factors_set = set()
product = 1

while product < 600851475143:
    while num % factor == 0:
        num /= factor
        product *= factor
        if factor not in factors_set:
            factors_set.add(factor)
    factor += 1

print(sorted(list(factors_set))[-1])