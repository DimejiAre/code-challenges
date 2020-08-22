"""
https://www.hackerrank.com/challenges/fair-rations/problem
"""

def fairRations(B):
    count = 0
    for i in range(len(B)):
        if (i == len(B)-1) and B[i] % 2 != 0:
            return 'NO'
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            count += 2

    return count