"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""

def extraLongFactorials(n):
    answer = n
    while n > 1:
        answer *= (n - 1)
        n -= 1
    
    print(answer)