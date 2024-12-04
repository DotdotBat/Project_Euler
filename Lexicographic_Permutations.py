import timeit
def factorial(n: int):
    if n < 2: return 1
    return n * factorial(n-1)





def lexicograph_digits_at(place:int, number_of_digits:int):
    digits = [i for i in range(number_of_digits)]
    result = []
    for _ in range(number_of_digits):
        number_of_digits = len(digits)
        number_of_permutations = factorial(number_of_digits)
        digit_index =  (number_of_digits * (place-1) )//number_of_permutations
        result.append(digits.pop(digit_index))
        place%= number_of_permutations//number_of_digits
    result = [str(i) for i in result]
    result_string = ""
    for dig in result:
        result_string+=dig
        
    return result_string

print(lexicograph_digits_at(1000000, 10))

print(timeit.timeit(lexicograph_digits_at(1000000, 10), number=1000000)/1000)
