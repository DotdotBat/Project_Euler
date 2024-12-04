# The decimal number 585 is palindromic.
# In both bases 10 and 2.
# Find the sum of all numbers.
# Less than one million.
# Which are palindromic in both base 10 and base 2.
# The palindromic number may not include leading zeros

import unittest

def is_base_10_palindrome(num):
    return str(num) == str(num)[::-1]

def is_base_2_palindrome(num):
    binary_representation = bin(num)[2:]
    return binary_representation == binary_representation[::-1]

class TestPalindromeFunctions(unittest.TestCase):

    def test_is_base_10_palindrome(self):
        self.assertTrue(is_base_10_palindrome(121))
        self.assertTrue(is_base_10_palindrome(12321))
        self.assertFalse(is_base_10_palindrome(123))
        self.assertFalse(is_base_10_palindrome(12345))

    def test_is_base_2_palindrome(self):
        self.assertTrue(is_base_2_palindrome(5))  # 101 in binary
        self.assertTrue(is_base_2_palindrome(9))  # 1001 in binary
        self.assertFalse(is_base_2_palindrome(10))  # 1010 in binary
        self.assertFalse(is_base_2_palindrome(12))  # 1100 in binary

# if __name__ == '__main__':
#     unittest.main()

double_palindromes = []

for i in range(1, 1000000, 2):
    if is_base_10_palindrome(i) and is_base_2_palindrome(i):
        double_palindromes.append(i)

print(double_palindromes)
print(len(double_palindromes))
print(sum(double_palindromes))
