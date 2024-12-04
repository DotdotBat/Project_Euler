digits = [1]

def add_digit(digits: list[int], digit:int, rank:int):
    while( len(digits) < rank+1):
        digits.append(0)
    digits[rank]+=digit
    if digits[rank]>9:
        digits[rank]%=10
        add_digit(digits=digits, digit=1, rank=rank+1)


digits=[9,9]
add_digit(digits, 1, rank=0)
print(digits)


def add(digits:list[int], number:int, rank:int):
    while number>0:
        digit = number%10
        add_digit(digits, digit, rank)
        number= number//10
        rank+=1


digits = [6,6]
add(digits, number=44, rank=0)
print(digits)
add(digits, number=99, rank=1)
print(digits)

def multiply(digits:list[int], number:int):
    additions = [(number-1)*digit for digit in digits]
    for rank, addition in enumerate(additions):
        add(digits, number=addition, rank=rank)

digits = [3,3,3]
multiply(digits, 4)
print(digits, 333*4)

def compute_factorial(n):
    digits = [1]
    for i in range(n):
        multiply(digits, i+1)
    return digits

print(compute_factorial(3))
print(compute_factorial(5))
print(compute_factorial(10))
f_100 = compute_factorial(100)
print(sum(f_100))

    