def long_division_step(numerator:int, diviser:int):
    digit = numerator//diviser
    remainder = numerator % diviser
    return digit, remainder


def get_reciprocal_cycle(numerator:int, diviser:int):
    digits = []
    remainders = []
    while(True):
        if numerator == 0:
            cycle = []
            return cycle, remainders
        digit, remainder = long_division_step(numerator, diviser)
        digits.append(digit)
        if remainder in remainders:
            index = remainders.index(remainder)
            cycle = digits[index+1:]
            return cycle, remainders
        remainders.append(remainder)
        numerator = 10*remainder

longest = [], 0, 0, 0,[]
for d in range(1, 999):
    _, longest_len_so_far, _, _ ,_ = longest
    cycle, _ = get_reciprocal_cycle(1,d)
    if len(cycle) > longest_len_so_far:
        cycle, remainders = get_reciprocal_cycle(1, d)
        length = len(cycle)
        numerator = 1
        diviser = d
        longest = (cycle, length, numerator, diviser, remainders)

cycle, length, numerator, diviser,remainders = longest
print("LONGEST")
# print("cycle:", cycle)
print("length:", length)
print("numerator:", numerator)
print("diviser:", diviser)
# print("remainders:", remainders)

