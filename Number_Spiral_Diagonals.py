spiral_width = 1001 #must be odd
layers = (spiral_width - 1)//2 

#first approach is to just constract the diagonals and sum them
diagonals = [[], [], [], []]
current_number = 1
for i in range(1, layers+1):
    step = 2*i
    for j in range(4):
        current_number+=step
        diagonals[j].append(current_number)
print(sum([sum(d) for d in diagonals]) + 1)
for d in diagonals:
    print(d)

summs = [sum([diagonals[d][i] for d in range(4)]) for i in range(len(diagonals[0]))]
print(summs)

#found a polynomial that fits the summs exactly. Via wolfram alpha
approximation = [4*(1 + n + 4*n*n) for n in range(1, layers+1)]
print(approximation)



#after playing around in wolfram alpha I arrived at this formula for a sum of the summs
x = layers
sums = 1+ (2*x*(13 + x*(15 + 8*x)))//3 
print(sums)
