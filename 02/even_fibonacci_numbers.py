"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.
"""

prev = 1
curr = 2
sum_even = 0

while curr < 4000000:
    if curr % 2 == 0:
        sum_even += curr

    curr, prev = prev + curr, curr

print(sum_even)