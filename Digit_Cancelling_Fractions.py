from reusable_functions import rank_ordered_digits
from math import isclose
funny_numerators = []
funny_denominators = []

def remove_common_element_pairs(l1:list, l2:list):
    l1_c, l2_c = l1.copy(), l2.copy()
    for e in l1:
        if e in l2_c:
            l1_c.remove(e)
            l2_c.remove(e)
    return l1_c, l2_c

def count_common_element_pairs(l1:list, l2:list):
    l1_c, l2_c = remove_common_element_pairs(l1, l2)
    removed_element_count = len(l1) - len(l1_c)
    return removed_element_count

# iterate over all the fractions
for denominator in range(11, 100):
    for numerator in range(10, denominator):
        numerator_digits = rank_ordered_digits(numerator)
        denominator_digits = rank_ordered_digits(denominator)
        
        assert len(numerator_digits) == len(denominator_digits) == 2
        #Check if only one digit canceles out
        if count_common_element_pairs(numerator_digits, denominator_digits) == 1:
            #Does the remaining fraction equal to the original? 
            num_digits, den_digits = remove_common_element_pairs(numerator_digits, denominator_digits)
            num, den = num_digits[0], den_digits[0]
            
            if den != 0 and denominator//den != 10 and isclose(numerator/denominator, num/den):
                funny_numerators.append(numerator)
                funny_denominators.append(denominator)

            
for i in range(len(funny_denominators)):
    print(funny_numerators[i], '/', funny_denominators[i])