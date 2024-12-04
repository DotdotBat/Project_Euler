import math


number_dictionary = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million"
}

def number_to_written_representation(n:int, something_above = False):

    if n in number_dictionary:
        result = number_dictionary[n]
        if n in [100, 1000, 1000000]:
            result = "one "+ result
        elif something_above:
            result = "and "+ result
        return result
    
    mil = 1000000
    if n>= mil:
        rem = n%mil
        result =number_to_written_representation(n//mil) + " million"
        if rem>0 and rem<100:
            result = result + " " + number_to_written_representation(rem, something_above=True)
        if rem>=100 and rem<1000:
            result = result + ", " + number_to_written_representation(rem, something_above=True)
        if rem>=100000:
            result = result + ", " + number_to_written_representation(rem, something_above=True)
        return result

    th = 1000
    if n>= th:
        rem = n%th
        result = number_to_written_representation(n//th) + " thousand"
        if rem>0 and rem<100:
            result = result + " " + number_to_written_representation(rem, something_above=True)
        if rem>=100:
            result = result + ", " + number_to_written_representation(rem, something_above=True)
        return result

    if n>= 100:
        rem = n%100
        result =  number_to_written_representation(n//100) + " hundred"
        if rem>0:
            result = result + " " + number_to_written_representation(rem, something_above=True)
        return result

    #its a two digit number that is not in the dictionary 
    # so its between 20 and 100 and the second digit isnt a zero so
    last_digit = n%10
    result =  number_to_written_representation(n-last_digit) + "-" + number_to_written_representation(last_digit)
    if something_above:
        result = "and " + result
    return result




# print(number_to_written_representation(100001))


def count_chars(s:str):
    #remove
    # s = s.replace(" ", "")#spaces
    # s = s.replace("-", "")#hyphens
    # s = s.replace(",", "")#commas
    return len(s)

summ = 0
for i in range(1, 1000+1):
    representation = number_to_written_representation(i)
    summ+= count_chars(representation)
print(summ)








import unittest

class TestNumberToWrittenRepresentation(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(number_to_written_representation(1), "one")

    def test_two_digit(self):
        self.assertEqual(number_to_written_representation(21), "twenty-one")
        self.assertEqual(number_to_written_representation(12), "twelve")

    def test_three_digit(self):
        self.assertEqual(number_to_written_representation(111), "one hundred and eleven")
        self.assertEqual(number_to_written_representation(101), "one hundred and one")
        self.assertEqual(number_to_written_representation(190), "one hundred and ninety")
        self.assertEqual(number_to_written_representation(191), "one hundred and ninety-one")
        self.assertEqual(number_to_written_representation(206), "two hundred and six")
        self.assertEqual(number_to_written_representation(342), "three hundred and forty-two")
        self.assertEqual(number_to_written_representation(115), "one hundred and fifteen")

    def test_thousand(self):
        self.assertEqual(number_to_written_representation(1002), "one thousand and two")
        self.assertEqual(number_to_written_representation(15726), "fifteen thousand, seven hundred and twenty-six")
        self.assertEqual(number_to_written_representation(1999), "one thousand, nine hundred and ninety-nine")

    def test_hundred_thousand(self):
        self.assertEqual(number_to_written_representation(276521), "two hundred and seventy-six thousand, five hundred and twenty-one")
        self.assertEqual(number_to_written_representation(100001), "one hundred thousand and one")
        self.assertEqual(number_to_written_representation(100100), "one hundred thousand, one hundred")
        self.assertEqual(number_to_written_representation(999999), "nine hundred and ninety-nine thousand, nine hundred and ninety-nine")

    def test_million(self):
        self.assertEqual(number_to_written_representation(1000001), "one million and one")
        self.assertEqual(number_to_written_representation(1234567), "one million, two hundred and thirty-four thousand, five hundred and sixty-seven")
        self.assertEqual(number_to_written_representation(10000000), "ten million")
        self.assertEqual(number_to_written_representation(123456789), "one hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine")

if __name__ == '__main__':
    unittest.main()


