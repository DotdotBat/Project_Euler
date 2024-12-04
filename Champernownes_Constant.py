# An irrational decimal fraction is created by concatenating
# the positive integers: 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If d_n represents the nth digit of the fractional part,
# find the value of the following expression:
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

#lets forget about irrational fractions, 
# that is just a fancy way to concatenate 
# the digits of the natural numbers. 
# The first 9 numbers have 1 digit
# the next 90 numbers have 2 digits
# the next 900 numbers have 3 digits...
from reusable_functions import rank_ordered_digits
import math
def nth_digit(n:int):
    rank = 1
    highest_digit_place_of_previous_rank = 0
    
    number_range = 10**(rank-1)-1, 10**rank - 1
    highest_digit_place_of_current_rank = 9
    while n > highest_digit_place_of_current_rank:
        rank+=1
        highest_digit_place_of_previous_rank = highest_digit_place_of_current_rank
        number_range = 10**(rank-1)-1, 10**rank - 1
        a, b = number_range
        number_amount = b - a
        highest_digit_place_of_current_rank+= number_amount * rank
    a, b = number_range
    number = a + math.ceil((n - highest_digit_place_of_previous_rank)/rank)
    digit_place = (n - highest_digit_place_of_previous_rank) % rank
    digits = rank_ordered_digits(number)
    digits.reverse()
    digit = digits[digit_place-1]
    return digit


places = [10**i for i in range(7)]
digits = list(map(nth_digit, places))
product = math.prod(digits)
print(product)

# As an experiment I asked GPT4o for feedback. 
# Most of it was BS,
#  but one claim I have to verify. 
# its that
def get_digits_str(num: int) -> list[int]:
    return [int(d) for d in str(num)]
#via string manipulation will be faster
#  than my modulo method
def get_digits_modulo(num:int)->list[int]:
    digits = []
    while num>0:
        last_digit = num%10
        digits.append(last_digit)
        num= num//10
    digits.reverse()
    return digits

from timeit import timeit\

def my_method():
    n = 123456
    for i in range(n):
        get_digits_modulo(i)

def other_method():
    n = 123456
    for i in range(n):
        get_digits_str(i)

print( "Via strings", timeit(other_method,number=100))
print( "Via modulo", timeit(my_method, number=100))

#output
# Via strings 19.44288210000377
# Via modulo 13.681246799998917

# I am actually surprized by how close they are.
# well, if you think about it,
#  even though the str handles much more scenarios
# under the hood of this function,
# the manipulaitons they are performing 
# are about the same 