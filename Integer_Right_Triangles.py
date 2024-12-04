# If p is the perimeter of a right angle triangle 
# with integral length sides, {a, b, c}, 
# there are exactly three solutions for p = 120.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}

# For which value of p ≤ 1000, 
# is the number of solutions maximised?
import math
p_max = 1000
lists_of_solutions_by_p = [[].copy() for _ in range(p_max+1+1)]

def is_perfect_square(num:int):
    sqrt = math.sqrt(num)
    return sqrt.is_integer()

for a in range(1, p_max//2):
    aa = a*a
    for b in range(1, a+1):
        bb = b*b
        cc = a*a + b*b
        if not is_perfect_square(cc):
            continue
        c = int(math.sqrt(cc))
        p = a + b + c
        if p > p_max:
            break
        list_of_solutions_with_p = lists_of_solutions_by_p[p]
        solution = (a, b, c)
        list_of_solutions_with_p.append(solution)
print("Start: +++++++++++++++++ ")

lists_of_solutions_by_p.sort(key=len, reverse=False)
for list_of_solutions in lists_of_solutions_by_p:
    l = len(list_of_solutions)
    if l == 0:
        continue
    a, b, c = list_of_solutions[0]
    p = a + b + c 
    print(l, " solutions for perimeter ", p)
    print(list_of_solutions)
