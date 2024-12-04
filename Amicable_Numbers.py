import math
from reusable_functions import get_divisers



print(get_divisers(220))
print(sum(get_divisers(220)))

amicable_divisers = []

for i in range(4, 10000):
    sum_i = sum(get_divisers(i))
    if sum_i>i:
        sum_sum_i = sum(get_divisers(sum_i))
        if sum_sum_i == i:
            amicable_divisers.append(i)
            amicable_divisers.append(sum_i)
print(amicable_divisers)
print(sum(amicable_divisers))

print(get_divisers(12))