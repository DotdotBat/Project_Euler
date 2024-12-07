"""
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list 
to obtain a name score.
What is the total of all the name scores in the file?
"""

file = open(file="attached_files/0022_names.txt", mode="r")
data = file.read()
names = data.split(",")
for i, name in enumerate(names):
    names[i] = name.strip('"')
names.sort()



from reusable_functions import letter_value


def name_value(name):
    return sum([letter_value(letter) for letter in name])

score = 0
for i, name in enumerate(names):
    score+= (i+1) * name_value(name)
print(score)