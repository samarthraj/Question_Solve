
def solve(accounts):
    #i customer ; j bank account 
    rows_cust = len(accounts) 
    cols_bank = len(accounts[0]) 
    max_sum = 0
    for i in range(rows_cust): 
        sum = 0 
        for j in range(cols_bank): 
            sum += accounts[i][j] 
        max_sum = max(sum, max_sum) 
    
    return max_sum

accounts =  [[1,2,3],[3,2,1]]
ans = solve(accounts)
print(ans) 