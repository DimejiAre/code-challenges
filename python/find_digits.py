"""
https://www.hackerrank.com/challenges/find-digits/problem
"""

def findDigits(n):
    non_zero_digits = [int(char) for char in str(n) if char != '0']

    divisors = [digit for digit in non_zero_digits if n % digit == 0]

    return len(divisors)