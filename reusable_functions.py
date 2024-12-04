# if I notice that I already implemented something for one task 
# and need it for another, 
# I move it here

import math

def get_divisers(n:int)->set[int]:
    higher_bound = 1+math.ceil(math.sqrt(n))
    divisers = {1}
    if n == 2:
        return {1}
    for i in range(2, higher_bound):
        if n%i == 0:
            divisers.add(i)
            other_diviser = n//i
            divisers.add(other_diviser)
    return divisers

primes_list = [2, 3, 5, 7] 

biggest_checked_number_so_far = 8
def extend_primes_list_up_to(num):
    global biggest_checked_number_so_far, primes_list
    if num<biggest_checked_number_so_far:
        return
    for i in range(biggest_checked_number_so_far+1, num+1):
        if all(i%smaller_prime!=0 for smaller_prime in primes_list):
            primes_list.append(i)
    biggest_checked_number_so_far = num

def is_prime(num:int)->bool:
    global sorted_primes_list, biggest_checked_number_so_far
    if num<=1:
        return False
    if num < biggest_checked_number_so_far:
        return num in primes_list
    upper_bound = math.floor(math.sqrt(num))
    extend_primes_list_up_to(upper_bound)
    for prime in primes_list:
        if num % prime == 0:
            return False
        if prime > upper_bound:
            break
    return True    
    
    
       
def rank_ordered_digits(num:int)->list[int]:
    digits = get_digits()
    digits.reverse()
    return digits

def count_digits(num):
    if num ==0:
        return 1
    log10 = math.log10(abs(num))
    count = math.floor(log10) +1 
    return count

def get_digits(num:int)->list[int]:
    digits = []
    while num>0:
        last_digit = num%10
        digits.append(last_digit)
        num= num//10
    digits.reverse()
    return digits