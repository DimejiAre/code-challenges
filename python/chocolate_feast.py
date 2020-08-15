"""
https://www.hackerrank.com/challenges/chocolate-feast/problem
"""

def chocolateFeast(n, c, m):
    cash = n
    cost = c

    chocolates_eaten =  cash // cost
    wrappers = chocolates_eaten

    while wrappers >= m:
        new_wrappers = wrappers // m
        chocolates_eaten += new_wrappers

        remainder_wrappers = wrappers % m
        wrappers = new_wrappers + remainder_wrappers

    return chocolates_eaten


