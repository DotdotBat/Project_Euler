# We shall say that an n-digit number is pandigital
# if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
from reusable_functions import is_prime
from itertools import permutations
def biggest_pandigital_prime():
    for digits_number in range(7, 0,-1):
        #staring from 8 digits and going down
        #there is no point checking the 9 digit numbers
        #they will all be divisible by nine
        #same goes for 8 digit numbers
        digits = [str(i) for i in range(1, digits_number+1)]
        perms = [int("".join(p)) for p in permutations(digits)]
        perms.sort(reverse=True)
        for num in perms:
            if is_prime(num):
                return num
        print(f"Checked all {digits_number}-digital permutations")
        print(f"None of them is a prime")
        
print(biggest_pandigital_prime())

