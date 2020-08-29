"""
https://www.hackerrank.com/challenges/happy-ladybugs/problem
"""

def happyLadybugs(b):
    #check if there are at least 2 of each color
    # ensure there is at least one space

    boardCount = {}
    for char in b:
        if char in boardCount:
            boardCount[char] += 1
        else:
            boardCount[char] = 1

    for k,v in boardCount.items():
        if k.isalpha() and boardCount[k] < 2:
            return 'NO'

    count = 0
    if '_' not in boardCount:
        for i in range(len(b) - 1):
            if b[i] == b[i+1]:
                count = 1
            elif b[i] != b[i+1] and count == 2:
                return 'NO'
            else:
                count = 2
        return 'YES'

    return 'YES'