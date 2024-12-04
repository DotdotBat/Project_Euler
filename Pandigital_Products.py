from reusable_functions import rank_ordered_digits
from math import sqrt, floor

# Find the sum of all products whose multiplicand/multiplier/product 
# identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.



def digits_are_nonrepeating(digits:list[int]):
    digits = digits.copy()
    while(len(digits)>1):
        digit = digits.pop()
        if digit in digits:
            return False
    return True

upper_search_bound = floor(sqrt(sqrt(10**11)))

products = set()
for multiplicant in range(1, upper_search_bound):
    multiplicant_digits = rank_ordered_digits(multiplicant)
    if not digits_are_nonrepeating(multiplicant_digits):
        continue
    for multiplier in range(1, 10**10):
        product = multiplicant * multiplier
        expression_digits = rank_ordered_digits(multiplicant) + rank_ordered_digits(multiplier) + rank_ordered_digits(product)
        expression_length = len(expression_digits)
        if expression_length < 9:
            continue
        if expression_length > 9:
            break
        if 0 in expression_digits:
            continue
        if digits_are_nonrepeating(expression_digits):
            products.add(product)
            print(multiplicant, " X ", multiplier, " = ", product)

print("found ", len(products), " products")

print("sum is: ", sum(products))

