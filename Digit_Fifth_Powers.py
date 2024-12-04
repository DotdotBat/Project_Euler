#Find the sum of all the numbers 
# that can be written 
# as the sum of fifth powers of their digits.

from reusable_functions import rank_ordered_digits

def power_digit_sum(num:int, power:int):
    digits = rank_ordered_digits(num)
    return sum([d**power for d in digits])


upper_bound = 10**6
#why stop at six digits?
#because the biggest 7 digit number 9999999 has a digits fifth power sum of
assert power_digit_sum(9999999, 5) == 413343
# which is a 6 digit number. 
# So every 7 digit number can't have a digit 5 power sum equal to itself. 
# and while every digit grows the number exponentially
# the digit sum grows linearly.


first = []
second = []
third = []
fourth = []
fifth = []
for i in range(2, upper_bound):
    if i == power_digit_sum(i, 1):
        first.append(i)
    if i == power_digit_sum(i, 2):
        second.append(i)
    if i == power_digit_sum(i, 3):
        third.append(i)
    if i == power_digit_sum(i, 4):
        fourth.append(i)
    if i == power_digit_sum(i, 5):
        fifth.append(i)

print("Results")
print("first:", first)
print("sum:", sum(first))
print("second:", second)
print("sum:", sum(second))
print("third:", third)
print("sum:", sum(third))
print("fourth:", fourth)
print("sum:", sum(fourth))
print("Fifth:", fifth)
print("sum:", sum(fifth))

