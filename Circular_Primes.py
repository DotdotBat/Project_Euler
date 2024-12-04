# The number 197 is called a circular prime.
# All rotations of the digits: 197, 971, and 719 are prime.
# There are thirteen such primes below 100.
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from reusable_functions import is_prime, primes_list, extend_primes_list_up_to, count_digits
import math



def rotate(num:int)->int:
    lowest_digit = num%10
    highest_rank = count_digits(num)
    num = num//10
    num+= lowest_digit * 10**(highest_rank-1)
    return num

def get_rotations(num):
    result = []
    for _ in range(count_digits(num)):
        result.append(num)
        num = rotate(num)
    return result

def is_circular_prime(num):
    return all(is_prime(r) for r in get_rotations(num))


circular_primes = set([2,5])
possible_digits = [1,3,7,9]

def my_function(num:int, limit:int):
    if num> limit:
        return
    if is_circular_prime(num):
        circular_primes.update(get_rotations(num))
    for d in possible_digits:
        n = 10*num + d
        if n <= limit:
            my_function(n, limit)

my_function(0, limit=1000000)
sorted = list(circular_primes)
sorted.sort()
print(sorted)
print(len(sorted))
    

# for p in range(1, 5):
#     for n in range(1, 10):
#         num = n*10**p
#         print(num)
#         is_prime(num)

import winsound
winsound.Beep(440, 3000)
