#What is the index of the first term in the Fibonacci sequence 
#to contain 1000 digits?
import math
from math import log10, log, sqrt, ceil
number_of_digits = 1000
log10_of_1000_digit_number = number_of_digits-1


phi = (1 + sqrt(5)) / 2
#I have manipulated the formula a bit, and this was carried out of the brakets
other_term = log(5, phi)/2 
index = ceil(log10_of_1000_digit_number/log10(phi) - 1/log10_of_1000_digit_number + other_term)
print(index)