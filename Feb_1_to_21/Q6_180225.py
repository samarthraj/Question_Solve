def check(n):
    sum = 0 
    ct = 0 
    numb = n
    final_check = n
    while numb > 0: 
        numb = numb // 10 
        ct += 1
    
    while n > 0: 
        last_digit = n % 10 
        n = n // 10  
        sum += last_digit**ct
    
    #print(ct, sum, final_check)
        
    if sum == final_check: 
        return True 
    return False


n = 71 
ans = check(n)
print(ans) 





