#best time to buy stock 
def stock_best(prices): 
    max_profit = 0 
    min_stock_price = prices[0] 
    for i in range(0, len(prices)): 
        if prices[i] - min_stock_price > max_profit: 
            max_profit = prices[i] - min_stock_price
        elif prices[i] < min_stock_price: 
            min_stock_price = prices[i] 
    
    return max_profit

prices = [7,1,5,3,6,4] 
ans = stock_best(prices) 
print(ans) 

