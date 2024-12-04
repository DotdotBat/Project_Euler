# Take the number 192 and multiply it by 1, 2, and 3.
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# Concatenate the products: 192384576
# This is the concatenated product of 192 and (1,2,3).
# Another example: Start with 9 and multiply by 1, 2, 3, 4, 5.
# 9 × 1 = 9
# 9 × 2 = 18
# 9 × 3 = 27
# 9 × 4 = 36
# 9 × 5 = 45
# Concatenate the products: 918273645
# This is the concatenated product of 9 and (1,2,3,4,5).
# Find the largest 1 to 9 pandigital 9-digit number.
# It should be formed as the concatenated product.
# The integer should be multiplied with (1,2,...,n).

#can we go downward? 
# There aren't that many pandigital 
# numbers bigger than 918273645
#first one must be 9, second should be higher than 1

#def concatenate_numbers
#def concatenate_products_till_at_least_nine_digit
#is pandigital?

from itertools import permutations
simple = "12345678"
digits_8_permutations = permutations(simple, 8)
pandigital_numbers = []
for eight_digit_character_permutation in digits_8_permutations:
    chars = ['9'] + list(eight_digit_character_permutation)
    number = int("".join(chars))
    pandigital_numbers.append(number)
pandigital_numbers.sort(reverse=True)

def can_be_represented_as_product_concatenation(number:int)->bool:
    s = str(number)
    for i in range(1, len(s)):
        mult = int(s[:i])
        contact_products = ""
        product_number = 0
        while len(contact_products)<9:
            product_number+= 1
            product = mult*product_number
            contact_products += str(product)
        if contact_products == s:
            print(mult,product_number, s)
            return True
    return False

result = [p for p in pandigital_numbers if can_be_represented_as_product_concatenation(p)]
print(len(result))
print(result[:5])



