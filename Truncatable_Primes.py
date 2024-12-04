# The number 3797 has an interesting property.
# Being prime itself.
# It is possible to continuously remove digits.
# From left to right, and remain prime.
# At each stage: 3797, 797, 97, and 7.
# Similarly, we can work from right to left.
# 3797, 379, 37, and 3.
# Find the sum of the only eleven primes.
# That are both truncatable from left to right.
# And right to left.
# NOTE: 2, 3, 5, and 7 are not considered.
# To be truncatable primes.

from reusable_functions import is_prime, count_digits
number_of_truncatable_primes = 11
one_digit_primes = [2,3,5,7]
possible_lowest_rank_digits = [1,3,7,9]

def truncate_left(num:int):
    highest_digit_rank = count_digits(num)
    return num % 10**(highest_digit_rank - 1)

def is_left_truncatable_prime(num): 
    while num>0:
        if not is_prime(num):
            return False
        num = truncate_left(num)
    return True

def construct_next_right_trancatable_primes(num:int)->list[int]:
    base = num*10
    primes = []
    for digit in possible_lowest_rank_digits:
        candidate = base + digit
        if is_prime(candidate):
            primes.append(candidate)
    return primes

truncatable_primes = []

search_space = one_digit_primes.copy()

digits = 1


while len(search_space)>0:#len(truncatable_primes) < number_of_truncatable_primes:
    digits+=1
    print(digits)
    more_digits_search_space = []
    for right_prime in search_space:
        more_digits_search_space.extend(construct_next_right_trancatable_primes(right_prime))
    search_space = more_digits_search_space
    for right_prime in search_space:
        if is_left_truncatable_prime(right_prime):
            truncatable_primes.append(right_prime)
            print(len(truncatable_primes), right_prime)
    
print(truncatable_primes)
print(sum(truncatable_primes))
print('\a')