"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

max_palindrome = 0

def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

for num1 in range(100, 1000):
    for num2 in range(num1, 1000):
        product = num1 * num2
        if is_palindrome_number(product):
            max_palindrome = max(max_palindrome, product)

print(max_palindrome)