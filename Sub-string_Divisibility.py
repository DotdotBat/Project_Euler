# The number, 1406357289, is a 0 to 9 pandigital number.
# It has a sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
# d2d3d4 = 406 is divisible by 2.
# d3d4d5 = 063 is divisible by 3.
# d4d5d6 = 635 is divisible by 5.
# d5d6d7 = 357 is divisible by 7.
# d6d7d8 = 572 is divisible by 11.
# d7d8d9 = 728 is divisible by 13.
# d8d9d10 = 289 is divisible by 17.
# Find the sum of all 0 to 9 pandigital numbers with this property.

#note that there is no d1d2d3 triad. 
#get the first primes up to 17
from reusable_functions import primes_list, extend_primes_list_up_to
extend_primes_list_up_to(18)
assert len(primes_list) == 7

from itertools import permutations

candidates = []

for p in permutations('1234567890'):
    is_divisible = True
    for i in range(2-1, 8+1-1):
        s = p[i] + p[i+1] + p[i+2]
        num = int(s)
        prime = primes_list[i-1]
        if num%prime != 0:
            is_divisible = False
            break
    if is_divisible:
        num = int("".join(p))
        candidates.append(num)

print(len(candidates))
print(sum(candidates))