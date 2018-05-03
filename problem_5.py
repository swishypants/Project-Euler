"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

factor_map = {}
for i in range(2, 21):
    num = i
    factor_map[i] = {}
    for j in range(2, i):
        while num % j == 0:
            if j in factor_map[i]:
                factor_map[i][j] += 1
            else:
                factor_map[i][j] = 1
            num //= j
        if num == 1:
            break
    if not factor_map[i]:
        factor_map[i][i] = 1

factor_totals = {}
for num in factor_map:
    for factor in factor_map[num]:
        if factor in factor_totals:
            factor_totals[factor] = max(factor_totals[factor], factor_map[num][factor])
        else:
            factor_totals[factor] = factor_map[num][factor]

product = 1
for factor in factor_totals:
    for i in range(factor_totals[factor]):
        product *= factor

print(product)