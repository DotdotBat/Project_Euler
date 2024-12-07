# The nth term of the sequence of triangle numbers is given by tn = 1/2 * n * (n + 1).
# The first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values, we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55, which is the 10th triangle number.
# If the word value is a triangle number, then we call the word a triangle word.
# Using a text file containing nearly two thousand common English words, how many are triangle words?


#the problem can be broken down into 4 parts
# text from file V
# array of words V
# word to score
# is a number a triangle number?


# I a similar thing was done in Names_Scores
file = open(file="attached_files/0042_words.txt", mode="r")
data = file.read()
words = data.split(",")
for i, name in enumerate(words):
    words[i] = name.strip('"')

import math
from reusable_functions import letter_value

def word_score(word:str):
    return sum([letter_value(l) for l in word])

scores = [word_score(word) for word in words]

def is_triangle(num:int):
    # 1/2 * n * (n+1) = num
    # n^2 + n = 2num
    n = math.isqrt(2*num)
    is_a_triangle = n*(n+1) == 2*num
    return is_a_triangle

count = sum(is_triangle(score) for score in scores)

print(count)