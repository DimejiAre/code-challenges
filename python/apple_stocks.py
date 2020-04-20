#Greedy Algorithm

"""
Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
"""

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = None

    if len(stock_prices) > 2:
        for i in range(1, len(stock_prices)):
            current_price = stock_prices[i]
            
            profit = current_price - min_price
            
            max_profit = max(profit, max_profit) if max_profit else profit
            
            min_price = min(current_price, min_price)
            
            
        return max_profit
        
    else:
        raise Exception()


print(get_max_profit([10, 7, 5, 8, 11, 9]))