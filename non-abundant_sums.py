from reusable_functions import get_divisers
print("Non-Abundant sums")
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 
#  would be 
# , which means that 
#  is a perfect number.

# A number 
#  is called deficient if the sum of its proper divisors is less than 
#  and it is called abundant if this sum exceeds 
# .

# As 
#  is the smallest abundant number, 
# , the smallest number that can be written as the sum of two abundant numbers is 
# . By mathematical analysis, it can be shown that all integers greater than 28123 
#  can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def is_abundant(number)->bool:
    return number < sum(get_divisers(number))


upper_limit_abundant_numbers = (28123 + 10)
abundant_numbers = [i for i in range(1, upper_limit_abundant_numbers + 1) if is_abundant(i)]
print("found all abundant numbers under ", upper_limit_abundant_numbers)
print(abundant_numbers[:10])
def is_non_sum(number, verbose = False):
    for a in abundant_numbers:
        if a > 1 + number//2 :
            return True
        if is_abundant(number - a):
            if verbose: print(a, "+", number-a, "=", number)
            return False
    raise RuntimeError("checking ", number, " last abundant:", a)

check_list = [1, 2,12,24,32,42,100,16, 13]
for n in check_list:
    print(n, is_non_sum(n, verbose=True))



upper_limit_non_sums = 28123+5
non_sums = [i for i in range(1, upper_limit_non_sums) if is_non_sum(i)]
print(non_sums[:100], non_sums[-10:])
print("len non_sums", len(non_sums))
print("sum non_sums",sum(non_sums))