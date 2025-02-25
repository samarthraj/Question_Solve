def max_zero_switch(arr): 
    
    sum = 0
    max_sum = 0
    for i in range(0, len(arr)): 
        if arr[i] == 1: 
            sum += 1
            max_sum = max(max_sum, sum)
        else: 
            sum = 0
    
    return max_sum


arr = [1,0,1,1,1,0,1,0]
ans = max_zero_switch(arr) 
print(ans) 
