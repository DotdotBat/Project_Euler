factorials = []
for i in range(10):
    if i == 0:
        factorials.append(1)
        continue
    factorial = i * factorials[i-1]
    factorials.append(factorial)

upper_limit:int
for i in range(1, 100):
    a = 10**i
    b = factorials[9] * i
    if a>b:
        upper_limit = b
        break
        
from reusable_functions import rank_ordered_digits as get_digits
def digits_factorial_sum(num):
    digits = get_digits(num)
    return sum([factorials[i] for i in digits])

interesting_numbers = []

for i in range(10, upper_limit):
    if i == digits_factorial_sum(i):
        interesting_numbers.append(i)

print(interesting_numbers)
print(sum(interesting_numbers))