import math
def maxProfit(prices):
    maxProfit = 0 
    minPrice = math.inf
    for price in prices:
        minPrice = min(price, minPrice)
        profit = price - minPrice
        maxProfit = max(profit, maxProfit)
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
