"""
https://www.hackerrank.com/challenges/save-the-prisoner/problem
"""

def saveThePrisoner(n, m, s):
    position = (m + (s - 1)) % n
    actual_position = position or n
    
    return actual_position