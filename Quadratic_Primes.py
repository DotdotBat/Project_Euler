# Euler discovered a remarkable quadratic formula:
#  n^2 + n + 41. 
# It turns out that the formula will produce 40 primes 
# for the consecutive integer values 0 ≤ n ≤ 39.
#  However, when n = 40, 40^2 + 40 + 41 is divisible by 41, 
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, 
# which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
#  The product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form: 
# n^2 + an + b, 
# where |a| < 1000 and |b| ≤ 1000 
# find the product of the coefficients, a and b, 
# for the quadratic expression that produces the maximum number of primes
#  for consecutive values of n, starting with n = 0.


def quadratic_formula_result(a:int, b:int, n:int)->int:
    return n*n + a*n + b

from reusable_functions import is_prime, primes_list, biggest_checked_number_so_far

def count_streak(a, b):
    n = 0
    while(is_prime(quadratic_formula_result(a, b, n))):
        n+=1
    return n

print(1, 41, count_streak(1, 41))
print(-79, 1601, count_streak(-79, 1601))
print("primes_list_length = ", len(primes_list))
print("biggest_checked_number = ", biggest_checked_number_so_far)

a, b, streak = 0, 0, 0
best = a, b, streak
for a in range(-998, 1000):
    for b in range(-999, 1001):
        _, _, best_steak_so_far = best
        if best_steak_so_far < count_streak(a, b):
            best = a, b, count_streak(a, b)

a, b, streak = best
print("-------------------")
print("found ", len(primes_list)," primes")
print("largest checked number is: ", biggest_checked_number_so_far)
print("largest found prime is: ", primes_list[-1])
print("best found indexes")
print("a:", a, " b:", b )
print("streak:", streak)
print("a*b = ", a*b)
