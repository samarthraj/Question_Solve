#Given Some Prices 
#7, 10, 1, 3, 6, 9, 2 
#stock prices 
#buy and sell it - only one time 
#how much max profit can you make 

def stock_prices(prices): 

    max_profit = 0
    min_num = prices[0]
        
    for i in range(0,len(prices)): 
        if prices[i] - min_num > max_profit:
            max_profit = prices[i] - min_num
        elif prices[i] < min_num: 
            min_num = prices[i]
    return max_profit

arr = [7,10,1,3,6,9,2] 
ans = stock_prices(arr)
print(ans) 
