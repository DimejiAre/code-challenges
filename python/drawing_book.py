"""
https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""
import math

def pageCount(n, p):
    front_turns = math.ceil((p-1)/2)

    if n % 2 == 0:
        back_turns = math.ceil((n-p)/2)
    else:
        back_turns = math.floor((n-p)/2)

    return min(front_turns, back_turns)


print(pageCount(10, 4))