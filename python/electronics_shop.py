"""
https://www.hackerrank.com/challenges/electronics-shop/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""

def getMoneySpent(keyboards, drives, b):
    money_spent = 0
    budget = b
    for i in keyboards:
        for j in drives:
            sum = i + j
            if money_spent < sum <= budget:
                money_spent = sum
    if money_spent == 0:
        return -1
    else:
        return money_spent

print(getMoneySpent([3,1], [5,2,8], 10))