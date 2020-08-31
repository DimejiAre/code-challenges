"""
https://www.hackerrank.com/challenges/halloween-sale/problem
"""

def howManyGames(p, d, m, s):
    cash = s
    cost = p
    discount = d
    standard_price = m
    games_bought = 0
    
    if cost > cash:
        return games_bought

    while True:
        if cost > m:
            cash -= cost
            games_bought += 1
            cost -= discount
            if cost > cash or m > cash:
                break
            continue
        cost = standard_price
        cash -= cost
        games_bought += 1
        if cost > cash:
            break

    return games_bought